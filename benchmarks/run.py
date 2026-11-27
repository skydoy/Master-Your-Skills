"""With/without-skill benchmark. Usage: python3 benchmarks/run.py [runs] [model]

Each task runs in a fresh copy of tasks/<task>/repo, once with no skill and once with the
task's skill appended to the system prompt. Plugins and hooks are disabled in both arms so
the only difference is the skill. Results go to benchmarks/results/<date>.jsonl.
"""
import concurrent.futures as cf
import datetime
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent
SKILLS = ROOT.parent / "skills"
TASKS = {  # task -> skill under test
    "fix-duration": "debug",
    "json-flag": "lean",
    "group-by": "lean",
    "cart-discount": "tdd",
    "review-diff": "check-code",
}
CLEAN = json.dumps({"disableAllHooks": True, "enabledPlugins": {
    "ponytail@synced": False, "agent-skills@synced": False, "master-your-skills@master-your-skills": False}})


def claude(prompt, cwd, model, system=None):
    cmd = ["claude", "-p", prompt, "--model", model, "--output-format", "json",
           "--settings", CLEAN, "--disable-slash-commands",
           "--allowedTools", "Read,Edit,Write,Glob,Grep,Bash"]
    if system:
        cmd += ["--append-system-prompt", system]
    out = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=900)
    try:
        return json.loads(out.stdout)
    except json.JSONDecodeError:
        return {"is_error": True, "result": (out.stdout + out.stderr)[-500:]}


def skill_text(name):
    body = (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
    return re.sub(r"^---.*?---\s*", "", body, flags=re.S)  # drop frontmatter


def diff_lines(cwd):
    subprocess.run(["git", "add", "-A"], cwd=cwd, capture_output=True)
    out = subprocess.run(["git", "diff", "--cached", "--numstat"], cwd=cwd, capture_output=True, text=True).stdout
    code = tests = 0
    for line in out.splitlines():
        add, rem, path = line.split("\t")
        n = int(add) + int(rem) if add != "-" else 0
        if pathlib.Path(path).name.startswith("test_"):
            tests += n
        elif path.endswith(".py"):
            code += n
    return code, tests


def hidden_score(task, cwd):
    hidden = ROOT / "tasks" / task / "hidden"
    if not hidden.exists():
        return None
    for f in hidden.iterdir():
        shutil.copy(f, cwd / f"zz_{f.name}")
    out = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "zz_test_hidden.py"],
                         cwd=cwd, capture_output=True, text=True).stdout
    passed = int(m.group(1)) if (m := re.search(r"(\d+) passed", out)) else 0
    failed = int(m.group(1)) if (m := re.search(r"(\d+) (failed|error)", out)) else 0
    total = passed + failed
    return passed / total if total else 0.0


def review_score(cwd, model):
    review = cwd / "REVIEW.md"
    if not review.exists():
        return 0.0, 0
    rubric = (ROOT / "tasks" / "review-diff" / "rubric.txt").read_text()
    ask = (f"{rubric}\n\nReview to grade:\n<review>\n{review.read_text()[:12000]}\n</review>\n"
           'Reply with only JSON: {"A":bool,"B":bool,"C":bool,"false_positives":int}')
    res = claude(ask, cwd, model)
    m = re.search(r"\{.*\}", res.get("result", ""), re.S)
    g = json.loads(m.group(0)) if m else {}
    return sum(bool(g.get(k)) for k in "ABC") / 3, int(g.get("false_positives", 0))


def run_one(task, arm, i, model):
    with tempfile.TemporaryDirectory() as tmp:
        cwd = pathlib.Path(tmp) / "repo"
        shutil.copytree(ROOT / "tasks" / task / "repo", cwd)
        for c in (["git", "init", "-q"], ["git", "add", "-A"],
                  ["git", "-c", "user.name=b", "-c", "user.email=b@b", "commit", "-qm", "base"]):
            subprocess.run(c, cwd=cwd, capture_output=True)
        prompt = (ROOT / "tasks" / task / "prompt.txt").read_text().strip()
        res = claude(prompt, cwd, model, skill_text(TASKS[task]) if arm == "skill" else None)
        code, tests = diff_lines(cwd)
        row = {"task": task, "skill": TASKS[task], "arm": arm, "run": i, "model": model,
               "error": bool(res.get("is_error")), "cost_usd": res.get("total_cost_usd"),
               "output_tokens": res.get("usage", {}).get("output_tokens"),
               "turns": res.get("num_turns"), "seconds": (res.get("duration_ms") or 0) / 1000,
               "code_lines": code, "test_lines": tests}
        if task == "review-diff":
            row["correct"], row["false_positives"] = review_score(cwd, model)
        else:
            row["correct"] = hidden_score(task, cwd)
        return row


def main():
    runs = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    model = sys.argv[2] if len(sys.argv) > 2 else "sonnet"
    out = ROOT / "results" / f"{datetime.date.today()}.jsonl"
    out.parent.mkdir(exist_ok=True)
    jobs = [(t, a, i) for t in TASKS for a in ("none", "skill") for i in range(runs)]
    with cf.ThreadPoolExecutor(int(os.environ.get("BENCH_WORKERS", 6))) as pool, out.open("a") as f:
        for row in pool.map(lambda j: run_one(*j, model), jobs):
            f.write(json.dumps(row) + "\n")
            f.flush()
            print(row["task"], row["arm"], row["correct"], row["code_lines"], row["output_tokens"], flush=True)


if __name__ == "__main__":
    main()

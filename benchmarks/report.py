"""Summarise benchmark results into docs/img/benchmark.png and the gains table in GLOSSARY.md.
Usage: python3 benchmarks/report.py   (needs node + playwright for the PNG)"""
import collections
import glob
import html
import json
import pathlib
import statistics as st
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
rows = [json.loads(l) for f in sorted(glob.glob(str(ROOT / "benchmarks/results/*.jsonl"))) for l in open(f)]
rows = [r for r in rows if not r["error"]]
by = collections.defaultdict(lambda: collections.defaultdict(list))
for r in rows:
    by[(r["skill"], r["task"])][r["arm"]].append(r)


def summary(rs):
    return {"n": len(rs), "correct": st.mean(r["correct"] or 0 for r in rs),
            "tested": sum(r["test_lines"] > 0 for r in rs) / len(rs),
            "tokens": st.median(r["output_tokens"] or 0 for r in rs),
            "cost": st.median(r["cost_usd"] or 0 for r in rs)}


stats = {s: {a: summary(rs) for a, rs in arms.items()} for s, arms in by.items() if len(arms) == 2}


def pct(x):
    return f"{x * 100:.0f}%"


def gain_line(s):
    n, k = stats[s]["none"], stats[s]["skill"]
    tok = k["tokens"] / n["tokens"] - 1 if n["tokens"] else 0
    return (f"correct {pct(n['correct'])} → {pct(k['correct'])} · tests written {pct(n['tested'])} → "
            f"{pct(k['tested'])} · output tokens {tok:+.0%}")


# Gains table for GLOSSARY.md (between markers)
table = ["| Skill | Task | Runs | Correct (without → with) | Wrote a test | Output tokens |", "|---|---|---|---|---|---|"]
for s in sorted(stats):
    n, k = stats[s]["none"], stats[s]["skill"]
    tok = k["tokens"] / n["tokens"] - 1 if n["tokens"] else 0
    table.append(f"| `{s[0]}` | {s[1]} | {n['n']}+{k['n']} | {pct(n['correct'])} → {pct(k['correct'])} | "
                 f"{pct(n['tested'])} → {pct(k['tested'])} | {tok:+.0%} |")
gl = ROOT / "GLOSSARY.md"
text = gl.read_text()
a, b = "<!-- gains:start -->", "<!-- gains:end -->"
gl.write_text(text[:text.index(a) + len(a)] + "\n" + "\n".join(table) + "\n" + text[text.index(b):])

# Chart card in the brand style
models = sorted({r["model"] for r in rows})
bars = []
for s in sorted(stats):
    n, k = stats[s]["none"], stats[s]["skill"]
    bars.append(f"""<div class="row"><div class="name">{html.escape(s[0])}<small>{html.escape(s[1])}</small></div><div class="cols">
<div class="m"><span>tests written</span><i style="width:{n['tested']*68:.0f}%" class="off"></i><i style="width:{k['tested']*68:.0f}%" class="on"></i><b>{pct(n['tested'])} → {pct(k['tested'])}</b></div>
<div class="m"><span>correct</span><i style="width:{n['correct']*68:.0f}%" class="off"></i><i style="width:{k['correct']*68:.0f}%" class="on"></i><b>{pct(n['correct'])} → {pct(k['correct'])}</b></div>
</div></div>""")
page = f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=JetBrains+Mono:wght@400;600&display=block" rel="stylesheet">
<style>html,body{{margin:0;background:#0B1020;color:#EEF1FF;font-family:'Space Grotesk',sans-serif;width:1600px}}
.card{{padding:70px 90px}}.tag{{font-family:'JetBrains Mono';letter-spacing:.25em;color:#C6F432;font-size:20px}}
h1{{font-size:62px;margin:18px 0 40px;letter-spacing:-.02em}}h1 span{{color:#C6F432}}
.row{{display:flex;align-items:center;border-top:1px solid #232C4A;padding:22px 0}}.name{{width:260px;font-family:'JetBrains Mono';font-size:26px}}.name small{{display:block;font-size:15px;color:#8A93B8;margin-top:4px}}
.cols{{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:40px}}.m{{position:relative}}
.m span{{display:block;font-size:16px;color:#8A93B8;font-family:'JetBrains Mono';margin-bottom:8px}}
.m i{{display:block;height:14px;border-radius:7px;margin:4px 0}}.off{{background:#2A3352}}.on{{background:#C6F432}}
.m b{{position:absolute;right:0;top:26px;font-family:'JetBrains Mono';font-size:20px}}
.foot{{margin-top:34px;color:#8A93B8;font-family:'JetBrains Mono';font-size:18px}}.k{{display:inline-block;width:14px;height:14px;border-radius:3px;margin:0 8px 0 24px;vertical-align:-1px}}</style></head>
<body><div class="card"><div class="tag">● BENCHMARK · {html.escape(", ".join(models)).upper()} · {len(rows)} RUNS</div>
<h1>Same task, same model. <span>With vs without the skill.</span></h1>{''.join(bars)}
<div class="foot"><i class="k" style="background:#2A3352"></i>without skill<i class="k" style="background:#C6F432"></i>with skill · hidden tests or a fixed rubric decide "correct" · source: benchmarks/results/</div></div></body></html>"""
out = ROOT / "docs/img"
out.mkdir(parents=True, exist_ok=True)
(out / "benchmark.html").write_text(page)
subprocess.run(["node", str(ROOT / "scripts/render.js"), str(out / "benchmark.html"), str(out / "benchmark.png"),
                "1600", str(400 + 105 * len(stats))], check=True)
(out / "benchmark.html").unlink()
for s in sorted(stats):
    print(*s, gain_line(s))

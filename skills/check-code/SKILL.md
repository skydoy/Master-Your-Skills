---
name: check-code
description: Review a change for bugs, security, load, missing tests, speed and needless code, with ranked findings in plain words. Use when the user says "check this", "review my PR", "review the last commit", "is this ready to merge", "is this over-engineered", or before merging any change.
---

Judge a change like the person paged when it breaks; report only what you can prove.

## Do this

1. **Pin the target.** What the user names (PR, branch, commit, files); else uncommitted changes, else the last commit. Before running anything, check the tree is clean and on that ref, or your evidence describes other code.
2. **Learn the intent.** Read the issue, spec or PR text, to flag what is missing and what was added unasked.
3. **Read beyond the diff.** Open callers of changed functions (grep all of them when a signature changes), what they call, and their tests. Find the expected load and say what you assumed.
4. **Test the tests.** Flip one condition the change adds, run the tests, restore from a copy. Still green means a test is missing; name the case.
5. **Look, in this order:**
   1. Correct: wrong result, crash, empty/zero/last item, time zones, a broken caller, a fix in one caller while shared code stays wrong.
   2. Safe: unchecked input, injection, secrets in code or logs, missing auth, swallowed errors, data loss.
   3. Holds under load: check-then-write races, a query per item, lists that only grow, per-process state that must be shared.
   4. Tested: parsers, money, security, writes and bug fixes that no test would catch breaking.
   5. Spec and conventions: missing or unrequested behavior, the repo's documented rules.
   6. Lean: unused code, a reinvented helper the repo already ships (give its path), a new package for a handful of lines, an abstraction with a single caller.
6. **Prove each finding.** Give the exact input and the bad outcome it produces; if you can't, delete the finding. Re-read the code to be sure. Label issues that predate this change "pre-existing".
7. **Propose the smallest fix,** ideally one that deletes code.
8. **High stakes** (auth, payments, migrations, public API): ask a fresh subagent to break it. Give it only the diff and the requirement, not your conclusions, so it can't just agree.

## Report

Plain short sentences. Open with `What this change does:` in two sentences. Then numbered findings across three groups, skipping empty ones: **Must fix** (bug, security, data loss, fails at expected load), **Should fix** (untested risk, real slowness, needless code), **Nice to have**. Each: title and `file:line`, the concrete case, the fix, the cost of skipping.

Finish with `Verdict: ship it` or `Verdict: fix 1 and 3 first`, then `Not checked:` listing anything important you couldn't confirm. A clean result is fine; list what you looked at.

This skill reports; it changes no code unless the user asks.

## Done when

- Callers and tests were read, not only the diff.
- The mutation check ran.
- Every finding has a concrete failing case and a fix.

## Traps

- Style taste and vague worries; they bury the real bug.
- Trusting green CI without checking what tests assert.
- A `shortcut:` marker that states its limit is a deliberate choice; report it only if real usage is already past that limit.

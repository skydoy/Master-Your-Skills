---
name: audit
description: Read-only health check of a repo or folder: defects, security gaps, scaling limits, untested risky logic, slow spots, dead weight, and a ledger of `shortcut:` debt markers. Use for "audit this repo", "what can I delete", "list the shortcuts", "tech debt".
---

Audit like the new owner who gets paged when it breaks. Report only; change nothing.

## Do this

1. **Set scope and load.** Audit what the user named, else the whole repo. Write down the real usage level (a solo script or a busy service) and rate every scaling issue against that number.
2. **Map before judging.** Read dependencies, entry points, tests and config. Trace each main flow from input to storage to output; read money, auth, data writes and shared state in full.
3. **Hunt, in this order:**
   - Wrong results: empty input, zero, the final element, rounding, time zones; a caller that misreads what it gets back; the same rule implemented twice, differently.
   - Safety: injection, secrets in code, unchecked input, swallowed errors, writes without a transaction.
   - Load: check-then-write races, queries in loops, caches that only grow, per-process state that must be shared.
   - Untested risk: a branch, parser, money or security path no test would catch breaking.
   - Speed: big slowdowns only.
   - Excess: dead code, unused flags, forwarding wrappers, duplicate helpers, a dependency the standard library replaces.
4. **Back every finding** with the input or situation that breaks it; without one, drop it. Before declaring code dead, search everywhere it could be referenced: tests, config, dynamic string lookups.
5. **Build the debt ledger:** `git grep -nE '(#|//|/\*|--) ?shortcut:'` (or the user's marker word). Per hit: file:line, what was simplified, its limit, its upgrade trigger. Flag rows with no trigger as `no-trigger`, since nobody will ever revisit them. A documented shortcut counts as a choice, and becomes a finding only once real usage has passed its stated limit.
6. **Propose the smallest fix**, preferring ones that delete code.

## Report

- `What this repo does:` two or three sentences plus the assumed load.
- One running number across all groups, so the user can reply "do 2 and 5". Cap at 20 and say how many minor items were omitted:
  - **Must fix**: wrong results, security, data loss, fails at expected load.
  - **Should fix**: untested risk, real slowness, duplication, code that should not exist.
  - **Nice to have**: small wins.
  Each: title, `path:lines`, then one line each for what the code does, the problem with its case, the fix, the cost of skipping it.
- `Debt ledger:` rows grouped by file, ending `<N> markers, <M> without a trigger.`
- `Verdict:` healthy, or the first thing to fix. Add `Lean: about -<N> lines, -<M> dependencies` when excess was found.
- `Not checked:` what you did not read or run.

## Stop and ask when

- The user wants fixes applied: that is separate work.

## Done when

- Every finding has a location and a concrete failing case.
- The ledger lists every marker, with `no-trigger` tags.
- Load assumption and `Not checked:` are stated.
- No file was changed.

## Traps

- Style opinions or vague worries reported as findings.
- Calling code dead after a grep that missed dynamic or config references.
- Reading file by file and missing a bug that lives between two files.

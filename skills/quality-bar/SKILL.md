---
name: quality-bar
description: Write the project's quality bar once in CONSTRAINTS.md with real commands and numbers, then refuse any change that quietly lowers it (skipped tests, ts-ignore, eslint-disable, removed asserts, lowered thresholds, stubs). Use for "set our standards", "add quality gates", "stop the agent cheating to green".
---

Agents write more than anyone reads, so the bar must live in checks that run, and lowering it must be loud.

## Do this

1. **Read before asking:** stack, test runner, linters, type checker, CI, current coverage. If `CONSTRAINTS.md` exists, follow it unless the user wants it changed.
2. **Ask at most four questions, each with a default**, so "don't know" still works:
   - Which dimensions beyond the floor? (default: changed-line coverage, security)
   - Block or warn? (default: block the floor, warn on the rest for two weeks)
   - Targets, or measure today and hold? (default: measure and hold)
   - Slowest check you'll wait for? (default: 90 s)
   No live user (CI, autonomous run)? Apply the floor only.
3. **Write `CONSTRAINTS.md`** at the root:
   - **Floor**, always on: no new suppression comments, skipped or deleted tests, removed assertions, stubs or empty `catch`, secrets in source; this file is never loosened to make a change pass.
   - **Enforced**: per dimension the rule, number, reason, exact command, and stage. A number without a command is a wish; leave it out.
   - **Measured**: today's value and a direction (`must not fall`). A target failed today teaches people to ignore red.
   - **Exceptions**: rule, path, reason, owner, expiry (default 90 days).
4. **Place checks by cost:** seconds-fast after each edit, tests and coverage at task end, slow scans in CI. Slow checks in the edit loop get switched off.
5. **Prove each enforced row:** it fails on a planted violation, passes on clean code, and fails (not passes) when the scanner itself errors.
6. **Point agents at it:** add `Read CONSTRAINTS.md before coding; never weaken it to pass.` to the agent rules file (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`...).
7. **Guard every diff** against the merge base, untracked files included. Flag: a threshold loosened or rule removed, a new skip or deleted test, an assertion removed from a surviving test, a new suppression, a new stub, a new exception row. Fix the code instead; if truly needed, add a dated exception and say so.
8. **Ratchet:** when a measured value improves, record the new value.

Read `reference.md` here for default numbers, a tool per dimension, and grep patterns for step 7.

## Stop and ask when

- Passing would need any loosening move from step 7.
- A dimension has no tool that runs here: drop it, don't fake it.

## Done when

- `CONSTRAINTS.md` exists; every number has a reason and a command.
- The floor passes on current code without edits.
- Each enforced command failed on a violation and passed on clean code.
- At least one check is external to the project's own tests (type checker, vulnerability scanner).
- The agent instruction file points to it.

## Traps

- Constraints edited in the same commit as the failing code.
- `istanbul ignore` or `nosemgrep` slipped in: they hide exactly what you measure.
- Scanners that exit 0 on findings; parse output and fail on severity.
- Printing a found secret; report rule and location only.

---
name: ship
description: Get a change to production safely and keep it healthy. Use when deploying or launching, asking "is this ready to ship?", setting up CI gates, planning a staged rollout or rollback, adding logs/metrics/alerts, or removing an old API, feature or database column.
---

Every release is gated, watched, and undoable faster than it can hurt anyone.

## Do this

1. **Name how you would undo it.** The cheapest undo that works decides everything after:
   - *Flag off* (seconds): new behavior behind a flag, old path intact.
   - *Redeploy previous build* (minutes): code-only change, no data or contract change.
   - *Data or contract change* (hours, maybe never): migrations, deletes, public API changes, sent emails. A one-way door; see step 5.
2. **Pass the gates in CI, not by hand.** Lint, types, tests, build and dependency audit run on every PR and block merge. Fix a red gate at the cause, never by skipping, disabling or lowering it. Setting up or repairing CI: read `reference.md` § CI.
3. **Decide what "working" means before deploying.** Write 2–4 questions on-call will ask ("how many checkouts fail, and why?"). Make a log, metric or alert answer each, then trigger it once and see it arrive. Details: `reference.md` § Telemetry.
4. **Roll out in steps that match the risk.** Small or flagged: deploy, smoke-test the main flow, watch for an hour. Risky and user-facing: staging, production with flag off, team, a small slice of users, wider. At each step compare to baseline and advance, hold or roll back by the thresholds in `reference.md` § Rollout, written down before you start so the call isn't made under pressure.
5. **Change shared shapes in phases.** For a column, API field or event format: add the new shape beside the old, write both, backfill in batches, move readers, and only then remove the old one in a separate later deploy. Every phase must work with old and new code running at once, and ship with a tested way back. Example: `reference.md` § Phased change.
6. **Remove what you replaced.** Once measured usage of the old path is zero, delete its code, flag, config, tests and docs.

No users yet, or an internal tool: skip steps 4–6. First launch or big release: also `reference.md` § Pre-launch sweep.

## Stop and ask when

- The undo is "data or contract change" and nobody has approved the one-way step.
- The error budget is spent: ship only fixes until it recovers.
- A rollout threshold hits "roll back" and someone wants to push on.
- Removing an API or feature that still has usage.

## Done when

- The undo path is written down and checked (flag toggles, previous build deploys, migration has a down step).
- CI gates all pass and block merge on failure.
- Each on-call question has a signal seen firing once.
- Rollout hit 100% inside the advance thresholds, or was rolled back on purpose.
- Paths and flags this change made dead are gone or have a dated removal ticket.

## Traps

- Renaming or dropping a column in the same deploy that stops using it.
- Average latency instead of p95/p99; user IDs as metric labels.
- Alerts on CPU while user-facing errors go unwatched.
- Late-Friday deploys nobody watches.

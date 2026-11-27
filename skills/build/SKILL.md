---
name: build
description: Implement a plan or ticket in small working slices, each one tested, verified and committed before the next. Use when the user says "implement this", "build the plan", "do task 3", "work through the tickets", or a change will touch more than one file.
---

Turn a plan into working code one thin slice at a time, so the project is never broken for long and any slice can be reverted alone.

## Do this

1. **Find the commands.** Get the repo's own test, typecheck and build commands from README, CI config and build files. Prefer checked-in wrappers (`./gradlew`, `make test`); never assume `npm test`.
2. **Open a progress file.** Create a git-ignored `.progress.md`: the plan's path on line one, one line per task. If it exists, trust it and `git log` over your memory: tasks marked done are done. This lets work survive a context reset.
3. **Cut the next slice.** One behavior, end to end (data + logic + interface), small enough to finish in under ~100 lines. Do the riskiest unknown first, so a dead end shows up early.
4. **Implement it test-first** with the `tdd` skill where there is logic. Simplest version that works.
5. **Verify.** Run the focused tests, then typecheck. Read the output. Unexpected failure: stop and use the `debug` skill; never stack a slice on a red one.
6. **Commit the slice** with a message that says what behavior now works. Add the progress line in the same step: `Task N: done (abc123..def456, <test command> passed)`.
7. **Record rulings.** Plan wrong or silent? Pick the smallest choice that meets the spec, continue, and log it: `Ruling: <decision> - <why> - <cost if wrong>`. A deviation without a ruling is a decision hidden from the user.
8. **Park side findings.** Something outside the slice needs fixing? Add it to a "Noticed, not touched" list; mixed changes hide bugs and block clean reverts.
9. **Finish.** Run the full suite and build once. Then run the `check-code` skill on the whole branch and fix what it marks must-fix, each fix with a test. Report the rulings and the noticed list to the user.

Small task (one file, one behavior): skip the progress file and rulings; keep steps 4-6.

## Stop and ask when

- A step is destructive or hard to undo: data migration, deleting user data, force-push, publishing.
- It touches auth, secrets, payments or permissions in a way the plan doesn't spell out.
- The plan is so broken that every path forward is a guess.
- You are on the main branch and nobody said that is fine.

Anything else: decide, log the ruling, continue. Don't ask "shall I go on?" between tasks.

## Done when

- Every task has a done line with commits and a passing test run.
- Full test suite, typecheck and build pass on the final commit.
- No uncommitted changes remain.
- The user has the list of rulings and noticed-but-untouched items.

## Traps

- Writing several slices before running anything; then nobody knows which one broke it.
- Unfinished behavior reaching users. Hide it behind a flag that defaults to off.
- Re-running a green command on unchanged code "to be sure".

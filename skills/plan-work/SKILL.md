---
name: plan-work
description: Break an approved spec or clear request into ordered, vertical-slice tasks, each with acceptance checks, a verify command and its blockers. Use when the user says "plan this", "break it down", "make tickets", "task list", or when work is too big to start in one go.
---

Cut the work into thin end-to-end slices that each leave the system working and can be checked alone.

## Do this

1. **Read the spec and the code it touches.** Note patterns and the test and build commands. No code yet.
2. **Check for an open plan.** If a plan file for other work still has unchecked tasks, stop and ask.
3. **Find prep work.** If one small refactor makes the feature easy, make it task 1.
4. **Slice vertically.** Each task delivers one behaviour a user or caller can see, through every layer it needs (data, logic, interface, test). "Users can log in" is a slice; "build all endpoints" is not.
5. **Size each task.** It fits one focused session, touches about five files or fewer, and has at most three acceptance checks. An "and" in the title means two tasks.
6. **Order by blockers, risk first.** Each task names the tasks that must finish before it. Put the most uncertain slice early: it fails cheaply. Mark tasks with no shared files as safe to run in parallel.
7. **Name the hand-offs.** When a task produces something later tasks use, write its name and shape (function signature, endpoint, table) so both sides agree.
8. **Add a checkpoint** every 3 tasks: full tests, build, one end-to-end run.
9. **Self-check:** every spec behaviour and "Done when" line maps to a task; names match across tasks; no task says "handle edge cases" without naming them.
10. **Save** to `docs/plans/<name>.md` or the project's tracker (each issue names its parent by title and link), and ask for approval. Build starts after a yes.

## Task format

```
### T<n>: <behaviour, verb first>
Blocked by: <T#s or none>   Parallel: <yes/no>
Delivers:   <what works afterwards, from the user's side>
Accept:     - <testable check> (max 3)
Verify:     <exact command and the result that means pass>
Produces:   <names/shapes later tasks rely on, if any>
```

## Wide renames and type changes

When one mechanical change breaks callers everywhere, vertical slices cannot stay green. Plan it as expand, migrate, contract: add the new form beside the old, move callers over in batches (one task each), then delete the old form once nothing uses it.

## Small work

Three steps or fewer: write them as a checklist in the reply, each with its verify step, and skip the file.

## Stop and ask when

- The spec is missing, unapproved, or contradicts the code.
- A task needs a schema change, new dependency or data migration the spec did not mention.

## Done when

- Every spec requirement points to a task.
- Every task has blockers, checks and a runnable verify command.
- No task is larger than the size rule.
- The user approved the plan.

## Traps

- Layer-by-layer tasks: nothing works until the last one.
- Plans that contain the full code. Decide names, values and tests; let the builder write bodies.
- Setup or docs as separate tasks: fold them into the slice needing them.

---
name: parallel
description: Split work across parallel subagents and merge the results safely. Use when the user says "run these in parallel", "fan out", "use subagents", "spin up a team", or when a task has several independent parts (separate bugs, modules, files, questions) that could run at the same time.
---

Run independent parts of a task at once with subagents, then merge into one checked result.

## Go / no-go

Fan out only if all three are yes; otherwise work inline.

1. **Independent?** Each part can finish without another's result. If fixing one may fix another, they are one part.
2. **No shared write surface?** No two parts edit the same file, table, branch, or running service. Read-only parts always pass.
3. **Worth the cold start?** Each agent knows nothing and re-reads the code first, at a cost of thousands of tokens. A part you could finish in a few tool calls is cheaper inline. Usual range: 2-5 agents.

## Do this

1. **Map ownership.** One line per part: what it may change. Any overlap: merge those parts or run them in order.
2. **Write one brief per agent** (template below). Paste facts (error text, paths, interfaces to keep); the agent never saw this chat.
3. **Isolate writers.** Each agent that edits gets its own git worktree and branch. Readers (review, audit, research) stay in the main checkout and must not edit.
4. **Dispatch all agents in one message.** Calls in separate messages run one after another.
5. **No agent spawns agents.** Say so in every brief; nested agents multiply cost and hide work from the merge.
6. **Merge once, yourself.** Read every report, merge branches one at a time, resolve conflicts, then run the full tests and build on the merged result. Green branches can still clash.
7. **Review (optional, for code that ships).** One fresh reviewer per branch, two passes: first "does it do exactly what the brief asked, nothing missing or extra?", then "is it correct, simple, tested?". Close spec gaps before quality notes.

```
Goal: <one sentence; what done looks like>
Inputs: <exact paths, error output, commit, URLs>
May change: <paths>    Must not touch: <paths>
Constraints: <keep API X; no new deps; do not spawn agents>
Return: <status, files changed, test result, open risks>
Limit: at most <N> words.
```

The word limit keeps reports from crowding your context.

Small task with only read-only parts: skip steps 1, 3, and 7.

Ready teams for review, audit, and research: read `reference.md` when the user asks for one.

## Stop and ask when

- The merge needs a choice the briefs did not cover (two agents picked opposite designs).
- A part needs a destructive or shared action: migration, deploy, force push.

## Done when

- [ ] Every part passed the go/no-go test before dispatch.
- [ ] All agents went out in one message; writers each had a worktree.
- [ ] Conflicts were resolved by reading both sides.
- [ ] Full tests and build pass on the merged result.
- [ ] The answer lists what each agent did and what is open.

## Traps

- A brief like "fix the tests" with no file names: the agent wanders.
- Believing a report's "all tests pass" instead of running them after the merge.

---
name: spec
description: Write a short spec before building new or unclear work, and get it approved before any code. Use for a new feature, project or significant change, a vague requirement, or when the user says "write a spec", "PRD", "requirements", "scope this", "what exactly are we building".
---

Pin down what gets built and how anyone will know it works, before code makes the choices for you.

## Do this

1. **Read first.** Check the code, docs and decision records in the area. Use the project's own terms. If a spec format or folder already exists, use it.
2. **Check the size.** If the request holds parts that could ship and be tested separately (say, accounts and billing), list them with one line each and which depends on which, and get that map approved. Then write one spec per part, in dependency order.
3. **List your assumptions** as numbered lines (stack, users, data, limits), worded so "yes" accepts them all. Ask only what code and conversation cannot answer, in one round.
4. **Turn vague words into checks.** "Fast" becomes "search returns in under 300 ms for 10k rows". "Easy" becomes a step count. If no number is known, propose one and mark it.
5. **Write the spec** with the template, in `docs/specs/<name>.md` unless the project says otherwise. Keep it to one screen for a normal feature.
6. **Self-check:** every criterion is testable, every goal has a criterion, nothing in "Not doing" sneaks back into the behaviour list.
7. **Hand it over:** summarise in three lines, list open questions, ask for approval, and end your turn. Planning and code start only after a yes.

## Template

```
# <Feature> spec
Problem:   <who hurts, how, in their words>
Outcome:   <what changes for them when this ships>
Behaviour: <numbered: "When <actor> does X, Y happens", incl. errors and empty states>
Done when: <measurable checks, each one testable>
Test at:   <the highest public seam that proves the behaviour; reuse existing test style>
Limits:    <stack, performance, security, compatibility it must respect>
Ask first: <changes needing a human yes: schema, new deps, data deletion>
Not doing: <deferred ideas, one line each with why>
Open:      <unresolved questions>
```

Leave out file paths and code: they go stale before the work lands. A data shape or state table that a prototype settled may go in, marked as such.

## Small work

A change under an hour with clear behaviour needs no file: state Outcome, Done when and Not doing in the reply and continue.

## Stop and ask when

- The goal or the users are unknown and no suggestion fits.
- The request conflicts with existing behaviour or a recorded decision.

## Done when

- The spec is saved and fits the template.
- Every "Done when" line could be turned into a test.
- "Not doing" has at least one entry.
- The user approved it in words.

## Traps

- Long lists of user stories that restate one behaviour ten ways.
- Copying the request as the spec: if nothing got sharper, it is not done.
- Starting the plan in the same turn as the spec.

---
name: start
description: Entry point. Picks the right skills for a request and turns a vague ask into a confirmed brief with one round of questions, each with a suggested answer. Use at the start of work, or when the user says "I want to build", "help me with", "where do I start", "which skill".
---

Turn the request into a brief you could hand to a stranger, then route it.

## Do this

1. **Look first.** Read what the user pointed at and the code it touches. Find facts yourself; ask the user only for decisions.
2. **Test clarity.** Can you fill every brief field without a guess that would change the result? Then state the brief in two lines and go. A typo or clear one-file fix skips the brief. Format, fields, order, naming and placement are decisions, not facts: if the code does not settle them, ask. "Add an export" leaves all of them open. Asking costs one message; a wrong guess costs a rebuild.
3. **Ask one round.** Ask only about missing fields: numbered, at most 6, each with a suggested answer, worded so "yes" accepts all. Questions that depend on an earlier answer wait for a second round; never run a third.
4. **Show the brief** and wait for an explicit OK. "Whatever you think" means: take the suggestions and say so.
5. **Route.** Name the skills you will use, in order, and start the first.

## Brief template

```
Goal:      <the outcome, one sentence, in the user's words>
Audience:  <who uses or reads the result>
Context:   <what exists now, constraints, what must not break>
Inputs:    <files, data, links, accounts needed>
Format:    <code change, doc, page, report; where it lands>
Done when: <2-4 checks anyone can verify>
Not doing: <what is out of scope>
```

Keep "Not doing": most mismatches are silent disagreement about scope.

## Skills to route to

Code:
- Define: **spec** (fuzzy feature, over an hour), **plan-work** (spec to ordered tasks), **prototype** (one design question).
- Design: **api-design** (public interface), **design-code** (tangled code).
- Build: **build** (plan slice by slice), **tdd** (logic or bug fix needing proof), **frontend-ui** (screens), **parallel** (independent parts at once), **context-diet** (big repo, versioned APIs, handoff). **lean** is always on.
- Verify: **debug** (unknown failure), **check-code** (before merge), **browser-test**, **accessibility**, **performance**, **security** (input, auth, secrets, personal data), **audit** (whole repo), **quality-bar** (no written standard).
- Ship: **git**, **ship** (deploy, CI, rollback), **docs** (decisions, terms, stale docs).

Office: **speech**, **deck**, **email**, **exec-brief**, **decision**, **board-pack**, **okr**, **crisis-comms**, **meeting**, **weekly-status**, **feedback-review**, **project-plan**, **delegate**, **sop**, **summarize-doc**, **clear-request**, **spreadsheet-help**, **plan-my-day**. Office skills bring their own questions: merge them into your one round.

Chains: feature = spec, plan-work, build, check-code, git. Bug = debug, tdd, check-code.

## Stop and ask when

Two readings lead to different work, or the request conflicts with the code or an earlier decision.

## Done when

- Every brief field is filled or marked "n/a".
- The user said OK, or the request needed no brief.
- The next skill is named and started.

## Traps

- One question per message: batch them, the user's patience is finite.
- A full brief for a one-line fix.

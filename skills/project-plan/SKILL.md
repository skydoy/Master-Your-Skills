---
name: project-plan
description: Builds a project plan table with tasks, owners, dates, dependencies, risks, critical path and milestones, as Markdown or CSV for Excel; asks for deadline and team capacity. Use for "project plan", "timeline", "cronograma", "plano de projeto", "work breakdown".
---

Turn a goal into a plan someone can run and a sponsor can challenge.

## Mode

- Direct when you have the goal, the deadline and who works on it with their availability.
- Otherwise Guided. One numbered round, max 6 questions, each with a suggested answer in brackets ("ok" accepts all): the deliverable and what "done" means, hard deadline or start date, team with hours per week [4 people, 30 h each], known fixed dates (holidays, launches), output format [Markdown table; CSV for Excel], language. Max 2 rounds. Show a 4-6 line brief first.
- The deadline and capacity are required. If still missing, plan with a placeholder and say the dates are not real.

## Do this

1. Break the goal into 8-25 tasks, each ending in a checkable result. Split any task over 5 working days.
2. Estimate in working days from what the user gave; mark guesses as [ESTIMATE] and ask the owner to confirm. Do not hide uncertainty.
3. Assign an owner per task. Unknown means [OWNER]. Check load: owner days per week must not exceed their capacity.
4. Set dependencies by task ID. Compute start and end dates from the start date, skipping weekends and the stated holidays.
5. Find the critical path: the longest chain of dependent tasks. Name its IDs and total days. Anything on it has no slack.
6. Add 3-6 milestones, each a verifiable event with a date, not an activity.
7. Add risks: risk, likelihood, impact, mitigation, owner. Link each to the task it threatens.
8. Compare the end of the critical path with the deadline. If it overruns, say by how much and give 2-3 options: cut scope, add capacity, move the date.

## Table columns

ID | Task | Owner | Start | End | Days | Depends on | Milestone | Notes

For Excel, output the same columns as CSV with a header row, comma separated, dates as YYYY-MM-DD, in a code block. Keep the risks as a second CSV block.

## Done when

- Every task has an ID, owner or placeholder, dates, and dependencies without cycles.
- The critical path and the deadline comparison are stated.
- No owner is over capacity.
- Ends with "Check before using": estimates confirmed by owners, holidays, placeholders, assumptions about capacity.

## Traps

- A plan that fits the deadline only because the estimates were shrunk.
- Dependencies written in prose instead of IDs.
- Ignoring people who work on other projects too.

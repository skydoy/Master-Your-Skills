# Ready-made teams

All three teams are read-only, so no worktrees are needed. Dispatch every member in one message, use the brief template from SKILL.md, and add "do not edit files, do not spawn agents" to each brief. You do the merge.

## 1. Review team (a diff or PR)

Use for a change over ~300 lines or one touching auth, money, or data. Smaller diffs: one reviewer is enough.

| Member | Looks only at |
|---|---|
| Correctness | logic errors, edge cases, broken callers, missing tests for new branches |
| Security | input checks at trust boundaries, auth, secrets, injection, unsafe defaults |
| Simplicity | code that can be deleted, needless layers, duplicated helpers |

Shared inputs: the base and head commit, the diff saved to a file (pass the path, not the text), the task or spec it claims to meet.

Return per finding: `severity (high/med/low) | file:line | problem in one sentence | suggested fix`. Limit 300 words. No praise, no style nits a formatter would catch.

Merge: remove duplicates, keep the highest severity when two members flag the same line, sort high first. Check every high finding yourself by reading the code before you report it.

## 2. Audit team (a whole repo)

Use for "audit this codebase" on anything larger than a few thousand lines. Split by area, not by concern, so each agent reads less code.

1. List top-level modules (`ls`, the build file, the entry points).
2. Group them into 3-5 slices of similar size. Shared code (utils, config) goes to one slice only.
3. One agent per slice, each looking for: bugs, security holes, what fails under real load, risky code with no tests, dead code.

Return: up to 10 findings, ranked, each as `rank | file:line | what goes wrong for a user | effort to fix (S/M/L)`. Limit 400 words.

Merge: drop duplicates across slices, then rank the combined list by user impact divided by effort. Add one cross-slice pass yourself: patterns that appear in several slices (the same unchecked input, the same copy-pasted helper) are one finding, not many.

## 3. Research team (a question with several angles)

Use when the answer needs several independent sources: comparing libraries, checking how a feature is built in three places, reading docs for several versions. Do not use for one fact you can look up in one search.

1. Write the question in one sentence and the decision it feeds.
2. Split into 2-4 sub-questions that do not depend on each other, for example one per option being compared.
3. One agent per sub-question.

Brief additions: name the source types to trust (official docs, the code itself, changelogs) and the ones to skip (unsourced blog posts). Ask for a link or `file:line` behind every claim.

Return: `answer in 2 sentences | evidence list with links | what is still unknown`. Limit 250 words.

Merge: put the answers side by side in one table with the same columns for each option. Where agents disagree, check the source yourself rather than picking the majority. End with a recommendation and the one fact that would change it.

## Sizing

| Situation | Agents |
|---|---|
| Small diff, short question | 0, do it inline |
| Normal review or comparison | 2-3 |
| Large repo audit | 4-5 |

More than 5 rarely helps: the merge becomes the bottleneck and reports start to overlap.

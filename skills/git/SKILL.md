---
name: git
description: Turn work into clean git history and reviewable pull requests. Use when committing, writing a commit message, splitting a messy working tree into commits, naming or cleaning up branches, opening or describing a PR, tagging a release, picking a version bump or writing a changelog entry.
---

Make every change easy to review, revert and find later.

## Do this

1. **Look before you stage.** Run `git status` and `git diff`. Sort the hunks into logical changes (a fix, a feature step, a refactor, a formatting pass). Each becomes its own commit, because a mixed commit can't be reverted cleanly.
2. **Stage by change, not by file.** Use `git add -p` (or `git add <path>`) so each commit holds one change. Run its tests first; a broken commit poisons `git bisect`.
3. **Check for things that must never land.** Scan the staged diff for secrets, `.env` files, build output and large binaries. If a secret was already committed, stop: deleting it in a new commit does not remove it from history.
4. **Write the message.** Subject: `type: what changed`, imperative, under ~70 characters (`fix`, `feat`, `refactor`, `test`, `docs`, `chore`, or the repo's own scheme if `git log` shows one). Body only when the why isn't obvious from the diff: the reason, the trade-off, the issue link. Never "update", "wip", "misc".
5. **Branch short.** Branch from the default branch (`fix/…`, `feat/…`), merge within days, delete after merge. Unfinished work that must merge early goes behind a flag.
6. **Write the PR so a reviewer can decide in two minutes.** Use the template below. Aim for 100–300 changed lines; past ~1000, split (refactor first, behavior second).
7. **Release only for things with consumers.** Bump by what users can observe: breaking → major, new and compatible → minor, fix → patch. When unsure if it breaks someone, treat it as major. Tag it (`git tag -a vX.Y.Z`); add a user-facing changelog line in the same PR as the change.

PR body:

```
## What and why
<one or two sentences>  +  the smallest picture that shows the shape:
a diff-sketch of the call tree, file tree or component tree, or pseudocode

## Proof
Before: <failing test / output / screenshot>   After: <passing one>

## Risk
Reversible? <yes: plain revert | no: migration, deleted data, public API>
Could break: <who or what, in a few words>
Not touched on purpose: <related problems left for later>
```

## Stop and ask when

- You'd need to rewrite shared history: force-push, rebase of a pushed branch, `reset --hard` on others' work.
- A secret is already in history.
- The change is a one-way door (data deletion, schema drop, public API removal) and nobody has signed off.

## Done when

- Each commit does one thing and passes tests on its own.
- No secrets, build output or unrelated formatting in the diff.
- Messages say why when the diff can't.
- The PR shows proof (before/after) and names its risk and what it left alone.
- Releases, if any: version bump matches impact, tag pushed, changelog updated.

## Traps

- An "address review" commit that sneaks in a refactor.
- A "patch" that changes behavior someone relied on.
- Squashing a careful series by default; squash only when the repo does.

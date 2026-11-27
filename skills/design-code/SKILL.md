---
name: design-code
description: Shape or reshape code structure so each module hides a lot behind a small interface. Use for "improve the architecture", "this code is hard to change", "where should this boundary go", "make it testable", "clean up / simplify this module", or before adding a new layer or abstraction.
---

Good structure means a caller learns little and gets a lot, and a change lands in one place. Judge every proposal by that, not by line count or pattern names.

## Words we use

- **Interface**: everything a caller must know: types, call order, errors, side effects, config.
- **Deep module**: small interface, much hidden behavior. **Shallow**: interface about as big as the code behind it.
- **Seam**: a place where behavior can be swapped without editing callers.

## Do this

1. **Pick the area.** Take what the user named. Otherwise start with the files `git log --name-only` shows changing most; structure pays off only where code keeps changing.
2. **Learn why it is shaped this way** first: callers, tests, `git blame` on odd parts.
3. **Find friction:** one idea spread over many tiny files, wrappers that only forward calls, one rule written twice, callers that must call things in a set order, tests reaching into private state.
4. **Run the deletion test** on each suspect: imagine inlining it into its callers. Nothing gets worse? It is a pass-through; remove it. Same complexity reappears in several callers? It earns its place; make it deeper.
5. **Add a seam only for two real implementations** that exist today (often production and a test fake). One implementation is just indirection.
6. **Pass dependencies in, return values out.** Code that builds its own client or mutates its input is hard to test.
7. **List candidates before code:** files, the problem and the change in one sentence each, what gets simpler for callers. Rank them; name the first.
8. **Refactor in small behavior-neutral steps:** change, run tests, commit. Never mix a refactor with a feature or fix in one commit.
9. **Replace tests, don't stack them:** test the deepened module at its interface and delete tests of the parts it swallowed.

Single messy function? Skip 1, 5 and 7: flatten nesting with early returns, name unclear values, delete dead branches, keep behavior identical.

## Stop and ask when

- A public interface other teams or users call would change.
- A candidate contradicts a recorded decision (ADR); show the friction, ask before reopening it.
- The change would touch more than about 500 lines; propose a codemod or a split.

## Done when

- Every existing test passes with its assertions unchanged.
- The interface is no larger, and at least one concept, wrapper or file is gone.
- Each commit is refactor-only or behavior-only.
- No error handling, validation or accessibility was dropped to look cleaner.

## Traps

- Splitting a function by length into helpers no one else calls: more interface, same work.
- Inlining a helper whose name explained the idea.
- An interface "for flexibility later" with one implementation.
- Clever one-liners that need a pause to read.
- Drive-by cleanup outside the area you were asked to touch.

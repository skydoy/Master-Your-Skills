---
name: tdd
description: Write the failing test first, then the code, one behavior at a time, with tests that catch real bugs. Use when the user says "TDD", "test first", "red-green", "add tests", or when you implement logic, fix a bug, or change behavior.
---

Prove each behavior with a test you watched fail, then make it pass with the least code.

## Do this

1. **Learn how this repo tests.** Find the framework and two commands: one test file, and the full suite. Copy the style of the nearest existing test.
2. **Pick the seam.** Test through the public interface a caller uses (a function, an endpoint, a command), never private helpers. For a new module, list the seams and confirm them with the user first.
3. **Name the break.** Before writing the test, say which wrong production change would turn it red ("returns the old price", "skips the last item"). Can't name one? The test checks nothing.
4. **Red.** Write one test for one behavior. Expected values are literals you worked out by hand, never computed with the code under test. Run it. It must fail on the assertion, for the reason you named; an import error is not red. Passes at once? It tests existing behavior; rethink it.
5. **Green.** Simplest code that passes; nothing a test doesn't demand yet. Run it.
6. **Tidy** while green: remove duplication, fix names, rerun.
7. **Repeat** from step 3, letting each cycle shape the next test.
8. **Close.** Run the full suite. Then flip one condition in your new code (a `<` to `<=`, drop a `!`), confirm a test goes red, and restore the file. Report any failure by name, even ones you didn't cause.

Bug fix: the first test reproduces the reported symptom and must fail before you touch the code.

## Good tests

- Named as behavior: `rejects an expired coupon`.
- Survive a refactor that keeps behavior.
- Mock only what you don't own or can't control: network, clock, randomness, paid APIs. Your own modules stay real.
- Each test sets up its own state and runs in any order.

## Traps

- **Mirror test:** the expected value is computed the way the code computes it, so it can never disagree.
- **Mock test:** asserting the mock was called proves the mock exists, not that the feature works.
- **Change detector:** asserting a constant or exact wording; fires on redesign, sleeps through bugs.
- **All tests first:** a batch of tests written before any code locks in an imagined design.
- **Sleeps:** wait for the condition, not a fixed delay, or the test goes flaky under load.

## Stop and ask when

- The only way to test needs a large refactor or a new test framework.
- The design is so tangled that tests need piles of mocks. Hard to test means hard to use; say so.

Skip the loop for config, docs, generated code and throwaway prototypes.

## Done when

- Every new behavior has a test that you saw fail for the named reason.
- The full suite passes, with no new warnings.
- The mutation check in step 8 turned a test red.

---
name: lean
description: Always-on base for coding work. Solve the whole task with the least new code, touch only what the task needs, and end by saying what was skipped. Use on any write, fix or refactor, and when the user says "keep it simple", "yagni", "too much code", "over-engineered".
---

Every changed line should trace back to the request, and every part of the request should be covered.

## Do this

1. **Map the reach.** Before editing, list what the change must touch: callers, tests, fixtures, config, exports, docs. That is the scope; anything else is not.
2. **Pick the first option on this ladder that fully works:**
   1. Not needed at all? Skip it and say so.
   2. Already in the codebase? Reuse it the way nearby code does.
   3. In the standard library or platform? Use it.
   4. In an installed dependency? Use it. Don't add a package for a few lines.
   5. Otherwise write the least code a reader understands at once.
3. **Edit surgically.** Match the local style. Remove only what your own change orphaned. Note unrelated problems in one line instead of fixing them.
4. **Prove it.** New branching logic gets one small test or assert; a bug gets a test that failed before the fix. Fix causes in the shared code, not symptoms at each caller.
5. **Mark known limits** in the code: `shortcut: <limit>, <when to upgrade>`, so debt stays searchable.
6. **Close** with a short footer: what you left out or didn't verify, and the one risk worth the user's attention.

## Never cut

Checks on untrusted input, error paths that protect data, security, accessibility, and every part of the request. Dropping any of these makes the work incomplete, not lean.

## Done when

- Every place on the reach list is updated and tests pass.
- No line exists that the request does not need.
- The closing line is written.

## Stop and ask when

- The smallest fix needs a schema change, a new dependency, or deleting user data.
- Two readings of the request give different code.

## Traps

- Options, wrappers or config "for later". Later rarely comes; the cost stays.
- A clever one-liner that needs decoding. Short means fast to read.
- Being lazy about the change itself: leaving broken callers or tests behind.
- Tidying neighbouring code: it hides the real change.

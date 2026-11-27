---
name: prototype
description: Build a throwaway prototype that answers one design question, then keep the answer and bin the code. Use when someone asks "will this state model hold up?", "what should this page look like?", wants to try a few layouts, or wants to click through logic before building it for real.
---

A prototype is a question with code attached. Answer it fast, record the verdict, keep the code out of main.

## Do this

1. **Write the question and what would change your mind.** One sentence each, at the top of the prototype: "Can an order be partly cancelled after shipping? If the walkthrough reaches an impossible state, we redesign the states." Set a timebox (an hour or two). No clear question? You need a spec instead.
2. **Pick the shape by the question.**
   - *Logic or state* ("does this model hold up?") → one self-contained HTML file, no build or server. Logic lives in a small pure module (reducer, state machine or functions) with no DOM access, so it lifts into real code later. Around it: current state as labelled fields re-rendered after every action, one button per action, and a few scripted scenarios (happy path, edge case, something that must be refused), each from the same start. Domain words, not code names, so a non-developer can drive it.
   - *Look and layout* ("what should this be?") → 3 variants (max 5) on the real page behind `?variant=`, with real data and density; on an empty page every variant looks fine. No host page? A route with "prototype" in its name, per the project's routing. Variants differ in structure, not color. A small floating switcher (arrows and arrow keys, ignored while typing) updates the URL and is excluded from production builds.
   Ambiguous and nobody to ask? Pick by surrounding code (module → logic, page → look) and say so at the top.
3. **Cut everything that doesn't serve the answer.** No tests, no abstractions, no persistence (memory only; if storage is the question, a scratch DB named to be wiped), no real writes (stubs).
4. **Hand it over with one command or one file.** Give the path or URL and what to try. "That shouldn't be possible" and "header from B, sidebar from C" are the real results.
5. **Record the verdict, then clear main.** Write the question, the answer and why in the issue, spec or commit message. Move the prototype to a throwaway branch and link it from there. Main gets only the decision: the lifted logic module, or the winning variant rebuilt properly with tests and error handling.

## Stop and ask when

- The prototype would need production data, real credentials or real writes.
- The timebox is spent without an answer: report what you learned and ask whether the question was wrong.

## Done when

- The question and the verdict are written down where the real work is tracked.
- Prototype code is off main, on a linked throwaway branch.
- Anything kept went through normal build and test rules.
- No switcher, prototype route or scratch storage is left in production paths.

## Traps

- Polishing a prototype until it becomes the product.
- Three variants that are the same card grid in different colors.
- Logic tangled with button handlers, so nothing can be lifted out.

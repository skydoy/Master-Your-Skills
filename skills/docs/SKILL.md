---
name: docs
description: Write down decisions and domain terms so they stay true. Use when recording an architecture decision (ADR), defining or settling project vocabulary (GLOSSARY.md), updating a README or API docs after a change, or checking whether a doc is stale or "out of date" with the code.
---

Record only what the code can't say, in the one place a reader looks, and keep it true.

## Do this

1. **Pick one home per fact.** A second copy is the one that goes stale.

   | It is… | Goes in |
   |---|---|
   | why this line looks odd, a gotcha | a one-line comment beside it |
   | what a domain word means | `GLOSSARY.md` |
   | a costly-to-undo, surprising choice with real alternatives | an ADR |
   | how to install, run, test | `README` |
   | inputs, outputs, errors of a public interface | doc comments or the API spec |
   | what changed for users | the changelog |

   Fits none? It likely needs no doc. Comments restating code, commented-out code and stale TODOs get deleted or done.
2. **Follow the house style first.** Find existing ADRs, glossaries, docs folders; keep their location, numbering, file type and headings. Two conflicting conventions: say so, don't add a third.
3. **Write an ADR only if all three hold:** hard to reverse, a future reader would ask "why?", and you rejected real alternatives. A short paragraph is enough: context, decision, reason. Add rejected options only if someone would propose them again. To change an accepted decision, write a new ADR that supersedes it.
4. **Settle terms while you talk.** When a word is vague or used two ways ("account": customer or login?), propose one name, test it with an edge case, check the code agrees, then add it to the glossary at once: one or two sentences on what it is, words to avoid, related terms in bold. No implementation detail or general programming terms. Separate domains get one glossary each plus a root map.
5. **Update docs in the same change as their code**, so review sees both.
6. **Check for drift with history, not tone.** Compare the last commit touching the doc with the last commit touching its code (`git log -1 --format=%H -- <path>`, then `git merge-base --is-ancestor`). Code newer means suspect; unordered or shallow history means "can't tell", never "current".
7. **When editing prose, keep every fact.** Names, numbers, commands and caveats survive. Cut filler, not qualifiers; promise nothing the source doesn't.

Small change: steps 1 and 5 only.

## Stop and ask when

- An accepted ADR would change and nobody agreed.
- The user's meaning of a term contradicts the glossary or the code.

## Done when

- Each new fact lives in exactly one home from the table.
- New ADRs pass the three-part test and follow the repo's numbering.
- New domain terms in this change are in the glossary.
- Affected docs changed in the same commit; drift checks say "current" or an honest "can't tell".
- Change logs were appended to, never rewritten.

## Traps

- An ADR for a library pick you could swap in an afternoon.
- A glossary that slowly fills with implementation notes.
- Polishing a wrong doc; fix the facts first.

---
name: decision
description: Compares 2-5 options against explicit weighted criteria (cost, risk, time, reversibility), shows the trade-off table, recommends one and names what would change it. Use for "compare options", "which should we choose", "decision memo", "decidir entre", "comparar opções".
---

Make a choice explicit, scored and challengeable, so the reader can disagree with a weight instead of a feeling.

## Mode
- **Direct**: options and context given. Build the analysis now.
- **Guided**: one numbered round, max 6 questions, each with a bracketed suggestion: options [the ones you named, plus "do nothing"], decider [the user], deadline [none], hard constraints [none], criteria that matter most [cost, risk, time, reversibility], language [the user's]. Show a 4-6 line brief before the full output. Max 2 rounds.

## Do this
1. List 2-5 options. Always include "do nothing" or "defer" as the baseline, unless the user says it is impossible.
2. Fix the criteria before scoring. Default: cost, risk, time to value, reversibility; add only criteria that could change the result. Maximum 6.
3. Give weights that sum to 100. Say why the top weight is highest. Ask the user to confirm weights if they are a guess.
4. Mark hard constraints (budget cap, legal, deadline) as pass/fail first. An option that fails is out, not scored low.
5. Score each option 1-5 per criterion, one short evidence phrase each. Use stated data; an estimate is labelled "est.".
6. Show the table: rows = options, columns = criteria with weights, last column = weighted total. Recompute totals yourself and check they add up.
7. Recommend one option in two sentences: why it wins and what you accept losing.
8. **What would change this**: 2-4 specific triggers, such as "if the cost exceeds [VALUE]" or "if the vendor cannot deliver by [DATE]". Include one sensitivity check: does the winner still win if the top weight halves?
9. List next steps with an owner and a date, and the first review point for reversible choices.

## Rules
- Never invent costs, dates or facts. Gaps become [VALUE] and are listed at the end.
- If the totals are within 10%, say it is close and decide on reversibility or risk.
- Write in the language of the audience. Plain words, no jargon.

## Stop and ask when
- The user has not said what matters most and the options trade off sharply.

## Done when
- Weights sum to 100 and totals are correct.
- Every score has evidence or an "est." label.
- One option is recommended, with triggers that would reverse it.

## End with
**Check before using**: weights agreed by the decider; estimates replaced by real quotes where possible; placeholders filled; the baseline option fairly scored.

---
name: deck
description: Builds corporate PowerPoint decks on the company template, storyline first, with native charts from real data and a rendered QA pass. Use when the user says "make a deck", "PowerPoint", "slides for", "presentation for the board", "build on our template", or gives a .pptx/.potx.
---

Build a deck where each slide states one takeaway, on the company's own template, from the real numbers.

## Do this

1. **Check the brief.** You need: template path (.pptx/.potx, or none), context, goal or decision wanted, audience, data (files or numbers), slide count or time. All present: go (Direct). Gaps: one numbered round of up to 6 questions, each with a suggested answer in brackets, so "ok" accepts all (Guided). Max 2 rounds. Read data files yourself.
2. **Open the template and list its layouts and placeholders.** Read `reference.md` now; it has tested python-pptx code for each step. If python-pptx is missing, ask before `pip install python-pptx`.
3. **Write the storyline.** One line per slide: a headline sentence stating the takeaway, plus layout and content (bullets, chart, which data). Headlines are "so what" claims ("Churn fell 30% after the onboarding change"), not topics ("Churn"). Read in order, the headlines alone must tell the argument and end on the decision wanted. Sizing: about one slide per 2 minutes.
4. **Get OK** on the storyline in Guided mode, with a 4-6 line brief above it. Direct mode: show it and continue.
5. **Build** with python-pptx on the template's layouts.
   - Fill placeholders; no free text boxes over them.
   - Never change the template's fonts, colors, logos or masters.
   - Charts are native, built from the real data, so the user can edit them. No chart images.
   - Missing numbers become `[VALUE]`, never a plausible guess.
   - Sources and talking points go in speaker notes.
6. **QA, every time.** Run the structural check in `reference.md`. If `soffice` exists, render and look at every slide. Fix until clean:
   - no text overflowing its box or the slide;
   - no empty title or body placeholders;
   - body text 14 pt or larger;
   - one message per slide; split a slide that makes two.
   No LibreOffice: say the visual check was skipped.
7. **Deliver** the .pptx path, the headline list, and Check before using.

Three slides or fewer: skip the brief, keep storyline and QA.

## Stop and ask when

- The data does not support the wanted headline. Show what it says.
- The template lacks a layout the content needs. Offer the closest one; do not invent one.
- A number would have to be estimated or derived in a way the user has not seen.

## Done when

- Every title is a takeaway sentence; titles alone tell the story.
- The deck uses only the template's layouts; nothing restyled.
- Every chart is native and traceable to the given data.
- QA passed: no overflow, no empty placeholders, body ≥14 pt, or the visual check is flagged as skipped.

Check before using lists 2-4 items: placeholders left, numbers to verify, sensitive slides, QA checks not run.

## Traps

- Topic titles ("Q3 results") that leave the audience to find the point.
- Shrinking fonts instead of splitting a crowded slide.
- Leaving the template's sample slides in the file.

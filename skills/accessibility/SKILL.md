---
name: accessibility
description: Audit an existing page or component against WCAG 2.2 AA and fix what fails. Use for an accessibility or a11y audit, running axe or pa11y, triaging a11y violations, or when "screen reader can't read this", "keyboard doesn't work" or "contrast is too low" comes up.
---

Find the real barriers on a built interface, fix them at the source, and report only what was actually tested.

## Do this

1. **Fix the scope.** List the pages or components and the user tasks to test ("sign up", "open an order"). Tasks find more than URLs, because barriers sit in flows: dialogs, errors, updates.
2. **Run an automated scan** with what the project already has (axe in tests, Lighthouse, an axe or pa11y CLI pinned to a version). Scan every state, not only first load: open the dialog, trigger the error, scan again. Confirm each hit in the DOM; drop false positives with a one-line reason.
3. **Test by keyboard.** Complete each task with Tab, Shift+Tab, Enter, Space, Escape and arrow keys only. Check: every control reachable, focus always visible and never hidden under sticky bars, order matches the screen, no traps, focus moves into dialogs and returns on close.
4. **Test the meaning layer.** Read the accessibility tree (browser DevTools or the browser-test skill): names, roles and states of controls, heading outline, landmarks, form labels and error links, live-region announcements. Use a real screen reader when available.
5. **Test the visual layer.** Contrast (4.5:1 text, 3:1 large text and UI parts and focus rings), 200% zoom and 320px width without loss, reduced motion, color never the only signal. Read `reference.md` for the full AA list, including the criteria new in 2.2.
6. **Rank findings.** Blocker (task impossible for some users), serious (possible but very hard), moderate, minor. For each: element, criterion number, who is affected, how you found it.
7. **Fix in this order:** use the right native element (`button`, `a`, `label`, `fieldset`, `dialog`), then fix structure and CSS, and add ARIA only where HTML cannot say it. Fix shared components once, not per page.
8. **Re-test each fix** the way it was found: scan again for scan findings, keyboard again for keyboard findings.

Single component: steps 2-5 on that component only.

## Stop and ask when

- A fix changes the visual design (colors, focus style, layout) beyond the token you are touching.
- The target is a legal conformance claim (VPAT, ACR): that needs a human screen-reader pass you cannot replace.

## Done when

- [ ] No blocker or serious findings remain open, or each open one has an owner and a reason.
- [ ] Every user task in scope was completed by keyboard alone.
- [ ] Automated scan is clean on every tested state.
- [ ] Each finding is marked with how it was tested: scan, keyboard, tree, or named screen reader plus browser. Anything not tested is listed as "not tested", never as passing.

## Traps

- A clean axe score treated as a pass; scans miss most issues.
- `aria-label` on a `div` instead of using a `button`.
- `outline: none` with no replacement focus style.
- Live regions added after content changes, so nothing is announced.
- Fixing one page while the broken shared component stays broken.

---
name: frontend-ui
description: Build or change user-facing UI that looks deliberate, not AI-generated. Use when making a page, screen, component, form, dashboard or landing page, when picking colors, fonts or spacing, or when someone says the UI "looks generic" or "looks like AI".
---

Ship UI whose every visual choice traces to the product, its users or its design system, never to a model's habits.

## Do this

1. **Read what exists first.** Find the design tokens (CSS variables, Tailwind config, theme file), the component library, and two screens that already look right. Reuse them; a new value needs a one-line reason.
2. **Write a five-line design contract** before code:
   - *Job*: what the user comes to this screen to do, and the one primary action.
   - *Audience and setting*: who, on what device, how often (daily tool vs. one visit).
   - *Density*: dense (data, admin, repeat use) or airy (marketing, first contact).
   - *Tone*: two words from the product type, e.g. "calm, precise" for finance.
   - *Reject*: the defaults you will not use here (see Traps).
   No design system? Derive a small token set from the contract (1 accent, neutrals, 1 type family, a 4px or 8px spacing scale, 2 radii); `reference.md` maps product types to choices.
3. **Lay out by priority, not by template.** The primary action and the data the user came for get the most weight. Use realistic content; placeholder text hides wrapping and overflow bugs.
4. **Build from small focused components.** Composition over prop flags; data loading separated from rendering. Keep state as local as possible: component, lifted, URL (filters, pages), and a store only when many distant parts write it.
5. **Cover every state.** Loading (skeleton shaped like the content), empty (says what to do next), error (what happened, plus retry), partial or long data, success, no permission. A blank screen is a bug.
6. **Build it accessible from the start.** Native elements (`button`, `a`, `label`, `dialog`), visible focus, text contrast 4.5:1, nothing conveyed by color alone. For an audit of existing UI, use the accessibility skill.
7. **Look at it.** Render at about 360px and 1280px wide (browser-test skill), in dark mode if the product has one. Fix overflow and crowded tap targets.

Small change (one button, one fix): skip step 2 and match the neighbors exactly.

## Stop and ask when

- The change needs a new brand color, font or visual direction and no designer or design system says which.
- The request conflicts with the existing design system.

## Done when

- [ ] Every color, size and spacing value is a token or matches the existing scale.
- [ ] Loading, empty, error and long-content states render and were looked at.
- [ ] Works at 360px and 1280px with no horizontal scroll.
- [ ] Keyboard can reach and operate every control; focus is visible.
- [ ] No console errors on the rendered page.

## Traps

- Purple gradients, glassy cards, `rounded-2xl` everywhere, big centered heroes: model defaults, not product choices.
- Identical card grids for content that has a clear order of importance.
- Same generous padding everywhere, which flattens the hierarchy.
- Emoji used as icons; mixed icon sets or stroke widths.
- Styling only the happy path.

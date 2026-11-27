# frontend-ui reference

Read this when step 2 of the skill finds no design system, or when the user says the result looks generic.

## Product type to starting choices

These are starting points to adapt, not rules. Check each against the product's real users and content.

| Product type | Density | Color | Type | Motion |
|---|---|---|---|---|
| Admin, analytics, ops tools | Dense: 4-8px base step, tables over cards | Neutral greys, one accent for actions, status colors kept for status only | One sans family, tabular numbers | Almost none; 100-150ms state changes |
| B2B SaaS app | Medium | Calm neutral base, one confident accent | Sans for UI, clear weight steps | Subtle hover and focus feedback |
| Finance, legal, health | Medium | Low saturation, high contrast, no playful accents | Highly legible sans, generous line height | Minimal; never on numbers |
| Marketing / landing | Airy: 16-24px base step, wide sections | Brand color carries the page; one contrast color for the main CTA | A display face for headings is fine, body stays simple | Short entrance effects, honors reduced motion |
| Consumer / social | Medium to airy | Brighter accent, warm neutrals | Friendly sans | Quick, springy feedback on taps |
| Content, docs, blog | Airy, narrow measure (60-75 characters per line) | Near-black text on off-white | A serif or readable sans at 16-18px body | None |
| E-commerce | Medium | Product images carry color; UI stays quiet | Clear price and title hierarchy | Minimal; fast image loading matters more |

## Minimum token set

- Colors: background, surface, border, text, text-muted, accent, accent-text, danger, success. Define dark values separately and check contrast in both themes.
- Type: one family (two at most), sizes from a ratio scale (for example 12, 14, 16, 20, 24, 32), body line height about 1.5.
- Spacing: multiples of 4 or 8 only.
- Radii: one small (inputs, buttons), one large (dialogs, panels).
- Shadow: one level, or none.
- Motion: one short duration (about 150ms) and one medium (about 250ms), plus a `prefers-reduced-motion` override.

## Why generic UI looks generic

| Default | What it signals | Better |
|---|---|---|
| Indigo or purple accent with gradient | No brand thinking | The product's color, or one chosen from the tone words |
| Every corner fully rounded | No hierarchy of shapes | Two radii, used by role |
| Shadow on every card | Depth with no meaning | Borders or spacing; shadow only for things that float |
| Centered hero, three feature cards, CTA | A template, not this product | Lead with the thing users came for: data, product, the main task |
| Same padding everywhere | Nothing is more important than anything else | Tight inside groups, loose between groups |
| Lorem ipsum, "John Doe", round numbers | Untested layout | Real lengths: long names, empty values, 5-digit numbers, translations |
| Spinner for page content | Layout jumps when data lands | Skeleton with the content's shape |
| Icon-only buttons | Guessing game | Icon plus label, or a label in the accessible name and a tooltip |

## Layout checks

- One clear primary action per screen; secondary actions look secondary.
- Headings in order (h1, then h2, then h3); one h1 per page.
- Forms: label above or beside each field, errors next to the field, the submit button says what it does ("Save changes", not "Submit").
- Long content: tables scroll inside their container on small screens; text never sits edge to edge on wide screens.
- Touch targets at least 24x24 CSS px with spacing, 44x44 for primary mobile actions.
- Fixed headers and footers never cover content or the focused element.
- Images and embeds reserve their space (width and height set) so nothing jumps.

## Interaction checks

- Every interactive element has hover, focus, active and disabled styles, and the state change does not move the layout.
- Feedback within about 100ms of a click: pressed state, optimistic update or progress.
- Destructive actions ask for confirmation or offer undo.
- Animations use transform and opacity, carry meaning (where did this come from, where did it go), and stop under reduced motion.
- Dark mode: check borders, dividers and focus rings separately; values from light mode rarely carry over.

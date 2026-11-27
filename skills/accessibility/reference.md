# accessibility reference: WCAG 2.2 AA in practice

Read this at step 5 of the skill, or when a finding needs its criterion number.

## Perceivable

- **1.1.1 Text alternatives.** Meaningful images have `alt` that says what they convey; decorative ones have `alt=""`; icon-only controls have an accessible name; charts have a text summary or table.
- **1.2.x Media.** Captions for video with speech; a transcript for audio; no autoplay with sound.
- **1.3.1 Structure.** Headings, lists, tables (`th` with `scope`), landmarks and label-input links exist in the markup, not just in the visuals.
- **1.3.2 / 2.4.3 Order.** Reading and focus order match the visual order; CSS reordering does not scramble them.
- **1.3.5 Input purpose.** Personal fields use `autocomplete` (`email`, `name`, `tel`, `street-address`).
- **1.4.1 Color.** Errors, required fields, links in text and chart series are told apart by more than color.
- **1.4.3 Text contrast.** 4.5:1; 3:1 for large text (24px, or 18.66px bold). Check placeholder, disabled-looking-but-active, and hover text too. Do not round 4.4 up.
- **1.4.4 / 1.4.10 Resize and reflow.** 200% zoom keeps all content; at 320px width there is no two-way scrolling (data tables and maps excepted).
- **1.4.11 Non-text contrast.** Input borders, icons that carry meaning, focus rings and chart lines reach 3:1 against what is next to them.
- **1.4.12 Text spacing.** Layout survives larger line, letter and word spacing (no fixed-height text boxes).
- **1.4.13 Hover or focus content.** Tooltips can be dismissed with Escape, can be hovered, and stay until dismissed.

## Operable

- **2.1.1 / 2.1.2 Keyboard.** Everything works by keyboard; nothing traps focus except a modal, which releases on close.
- **2.2.1 / 2.2.2 Timing and motion.** Time limits can be extended; carousels and auto-updates can be paused.
- **2.3.1 Flashes.** Nothing flashes more than three times a second.
- **2.4.1 Bypass.** A skip link or landmarks let users jump past repeated navigation.
- **2.4.2 Page title.** Each page or route has a unique, descriptive `title`.
- **2.4.4 Link purpose.** Link text makes sense with its context; no bare "click here" lists.
- **2.4.6 Headings and labels.** They describe the content or the field.
- **2.4.7 Focus visible.** Every focused element shows a clear indicator.
- **2.4.11 Focus not obscured (new in 2.2).** Sticky headers, cookie banners and chat widgets never fully hide the focused element.
- **2.5.3 Label in name.** The accessible name contains the visible label text, so voice users can say what they see.
- **2.5.7 Dragging (new).** Every drag action (sliders, sortable lists, maps) has a single-pointer alternative such as buttons.
- **2.5.8 Target size (new).** Targets are at least 24x24 CSS px, or have enough space around them; inline links in text are exempt.

## Understandable

- **3.1.1 Language.** `html lang` is set; passages in another language are marked.
- **3.2.1 / 3.2.2 Predictable.** Focus or input alone never submits a form or jumps to a new page.
- **3.2.6 Consistent help (new).** Help links or contact options sit in the same place across pages.
- **3.3.1 / 3.3.3 Errors.** Errors are described in text, tied to the field (`aria-describedby`), and suggest a fix; on submit, focus moves to an error summary or the first bad field.
- **3.3.2 Labels.** Every input has a visible label; placeholder text is not a label.
- **3.3.7 Redundant entry (new).** Do not ask again for what the user already entered in the same process; prefill or offer to reuse it.
- **3.3.8 Accessible authentication (new).** Login needs no memory or puzzle test without an alternative: allow paste and password managers, offer a non-cognitive option for CAPTCHAs.

## Robust

- **4.1.2 Name, role, value.** Custom widgets expose role, name and state (`aria-expanded`, `aria-selected`, `aria-pressed`, `aria-checked`) and update them. Follow the ARIA Authoring Practices pattern for menus, tabs, comboboxes and dialogs exactly, keys included.
- **4.1.3 Status messages.** Saves, results counts and background errors are announced through `role="status"` (polite) or `role="alert"` (urgent) on a container that exists before the message appears.

## Quick fixes

| Found | Fix |
|---|---|
| Clickable `div` or `span` | `button` for actions, `a href` for navigation |
| Custom select without keyboard support | Native `select`, or the full listbox pattern |
| `tabindex` above 0 | Remove it; fix the DOM order |
| Error shown only in red | Add icon and text, link with `aria-describedby`, set `aria-invalid` |
| Modal opens, focus stays behind | Native `dialog` with `showModal()`, focus the first control, restore on close |
| Spinner with no text | `role="status"` with a text label such as "Loading orders" |

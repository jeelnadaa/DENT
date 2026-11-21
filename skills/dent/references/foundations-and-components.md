# Foundations and Components

Moved from SKILL.md §3–4 in DENT 2.0. Read this file whenever you create tokens or build/spec components (almost every Create, Redesign, Extend and Implement task). Section numbers below are kept from DENT 1.x so older notes still match ("§3 Foundations", "§4 Components").

Labels: **[Law]** research-backed · **[Rule]** measurable standard, never overridden · **[Convention]** default you may change deliberately (log it).

---

## §3 Foundations (design tokens)

Define these as named tokens first. Every component uses only tokens.

### Color
- **Default palette (when the user gives no colors):** build a concept palette (`references/color.md` §12): a seed from the concept run through `scripts/palette.py make`, which returns role tokens for light and dark (bg, surface, raised, border, text, muted, accent, on-accent, accent-text, focus, optional second) with every pair contrast-checked and a cliché report. Twenty verified concept palettes are in `references/color.md` §13 as starting points. Scales, harmony, dark mode and color theory: `references/color.md` Part 1.
- **Structure:** neutrals (background, surface, border, text levels), one brand/primary, optional accent, semantic set (success, warning, error, info).
- **[Rule] Contrast (WCAG 2.x AA):** body text ≥ 4.5:1; large text (≥ 24px regular or ≥ ~18.7px bold) ≥ 3:1; UI components and meaningful graphics (input borders, icons, focus rings) ≥ 3:1 against adjacent colors.
- **[Rule] Never use color alone** to convey meaning — pair with text, icon or shape (errors, status, charts).
- **[Convention]** Use a few text levels (primary, secondary, disabled) instead of many greys.
- **[Convention]** Reserve the primary color for interactive and key elements so it keeps its meaning.
- **[Convention]** If supporting dark mode, design it as its own palette (lower saturation, raised surfaces get lighter), not an inversion.

### Typography
- **[Convention]** One or two typefaces maximum.
- **[Convention]** Use a modular type scale (e.g. ratio 1.2–1.333) so sizes relate to each other.
- **[Convention]** Body text on screens: ~16px minimum on web; follow platform defaults on native (iOS Body 17pt, Android 14–16sp).
- **[Law/Convention]** Line length ~45–75 characters for body text (~66 ideal) for comfortable reading.
- **[Convention]** Line height ~1.4–1.6 for body text; tighter (~1.1–1.3) for large headings.
- **[Convention]** Build hierarchy with size, weight and color together, not size alone. Limit to a handful of styles (display, heading levels, body, small/caption, label).
- **[Rule]** Text must remain usable when zoomed to 200% (WCAG 1.4.4).

### Spacing
- **[Convention]** Use a base unit of 4 or 8px; every margin, padding and gap is a multiple (4, 8, 12, 16, 24, 32, 48, 64…).
- **[Law: proximity]** Space inside a group must be smaller than space between groups.
- **[Convention]** Whitespace is a tool for hierarchy, not leftover area.

### Layout grid
- **[Convention]** Use a column grid (commonly 4 columns mobile, 8 tablet, 12 desktop) with consistent gutters and margins.
- **[Convention]** Set a max content width so lines and layouts don't stretch on wide screens.
- **[Convention]** Define breakpoints from content needs, not specific devices.

### Shape
- **[Convention]** Pick a small radius scale (e.g. none, small, medium, large, full) and use it consistently.
- **[Convention]** Nested radii: inner radius = outer radius − padding, so curves look concentric.

### Elevation
- **[Convention]** Define a few elevation levels (flat, raised, overlay, modal). Higher = closer to user = more prominent.
- **[Convention]** Shadows should imply one consistent light source.

### Iconography
- **[Convention]** One icon family, one stroke weight, consistent sizes on the spacing grid.
- **[Law: recognition over recall]** Icons alone are often ambiguous; label them unless universally understood (search, close, home, menu).

---

## §4 Components — consistent specs

**The core rule [Law: similarity + consistency heuristic]:** every instance of a component looks and behaves the same across the whole product. A button on the settings screen and a button on the checkout screen of the same variant and size are identical. To guarantee this, each component is defined ONCE as a spec with fixed parameters, and every screen reuses that spec. No screen-level overrides.

The numbers below are **[Convention]** defaults. Change them per project or per aesthetic style, but once chosen they apply everywhere. Values marked **[Rule]** don't change.

These are **design specs** (sizes, spacing, states, behaviour). On the web, build each component the way its Modern Web Guidance guide says (native element first, MWG's markup, ARIA, fallbacks; `modern-web-guidance.md` §4 maps components to guides), then apply these specs to it. Px values are design units: in CSS, type sizes become `rem`, and heights of anything containing text become `min-block-size` so text can grow (`mwg:typography`).

Browser-drawn pieces of these components (checkbox and radio marks, slider tracks, select pickers, scrollbars, selection, caret, placeholder, autofill, tooltips) follow the product's built-in surface level (Match / Tint / Native) in `built-in-surfaces.md`.

### 4.1 Shared control tokens (define these first)

"Controls" = anything the user types into or presses: buttons, inputs, selects, chips, segmented controls. They share these tokens so they line up when placed side by side.

| Parameter | Default | Notes |
|---|---|---|
| Control height | sm 32 · **md 40** · lg 48 px | On touch-first products, make md = 44–48. A minimum (`min-block-size`), not a fixed height. |
| Horizontal padding | sm 12 · md 16 · lg 20 px | |
| Control radius | one value, e.g. **8px** | Buttons, inputs, selects, chips all use it. |
| Container radius | control radius + 4–8px, e.g. **12–16px** | Cards, modals, menus, sheets. Containers are rounder than the controls inside them. |
| Border width | **1px** (inputs, outlined buttons); 1.5–2px (checkbox, radio) | |
| Control font | 14–16px, weight 500 (medium) | One "label" text style for all control text. |
| Icon size in controls | 16px (sm) · **20px (md/lg)** | |
| Icon–text gap | **8px** | |
| Focus ring | **2px** outline, **2px** offset, Off/primary color | **[Rule]** ≥ 3:1 contrast against background. Same ring on every focusable element. |
| Disabled | reduced contrast (e.g. 40–50% opacity) + no pointer events | Disabled text is exempt from WCAG contrast, but must still look clearly disabled, not just "light". |
| State transition | 100–150ms ease-out | Hover/press color changes. |
| Hit area | **[Rule]** ≥ 44×44 touch, ≥ 24×24 pointer (WCAG 2.2) | Extend invisibly with padding if the visual is smaller; bump up under `@media (pointer: coarse)` (`mwg:accessibility`). |

**Alignment rule:** a button and an input of the same size in the same row have the same height, radius and font size.

**State color formula (use for all controls):**
- Hover: base color shifted ~8% (darker on light mode, lighter on dark mode)
- Pressed: shifted ~12–16%
- Focus: base color + focus ring (never remove the ring for mouse-free users)
- Disabled: see table above
- Error: error color for border/text + icon + message

### 4.2 Buttons

| Parameter | Default |
|---|---|
| Variants | **Primary** (filled, Off/primary color), **Secondary** (outlined or tinted), **Tertiary/Ghost** (text only), **Destructive** (filled or outlined, error color) |
| Sizes | sm / md / lg from shared tokens |
| Min width | ~64–80px so short labels ("OK") don't make tiny buttons |
| Label | sentence case, verb + object ("Save changes"), no wrapping (single line) |
| Text on filled button | must be ≥ 4.5:1 on the fill **[Rule]** |
| Icon | optional leading icon; trailing only for direction (→, ▾, external link) |
| Loading | spinner replaces or precedes label; **button keeps its width**; disabled while loading |
| Full width | on mobile, primary actions in forms/sheets may be full width; on desktop, size to content |
| Button groups | 8–12px gap; primary goes in the same position every time (pick one: right on desktop dialogs is common on web; follow platform on native) |

Rules:
- One Primary button per view or section (Von Restorff).
- Destructive actions are never the default focus and need confirmation or undo.
- Don't use a link styled as a button, or a button styled as a link: buttons do actions, links navigate.

### 4.3 Icon buttons
- Square: width = height = control height (32/40/48).
- Icon 20px (md). Same variants as buttons (filled, tinted, ghost).
- **[Rule]** Needs an accessible name (aria-label) and, on pointer devices, a tooltip.
- **[Rule]** Hit area ≥ 44px on touch even if the visible circle is smaller.

### 4.4 Text inputs (text field, textarea)

| Parameter | Default |
|---|---|
| Height | = control height (md 40, or 44–48 on touch) |
| Padding-x | 12px |
| Radius | control radius |
| Border | 1px, neutral color with **≥ 3:1** contrast to background **[Rule]** (or a filled background with a ≥ 3:1 bottom border) |
| Background | surface color (same in every input) |
| Label | **above** the field, always visible, label text style, 6–8px gap to field |
| Placeholder | example format only ("name@example.com"), never a replacement for the label |
| Helper text | below field, caption style (12–14px), 4–6px gap |
| Error | error-color border + error icon + specific message in place of helper text **[Rule: not color alone]** |
| Focus | border becomes Off/primary + focus ring |
| Disabled / read-only | disabled = dimmed + not editable; read-only = normal text, no border emphasis, still selectable |
| Prefix/suffix | icons 20px, 8px from edge; e.g. search icon, clear (×), show/hide password |
| Required/optional | mark one consistently across the product (usually mark "Optional" when most fields are required) |
| Textarea | same tokens; min 3 rows; vertical resize only; optional character counter bottom-right |

### 4.5 Select / dropdown / combobox
- Closed state is identical to a text input (same height, border, radius, padding) + chevron 16–20px on the right.
- Menu: container radius, overlay elevation, 4–8px gap below the field, width ≥ field width.
- Menu items: height ≥ 36px pointer / 44px touch, padding-x 12px, hover background tint, selected item marked with a check icon (not color alone).
- Max height ~5–8 visible items, then scroll.
- **[Rule]** Full keyboard support (arrows, Enter, Esc, type-to-search).
- Web: style the native `<select>` (customizable select, `appearance: base-select`) to these specs before reaching for a custom listbox (`mwg:branded-select-styling`, `mwg:custom-select-picker-layouts`); a searchable combobox is a library job.
- If there are ≤ 5 options and space allows, use radio buttons or a segmented control instead (Hick's Law: visible options are faster).

### 4.6 Checkboxes

| Parameter | Default |
|---|---|
| Box size | **18px** (16–20) |
| Radius | small, 3–4px (less than control radius) |
| Border | 1.5–2px, ≥ 3:1 contrast **[Rule]** |
| Checked | fill = Off/primary, check icon in on-primary color |
| Indeterminate | same fill with a horizontal dash (for "some selected" parent) |
| Label | right of box (LTR), 8px gap, body text style, **label is clickable** |
| Group spacing | 8–12px between items, vertical list preferred |
| Hit area | box + label together ≥ 44px tall on touch |

Use for: multiple independent choices, or a single on/off that takes effect on form submit ("I agree to…").

### 4.7 Radio buttons

| Parameter | Default |
|---|---|
| Circle size | **same as checkbox (18px)** so they align in mixed forms |
| Border | same as checkbox |
| Selected | Off/primary outer ring + inner dot ~40–50% of diameter |
| Label, gap, spacing, hit area | identical to checkbox |
| Group | always has a group label (legend); one option pre-selected when a sensible default exists |

Use for: exactly one choice from 2–5 visible options.

### 4.8 Toggles / switches

| Parameter | Default |
|---|---|
| Track | 36–44 × 20–24px, fully rounded |
| Thumb | track height − 4px (2px inset), circle |
| On | track = Off/primary, thumb = on-primary |
| Off | neutral track with ≥ 3:1 contrast boundary **[Rule]** |
| Motion | thumb slides 150–200ms ease-out |
| Label | left of switch in settings lists (label left, switch right) |

Rule: a toggle **takes effect immediately** (like a light switch). If the change only applies after pressing Save, use a checkbox instead.
Web: `<input type="checkbox" switch>` with a `<label>`, styled to these specs (`mwg:switch`).

### 4.9 Segmented control / tabs
- Segmented control: height = control height, container radius = control radius, selected segment filled or raised, 2–5 options, equal widths.
- Tabs: height 40–48px, label text style, active tab = Off/primary text + 2–3px indicator bar; inactive = secondary text. Indicator animates between tabs (150–250ms).
- Tabs switch views; segmented controls switch modes/filters of the same view.

### 4.10 Sliders
- Track height 4px, radius full; filled portion Off/primary; unfilled neutral (≥ 3:1).
- Thumb 16–20px circle with ≥ 44px hit area.
- Show the current value (label or tooltip while dragging). Provide a text input alongside when precise values matter.
- **[Rule]** Operable by keyboard (arrow keys).

### 4.11 Links
- Off/primary color; **underlined inside body text [Rule: not color alone]**; may drop underline in nav menus where context makes them clearly clickable.
- Hover: underline thickens or color shifts. Focus: standard focus ring.
- Link text says where it goes ("View invoice"), never "click here".

### 4.12 Chips, tags and badges
- **Chips** (interactive filters/selections): height 28–32px, padding-x 10–12px, radius full or control radius (pick one product-wide), selected = tinted fill + check icon.
- **Tags** (static labels): same shape as chips, smaller (24px), not interactive-looking.
- **Badges** (counts/status): height 16–20px, caption text, radius full; dot-only badge 8px. Status badges pair color with text ("Paid", "Overdue").

### 4.13 Cards

| Parameter | Default |
|---|---|
| Padding | 16px (compact) / **24px** (default) — one value product-wide per density |
| Radius | container radius |
| Separation | **border OR shadow, not both** — pick one approach for the whole product |
| Internal spacing | from spacing scale; title → body 8px, sections 16px |
| Clickable cards | entire card is the hit area; hover elevation or tint; no separate nested buttons that compete unless clearly secondary |

### 4.14 Lists and rows
- Single-line row 48–56px; two-line row 64–72px; padding-x 16px.
- Leading element (icon 24 / avatar 40) and trailing element (chevron, switch, meta text) align on the same column in every row.
- Separate rows by divider OR spacing — consistently.

### 4.15 Tables
- Row height: compact 36–40, default **48**, relaxed 56px. Header row same height, medium weight, secondary color.
- **Numbers right-aligned with tabular (monospaced) figures; text left-aligned**; column headers align with their data.
- Dividers between rows (1px, low contrast) or zebra striping — one choice.
- Sticky header on long tables; horizontal scroll on narrow screens rather than squashing columns.

### 4.16 Navigation
- Top bar: 56–64px height; same position, content and order on every screen.
- Mobile bottom nav: 56–64px + safe area, 3–5 destinations, icon + label, active = Off/primary icon and label.
- Sidebar: item height 36–44px, icon 20px, active item has tinted background + Off/primary text.
- **[Rule: visibility of status]** The current location is always marked.

### 4.17 Overlays

**Modal / dialog**
- Widths: sm 400 · md 560 · lg 720px; mobile: full width with 16px margins, or a bottom sheet.
- Padding 24px; container radius; modal elevation.
- Scrim (backdrop): black at 40–60% opacity (both modes).
- Structure: title → content → actions. Actions in a fixed position and order across ALL dialogs.
- **[Rule]** Focus moves into the dialog and can't reach the page behind it, Esc closes (unless destructive in-progress), focus returns to the trigger on close, the page behind doesn't scroll. On the web all of this comes from a native `<dialog>` opened with `showModal()`: don't add `role="dialog"`, `aria-modal`, a focus trap or an `overflow: hidden` scroll lock (`mwg:dialog`, `mwg:prevent-page-scroll-under-modal-dialog`). Light dismiss: `closedby="any"` (`mwg:light-dismiss-a-dialog`). Animate with `@starting-style` + `overlay` (`mwg:animate-to-from-top-layer`).

**Drawer / bottom sheet**
- Side drawer 320–400px wide; bottom sheet with a 32×4px drag handle and container radius on top corners only.
- Web: build navigation drawers and sheets as in `mwg:navigation-drawer` (a `<dialog>` with a scroll-snap swipe surface), not with a hand-made overlay.

**Menus / popovers**
- Container radius, overlay elevation, 4–8px offset from trigger, item height as in 4.5.
- Web: `popover` + CSS anchor positioning with `position-try` fallbacks so it flips at viewport edges (`mwg:menu`, `mwg:viewport-aware-dropdowns`); no JS positioning library.

**Tooltips**
- Caption text (12–13px), padding 6×10px, small radius (4–6px), high-contrast background (inverted colors), from the `--tooltip-*` tokens (`built-in-surfaces.md` §3). Never a `title` attribute for information users need.
- Appear after ~300–500ms hover / on focus; disappear on mouse-out/Esc. No interactive content inside.
- Web: `popover="hint"` + `interestfor` + anchor positioning (`mwg:interest-triggered-tooltips`, `mwg:position-aware-tooltips`); on touch use a toggletip.

### 4.18 Feedback components
- **Toasts/snackbars:** same screen position every time (e.g. bottom-center mobile, bottom-left/right desktop); max one action ("Undo"), which must also exist outside the toast; success/info auto-dismiss after ~4–6s, **errors stay until dismissed**; **[Rule]** announced to screen readers (live region). Web: `popover="manual"` container per `mwg:persistent-toast-notifications`.
- **Inline alerts/banners:** semantic color tint background + icon + text; dismissible only if non-critical.
- **Spinners:** 16 / 24 / 32 / 48px; use for short, unknown waits.
- **Progress bars:** 4–8px tall; use when progress is known (Goal-gradient effect).
- **Skeletons:** match the shape of the real content; subtle shimmer or pulse (static under reduced motion).

### 4.19 Avatars and dividers
- Avatar sizes 24 / 32 / 40 / 48 / 64px; circle (or one consistent radius); fallback = initials on a tinted background.
- Dividers 1px, Complement at low opacity (~10–15%); full-bleed or inset (aligned to content) — consistent per list type.

### 4.20 Screen-level requirements
- **Every screen needs:** an empty state, a loading state, an error state and a success/content state.
- Feedback choice: inline message for field-level issues, toast for non-blocking confirmations, dialog only for decisions that need interruption.

### 4.21 Spec template for any new component

More components (date picker, file upload, stepper, command palette, data-table features, kanban, OTP, carousel…) are specced in `references/components-extended.md`. When adding a component not listed in either place, define it with these parameters before using it:
1. **Purpose** — when to use it, and when to use something else instead
2. **Anatomy** — its parts (container, label, icon, indicator…)
3. **Variants and sizes** — mapped to shared tokens
4. **Dimensions** — height, padding, radius, border, icon size, gaps (all from tokens)
5. **Typography** — which text style each part uses
6. **Colors per state** — default, hover, focus, pressed, selected, disabled, error, loading
7. **Behavior** — interaction, motion, keyboard, touch
8. **Accessibility** — role, accessible name, contrast, hit area
9. **Content rules** — label length, casing, truncation

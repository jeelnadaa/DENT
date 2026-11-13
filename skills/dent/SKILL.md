---
name: dent
description: DENT is a product design skill for any UI work - designing, redesigning, auditing or building websites, web apps, mobile and desktop apps, dashboards, landing pages, design systems and marketing assets. Use it whenever the task involves layout, visual style, components, UX flows, accessibility, design tokens, DESIGN.md, or turning a design into front-end code. It asks focused questions first, lets the user pick an effort level and one of 41 aesthetic styles, applies proven UX laws and WCAG rules, avoids generic AI-looking output, verifies the result visually, and records everything in an approved DESIGN.md.
license: Apache-2.0
metadata:
  author: Jeel Nada (solarquack)
  version: "1.0.0"
  homepage: https://github.com/jeelnadaa/DENT
---

# DENT — Product Design Skill

A complete design skill for products, websites and apps. This file holds the workflow (§1) and everything that applies to every design regardless of style (§2–8). Reference files hold the deeper material and are read only when needed (§9). Paths in this file are relative to this skill's folder.

**DENT's promise:** designs that are correct (laws, rules, accessibility), consistent (tokens and specs), distinctive (no template look) and documented (Decision Log → DESIGN.md).

Labels used throughout:
- **[Law]** — backed by research or long-established perceptual/cognitive findings.
- **[Rule]** — a standard or measurable threshold (WCAG, platform guidelines). Non-negotiable, in every style and effort level.
- **[Convention]** — widely used industry practice. Default to it; deviate only on purpose (aesthetic styles may override these).

---

## 1. Workflow — how to work with the user

Users rarely describe how a design should look. **Asking questions is the top priority.** Full rules, wording and tables: **`references/workflow-questions-and-effort.md`**.

### 1.0 Pick the mode, and check what already exists
Before asking anything, decide the mode (details: `references/modes-existing-products.md`):
- **Create** (nothing exists) → normal workflow below.
- **Redesign** (existing product) → inventory first, ask what must stay, plan the migration.
- **Audit / review** (screenshot, URL, "what's wrong?") → look first, then a prioritized findings report. Don't redesign unasked.
- **Extend** (add to a DENT design) → read `DESIGN.md`, use the add-on routing (§1.5).
- **Implement** (build in code) → read `DESIGN.md`, detect the stack, tokens first.

**In a codebase, always look before designing:** if a `DESIGN.md`, token files, a theme config or a UI library (shadcn/ui, MUI, Chakra, Tailwind theme…) exists, **adopt and extend it — never introduce a second design system.**

### 1.1 Ask first, one question at a time
1. Note what the prompt already tells you (product, platform, style words, colors, audience); don't ask about those.
2. **Question 0 is always the effort level** (unless the prompt already states it): **Essential · Standard (Recommended) · Polished · All-out**, each explained in one line.
3. Then ask what's missing, **one question per message**, with **2–4 options tailored to the prompt**, each explained in one plain line, the best one marked **(Recommended)**, plus a free answer. Use the question tool if available.
4. The first question always offers **"Skip the questions — you decide everything."** If chosen (or the user says "don't ask"), stop and pick the best defaults from this skill; list them afterwards.
5. If the user shares a reference site or screenshot, follow `references/inspiration-and-reference-sites.md` §2.

### 1.2 Effort levels decide the depth
| Level | In short |
|---|---|
| **Essential** | Clean, consistent, correct — nothing extra |
| **Standard** | Complete professional design in the chosen style, all states, subtle motion |
| **Polished** | Premium: typography craft, hover/scroll motion, dark mode, imagery direction, full review |
| **All-out** | Everything: research, brand, many screens/flows, advanced motion, deep accessibility & localization, assets |

**The floor — every level, never skipped:** consistent tokens (§3), foundation components with their states (§4), color rules and contrast, core laws (§2: hierarchy, one primary action, proximity, Fitts, Hick, Jakob), the accessibility minimum (§5), a Decision Log, and DESIGN.md after approval. The full level-by-level table is in the workflow file §2. Stay inside the chosen level; offer the next level in one line at the end.

### 1.3 Design
0. **Concept** — one sentence describing the experience through a metaphor, plus the one signature element (`references/creative-direction.md`). At Polished/All-out, write the one-page brief first (`references/design-brief-and-metrics.md`) and, at All-out, show 2–3 divergent directions to choose from.
1. **Foundations (§3)** from the answers; apply the chosen style's overrides (§9.1).
2. **Components (§4)** from those foundations only — no one-off values.
3. **Laws (§2)** + matching page/flow pattern (`references/page-and-flow-patterns.md`) + platform rules (`references/platforms-and-devices.md`).
4. **Modern layer (§7)** only at the depth the effort level allows, after the screen works without it.
5. **Pre-ship checklist (§8)**, then visual verification and review (`references/quality-review.md`) as the level requires.

### 1.4 Document every decision (Decision Log)
Never just say "I used X". With every draft, show the key decisions (5–8 rows in chat; the full log goes into DESIGN.md):

| Decision | Choice | Why | Source |
|---|---|---|---|
| Style | Minimal | Productivity app, user wants focus | User |
| Accent color | #2F5BEA | Calm, trustworthy, 5.2:1 on white | Default (Minimal) |
| Body font | Inter 16px | Highly readable at small sizes | Default |

### 1.5 Changes and add-ons — change only what was asked
- **Change request:** restate it in one line; if vague ("make it pop"), ask one question with 2–4 explained interpretations; change **only** that part; if it breaks a [Rule], say so and propose the smallest fix; log it.
- **Add-on request** ("now add animations", "add dark mode", "translate to Hindi"): **look it up again in this skill** (routing table in the workflow file §4), ask 1–2 short questions (where / how strong), add only that using existing tokens, verify, update the log and DESIGN.md.

### 1.6 Approve → create DESIGN.md
When the user approves ("looks good", "approved", "go ahead"), create **`DESIGN.md`** from `references/design-md-template.md`. From then on it is the source of truth: read it before any future work on this product and update it (with a changelog line) whenever the design changes.

### 1.7 Don't overwhelm
One question per message; short explanations; no internal file names or labels in replies; compact Decision Log; reply length matches the effort level; visual previews over long descriptions; offer next steps in one line.

### 1.8 Adapt to the agent environment
DENT runs in many agents; use what the environment offers and never pretend otherwise.
- **Questions:** use the agent's multiple-choice question tool if it has one; otherwise numbered options in plain text. In non-interactive runs (no user to answer, e.g. CI or a batch task), don't ask: use the "don't ask" defaults (workflow file §5) and list them.
- **Previews:** if HTML can be rendered (artifacts, browser preview, local file), show a style tile or screen preview; if images can be shown, render to PNG; otherwise ASCII wireframe + hex codes, and say it isn't visually verified (`references/tooling-and-handoff.md` §1).
- **Verification:** use browser/screenshot tools when available (`references/quality-review.md` Part 1); never claim visual verification you didn't do.
- **Files:** write `DESIGN.md` at the project root (or where the user says). If you can't write files, output it in full in a code block.

### 1.9 Never
- Never ship a [Rule] violation (contrast, targets, focus, keyboard, color-alone, reduced motion) — in any style or level.
- Never design deceptive patterns (`references/persuasion-and-ethics.md`), even when asked; offer the honest alternative.
- Never copy a specific existing product's look, logo, illustrations or copy 1:1; take principles, not pixels.
- Never use fake social proof (invented testimonials, logos, user counts) — use clearly marked placeholders.

---

## 2. Proven principles and laws

### Perception — Gestalt principles [Law]
- **Proximity** — things close together are read as a group. Spacing is the primary grouping tool; use it before borders or boxes.
- **Similarity** — things that look alike (color, shape, size) are read as related. Same function → same look; different function → visibly different.
- **Common region** — things inside a shared boundary (card, panel) are read as a group.
- **Continuity** — the eye follows lines and alignments. Align to shared edges.
- **Closure** — the mind completes incomplete shapes; you rarely need every border.
- **Figure/ground** — users must instantly tell content from background (key for modals, overlays, cards).
- **Common fate** — things that move together are read as related (use in motion).
- **Prägnanz (simplicity)** — people read complex visuals in the simplest form possible. Prefer simple shapes and layouts.

### Interaction and cognition [Law]
- **Fitts's Law** — time to hit a target depends on its size and distance. Make primary actions big and close to where attention/pointer already is; put frequent actions within thumb reach on mobile; screen edges and corners are easy targets on desktop.
- **Hick's Law** — decision time grows with the number and complexity of choices. Reduce options per step, highlight a recommended option, use progressive disclosure.
- **Miller's Law / working-memory limits** — people hold only a few chunks in mind at once (classic 7±2; modern estimates closer to ~4). Use it to justify **chunking** (phone numbers, grouped settings), not as a hard cap on menu items.
- **Jakob's Law** — users spend most of their time on other products and expect yours to work the same way. Follow platform and web conventions for navigation, icons, form behavior and gestures unless you have a strong reason not to.
- **Tesler's Law (conservation of complexity)** — every system has complexity that can't be removed, only moved. Move it to the system, not the user.
- **Doherty Threshold** — productivity rises sharply when the system responds in under ~400ms. Keep interactions fast or give instant feedback.
- **Nielsen response-time limits** — ~0.1s feels instant; ~1s keeps flow of thought (show subtle feedback); ~10s is the attention limit (show progress and allow cancel).
- **Von Restorff (isolation) effect** — the item that differs stands out and is remembered. Give each screen ONE visually distinct primary action. If everything is emphasised, nothing is.
- **Serial position effect** — first and last items in a list are remembered best. Put key nav items at the ends.
- **Aesthetic-usability effect** — attractive designs are perceived as easier to use and earn more tolerance for small issues. Polish matters, but it does not fix real usability problems.
- **Peak-end rule** — experiences are judged by their most intense moment and their end. Invest in key moments and in completion/success states.
- **Goal-gradient effect** — motivation rises as people near a goal. Show progress in multi-step flows.
- **Zeigarnik effect** — unfinished tasks are remembered. Progress indicators and checklists encourage completion (don't abuse it).
- **Postel's Law** — be liberal in what you accept, strict in what you output. Accept varied input formats (phone numbers, dates) and normalise them.

### Usability heuristics — Nielsen's 10 [Law, widely validated]
1. Visibility of system status
2. Match between system and the real world
3. User control and freedom (undo, cancel, back)
4. Consistency and standards
5. Error prevention
6. Recognition rather than recall
7. Flexibility and efficiency of use (shortcuts for experts)
8. Aesthetic and minimalist design
9. Help users recognise, diagnose and recover from errors
10. Help and documentation

### Visual design fundamentals (CRAP) [Convention, foundational]
- **Contrast** — differences must be clearly different, not slightly different.
- **Repetition** — reuse the same styles to build consistency.
- **Alignment** — every element aligns to something. No arbitrary placement.
- **Proximity** — related things close, unrelated things apart.

---

## 3. Foundations (design tokens)

Define these as named tokens first. Every component uses only tokens.

### Color
- **Default palette (when the user gives no colors):** use three colors with fixed roles: **Dominant** (~60%, backgrounds and main surfaces), **Complement** (~30%, text, icons, borders, secondary surfaces) and **Off color** (~10%, the accent for primary actions, links and highlights). Ten ready-made, contrast-checked palettes (5 light, 5 dark) are in `references/color.md` Part 2. They are optional: use them only as a fallback. Scales, harmony, dark mode and color theory: `references/color.md` Part 1.
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

## 4. Components — consistent specs

**The core rule [Law: similarity + consistency heuristic]:** every instance of a component looks and behaves the same across the whole product. A button on the settings screen and a button on the checkout screen of the same variant and size are identical. To guarantee this, each component is defined ONCE as a spec with fixed parameters, and every screen reuses that spec. No screen-level overrides.

The numbers below are **[Convention]** defaults. Change them per project or per aesthetic style, but once chosen they apply everywhere. Values marked **[Rule]** don't change.

### 4.1 Shared control tokens (define these first)

"Controls" = anything the user types into or presses: buttons, inputs, selects, chips, segmented controls. They share these tokens so they line up when placed side by side.

| Parameter | Default | Notes |
|---|---|---|
| Control height | sm 32 · **md 40** · lg 48 px | On touch-first products, make md = 44–48. |
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
| Hit area | **[Rule]** ≥ 44×44 touch, ≥ 24×24 pointer (WCAG 2.2) | Extend invisibly with padding if the visual is smaller. |

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
- **[Rule]** Focus moves into the dialog, is trapped inside, Esc closes (unless destructive in-progress), focus returns to the trigger on close.

**Drawer / bottom sheet**
- Side drawer 320–400px wide; bottom sheet with a 32×4px drag handle and container radius on top corners only.

**Menus / popovers**
- Container radius, overlay elevation, 4–8px offset from trigger, item height as in 4.5.

**Tooltips**
- Caption text (12–13px), padding 6×10px, small radius (4–6px), high-contrast background (inverted colors).
- Appear after ~300–500ms hover / on focus; disappear on mouse-out/Esc. No interactive content inside.

### 4.18 Feedback components
- **Toasts/snackbars:** same screen position every time (e.g. bottom-center mobile, bottom-left/right desktop); max one action ("Undo"); success/info auto-dismiss after ~4–6s, **errors stay until dismissed**; **[Rule]** announced to screen readers (live region).
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

---

## 5. Accessibility — minimum bar [Rule]

- Color contrast as in §3.
- **Touch/click targets:** Apple HIG 44×44pt; Material 48×48dp; WCAG 2.2 minimum 24×24 CSS px (2.5.8). Default to 44–48.
- Visible focus indicator on every interactive element; logical keyboard order.
- All functionality available via keyboard on web.
- Semantic structure: real headings in order, buttons are buttons, links are links, form fields have labels.
- Text alternatives for meaningful images and icon-only buttons.
- Don't rely on hover alone to reveal essential information or actions.
- Errors identified in text and described with how to fix them.

Deeper: full WCAG 2.2 AA checklist, component ARIA patterns, cognitive/motor/vision guidance — `references/accessibility.md`.

---

## 6. Content (UX writing)

- **[Convention]** Front-load the important words; people scan, they don't read.
- **[Convention]** Use the user's words, not internal jargon (heuristic 2).
- **[Convention]** Be specific: "Password must be 8+ characters" beats "Invalid input".
- **[Convention]** Consistent terms everywhere — don't call the same thing "Projects" in one place and "Workspaces" in another.
- **[Convention]** Error messages: say what happened, why, and what to do next. No blame.

Deeper: voice & tone, style rules, microcopy library, inclusive language — `references/ux-writing.md`.

---

## 7. The modern layer — what makes a design feel modern

A modern design is not a style; it is **craft on top of solid foundations**. Every technique here is a multiplier: on a good structure it makes the product feel premium, on a weak structure it makes the problems louder. Apply this layer last.

### 7.0 Ground rules for the whole modern layer
- **Purpose first [Law: aesthetic-usability effect cuts both ways].** Every effect must do at least one job: show hierarchy, explain a change, give feedback, guide attention, or express the brand. If it does none, remove it.
- **Restraint is the signature of modern design.** One or two "hero" moments per page or screen. Everything else is quiet and fast.
- **Consistency [Law: similarity].** Motion, hover and typography behaviors are tokens too. The same kind of thing always moves and reacts the same way.
- **[Rule] Performance:** effects never block input or drop frames. Animate only `transform` and `opacity` (and `filter` sparingly). Never animate `width`, `height`, `top`, `left`, `margin` or `box-shadow` directly on large or many elements.
- **[Rule] Reduced motion:** every non-essential animation has a reduced-motion version (fade or no motion). See 7.9.
- **Progressive enhancement:** the product works and looks good with effects off. Effects are added on top, never required to read or use content.

---

### 7.1 Custom and expressive typography

Typography is the single biggest driver of a modern look. Most of a screen is text.

**Choosing typefaces**
- Pair a **characterful display face** (headings, hero, numbers) with a **highly readable text face** (body, UI). Or use one well-designed family with wide weight range for both.
- Prefer **variable fonts**: one file, every weight/width, smooth weight animation, better performance than many static files.
- Choose fonts with good **tabular figures** for data, real **italics**, and enough weights (at least 400, 500, 600/700).
- Avoid the default-everywhere choice when the product needs identity; a distinctive font choice is the cheapest way to not look templated.

**Craft details that read as "modern"**
- **Large type, tight tracking:** big headings (40px+) usually need negative letter-spacing (about −1% to −3%); small text (≤ 13px) and all-caps labels need positive tracking (+2% to +8%).
- **Tight heading line-height:** 1.0–1.2 for display sizes; body stays 1.4–1.6.
- **Strong scale contrast:** a big jump between hero/heading and body creates hierarchy at a glance (Von Restorff). Don't use many sizes that are only slightly different.
- **Weight contrast** instead of extra sizes: e.g. 600 heading vs 400 body.
- **Balanced line breaks:** `text-wrap: balance` for headings (no single orphaned word); `text-wrap: pretty` for paragraphs.
- **Tabular numbers** in tables, prices, timers, counters: `font-variant-numeric: tabular-nums` so digits don't jitter.
- **Optical sizing:** use `font-optical-sizing: auto` when the font supports it.
- **Correct typographic characters:** real quotes (" "), apostrophes ('), en/em dashes (– —), ellipsis (…), × for dimensions.

**Fluid type (scales smoothly with screen width)**
```css
/* min size, preferred (viewport-relative), max size */
h1   { font-size: clamp(2.25rem, 1.5rem + 3vw, 4.5rem); }
body { font-size: clamp(1rem, 0.95rem + 0.25vw, 1.125rem); }
```
- **[Rule]** Always include a `rem` part so text still scales with the user's zoom/font settings (WCAG 1.4.4). Never pure `vw`.

**Font loading**
- Use `font-display: swap` (or `optional` for non-critical fonts), preload the 1–2 critical files, subset to needed characters, and set fallback font metrics (`size-adjust`) so text doesn't jump when the font loads (layout shift).

**Typography as a visual element**
- Oversized headings, outline or mixed-weight words, text masked over images, and kinetic (animated) type can be hero moments. Use for **one** headline per page, never for body content, and keep it readable.

---

### 7.2 Motion system (fluid motion)

Motion that feels "fluid" comes from three things: **the right easing, the right duration, and continuity** (things move from where they were to where they go, rather than appearing/disappearing).

**Why motion helps [Law]:** animated transitions help people track what changed and where things went (object constancy), reducing the cognitive cost of a change. Badly used, motion distracts and slows people down.

**Duration tokens** [Convention]
| Token | Duration | Used for |
|---|---|---|
| instant | 50–100ms | color/opacity on hover, press feedback |
| fast | 150–200ms | small elements: toggles, checkboxes, tooltips, icon swaps |
| normal | 250–300ms | menus, dropdowns, cards expanding, tab indicators |
| slow | 350–500ms | modals, drawers, large panels, page sections |
| page | 400–700ms | full-page / route transitions, hero entrances |

- Bigger distance or bigger element → longer duration. Small UI never takes longer than ~300ms.
- Exits are ~20–30% faster than entrances (people want the old thing gone quickly).
- Frequent actions get the shortest (or no) animation; rare, meaningful moments get more.

**Easing tokens** [Convention]
```css
--ease-out:       cubic-bezier(0.16, 1, 0.3, 1);   /* entering, expanding — fast start, soft landing */
--ease-in:        cubic-bezier(0.7, 0, 0.84, 0);   /* exiting — gentle start, quick finish */
--ease-in-out:    cubic-bezier(0.65, 0, 0.35, 1);  /* moving between two on-screen positions */
--ease-standard:  cubic-bezier(0.2, 0, 0, 1);      /* general UI default */
```
- **Never `linear`** for UI movement (only for spinners, progress, and continuous loops).
- Real objects don't start or stop instantly; easing is what makes motion feel physical.

**Springs** (for drag, gestures, playful/premium feel)
- Springs feel more natural than fixed curves for interactive motion because they keep the user's velocity (a flick continues smoothly).
- Typical: quick, almost no bounce for UI (damping ratio ~0.8–1.0, response ~0.3–0.5s); a small bounce (~0.6–0.75) only for playful, celebratory or physical elements.
- Use springs for: dragging, swiping, sheets, reordering, pull-to-refresh, toggles on mobile. Use curves for: fades, color changes, simple reveals.

**Choreography**
- **Stagger** lists and grids: 20–50ms between items, max ~8–10 items staggered (then show the rest together), total under ~500ms.
- **Order:** container first, then content; the most important element arrives first.
- **Direction is meaning:** forward/deeper = from right or from below; back/up a level = reverse. Keep it consistent across the product.
- **Small distances:** entrances move 8–24px, not across the screen. Combine with opacity (fade + slight move) for the classic modern reveal.
- **Scale subtly:** pop-ins from 0.95–0.98 to 1, not from 0.

**Continuity techniques**
- **Shared-element transitions:** a thumbnail grows into the detail view instead of the screen cutting. On web: View Transitions API (`view-transition-name`); in apps: shared element / matched geometry; libraries: FLIP technique.
- **Layout animation:** when items are added, removed or reordered, the others slide to their new places instead of jumping.
- **Morphing:** a button expanding into a panel, an icon morphing (play ↔ pause, menu ↔ close).
- **Animate numbers:** counters roll to the new value; charts animate from previous to new data, not from zero every time.

---

### 7.3 Micro-interactions

Small responses to user actions; they make a product feel alive and confirm that something happened [Law: visibility of system status].

Structure every micro-interaction as **trigger → rules → feedback → loop/end**.

Good uses:
- **Press feedback:** buttons scale to ~0.97–0.98 on press (fast, 100ms) and return on release.
- **Toggle/checkbox:** check mark draws in, thumb slides with a slight squash.
- **Success moments:** a check mark animation or subtle confetti at the *end* of meaningful flows (Peak-end rule) — not on every save.
- **Copy to clipboard:** icon morphs to a check for ~1.5s.
- **Like/favourite:** quick scale bounce + color fill.
- **Inline validation:** a gentle shake (±4–6px, 2–3 cycles, ~300ms) on wrong input, plus the text message **[Rule: not motion alone]**.
- **Optimistic UI:** show the result instantly (item appears, like count increments) and reconcile with the server after; roll back with a message if it fails. Feels faster than any spinner (Doherty threshold).

---

### 7.4 Hover animations (pointer devices)

**[Rule]** Hover is an enhancement, never the only way to see information or reach an action (touch devices have no hover). Wrap hover effects so they only apply to real pointers:
```css
@media (hover: hover) and (pointer: fine) {
  .card:hover { transform: translateY(-2px); }
}
```

**Good hover effects** (pick a small set and use them consistently):
| Element | Effect | Timing |
|---|---|---|
| Buttons | background shift (~8%), optional tiny lift or icon nudge (→ moves 2–4px) | 100–150ms |
| Cards (clickable) | lift 2–4px + slightly stronger shadow, or border/tint change; image inside zooms to ~1.03–1.05 with overflow hidden | 200–300ms |
| Links | underline grows/slides in, or thickness change | 150–200ms |
| Icons/icon buttons | tinted circular background appears | 100–150ms |
| Images/media | subtle zoom, overlay with title/action fades in (action must also be reachable without hover) | 250–400ms |
| Nav items | indicator/pill slides to hovered item | 200–250ms |

**Expressive hover (use sparingly, hero areas only):**
- **Spotlight/glow:** a soft radial highlight follows the cursor inside a card or border.
- **Magnetic buttons:** button moves a few px toward the cursor (max ~6–10px).
- **Tilt/3D:** card rotates a few degrees toward the cursor (max ~5–8°).
- **Custom cursor:** only on creative/portfolio sites; never hide the system cursor in apps or forms, and keep it fast (no lag).

Rules:
- Hover-in can be a bit slower than hover-out; hover-out should feel instant (~100ms).
- Don't move the element away from the cursor or change its size enough to cause flicker at the edges.
- Add a short delay (~100–200ms) before hover opens menus/previews, so passing over things doesn't trigger them.

---

### 7.5 Scroll animations

Scroll is the main interaction on websites and long app screens. Used well, it tells a story; used badly, it fights the user.

**[Rule] Never scroll-jack:** don't override scroll speed, direction or distance, or force snapping through content the user wants to skim. The user controls the scroll.

**Good scroll techniques**
- **Reveal on enter:** sections/items fade in and rise 16–24px when they enter the viewport. Trigger once, early (when ~10–20% visible), duration 400–600ms, stagger children. Content must be readable even if the animation never runs.
- **Scroll-linked progress:** reading progress bar, header that shrinks/condenses or gains a background after scrolling, step indicators.
- **Sticky storytelling:** a pinned visual on one side changes as text sections scroll past (product tours, features). Keep each step short.
- **Subtle parallax:** background layers move at a slightly different speed (10–30% difference). Large parallax causes motion sickness — keep it subtle and disable under reduced motion.
- **Horizontal scroll sections:** only for galleries/carousels the user expects to swipe; always show that more content exists (peek the next item).
- **Scroll snap:** for carousels, onboarding pages, full-screen media — not for regular reading pages.
- **Hide/reveal header:** header hides on scroll down and returns on scroll up (more space for content, always reachable).
- **Back-to-top** button appears after ~2 screens of scroll on long pages.

**Implementation**
- Prefer **CSS scroll-driven animations** (`animation-timeline: view()` / `scroll()`) or **IntersectionObserver** over scroll event listeners (better performance).
```css
@media (prefers-reduced-motion: no-preference) {
  .reveal {
    animation: reveal linear both;
    animation-timeline: view();
    animation-range: entry 10% cover 30%;
  }
}
@keyframes reveal { from { opacity: 0; translate: 0 24px; } to { opacity: 1; translate: 0 0; } }
```
- Don't animate everything that enters: headings and key visuals yes; every paragraph and every icon no.
- Never delay important content (prices, CTAs, form fields) behind long animations.

---

### 7.6 Depth, surface and texture

Modern designs use **soft, layered depth** instead of hard lines.

- **Layered shadows:** combine 2–3 shadows (a tight one for contact + a large soft one for ambient) at low opacity for realistic elevation. Shadows tinted with the background hue look better than pure black.
- **Subtle borders on dark mode:** shadows are hard to see on dark backgrounds; use a 1px light border at low opacity (~6–12%) and lighter surfaces for elevation.
- **Inner highlights:** a 1px top inner light line on raised elements (buttons, cards) adds a premium "lit from above" feel.
- **Background blur (glass):** `backdrop-filter: blur()` for nav bars, sheets and overlays above content. **[Rule]** Text on glass must still meet contrast — add a semi-opaque tint behind it. Use on a few surfaces, not everywhere (expensive to render).
- **Gradients:** soft, low-contrast gradients (mesh or radial) for hero backgrounds and accents; gradient text only on short display headings. Use smooth color spaces (`in oklch`) to avoid muddy middles.
- **Grain/noise:** a very subtle noise overlay (2–5% opacity) removes the flat "digital" look and hides gradient banding.
- **Radius hierarchy:** nested radii are concentric (inner = outer − padding), containers rounder than controls (see 4.1).

---

### 7.7 Layout patterns that read as modern

- **Generous whitespace** and a clear max width; let content breathe [Law: proximity].
- **Bento grids:** content in a grid of differently sized rounded tiles; size reflects importance. Keep consistent gaps and radii.
- **Big, confident hero:** one clear headline, one supporting line, one primary CTA, one strong visual. Not five messages.
- **Asymmetry with a grid underneath:** offset layouts look dynamic but still snap to the column grid.
- **Edge-to-edge media** mixed with contained text columns.
- **Fluid, intrinsic layouts:** `clamp()` for spacing, CSS grid with `auto-fit/minmax`, **container queries** so components adapt to their container, not just the screen.
- **Sticky, context-aware UI:** sticky headers, sticky action bars on mobile (primary action always reachable — Fitts's Law), sticky table headers.

---

### 7.8 Modern interaction patterns

- **Command palette (⌘K / Ctrl+K):** search-everything + actions for power users (heuristic 7: flexibility and efficiency).
- **Keyboard shortcuts** for frequent actions, discoverable in tooltips and menus.
- **Instant search / filter-as-you-type** with debounced queries (~150–300ms).
- **Inline editing** instead of separate edit pages where possible.
- **Undo instead of "Are you sure?"** for reversible actions (heuristic 3: user control and freedom).
- **Skeleton loading + optimistic UI** instead of full-page spinners.
- **Smart defaults and autofill** (Tesler's Law: take the complexity onto the system).
- **Gestures on mobile:** swipe actions on rows, pull to refresh, swipe-to-dismiss sheets — always with a visible alternative.
- **Dark mode + system theme** support, switching smoothly (no flash of the wrong theme on load).

---

### 7.9 Reduced motion and accessibility for the modern layer [Rule]

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```
- Under reduced motion: replace movement with simple fades or instant changes; remove parallax, auto-playing motion, zoom and large slides. Keep essential feedback (state changes) visible.
- **[Rule]** Anything that moves automatically for more than 5 seconds (carousels, background video, looping animations) needs a pause/stop control (WCAG 2.2.2).
- **[Rule]** No flashing more than 3 times per second (WCAG 2.3.1).
- Motion never carries meaning alone — pair with text/icon change.
- Focus states stay visible during and after animations; animations must not move focused elements off-screen.

---

### 7.10 Performance budget for the modern layer

- Target **60fps** (16ms per frame); interactions respond within ~100ms (and INP < 200ms on web).
- Animate `transform` and `opacity` only; use `will-change` only on elements about to animate, then remove it.
- Limit simultaneous animations; pause off-screen animations and videos.
- Avoid layout shift (CLS): reserve space for images, fonts and late content.
- Heavy effects (WebGL, 3D, large videos, many blurs) only where they are the point of the page, lazy-loaded, with a static fallback.
- Test on a mid-range phone, not only a fast laptop.

---

### 7.11 Anti-patterns (things that look "modern" but hurt)

- Everything fades/slides in on scroll — the page feels slow and the user waits for content.
- Long or bouncy animations on frequent actions (opening a menu 50 times a day).
- Scroll-jacking, forced smooth-scroll overrides, or sections that trap the scroll.
- Hover-only actions or information.
- Low-contrast "aesthetic" grey text, or text on busy glass/gradients.
- Too many fonts, sizes or effects competing; multiple "hero" moments on one screen.
- Custom cursors or loading screens that delay usage.
- Motion that ignores reduced-motion settings.
- Effects that drop frames on normal phones.

---

## 8. Pre-ship checklist

Run this before presenting any design.

**Hierarchy and clarity**
- [ ] Can you tell the single most important action on each screen within ~5 seconds?
- [ ] Exactly one primary action per view/section.
- [ ] Grouping is clear from spacing alone (squint test).

**Consistency**
- [ ] All colors, sizes, spacing, radii and shadows come from tokens — no one-off values.
- [ ] Same element = same appearance and behavior everywhere.
- [ ] Every component follows its spec in §4 — same height, padding, radius, border, font and state colors on every screen.
- [ ] Buttons and inputs in the same row share height and radius; checkboxes and radios share size.
- [ ] Follows platform/web conventions unless deliberately deviating.

**Accessibility**
- [ ] Text and UI contrast meet AA.
- [ ] Targets ≥ 44px (or platform equivalent).
- [ ] Focus states visible; keyboard path works.
- [ ] Meaning never carried by color alone.
- [ ] Reduced-motion respected.

**States and edge cases**
- [ ] Empty, loading, error and success states designed.
- [ ] Hover, focus, active, disabled states for every interactive element.
- [ ] Long text, missing images, zero/one/many items handled.

**Responsiveness**
- [ ] Works at mobile, tablet and desktop widths.
- [ ] Body line length stays within ~45–75 characters.

**Modern layer**
- [ ] Every animation/effect has a clear purpose (hierarchy, change, feedback, attention, brand).
- [ ] Durations and easings come from the motion tokens; no `linear` UI movement.
- [ ] Hover effects are pointer-only and nothing depends on hover.
- [ ] No scroll-jacking; key content isn't delayed by reveal animations.
- [ ] Reduced-motion version works; auto-moving content can be paused.
- [ ] Only `transform`/`opacity` animated; smooth on a mid-range phone; no layout shift.
- [ ] Typography craft applied: tracking, heading line-height, balanced wraps, tabular numbers.

**Content**
- [ ] Button labels describe outcomes.
- [ ] Error messages explain how to fix.
- [ ] Realistic content (no lorem ipsum, no invented testimonials or logos presented as real).

**Distinctiveness**
- [ ] The concept sentence explains the main color, type and motion choices.
- [ ] At least one signature element is present; nothing from the "default look" list (`references/creative-direction.md` §6) is there by accident.
- [ ] In an existing codebase: no second design system introduced; new values added as tokens in the existing convention.

---

## 9. Aesthetic styles and reference files

### 9.1 Applying an aesthetic style (override rules)
1. Find the style in **`references/styles/_styles-index.md`** (by name, alias, or the user's feeling words). Open only that style's file.
2. The style's **Overrides** table **replaces** the matching [Convention] defaults in this file (colors, fonts, spacing step, radius, borders, depth, motion, hover, imagery, component looks). Anything the style doesn't mention keeps this file's default.
3. **[Rule]s are never overridden** — contrast, target sizes, focus, not-color-alone, reduced motion, keyboard access. Each style file's "Accessibility watch-outs" gives the fix where that style tends to break a rule.
4. **[Law]s still apply** — a style changes *how* hierarchy looks, not whether there is hierarchy.
5. The style's **Signature moves** must be present, or the style isn't there.
6. Platform rules keep native navigation and gestures; the style changes the look on top.
7. Combining: one base style + at most one accent style (see the index).
8. Record the style and its overrides in the Decision Log and DESIGN.md.

### 9.2 Reference files (read only what the task needs)

| File | Read when |
|---|---|
| `references/workflow-questions-and-effort.md` | Every design task: questions, effort levels, change/add-on routing, "don't ask" defaults |
| `references/modes-existing-products.md` | Redesign, audit/review, or working inside an existing codebase / UI library |
| `references/design-md-template.md` | The user approves → create DESIGN.md |
| `references/creative-direction.md` | Concept, signature element, composition, divergent directions, avoiding the generic/AI look |
| `references/design-brief-and-metrics.md` | Brief (Polished+), JTBD, success metrics, measurement, A/B tests |
| `references/inspiration-and-reference-sites.md` | User shares a reference site/screenshot; looking for inspiration or component examples |
| `references/styles/_styles-index.md` + one style file | A look is named or described, or one must be picked (41 styles) |
| `references/color.md` | Colors: scales, harmony, dark mode, accessible color, default palettes |
| `references/typography.md` | Choosing/pairing fonts, type scale ratios, line heights, font stacks and loading |
| `references/design-tokens-and-code.md` | Token architecture/naming/export; building the design in code (HTML, Tailwind, React, Flutter, SwiftUI, Compose…) |
| `references/page-and-flow-patterns.md` | Landing, pricing, dashboard, onboarding, auth, forms, checkout, settings, search, lists, empty/error states, navigation, modals, notifications, AI/chat/agents, mobile patterns |
| `references/components-extended.md` | Components beyond §4: accordion, breadcrumbs, pagination, stepper, date picker, file upload, search, command palette, OTP, tag input, carousel, tree, advanced tables, kanban, calendar, timeline, editor toolbar, empty state… |
| `references/complex-product-patterns.md` | Workspaces, roles, billing, notification center, audit log, versions, collaboration, offline, bulk/import/export, admin, security & privacy UX; blog, docs, changelog, careers, 404, legal, comparison, waitlist pages |
| `references/tooling-and-handoff.md` | Previews in agent environments, Figma, Storybook, developer handoff, design QA |
| `references/platforms-and-devices.md` | iOS, Android, web, desktop, tablet, watch, TV, car, voice, AR/VR, sound & haptics |
| `references/industry-playbooks.md` | Product is in a specific industry (fintech, health, e-commerce, SaaS, education, gov…) |
| `references/data-visualization.md` | Charts, KPIs, tables, dashboards |
| `references/accessibility.md` | Accessibility beyond the minimum (Polished/All-out, or on request) |
| `references/internationalization.md` | Other languages, RTL, Indic/CJK scripts, locale formats |
| `references/ux-writing.md` | Copy, voice & tone, microcopy |
| `references/icons-illustration-and-imagery.md` | Icon sets, custom icons, illustration style, photography and art direction |
| `references/brand-identity.md` | Logo, brand basics, mini brand when none exists |
| `references/assets-and-marketing-graphics.md` | Favicons, app icons, OG images, splash screens; social posts, print, slides, ads, email |
| `references/research-and-information-architecture.md` | Personas, journeys, flows, usability testing, sitemaps, navigation structure |
| `references/persuasion-and-ethics.md` | Conversion design; checking for deceptive patterns (never design them) |
| `references/quality-review.md` | Verifying what was built (screenshots) and reviewing design quality / anti-patterns |

To extend the skill: new styles go in `references/styles/` following `_style-template.md` and get a row in `_styles-index.md`; new topics get their own reference file plus a row in the table above and in the add-on routing table.

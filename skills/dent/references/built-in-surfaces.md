# Built-in surfaces: nothing ships with a default look by accident

**Built-in surfaces** are the parts of an interface the browser or OS draws for you: tooltips, scrollbars, range sliders, checkboxes, radios, switches, dropdowns, the text-selection highlight, the text caret, placeholders, autofill highlights, file-input buttons, progress bars, disclosure markers, dialog backdrops, validation bubbles. Left alone they show the OS defaults: a blue checkbox on an orange brand, a grey scrollbar on a dark theme, a yellow system tooltip from a `title` attribute. That mismatch is one of the fastest tells that an interface wasn't designed (`creative/anti-slop.md`).

This file decides **how each surface should look** and when to ask. **How to build it** comes from Modern Web Guidance (`modern-web-guidance.md`): start with `mwg:browser-ui-theming`, then the surface's own guide (§4). MWG's principle applies throughout: theme the native control with CSS first, and rebuild a control only when CSS can't reach the design, because a rebuilt control loses semantics, keyboard handling, IME and assistive-tech support for free.

Used by `/dent:surfaces`, `/dent:create`, `/dent:polish`, `/dent:extend`, `/dent:system` and the recipes.

---

## 1. The rule [Rule]

1. **Every built-in surface present in the deliverable gets a deliberate level**: **Match**, **Tint** or **Native** (§2), recorded in DESIGN.md (Built-in surfaces section) and the Decision Log. "Native" is a valid choice when chosen; "native because nobody thought about it" is a defect that fails G8.
2. **One level for the product**, with per-surface exceptions written down (e.g. Match everywhere, but native date pickers on mobile).
3. **Never** use a `title` attribute for information people need: it can't be styled, doesn't appear on touch or keyboard focus, and disappears on hover-out. Use a designed tooltip or toggletip (`mwg:interest-triggered-tooltips`).
4. **Never** trade accessibility for looks: styled surfaces keep native semantics, keyboard behaviour, ≥ 3:1 non-text contrast (thumb vs track, control vs background), ≥ 4.5:1 text contrast, visible focus, forced-colors support, and touch targets (§3, `accessibility.md`).
5. **Never** make scrollbars thinner than `auto` unless another accessible way to scroll exists (MWG); "match" changes their colours, not their size.

---

## 2. Ask (one question, Standard effort and above)

Ask for any visual build at **Standard+**, after colours and light/dark and before motion (`workflow-questions-and-effort.md` §3), unless the user already said. Use the question tool; one option recommended:

> **How should the browser's built-in pieces look: tooltips, scrollbars, sliders, checkboxes, dropdowns, text highlight and so on?**
> - **Match my design everywhere (Recommended)**: styled with your colours, type, corners and motion, so nothing looks like a default.
> - **Brand tint only**: your accent colour on native controls, themed scrollbars and highlight; native shapes stay.
> - **Keep the native platform look**: familiar OS controls; best for internal tools and OS-like apps.
> - **Let me choose per element**: then ask one multi-select of the groups to Match: Tooltips & popovers · Scrollbars · Form controls (checkbox, radio, switch, slider, select, file) · Text (selection, caret, placeholder, autofill).

**Recommend** Match for marketing sites, consumer apps and anything brand-led; Tint for dense internal or enterprise tools where speed and familiarity matter; Native for desktop-like or OS-integrated apps, or when the user's design system says so.

**Don't-ask defaults:** Essential → **Tint**. Standard and above → **Match**. Existing product → whatever it already does, consistently (Match if it already styles some surfaces; don't leave a mix).

**Add-on requests** ("the tooltip looks default", "make the scrollbars match", "the slider looks off", "style the checkboxes") → run `/dent:surfaces` for the surfaces mentioned and check their siblings: fixing one tooltip and leaving the scrollbar grey is still a mismatch.

---

## 3. Surface tokens

Derive every surface from DESIGN.md's semantic tokens; never pick new colours for them. Define both themes.

| Token | Derive from | Must meet |
|---|---|---|
| `--tooltip-bg`, `--tooltip-text` | Inverted surface (text colour as background) or the style's overlay surface | Text ≥ 4.5:1; caption text style; small radius; overlay elevation; motion `fast` |
| `--scrollbar-thumb`, `--scrollbar-track` | Thumb: border-strong or muted text; track: surface or transparent | Thumb ≥ 3:1 against track; forced-colors fallback (`mwg:adapt-scrollbar-to-contrast-preferences`) |
| `--control-accent` | Brand accent (the primary action colour) | ≥ 3:1 against the page background (MWG: don't trust the browser to fix contrast) |
| `--range-track`, `--range-fill`, `--range-thumb`, `--range-thumb-size` | Track: subtle border; fill: accent; thumb: accent or surface with an accent ring | Thumb target ≥ 24 px (44 on touch); fill and thumb ≥ 3:1 against track |
| `--selection-bg`, `--selection-text` | Accent at a light tint, or accent with on-accent text | Selected text ≥ 4.5:1 |
| `--caret` | Accent (or text colour on accent-heavy styles) | Visible on the field background (≥ 3:1) |
| `--placeholder` | Muted text | ≥ 4.5:1 (it is text); never the only label |
| `--autofill-ring` | Accent or info colour | Keep the browser's autofill tint (users recognise it) and add the ring; no layout shift (`mwg:autofill-highlight-inputs`) |
| `--scrim` | Existing overlay scrim token | Backdrop of modal dialogs and drawers |
| `--focus` | Existing focus token | Unchanged on every styled surface |

Put them in the token file next to the component tokens (`design-tokens-and-code.md` Part 1 §3).

---

## 4. Surface inventory: what each level means

| Surface | Match | Tint | Native watch-outs | Build with |
|---|---|---|---|---|
| **Tooltip** (hover/focus hint) | Designed tooltip: tokens above, caption type, delay, entry motion, edge-aware placement; toggletip on touch | Same component, default token values | `title` tooltips are never acceptable for needed info | `mwg:interest-triggered-tooltips`, `mwg:position-aware-tooltips` |
| **Info popover / hover card** | Container radius, overlay elevation, style's surface | Default tokens | Must be reachable by keyboard and touch | `mwg:hovercard`, `mwg:menu` |
| **Scrollbars** (page and scroll containers) | Thumb/track colours per theme; per-surface colours for dark panels and code blocks | Accent-tinted thumb | Never thinner than `auto` without another scroll method; hidden scrollbars need a visible "more" hint | `mwg:customize-scrollbar-color-and-thickness`, `mwg:scrollability-affordance-hints` |
| **Range slider** | Custom track, active fill, thumb shape from the style, value label in the DOM | `accent-color` only (UA-dependent) | Value must be visible or announced (`aria-valuetext`) | `mwg:slider` |
| **Checkbox / radio** | Drawn with the control radius and stroke weight, animated check | `accent-color` | Keep the native input; style via `appearance` | `mwg:checkbox`, `mwg:brand-consistent-forms` |
| **Switch** | Track and thumb per `foundations-and-components.md` §4.8 | `accent-color` | Takes effect immediately | `mwg:switch` |
| **Select / dropdown** | Customizable select: field matches inputs, picker uses the menu spec, option states, entry motion | Field styled, native picker | Mobile native pickers are often better: a logged exception is fine | `mwg:branded-select-styling`, `mwg:custom-select-picker-layouts`, `mwg:animated-select-picker` |
| **Text selection** | Brand tint + readable text | Brand tint | Don't disable selection on content text | `mwg:browser-ui-theming` |
| **Caret** | Accent caret | Accent caret | — | `mwg:browser-ui-theming` |
| **Placeholder** | Muted token, same font | Muted token | Never a label substitute | `mwg:forms` |
| **Autofill** | Browser tint kept + token ring | Browser default | No layout shift; focus still distinct | `mwg:autofill-highlight-inputs` |
| **Validation** | Inline messages in the design (error token, icon, text); browser bubbles replaced | Inline messages | Validate after interaction | `mwg:validate-input-after-interaction`, `mwg:forms` |
| **File input** | Button styled as the secondary button; drop zone per `components-extended.md` §6 | Button styled | Keep the native input for keyboard and AT | `mwg:browser-ui-theming` |
| **Progress, meter, spinner** | Track/fill/shape from tokens; reduced-motion version | `accent-color` | Determinate vs indeterminate states | `mwg:progress`, `mwg:progress-ring`, `mwg:spinner` |
| **Disclosure marker** (`<details>`) | Custom marker that rotates per motion tokens | Default marker tinted | No headings inside `summary` | `mwg:accordion` |
| **Dialog backdrop** | Scrim token, blur only if the style uses glass | Scrim token | — | `mwg:dialog`, `mwg:animate-to-from-top-layer` |
| **Date, time, colour inputs** | Field styled like text inputs; calendar from a library only if the design needs it | Field styled, native picker | Native pickers are better on mobile | `components-extended.md` §5, `mwg:support-global-calendar-systems` |
| **Links** | Underline colour, thickness and offset from tokens | Tinted underline | Never colour alone | `mwg:custom-text-decorations` |
| **Browser chrome** | `theme-color` per theme, `color-scheme`, favicon set | `color-scheme` + `theme-color` | Needed at every level once dark mode exists | `mwg:browser-ui-theming`, `mwg:dark-mode`, `assets-and-marketing-graphics.md` |
| **System dialogs** (`alert`, `confirm`, `prompt`) | Never: always a designed `<dialog>` | Same | — | `mwg:dialog` |

Library components follow the same rule: never ship a library's default look (`catalog/component-selection.md` §5).

---

## 5. Style personalities

A surface should look like it belongs to the chosen style (`styles/_styles-index.md`). Examples; derive the rest from the style's Overrides and tokens:

| Style | Tooltip | Scrollbar | Controls |
|---|---|---|---|
| Minimal / Swiss | Ink on paper, square-ish, no arrow | Hairline-coloured thumb, transparent track | Thin strokes, square checkboxes |
| Editorial | Serif caption, paper tone | Ink thumb on paper track | Underlined selects, classic radios |
| Neo-brutalism | Hard 2 px border, offset shadow | High-contrast thumb | Thick borders, square, offset shadow on press |
| Glassmorphism | Translucent tint with readable backing | Translucent thumb with a contrast backing | Frosted track, bright thumb |
| Dark tech / Terminal | Monospace, accent border | Dim thumb, near-black track | Mono labels, accent fills |
| Luxury | Small caps, generous padding, slow fade | Gold-toned thumb | Fine strokes, restrained motion |
| Retro OS | Bevelled system-style tooltip (custom, not native) | Bevelled thumb drawn in the style | Bevelled 3D controls |
| Playful / Memphis | Rounded, coloured, bouncy entry | Accent thumb | Chunky rounded controls, spring checks |

---

## 6. Build order

1. **Inventory** the surfaces actually present: `python scripts/verify_page.py <page> --surfaces match` lists them, or scan the code for the elements in §4.
2. **Tokens** (§3) in both themes.
3. **Retrieve** the MWG guide for each surface (§4) and build; keep native elements underneath.
4. **States** for every surface: default, hover (pointer only), focus-visible, active, checked/indeterminate, disabled, error, autofilled, and reduced motion.
5. **Surface sheet**: one page or Storybook story that renders every built-in surface in every state, light and dark. It is the evidence for G8 and part of the component sheet (`/dent:system`).

---

## 7. Verify

- `python scripts/verify_page.py <page> --surfaces match|tint|native` reports which surfaces are present, which are styled, any `title` tooltips and thin scrollbars, and sets gate **G8_surfaces** to Failed when the chosen level isn't met.
- Look at the surface sheet in light, dark and forced colors (Chrome DevTools rendering emulation), at phone width with touch (toggletips), and by keyboard (slider arrows, select type-ahead, focus rings).
- Contrast: thumb vs track ≥ 3:1, control accent vs background ≥ 3:1, selection text and placeholder ≥ 4.5:1 (`scripts/contrast.py`).

---

## 8. Native apps

iOS, Android and desktop: keep platform controls and tint them (`tintColor`/`accentColor`, Material `ColorScheme`, WinUI accent); customise only where the platform supports it; keep system scroll indicators; use platform tooltips (macOS help tags, `TooltipCompat`, WinUI `ToolTip`) styled where allowed. Platform rules: `platforms-and-devices.md`.

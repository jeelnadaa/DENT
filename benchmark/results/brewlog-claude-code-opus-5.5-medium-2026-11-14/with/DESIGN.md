# DESIGN.md — Brewlog marketing site

Source of truth for `index.html`. Read before changing anything; add a changelog line on every change.

## 1. Direction
- **Concept:** a home barista's grid-paper notebook: pencil numbers, red-pen circles around the cup that finally tasted right.
- **Mood:** curious, precise, warm. **Anti-words:** moody, slick.
- **Category cliché avoided:** espresso brown + orange, steam icons, dark moody photos. Divergence on colour (paper / blue-black ink / red pen / highlighter), imagery (data + notes, no photos) and layout (grid paper, margin annotations).
- **Base style:** Editorial (serif display, rules, numbered kickers). **Accent:** Hand-Drawn (Caveat notes, marker highlight, wobbly card border, red-pen circles).
- **Signature:** the red-pen circle around the best result: hero word "twice", best cluster in the Insights chart, Pro trend point. Plus the highlighter swipe on one phrase per section.

## 2. Tokens (CSS custom properties in `:root`)
| Role | Light | Dark |
|---|---|---|
| `--paper` | #FAFAF5 | #11151B |
| `--card` | #FFFFFF | #1A2029 |
| `--ink` | #1C2430 (14.9:1) | #E9EDF3 (15.6:1) |
| `--pencil` (secondary text) | #5B6573 (5.6:1) | #A3ADBB (8.1:1) |
| `--rule-strong` (input/control borders) | #7D8794 (3.5:1) | #6E7989 (4.2:1) |
| `--red` (accent text) | #B8322A (5.7:1) | #FF8A7A (8.0:1) |
| `--cta-bg / --cta-fg` | #B8322A / #FFF (5.95:1) | #FF8A7A / #11151B (8.0:1) |
| `--focus` | #1F5BD8 (5.7:1) | #7FA8FF (7.8:1) |
| `--marker` | yellow 85% | yellow 26% |
Type: Fraunces (display), Instrument Sans (UI/body), JetBrains Mono (numbers, tabular), Caveat (short annotations only). Fluid scale `--step--1…4` with `clamp()`. Spacing 4px base `--s-1…9`. Radius: 4/8/14 + `--wobble`. Motion: `--ease-out`, `--d-fast 140ms`, `--d-base 240ms`, `--d-slow 700ms`.

## 3. Components
Buttons (primary red / secondary ink outline / ghost), icon button 44×44, tag, notebook card (`.note`), billing toggle (`button[aria-pressed]`), WAI-ARIA tabs (arrow/Home/End keys), native `<details>` accordion, form field (label above, hint, inline error with icon, `aria-invalid`, `aria-describedby`), password show/hide (`aria-pressed`), plan radio cards, error summary (`role=alert`, focusable links), success panel (focus moves to heading).

## 4. Motion
| Animation | Purpose | Reduced motion |
|---|---|---|
| Hero rise + red circle draws round "twice" | Entrance; points at the promise | Shown instantly |
| Margin note fades in after the card | Reads as a note written afterwards | Shown instantly |
| Insights chart dots plot, ring draws | The one storytelling moment: pattern emerges | Final state |
| Tab panel slide-in, price swap, FAQ +/× rotate | State change feedback | Instant |
| Submit spinner, success tick draws | System status | Static |
Only `opacity`, `transform`, `stroke-dashoffset` are animated. No sound (not on-brand for a marketing page; nothing autoplays).

## 5. Content rules
- No invented proof: no user counts, ratings, testimonials, logos. Mockups are labelled "Example entry" / "Screens show example data".
- Free-plan recipe limit was not specified → written as "limited", never a number.
- One CTA label: "Start logging free". Pro CTA reflects billing: "Choose Pro monthly/yearly", and preselects the plan in the form.
- Yearly maths: $6 × 12 = $72; $60/yr saves $12 = $5/month.

## 6. Licences
| Asset | Source | Licence |
|---|---|---|
| Fraunces, Instrument Sans, JetBrains Mono, Caveat | Google Fonts | SIL Open Font License 1.1 |
| Icons, logo, favicon, illustrations, charts | Hand-made inline SVG in this file | Project-owned |
No libraries, images or audio.

## 7. Known gaps
- No OG/Twitter image: the brief forbids external files (text meta tags are present).
- No legal pages or contact address exist; the footer carries a true privacy note about the form instead of dead links.
- Sign-up has no backend (by brief); success state is client-side.

## Changelog
- 2026-11-14 — v1: initial build (DENT All-out pipeline: plan → direction → create → verify → score → improve).

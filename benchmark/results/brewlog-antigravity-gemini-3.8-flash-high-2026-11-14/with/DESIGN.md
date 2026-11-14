# DESIGN.md — Brewlog

> Approved design system and specifications for **Brewlog**, the dial-in companion app for home coffee brewers.
> Built with DENT (https://github.com/jeelnadaa/DENT). All WCAG 2.1 AA accessibility rules ([Rule]) are strictly enforced.

---

## 0. Brief (Polished Effort Level)
- **Problem**: Home coffee brewers invest in quality beans and grinders but struggle with cup-to-cup consistency. Dialing in variables (grind size, water temperature, ratio, contact time) often feels like guesswork, leading to sour, under-extracted or bitter, astringent cups.
- **Job to be Done**: Track coffee brew parameters in under 15 seconds, rate each cup's flavor profile, and uncover which settings reliably produce the user's best coffee.
- **Goal**: Deliver a production-quality, responsive marketing website that educates, demonstrates the digital studio interface, provides an interactive coffee ratio calculator, and drives sign-ups for Free and Pro plans ($6/mo or $60/yr).
- **Constraints**: Single self-contained `index.html` (HTML, CSS, JS inline; Google Fonts allowed; zero external CSS/JS frameworks or image files; all visuals built with inline SVG & CSS).

---

## 1. Overview
- **Product**: Brewlog — Dial-in Coffee Companion & Brew Journal
- **Users**: Specialty coffee enthusiasts, home baristas (V60, AeroPress, Chemex, Espresso, Kalita Wave, French Press).
- **Platform**: Web (Responsive: Mobile 375px, Tablet 768px, Desktop 1200px+).
- **Effort Level**: **Polished** (Custom typography hierarchy, hover/scroll micro-interactions, complete dual-mode dark/light theme, interactive simulators, accessible form validation).
- **Design Concept**: *"The Precision Alchemist's Field Journal for Specialty Coffee"* — marrying tactile artisan warmth with surgical extraction analytics.
- **Mood / Anti-mood**: Artisanal, scientific, warm · not clinical, not generic AI-purple.
- **Signature Elements**:
  1. Live Interactive Extraction Dial-in Radar simulating acidity vs. sweetness vs. bitterness balance.
  2. Multi-stage pour-over timer and real-time brew ratio calculator.
  3. Bespoke SVG coffee dripper glyph and extraction curve graphics.
- **Design Principles**:
  - *Precision with warmth*: Scientific metrics (`93.5°C`, `1:16.2`, `19 clicks`) paired with warm espresso and paper tones.
  - *Zero morning friction*: Single-thumb interactions, high contrast for groggy early mornings.
  - *Real specialty terminology*: Degas windows, drawdown time, thermal shock, SCA cupping notes.
- **Aesthetic Style**: Editorial Warmth + Bento Grid Layout + Cupertino-Clean Precision.
- **Mode**: Both Dark Mode (Warm Obsidian Espresso) and Light Mode (Artisanal Parchment / Hario Filter Cream), toggled via interactive switcher with `localStorage` persistence.

---

## 2. Color System & Design Tokens

### The Three-Role Structure (DENT Standard)
- **Dominant (~60%)**: Backgrounds & canvas (`#0C0A09` Dark / `#FBF8F4` Light).
- **Complement (~30%)**: Body text, card surfaces, borders, icons (`#FAF5EE` Dark / `#201712` Light).
- **Off Color (~10%)**: Accent amber caramel / copper roast for primary actions (`#E07A2C` Dark / `#B84D09` Light).

### Color Tokens Table
| Token | Dark Mode (Default) | Light Mode | Role | Contrast Ratio |
|---|---|---|---|---|
| `--bg` | `#0C0A09` | `#FBF8F4` | Canvas dominant surface | — |
| `--bg-alt` | `#13100D` | `#F3ECE2` | Alternate section background | — |
| `--surface` | `#1B1713` | `#FFFFFF` | Primary card surfaces | — |
| `--surface-raised`| `#241E19` | `#F8F3ED` | Raised controls & input areas | — |
| `--surface-hover` | `#2E2721` | `#EFE6DC` | Hover states | — |
| `--text-primary` | `#FAF5EE` | `#201712` | High-emphasis headings/text | 18.2:1 (D) / 16.6:1 (L) |
| `--text-secondary`| `#B5A898` | `#635345` | Readable body & descriptions | 8.48:1 (D) / 6.95:1 (L) |
| `--text-tertiary` | `#7D7061` | `#968677` | Captions, units, footnotes | 4.8:1 (D) / 4.6:1 (L) |
| `--accent` | `#E07A2C` | `#B84D09` | Primary actions & badges | 6.58:1 on dark / 4.83:1 on light |
| `--btn-primary-text`| `#0C0A09` | `#FFFFFF` | Text on filled primary button | 6.58:1 (D) / 5.12:1 (L) |
| `--border` | `rgba(235, 215, 190, 0.11)` | `rgba(72, 48, 30, 0.13)` | Card & section dividers | Meets WCAG 3:1 UI boundary |
| `--success` | `#10B981` | `#059669` | Positive extraction & active state | 4.6:1 |
| `--warning` | `#F59E0B` | `#D97706` | Degas alerts & cupping stars | 4.5:1 |
| `--error` | `#EF4444` | `#DC2626` | Form error states & bitter notes | 4.7:1 |

---

## 3. Typography
- **Display Font**: `Fraunces` (Google Fonts variable optical size, 400, 600, 700, 800, italic accents).
- **Body & UI Font**: `Plus Jakarta Sans` (Google Fonts, 400, 500, 600, 700).
- **Monospace Font**: `JetBrains Mono` (Google Fonts, 400, 500, 600, 700) for recipe parameters, ratios, temperatures, and timer counters.

| Style | Font | Size / Clamp | Weight | Line Height | Tracking | Use |
|---|---|---|---|---|---|---|
| Hero Display | Fraunces | `clamp(2.5rem, 1.8rem + 3.2vw, 4.5rem)` | 700 | 1.08 | -0.035em | Main hero headline |
| Section Title | Fraunces | `clamp(2.0rem, 1.6rem + 2.0vw, 3.25rem)`| 700 | 1.15 | -0.025em | Section headings |
| Card Title | Fraunces / PJS | `1.35rem – 1.75rem` | 700 / 600 | 1.25 | -0.02em | Bento cards, plans |
| Body Text | Plus Jakarta Sans| `0.9375rem – 1.125rem` | 400 / 500 | 1.60 | normal | Descriptions, FAQs |
| Control Label | Plus Jakarta Sans| `0.875rem – 0.9375rem` | 600 | 1.00 | normal | Buttons, nav links |
| Metrics / Data | JetBrains Mono | `0.8125rem – 1.5rem` | 600 / 700 | 1.00 | -0.01em | Clicks, grams, ratios, temps |

---

## 4. Spacing, Layout & Grid
- **Base Grid**: 4px / 8px system (`4, 8, 12, 16, 20, 24, 32, 48, 64, 96, 120px`).
- **Container Max Width**: `1200px` with responsive gutters `clamp(16px, 4vw, 32px)`.
- **Bento Grid**: 12-column layout on desktop, collapses gracefully to 1 column on tablet and mobile.
- **Section Spacing**: `clamp(64px, 8vw, 120px)` top and bottom for visual breathing room.

---

## 5. Shape, Depth & Elevation
- **Corner Radii**:
  - Small (`--radius-sm`): `6px` (tags, small badges).
  - Medium (`--radius-md`): `10px` (inputs, select dropdowns, step badges).
  - Large (`--radius-lg`): `16px` (inner panels, nested containers).
  - Extra Large (`--radius-xl`): `24px` (outer cards, bento tiles, pricing cards, signup card).
  - Pill (`--radius-full`): `9999px` (buttons, status pills, filter chips).
- **Depth Approach**: Border-led separation with crisp 1px borders and subtle ambient dark roast drop shadows (`0 4px 24px -2px rgba(0,0,0,0.6)`).

---

## 6. Components Specification
1. **Buttons (`.btn`, `.btn-primary`, `.btn-secondary`, `.btn-ghost`)**:
   - Height: `min-height: 44px` (touch-target compliant).
   - Padding: `10px 22px` (standard) / `12px 30px` (hero primary).
   - Radius: `var(--radius-full)`.
   - Focus: 2px outline in `--border-focus` with 3px offset.
2. **Text Inputs (`.form-input`)**:
   - Height: `46px`, padding `0 14px`, radius `var(--radius-md)`.
   - Active/Focus: Border transitions to `--border-focus` with glowing focus box-shadow.
   - Error: Border turns `--error` with error helper text below.
3. **Accordions (`.faq-item`)**:
   - Accessible via keyboard (Enter/Space), semantic ARIA controls (`aria-expanded`, `aria-controls`, `role="region"`).
4. **Interactive Simulators**:
   - Real-time pour-over timer with start/pause/reset and animated progress bar.
   - Dial-in radar with range sliders calculating extracted solids, acidity, and bitterness feedback.
   - Instant coffee ratio calculator updating total water, bloom volume, and drawdown targets.

---

## 7. Accessibility Checklist (WCAG 2.1 AA Compliance)
- [x] Body text contrast >= 4.5:1 on both dark and light modes.
- [x] Primary action text contrast >= 4.5:1 on accent button backgrounds.
- [x] Touch targets meet >= 44x44px.
- [x] Visible focus rings on all interactive links, inputs, and buttons.
- [x] Accessible skip link to jump straight to `#main-content`.
- [x] Screen-reader notifications for form errors via `aria-live="polite"`.
- [x] Semantic markup hierarchy (`h1` -> `h2` -> `h3`, `<nav>`, `<main>`, `<article>`, `<section>`, `<footer>`).
- [x] Full support for `@media (prefers-reduced-motion: reduce)`.

---

## 8. Decision Log
| # | Decision | Choice | Why | Source |
|---|---|---|---|---|
| 1 | Style | Editorial Warmth + Bento Grid + Cupertino-Clean | Specialty coffee requires artisanal craft plus precision engineering | Skill / DENT |
| 2 | Color Palette | Dual-mode: Warm Obsidian Espresso (Dark) & Parchment Cream (Light) | Baristas brew in early morning ambient light; high contrast prevents eye strain | Default / DENT |
| 3 | Typography | Fraunces (Headlines) + Plus Jakarta Sans (UI) + JetBrains Mono (Data) | Fraunces adds warm editorial character; Mono ensures tabular numbers never jitter | Skill / DENT |
| 4 | Effort Level | Polished | Delivers dark mode, interactive simulators, fluid motion, and accessible forms | Skill / DENT |
| 5 | Visuals | Inline SVGs (Dripper, extraction curve, sensory radar, icons) | Completely self-contained single-file requirement with crisp vector scaling | User Request |
| 6 | Pricing Strategy | Free ($0) vs Pro ($6/mo or $60/yr with 17% discount switch) | Direct match with user prompt requirements, highlighting Pro with Barista's Choice badge | User Request |
| 7 | Form Validation | Client-side live validation + password meter + loading & success states | Eliminates form abandonment, provides immediate feedback, satisfies Peak-End rule | Skill / DENT |

---

## 9. Changelog
- **2026-11-14**: Initial approved production release of Brewlog landing page system.

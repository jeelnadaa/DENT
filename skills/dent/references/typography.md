# Typography — Font Priority, Pairings, Scales and Font Stacks

The type basics are in `foundations-and-components.md` §3 (Typography), and the craft details in `modern-layer.md` §7.1. Hero compositions are in `creative/hero-typography.md`. This file decides **which fonts** to use: a priority list, genuinely good pairings, scale ratios, stacks and loading rules (including licences).

---

## 0. Font priority (read this first)

Fonts are the fastest way a design looks either *designed* or *default*. DENT prefers **modern grotesks with character**, in the spirit of **Satoshi**: geometric-leaning, clean, slightly warm, with distinctive details (single-storey forms, open apertures, confident bold weights), and pairs them with serifs or display faces that have real personality.

**Tier 1 — reach for these first** (free; licences in §9):

| Font | Source | Character | Best as |
|---|---|---|---|
| **Satoshi** | Fontshare | Modernist geometric grotesk, crisp and warm; the reference for DENT's taste | Body + UI, also bold headings |
| **General Sans** | Fontshare | Neo-grotesk with geometric touches, very versatile | Body, UI, headings |
| **Switzer** | Fontshare | Swiss neo-grotesk with a friendlier rhythm | Body/UI for calm, precise products |
| **Supreme** | Fontshare | Geometric grotesk with wide range of weights | UI, product marketing |
| **Cabinet Grotesk** | Fontshare | Characterful display grotesk, tight and punchy at heavy weights | Headlines, wordmarks |
| **Clash Display / Clash Grotesk** | Fontshare | Bold, sharp, contemporary display | Big headlines, launches |
| **Geist** (+ Geist Mono) | Vercel, Google Fonts | Precise Swiss-tech grotesk | Dev tools, technical products |
| **Manrope** | Google Fonts | Semi-geometric, open, modern | Body/UI (closest free Google option to Satoshi's feel) |
| **Plus Jakarta Sans** | Google Fonts | Geometric with soft, friendly details | Consumer apps, SaaS |
| **Onest** | Google Fonts | Clean geometric grotesk, excellent at small sizes | Body/UI |
| **Figtree** | Google Fonts | Clean, friendly geometric | Body/UI, onboarding |
| **Hanken Grotesk** | Google Fonts | Modern grotesk, neutral but not bland | Body/UI |
| **Instrument Sans** | Google Fonts | Neo-grotesk with width axis, precise | UI, editorial-tech |
| **Schibsted Grotesk** | Google Fonts | Editorial grotesk with character | News, editorial UI |
| **Host Grotesk**, **Funnel Sans / Funnel Display** | Google Fonts | Contemporary grotesks with distinct personalities | Modern brands |
| **Mona Sans / Hubot Sans** | GitHub, Google Fonts | Variable width + weight grotesks | Tech, expressive headings |
| **Bricolage Grotesque** | Google Fonts | Quirky, optical-size grotesk | Indie, creative, playful-modern |

**Serifs and display partners (Tier 1):**

| Font | Source | Character |
|---|---|---|
| **Gambetta** | Fontshare | Warm, sharp transitional serif; superb italics |
| **Zodiak** | Fontshare | Elegant high-contrast serif for display |
| **Erode** | Fontshare | Calm, readable serif with a contemporary edge |
| **Sentient** | Fontshare | Soft, literary serif |
| **Boska** | Fontshare | Dramatic high-contrast serif for fashion/editorial |
| **Bespoke Serif** | Fontshare | Characterful display serif |
| **Panchang** | Fontshare | Ultra-wide display sans; architectural, techy |
| **Instrument Serif** | Google Fonts | Condensed editorial display serif, beautiful italic |
| **Fraunces** | Google Fonts | Variable "wonky" soft serif (SOFT/WONK/opsz axes) |
| **Newsreader** / **Source Serif 4** | Google Fonts | Text serifs for long reading |
| **Young Serif**, **Gloock** | Google Fonts | Characterful display serifs |

**Mono partners:** Geist Mono, JetBrains Mono, IBM Plex Mono, Commit Mono, Martian Mono.

**Tier 3 — not defaults.** Use only as a deliberate, logged choice (a style or brand truly needs it):
- **Overused UI defaults:** Inter (as the only face), Roboto, Open Sans, Lato, Montserrat, Poppins, Nunito Sans, Source Sans as a first pick. They're legible but read as "default". If you need Inter's neutrality, consider Switzer, Geist or Hanken Grotesk first.
- **Cliché display faces:** Playfair Display (default "luxury"), Bebas Neue / Anton everywhere, Lobster, Pacifico, Raleway thin, Space Grotesk as the automatic "tech" choice.
- Never use more than one novelty/script face, never for UI text.

**Rules:**
1. Default body/UI choice: **Satoshi** (Fontshare). If Fontshare can't be used (offline, policy, no external fonts allowed), use **Manrope**, **Onest** or **General Sans → Hanken Grotesk** from Google Fonts or self-hosted.
2. Pick the display face **after** the concept: serif from the table above for warmth/editorial, a characterful grotesk (Cabinet Grotesk, Clash Display, Panchang) for bold/modern, or the body family in heavy weight for minimal.
3. When a style file (`styles/*.md`) or direction suggests Inter/Roboto/Poppins/Montserrat, prefer a Tier 1 font with the same role unless the style specifically depends on that face. Log the choice.
4. A strong model may choose other excellent fonts (including paid ones the user owns) under the override clause; log why.

## 1. Choosing fonts — quick method
1. **Body/UI font first:** it carries most of the text. Needs high legibility at 14–16px, open shapes, clear I/l/1 and O/0, several weights, tabular figures. Start from §0 Tier 1.
2. **Display font second** (optional): personality for headings. Contrast it with the body (grotesk + serif, or grotesk + wide/condensed display), or use the body family in a heavier weight.
3. **Limit:** 2 families (+ a monospace if needed for code/data).
4. **Check script support** for every language in scope (`internationalization.md`). Fontshare fonts are mostly Latin; pair with Noto for Devanagari, Arabic, CJK.
5. **Check the licence** (§9) before shipping.
6. **Test** with real content at real sizes, in light and dark. Render 2–3 candidate pairings side by side in a style tile and choose by eye.

## 2. Classification (what each kind feels like)
| Kind | Examples (preferred first) | Feel | Use |
|---|---|---|---|
| Modern grotesk with character | **Satoshi, General Sans, Switzer, Supreme, Manrope, Onest, Figtree, Hanken Grotesk** | Clean, modern, warm-precise | UI, SaaS, startups, most products |
| Neo-grotesque (neutral) | Geist, Instrument Sans, Schibsted Grotesk (Inter, Arimo as fallbacks) | Neutral, precise | Swiss, minimal, dev tools |
| Display grotesk | **Cabinet Grotesk, Clash Display, Clash Grotesk**, Funnel Display, Bricolage Grotesque, Mona Sans (wide) | Bold, contemporary, punchy | Headlines, launches, wordmarks |
| Wide / extended display | **Panchang**, Unbounded, Mona Sans (wdth 125) | Architectural, techy | Hero type, posters |
| Humanist sans | Source Sans 3, Fira Sans, Atkinson Hyperlegible | Warm, highly readable | Public services, accessibility-first |
| Rounded sans | Nunito, Quicksand, Fredoka, Baloo 2 | Soft, playful | Kids, playful, clay |
| Text serif | **Gambetta, Erode, Sentient**, Newsreader, Source Serif 4, Literata, EB Garamond | Literary, trustworthy | Reading, editorial |
| Display serif | **Zodiak, Boska, Bespoke Serif, Instrument Serif, Fraunces**, Young Serif, Gloock, DM Serif Display | Elegant, expressive | Headlines, editorial, premium |
| Didone (high contrast) | Boska, Bodoni Moda | Fashion, luxury | Large display only |
| Slab serif | Zilla Slab, Roboto Slab | Sturdy, retro | Vintage, bold headings |
| Monospace | Geist Mono, JetBrains Mono, IBM Plex Mono, Commit Mono, Martian Mono | Technical | Code, data, labels |
| Script/handwritten | Caveat, Kalam | Personal, casual | Accents only |
| Decorative | Bungee, Monoton, Press Start 2P | Thematic | One headline or logo only |

## 3. Pairing library (genuinely good combinations)

Ordered by how often they fit. Weights are starting points.

| # | Display / headings | Body / UI | Mood | Fits |
|---|---|---|---|---|
| 1 | **Cabinet Grotesk** 800 (tight tracking) | **Satoshi** 400/500 | Bold, modern, confident | Product launches, SaaS, agencies, Neo-brutalism |
| 2 | **Gambetta** 500 (italic accents) | **Satoshi** | Warm, editorial-modern | Consumer apps, food, lifestyle, Kissaten/Herbarium directions |
| 3 | **Clash Display** 600 | **General Sans** | Punchy startup | Launch pages, events, Dark Tech |
| 4 | **Zodiak** 400–700 | **General Sans** | Premium editorial | Fintech-premium, Luxury, Editorial |
| 5 | **Erode** 500 | **Switzer** | Calm, trustworthy | Health, public services, Corporate done well |
| 6 | **Instrument Serif** (italic for one word) | **Satoshi** | Elegant tech | AI products, portfolios, Premium Product |
| 7 | **Panchang** 700 (wide) | **Satoshi** / Geist Mono labels | Architectural, technical | Hardware, dev tools, Utilitarian, Blueprint |
| 8 | **Boska** 500 | **Switzer** | Fashion, dramatic | Luxury, fashion, Monolith |
| 9 | **Fraunces** (SOFT 100, opsz 144) | **Satoshi** or Manrope | Warm, characterful | Wellness, food, education |
| 10 | **Geist** 600 | **Geist** + Geist Mono | Precise developer | Dev tools, docs, Dark Tech, Terminal accents |
| 11 | **Sentient** 500 | **Supreme** | Literary product | Reading, notes, publishing tools |
| 12 | **Bricolage Grotesque** 700 (opsz) | **Instrument Sans** | Indie, playful-modern | Creative tools, community, Riso Club |
| 13 | **Mona Sans** (wdth 125, 800) | **Hubot Sans** / Mona Sans | Tech-expressive | Developer brands, launches |
| 14 | **Satoshi** 900 (one family) | **Satoshi** 400 | Minimal, confident | Minimal, Swiss-lite, tools |
| 15 | **Newsreader** (display opsz) | **Onest** | Calm reading | News, long-form, Lab Notebook |
| 16 | **Young Serif** | **Figtree** | Friendly vintage | Vintage, cafés, playful brands |
| 17 | **Funnel Display** | **Funnel Sans** | Fresh, rounded-modern | Consumer apps, playful SaaS |
| 18 | **EB Garamond** | **Switzer** | Academic-modern | Dark Academia, education |
| 19 | **Fredoka** / Baloo 2 | **Nunito** | Playful, kids | Playful, Toybox, Claymorphism |
| 20 | **Mukta / Anek / Noto** | Same family | Multilingual | Products in Indian languages (Fontshare Latin faces don't cover Indic scripts) |

How to choose between them: match the **mood** to the concept sentence, then render the top 2–3 in the style tile with the real headline and a paragraph of real body copy.

## 4. Type scale ratios
| Ratio | Name | Steps from 16px (body) | Use |
|---|---|---|---|
| 1.125 | Major second | 16, 18, 20, 23, 26 | Dense apps, dashboards |
| 1.2 | Minor third | 16, 19, 23, 28, 33, 40 | **Most UIs (default)** |
| 1.25 | Major third | 16, 20, 25, 31, 39, 49 | Content sites, apps with marketing |
| 1.333 | Perfect fourth | 16, 21, 28, 38, 50, 67 | Marketing, editorial |
| 1.5 | Perfect fifth | 16, 24, 36, 54, 81 | Bold landing pages, posters |
| 1.618 | Golden ratio | 16, 26, 42, 68, 110 | Expressive heroes only |

Round to whole pixels, then adjust by eye. Smaller ratios on mobile, larger on desktop (fluid `clamp()` between them).

## 5. Recommended line heights and tracking
| Text | Line height | Letter spacing |
|---|---|---|
| Display (48px+) | 0.95–1.1 | −2% to −4% (Cabinet/Clash/Satoshi bold like −3%) |
| Headings (24–40px) | 1.15–1.3 | −1% to −2% |
| Body (15–18px) | 1.45–1.6 | 0 (Satoshi/General Sans read well at 0 to +0.5%) |
| Small/caption (12–14px) | 1.4–1.5 | 0 to +1% |
| All-caps labels | 1.2–1.4 | +4% to +10% |
| Indic / Thai / Arabic | +0.1–0.2 vs Latin | 0 (no tracking on Indic) |

Line length 45–75 characters (≈ 60–70ch ideal) for body text.

## 6. Font stacks (fallbacks)
```css
--font-sans: "Satoshi", "General Sans", "Manrope", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif;
--font-display: "Cabinet Grotesk", "Satoshi", system-ui, sans-serif;           /* or a serif from §0 */
--font-serif: "Gambetta", "Newsreader", Georgia, "Times New Roman", "Noto Serif", serif;
--font-mono: "Geist Mono", "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
--font-system: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;       /* fastest, native feel */
```
Add per-script fallbacks when needed, e.g. `"Noto Sans Devanagari"` after the Latin font.

## 7. Font loading checklist
- [ ] Only the weights/styles used (variable font if many weights).
- [ ] `font-display: swap` (or `optional` for decorative fonts).
- [ ] Preload the 1–2 fonts used above the fold (same-origin files only; preloading from `file://` or cross-origin without CORS fails).
- [ ] Fallback metrics adjusted (`size-adjust`, `ascent-override`) to avoid layout shift.
- [ ] **OFL / Google Fonts:** subsetting and self-hosting are allowed.
- [ ] **Fontshare (ITF Free Font License):** **do not subset, convert formats or modify** the files (the licence forbids it). Use the files as downloaded (they include WOFF2) or the Fontshare CSS API.
- [ ] **Public repositories, templates and open-source projects:** don't commit ITF/Fontshare font files (redistribution through public servers isn't allowed). Load them from the Fontshare API, or document "download Satoshi from fontshare.com" and fall back gracefully.

Loading Fontshare fonts:
```html
<link rel="preconnect" href="https://api.fontshare.com" crossorigin>
<link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=satoshi@400,500,700&f[]=cabinet-grotesk@800&display=swap">
```
Font IDs are the lowercase hyphenated names (`general-sans`, `clash-display`, `cabinet-grotesk`, `switzer`, `gambetta`, `zodiak`, `erode`, `panchang`…); check the family page on fontshare.com for exact IDs and weights.

## 8. Common typography mistakes
- Defaulting to Inter/Roboto/Poppins/Montserrat for everything (reads as "template"; see §0).
- Pairing two fonts that are too similar (two neutral grotesks) or that fight (two expressive displays).
- Too many sizes that are only slightly different (no clear hierarchy).
- Light (300) weights for body text, or grey body text on grey.
- Centered long paragraphs; justified text on the web (rivers of space).
- All caps for long text; fake bold/italic (font lacks the weight).
- Display fonts used for body or UI text.
- Tight line height on body text or Indic scripts (clipped marks).
- Ignoring tabular numbers in tables and prices.
- Breaking a font licence (subsetting ITF fonts, committing them to public repos).

## 9. Licences (checked)
| Source | Licence | Key terms | Status |
|---|---|---|---|
| [Fontshare](https://www.fontshare.com) (ITF) | ITF Free Font License (EULA, not open source) | Free for personal **and commercial** use in any media (web, apps, video, print, social, games); self-hosting via `@font-face` allowed; Fontshare API optional. **Not allowed:** modification (incl. subsetting and format conversion), redistribution (incl. public servers, repositories, other font sites), offering the font to third parties inside a tool/SaaS/template editor. Some Fontshare families use OFL instead: check each family page. | ✓ 2026-11-14 (licence text shipped with Satoshi) |
| [Google Fonts](https://fonts.google.com) | Mostly SIL OFL 1.1 (some Apache-2.0) | Free commercial use, modification and redistribution with the licence; can't sell the fonts alone | K |
| Geist (Vercel) | SIL OFL 1.1 | As OFL | K |
| Mona Sans / Hubot Sans (GitHub) | SIL OFL 1.1 | As OFL | K |
| Commercial foundries | Paid desktop/web/app licences | Only if the user owns the licence | — |

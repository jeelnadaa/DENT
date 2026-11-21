# Typography — Font Priority, Pairings, Scales and Font Stacks

The type basics are in `foundations-and-components.md` §3 (Typography), and the craft details in `modern-layer.md` §7.1. Hero compositions are in `creative/hero-typography.md`. This file decides **which fonts** to use: a priority list, genuinely good pairings, scale ratios, stacks and loading rules (including licences).

---

## 0. How DENT chooses fonts (read this first)

Fonts are the fastest way a design looks either *designed* or *default*. DENT has **no house font**. Earlier versions put Satoshi, Cabinet Grotesk and Clash Display first; by 2026 those, together with DM Sans, Manrope, Plus Jakarta Sans, Space Grotesk, Instrument Serif and Fraunces, had become the "not-Inter" default of AI-built sites, so a fixed favourite list was itself the problem. The method below replaces it.

1. **Concept first.** Write the concept sentence (`creative-direction.md` §1) and name the **voice** the type must have (§2): what would this product sound like if it spoke? Choose the voice, then the faces.
2. **Ask where fonts may come from** (once, with the other sourcing questions; `media-sourcing.md` §3): *Free and open fonts (Recommended)* · *I own fonts or have Adobe Fonts* · *Suggest paid fonts worth buying* · *You decide*. Never pick a paid font the user has not licensed.
3. **Search, don't recall.** Run `python scripts/fonts.py suggest --role <body|display|serif|sans|mono> [--axes wdth,opsz] [--script latin-ext,devanagari] [--fresh]` for current, well-made, less-used candidates (Google Fonts' own popularity ranks and dates), and add candidates from §2 and the free foundries in §9. A strong model may know better faces: use them and log why.
4. **Check every candidate:** `python scripts/fonts.py check "<family>" --verify` reports overuse (§0.1), Google Fonts rank, axes, weights, scripts and the verified licence.
5. **Render 2–3 pairings** with the real headline and a real paragraph, in both themes, at 320 px and 1440 px, and choose by eye. Body faces must survive 14–16 px; display faces must survive the hero.
6. **Rotate.** Never reuse the previous project's pairing in the same session or repository unless it is the same brand.
7. **Log** the faces, the voice, the source and the licence in the Decision Log and DESIGN.md.

### 0.1 The overused registry (allowed only as a logged decision)
`scripts/fonts.py` holds the list and flags these automatically:
- **First order (template defaults):** Inter as the only face, Roboto, Open Sans, Lato, Montserrat, Poppins, Nunito Sans, Source Sans as a first pick, Raleway, Arial/Helvetica, Playfair Display as "luxury", Bebas Neue / Anton / Oswald as automatic display.
- **Second order (the anti-slop picks that became slop):** Satoshi, General Sans, Switzer, Cabinet Grotesk, Clash Display/Grotesk, DM Sans, Manrope, Plus Jakarta Sans, Space Grotesk/Mono, Geist, Instrument Serif (especially one italic word in the headline), Fraunces, Bricolage Grotesque, Outfit, Sora, Urbanist, Figtree.
- **Common (Google Fonts rank ≤ 40):** fine for body text and UI, weak as the identity face.

A registry font earns its place when the brand already uses it, the project's design system ships it, a style depends on it (Material → Roboto Flex), or it is the best face for a hard constraint (script coverage, legibility); log the reason. Inter, Geist and their kin remain excellent UI faces in an existing product; this rule is about new identities.

## 1. Choosing fonts: quick method
1. **Body/UI font first:** it carries most of the text. High legibility at 14–16 px, open shapes, clear I/l/1 and O/0, at least regular + medium + bold (or a `wght` axis), tabular figures for data.
2. **Display font second** (optional): the voice. Contrast it with the body on one clear axis (serif vs sans, wide vs normal, high vs low contrast, geometric vs humanist), or use one family across sizes with `opsz`/`wdth` axes.
3. **Limit:** 2 families (+ a monospace if needed for code or data). One expressive face per page.
4. **Scripts:** check every language in scope (`internationalization.md`): `fonts.py suggest --script devanagari` (or arabic, cyrillic, greek, vietnamese…).
5. **Licence:** §9, before shipping.
6. **Test** with real content at real sizes, in light and dark; render candidates side by side in a style tile and choose by eye.

## 2. Type voices (pick the voice, then the faces)
All "Free" faces below are on Google Fonts and were confirmed as SIL OFL 1.1 in github.com/google/fonts on 2026-11-21. "Paid" faces are suggestions only when the user buys or owns them (status K: check the foundry). Ranks change; `fonts.py` has the current ones.

| Voice | Feels like | Free (Google Fonts, OFL) | Paid suggestions (K) |
|---|---|---|---|
| **Precise neutral** | Instruments, infrastructure, calm tools | Zalando Sans (+ SemiExpanded/Expanded), Mozilla Text, Stack Sans Text, Hanken Grotesk, Golos Text, Wix Madefor Text, IBM Plex Sans | Söhne (Klim), ABC Diatype (Dinamo), Graphik (Commercial Type) |
| **Characterful grotesk** | Opinionated product, a confident startup that isn't a template | Mozilla Headline (wdth), Familjen Grotesk, Special Gothic (+ Condensed/Expanded One), Host Grotesk, Epilogue, Rethink Sans, Nata Sans | GT America (Grilli Type), ABC Favorit (Dinamo), Degular (OH no Type) |
| **Wide / architectural** | Hardware, engineering, posters | Zalando Sans Expanded, Science Gothic (wdth + contrast axes), Anybody (wdth 50–150), Special Gothic Expanded One, Syne (heavy weights) | ABC Monument Grotesk (Dinamo), GT America Extended |
| **Humane / legible** | Public services, health, education, accessibility-first | Atkinson Hyperlegible Next, Inclusive Sans, Radio Canada Big, Libre Franklin, Public Sans, Lexend | Neue Frutiger (Linotype), Untitled Sans (Klim) |
| **Literary serif (reading)** | Long-form, publishing, research | Literata (opsz), Newsreader (opsz), Spectral, Source Serif 4, Libertinus Serif, Petrona, Crimson Pro | Tiempos Text (Klim), Lyon Text (Commercial Type), GT Alpina (Grilli Type) |
| **Expressive display serif** | Editorial, culture, premium with a point of view | Redaction (with its degraded 10–100 cuts), Gloock, Young Serif, Kalnia (wdth), Hedvig Letters Serif (opsz), Libre Caslon Condensed, Brygada 1918 | Canela (Commercial Type), GT Super (Grilli Type), Signifier (Klim), PP Editorial New (Pangram Pangram: free only for personal use) |
| **Didone / fashion** | Luxury, fashion, beauty | Bodoni Moda (opsz), Imbue (condensed, opsz), Libre Bodoni | High-contrast display serifs from paid foundries |
| **Slab / sturdy** | Workshops, outdoors, vintage, civic | Montagu Slab (opsz), Besley, Zilla Slab, Roboto Serif | GT Sectra (Grilli Type) |
| **Warm geometric / friendly** | Consumer apps, kids-but-grown-up, food | SUSE, Albert Sans, Parkinsans, Afacad Flux, Geologica (sharpness axis), Winky Sans | Paid geometric families (check the foundry) |
| **Technical mono** | Dev tools, data, labels, receipts | Datatype (wdth), Martian Mono (wdth), Fragment Mono, Reddit Mono, Sometype Mono, Atkinson Hyperlegible Mono, Victor Mono, IBM Plex Mono | Berkeley Mono, ABC Diatype Mono, GT America Mono |
| **Pixel / screen / bitmap** | Games, retro OS, terminals, playful tech | Doto (dot-matrix), Handjet (element axes), Bitcount, Jacquard 24, Micro 5, Tiny5, Sixtyfour, Workbench, Pixelify Sans, Silkscreen | — (Departure Mono by Helena Zhang is free outside Google Fonts, K) |
| **Hand / human** | Notes, community, personal | Mansalva, Caveat, Shantell Sans, Playpen Sans, Story Script, Winky Rough | — |
| **Multiscript** | Products in Arabic, Indic, CJK and Latin together | Fustat, Alan Sans, Firjar (Arabic + Latin); the Anek family (Anek Latin, Anek Devanagari, Anek Bangla…), Mukta, Tiro Devanagari Hindi (Indic); Noto for full coverage | Paid multi-script families (check the foundry) |

Free foundries outside Google Fonts (check each family's licence, status K): **Velvetyne** (libre/OFL experimental faces), **Collletttivo** (free/OFL contemporary faces), **The League of Moveable Type** (OFL), **uncut.wtf** (a directory of free contemporary typefaces, each with its own licence), **Fontshare** (ITF Free Font Licence; see §9 for its no-modification terms). Fontshare's Satoshi, General Sans, Switzer, Cabinet Grotesk and Clash are on the overused registry; its quieter families (Erode, Gambetta, Zodiak, Sentient, Boska, Panchang, Tanker, Chillax, Ranade, Author, Telma) remain good options.

## 3. Pairing library (starting points, not prescriptions)
Each pairing is built around a voice and avoids the overused registry. Weights are starting points; check that each face has the weights you need (`fonts.py check`).

| # | Display / headings | Body / UI | Voice | Fits |
|---|---|---|---|---|
| 1 | **Mozilla Headline** 700, condensed `wdth` | **Mozilla Text** | Characterful grotesk | Product launches, open-source tools, community |
| 2 | **Zalando Sans Expanded** 800 | **Zalando Sans** | Wide + precise | Hardware, logistics, fintech infrastructure |
| 3 | **Redaction 35** (one degraded cut for one moment) | **Redaction** + **Inclusive Sans** | Expressive serif | Journalism, civic tech, archives, justice |
| 4 | **Gloock** | **Hanken Grotesk** | Display serif + neutral | Premium consumer, editorial product pages |
| 5 | **Young Serif** | **Rethink Sans** | Warm, sturdy | Food, cafés, small businesses, craft |
| 6 | **Hedvig Letters Serif** (opsz, 400) | **Hedvig Letters Sans** | Friendly-institutional | Insurance, banking done humanely, healthcare |
| 7 | **Science Gothic** (wide, high-contrast axis) | **Golos Text** | Architectural | Engineering, aerospace, research labs |
| 8 | **Special Gothic Expanded One** | **Special Gothic** | Poster grotesk | Events, music, sport |
| 9 | **Bodoni Moda** (opsz 96) | **Albert Sans** | Didone + clean | Fashion, beauty, jewellery |
| 10 | **Imbue** (condensed) | **Epilogue** | Editorial fashion | Magazines, portfolios, galleries |
| 11 | **Kalnia** (wide, 600) | **Familjen Grotesk** | Expressive serif + quirky grotesk | Culture, festivals, indie brands |
| 12 | **Libre Caslon Condensed** | **Libre Franklin** | Classic American editorial | News, long-form, publishing |
| 13 | **Literata** (display opsz) | **Literata** (text opsz) | One-family reading | Reading apps, research, documentation |
| 14 | **Newsreader** (display opsz) | **Wix Madefor Text** | Calm reading | Newsletters, knowledge bases |
| 15 | **Montagu Slab** (opsz 144) | **SUSE** | Sturdy + friendly | Outdoor, tools, civic services |
| 16 | **Besley** 700 | **Radio Canada Big** | Clarendon warmth | Education, libraries, non-profits |
| 17 | **Anybody** (wdth 150, 900) | **Anybody** (wdth 100, 400) | One family, width as hierarchy | Sports, games, bold launches |
| 18 | **Syne** 800 | **Atkinson Hyperlegible Next** | Gallery display + legible body | Art, design schools, accessible culture |
| 19 | **Stack Sans Headline** | **Stack Sans Text** + **Fragment Mono** | Technical | Developer docs, APIs, Q&A |
| 20 | **Host Grotesk** 700 | **Host Grotesk** + **Martian Mono** labels | Precise developer | Dev tools, monitoring, CLIs |
| 21 | **Geologica** (sharp, 800) | **Geologica** (soft, 400) | One family, sharpness as hierarchy | Consumer fintech, travel, mobility |
| 22 | **Doto** (dot-matrix, one line) | **Reddit Sans** | Screen-native | Transit, displays, retro tech |
| 23 | **Brygada 1918** | **Afacad Flux** | Heritage + modern | Museums, heritage brands, wine |
| 24 | **Fustat** or **Alan Sans** | Same family | Arabic + Latin | Products in Arabic and English |
| 25 | **Anek Devanagari** (wide `wdth`) | **Anek Latin** or **Mukta** | Indic + Latin | Products in Indian languages (with **Tiro Devanagari Hindi** for literary display; other scripts: Anek Bangla, Anek Tamil…) |

How to choose: match the voice to the concept sentence, then render the top 2–3 in the style tile with the real headline and real body copy. If none fits, run `fonts.py suggest` for the role and build your own pairing on one contrast axis.

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
| Display (48px+) | 0.95–1.1 | −2% to −4% for grotesks at heavy weights; serifs and wide faces usually need less (−1% to 0) |
| Headings (24–40px) | 1.15–1.3 | −1% to −2% |
| Body (15–18px) | 1.45–1.6 | 0 (text faces are spaced for 0; +0.5–1% only for tight faces) |
| Small/caption (12–14px) | 1.4–1.5 | 0 to +1% |
| All-caps labels | 1.2–1.4 | +4% to +10% |
| Indic / Thai / Arabic | +0.1–0.2 vs Latin | 0 (no tracking on Indic) |

Line length 45–75 characters (≈ 60–70ch ideal) for body text.

## 6. Font stacks (fallbacks)
Put your chosen families (§0) first; the fallbacks keep layout stable and cover scripts.
```css
--font-sans: "<body family>", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif;
--font-display: "<display family>", var(--font-sans);
--font-serif: "<serif family>", Georgia, "Times New Roman", "Noto Serif", serif;
--font-mono: "<mono family>", ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
--font-system: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;       /* fastest, native feel */
```
Add per-script fallbacks when needed, e.g. `"Noto Sans Devanagari"` after the Latin font.

## 7. Font loading checklist
- [ ] Only the weights/styles used (variable font if many weights).
- [ ] `font-display: swap` (or `optional` for decorative fonts).
- [ ] Preload the 1–2 fonts used above the fold (same-origin files only; preloading from `file://` or cross-origin without CORS fails).
- [ ] Fallback kept visually stable to avoid layout shift: `font-size-adjust` on the text matched to the web font's x-height, plus `size-adjust`/`ascent-override` on a fallback `@font-face` where needed (`mwg:visually-stable-font-fallbacks`).
- [ ] CSS type sizes in `rem`, never `px`; fluid sizes with a rem term and a max ≤ 2.5× the min (`mwg:typography`, `mwg:responsive-design`).
- [ ] **OFL / Google Fonts:** subsetting and self-hosting are allowed.
- [ ] **Fontshare (ITF Free Font License):** **do not subset, convert formats or modify** the files (the licence forbids it). Use the files as downloaded (they include WOFF2) or the Fontshare CSS API.
- [ ] **Public repositories, templates and open-source projects:** don't commit ITF/Fontshare font files (redistribution through public servers isn't allowed). Load them from the Fontshare API, or document "download <family> from fontshare.com" and fall back gracefully.

Loading Fontshare fonts:
```html
<link rel="preconnect" href="https://api.fontshare.com" crossorigin>
<link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=erode@400,500,700&f[]=panchang@700&display=swap">
```
Font IDs are the lowercase hyphenated names (`erode`, `gambetta`, `zodiak`, `panchang`, `sentient`, `tanker`…); check the family page on fontshare.com for exact IDs and weights.

## 8. Common typography mistakes
- Defaulting to a registry font (§0.1): Inter/Roboto/Poppins, or the second-order set (Satoshi, Cabinet Grotesk, Clash Display, DM Sans, Manrope, an Instrument Serif italic word…). Reads as "template" or "AI-built".
- Reusing the same pairing on every project.
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
| [Google Fonts](https://fonts.google.com) | SIL OFL 1.1 (a few Apache-2.0 or UFL) | Free commercial use, modification, subsetting and redistribution with the licence; can't sell the fonts alone | ✓ 2026-11-21 (every free face in §2–§3 confirmed in github.com/google/fonts `ofl/`; `fonts.py check --verify` repeats this per family) |
| [Velvetyne](https://velvetyne.fr), [Collletttivo](https://www.collletttivo.it), [The League of Moveable Type](https://www.theleagueofmoveabletype.com) | Mostly SIL OFL 1.1 | As OFL; check each family | K |
| [uncut.wtf](https://uncut.wtf) | Directory; each typeface has its own licence | Read the linked licence before use | K |
| [Pangram Pangram](https://pangrampangram.com) | Free trial for personal use; paid commercial licence | Never ship commercially without the paid licence | K |
| [Adobe Fonts](https://fonts.adobe.com) | Included with a Creative Cloud subscription | Web use through Adobe's kit while the subscription is active | K |
| Commercial foundries (Klim, Grilli Type, Dinamo, Commercial Type, OH no Type, Colophon, Displaay…) | Paid desktop/web/app licences | Only if the user owns the licence; never download from mirrors | K |

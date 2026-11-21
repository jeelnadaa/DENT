# Color — Theory, Scales, Dark Mode and Default Palettes

Everything about color beyond the basics in `foundations-and-components.md` §3 (Color). Part 1 is theory and systems; Part 2 is the palette method (`scripts/palette.py`) and a library of verified concept palettes.

# Part 1 — Color system

---

## 1. Color basics that matter for UI
- **Hue** (which color), **saturation/chroma** (how intense), **lightness** (how light/dark).
- **Lightness drives contrast and hierarchy** more than hue. Two different hues with the same lightness look equally prominent and can fail contrast.
- Work in a **perceptual color space** (OKLCH, or HSLuv) when generating scales: equal lightness steps *look* equal. In plain HSL, yellow at 50% lightness looks much lighter than blue at 50%.
- CSS supports it: `color: oklch(62% 0.19 260);`, mixing with `color-mix(in oklch, …)`, gradients `linear-gradient(in oklch, …)`.

## 2. Color harmony (choosing hues)
| Scheme | What | Feels | Use |
|---|---|---|---|
| **Monochromatic** | One hue, many lightness/chroma steps | Calm, cohesive | Minimal, corporate, most UIs |
| **Analogous** | Neighboring hues (±30°) | Harmonious, natural | Organic, wellness, gradients |
| **Complementary** | Opposite hues | High contrast, energetic | Accent vs base (e.g. blue UI + orange CTA) |
| **Split-complementary** | Base + two neighbors of its complement | Vivid but balanced | Playful brands |
| **Triadic** | Three evenly spaced hues | Lively | Illustrations, kids, Bauhaus/Memphis |
| **Neutral + accent** | Neutrals + one saturated color | Modern, focused | **Default for UI** |

Use harmony for brand/illustration; in UI, most surfaces should be **neutral**, with color reserved for meaning.

## 3. Color psychology (associations, culture-dependent — use as hints, not laws)
- Blue: trust, calm, tech, finance. Green: growth, health, money, success. Red: urgency, error, passion, sale (in China: luck/celebration). Orange: energy, friendly, action. Yellow: optimism, attention, warning. Purple: creativity, luxury, mystery. Pink: playful, caring. Black: luxury, power, elegance. White: clean, simple (in parts of East Asia: mourning). Brown/earth: natural, warm, reliable.
- In India: saffron/orange auspicious; red for weddings/celebration; green associated with nature/prosperity; white also with mourning.
- Check meaning for the target culture; never rely on color meaning alone.

## 4. The 60-30-10 proportion [Convention]
~60% dominant (backgrounds), ~30% secondary (text, surfaces, structure), ~10% accent (actions, highlights). In `palette.py` terms: bg/surface/raised (dominant), text/muted/border (secondary), accent/brand (the 10 %).

## 5. Building a full color scale (50–950)

Each brand/neutral color becomes an 11-step scale: 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950.

**Method (OKLCH):**
1. Put the brand color at the step whose lightness matches it (often 500 or 600).
2. Set lightness targets, e.g. 50: 97%, 100: 94%, 200: 88%, 300: 80%, 400: 70%, 500: 62%, 600: 54%, 700: 46%, 800: 38%, 900: 30%, 950: 22% (adjust per hue).
3. Keep hue roughly constant (small hue shifts make it look natural: shift slightly toward warmer in lights and cooler/deeper in darks for some hues).
4. Chroma: highest in the middle (400–600), lower at the very light and very dark ends.
5. Check contrast at the steps you'll use for text and buttons.

**Neutrals:** slightly tint greys toward the brand hue (chroma 0.005–0.02) — "warm grey" or "cool grey" — instead of pure grey; feels more cohesive.

**Usage map (light mode, typical):**
| Step | Use |
|---|---|
| 50–100 | Subtle backgrounds, hover backgrounds, selected rows |
| 200–300 | Borders, dividers, disabled backgrounds |
| 400–500 | Icons, input borders (check 3:1), decorative |
| 600–700 | **Primary buttons, links, accent text** (check 4.5:1) |
| 800–950 | Headings, body text (neutrals), dark surfaces |

**Contrast rule of thumb:** steps ~5 apart (e.g. 100 vs 600) usually reach 4.5:1; always verify.

## 6. Semantic colors
For each of success, warning, error, info define: **base** (icon/border), **subtle** (background tint), **text** (on subtle bg, ≥ 4.5:1), **on-base** (text on solid). Warnings: yellow/amber text needs dark shades. Errors never only red — add icon + message.

## 7. Dark mode done right
Dark mode is a **separate palette**, not an inversion.

- **Background:** not pure black for apps: a tinted near-black around OKLCH L 17–22 % that carries the palette's hue (`palette.py` does this). Avoid the reflex blue-grey zinc/slate (#09090B, #18181B, #0F172A) unless the brand is cool on purpose; pure black only for OLED-focused or dramatic styles.
- **Elevation = lighter surfaces.** Higher layers get lighter (bg → surface +3–4 % L → raised +4 % → overlay +4 %), same hue as the background. Shadows are barely visible; add subtle borders (white 6–12%).
- **Text:** off-white (#EDEDEF / ~90–95% lightness) for body; muted ~65–70% lightness; avoid pure #FFF large areas (glare/halation).
- **Desaturate and lighten accents:** saturated colors vibrate on dark backgrounds. Use the 300–400 steps instead of 600 (e.g. blue-400 instead of blue-600), reduce chroma slightly.
- **Re-check every contrast pair** — they all change.
- **Images & illustrations:** reduce brightness slightly or provide dark variants; transparent PNG logos may need a light version.
- **Shadows → borders and lightness.**
- **Status colors:** use lighter variants; subtle backgrounds as low-opacity tints (e.g. error at 12–16% over surface).
- **Charts:** brighter, less saturated series colors; lighter gridlines at very low opacity.
- **Respect the system setting** (`prefers-color-scheme`) and offer a toggle (System / Light / Dark) where useful. Remember the choice; avoid theme flash. On the web, build it per `mwg:dark-mode` and `mwg:dark-mode-toggle` (`color-scheme` meta + `:root` property, `light-dark()` tokens, a stored override only when it differs from the system), and support forced colors (`mwg:color`).

## 8. Accessible color checklist
- [ ] Body text ≥ 4.5:1; large text ≥ 3:1; UI components/graphics ≥ 3:1.
- [ ] Text on accent buttons ≥ 4.5:1.
- [ ] Links distinguishable from body text by more than color (underline) — or ≥ 3:1 vs surrounding text plus a non-color cue on hover/focus.
- [ ] Never color alone for meaning.
- [ ] Check color-blind simulations (protanopia, deuteranopia, tritanopia) for charts and status.
- [ ] Dark mode pairs re-checked.
- [ ] Note: APCA (the proposed WCAG 3 contrast method) gives better results for dark mode and thin fonts; use it as an extra check, but WCAG 2.x ratios remain the compliance standard today.

## 9. Gradients
- Interpolate in OKLCH to avoid grey/muddy middles (`linear-gradient(in oklch, …)`).
- Use analogous hues for smooth gradients; complementary hues pass through grey unless in OKLCH.
- Add subtle noise (2–4%) to prevent banding.
- Text on gradients: check contrast at both ends.

## 10. Tools
**DENT's own:** `scripts/palette.py make` (concept seed → accent + tinted neutral scales → light and dark role tokens, every pair contrast-checked, cliché report) and `scripts/palette.py check` (contrast + cliché report for any colours); `scripts/contrast.py` for CSS token files.

Others: contrast checkers (WebAIM, Stark), OKLCH pickers (oklch.com), scale generators (Radix Colors, Tailwind palette generators, Leonardo by Adobe — contrast-based scales), color-blind simulators (Chrome DevTools rendering emulation, Sim Daltonism).

---

# Part 2 — Palettes: method first, library second

> **Optional, not required.** Brand colours, the user's choice and the direction always win. These exist so DENT never falls back to a template palette when nobody gave it colours.

## 11. Why the old defaults were retired (v2.5)
DENT's earlier palettes (cream + ink + burnt orange, sage + copper, Tailwind violet-400 and teal-400 on near-black, acid lime on forest black) were the same palettes every "avoid the AI look" guide recommends, so they became the new AI look. The 2026 tells, all detected by `palette.py`:
- **First order:** Tailwind indigo/violet/purple (`#6366F1`, `#8B5CF6`, `#7C3AED`), indigo→purple gradients, bright blue CTAs (`#2563EB`), cyan/teal glow, emerald "fintech green", zinc/slate dark backgrounds.
- **Second order:** cream/sand paper backgrounds with terracotta or burnt-orange accents, forest green + cream "boutique", acid lime/chartreuse on black, safety orange on navy.
A hit is not banned. It must be a decision the concept explains, logged in the Decision Log, never the default.

## 12. The method (use it before the library)
1. **Start from the concept sentence, not from a mood word.** Name the real-world material or scene the concept points to ("a ship's chart room", "a darkroom under safelight") and take the colours from it: one **seed** (identity) and, if the concept has one, a **second** colour (illustration, data, highlights). Reject the first colour that comes to mind for the category (`creative/anti-slop.md` §2).
2. **Choose the neutral temperature** deliberately: `tinted` (toward the seed: cohesive, the default), `warm`, `cool` or `pure` (graphic, technical). Neutrals carry 80–90 % of the screen; they set the mood more than the accent.
3. **Generate both themes:** `python scripts/palette.py make --accent <seed> --second <hex> --neutral <temp> --name "<name>" --css`. It returns the 50–950 scales and role tokens for light and dark (`brand`, `bg`, `surface`, `raised`, `border`, `text`, `muted`, `accent`, `on-accent`, `accent-text`, `focus`, `second`), moves any role that fails WCAG along its scale, and reports clichés.
4. **Decide the colour strategy** with `../creative-direction.md` §8 (one signal colour, colour-blocked sections, tinted monochrome, full-bleed brand colour, duotone imagery). The 60/30/10 split (§4) is a starting proportion, not a rule.
5. **Look at it**: render a style tile with real content in both themes; adjust the seed's lightness/chroma by eye, then re-run step 3.
6. **Record** the seed, the strategy and every override in DESIGN.md.

Role rules for every palette (generated or not):
- **[Rule]** Text and labels ≥ 4.5:1 (`text`, `muted`, `on-accent`, `accent-text`); UI shapes and focus ≥ 3:1 against the background.
- **[Rule]** `brand` is for large decorative areas, illustration and backgrounds behind dark/light text that passes; when the seed itself fails 3:1 as a button on the background, buttons use `accent` (a darker or lighter step of the seed) and the report says so.
- **[Rule]** Semantic colours (success, warning, error, info) are separate scales (§6); never reuse the accent as the error colour.
- **[Convention]** Keep `accent` scarce: if it is everywhere it stops meaning "act here".

## 13. Library: 20 concept palettes (generated and verified with `palette.py`, 2026-11-21)
Every row passes the role contrast pairs in both themes and has no cliché hit. Pick by concept, not by product category, and treat the seed as a starting point: shift hue ±10° or chroma to make it the product's own.

### 1. Signal & Graphite
*A safety sign on a site plan.* Seeds `#F2C230` + `#2F3A45`, pure neutrals. **Good for:** tools, logistics, construction, dev utilities. **Avoid for:** calm wellness, luxury.

| Theme | brand | bg | surface | text | muted | accent | on-accent | accent-text | second |
|---|---|---|---|---|---|---|---|---|---|
| light | `#F2C230` | `#F9F9F9` | `#FFFFFF` | `#151515` | `#5B5B5B` | `#8D6F0B` | `#FFFFFF` | `#8D6F0B` | `#808C99` |
| dark | `#F2C230` | `#151515` | `#1E1E1E` | `#F9F9F9` | `#A4A4A4` | `#F2C230` | `#151515` | `#F2C230` | `#98A5B1` |

### 2. Ultramarine & Vermilion
*A primary-colour print workshop.* Seeds `#2337B8` + `#E5482D`, pure neutrals. **Good for:** education, design tools, culture. **Avoid for:** finance, health.

| Theme | brand | bg | surface | text | muted | accent | on-accent | accent-text | second |
|---|---|---|---|---|---|---|---|---|---|
| light | `#2337B8` | `#F9F9F9` | `#FFFFFF` | `#151515` | `#5B5B5B` | `#2337B8` | `#FFFFFF` | `#2337B8` | `#EA4D32` |
| dark | `#2337B8` | `#151515` | `#1E1E1E` | `#F9F9F9` | `#A4A4A4` | `#7D9EFC` | `#151515` | `#7D9EFC` | `#FD7258` |

### 3. Racing Green & Chalk
*A vintage car's paint and pinstripe.* Seeds `#1F5640` + `#C9A43B`, tinted neutrals. **Good for:** premium products, outdoor, warm finance. **Avoid for:** neon tech.

| Theme | brand | bg | surface | text | muted | accent | on-accent | accent-text | second |
|---|---|---|---|---|---|---|---|---|---|
| light | `#1F5640` | `#F6FAF8` | `#FAFFFC` | `#111614` | `#555D59` | `#1F5640` | `#FAFFFC` | `#1F5640` | `#AA850A` |
| dark | `#1F5640` | `#111614` | `#1A201D` | `#F6FAF8` | `#9EA7A2` | `#7CB098` | `#111614` | `#7CB098` | `#C19F3D` |

### 4. Oxblood & Pistachio
*A leather-bound menu at a natural-wine bar.* Seeds `#7C2033` + `#9DBB72`, tinted neutrals. **Good for:** food, hospitality, books, fashion. **Avoid for:** medical, safety-critical UI.

| Theme | brand | bg | surface | text | muted | accent | on-accent | accent-text | second |
|---|---|---|---|---|---|---|---|---|---|
| light | `#7C2033` | `#FDF8F8` | `#FFFDFD` | `#191314` | `#615859` | `#7C2033` | `#FFFDFD` | `#7C2033` | `#7A964F` |
| dark | `#7C2033` | `#191314` | `#231C1D` | `#FDF8F8` | `#ACA2A2` | `#E3828D` | `#191314` | `#E3828D` | `#93AF6A` |

### 5. Persimmon & Slate
*Autumn fruit on a grey stone table.* Seeds `#E3582B` + `#4F6C86`, cool neutrals. **Good for:** consumer apps, marketplaces, creative tools. **Avoid for:** legal, banking.

| Theme | brand | bg | surface | text | muted | accent | on-accent | accent-text | second |
|---|---|---|---|---|---|---|---|---|---|
| light | `#E3582B` | `#F6FAFC` | `#FCFEFF` | `#111619` | `#555C61` | `#E3582B` | `#111619` | `#C63C02` | `#708EAA` |
| dark | `#E3582B` | `#111619` | `#1A1F23` | `#F6FAFC` | `#9EA6AB` | `#E3582B` | `#111619` | `#E3582B` | `#8AA7C2` |

### 6. Mineral Blue & Ochre
*A geological survey map.* Seeds `#2B6A8C` + `#C38C25`, tinted neutrals. **Good for:** research, data, maps, climate, B2B. **Avoid for:** kids, nightlife.

| Theme | brand | bg | surface | text | muted | accent | on-accent | accent-text | second |
|---|---|---|---|---|---|---|---|---|---|
| light | `#2B6A8C` | `#F6FAFC` | `#FCFEFF` | `#111619` | `#555C61` | `#2B6A8C` | `#FCFEFF` | `#2B6A8C` | `#B57F0C` |
| dark | `#2B6A8C` | `#111619` | `#191F23` | `#F6FAFC` | `#9EA6AB` | `#2B6A8C` | `#F6FAFC` | `#71ABCE` | `#CD983E` |

### 7. Mulberry & Jade
*Silk and stone in a museum case.* Seeds `#8A2A62` + `#23927A`, tinted neutrals. **Good for:** beauty, culture, community. **Avoid for:** enterprise dashboards.

| Theme | brand | bg | surface | text | muted | accent | on-accent | accent-text | second |
|---|---|---|---|---|---|---|---|---|---|
| light | `#8A2A62` | `#FCF8FA` | `#FFFDFE` | `#191316` | `#60585C` | `#8A2A62` | `#FFFDFE` | `#8A2A62` | `#359F86` |
| dark | `#8A2A62` | `#191316` | `#221C1F` | `#FCF8FA` | `#ABA2A6` | `#E07EB1` | `#191316` | `#E07EB1` | `#58B79F` |

### 8. Plum & Mustard
*A 1970s record sleeve.* Seeds `#5C2D63` + `#D2A32A`, tinted neutrals. **Good for:** music, events, editorial, indie brands. **Avoid for:** healthcare, finance.

| Theme | brand | bg | surface | text | muted | accent | on-accent | accent-text | second |
|---|---|---|---|---|---|---|---|---|---|
| light | `#5C2D63` | `#FBF8FB` | `#FFFDFF` | `#171318` | `#5E595F` | `#5C2D63` | `#FFFDFF` | `#5C2D63` | `#AE8301` |
| dark | `#5C2D63` | `#171318` | `#211C21` | `#FBF8FB` | `#A8A2A9` | `#C08EC8` | `#171318` | `#C08EC8` | `#C89C2C` |

### 9. Tomato & Sky
*A summer picnic cloth.* Seeds `#DA3B2B` + `#6FA9DA`, pure neutrals. **Good for:** playful consumer, food delivery, travel. **Avoid for:** serious B2B.

| Theme | brand | bg | surface | text | muted | accent | on-accent | accent-text | second |
|---|---|---|---|---|---|---|---|---|---|
| light | `#DA3B2B` | `#F9F9F9` | `#FFFFFF` | `#151515` | `#5B5B5B` | `#DA3B2B` | `#FFFFFF` | `#CD2D1F` | `#5790C0` |
| dark | `#DA3B2B` | `#151515` | `#1E1E1E` | `#F9F9F9` | `#A4A4A4` | `#FD715E` | `#151515` | `#FD715E` | `#72A9D8` |

### 10. Moss & Lilac
*A meadow at dusk.* Seeds `#556F2A` + `#A68BD8`, tinted neutrals. **Good for:** wellness, gardening, journaling, slow tech. **Avoid for:** alert-heavy tools.

| Theme | brand | bg | surface | text | muted | accent | on-accent | accent-text | second |
|---|---|---|---|---|---|---|---|---|---|
| light | `#556F2A` | `#F8FAF6` | `#FCFEFA` | `#141611` | `#595C55` | `#556F2A` | `#FCFEFA` | `#556F2A` | `#957AC6` |
| dark | `#556F2A` | `#141611` | `#1D1F1A` | `#F8FAF6` | `#A2A69E` | `#556F2A` | `#F8FAF6` | `#93AE6C` | `#AD93DD` |

### 11. Saffron & Indigo Ink
*Marigolds and block-print ink.* Seeds `#E39516` + `#28306E`, warm neutrals. **Good for:** South Asian brands, festivals, food, education. **Avoid for:** cold enterprise.

| Theme | brand | bg | surface | text | muted | accent | on-accent | accent-text | second |
|---|---|---|---|---|---|---|---|---|---|
| light | `#E39516` | `#FCF8F5` | `#FFFDFB` | `#18140F` | `#605A53` | `#9C6610` | `#FFFDFB` | `#9C6610` | `#7685CB` |
| dark | `#E39516` | `#18140F` | `#221D18` | `#FCF8F5` | `#AAA39B` | `#E39516` | `#18140F` | `#E39516` | `#8F9EE3` |

### 12. Kelp & Brass
*A ship's chart room.* Seeds `#1F6F5C` + `#E2A33B`, tinted neutrals. **Good for:** humane fintech, maritime, sustainability. **Avoid for:** children's products.

| Theme | brand | bg | surface | text | muted | accent | on-accent | accent-text | second |
|---|---|---|---|---|---|---|---|---|---|
| light | `#1F6F5C` | `#F6FAF9` | `#FAFFFD` | `#101614` | `#545D5A` | `#1F6F5C` | `#FAFFFD` | `#1F6F5C` | `#B67E15` |
| dark | `#1F6F5C` | `#101614` | `#19201E` | `#F6FAF9` | `#9DA7A4` | `#1F6F5C` | `#F6FAF9` | `#6DB39F` | `#D19634` |

### 13. Deep Teal & Salmon
*A coral reef at depth.* Seeds `#0F5F66` + `#EE8572`, tinted neutrals. **Good for:** health, travel, science communication. **Avoid for:** dev tools.

| Theme | brand | bg | surface | text | muted | accent | on-accent | accent-text | second |
|---|---|---|---|---|---|---|---|---|---|
| light | `#0F5F66` | `#F5FAFB` | `#FAFFFF` | `#101617` | `#535D5E` | `#0F5F66` | `#FAFFFF` | `#0F5F66` | `#CE6957` |
| dark | `#0F5F66` | `#101617` | `#182020` | `#F5FAFB` | `#9CA7A8` | `#6EB0B7` | `#101617` | `#6EB0B7` | `#E78371` |

### 14. Cobalt Glaze & Porcelain
*Blue-and-white ceramics.* Seeds `#1B4C9E` + `#C7D3E8`, cool neutrals. **Good for:** publishing, archives, civic services, insurance. **Avoid for:** nightlife.

| Theme | brand | bg | surface | text | muted | accent | on-accent | accent-text | second |
|---|---|---|---|---|---|---|---|---|---|
| light | `#1B4C9E` | `#F6FAFC` | `#FCFEFF` | `#111619` | `#555C61` | `#1B4C9E` | `#FCFEFF` | `#1B4C9E` | `#808B9F` |
| dark | `#1B4C9E` | `#111619` | `#1A1F23` | `#F6FAFC` | `#9EA6AB` | `#70A3F8` | `#111619` | `#70A3F8` | `#99A4B7` |

### 15. Bottle Green & Rose Quartz
*A florist's back room.* Seeds `#1D5A45` + `#E3A2B4`, tinted neutrals. **Good for:** beauty, weddings, gifting, slow fashion. **Avoid for:** heavy-data tools.

| Theme | brand | bg | surface | text | muted | accent | on-accent | accent-text | second |
|---|---|---|---|---|---|---|---|---|---|
| light | `#1D5A45` | `#F6FAF8` | `#FAFFFC` | `#111614` | `#555D59` | `#1D5A45` | `#FAFFFC` | `#1D5A45` | `#B37688` |
| dark | `#1D5A45` | `#111614` | `#19201D` | `#F6FAF8` | `#9EA7A3` | `#79B19A` | `#111614` | `#79B19A` | `#CC8FA0` |

### 16. Darkroom
*A photo darkroom under safelight.* Seeds `#E0473A` + `#F1B24A`, warm neutrals. **Good for:** photography, film, portfolios, night use. **Avoid for:** daytime productivity.

| Theme | brand | bg | surface | text | muted | accent | on-accent | accent-text | second |
|---|---|---|---|---|---|---|---|---|---|
| light | `#E0473A` | `#FCF8F5` | `#FFFDFB` | `#18140F` | `#605A53` | `#E84E41` | `#18140F` | `#CB3127` | `#B67E11` |
| dark | `#E0473A` | `#18140F` | `#221D18` | `#FCF8F5` | `#AAA39B` | `#FB7363` | `#18140F` | `#FB7363` | `#D19732` |

### 17. Night Garden
*A glasshouse at night.* Seeds `#8FCF73` + `#C7A6F0`, tinted neutrals. **Good for:** creative tools, music, astronomy, calm night apps. **Avoid for:** finance, legal.

| Theme | brand | bg | surface | text | muted | accent | on-accent | accent-text | second |
|---|---|---|---|---|---|---|---|---|---|
| light | `#8FCF73` | `#F7FAF6` | `#FCFEFA` | `#131612` | `#585C56` | `#376D19` | `#FCFEFA` | `#376D19` | `#9979C0` |
| dark | `#8FCF73` | `#131612` | `#1C1F1A` | `#F7FAF6` | `#A1A69F` | `#8FCF73` | `#131612` | `#8FCF73` | `#B193D7` |

### 18. Ink & Amber
*A lamp-lit study.* Seeds `#F0A63A` + `#7FB2C9`, cool neutrals. **Good for:** reading, writing, research, developer docs. **Avoid for:** kids, beauty.

| Theme | brand | bg | surface | text | muted | accent | on-accent | accent-text | second |
|---|---|---|---|---|---|---|---|---|---|
| light | `#F0A63A` | `#F6FAFC` | `#FCFEFF` | `#111619` | `#555C61` | `#9D6604` | `#FCFEFF` | `#9D6604` | `#6193A9` |
| dark | `#F0A63A` | `#111619` | `#1A1F23` | `#F6FAFC` | `#9EA6AB` | `#F0A63A` | `#111619` | `#F0A63A` | `#7BABC1` |

### 19. Aubergine & Peach
*Late dinner, warm light.* Seeds `#F2A285` + `#9DC3A8`, tinted neutrals. **Good for:** hospitality, lifestyle, social, audio. **Avoid for:** safety-critical.

| Theme | brand | bg | surface | text | muted | accent | on-accent | accent-text | second |
|---|---|---|---|---|---|---|---|---|---|
| light | `#F2A285` | `#FDF8F6` | `#FFFDFC` | `#191311` | `#615956` | `#A65C41` | `#FFFDFC` | `#A65C41` | `#70957B` |
| dark | `#F2A285` | `#191311` | `#231C1A` | `#FDF8F6` | `#ACA29F` | `#F2A285` | `#191311` | `#F2A285` | `#8AAD94` |

### 20. Graphite & Electric Coral
*A synth panel with one lit key.* Seeds `#FF6A57` + `#8FD3C9`, pure neutrals. **Good for:** audio, gaming, launches, creator tools. **Avoid for:** conservative B2B.

| Theme | brand | bg | surface | text | muted | accent | on-accent | accent-text | second |
|---|---|---|---|---|---|---|---|---|---|
| light | `#FF6A57` | `#F9F9F9` | `#FFFFFF` | `#151515` | `#5B5B5B` | `#C93628` | `#FFFFFF` | `#C93628` | `#569990` |
| dark | `#FF6A57` | `#151515` | `#1E1E1E` | `#F9F9F9` | `#A4A4A4` | `#FF6A57` | `#151515` | `#FF6A57` | `#72B1A8` |

## 14. Picking one when the user gave nothing
1. Write the concept sentence first (`../creative-direction.md` §1). Pick the palette whose *scene* matches it; if none does, run the method (§12) with your own seed. Running the method is better than forcing a library palette.
2. Light or dark from the context of use (reading, daytime, productivity → light; media, night use, creative → dark); every palette above has both.
3. Never reuse the palette from the previous project in the same session or repository; DENT outputs should not look related unless they are the same brand.
4. Tell the user which palette or seed you used and why, so they can swap it.

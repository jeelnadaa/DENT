# Color — Theory, Scales, Dark Mode and Default Palettes

Everything about color beyond the basics in `foundations-and-components.md` §3 (Color). Part 1 is theory and systems; Part 2 is the optional default palettes.

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
~60% dominant (backgrounds), ~30% secondary (text, surfaces, structure), ~10% accent (actions, highlights). This is the three-role structure (Dominant / Complement / Off color) used by the default palettes in Part 2.

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

- **Background:** not pure black for apps (use #0B0B0F–#121212 range, tinted); pure black only for OLED-focused or dramatic styles.
- **Elevation = lighter surfaces.** Higher layers get lighter (e.g. bg #111 → surface #18181B → raised #202024 → overlay #2A2A30). Shadows are barely visible; add subtle borders (white 6–12%).
- **Text:** off-white (#EDEDEF / ~90–95% lightness) for body; muted ~65–70% lightness; avoid pure #FFF large areas (glare/halation).
- **Desaturate and lighten accents:** saturated colors vibrate on dark backgrounds. Use the 300–400 steps instead of 600 (e.g. blue-400 instead of blue-600), reduce chroma slightly.
- **Re-check every contrast pair** — they all change.
- **Images & illustrations:** reduce brightness slightly or provide dark variants; transparent PNG logos may need a light version.
- **Shadows → borders and lightness.**
- **Status colors:** use lighter variants; subtle backgrounds as low-opacity tints (e.g. error at 12–16% over surface).
- **Charts:** brighter, less saturated series colors; lighter gridlines at very low opacity.
- **Respect the system setting** (`prefers-color-scheme`) and offer a toggle (System / Light / Dark) where useful. Remember the choice; avoid theme flash.

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
Contrast checkers (WebAIM, Stark), OKLCH pickers (oklch.com), scale generators (Radix Colors, Tailwind palette generators, Leonardo by Adobe — contrast-based scales), color-blind simulators (Chrome DevTools rendering emulation, Sim Daltonism).

---

# Part 2 — Default color palettes

> **⚠️ OPTIONAL — NOT REQUIRED.** These palettes are a fallback for when the user gives no colors, brand or direction. You are **not required** to use colors from this file. If the user, brand or chosen aesthetic style suggests other colors, use those instead and follow the same three-role structure below.

---

## The three-role structure

Every default palette has exactly three colors:

| Role | Share of the UI (approx.) | Used for |
|---|---|---|
| **Dominant** | ~60% | Page background, main surfaces. Sets the mood and the light/dark mode. |
| **Complement** | ~30% | Body text, headings, icons, borders, secondary surfaces (use tints/shades of it for subtle layers). |
| **Off color** (accent) | ~10% | Primary buttons, links, active states, highlights, key data. The one color that "pops". |

The 60/30/10 split is a **[Convention]** (Part 1 §4), not a law. Treat it as a starting proportion.

### Usage rules for these palettes
- **[Rule]** Text on a filled Off-color button uses the **Dominant** color, not the Complement. (Every palette below passes AA that way; Complement-on-Off does **not** pass in most of them.)
- **[Rule]** Semantic colors (success, warning, error, info) are added separately when needed. Do not reuse the Off color as an error color.
- **[Convention]** Derive extra shades by mixing Complement into Dominant (e.g. 5%, 10%, 20%) for surfaces, borders and muted text, so the palette stays to three base colors. Check muted text still meets 4.5:1.
- **[Convention]** Keep the Off color scarce. If it shows up everywhere, it stops meaning "act here" (Von Restorff effect).

Contrast values below are WCAG 2.x ratios, computed from the hex values.
- **C/D** = Complement text on Dominant background (needs ≥ 4.5 for body text)
- **O/D** = Off color on Dominant background, and also Dominant text on an Off-color button (needs ≥ 3 for UI elements, ≥ 4.5 for text)

---

## Light mode palettes

### 1. Paper & Ink
Warm, editorial, calm. Good for content, blogs, docs, productivity.

| Role | Hex |
|---|---|
| Dominant | `#F7F5F0` warm off-white |
| Complement | `#1F2A37` deep ink navy |
| Off color | `#C2410C` burnt vermilion |

C/D **13.34** · O/D **4.75**

### 2. Sage & Copper
Natural, grounded, organic. Good for wellness, food, agriculture, lifestyle.

| Role | Hex |
|---|---|
| Dominant | `#EEF2EC` pale sage |
| Complement | `#24352B` dark forest |
| Off color | `#A14A07` copper |

C/D **11.46** · O/D **5.30**

### 3. Cool Mist
Clean, trustworthy, techy. Good for SaaS, fintech, dashboards, dev tools.

| Role | Hex |
|---|---|
| Dominant | `#F2F5FA` cool mist white |
| Complement | `#1B2340` midnight blue |
| Off color | `#3451E8` electric indigo |

C/D **14.12** · O/D **5.51**

### 4. Sand & Teal
Warm but fresh, approachable. Good for travel, hospitality, education, marketplaces.

| Role | Hex |
|---|---|
| Dominant | `#F4EDE4` sand |
| Complement | `#3A2E28` espresso brown |
| Off color | `#1A6B5E` deep teal |

C/D **11.29** · O/D **5.46**

### 5. Lilac & Raspberry
Soft, friendly, modern. Good for social, creative tools, consumer apps.

| Role | Hex |
|---|---|
| Dominant | `#F6F3FA` lilac white |
| Complement | `#2B2340` dark plum |
| Off color | `#C2255C` raspberry |

C/D **13.49** · O/D **5.15**

---

## Dark mode palettes

### 6. Midnight Ember
Warm dark, focused, cinematic. Good for media players, creative tools, portfolios.

| Role | Hex |
|---|---|
| Dominant | `#0F1419` near-black slate |
| Complement | `#E6E1D8` warm bone |
| Off color | `#FF8A3D` ember orange |

C/D **14.22** · O/D **7.89**

### 7. Deep Forest Lime
Bold, energetic, techy. Good for developer tools, fitness, gaming, startups.

| Role | Hex |
|---|---|
| Dominant | `#0E1A16` deep forest black |
| Complement | `#DCE8E0` pale mint grey |
| Off color | `#C8F169` acid lime |

C/D **14.14** · O/D **13.79**

### 8. Obsidian Violet
Premium, moody, futuristic. Good for AI products, music, crypto, nightlife.

| Role | Hex |
|---|---|
| Dominant | `#14111C` obsidian purple-black |
| Complement | `#E9E4F5` lavender white |
| Off color | `#A78BFA` soft violet |

C/D **14.98** · O/D **6.85**

### 9. Ink & Teal
Cool, technical, precise. Good for analytics, monitoring, health tech, utilities.

| Role | Hex |
|---|---|
| Dominant | `#0B1620` deep ink blue |
| Complement | `#D7E3EA` frost grey |
| Off color | `#2DD4BF` aqua teal |

C/D **13.97** · O/D **9.81**

### 10. Charcoal Gold
Luxurious, restrained, confident. Good for finance, premium brands, watches, real estate.

| Role | Hex |
|---|---|
| Dominant | `#161616` charcoal |
| Complement | `#EDEAE3` ivory |
| Off color | `#E9B949` muted gold |

C/D **15.06** · O/D **9.91**

---

## Picking one (when the user gave nothing)

1. Decide light or dark from the product: reading/productivity/daytime → light; media/creative/night use/premium mood → dark. If unsure, default to light.
2. Match the product's mood to a palette's "Good for" line.
3. If two fit equally, prefer the one with higher C/D contrast.
4. Tell the user which palette was used, so they can swap it.

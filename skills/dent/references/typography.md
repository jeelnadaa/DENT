# Typography — Pairings, Scales and Font Stacks

The type basics are in `foundations-and-components.md` §3 (Typography), and the craft details in `modern-layer.md` §7.1. This file adds what those don't cover: a font pairing library, scale ratios and fallback stacks. All fonts listed are free (Google Fonts or Fontshare) unless noted.

---

## 1. Choosing fonts — quick method
1. **Body/UI font first:** it carries most of the text. It needs high legibility at 14–16px, open shapes, clear distinction between I/l/1 and O/0, several weights, tabular figures.
2. **Display font second** (optional): personality for headings. Contrast it with the body font (serif + sans, geometric + humanist), or use the same family in a heavier weight.
3. **Limit:** 2 families (+ a monospace if needed for code/data).
4. **Check script support** for every language in scope (internationalization.md).
5. **Test** with real content at real sizes, in light and dark.

## 2. Classification (what each kind feels like)
| Kind | Examples | Feel | Use |
|---|---|---|---|
| Neo-grotesque sans | Inter, Geist, Helvetica-like, Arimo | Neutral, modern, precise | UI, SaaS, Swiss, minimal |
| Geometric sans | Poppins, Outfit, Jost, Manrope, Plus Jakarta Sans, Satoshi | Clean, friendly, modern | Startups, consumer apps |
| Humanist sans | Source Sans 3, Open Sans, Nunito Sans, Fira Sans, Lato | Warm, readable, approachable | Long UI text, public services |
| Rounded sans | Nunito, Quicksand, Fredoka, Baloo 2 | Soft, playful | Kids, playful, clay |
| Grotesk with character | Space Grotesk, Bricolage Grotesque, Syne, Archivo, General Sans, Clash Display | Bold, trendy, editorial-tech | Neo-brutalism, agencies |
| Transitional/old-style serif (text) | Source Serif 4, Newsreader, Lora, Crimson Pro, EB Garamond, Libre Baskerville | Literary, trustworthy | Reading, editorial, academia |
| Display serif | Playfair Display, Fraunces, DM Serif Display, Instrument Serif, Young Serif | Elegant, expressive | Headlines, luxury, editorial |
| Didone (high contrast) | Bodoni Moda, Cormorant | Fashion, luxury | Large display only |
| Slab serif | Roboto Slab, Zilla Slab, Arvo | Sturdy, retro | Vintage, bold headings |
| Monospace | JetBrains Mono, IBM Plex Mono, Geist Mono, Fira Code, Space Mono | Technical | Code, data, terminal |
| Script/handwritten | Caveat, Kalam, Pacifico, Yellowtail | Personal, casual | Accents only |
| Display/decorative | Bungee, Monoton, Orbitron, Press Start 2P | Thematic | Single headline or logo only |

## 3. Pairing library (display / body)
| Mood | Heading | Body | Fits styles |
|---|---|---|---|
| Neutral modern | Inter Display (tight) | Inter | Minimal, Corporate, Dark Tech |
| Sharp tech | Geist | Geist (+ Geist Mono) | Dark Tech, Minimal |
| Friendly startup | Plus Jakarta Sans 700 | Plus Jakarta Sans 400 | Aurora, Glass, SaaS |
| Bold creative | Space Grotesk 700 / Clash Display | Inter or Space Grotesk | Neo-brutalism, agencies |
| Editorial classic | Playfair Display | Source Serif 4 | Editorial, magazine |
| Editorial modern | Instrument Serif | Inter | Editorial, Monochrome, Premium |
| Warm natural | Fraunces (soft) | DM Sans | Organic, wellness |
| Calm refined | Cormorant Garamond | Manrope | Japandi, Luxury |
| Luxury fashion | Bodoni Moda | Jost (light/regular) | Luxury |
| Academic | EB Garamond | EB Garamond / Source Serif 4 | Dark Academia |
| Playful | Fredoka / Baloo 2 | Nunito | Playful, Claymorphism |
| Retro warm | Young Serif / DM Serif Display | Work Sans | Vintage |
| Geometric Bauhaus | Jost 600 | Jost 400 | Bauhaus |
| Swiss | Inter Tight 700 (very large) | Inter | Swiss |
| Developer | JetBrains Mono (headings) | Inter | Terminal accents, dev docs |
| Indic-ready | Mukta / Hind / Anek (Latin + Devanagari etc.) | Same family | Products in Indian languages |

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

## 5. Recommended line heights and widths
| Text | Line height | Letter spacing |
|---|---|---|
| Display (48px+) | 1.0–1.1 | −2% to −4% |
| Headings (24–40px) | 1.15–1.3 | −1% to −2% |
| Body (15–18px) | 1.45–1.6 | 0 |
| Small/caption (12–14px) | 1.4–1.5 | 0 to +1% |
| All-caps labels | 1.2–1.4 | +4% to +10% |
| Indic / Thai / Arabic | +0.1–0.2 vs Latin | 0 (no tracking on Indic) |

Line length 45–75 characters (≈ 60–70ch ideal) for body text.

## 6. Font stacks (fallbacks)
```css
--font-sans: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif;
--font-serif: "Source Serif 4", Georgia, "Times New Roman", "Noto Serif", serif;
--font-mono: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
--font-system: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; /* fastest, native feel */
```
Add per-script fallbacks when needed, e.g. `"Noto Sans Devanagari"` after the Latin font.

## 7. Font loading checklist
- [ ] Only the weights/styles used (variable font if many weights).
- [ ] `font-display: swap` (or `optional` for decorative fonts).
- [ ] Preload the 1–2 fonts used above the fold.
- [ ] Subset to the needed character sets.
- [ ] Fallback metrics adjusted (`size-adjust`, `ascent-override`) to avoid layout shift.
- [ ] Self-host for performance/privacy when possible; check license.

## 8. Common typography mistakes
- Too many sizes that are only slightly different (no clear hierarchy).
- Light (300) weights for body text, or grey body text on grey.
- Centered long paragraphs; justified text on the web (rivers of space).
- All caps for long text; fake bold/italic (font lacks the weight).
- Display fonts used for body or UI text.
- Tight line height on body text or Indic scripts (clipped marks).
- Ignoring tabular numbers in tables and prices.

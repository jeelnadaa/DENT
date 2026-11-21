# Hero Typography and Expressive Type

Typography is the cheapest path to a distinctive design and the most common place AI-made pages look generic (one centered two-line headline in Inter, medium weight). This file is a system for **hero titles, section openers, wordmarks and kinetic type**: how to choose, compose, build and verify them.

Used by `/dent:type`, recipes (landing page §5), `/dent:motion-graphics`.

---

## 1. Decide the type role first

| Role | What it does | Example |
|---|---|---|
| **Wordmark scale** | The product name *is* the hero image | "DENT" at 22vw, cropped by the viewport |
| **Statement** | A short, strong claim carries the page | "Ship the design, not the template." |
| **Editorial** | Headline + deck + byline like a magazine | Serif headline, italic deck, small caps kicker |
| **System / technical** | Type as interface: labels, numbers, coordinates | Mono labels, tabular numbers, section codes |
| **Data type** | A number is the hero | "0 overflow at 6 widths" |
| **Kinetic** | Type moves to tell the story | Words swap, masks reveal, scale jumps |
| **Typographic illustration** | Letters become shapes and pictures | A giant ampersand as image |

Pick one per page (plus at most one secondary moment).

## 2. Headline writing rules (type starts with words)
- 2–8 words for a hero statement; the user's outcome, not your category ("Design that doesn't look generated" beats "AI-powered design platform").
- Concrete nouns and verbs; no "unlock, supercharge, seamless, revolutionize, next-gen" (`anti-slop.md` §4).
- Write 10 headline options, choose by reading them aloud. Test the two best at phone width.
- One idea per line when you control breaks; break by meaning ("Design that / doesn't look generated"), never mid-phrase.

## 3. Choosing faces (pairing matrix)

Use a **contrast axis**: pair faces that differ clearly in one dimension (classification, width, weight) and agree in another (x-height, mood). DENT has no default face: choose by voice and check overuse with `scripts/fonts.py` (`../typography.md` §0); the full pairing library is `../typography.md` §3. Strong hero pairings (free, OFL, verified 2026-11-21):

| Display (hero) | Text | Mood | Licence |
|---|---|---|---|
| **Mozilla Headline** 800, condensed `wdth`, tracking −3% | Mozilla Text | Bold, opinionated | OFL |
| **Zalando Sans Expanded** 800 | Zalando Sans | Wide, engineered | OFL |
| **Gloock** | Hanken Grotesk | Premium editorial | OFL |
| **Redaction 50** (one degraded word) | Redaction / Inclusive Sans | Archival, civic, investigative | OFL |
| **Kalnia** (wide, 600) | Familjen Grotesk | Cultural, expressive | OFL |
| **Science Gothic** (wide, high contrast) | Golos Text | Architectural, technical | OFL |
| **Bodoni Moda** (opsz 96) | Albert Sans | Fashion, dramatic | OFL |
| **Imbue** (condensed didone) | Epilogue | Magazine cover | OFL |
| **Anybody** (wdth 150, 900) | Anybody (wdth 100) | Sport, games, launch energy | OFL |
| **Special Gothic Expanded One** | Special Gothic | Poster, events | OFL |
| **Young Serif** | Rethink Sans | Soft vintage, craft | OFL |
| **Montagu Slab** (opsz 144) | SUSE | Sturdy, outdoorsy | OFL |
| **Doto** (dot matrix) | Reddit Sans | Screen-native, transit | OFL |
| **Erode** or **Zodiak** (Fontshare, ITF FFL) | Hanken Grotesk | Calm or premium serif | ITF FFL / OFL |

Avoid as automatic choices (use only deliberately, logged): Inter-only headlines, Playfair Display as "luxury", Bebas Neue/Anton for everything, Montserrat/Poppins headings. Paid families (Söhne, GT America, Neue Haas, PP Editorial, Canela…) are excellent; recommend only if the user owns a licence. Fontshare fonts: no subsetting or modification, don't commit them to public repos (load via the Fontshare API). Record every licence (`../catalog/asset-sources.md` §1).

## 4. Composition techniques (the move library)

Each technique: **what**, **when**, **build notes**, **watch-out**.

1. **Viewport-cropped wordmark.** The name set so large the viewport crops it (letters bleed off left/right or bottom). When: brand-led launches, portfolios. Build: `font-size: clamp(8rem, 2rem + 20vw, 20rem); line-height: .8; letter-spacing: -0.04em; white-space: nowrap; overflow: clip` on a wrapper that is `overflow-x: clip` (not the body). Watch-out: must not create page-level horizontal scroll; keep the real text accessible.
2. **Scale jump.** One word 4–8× bigger than the rest of the line ("Design that *doesn't* look generated"). When: statements with one key word. Watch-out: line height for mixed sizes; align baselines.
3. **Mixed faces in one line.** Serif italic for the emotional word, grotesk for the rest. When: editorial warmth in tech. Watch-out: match optical sizes; only one swap per headline.
4. **Stacked justify.** Each line scaled so all lines share the same width (like a poster). When: manifestos, events. Build: per-line font sizes computed at design time or with a fit-text script; or SVG `textLength`. Watch-out: reflow at narrow widths; provide a simpler stack under 480 px.
5. **Outline + fill pair.** Repeat the headline: solid, outline (`-webkit-text-stroke`), outline… When: retro, posters, kinetic loops. Watch-out: outline text must not be the only readable copy; hide repeats from screen readers (`aria-hidden`).
6. **Masked image type.** Text filled with an image/video (`background-clip: text`). When: travel, film, photography. Watch-out: contrast; provide solid fallback color; never for body text.
7. **Variable axis expression.** Weight/width/softness changes with scroll, hover or time (Fraunces SOFT, Roboto Flex wdth, Recursive CASL). When: type-led brands, kinetic sections. Build: `font-variation-settings` or `font-weight` transitions; scroll-driven animation. Watch-out: reduced motion → static; performance OK because no layout change if width axis is avoided during scroll.
8. **Typographic grid.** Headline broken into grid cells with labels and numbers around it (Swiss / Field Manual). When: technical, editorial. Watch-out: reading order in DOM must follow the sentence.
9. **Rotated / vertical labels.** A vertical word running along the edge (`writing-mode: vertical-rl`). When: editorial, fashion. Watch-out: short words only; not essential content.
10. **Underline as gesture.** A hand-drawn SVG underline/circle draws under one word once. When: friendly, human brands. Watch-out: once, not on loop.
11. **Big numerals as hero.** A real metric or a version/date as giant tabular figures. When: data, launches, changelogs. Watch-out: the number must be real.
12. **Typewriter / overwrite.** A word types, gets struck through and replaced ("Design ~~templates~~ products"). When: copy-led, contrarian positioning. Watch-out: final text readable instantly with reduced motion; announce only the final text to screen readers.
13. **Split reveal.** Lines rise from a mask with 60–90 ms stagger. When: almost any premium hero. Build: wrap each line in `overflow: clip` span; animate `translate` 0 100% → 0 (individual transform property). Watch-out: don't split by characters for long text (SR noise); use `aria-label` on the parent if spans are needed.
14. **Text on a path.** Headline follows a curve/circle (SVG `textPath`). When: badges, playful, music. Watch-out: short text only.
15. **Ticker / marquee band.** A band of repeating words below the hero. When: events, energetic brands. Watch-out: pause control or pause on hover/focus; respects reduced motion; never the only place info appears.
16. **Glyph as illustration.** One giant character (ampersand, initial, "?") as the image. When: type-centric brands. Watch-out: decorative → `aria-hidden`.
17. **Footnote / annotation layer.** Headline with superscript numbers and margin notes. When: research, science, documentation, honest claims.
18. **Terminal headline.** Prompt + command as headline (`$ dent create --all-out`). When: dev tools. Watch-out: provide normal-language subhead.

## 5. Scale, spacing and craft numbers
- Hero size: `clamp(3rem, 1rem + 7vw, 7.5rem)` for statements; about 20vw for wordmarks (`clamp(8rem, 2rem + 20vw, 20rem)`). Always include a rem term and keep the maximum ≤ 2.5× the minimum so zoom still reaches 200% (WCAG 1.4.4, `mwg:responsive-design`); a bigger range is a design bug, not a style.
- Ratio hero : body ≥ 4 on marketing pages (e.g. 72 px vs 18 px). Timid scale reads as template.
- Tracking: −2% to −5% at ≥ 64 px; −1% to −2% at 32–64 px; +4% to +10% for small caps labels.
- Line-height: 0.85–1.0 for display caps, 0.95–1.1 for display mixed case, 1.5–1.65 body.
- `text-wrap: balance` on headings; `hanging-punctuation: first` where supported; use real quotes and dashes.
- Optical sizing on (`font-optical-sizing: auto`), use the display optical size for the hero.
- Max hero width 12–16 words per line; deck/subhead 45–65 characters.
- Numbers: `font-variant-numeric: tabular-nums lining-nums` for data, oldstyle for editorial prose.

## 6. Build recipes

**Split-line reveal (CSS only, reduced-motion safe):**
```html
<h1 class="hero"><span class="line"><span>Design that</span></span>
<span class="line"><span>doesn't look <em>generated</em>.</span></span></h1>
```
```css
.hero{font: 800 clamp(3rem,1rem + 7vw,7.5rem)/.95 "Mozilla Headline","Zalando Sans",sans-serif;font-stretch:75%;letter-spacing:-.03em;text-wrap:balance}
.hero em{font-style:normal;font-stretch:125%;font-weight:300;letter-spacing:-.01em} /* width contrast, not the italic-serif-word cliché */
.line{display:block;overflow:clip}
@media (prefers-reduced-motion:no-preference){
  .line>span{display:inline-block;translate:0 105%;animation:rise .9s cubic-bezier(.16,1,.3,1) forwards}
  .line:nth-child(2)>span{animation-delay:.09s}
}
@keyframes rise{to{translate:none}}
```

**Viewport-cropped wordmark without page overflow:**
```css
.wordmark-wrap{overflow-x:clip;width:100%}
.wordmark{font:900 clamp(8rem,2rem + 20vw,20rem)/.78 "Archivo",sans-serif;letter-spacing:-.05em;white-space:nowrap;margin-inline:-.04em}
```

**Variable weight on scroll (progressive enhancement):**
```css
@supports (animation-timeline: view()){
  @media (prefers-reduced-motion:no-preference){
    .flex{animation:wght linear both;animation-timeline:view();animation-range:entry 0% cover 40%}
  }
}
@keyframes wght{from{font-variation-settings:"wght" 200}to{font-variation-settings:"wght" 900}}
```

**Kinetic word swap (accessible):** keep the final sentence in the DOM as text; animate a visual-only layer with `aria-hidden="true"`; under reduced motion show the final sentence only.

**GSAP SplitText** (free since 2025 under GSAP's standard licence) for character/word splits with `autoSplit` and `aria` handling; use when CSS isn't enough. Respect `gsap.matchMedia()` for reduced motion.

## 7. Accessibility rules for expressive type
- Real text, never text baked into images/canvas for headings (except logos, which get alt text).
- Visual reorderings must keep DOM order = reading order.
- Splitting into spans: put the readable string on the parent (`aria-label`) and hide the span soup, or split by lines/words not characters.
- Contrast applies to outline, masked and gradient text: test the weakest part.
- Reduced motion shows the final composition immediately.
- 200 % zoom and 320 px width: no clipped words, no horizontal scroll (crop wrappers use `overflow-x: clip`).

## 8. Verify
Screenshot the hero at 320, 390, 768, 1440: check wraps (no orphans), no clipped glyphs or descenders, no overflow (verify script), font actually loaded (no fallback flash in the final screenshot), and the headline reads correctly with reduced motion.

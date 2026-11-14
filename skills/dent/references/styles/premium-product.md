# Premium Product (Cupertino-clean)

**Also called:** Apple-like, Apple style, iOS style, clean premium, product page style, "Cupertino"
**In one sentence:** Huge confident headlines, product imagery as the hero, generous space, smooth scroll storytelling and flawless details.
**Picture it:** A product launch page: black background, one gleaming device, a two-word headline in large bold type, and the page slowly revealing features as you scroll.
**Feels like:** premium, confident, precise, calm, cinematic.

**Use for:** hardware/product launches, premium apps, consumer tech, high-end SaaS marketing pages, iOS apps.
**Avoid for:** budget/discount brands, playful kid products, dense enterprise UIs (the app side uses platform conventions instead).

## Overrides
| Area | Override |
|---|---|
| Color | Neutral canvas: pure white #FFFFFF / light grey #F5F5F7 sections, or black #000 for dramatic sections. Text near-black #1D1D1F / white. **One** link/CTA blue (#0071E3) or the product's color. Color comes from imagery. |
| Typography | SF Pro-like grotesque (General Sans, Geist, Satoshi; system-ui on Apple). **Very large, bold, tightly tracked headlines** (−0.02 to −0.04em), short (2–6 words). Subheads in medium grey. |
| Spacing / layout | Full-width sections, each about ONE idea. Very large vertical spacing (120–200px between sections on desktop). Centered heroes, tiles/bento grids for feature lists. |
| Radius | Controls pill (980px) for CTAs; tiles/cards 18–28px; continuous ("squircle") corners where possible. |
| Borders | Almost none. |
| Depth | Very subtle; depth comes from photography and contrast between light/dark sections. Glass blur on sticky nav. |
| Motion | Cinematic, smooth: scroll-linked reveals, product rotation/zoom tied to scroll, slow fades (500–800ms on heroes), springs in apps. Always subtle and fluid. |
| Hover | Minimal: link underline, slight brightness on tiles. |
| Imagery / icons | **Studio-quality product renders/photos** on clean backgrounds; SF Symbols-style line icons. |
| Components | Pill buttons (filled blue primary, text link "Learn more ›" secondary). Sticky translucent nav bar. In apps: follow iOS HIG (large titles, grouped lists, sheets). |

## Signature moves
1. Giant, short, bold headline + one-line subhead.
2. One hero product image per section.
3. Alternating white / light-grey / black sections.
4. Smooth scroll-driven storytelling.
5. "Learn more ›" text links + one pill CTA.

## Do / Don't
- **Do** write very short headlines; let images carry the message.
- **Do** obsess over alignment, spacing and image quality.
- **Don't** clutter with many CTAs, badges or colors.
- **Don't** use cheap stock imagery — this style lives or dies on imagery.

## Accessibility watch-outs
- Grey subheads on light grey (#86868B on #F5F5F7) can fail for small text; use them only at large sizes or darken.
- Scroll-driven animations need reduced-motion fallbacks with all content visible.

## Starter tokens
```css
:root{
  --bg:#FFFFFF; --bg-alt:#F5F5F7; --bg-dark:#000000; --text:#1D1D1F; --text-2:#6E6E73; --text-on-dark:#F5F5F7;
  --accent:#0071E3; --on-accent:#FFFFFF;
  --font-sans:"General Sans","Geist",system-ui,-apple-system,sans-serif;
  --h1:clamp(2.75rem,1.75rem + 4.5vw,6rem); --tracking-h1:-0.035em;
  --radius-pill:980px; --radius-container:24px;
  --nav-glass:rgb(255 255 255 / .72); --blur:blur(20px) saturate(180%);
  --dur:500ms; --ease:cubic-bezier(.16,1,.3,1);
}
```

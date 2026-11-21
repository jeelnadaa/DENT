# Monochrome (High-Contrast Black & White)

**Also called:** black and white, mono, noir, high contrast, grayscale
**In one sentence:** Only black, white and greys — drama and hierarchy come from contrast, scale and typography alone.
**Picture it:** A fashion photographer's site: full-bleed black-and-white photos, huge white type on black, and a thin white line as the only decoration.
**Feels like:** bold, timeless, dramatic, serious, artistic.

**Use for:** photography, fashion, architecture, film, portfolios, typography-led brands, premium tools.
**Avoid for:** products needing color-coded status everywhere (use a single accent or semantic colors only for status), kids.

## Overrides
| Area | Override |
|---|---|
| Color | Black, white and 3–5 greys. **No hue** — except semantic colors for errors/success when functionally needed (keep them muted). Optional single accent used extremely rarely. |
| Typography | Strong type is the hero: big grotesk or serif display with dramatic size contrast (Special Gothic, Zalando Sans Expanded, "Neue Montreal"-like, Gloock, Redaction, "PP Editorial"-like). |
| Spacing / layout | Large, cinematic layouts; full-bleed imagery; alternating black and white sections. |
| Radius | 0–4px. |
| Borders | 1px lines in grey or white/black. |
| Depth | None; contrast inversion (dark section ↔ light section) creates rhythm. |
| Motion | Clean, deliberate: wipes, masks, slow fades; image reveals. |
| Hover | **Invert** (black ↔ white), image goes from grayscale to slightly brighter. |
| Imagery / icons | Black-and-white photography with strong contrast; minimal line icons. |
| Components | Black buttons on white / white on black; outlined secondary. |

## Signature moves
1. Zero color — just black, white, grey.
2. Big dramatic type and full-bleed B&W imagery.
3. Inversion as interaction and section rhythm.

## Do / Don't
- **Do** use grey levels deliberately (not 15 random greys).
- **Do** still show states clearly (use weight, underline, icons since color is unavailable).
- **Don't** rely on color for errors — but you may add a muted red for error text **[Rule: not color alone still applies]**.
- **Don't** use mid-grey text on mid-grey backgrounds.

## Accessibility watch-outs
- Pure black/white maximum contrast can cause glare for long reading; soften slightly (#111 on #F7F7F7).
- States (selected, error) need icon/text indicators.

## Starter tokens
```css
:root{
  --bg:#F7F7F7; --bg-inverse:#0D0D0D; --text:#0D0D0D; --text-2:#4D4D4D; --text-inverse:#F2F2F2; --border:#1A1A1A;
  --accent:#0D0D0D; --on-accent:#F7F7F7; --error:#A12622;
  --font-sans:"Special Gothic",system-ui,sans-serif; --font-serif:"Gloock",serif;
  --radius-control:0; --radius-container:0;
  --dur:350ms; --ease:cubic-bezier(.65,0,.35,1);
}
```

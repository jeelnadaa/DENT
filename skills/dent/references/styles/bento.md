# Bento Grid

**Also called:** bento box layout, tile layout, modular grid, card mosaic
**In one sentence:** Content arranged in a grid of rounded tiles of different sizes — like a Japanese bento box — where tile size shows importance.
**Picture it:** A feature section with one big square tile showing the main feature, two wide tiles beside it and four small tiles below, all with equal gaps and the same rounded corners.
**Feels like:** organized, modern, scannable, playful-structured.

Note: Bento is a **layout style** — combine it with a visual style (Minimal, Dark Tech, Premium Product, Neo-brutalism…). It controls structure; the other style controls colors and type.

**Use for:** feature overviews, portfolios, dashboards, profile/"link in bio" pages, product spec summaries.
**Avoid for:** long linear reading, step-by-step flows.

## Overrides
| Area | Override |
|---|---|
| Color | From the paired style. Tiles may each have a different background (tinted, image, dark) to create rhythm — but from one palette. |
| Typography | From the paired style; each tile has one short headline + optional one line; big numbers/stats work well. |
| Spacing / layout | CSS grid, 4–6 columns desktop, 2 columns tablet, 1 column mobile. **Equal gaps (12–24px)** everywhere. Tile sizes: 1×1, 2×1, 1×2, 2×2. One hero tile (largest). |
| Radius | Large and identical on all tiles: 16–32px. |
| Borders | From the paired style (hairline in dark, none in light). |
| Depth | Mostly flat; tiles separated by gaps. |
| Motion | Tiles stagger-in on scroll (30–50ms apart); inside tiles, small looping demos/animations. |
| Hover | Tile lifts slightly or its inner visual animates. |
| Imagery / icons | Each tile = one visual (screenshot crop, illustration, icon, chart, stat). |
| Components | Tiles can be links; whole tile clickable. |

## Signature moves
1. Mixed-size rounded tiles in a tight grid.
2. Equal gaps and equal radii everywhere.
3. One idea per tile; the biggest tile = the most important idea.

## Do / Don't
- **Do** plan the grid so it fills fully without holes at every breakpoint.
- **Do** keep tile content short.
- **Don't** put long paragraphs in tiles.
- **Don't** use different radii or gaps between tiles.

## Accessibility watch-outs
- Reading order: DOM order should follow the logical order, not just visual placement.
- Text over image tiles needs a scrim for contrast.

## Starter tokens
```css
.bento{display:grid;grid-template-columns:repeat(4,1fr);grid-auto-rows:minmax(180px,auto);gap:16px;}
.tile{border-radius:24px;padding:24px;overflow:hidden;}
.tile--hero{grid-column:span 2;grid-row:span 2;}
.tile--wide{grid-column:span 2;}
.tile--tall{grid-row:span 2;}
@media (max-width:900px){.bento{grid-template-columns:repeat(2,1fr);}}
@media (max-width:560px){.bento{grid-template-columns:1fr;}.tile--hero,.tile--wide{grid-column:auto;}}
```

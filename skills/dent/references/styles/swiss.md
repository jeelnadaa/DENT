# Swiss (International Typographic Style)

**Also called:** Swiss style, International style, grid design, Helvetica style
**In one sentence:** Strict grids, bold sans-serif type, asymmetric layouts and lots of white space — order and clarity above decoration.
**Picture it:** A 1960s Swiss concert poster: a giant black headline in Helvetica, a red block, and small text aligned to an invisible grid.
**Feels like:** rational, objective, bold, organized, timeless.

**Use for:** portfolios, agencies, architecture, museums, editorial, conferences, data-heavy sites that want character.
**Avoid for:** soft/friendly consumer brands, kids, wellness.

## Overrides
| Area | Override |
|---|---|
| Color | White + black + **one strong primary** (often red #E30613 or similar). Sometimes fully black and white. |
| Typography | Neo-grotesque sans (Switzer, Helvetica Neue, Neue Haas, Geist, "Archivo"). **Flush-left, ragged-right** text, never centered. Very large headlines (8–15vw on web heroes) next to small body text — extreme size contrast. |
| Spacing / layout | **Visible, strict column grid** (12 cols or a modular grid). Asymmetric compositions: content placed off-center but locked to columns. |
| Radius | **0** everywhere. |
| Borders | Thin black rules (1–2px) to divide sections, like a printed page. |
| Depth | None. Completely flat. |
| Motion | Minimal; hard cuts or quick slides along grid lines. |
| Hover | Color invert (black ↔ white) or underline. |
| Imagery / icons | Black-and-white photography, geometric shapes, numbers as graphics. Few icons. |
| Components | Rectangular buttons, black fill or outlined. Inputs as simple underlined fields or boxes. |

## Signature moves
1. Huge, tightly-tracked sans-serif headlines.
2. Everything snaps to a strict, sometimes visible grid.
3. Asymmetric layout with large empty areas.
4. Big numbers, rules and labels as structure (e.g. "01 — Work").

## Do / Don't
- **Do** let the grid be the decoration.
- **Do** use type size, not color, for emphasis.
- **Don't** center text or add rounded corners, gradients or shadows.
- **Don't** use more than one accent color.

## Accessibility watch-outs
- Huge headings need `rem`-based clamp so they don't overflow on mobile.
- Red text on white for small text is fine at #E30613 (~4.6:1) but check any lighter red.

## Starter tokens
```css
:root{
  --bg:#FFFFFF; --text:#000000; --text-2:#3D3D3D; --rule:#000000; --accent:#E30613; --on-accent:#FFFFFF;
  --font-sans:"Switzer","Helvetica Neue",Arial,sans-serif;
  --radius-control:0; --radius-container:0;
  --h1:clamp(4rem,2rem + 8vw,10rem); --tracking-h1:-0.04em;
  --dur:180ms; --ease:cubic-bezier(.2,0,0,1);
}
```

# Bauhaus (Geometric Modernism)

**Also called:** Bauhaus style, constructivist-geometric, primary geometric
**In one sentence:** Form follows function — primary colors, basic shapes (circle, square, triangle), bold sans type and asymmetric balance.
**Picture it:** A poster with a big red circle, a blue square and a yellow triangle overlapping, black bold lowercase type set at an angle on cream paper.
**Feels like:** artistic, rational, bold, historic-modern, constructive.

**Use for:** art/design schools, museums, architecture, creative agencies, posters/events, educational products.
**Avoid for:** soft/wellness, luxury fashion, dense apps (unless used lightly).

## Overrides
| Area | Override |
|---|---|
| Color | **Primary colors**: red #D02020, blue #1040C0, yellow #F0C020 + black #121212 and off-white/cream #F0EBE0. |
| Typography | Geometric sans (Futura-like: "Jost", "Josefin Sans", "Outfit", "Bauhaus 93" for display only). Often lowercase; bold; can be rotated 90°. |
| Spacing / layout | Asymmetric balance on a grid; large geometric shapes as composition; strong diagonals. |
| Radius | 0 for rectangles; perfect circles; nothing in between. |
| Borders | Thick black lines/bars as structure. |
| Depth | Flat. |
| Motion | Shapes slide/rotate into place along straight lines; simple and mechanical. |
| Hover | Shape swap (square → circle), color fill. |
| Imagery / icons | Pure geometric shapes, black-and-white photography, geometric icons. |
| Components | Rectangular solid buttons in primary colors; circular icon buttons. |

## Signature moves
1. Red, blue, yellow + black on cream.
2. Circles, squares, triangles as main graphics.
3. Geometric sans, often lowercase.
4. Asymmetric, constructed composition.

## Do / Don't
- **Do** use shapes as structure, not decoration scattered randomly (that's Memphis).
- **Do** keep it rational and grid-based.
- **Don't** add gradients, shadows or rounded rectangles.
- **Don't** use pastel or extra colors.

## Accessibility watch-outs
- Yellow backgrounds need black text, never white.
- Rotated text should be decorative only; real content stays horizontal.

## Starter tokens
```css
:root{
  --bg:#F0EBE0; --text:#121212; --text-2:#3A3A3A;
  --red:#D02020; --blue:#1040C0; --yellow:#F0C020;
  --accent:var(--red); --on-accent:#FFFFFF;
  --font-sans:"Jost","Futura",system-ui,sans-serif;
  --radius-control:0; --radius-container:0;
  --dur:300ms; --ease:cubic-bezier(.65,0,.35,1);
}
```

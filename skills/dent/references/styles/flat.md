# Flat Design

**Also called:** flat UI, flat 2.0 (with minimal shadows), "Metro"
**In one sentence:** Solid colors, simple shapes and no depth effects — clarity through color blocks and clean icons.
**Picture it:** An infographic made of colored rectangles and circles, with white icons on them and no shadows anywhere.
**Feels like:** clear, friendly, digital, straightforward, bright.

**Use for:** mobile apps, illustrations-heavy marketing sites, education, public services, onboarding flows.
**Avoid for:** luxury/premium positioning, products needing strong hierarchy of layers (use Flat 2.0 with subtle shadows then).

## Overrides
| Area | Override |
|---|---|
| Color | Bright, saturated but harmonious palette (4–6 colors) used as solid fills; white or light-grey background. |
| Typography | Friendly clean sans (Open Sans, Lato, Source Sans 3, Roboto, Poppins). |
| Spacing / layout | Grid of color blocks/tiles; clear sections with colored backgrounds. |
| Radius | 0–6px (classic flat) or 8–12px (flat 2.0). |
| Borders | None; separation by color. |
| Depth | **None** (classic) or one tiny shadow for clickable elements (Flat 2.0 — recommended for usability). |
| Motion | Simple slides and fades 150–250ms. |
| Hover | Color shift (darker/lighter shade). |
| Imagery / icons | Flat vector illustrations, solid or simple-line icons, long-shadow icons (optional, dated). |
| Components | Solid colored buttons; inputs with simple borders; colored tiles as navigation. |

## Signature moves
1. Solid color fills, no gradients or textures.
2. Simple geometric shapes and flat illustrations.
3. Color, not depth, shows hierarchy.

## Do / Don't
- **Do** make clickable things look clickable (color + shape + label) — classic flat often fails this.
- **Do** keep a disciplined palette.
- **Don't** use many unrelated bright colors.
- **Don't** make buttons look identical to static colored blocks.

## Accessibility watch-outs
- White text on bright fills (yellow, light green, orange) often fails — darken those fills or use dark text.
- Ensure links/buttons are distinguishable without color alone.

## Starter tokens
```css
:root{
  --bg:#FFFFFF; --surface:#F3F5F8; --text:#1F2933; --text-2:#52606D;
  --c1:#2E86DE; --c2:#10AC84; --c3:#EE5253; --c4:#FF9F43; --c5:#8854D0;
  --accent:#2E86DE; --on-accent:#FFFFFF;
  --font-sans:"Source Sans 3",system-ui,sans-serif;
  --radius-control:6px; --radius-container:8px;
  --shadow-1:0 1px 2px rgb(0 0 0 / .08);
  --dur:180ms; --ease:cubic-bezier(.2,0,0,1);
}
```

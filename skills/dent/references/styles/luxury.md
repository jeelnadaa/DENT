# Luxury (Elegant Premium)

**Also called:** luxe, high-end, elegant, fashion luxury, boutique, couture
**In one sentence:** Quiet, slow, spacious and refined — thin elegant serifs, muted rich colors, gold or ivory details and very few elements.
**Picture it:** A perfume brand page: ivory background, one bottle photographed in soft light, a thin serif wordmark in wide letter-spacing, and almost nothing else.
**Feels like:** exclusive, sophisticated, calm, timeless, expensive.

**Use for:** fashion, jewelry, watches, hotels, real estate, fine dining, beauty, premium services.
**Avoid for:** budget products, tools, anything needing speed or density.

## Overrides
| Area | Override |
|---|---|
| Color | Ivory/cream (#F6F1E9) or deep black/charcoal (#0E0E0E), with **muted rich tones** (champagne gold #B8975A, deep green #1F3B2F, burgundy #5E1B24, taupe). Very few colors. |
| Typography | **High-contrast thin serifs** for display (Bodoni Moda, Cormorant Garamond, Didot-like "Playfair Display" light, "Italiana"). Clean light sans for body (Jost, Montserrat light, "Manrope"). **Uppercase labels with wide letter-spacing (+0.15–0.3em).** |
| Spacing / layout | Extreme whitespace; centered or symmetric compositions; one focal element per screen; slow pacing. |
| Radius | 0 (sharp = tailored), or full circles for small accents. |
| Borders | Hairlines (0.5–1px) in gold or taupe; thin frames around images. |
| Depth | None or barely visible. |
| Motion | **Slow and graceful**: 600–1200ms fades, slow image zooms (scale 1 → 1.05 over seconds), elegant reveals. Never bouncy. |
| Hover | Slow underline draw, image slow zoom, subtle color fade. |
| Imagery / icons | Editorial, softly lit, often desaturated photography; models/products with lots of negative space. Icons thin and minimal or none. |
| Components | Text links or thin outlined buttons with uppercase tracked labels; no bright filled buttons. Minimal forms with underline inputs. |

## Signature moves
1. Thin high-contrast serif + wide-tracked uppercase sans labels.
2. Massive whitespace, single focal image.
3. Muted palette with one metallic/rich accent.
4. Slow, elegant motion.

## Do / Don't
- **Do** say less: one line of copy per screen if possible.
- **Do** let photography quality carry the brand.
- **Don't** use bright colors, badges, discounts, emojis or bouncy motion.
- **Don't** crowd the layout — crowding reads as cheap.

## Accessibility watch-outs
- Thin serifs and light-weight sans at small sizes often fail readability — keep body ≥ 16px at regular weight, light weights only for large text.
- Gold on ivory usually fails contrast for text; use gold for lines/decoration, dark for text.

## Starter tokens
```css
:root{
  --bg:#F6F1E9; --bg-dark:#0E0E0E; --text:#1A1A1A; --text-2:#5A544B; --gold:#B8975A; --rule:#CBBE9F;
  --accent:#1A1A1A; --on-accent:#F6F1E9;
  --font-display:"Bodoni Moda","Cormorant Garamond",serif; --font-sans:"Jost",system-ui,sans-serif;
  --label-tracking:0.22em;
  --radius-control:0; --radius-container:0;
  --dur:800ms; --ease:cubic-bezier(.25,.1,.25,1);
}
```

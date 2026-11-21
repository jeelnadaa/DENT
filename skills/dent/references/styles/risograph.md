# Risograph / Print (Riso, Zine, Halftone)

**Also called:** riso, risograph, zine, print aesthetic, halftone, screen print, grainy print
**In one sentence:** Looks like it was printed on a risograph — limited bright spot inks, grainy textures, slight misregistration and halftone dots.
**Picture it:** A zine page in fluorescent pink and blue ink that overlap into purple, with grainy texture and the two colors slightly misaligned.
**Feels like:** indie, artsy, tactile, warm, analog.

**Use for:** indie publishers, art events, bookstores, illustrators, music, coffee, creative communities, newsletters.
**Avoid for:** corporate, finance, dense apps.

## Overrides
| Area | Override |
|---|---|
| Color | **2–3 spot "inks"**: fluorescent pink #FF48B0, blue #0078BF, yellow #FFE800, teal #00A95C, orange #FF6C2F — on off-white paper #F8F4EC. Overlaps create mixes (use `mix-blend-mode: multiply`). |
| Typography | Bold grotesk or quirky serif for headlines ("Anybody" at heavy widths, "Familjen Grotesk", "Young Serif"), simple body; printed-looking (optional slight roughness). |
| Spacing / layout | Zine/poster layouts; blocks of solid ink color; overlapping shapes. |
| Radius | 0 or organic. |
| Borders | Thick ink lines. |
| Depth | **Grain/noise texture**, halftone dot patterns, misregistration (layer offset by 2–4px). |
| Motion | Minimal; subtle offset shifts, stop-motion feel (`steps()`). |
| Hover | Ink layers shift into or out of registration; color overprint. |
| Imagery / icons | Photos converted to halftone/duotone in the ink colors; bold illustrations. |
| Components | Solid ink buttons with paper-colored text; simple boxed inputs. |

## Signature moves
1. Limited fluorescent spot colors that overprint (multiply).
2. Grain and halftone textures.
3. Slight misregistration.

## Do / Don't
- **Do** apply duotone/halftone to all photos for consistency.
- **Do** keep text crisp (texture on shapes and images, not on body text).
- **Don't** use more than 3 inks.
- **Don't** use gradients or glossy effects.

## Accessibility watch-outs
- Fluorescent pink/yellow text on paper fails — use dark ink (blue/black) for text.
- Grain must not reduce text contrast.

## Starter tokens
```css
:root{
  --paper:#F8F4EC; --ink-blue:#0078BF; --ink-pink:#FF48B0; --ink-yellow:#FFE800; --ink-dark:#1B1B3A;
  --text:#1B1B3A; --text-2:#3F3F5C; --accent:var(--ink-blue); --on-accent:#F8F4EC;
  --font-display:"Anybody","Familjen Grotesk",sans-serif; --font-sans:"Epilogue",system-ui,sans-serif;
  --radius-control:0; --radius-container:0;
  --grain:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2'/></filter><rect width='100%' height='100%' filter='url(%23n)' opacity='.25'/></svg>");
  --dur:200ms; --ease:steps(3,end);
}
.ink{mix-blend-mode:multiply;}
```

# Art Deco (1920s Glamour)

**Also called:** deco, Gatsby style, 1920s, roaring twenties, geometric luxury
**In one sentence:** Glamorous symmetry — gold geometric lines, fans, sunbursts and tall elegant lettering on black or deep jewel tones.
**Picture it:** A black invitation with gold fan shapes in the corners, thin gold double borders and tall, narrow capital letters in the center.
**Feels like:** glamorous, opulent, festive, historic, celebratory.

**Use for:** events, weddings, hotels, bars/restaurants, premium spirits, theatre, galas, luxury promotions.
**Avoid for:** apps and tools, casual brands, minimal products.

## Overrides
| Area | Override |
|---|---|
| Color | Black #0B0B0B or deep jewel tones (emerald #0B3D2E, navy #0E1A3A, burgundy) + **gold** (#C9A646 / gradient #E8CF85 → #A7832E) + cream #F3E9D2. |
| Typography | Tall geometric display caps (Poiret One, "Limelight", "Federo", "Josefin Sans" uppercase, "Italiana"); wide letter-spacing. Elegant serif or light sans body. |
| Spacing / layout | **Symmetric, centered** compositions; framed panels; vertical emphasis. |
| Radius | 0; stepped corners and arches. |
| Borders | **Double/triple thin gold lines**, stepped frames, corner ornaments. |
| Depth | Flat with metallic gold gradients; no soft shadows. |
| Motion | Elegant reveals: lines drawing in, fans unfolding, slow fades (500–900ms). |
| Hover | Gold line draws under text, shimmer on gold. |
| Imagery / icons | Sunbursts, fans, chevrons, zigzags, stepped pyramids, geometric florals. |
| Components | Outlined gold buttons with uppercase tracked labels; framed cards. |

## Signature moves
1. Gold geometric ornaments (fans, sunbursts, chevrons).
2. Strict symmetry and frames.
3. Tall uppercase lettering with wide tracking.

## Do / Don't
- **Do** keep ornaments as frames and dividers.
- **Do** use gold sparingly to stay elegant.
- **Don't** use rounded modern UI shapes.
- **Don't** put long text in decorative display fonts.

## Accessibility watch-outs
- Gold on black is usually fine for large text but check small text; gold on cream fails.
- Decorative fonts only for headings.

## Starter tokens
```css
:root{
  --bg:#0B0B0B; --surface:#141414; --text:#F3E9D2; --text-2:#C8BC9F;
  --gold:#C9A646; --gold-grad:linear-gradient(180deg,#E8CF85 0%,#C9A646 50%,#A7832E 100%);
  --accent:var(--gold); --on-accent:#0B0B0B;
  --font-display:"Poiret One","Limelight",serif; --font-sans:"Josefin Sans",system-ui,sans-serif;
  --tracking-display:0.2em; --radius-control:0; --radius-container:0;
  --frame:1px solid var(--gold);
  --dur:700ms; --ease:cubic-bezier(.25,.1,.25,1);
}
```

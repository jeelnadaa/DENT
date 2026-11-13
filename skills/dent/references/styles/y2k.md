# Y2K (Early-2000s Digital)

**Also called:** Y2K aesthetic, millennium style, cyber Y2K, chrome Y2K, frutiger aero (close cousin)
**In one sentence:** Shiny chrome, bubbly glossy shapes, iridescent gradients, sparkles and techno optimism from around the year 2000.
**Picture it:** A silver chrome logo with a lens-flare sparkle, floating over a baby-blue and lilac gradient with bubbly glossy buttons.
**Feels like:** nostalgic, shiny, futuristic-retro, playful, pop.

**Use for:** fashion, music, Gen-Z brands, events, beauty, playful landing pages, creative portfolios.
**Avoid for:** serious tools, finance, enterprise, healthcare.

## Overrides
| Area | Override |
|---|---|
| Color | Iridescent/holographic gradients (baby blue #9AD8FF, lilac #C9A7FF, pink #FFB3E6, silver #DADDE3), chrome silvers, occasional lime/hot pink accents. |
| Typography | Futuristic/wide display (Orbitron, Michroma, "Syncopate", Monument Extended-like) or bubbly rounded (Baloo, "Righteous"); clean sans body. Chrome/gradient text effects on headlines. |
| Spacing / layout | Playful, floating, layered elements; stickers and badges scattered; can be centered and busy. |
| Radius | Very rounded/bubbly: pills and blobs (20px+). |
| Borders | Glossy gradient borders, white inner highlights. |
| Depth | Glossy highlights (white gradient on top half), chrome bevels, glows, lens flares, sparkles ✦. |
| Motion | Bouncy, floating loops, shimmer/sparkle animations, rotating 3D objects. |
| Hover | Shine sweep across buttons, glow intensifies, bounce. |
| Imagery / icons | 3D chrome objects, butterflies, stars/sparkles, blobby shapes, pixel cursors, early-web icons. |
| Components | Glossy "jelly" pill buttons, chrome toggles, rounded inputs with inner shadows. |

## Signature moves
1. Chrome / holographic gradients.
2. Glossy, bubbly, jelly-like buttons.
3. Sparkles ✦, stars and floating 3D shapes.
4. Wide futuristic display fonts.

## Do / Don't
- **Do** keep the body content area calm and readable.
- **Do** use effects on headlines, hero and buttons.
- **Don't** put body text on iridescent gradients.
- **Don't** overload every element with shine — pick hero moments.

## Accessibility watch-outs
- Pastel gradients + white text = fail. Use dark text on pastels.
- Looping sparkles/animations need pause under reduced motion.

## Starter tokens
```css
:root{
  --bg:linear-gradient(135deg,#E9F4FF 0%,#F3E8FF 50%,#FFE8F6 100%);
  --text:#1B1B3A; --text-2:#4B4B6E; --chrome:linear-gradient(180deg,#FFFFFF 0%,#C9CED6 45%,#8F96A3 55%,#E9ECF1 100%);
  --accent:#FF4FB4; --on-accent:#1B1B3A; --lime:#C6FF3D;
  --font-display:"Orbitron","Michroma",sans-serif; --font-sans:"Outfit",system-ui,sans-serif;
  --radius-control:999px; --radius-container:28px;
  --gloss:linear-gradient(180deg,rgb(255 255 255 / .7) 0%,rgb(255 255 255 / 0) 55%);
  --dur:300ms; --ease:cubic-bezier(.34,1.56,.64,1);
}
```

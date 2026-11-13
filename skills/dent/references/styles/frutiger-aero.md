# Frutiger Aero (Mid-2000s Glossy Nature-Tech)

**Also called:** aero, glossy 2000s, Windows Vista/7 style, web 2.0, eco-tech gloss
**In one sentence:** Mid-2000s optimism — glossy glass buttons, sky-blue and grass-green, bubbles, water, lens flares and clean humanist type.
**Picture it:** A shiny aqua button with a white gloss on top, floating over a photo of blue sky, green hills and water droplets.
**Feels like:** fresh, clean, optimistic, nostalgic, eco-tech.

**Use for:** nostalgic/playful brands, music, eco products, retro-tech projects, personal sites.
**Avoid for:** serious modern products (reads dated if not intentional).

## Overrides
| Area | Override |
|---|---|
| Color | Sky blue #4FC3F7, aqua #00B8D9, grass green #7ED957, white, silver; gradients from light to saturated. |
| Typography | Humanist sans (Frutiger-like: "Hind", "Segoe UI", "Myriad"-like "PT Sans", "Mukta"). |
| Spacing / layout | Rounded panels over nature photography; web 2.0 layouts with reflections. |
| Radius | Rounded 8–16px, pill buttons, bubbles. |
| Borders | Glossy light borders. |
| Depth | **Glossy highlights** (white gradient top half), reflections under objects, glass, bubbles, lens flares. |
| Motion | Smooth fades, floating bubbles, shine sweeps. |
| Hover | Brighter glow, shine sweep. |
| Imagery / icons | Sky, water, grass, bubbles, glossy 3D icons, aquariums, fish. |
| Components | Glossy "aqua" pill buttons, glass panels, reflective badges. |

## Signature moves
1. Glossy aqua/green buttons with white shine.
2. Nature imagery (sky, water, grass) + tech.
3. Bubbles, reflections and lens flares.

## Do / Don't
- **Do** use it intentionally as nostalgia.
- **Don't** put text on busy photos without panels.

## Accessibility watch-outs
- White text on light aqua/green gradients fails — darken button bases or use dark text.

## Starter tokens
```css
:root{
  --bg:linear-gradient(180deg,#BDE9FF 0%,#E9F9FF 60%,#CFF5C4 100%);
  --text:#0E3446; --text-2:#2E5A6E; --aqua:#0089A8; --green:#3E8E1E;
  --accent:var(--aqua); --on-accent:#FFFFFF;
  --gloss:linear-gradient(180deg,rgb(255 255 255 / .85) 0%,rgb(255 255 255 / .2) 50%,rgb(255 255 255 / 0) 51%);
  --font-sans:"PT Sans","Segoe UI",system-ui,sans-serif;
  --radius-control:999px; --radius-container:16px;
  --dur:300ms; --ease:cubic-bezier(.2,0,0,1);
}
```

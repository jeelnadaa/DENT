# Retro-Futurism (Space Age)

**Also called:** space age, atomic age, 60s-70s sci-fi, NASA-punk, mid-century futurism
**In one sentence:** The future as imagined in the 1960s–70s — rounded space-age shapes, warm oranges and creams, mission-control panels and bold sci-fi type.
**Picture it:** A mission-control panel in cream and burnt orange, rounded-rectangle screens, chunky switches and a rocket illustration in the corner.
**Feels like:** optimistic, adventurous, nostalgic, warm-technical.

**Use for:** space/aerospace, science education, music, creative tech brands, events, games.
**Avoid for:** conservative corporate, minimal productivity tools.

## Overrides
| Area | Override |
|---|---|
| Color | Warm retro: cream #F2E8D5, burnt orange #D9541E, mustard #E3A81B, avocado/teal #2F6F6A, brown #3B2A20, off-black. |
| Typography | Space-age display ("Space Mono" for data, "Michroma", "Orbitron" lightly, "Eurostile"-like "Audiowide", rounded "Righteous"); NASA-like wide caps for labels. |
| Spacing / layout | Panel/console layouts, stripes, rounded screens; strong horizontal bands. |
| Radius | Rounded-rectangle "TV screen" shapes (16–32px), pills, circles (portholes). |
| Borders | Thick colored stripes (racing stripes, multi-band lines). |
| Depth | Subtle bevels on panels; mostly flat with stripes and grain. |
| Motion | Mechanical: switches flip, dials rotate, counters roll, rocket-launch transitions. |
| Hover | Indicator lights turn on, stripes extend. |
| Imagery / icons | Rockets, planets, orbits, starbursts, retro illustrations, NASA-like patches. |
| Components | Chunky toggle switches, pill buttons with indicator lights, numeric readouts in mono. |

## Signature moves
1. Warm 70s palette (cream, orange, mustard, teal, brown).
2. Multi-band retro stripes.
3. Mission-control panels and readouts.
4. Space imagery.

## Do / Don't
- **Do** combine retro shapes with modern clarity and spacing.
- **Don't** use neon (that's synthwave) or cold blue tech palettes.

## Accessibility watch-outs
- Mustard/orange text on cream fails — use brown/off-black for text.

## Starter tokens
```css
:root{
  --bg:#F2E8D5; --surface:#FBF4E6; --text:#2A1E16; --text-2:#5A4636;
  --orange:#C2481A; --mustard:#E3A81B; --teal:#2F6F6A; --brown:#3B2A20;
  --accent:var(--orange); --on-accent:#FFFFFF;
  --stripes:linear-gradient(180deg,#E3A81B 0 33%,#D9541E 33% 66%,#8C2F1B 66% 100%);
  --font-display:"Michroma","Audiowide",sans-serif; --font-mono:"Space Mono",monospace; --font-sans:"Outfit",system-ui,sans-serif;
  --radius-control:999px; --radius-container:24px;
  --dur:250ms; --ease:cubic-bezier(.65,0,.35,1);
}
```

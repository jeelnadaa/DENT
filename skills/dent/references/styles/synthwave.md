# Synthwave / Vaporwave (Retro 80s Neon)

**Also called:** retrowave, outrun, 80s neon, vaporwave (pastel, ironic variant)
**In one sentence:** 1980s sci-fi nostalgia — neon pink and cyan on deep purple-black, glowing grids, sunsets and chrome text.
**Picture it:** A purple night sky, a striped neon sun setting behind a glowing pink grid floor that stretches to the horizon.
**Feels like:** nostalgic, dreamy, electric, nightlife, retro-futuristic.

Variants:
- **Synthwave/Outrun:** dark, neon, intense.
- **Vaporwave:** pastel pink/teal, Greek statues, old Windows UI, ironic and dreamy.

**Use for:** music, games, events, nightlife, creative portfolios, entertainment.
**Avoid for:** productivity, finance, health, anything serious.

## Overrides
| Area | Override |
|---|---|
| Color | Deep purple/navy background (#1A0B2E, #0D0221). Neon pink #FF2E97, cyan #00F0FF, purple #B026FF, orange-yellow sunset gradient (#FF8A00 → #FF2E97). Vaporwave: pastel pink #FF9ECD, mint #8EF6E4, lavender. |
| Typography | Chrome/italic display (Monoton, "Audiowide", "Orbitron", script like "Mr Dafoe" for accents); clean sans/mono body. Neon glow via text-shadow. |
| Spacing / layout | Centered hero with horizon composition; bold sections. |
| Radius | 0–8px (sharp, techy). |
| Borders | Neon outlines with glow. |
| Depth | **Glow** (multiple colored text/box shadows), perspective grid floors, scanlines. |
| Motion | Grid moving toward viewer, flicker on neon (subtle, not flashing), slow sun pulse. |
| Hover | Neon glow intensifies, color shift pink ↔ cyan. |
| Imagery / icons | Sunsets, palm trees, wireframe mountains, sports cars, cassettes, Greek busts (vaporwave), VHS noise. |
| Components | Outlined neon buttons, dark inputs with neon focus glow. |

## Signature moves
1. Neon pink + cyan glow on deep purple.
2. Perspective grid floor and striped sun.
3. Chrome or neon-glow headline text.

## Do / Don't
- **Do** keep body text plain (no glow) for readability.
- **Do** use glow on a few hero elements.
- **Don't** make neon text small.
- **Don't** add rapid flicker.

## Accessibility watch-outs
- **[Rule]** Neon flicker must never flash more than 3 times/sec; prefer no flicker.
- Glow blurs letterforms — keep glowing text large.

## Starter tokens
```css
:root{
  --bg:#12052B; --surface:#1E0B3D; --text:#F4ECFF; --text-2:#C3B3E6;
  --pink:#FF2E97; --cyan:#00F0FF; --purple:#B026FF; --sun:linear-gradient(180deg,#FFD319 0%,#FF8A00 40%,#FF2E97 100%);
  --accent:var(--cyan); --on-accent:#12052B;
  --font-display:"Audiowide","Orbitron",sans-serif; --font-sans:"Rajdhani","Outfit",sans-serif;
  --glow-pink:0 0 6px #FF2E97,0 0 18px rgb(255 46 151 / .6); --glow-cyan:0 0 6px #00F0FF,0 0 18px rgb(0 240 255 / .6);
  --radius-control:4px; --radius-container:8px;
  --dur:250ms; --ease:cubic-bezier(.2,0,0,1);
}
```

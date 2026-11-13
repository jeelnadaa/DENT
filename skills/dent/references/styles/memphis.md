# Memphis (80s Postmodern Pattern)

**Also called:** Memphis design, Memphis Group style, 80s geometric, postmodern pop
**In one sentence:** Loud, playful geometry — squiggles, zigzags, dots, triangles and clashing bright colors scattered over the layout.
**Picture it:** A poster with a pink background, black-and-white zigzag stripes, a yellow circle, a turquoise squiggle and confetti dots everywhere.
**Feels like:** fun, chaotic, bold, youthful, optimistic.

**Use for:** kids/youth brands, creative events, party/entertainment, playful marketing, education with energy.
**Avoid for:** serious, data-heavy, luxury or trust-critical products.

## Overrides
| Area | Override |
|---|---|
| Color | Bright clashing: hot pink #FF5FA2, turquoise #2EC4B6, yellow #FFD60A, purple #7B2CBF, red-orange #FF6B35 + black and white patterns. Background often pastel or white. |
| Typography | Bold geometric or quirky display (Righteous, "Bungee", "Rubik Mono One", "Shrikhand"); friendly sans body (Poppins, Rubik). |
| Spacing / layout | Content in clear blocks, surrounded by scattered geometric decorations; slight rotations. |
| Radius | Mix of perfect circles and sharp shapes; controls 0 or pill. |
| Borders | Thick black outlines (3px). |
| Depth | Hard offset shadows (no blur), often colored. |
| Motion | Floating/rotating shapes, bouncy entrances. |
| Hover | Wiggle, color swap, bounce. |
| Imagery / icons | Squiggles, zigzags, dots, grids, triangles, terrazzo patterns; flat illustrations. |
| Components | Bold colored buttons with black outline and hard shadow (similar to neo-brutalism). |

## Signature moves
1. Scattered geometric shapes and squiggles.
2. Black-and-white patterns (zigzag, dots, grid) mixed with bright colors.
3. Clashing color combos used on purpose.

## Do / Don't
- **Do** keep decorations in margins/backgrounds; keep content zones clear and readable.
- **Do** reuse the same shape set across pages.
- **Don't** put patterns behind body text.
- **Don't** let decorations cover interactive elements.

## Accessibility watch-outs
- Pattern backgrounds behind text destroy legibility — use solid panels for text.
- Constant floating motion must stop under reduced motion.

## Starter tokens
```css
:root{
  --bg:#FFF4F9; --surface:#FFFFFF; --text:#111111; --text-2:#3D3D3D;
  --pink:#FF5FA2; --teal:#2EC4B6; --yellow:#FFD60A; --purple:#7B2CBF; --orange:#FF6B35;
  --accent:var(--yellow); --on-accent:#111111;
  --font-display:"Bungee","Righteous",sans-serif; --font-sans:"Rubik",system-ui,sans-serif;
  --border-w:3px; --radius-control:999px; --radius-container:0;
  --shadow-1:5px 5px 0 #111;
  --dur:250ms; --ease:cubic-bezier(.34,1.56,.64,1);
}
```

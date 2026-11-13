# Pixel Art (8-bit / 16-bit Retro Game)

**Also called:** 8-bit, 16-bit, retro gaming, pixel UI, arcade style
**In one sentence:** Everything looks like it's from an old video game — pixel fonts, blocky borders, limited palettes and chunky sprites.
**Picture it:** A game start screen: "PRESS START" blinking in a pixel font, a dialogue box with a thick stepped border, and little pixel hearts as health.
**Feels like:** nostalgic, fun, playful, nerdy, game-like.

**Use for:** games, game studios, gamified apps, kids' coding, playful portfolios, events/hackathons.
**Avoid for:** serious, professional or reading-heavy products.

## Overrides
| Area | Override |
|---|---|
| Color | **Limited palette** (8–16 colors), e.g. NES/PICO-8-like: #000000, #1D2B53, #7E2553, #008751, #AB5236, #FF004D, #FFA300, #FFEC27, #29ADFF, #FFF1E8. |
| Typography | Pixel fonts for headings/UI ("Press Start 2P", "Silkscreen", "Pixelify Sans", VT323); readable sans or larger pixel font for body. Render at multiples of the font's pixel grid. |
| Spacing / layout | Snap everything to a pixel grid (multiples of 4px or 8px). Dialog boxes, panels like game menus. |
| Radius | 0 — or **stepped "pixel" corners** (made with box-shadows or clip-path). |
| Borders | Thick (4px) solid borders, often double or with pixel bevel (light top-left, dark bottom-right). |
| Depth | Pixel bevels; hard 4px drop shadows, no blur. |
| Motion | **Stepped animation** (`steps()` timing), sprite animation, blinking text, screen shake on errors (subtle). |
| Hover | Arrow/cursor sprite appears ▶, color swap, 4px jump. |
| Imagery / icons | Pixel sprites and icons; disable smoothing: `image-rendering: pixelated`. |
| Components | Chunky bordered buttons that press down 4px; health/progress bars as blocks; dialog boxes with typed text. |

## Signature moves
1. Pixel fonts and pixel-perfect sprites.
2. Limited retro palette.
3. Thick stepped borders and hard shadows.
4. Stepped (non-smooth) animations.

## Do / Don't
- **Do** keep pixel scaling crisp (integer multiples, `image-rendering: pixelated`).
- **Do** use a readable font for long text.
- **Don't** use smooth gradients or blur.
- **Don't** set long paragraphs in small pixel fonts.

## Accessibility watch-outs
- Pixel fonts at small sizes are hard to read — minimum 16px for pixel UI text, prefer normal font for body.
- Blinking "PRESS START" must stop under reduced motion.

## Starter tokens
```css
:root{
  --bg:#1D2B53; --surface:#000000; --text:#FFF1E8; --text-2:#C2C3C7;
  --red:#FF004D; --orange:#FFA300; --yellow:#FFEC27; --green:#00E436; --blue:#29ADFF;
  --accent:var(--yellow); --on-accent:#000000;
  --font-pixel:"Press Start 2P","Silkscreen",monospace; --font-sans:"Pixelify Sans",system-ui,sans-serif;
  --px:4px; --radius-control:0; --radius-container:0;
  --shadow-1:4px 4px 0 #000;
  --ease:steps(4,end); --dur:200ms;
}
img.pixel{image-rendering:pixelated;}
```

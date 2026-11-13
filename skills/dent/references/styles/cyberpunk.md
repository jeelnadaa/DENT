# Cyberpunk (Neon Dystopian HUD)

**Also called:** cyber, techwear UI, sci-fi HUD, futuristic interface, "Blade Runner style"
**In one sentence:** A high-tech dystopian interface — black, acid yellow and neon accents, angular cut corners, glitch effects and HUD details.
**Picture it:** A game menu: black background, acid-yellow panels with one corner sliced off, red warning labels, tiny technical numbers and a glitch flicker on the title.
**Feels like:** edgy, aggressive, technical, futuristic, rebellious.

**Use for:** games, esports, techwear fashion, hacker/security tools (marketing), sci-fi entertainment.
**Avoid for:** calm, trustworthy or mainstream products.

## Overrides
| Area | Override |
|---|---|
| Color | Black #0A0A0A / dark steel, **acid yellow #F3E600**, neon cyan #00FFF0, hot magenta #FF003C, warning red. Mostly dark with sharp neon accents. |
| Typography | Angular/technical display (Rajdhani, Orbitron, "Chakra Petch", "Oxanium", "Blender"-like); **monospace** for data and labels; uppercase labels with codes ("SYS_01 // ACCESS"). |
| Spacing / layout | HUD-like: panels, brackets, coordinates, data readouts; dense but structured; diagonal elements. |
| Radius | **0 with cut/chamfered corners** (clip-path polygons). |
| Borders | 1–2px neon lines, corner brackets ⌜ ⌟, dashed lines. |
| Depth | Glow, scanlines, chromatic aberration (red/cyan offset), noise. |
| Motion | **Glitch** (short, rare), typing/decoding text, scan-line sweeps, quick slides. |
| Hover | Glitch jitter, color invert, bracket expansion. |
| Imagery / icons | Neon city, techwear, wireframes, barcodes, warning symbols, technical schematics. |
| Components | Chamfered buttons (yellow fill, black text), bracket-framed inputs, progress bars as segmented blocks. |

## Signature moves
1. Chamfered (cut-corner) shapes.
2. Acid yellow / neon accents on black.
3. HUD details: codes, coordinates, brackets, barcodes.
4. Glitch and decode-text effects.

## Do / Don't
- **Do** keep glitches brief and occasional.
- **Do** make the HUD "noise" decorative and small; main content clean.
- **Don't** glitch body text or controls the user is reading.
- **Don't** use rounded, soft shapes.

## Accessibility watch-outs
- **[Rule]** Glitch/flicker effects: no more than 3 flashes per second; disable under reduced motion.
- Neon magenta/red text on black may fail at small sizes — check.

## Starter tokens
```css
:root{
  --bg:#0A0A0A; --surface:#141414; --text:#E8E8E8; --text-2:#9A9A9A;
  --yellow:#F3E600; --cyan:#00FFF0; --magenta:#FF003C;
  --accent:var(--yellow); --on-accent:#0A0A0A;
  --font-display:"Chakra Petch","Rajdhani",sans-serif; --font-mono:"Share Tech Mono","JetBrains Mono",monospace;
  --cut:polygon(0 0,calc(100% - 14px) 0,100% 14px,100% 100%,14px 100%,0 calc(100% - 14px));
  --dur:120ms; --ease:steps(4,end);
}
.btn{clip-path:var(--cut);background:var(--yellow);color:#0A0A0A;text-transform:uppercase;letter-spacing:.08em;}
```

# Terminal (Hacker / Command Line)

**Also called:** CLI style, hacker, monospace UI, retro computer, CRT, ASCII
**In one sentence:** The interface looks like a command-line terminal — monospace text, green/amber on black, blinking cursor, ASCII art.
**Picture it:** A black screen with green text, a blinking block cursor after `> _`, and a menu built from ASCII boxes.
**Feels like:** technical, nerdy, raw, nostalgic, "for builders".

**Use for:** developer portfolios, dev tools marketing, CTF/security, hackathons, docs for CLIs, easter eggs.
**Avoid for:** general consumer apps, non-technical audiences.

## Overrides
| Area | Override |
|---|---|
| Color | Black/very dark background (#0C0C0C); phosphor green #33FF66, amber #FFB000, or white-grey #D0D0D0 text. Optional second color for prompts/links. |
| Typography | **Monospace only** (JetBrains Mono, IBM Plex Mono, Fira Code, VT323 for CRT feel). Single size mostly; hierarchy via color, CAPS, ASCII underlines (=====). |
| Spacing / layout | Character grid: everything aligns to monospace columns; left-aligned; line-based layout. |
| Radius | 0. |
| Borders | ASCII/box-drawing characters (┌─┐ │ └─┘) or 1px solid lines. |
| Depth | None; optional CRT effects (scanlines, slight glow, vignette) — subtle. |
| Motion | Typing effect, blinking cursor (≈1s cycle), line-by-line output. |
| Hover | Inverted colors (green background, black text), `>` prefix appears. |
| Imagery / icons | ASCII art, no photos (or dithered/pixelated ones). |
| Components | Buttons as `[ Enter ]` or `> run`, inputs as prompt lines with cursor, lists as numbered options. Optional real command input. |

## Signature moves
1. Monospace everything.
2. Phosphor green/amber on black.
3. Blinking cursor and typed-out text.
4. ASCII boxes and art.

## Do / Don't
- **Do** offer normal clickable navigation as well as "commands".
- **Do** keep typing animations short or skippable.
- **Don't** force users to type commands to use the site.
- **Don't** overdo CRT distortion.

## Accessibility watch-outs
- Typing effects must not delay content; reveal instantly under reduced motion.
- ASCII art should be hidden from screen readers (aria-hidden) with a text alternative.

## Starter tokens
```css
:root{
  --bg:#0C0C0C; --text:#33FF66; --text-2:#1FAF47; --accent:#FFB000; --on-accent:#0C0C0C;
  --font-mono:"JetBrains Mono","IBM Plex Mono",ui-monospace,monospace;
  --radius-control:0; --radius-container:0;
  --glow:0 0 4px rgb(51 255 102 / .5);
  --dur:0ms;
}
.cursor{display:inline-block;width:.6ch;height:1.1em;background:currentColor;animation:blink 1s steps(1) infinite;}
@keyframes blink{50%{opacity:0;}}
@media (prefers-reduced-motion:reduce){.cursor{animation:none;}}
```

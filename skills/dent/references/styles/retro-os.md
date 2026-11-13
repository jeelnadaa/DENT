# Retro OS (90s Desktop)

**Also called:** retro desktop, 90s computer, classic OS, beveled UI, Windows 95 style, classic Mac style, "old computer"
**In one sentence:** The interface looks like a 1990s desktop operating system — grey beveled windows with title bars, chunky buttons and pixel-crisp icons on a flat desktop color.
**Picture it:** A teal desktop with a grey window; the window has a dark blue title bar with white bold text and three tiny square buttons; inside, raised grey buttons with 2px light/dark bevels.
**Feels like:** nostalgic, playful, honest, tactile, a little ironic.

**Use for:** personal sites and portfolios, indie games and tools, creative agencies, event/campaign microsites, nostalgic products, easter-egg modes.
**Avoid for:** serious finance/health products, enterprise apps, anything where the joke would undermine trust.

This style is an homage to an era, not a copy of any specific operating system: use original icons and wording, never real OS logos, sounds or system artwork.

## Overrides
| Area | Override |
|---|---|
| Color | Desktop background in a flat saturated color (teal #008080 or a muted blue); window/control grey #C0C0C0; title bar navy #000080 with white text (inactive: grey #808080); black text; white and dark-grey (#808080) for bevels. |
| Typography | Pixel-crisp sans for UI (e.g. a pixel/bitmap-style font for titles, Tahoma/Verdana-like system sans for body); bold title bars; small UI sizes (12–14px) — but body text ≥ 16px on content pages. |
| Spacing / layout | Content inside windows; windows may be draggable on desktop; dense, functional layouts; menu bar ("File  Edit  View  Help") inside windows. |
| Radius | 0 everywhere. |
| Borders | **Bevels:** raised = light top-left + dark bottom-right (2px each); pressed/inset fields = reversed. |
| Depth | Bevels only; optional hard 1–2px drop shadow under windows. No blur. |
| Motion | Almost none, instant. Optional window "zoom" outline animation; progress bars in chunky blocks. |
| Hover | Usually no hover change (authentic) — but keep a visible focus ring (dotted 1px inside buttons is on-style). |
| Imagery / icons | 32×32 pixel-art icons, original; dithered images; desktop icons with labels under them. |
| Components | Beveled buttons; inset text fields with white background; checkboxes as small inset squares with ✓; title-bar windows as cards; taskbar/dock as bottom nav; dialogs with an icon + message + OK/Cancel. |

## Signature moves
1. Beveled grey controls (light top-left, dark bottom-right).
2. Windows with a solid title bar and tiny square control buttons.
3. Flat saturated desktop color behind everything.
4. Pixel-art icons with labels.

## Do / Don't
- **Do** keep real usability: windows must also work as normal scrollable content on mobile (stack them full-width; no dragging required).
- **Do** use the window metaphor to organize content (each section a "window").
- **Don't** reproduce real OS logos, startup sounds, error dialogs or icons — make original ones.
- **Don't** make users "double-click" to open things; single click/tap with clear affordance.

## Accessibility watch-outs
- Bevels alone may not reach 3:1 against grey — ensure the dark bevel edge (#808080 or darker, often #000 outer line) gives controls a clear boundary.
- Small pixel fonts: keep content text ≥ 16px and readable; pixel fonts only for titles/labels.
- Draggable windows need a keyboard alternative and must not trap focus.
- Fake "error dialogs" as decoration confuse screen reader users — don't use real alert roles for decorative windows.

## Starter tokens
```css
:root{
  --desktop:#008080; --face:#C0C0C0; --text:#000; --field:#FFF;
  --hi:#FFF; --shadow:#808080; --dark:#000;
  --title:#000080; --title-text:#FFF; --title-inactive:#808080;
  --font-ui:Tahoma,Verdana,"Segoe UI",system-ui,sans-serif;
  --radius-control:0; --radius-container:0; --dur:0ms;
}
.btn{background:var(--face);color:var(--text);border:0;padding:6px 16px;
  box-shadow:inset -1px -1px var(--dark),inset 1px 1px var(--hi),inset -2px -2px var(--shadow),inset 2px 2px #DFDFDF;}
.btn:active{box-shadow:inset 1px 1px var(--dark),inset -1px -1px var(--hi),inset 2px 2px var(--shadow),inset -2px -2px #DFDFDF;}
.btn:focus-visible{outline:1px dotted var(--text);outline-offset:-5px;}
.field{background:var(--field);box-shadow:inset 1px 1px var(--shadow),inset -1px -1px var(--hi),inset 2px 2px var(--dark),inset -2px -2px #DFDFDF;}
```

# Glassmorphism

**Also called:** glass UI, frosted glass, translucent UI, acrylic, liquid glass
**In one sentence:** Panels look like frosted glass floating over a colorful background — you see blurred color through them.
**Picture it:** A frosted bathroom window in front of a sunset: you see soft colors behind, but nothing sharp.
**Feels like:** light, airy, futuristic, premium, layered.

**Use for:** music/media apps, weather, crypto/fintech dashboards, OS-like interfaces, landing page heroes, overlays and nav bars.
**Avoid for:** text-heavy reading, forms-heavy enterprise tools, low-end devices (blur is expensive).

## Overrides
| Area | Override |
|---|---|
| Color | **A colorful background is required** (gradient, blurred blobs, photo). Glass panels: white at 10–25% opacity (light) or black/white at 6–15% (dark). Text solid white or near-black. |
| Typography | Clean geometric/neo-grotesque sans (SUSE, Albert Sans, Rethink Sans, SF Pro on Apple). Medium weights. |
| Spacing / layout | Floating cards with clear gaps so the background shows between them. |
| Radius | Large: controls 12px, containers 20–28px. |
| Borders | **1px semi-transparent white border** (rgba 255,255,255,.25–.4) — catches "light" on the glass edge. |
| Depth | `backdrop-filter: blur(16–32px) saturate(140–180%)`, plus a soft large shadow. Layers = more blur/opacity. |
| Motion | Smooth, floaty: 250–400ms ease-out; background blobs drift slowly (paused under reduced motion). |
| Hover | Glass gets slightly more opaque/brighter; subtle highlight sweep. |
| Imagery / icons | Gradient blobs, 3D renders, soft glows; icons simple and white/filled. |
| Components | Glass buttons for secondary; **primary stays solid** (solid fill) so it stands out. Inputs as glass with brighter border on focus. |

## Signature moves
1. Background blur through translucent panels.
2. A vivid, soft background behind the glass.
3. Thin light border on glass edges.
4. Big rounded corners and floating layers.

## Do / Don't
- **Do** limit glass to a few surfaces (nav, cards, modals).
- **Do** add a tint behind text so it stays readable no matter what's behind.
- **Don't** put glass on a plain flat background — the effect disappears.
- **Don't** stack many blurred layers (performance + mud).

## Accessibility watch-outs
- **Contrast varies with what's behind the glass.** Test text against the lightest and darkest spots of the background; raise panel opacity until it passes 4.5:1 everywhere.
- Provide a fallback when `backdrop-filter` is unsupported or "reduce transparency" is on: a solid semi-opaque surface.

## Starter tokens
```css
:root{
  --bg:linear-gradient(in oklch 135deg,#0F5F66 0%,#2B4C8C 50%,#7C2D5E 100%); /* any rich backdrop from the concept; avoid the indigo→purple→pink template gradient */
  --glass:rgb(255 255 255 / .16); --glass-strong:rgb(255 255 255 / .28); --glass-border:rgb(255 255 255 / .35);
  --text:#FFFFFF; --text-2:rgb(255 255 255 / .8); --accent:#FFFFFF; --on-accent:#1D3A5F;
  --font-sans:"SUSE","Albert Sans",system-ui,sans-serif;
  --radius-control:12px; --radius-container:24px;
  --blur:blur(24px) saturate(160%);
  --shadow-1:0 8px 32px rgb(0 0 0 / .18);
  --dur:300ms; --ease:cubic-bezier(.16,1,.3,1);
}
.glass{background:var(--glass);backdrop-filter:var(--blur);-webkit-backdrop-filter:var(--blur);border:1px solid var(--glass-border);border-radius:var(--radius-container);box-shadow:var(--shadow-1);}
@media (prefers-reduced-transparency: reduce){.glass{background:rgb(40 20 90 / .92);backdrop-filter:none;}}
```

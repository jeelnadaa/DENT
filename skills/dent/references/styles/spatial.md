# Spatial (visionOS-like / Depth UI)

**Also called:** spatial UI, visionOS style, AR/VR UI, 3D glass windows, depth UI, liquid glass
**In one sentence:** Floating translucent windows in 3D space, with depth, soft lighting, large rounded panels and focus-based highlights.
**Picture it:** Frosted glass windows floating in a living room, gently glowing at the edges, with a button that lights up when you look at it.
**Feels like:** futuristic, immersive, calm, premium, airy.

**Use for:** AR/VR apps, futuristic product concepts, premium media apps, OS-like web experiences, launch pages for spatial products.
**Avoid for:** dense data tools, low-end devices, conservative audiences.

## Overrides
| Area | Override |
|---|---|
| Color | Mostly neutral glass (white/grey translucency) over the environment or a photo/gradient; color comes from content. White text. Accent rarely (system blue). |
| Typography | System-like sans with **heavier weights** for legibility on glass (SF Pro-like: Satoshi, General Sans, "Geist") — medium for body, bold for titles. Larger sizes than flat UI. |
| Spacing / layout | Content in floating windows/panels with generous padding (24–32px); tab bars and toolbars float outside the window edges ("ornaments"). |
| Radius | **Very large and continuous:** windows 32–46px, buttons pill/circle. |
| Borders | Subtle light edge (gradient border, brighter top). |
| Depth | Glass material (blur + light tint), **layered depth**, soft shadows beneath floating panels, specular highlights. Parallax of layers on pointer/tilt. |
| Motion | Smooth springs; panels scale and fade with depth; hover/focus highlight glides. |
| Hover/focus | **Highlight glow follows the pointer/gaze** on buttons; elements lift (scale 1.04) slightly toward the user. |
| Imagery / icons | 3D, layered app icons; immersive photography/environments; SF Symbols-like icons. |
| Components | Glass pill buttons, segmented controls, floating tab bars, sheets that slide forward in depth. |

## Signature moves
1. Floating glass windows with very large radii.
2. Layered depth and parallax.
3. Pointer/gaze highlight on interactive elements.
4. Floating toolbars outside the main window.

## Do / Don't
- **Do** use heavier font weights and high contrast on glass.
- **Do** keep a clear focus highlight on every interactive element.
- **Don't** put too many floating layers at once.
- **Don't** use thin fonts or small text.

## Accessibility watch-outs
- Same as glassmorphism: test contrast on worst-case backgrounds; provide reduced-transparency fallback.
- Parallax/tilt must disable under reduced motion.

## Starter tokens
```css
:root{
  --env:linear-gradient(160deg,#4B6A88 0%,#2C3E50 100%);
  --glass:rgb(128 128 128 / .30); --glass-strong:rgb(255 255 255 / .18); --edge:linear-gradient(180deg,rgb(255 255 255 / .5),rgb(255 255 255 / .08));
  --text:#FFFFFF; --text-2:rgb(255 255 255 / .82); --accent:#0A84FF; --on-accent:#FFFFFF;
  --font-sans:"Satoshi","Manrope",system-ui,-apple-system,sans-serif;
  --radius-control:999px; --radius-container:40px;
  --blur:blur(40px) saturate(150%);
  --shadow-float:0 30px 60px rgb(0 0 0 / .25);
  --dur:350ms; --ease:cubic-bezier(.16,1,.3,1);
}
```

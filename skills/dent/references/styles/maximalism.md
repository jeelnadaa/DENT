# Maximalism

**Also called:** more is more, eclectic, busy, collage, bold maximal, dopamine design
**In one sentence:** Rich, layered and loud on purpose — many colors, patterns, fonts, images and textures combined with confidence.
**Picture it:** A fashion site where a collage of photos, stickers, patterned backgrounds, three bold fonts and a spinning badge all overlap — chaotic but clearly curated.
**Feels like:** exciting, expressive, bold, artistic, joyful.

**Use for:** fashion, music, art, festivals, creative agencies, youth brands, editorial features.
**Avoid for:** tools, forms, finance, healthcare, anything where speed and clarity come first.

## Overrides
| Area | Override |
|---|---|
| Color | Many saturated colors, clashing on purpose, plus patterns — but drawn from a **defined palette (6–10 colors)** so it stays curated. |
| Typography | 2–4 contrasting display fonts (serif + grotesk + script/display) with huge size range; type on paths, rotated, outlined. One plain readable font for body. |
| Spacing / layout | Layered collage: overlapping images, text and shapes; broken grid; dense. |
| Radius | Mixed on purpose (circles, sharp, blobs). |
| Borders | Mixed: thick outlines, stickers, frames. |
| Depth | Layering, cutouts, stickers, drop shadows, textures (paper, halftone). |
| Motion | Lots: rotating badges, marquees, parallax layers, cursor trails — but each optional and pausable. |
| Hover | Big, surprising reactions: images pop up, colors flip, elements spin. |
| Imagery / icons | Collages, cutout photos, patterns, illustrations, textures, stickers, emoji. |
| Components | Expressive custom buttons and cursors — but forms and checkout stay standard and calm. |

## Signature moves
1. Layered collage of images, type and patterns.
2. Multiple bold fonts and many colors — curated.
3. Constant visual surprise and motion.

## Do / Don't
- **Do** keep a clear path: navigation, CTA and key info must still stand out (give them the calmest, highest-contrast treatment).
- **Do** keep forms, checkout and settings calm.
- **Don't** confuse maximal with random — repeat motifs so it feels designed.
- **Don't** put body text over patterns.

## Accessibility watch-outs
- All motion must respect reduced motion and be pausable.
- Check contrast of every text-on-color combination; busy backgrounds behind text are not allowed.

## Starter tokens
```css
:root{
  --bg:#FFF1E0; --text:#160F29; --text-2:#3E3458;
  --c1:#FF3D7F; --c2:#00C2A8; --c3:#FFD23F; --c4:#3A2BFF; --c5:#FF7A00; --c6:#9B5DE5;
  --accent:var(--c4); --on-accent:#FFFFFF;
  --font-display-1:"Shrikhand",serif; --font-display-2:"Syne",sans-serif; --font-display-3:"Instrument Serif",serif; --font-sans:"DM Sans",system-ui,sans-serif;
  --shadow-1:6px 6px 0 #160F29;
  --dur:350ms; --ease:cubic-bezier(.34,1.56,.64,1);
}
```

# Anti-Design / Experimental

**Also called:** experimental, deconstructed, chaotic, post-internet, "weird web", new ugly
**In one sentence:** Breaks design rules on purpose — clashing type, overlapping elements, distorted images and unexpected interactions to provoke and stand out.
**Picture it:** An artist's site where text overlaps images, a heading is stretched sideways, the cursor leaves a trail, and the nav is scattered around the screen edges.
**Feels like:** provocative, artistic, unpredictable, raw, bold.

Difference from **Brutalism**: brutalism is raw and plain (defaults, structure); anti-design is **chaotic and expressive** (distortion, overlap, rule-breaking).

**Use for:** artists, experimental studios, music releases, fashion drops, festivals, art projects.
**Avoid for:** anything users must use efficiently or trust: tools, commerce checkout, healthcare, finance.

## Overrides
| Area | Override |
|---|---|
| Color | Anything — often harsh (acid green, RGB primaries, neon) or a deliberate "wrong" combination. Keep a defined set. |
| Typography | Distorted, stretched (font-stretch / scaleX), mixed fonts, overlapping lines, extreme sizes, vertical text. Body still in one readable font. |
| Spacing / layout | Broken grids, overlap, elements off-canvas, random-feeling placement (but intentional). |
| Radius | Anything. |
| Borders | Anything. |
| Depth | Blend modes (difference, exclusion), distortion, glitches. |
| Motion | Unexpected: cursor trails, elements following the cursor, things that react strangely. |
| Hover | Distortion, blend-mode inversion, element runs away (only for decorative elements). |
| Imagery / icons | Distorted/pixelated/collaged images, 3D objects, scans. |
| Components | Custom everything — but **core interactive components still follow the [Rule]s**. |

## Signature moves
1. Intentional rule-breaking (overlap, distortion, clashing).
2. Blend modes and unusual interactions.
3. Surprising, art-gallery feel.

## Do / Don't
- **Do** keep at least the navigation, content text and CTAs usable and findable.
- **Do** break rules consistently so it reads as a choice, not a bug.
- **Don't** break accessibility rules — those are never part of the "anti".
- **Don't** use for flows with real tasks.

## Accessibility watch-outs
- Overlapping text must not hide readable content; keep a clean reading layer.
- Every effect needs a reduced-motion version; nothing flashes > 3 times/sec.

## Starter tokens
```css
:root{
  --bg:#E8E8E8; --text:#000000; --acid:#C6FF00; --rgb-red:#FF0000; --rgb-blue:#0000FF;
  --accent:var(--rgb-blue); --on-accent:#FFFFFF;
  --font-display:"Syne","Unbounded",sans-serif; --font-sans:"Inter",system-ui,sans-serif; --font-serif:"Times New Roman",serif;
  --dur:400ms; --ease:cubic-bezier(.68,-0.6,.32,1.6);
}
.invert-hover:hover{mix-blend-mode:difference;}
```

# Organic (Natural / Earthy)

**Also called:** natural, earthy, eco, botanical, wellness, soft organic
**In one sentence:** Warm, natural colors, soft blob shapes, textures like paper and stone, and gentle motion — design that feels grown, not built.
**Picture it:** A beige page with a soft sage-green blob shape behind a photo of a ceramic cup, warm serif headings and a leaf illustration.
**Feels like:** calm, warm, healthy, sustainable, human.

**Use for:** wellness, food, skincare, sustainability, agriculture, yoga/meditation, cafés, handmade goods.
**Avoid for:** high-tech, gaming, finance dashboards.

## Overrides
| Area | Override |
|---|---|
| Color | Earth tones: sand #EFE6D8, clay/terracotta #C66B3D, sage #8A9A7B, olive #5C6B3A, warm brown #4A3B2F, cream. Low saturation. |
| Typography | Soft serifs (Fraunces soft, "Recoleta"-like, "Lora", "DM Serif Display") for headings; warm humanist sans (DM Sans, "Nunito Sans", "Figtree") body. |
| Spacing / layout | Relaxed, airy; organic overlap of images and shapes; asymmetric but calm. |
| Radius | Large and soft (16–32px), **blob/irregular shapes** for decorative containers and image masks, arches. |
| Borders | Few; if used, soft earthy color. |
| Depth | Very soft warm shadows; paper/grain textures. |
| Motion | Slow, gentle: 300–600ms, morphing blobs, floating leaves (subtle). |
| Hover | Soft color shift, slight scale, image gentle zoom. |
| Imagery / icons | Natural photography (plants, hands, food, textures), botanical line illustrations, hand-drawn icons. |
| Components | Rounded pill buttons in clay or olive; soft inputs with warm backgrounds; arch-shaped image frames. |

## Signature moves
1. Earth-tone palette.
2. Blob and arch shapes.
3. Natural textures and photography.
4. Soft serifs with warm sans.

## Do / Don't
- **Do** use texture subtly (grain, paper).
- **Do** keep motion slow and calm.
- **Don't** use neon, pure black or harsh geometry.
- **Don't** over-desaturate so everything blends together — hierarchy still needs contrast.

## Accessibility watch-outs
- Earthy mid-tones (sage, clay) often fail as text colors or with white text — check; darken for text use.

## Starter tokens
```css
:root{
  --bg:#F4EDE2; --surface:#FBF7F0; --text:#3A2E24; --text-2:#6B5A4A;
  --clay:#B5582E; --sage:#8A9A7B; --olive:#4F5D2F;
  --accent:var(--olive); --on-accent:#FBF7F0;
  --font-display:"Fraunces",Georgia,serif; --font-sans:"DM Sans",system-ui,sans-serif;
  --radius-control:999px; --radius-container:28px; --blob:42% 58% 63% 37% / 41% 44% 56% 59%;
  --shadow-1:0 6px 24px rgb(90 60 30 / .10);
  --dur:450ms; --ease:cubic-bezier(.25,.1,.25,1);
}
```

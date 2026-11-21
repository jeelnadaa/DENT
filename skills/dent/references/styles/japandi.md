# Japandi / Nordic Calm

**Also called:** Japandi, Scandinavian, Nordic, Scandi, zen minimal, wabi-sabi minimal, muji style
**In one sentence:** Japanese calm meets Scandinavian warmth — muted natural neutrals, simple forms, natural materials and lots of quiet space.
**Picture it:** A light oak table, a linen cloth, one small ceramic bowl, soft daylight, and a thin grey line of text in the corner.
**Feels like:** serene, warm, honest, handcrafted, quiet.

Difference from **Minimal**: Minimal is cool and digital (white + black + accent). Japandi/Nordic is **warm and material** (beige, wood, stone, linen) and softer.

**Use for:** furniture, interior, home goods, wellness, tea/coffee, slow-living blogs, mindful productivity apps, architecture.
**Avoid for:** loud marketing, gaming, kids.

## Overrides
| Area | Override |
|---|---|
| Color | Warm neutrals: rice paper #F5F1EA, linen #E8E1D5, stone #B9B2A6, charcoal #2E2B28, muted accents: indigo #3E4A61, moss #6B705C, rust #9C5A3C (one only). |
| Typography | Light, refined sans ("Albert Sans", "Karla", "Work Sans" light, "Zen Kaku Gothic New"); optional elegant serif ("Cormorant", "Shippori Mincho") for headings. Small sizes, generous spacing. |
| Spacing / layout | **Asymmetric balance with lots of empty space (ma)**; low density; content aligned to a quiet grid. |
| Radius | Small (2–6px) or natural (slightly rounded like wood edges). |
| Borders | Thin, soft (stone at low contrast for decoration; ≥ 3:1 for inputs). |
| Depth | Flat; texture of paper, linen or wood grain at very low opacity. |
| Motion | Slow and soft: fades 400–700ms; nothing bouncy. |
| Hover | Slow opacity/color change, thin underline. |
| Imagery / icons | Natural-light photography of materials and objects, plenty of negative space; thin minimal icons. |
| Components | Quiet outlined or muted-fill buttons; underline or soft-filled inputs. |

## Signature moves
1. Warm neutral palette from natural materials.
2. Large intentional empty space, asymmetric calm.
3. Thin light typography.
4. Subtle natural texture.

## Do / Don't
- **Do** let imperfection and texture show (wabi-sabi).
- **Do** use one muted accent at most.
- **Don't** use bright colors, heavy shadows or busy layouts.
- **Don't** make text so light it can't be read.

## Accessibility watch-outs
- Light-weight, small, grey text is the main risk — keep body ≥ 16px regular weight with ≥ 4.5:1.

## Starter tokens
```css
:root{
  --bg:#F5F1EA; --surface:#EDE7DC; --text:#2E2B28; --text-2:#5E5850; --border:#CFC7B9; --border-input:#8F877A;
  --accent:#3E4A61; --on-accent:#F5F1EA;
  --font-sans:"Albert Sans","Karla",system-ui,sans-serif; --font-serif:"Cormorant Garamond",serif;
  --radius-control:4px; --radius-container:6px;
  --dur:500ms; --ease:cubic-bezier(.25,.1,.25,1);
}
```

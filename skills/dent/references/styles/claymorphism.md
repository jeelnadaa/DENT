# Claymorphism (3D Clay)

**Also called:** clay UI, soft 3D, inflated UI, puffy UI, 3D cartoon
**In one sentence:** Elements look like soft, puffy clay or inflated plastic — pastel colors, very round shapes, inner highlights and soft outer shadows.
**Picture it:** Pastel buttons and cards that look like squishy toys made of modeling clay, floating slightly above a light background, next to cute 3D illustrations.
**Feels like:** cute, soft, friendly, tactile, playful.

**Use for:** kids/education, playful consumer apps, fintech for young users, landing pages with 3D illustrations, games-lite.
**Avoid for:** serious B2B, data-dense tools, luxury.

## Overrides
| Area | Override |
|---|---|
| Color | Pastel fills: peach #FFC8A2, lilac #CDB4FF, mint #B5EAD7, sky #A0D2FF, butter #FFE8A3 on a light background (#F4F1FF). Dark text for contrast. |
| Typography | Rounded bold sans (Nunito, Fredoka, "Baloo 2", Poppins semibold). |
| Spacing / layout | Floating cards with generous gaps; big 3D illustrations as hero. |
| Radius | **Very large** — controls 20px+/pill, cards 28–40px. |
| Borders | None. |
| Depth | **Clay recipe:** soft outer drop shadow + inner top-left light highlight + inner bottom-right darker shadow. |
| Motion | Squishy springs: press = squash (scale .96), release = bounce back. Floating idle animations on 3D objects. |
| Hover | Slight lift and scale 1.02. |
| Imagery / icons | Cute 3D renders (rounded, matte, pastel) — characters, objects, icons. |
| Components | Puffy buttons, pill toggles, rounded chunky inputs with inner shadow. |

## Signature moves
1. Pastel, puffy, rounded shapes.
2. Inner highlights + inner shadows + soft outer shadow.
3. Cute 3D illustrations.

## Do / Don't
- **Do** keep text dark on pastel fills.
- **Do** use the same clay shadow recipe on every element.
- **Don't** combine with sharp corners or hairline borders.
- **Don't** use clay for dense tables/forms.

## Accessibility watch-outs
- Pastel fills + white text fail — always dark text.
- Pastel buttons may not be distinct from pastel cards; give primary actions a stronger color.

## Starter tokens
```css
:root{
  --bg:#F4F1FF; --surface:#FFFFFF; --text:#2B2440; --text-2:#5A5373;
  --peach:#FFC8A2; --lilac:#CDB4FF; --mint:#B5EAD7; --sky:#A0D2FF;
  --accent:#6C4CF1; --on-accent:#FFFFFF;
  --font-sans:"Fredoka","Nunito",system-ui,sans-serif;
  --radius-control:22px; --radius-container:36px;
  --clay:inset 4px 4px 8px rgb(255 255 255 / .7), inset -6px -6px 12px rgb(0 0 0 / .08), 12px 16px 32px rgb(80 60 160 / .18);
  --dur:220ms; --ease:cubic-bezier(.34,1.56,.64,1);
}
```

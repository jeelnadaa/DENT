# Aurora (Gradient Mesh)

**Also called:** gradient style, mesh gradient, aurora UI, blurry gradient blobs, "Stripe style" gradients
**In one sentence:** Soft, flowing, blurred color gradients — like northern lights — as backgrounds behind clean, minimal UI.
**Picture it:** A clean white headline and button over a background of slowly drifting blurred blobs of purple, pink, orange and teal.
**Feels like:** modern, vibrant, dreamy, innovative, optimistic.

**Use for:** SaaS/AI landing pages, fintech, startup marketing, app onboarding, music, event pages.
**Avoid for:** text-heavy content areas, conservative brands.

## Overrides
| Area | Override |
|---|---|
| Color | 3–5 harmonious vivid colors (e.g. violet #7F5AF0, pink #FF6AC1, orange #FFB86B, teal #2CB1BC, blue #3A86FF) blended as **blurred blobs/mesh**; the UI on top is neutral (white or dark). |
| Typography | Clean modern sans (Inter, "Satoshi", "General Sans", "Plus Jakarta Sans"); large bold headlines. |
| Spacing / layout | Gradient lives in hero/section backgrounds; content in clean containers with plenty of space. |
| Radius | Medium-large (12–24px). |
| Borders | Optional subtle white/transparent borders on cards over gradients. |
| Depth | Gradients provide depth; cards may use light glass or solid white. Add **grain** (2–4%) to avoid banding. |
| Motion | **Slow drifting blobs** (20–40s loops), gradients shifting on scroll. Pause under reduced motion. |
| Hover | Gradient border or glow appears on cards; button gradient shifts. |
| Imagery / icons | Abstract shapes, 3D glass objects, product screenshots on gradient backdrops. |
| Components | Solid or gradient primary button; white/glass cards over gradient. |

## Signature moves
1. Large, blurred, multi-color gradient blobs.
2. Clean neutral UI floating on top.
3. Slow ambient motion and grain.

## Do / Don't
- **Do** interpolate gradients in OKLCH (`in oklch`) for clean, non-muddy blends.
- **Do** keep text on solid or tinted panels.
- **Don't** use gradients on every component.
- **Don't** put small text directly on bright gradient areas.

## Accessibility watch-outs
- Text over gradients: check contrast against the lightest and darkest parts.
- Infinite background motion: provide reduced-motion (static gradient).

## Starter tokens
```css
:root{
  --bg:#0E0B1F; --text:#FFFFFF; --text-2:rgb(255 255 255 / .78);
  --c1:#7F5AF0; --c2:#FF6AC1; --c3:#FFB86B; --c4:#2CB1BC;
  --accent:#FFFFFF; --on-accent:#0E0B1F;
  --font-sans:"Plus Jakarta Sans","Inter",system-ui,sans-serif;
  --radius-control:12px; --radius-container:20px;
  --dur:300ms; --ease:cubic-bezier(.16,1,.3,1);
}
.aurora{background:
  radial-gradient(40% 50% at 20% 30%, var(--c1), transparent 70%),
  radial-gradient(35% 45% at 80% 20%, var(--c2), transparent 70%),
  radial-gradient(40% 50% at 60% 80%, var(--c4), transparent 70%),
  var(--bg); filter:saturate(120%);}
```

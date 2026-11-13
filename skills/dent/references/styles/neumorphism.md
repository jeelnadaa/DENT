# Neumorphism (Soft UI)

**Also called:** soft UI, neomorphism, extruded UI
**In one sentence:** Elements look pushed out of (or pressed into) the same soft material as the background, using a light shadow and a dark shadow.
**Picture it:** Buttons molded from the same grey clay as the table they sit on — only light and shadow show their shape.
**Feels like:** soft, tactile, calm, minimal, physical.

**Use for:** small apps with few controls — smart home, music controls, calculators, timers, settings panels, concept shots.
**Avoid for:** forms, data-heavy screens, anything where users must quickly see what's clickable. Rarely good for a whole product.

## Overrides
| Area | Override |
|---|---|
| Color | **Background and elements are the same color** (e.g. #E6E9EF light or #2A2D34 dark). One accent color for active states and primary actions. |
| Typography | Rounded/soft sans (Nunito, Poppins, Manrope, Quicksand). Medium weights, darker than you'd think (contrast!). |
| Spacing / layout | Generous spacing so each shadow has room. Few elements per screen. |
| Radius | Large and soft: 12–24px; circular buttons common. |
| Borders | None (shape comes from shadows). Add a subtle border only for accessibility. |
| Depth | **Two shadows:** light one top-left, dark one bottom-right. Raised = outer shadows; pressed/active = **inset** shadows. |
| Motion | Gentle 150–250ms transitions between raised and pressed. |
| Hover | Shadows deepen slightly. |
| Imagery / icons | Simple line or filled icons in the accent or dark grey; minimal imagery. |
| Components | Raised buttons → inset when pressed/active. Inputs are **inset** wells. Toggles: inset track, raised thumb. |

## Signature moves
1. Same color for background and elements.
2. Dual light/dark shadows creating soft extrusion.
3. Pressed state = inset shadow.

## Do / Don't
- **Do** use the accent color to mark active/selected state clearly — shadows alone are too subtle.
- **Do** keep the light source consistent (top-left).
- **Don't** use on busy or colored backgrounds.
- **Don't** rely on shadows alone to show that something is a button.

## Accessibility watch-outs
- **This style naturally fails the 3:1 UI contrast rule.** Fix: add a subtle 1px border (≥ 3:1) on interactive elements, or use accent color for primary actions and selected states, and make text dark enough (≥ 4.5:1).
- Focus rings must be clearly visible (use the accent color).

## Starter tokens
```css
:root{
  --bg:#E6E9EF; --surface:#E6E9EF; --text:#2D3343; --text-2:#545B6E; --accent:#5B6CFF; --on-accent:#FFFFFF;
  --font-sans:"Nunito",system-ui,sans-serif;
  --radius-control:14px; --radius-container:24px;
  --shadow-raised:8px 8px 16px #C4C8D0, -8px -8px 16px #FFFFFF;
  --shadow-inset:inset 6px 6px 12px #C4C8D0, inset -6px -6px 12px #FFFFFF;
  --border-a11y:1px solid #A3A9B6;
  --dur:200ms; --ease:cubic-bezier(.2,0,0,1);
}
```

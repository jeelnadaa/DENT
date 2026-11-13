# Material-Inspired (Material You style)

**Also called:** Material Design, Material 3, Android style, Google style, dynamic color
**In one sentence:** Tonal color surfaces generated from one seed color, rounded shapes, clear elevation by tone, and motion that follows physical rules.
**Picture it:** An Android settings screen tinted softly in the user's wallpaper color, with pill-shaped buttons and a big rounded floating action button.
**Feels like:** friendly, systematic, personal, accessible, familiar.

**Use for:** Android apps, cross-platform apps, admin tools, products that want a well-documented, accessible system.
**Avoid for:** products needing a very distinct brand identity (it can look generic), luxury.

## Overrides
| Area | Override |
|---|---|
| Color | Pick one **seed color** → generate tonal palettes (primary, secondary, tertiary, neutral) with tones 0–100. Surfaces use tinted neutrals; containers use light tones of each role ("primary container"). |
| Typography | Roboto / Roboto Flex / Google Sans-like (e.g. "Product Sans" alternative: Outfit, Figtree). Type roles: Display, Headline, Title, Body, Label (each L/M/S). |
| Spacing / layout | 4dp base grid, 16dp screen margins on mobile, 24dp on larger. |
| Radius | **Shape scale:** extra-small 4, small 8, medium 12, large 16, extra-large 28, full (pills). Buttons are **full pills**; cards 12; dialogs/sheets 28. |
| Borders | Outlined variants use 1px "outline" color; most surfaces borderless. |
| Depth | **Tonal elevation**: higher surfaces are tinted more with primary, plus light shadows only where needed (FAB, menus). |
| Motion | Emphasized easing `cubic-bezier(.2,0,0,1)`; durations 200–500ms; container transforms (card → full screen). |
| Hover | **State layers**: overlay of the content color at 8% hover, 10% focus/pressed. Ripple on press. |
| Imagery / icons | Material Symbols (rounded/outlined), 24dp, adjustable fill/weight. |
| Components | Filled, tonal, outlined, text and elevated buttons; FAB; chips; navigation bar/rail/drawer; top app bars; text fields filled or outlined. |

## Signature moves
1. Color system from one seed color, tonal containers.
2. Pill-shaped buttons and large rounded sheets/dialogs.
3. State layers + ripple feedback.
4. Floating action button for the main action.

## Do / Don't
- **Do** use the role-based color tokens (on-primary, primary-container…) consistently.
- **Do** follow the shape scale exactly.
- **Don't** mix iOS-style components in a Material app.
- **Don't** invent extra elevation shadows — use tone.

## Accessibility watch-outs
- Generated palettes are built for contrast; keep "on-X" text colors on matching "X" backgrounds.
- 48dp minimum touch targets.

## Starter tokens
```css
:root{
  --primary:#6750A4; --on-primary:#FFFFFF; --primary-container:#EADDFF; --on-primary-container:#21005D;
  --secondary-container:#E8DEF8; --on-secondary-container:#1D192B;
  --surface:#FEF7FF; --surface-container:#F3EDF7; --on-surface:#1D1B20; --on-surface-variant:#49454F; --outline:#79747E;
  --font-sans:"Roboto Flex","Roboto",system-ui,sans-serif;
  --shape-xs:4px; --shape-s:8px; --shape-m:12px; --shape-l:16px; --shape-xl:28px; --shape-full:999px;
  --state-hover:.08; --state-press:.10;
  --dur:300ms; --ease:cubic-bezier(.2,0,0,1);
}
```

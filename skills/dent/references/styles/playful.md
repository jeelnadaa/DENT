# Playful (Friendly Cartoon)

**Also called:** fun, friendly, cartoon, bubbly, Duolingo-like, cheerful, gamified
**In one sentence:** Bright cheerful colors, round chunky shapes, bouncy motion and illustrated characters that make the product feel like a friend.
**Picture it:** A learning app with a big green rounded button that squishes when tapped, a smiling mascot cheering, and confetti when you finish a lesson.
**Feels like:** happy, encouraging, approachable, energetic, safe.

**Use for:** education, kids/family, habit trackers, consumer apps, onboarding, games-lite, community apps.
**Avoid for:** luxury, legal/finance B2B, serious medical.

## Overrides
| Area | Override |
|---|---|
| Color | Bright but friendly: grass green #58CC02, sky blue #1CB0F6, sunny yellow #FFC800, coral #FF4B4B, purple #CE82FF on white or very light backgrounds. Each color has a **darker "lip" shade** for 3D buttons. |
| Typography | **Rounded, chunky sans** (Nunito, Baloo 2, "Fredoka", "Feather"-like, Quicksand bold). Heavy weights for headings; friendly casual copy. |
| Spacing / layout | Big touch targets, generous padding, centered single-column flows on mobile. |
| Radius | Large: controls 14–16px or pill; cards 20–24px. |
| Borders | 2px light-grey borders on cards/inputs; buttons have a **solid bottom "lip"** (4px darker shade). |
| Depth | Chunky 3D buttons via bottom border/shadow (no blur); flat elsewhere. |
| Motion | **Bouncy springs** (overshoot), squash-and-stretch on press, celebratory confetti/stars at milestones, mascot reactions. |
| Hover/press | Press = button moves down into its lip (translateY 4px, lip shrinks). Hover = brighten. |
| Imagery / icons | Mascot/character illustrations, rounded filled icons, stickers, badges, streak flames. |
| Components | 3D pill buttons, progress bars with rounded ends, badges/achievements, bottom sheets with friendly copy. |

## Signature moves
1. Chunky rounded type and shapes.
2. 3D buttons with a darker bottom lip that press down.
3. Bouncy, rewarding motion and celebrations.
4. A mascot or illustrated characters.

## Do / Don't
- **Do** celebrate progress (Goal-gradient, Peak-end).
- **Do** write friendly, encouraging microcopy.
- **Don't** make errors scary — be kind and helpful.
- **Don't** let celebrations block the next action or repeat too often.

## Accessibility watch-outs
- White text on bright green/yellow/light blue often fails — use darker shades or dark text.
- Bouncy motion and confetti need reduced-motion versions.

## Starter tokens
```css
:root{
  --bg:#FFFFFF; --surface:#F7F7F7; --text:#3C3C3C; --text-2:#777777; --border:#E5E5E5;
  --green:#58A700; --green-lip:#3F7A00; --blue:#1899D6; --blue-lip:#1172A3; --yellow:#FFC800; --coral:#FF4B4B;
  --accent:var(--green); --accent-lip:var(--green-lip); --on-accent:#FFFFFF;
  --font-sans:"Nunito","Baloo 2",system-ui,sans-serif;
  --radius-control:16px; --radius-container:24px;
  --dur:180ms; --ease:cubic-bezier(.34,1.56,.64,1);
}
.btn{background:var(--accent);color:var(--on-accent);border-radius:var(--radius-control);box-shadow:0 4px 0 var(--accent-lip);font-weight:800;}
.btn:active{transform:translateY(4px);box-shadow:0 0 0 var(--accent-lip);}
```

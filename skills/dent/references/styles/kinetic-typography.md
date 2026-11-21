# Kinetic Typography (Type-Led)

**Also called:** typographic, type-first, big type, motion type, oversized typography
**In one sentence:** Huge, moving, expressive type is the main visual — words scroll, stretch, split and react instead of using images.
**Picture it:** A landing page where a giant word fills the screen edge to edge, letters slide in one by one, and a line of text scrolls endlessly like a ticker.
**Feels like:** bold, loud, creative, editorial, energetic.

**Use for:** agencies, portfolios, events/conferences, music, fashion campaigns, brand launches.
**Avoid for:** apps and tools (use only in marketing hero areas), information-dense pages.

## Overrides
| Area | Override |
|---|---|
| Color | Usually 2 colors (e.g. black + one bold color, or a single color on black); type color contrast is the main design. |
| Typography | **Display fonts with character and variable axes** (weight/width), e.g. "Anton", "Bebas Neue", "Syne", "Big Shoulders Display", "Unbounded", variable "Roboto Flex". Sizes up to 20–30vw; tight tracking and leading (0.85–1). |
| Spacing / layout | Type fills the viewport edge to edge; few other elements; layout built from text blocks. |
| Radius | 0 (type is the shape). |
| Borders | Rarely; maybe rules between text rows. |
| Depth | None. |
| Motion | **Letter-by-letter reveals**, marquee/ticker lines, variable-weight animation on scroll/hover, text masks over video, split words sliding. |
| Hover | Letters change weight/width, skew, or reveal an image inside the text. |
| Imagery / icons | Minimal; images often appear *inside* text (background-clip: text) or on hover. |
| Components | Text links as huge words; simple buttons. |

## Signature moves
1. Massive type filling the screen.
2. Text in motion (marquees, split reveals, variable weight).
3. Images used inside or behind type, not as main blocks.

## Do / Don't
- **Do** keep the real message readable even while animating.
- **Do** use `clamp()` with rem so it scales and respects zoom, with the maximum ≤ 2.5× the minimum (`mwg:responsive-design`).
- **Don't** split words in ways screen readers can't read — keep accessible text (aria-label on the parent, or visually hidden copy).
- **Don't** apply kinetic effects to body text.

## Accessibility watch-outs
- Marquees moving > 5s need a pause control **[Rule]**.
- Split-letter animations: wrap letters `aria-hidden="true"` and provide the full word to assistive tech.

## Starter tokens
```css
:root{
  --bg:#0F0F0F; --text:#F4F1EA; --accent:#FF4D00; --on-accent:#0F0F0F;
  --font-display:"Anybody","Special Gothic Expanded One",sans-serif; --font-sans:"Special Gothic","Hanken Grotesk",system-ui,sans-serif;
  --mega:clamp(6rem,2rem + 15vw,15rem); --leading-mega:.85; --tracking-mega:-0.04em;
  --dur:600ms; --ease:cubic-bezier(.16,1,.3,1);
}
.marquee{display:flex;gap:2rem;white-space:nowrap;animation:marquee 25s linear infinite;}
@keyframes marquee{to{transform:translateX(-50%);}}
@media (prefers-reduced-motion:reduce){.marquee{animation:none;}}
```

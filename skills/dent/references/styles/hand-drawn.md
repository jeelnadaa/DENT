# Hand-Drawn (Sketch / Doodle)

**Also called:** sketchy, doodle, handmade, notebook, scrapbook, wireframe-sketch
**In one sentence:** The interface looks drawn by hand — wobbly lines, handwritten fonts, marker highlights and doodles on paper.
**Picture it:** A notebook page with a hand-drawn box around a button, a marker-yellow highlight behind a word, and a little arrow doodle pointing to "Start here!".
**Feels like:** personal, informal, creative, human, approachable.

**Use for:** personal blogs/portfolios, note-taking/whiteboard apps, education, creative workshops, indie products, kids.
**Avoid for:** corporate, finance, luxury, serious enterprise.

## Overrides
| Area | Override |
|---|---|
| Color | Paper white/cream #FFFDF6 or grid/lined paper; ink black/blue #1E2A4A; marker highlights (yellow #FFE45E, pink, mint) at partial opacity. |
| Typography | Handwritten for headings/annotations (Caveat, "Kalam", "Patrick Hand", "Gochi Hand"); readable sans or mono for body (never all-handwritten body). |
| Spacing / layout | Loose, slightly imperfect; elements can be tilted ±1–3°; annotations and arrows. |
| Radius | Irregular — use wobbly borders (SVG filters, rough.js, or `border-radius` with uneven values like `255px 15px 225px 15px / 15px 225px 15px 255px`). |
| Borders | 2px ink lines with a hand-drawn wobble. |
| Depth | Flat; hard offset "shadow" drawn as a second sketchy outline. |
| Motion | Lines drawing themselves (SVG stroke-dashoffset), slight wiggle. |
| Hover | Scribble underline, highlight marker sweep, wiggle. |
| Imagery / icons | Doodles, hand-drawn icons, arrows, stars, circles around important words, tape/sticker elements. |
| Components | Sketchy-bordered buttons and inputs; checkboxes with a hand-drawn check. |

## Signature moves
1. Wobbly, hand-drawn borders.
2. Handwritten headings + marker highlights.
3. Doodled arrows and annotations.

## Do / Don't
- **Do** keep body text in a clean readable font.
- **Do** keep imperfections consistent (same wobble style).
- **Don't** handwrite long paragraphs or form labels.
- **Don't** tilt interactive elements so much they look broken.

## Accessibility watch-outs
- Handwritten fonts lower readability — use for short display text only.
- Marker highlights behind text must keep text contrast ≥ 4.5:1.

## Starter tokens
```css
:root{
  --bg:#FFFDF6; --text:#1E2A4A; --text-2:#4A5575; --ink:#1E2A4A; --marker:rgb(255 228 94 / .75);
  --accent:#1E2A4A; --on-accent:#FFFDF6;
  --font-hand:"Caveat","Kalam",cursive; --font-sans:"Patrick Hand","Nunito",system-ui,sans-serif;
  --radius-sketch:255px 15px 225px 15px / 15px 225px 15px 255px;
  --border-w:2px;
  --dur:250ms; --ease:cubic-bezier(.34,1.3,.64,1);
}
.highlight{background:linear-gradient(104deg,transparent .9%,var(--marker) 2.4%,var(--marker) 97%,transparent 98%);}
```

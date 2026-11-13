# Dark Academia (Classic Library)

**Also called:** academia, classic, old library, scholarly, gothic-classic, light academia (light variant)
**In one sentence:** Old libraries and classic universities — deep browns, greens and burgundy, classic serifs, parchment textures and gold details.
**Picture it:** A dark wooden library, leather-bound books, a brass lamp, and an elegant serif title on parchment with a thin gold rule.
**Feels like:** intellectual, moody, classic, literary, cozy.

Variant: **Light Academia** uses cream, beige and soft browns instead of dark tones.

**Use for:** books, literature, writing apps, study tools, universities, museums, history content, journaling.
**Avoid for:** tech-forward, playful, fast-paced commerce.

## Overrides
| Area | Override |
|---|---|
| Color | Deep brown #2B1D14, forest green #1F3326, burgundy #5A1E24, parchment #EDE3CF, aged gold #B08D57, ink black. |
| Typography | Classic serifs: "EB Garamond", "Cormorant Garamond", "Crimson Pro", "Libre Baskerville"; small caps; italics; optional blackletter for one decorative element only. |
| Spacing / layout | Book-like: centered narrow text columns, chapters, ornaments; generous margins like a page. |
| Radius | 0–4px; arches for images. |
| Borders | Thin double rules, gold lines, ornamental dividers (❦ ✦). |
| Depth | Paper/parchment and leather textures (subtle), warm vignette. |
| Motion | Slow, page-like: fades, page-turn transitions (gentle). |
| Hover | Gold underline, ink-color shift. |
| Imagery / icons | Books, manuscripts, classical art, architecture, candles; engraved-style illustrations. |
| Components | Outlined buttons with small caps, underlined inputs like a form on paper. |

## Signature moves
1. Dark browns/greens/burgundy + parchment + gold.
2. Classic Garamond-style serif typography with small caps.
3. Ornaments and book-like layout.

## Do / Don't
- **Do** prioritize reading comfort (large serif body, good line-height).
- **Don't** use neon, gradients or rounded pill UI.

## Accessibility watch-outs
- Dark brown on dark green, or gold on parchment, fails — pair dark with light only.

## Starter tokens
```css
:root{
  --bg:#1F1610; --surface:#2B1D14; --paper:#EDE3CF; --text:#EDE3CF; --text-2:#C9BA9B; --text-on-paper:#2B1D14;
  --green:#1F3326; --burgundy:#5A1E24; --gold:#B08D57;
  --accent:var(--gold); --on-accent:#1F1610;
  --font-serif:"EB Garamond","Cormorant Garamond",Georgia,serif;
  --radius-control:2px; --radius-container:2px;
  --dur:500ms; --ease:cubic-bezier(.25,.1,.25,1);
}
```

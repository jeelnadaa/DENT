# Brutalism (Web Brutalism)

**Also called:** brutalist, raw, anti-design, ugly-on-purpose, raw HTML
**In one sentence:** Deliberately raw and unpolished — default-looking fonts, harsh contrast, visible structure and no decoration.
**Picture it:** A web page that looks like it was hand-coded in 1997 by an artist: Times New Roman, blue underlined links, black borders, and one giant word.
**Feels like:** raw, honest, rebellious, artsy, confrontational.

**Use for:** art/creative portfolios, indie publications, fashion/streetwear, music, experimental projects.
**Avoid for:** banking, healthcare, enterprise tools, anything that must feel trustworthy or easy for everyone.

## Overrides
| Area | Override |
|---|---|
| Color | Black, white and default-browser colors (pure blue #0000EE links, pure red, yellow). Or one clashing color. |
| Typography | System/default fonts: Times New Roman, Arial, Courier, or monospace. Mixed sizes with abrupt jumps. ALL CAPS allowed. |
| Spacing / layout | Dense or deliberately uneven. Visible boxes, tables, overlapping blocks. Grid may be broken on purpose. |
| Radius | 0. |
| Borders | Thick black borders (2–4px) everywhere, visible outlines. |
| Depth | None, or harsh hard shadows (no blur). |
| Motion | Little to none; abrupt changes; marquee text is allowed as a gag. |
| Hover | Invert colors, underline, cursor change. |
| Imagery / icons | Raw photos, scans, pixelated images, emoji or ASCII. Rarely icon sets. |
| Components | Default-looking buttons and inputs, or plain bordered boxes. |

## Signature moves
1. Default/system fonts used on purpose.
2. Visible structure: borders, boxes, tables.
3. Harsh contrast and no polish.
4. One oversized element breaking the layout.

## Do / Don't
- **Do** keep navigation and content findable — raw ≠ broken.
- **Do** make the rawness look intentional (consistent rules, even if odd).
- **Don't** use soft shadows, gradients, rounded corners or pastel colors.
- **Don't** use it where users need comfort and trust.

## Accessibility watch-outs
- Clashing color combos (red on blue, yellow on white) often fail contrast — check every text pair.
- Broken layouts must still have logical reading/keyboard order.

## Starter tokens
```css
:root{
  --bg:#FFFFFF; --text:#000000; --link:#0000EE; --accent:#FF0000; --border:#000000;
  --font-sans:Arial,Helvetica,sans-serif; --font-serif:"Times New Roman",Times,serif; --font-mono:"Courier New",monospace;
  --radius-control:0; --radius-container:0; --border-w:3px;
  --dur:0ms;
}
```

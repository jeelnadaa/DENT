# Editorial (Magazine)

**Also called:** magazine style, publication, newspaper style, serif editorial, journal
**In one sentence:** Design like a high-end printed magazine — elegant serif headlines, strong typographic hierarchy, columns and big imagery.
**Picture it:** A magazine feature spread: a huge serif headline, a short italic intro, a full-bleed photo, and text in neat columns with a drop cap.
**Feels like:** intelligent, cultured, trustworthy, refined, story-driven.

**Use for:** blogs, newsletters, news, long-form content, culture/fashion brands, portfolios, book/author sites, research.
**Avoid for:** dense app interfaces, dashboards, quick-action utility tools.

## Overrides
| Area | Override |
|---|---|
| Color | Paper-like background (#FAF8F3 or white), ink-black text (#141414), **one** editorial accent (deep red #B3261E, forest, or navy). Mostly monochrome. |
| Typography | **Serif display for headlines** (Playfair Display, Fraunces, Instrument Serif, GT Super-like, "Newsreader", "Cormorant") + readable serif or clean sans for body (Source Serif 4, Newsreader, Inter). Italics for intros/standfirsts. Small caps / uppercase tracked labels for categories. |
| Spacing / layout | Multi-column grids; text column 60–70 characters; pull quotes breaking the grid; full-bleed images; clear article structure (kicker → headline → standfirst → byline → body). |
| Radius | 0–4px. |
| Borders | Thin rules (1px) between sections and above headings, like print. |
| Depth | None; flat paper. |
| Motion | Restrained: gentle fades, image reveals. |
| Hover | Underline, headline color change to accent. |
| Imagery / icons | Large, art-directed photography; captions in small italic/sans. Few icons. |
| Components | Text-style buttons and links; minimal UI chrome; numbered lists; bylines with small avatars. |

## Signature moves
1. Big serif headlines with tight leading.
2. Drop caps, pull quotes, kickers and bylines.
3. Rules and column grid like print.
4. Generous reading typography.

## Do / Don't
- **Do** make reading comfortable: 18–21px body, 1.6 line-height, 60–70 characters per line.
- **Do** vary article layouts with the grid, like a real magazine.
- **Don't** use rounded cards, gradients or heavy UI widgets.
- **Don't** use more than two type families.

## Accessibility watch-outs
- Thin serif hairlines at small sizes can be hard to read — use serifs for large text, or choose a sturdy text serif.
- Accent red on paper must stay ≥ 4.5:1 for links.

## Starter tokens
```css
:root{
  --bg:#FAF8F3; --text:#141414; --text-2:#55524C; --rule:#D9D4C7; --accent:#B3261E; --on-accent:#FFFFFF;
  --font-display:"Fraunces","Playfair Display",Georgia,serif; --font-body:"Source Serif 4",Georgia,serif; --font-ui:"Inter",system-ui,sans-serif;
  --body-size:clamp(1.125rem,1.05rem + .3vw,1.3125rem); --measure:66ch;
  --radius-control:2px; --radius-container:0;
  --dur:300ms; --ease:cubic-bezier(.2,0,0,1);
}
```

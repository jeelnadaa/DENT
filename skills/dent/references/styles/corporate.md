# Corporate (Clean Enterprise)

**Also called:** enterprise, business, professional, B2B, trustworthy, banking style
**In one sentence:** Clear, dependable and efficient — a trustworthy blue-centered palette, readable type, structured layouts and no surprises.
**Picture it:** A bank's dashboard: white background, navy header, neat cards with numbers, clear tables and one blue "Transfer" button.
**Feels like:** trustworthy, competent, stable, efficient, serious.

**Use for:** banking, insurance, healthcare, government, B2B SaaS, HR/finance tools, consulting.
**Avoid for:** youth/creative brands, entertainment.

## Overrides
| Area | Override |
|---|---|
| Color | White/light-grey backgrounds; **navy/blue primary** (#0B3B8C / #1A56DB) or deep teal; neutral greys; clear semantic colors (critical for data/status). |
| Typography | Highly legible sans (Switzer, IBM Plex Sans, Hanken Grotesk, Public Sans). Regular/medium/semibold only. Tabular numbers. |
| Spacing / layout | Structured, predictable grids; sidebar + top bar apps; information density medium-high (compact rows available). |
| Radius | Small-medium: 4–8px. |
| Borders | 1px light borders on cards, tables, inputs. |
| Depth | Light shadows for menus/modals only. |
| Motion | Minimal and quick (100–200ms); no decorative motion. |
| Hover | Subtle background tint, underline links. |
| Imagery / icons | Real people at work, product screenshots, simple charts; consistent outlined icon set. |
| Components | Standard, clearly labeled buttons; data tables, filters, breadcrumbs, forms with clear validation. |

## Signature moves
1. Blue/navy as the trust color.
2. Clean, highly legible typography and tables.
3. Predictable layout and standard components (Jakob's Law).

## Do / Don't
- **Do** prioritize clarity, accessibility and density options.
- **Do** make status and errors extremely clear.
- **Don't** add trendy effects that reduce clarity.
- **Don't** let it become bland: a strong typographic hierarchy and one brand accent keep it distinctive.

## Accessibility watch-outs
- Often used by everyone — aim for WCAG AA everywhere, AAA for body text where possible.
- Dense tables still need ≥ 24px targets and visible focus.

## Starter tokens
```css
:root{
  --bg:#FFFFFF; --surface:#F7F9FC; --text:#111827; --text-2:#4B5563; --border:#E5E7EB; --border-input:#9CA3AF;
  --accent:#1A56DB; --on-accent:#FFFFFF; --navy:#0B2559;
  --success:#047857; --warning:#B45309; --error:#B91C1C; --info:#1D4ED8;
  --font-sans:"Switzer","IBM Plex Sans",system-ui,sans-serif;
  --radius-control:6px; --radius-container:8px;
  --shadow-2:0 4px 12px rgb(17 24 39 / .08);
  --dur:150ms; --ease:cubic-bezier(.2,0,0,1);
}
```

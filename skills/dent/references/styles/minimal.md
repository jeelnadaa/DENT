# Minimal (Clean Minimalism)

**Also called:** minimalist, clean, simple, modern minimal, "less is more"
**In one sentence:** Remove everything that isn't needed; let whitespace, alignment and typography do all the work.
**Picture it:** A white gallery wall with one framed photo and a small, perfectly aligned caption.
**Feels like:** calm, clear, confident, quiet, focused.

**Use for:** productivity tools, portfolios, SaaS, documentation, e-commerce for design-led brands, personal sites.
**Avoid for:** kids' products, games, brands that need loud energy, content-dense dashboards (minimal can still work there, but needs care).

## Overrides
| Area | Override |
|---|---|
| Color | Mostly neutrals (white/off-white + near-black + 2–3 greys). **One** accent color used only for primary actions/links. No gradients. |
| Typography | One sans-serif family (e.g. Inter, Geist, Manrope, Satoshi) in 2–3 weights. Hierarchy from size and weight, not color. Generous line-height. |
| Spacing / layout | **More whitespace than feels comfortable** — step up the spacing scale one level everywhere (e.g. card padding 24 → 32, section gaps 64 → 96–128). Strict grid alignment. |
| Radius | Small and consistent (4–8px), or 0 for a stricter look. |
| Borders | Hairline 1px, very light grey; often no borders at all — spacing separates. |
| Depth | Flat or one very soft shadow level. No heavy shadows. |
| Motion | Fast and subtle: fades and 8–12px slides, 150–250ms. No bounce. |
| Hover | Color/opacity change, underline slide. No lifts or glows. |
| Imagery / icons | Few, high-quality images with lots of space around them; thin line icons (1.5px stroke). |
| Components | Ghost/text buttons for secondary actions; one solid primary. Inputs with subtle borders or bottom line only. |

## Signature moves
1. Huge whitespace around few elements.
2. Perfect alignment to a grid — every edge lines up with something.
3. One accent color, used rarely.
4. Typography is the main visual element.

## Do / Don't
- **Do** cut content and features until each screen has one clear purpose.
- **Do** make the few remaining details perfect (spacing, alignment, type).
- **Don't** confuse minimal with empty or unfinished — it should feel intentional.
- **Don't** hide important actions to "look clean" (discoverability still matters).

## Accessibility watch-outs
- Light grey text on white is the classic failure — secondary text must still be ≥ 4.5:1.
- Borderless inputs must still have a ≥ 3:1 visible boundary.

## Starter tokens
```css
:root{
  --bg:#FFFFFF; --surface:#FAFAFA; --text:#111111; --text-2:#5C5C5C; --border:#E6E6E6;
  --accent:#2F5BEA; --on-accent:#FFFFFF;
  --font-sans:"Inter",system-ui,sans-serif;
  --radius-control:6px; --radius-container:10px;
  --shadow-1:0 1px 2px rgb(0 0 0 / .04);
  --dur:200ms; --ease:cubic-bezier(.2,0,0,1);
}
```

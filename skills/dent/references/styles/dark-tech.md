# Dark Tech (Modern Dark SaaS)

**Also called:** dark SaaS, dev-tool style, "Linear style", "Vercel style", sleek dark, startup dark mode
**In one sentence:** Near-black interfaces with crisp light text, subtle borders, faint glows and gradients, precise typography and fast motion.
**Picture it:** A dark product page where a glowing app screenshot floats in the center, thin grey grid lines fade into the background, and a soft purple light leaks from behind the headline.
**Feels like:** sharp, fast, technical, premium, focused.

**Use for:** developer tools, AI products, SaaS, analytics, productivity apps, crypto/fintech, startups.
**Avoid for:** warm consumer brands, kids, older audiences, long reading.

## Overrides
| Area | Override |
|---|---|
| Color | Background near-black, slightly tinted (#0A0A0B, #0B0D12). Surfaces step up in lightness (#111215, #17181C, #1E1F24). Text #EDEDEF / #A0A0AB secondary. **Borders do the separating**: white at 6–12%. One accent (violet #7C5CFF, blue #3B82F6, or green #22C55E) used for focus, links, glows. |
| Typography | Geometric/neo-grotesque (Geist, Satoshi, General Sans), medium weights; **gradient text** on hero headline (white → grey); monospace (Geist Mono, JetBrains Mono) for code, keys, metadata. |
| Spacing / layout | Centered hero with product screenshot; bento feature grids; tight, dense app UIs with compact rows (32–36px). |
| Radius | Controls 6–8px; cards 12–16px. |
| Borders | **1px hairline borders everywhere** (rgba 255,255,255,.08); sometimes a gradient border (light at top). |
| Depth | Elevation by lighter surface + border, not shadows. **Glows**: soft radial gradient of the accent behind key elements. Subtle grid/dot background patterns fading out with a mask. |
| Motion | Fast and precise: 120–200ms UI; hero elements fade-up with blur (filter: blur(8px) → 0). Keyboard-first feel. |
| Hover | Border brightens, spotlight glow following cursor inside cards, background +2–4% lighter. |
| Imagery / icons | Real product screenshots (dark), abstract 3D/light beams; thin 1.5px line icons (Lucide-style). |
| Components | Primary button white-on-black or accent; secondary = dark with border. Inputs dark with border, glow on focus. Keyboard shortcut chips (⌘K). Command palette. |

## Signature moves
1. Near-black + hairline borders instead of shadows.
2. Accent-colored glow behind hero/feature content.
3. Gradient (white → grey) headline text.
4. Faint grid/dot pattern with fade mask.
5. Monospace details and keyboard shortcuts.

## Do / Don't
- **Do** use lightness steps for layers (darker = further back).
- **Do** keep glows subtle and few.
- **Don't** use pure #000 with pure #FFF everywhere (harsh); slightly soften both.
- **Don't** use saturated colors for large areas.

## Accessibility watch-outs
- Secondary grey text on near-black must stay ≥ 4.5:1 (e.g. #A0A0AB on #0A0A0B passes; darker greys don't).
- Hairline borders on inputs are often < 3:1 — make input borders stronger (≈ 20–30% white) than decorative borders.

## Starter tokens
```css
:root{
  --bg:#0A0A0B; --surface-1:#111215; --surface-2:#17181C; --surface-3:#1E1F24;
  --text:#EDEDEF; --text-2:#A0A0AB; --border:rgb(255 255 255 / .08); --border-strong:rgb(255 255 255 / .22);
  --accent:#7C5CFF; --on-accent:#FFFFFF; --glow:radial-gradient(600px circle at 50% 0%,rgb(124 92 255 / .25),transparent 60%);
  --font-sans:"Geist","Satoshi",system-ui,sans-serif; --font-mono:"Geist Mono","JetBrains Mono",monospace;
  --radius-control:8px; --radius-container:14px;
  --dur:160ms; --ease:cubic-bezier(.2,0,0,1);
}
.headline{background:linear-gradient(180deg,#FFFFFF 0%,#9A9AA5 100%);-webkit-background-clip:text;background-clip:text;color:transparent;}
```

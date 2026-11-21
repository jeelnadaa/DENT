# Utilitarian (Industrial / Instrument Panel)

**Also called:** industrial, functional, instrument UI, engineering, lab equipment, spec-sheet, "tool aesthetic"
**In one sentence:** The interface looks like a precise piece of hardware or a technical spec sheet — every label functional, every element numbered, one signal color.
**Picture it:** A warm light-grey control panel with small mono labels, thin rules dividing a dense grid, numbered sections ("01 — INPUT"), and a single orange indicator that means "active".
**Feels like:** precise, honest, engineered, confident, no-nonsense.

**Use for:** developer and hardware products, data tools, audio/creative tools, technical B2B, portfolios of engineers/industrial designers, product spec pages.
**Avoid for:** emotional consumer products (wellness, kids, romance), luxury, anything that must feel soft or friendly.

## Overrides
| Area | Override |
|---|---|
| Color | Warm light grey or off-white surface (#E8E6E1), near-black text, mid-grey secondary; **one signal color** (safety orange #FF4F00, or signal yellow/green) used only for active/primary/alerts. Dark variant: graphite (#1A1A1A) with the same signal. |
| Typography | Grotesk for headings (Zalando Sans, Special Gothic, Neue Haas-style grotesks, Host Grotesk) + **monospace for labels, numbers and metadata** (JetBrains Mono, IBM Plex Mono). Labels small (11–12px) uppercase with +6–10% tracking. Big tabular numerals. |
| Spacing / layout | Dense, strict grid with visible 1px rules dividing cells; compact density; numbered sections; spec-table layouts. |
| Radius | 0–4px. Controls may be 2px; containers 0–4px. |
| Borders | 1px hairlines in mid-grey define structure instead of shadows. |
| Depth | Flat; optional subtle inset on controls (like a physical button bezel). |
| Motion | Fast and mechanical: 80–150ms, linear-ish ease-out, no bounce. Toggles snap. |
| Hover | Background shifts to a slightly darker grey; signal color only on the active state. |
| Imagery / icons | Technical drawings, exploded diagrams, product shots on plain backgrounds, schematic line icons (1.5px). |
| Components | Buttons rectangular with mono uppercase labels; segmented controls and toggles styled like hardware switches; indicator dots/LEDs for status (with text); data shown in spec tables; section headers as "01 / TITLE". |

## Signature moves
1. Mono uppercase micro-labels on everything ("LATENCY", "REV 2.1").
2. Thin rules dividing a dense grid of cells.
3. One signal color (orange) meaning "on / act".
4. Numbering: sections, steps, versions, coordinates.

## Do / Don't
- **Do** make every label real and useful — this style dies with decorative fake data.
- **Do** use big tabular numbers as the main visual for metrics.
- **Don't** use the signal color decoratively; it must mean something.
- **Don't** add soft shadows, gradients or rounded pills — they break the engineered feel.

## Accessibility watch-outs
- Small uppercase mono labels: keep ≥ 11px, ≥ 4.5:1, and never the only label for a control (keep a real accessible name).
- Status LEDs need text ("Online") — not color alone.
- Orange signal on light grey is below 3:1 as text; use it as a **fill** with near-black text, or a darker orange (#C23A00) for text.

## Starter tokens
```css
:root{
  --bg:#E8E6E1; --surface:#F2F1EE; --rule:#B9B6AE;
  --text:#161616; --text-2:#5A5A55;
  --signal:#FF4F00; --on-signal:#161616; --signal-text:#C23A00;
  --font-sans:"Zalando Sans","Host Grotesk",system-ui,sans-serif;
  --font-mono:"JetBrains Mono","IBM Plex Mono",ui-monospace,monospace;
  --label-size:11px; --label-tracking:.08em;
  --radius-control:2px; --radius-container:0;
  --dur-fast:100ms; --ease:cubic-bezier(.2,0,0,1);
}
.label{font:500 var(--label-size)/1.2 var(--font-mono);letter-spacing:var(--label-tracking);text-transform:uppercase;color:var(--text-2);}
```

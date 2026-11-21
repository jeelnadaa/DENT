# Skeuomorphism (and Modern Skeuomorphism)

**Also called:** skeuo, realistic UI, tactile UI, physical UI, "neo-skeuomorphism"
**In one sentence:** UI elements imitate real objects and materials — leather, metal, paper, knobs, switches — with realistic light and texture.
**Picture it:** A music app where the volume is a brushed-metal knob and the buttons look like real plastic keys you could press.
**Feels like:** tangible, nostalgic, crafted, warm, playful-premium.

Two levels:
- **Classic** (early-2010s): full textures (leather, wood, linen), heavy gloss.
- **Modern** (current): realistic lighting, gradients and highlights on otherwise clean shapes — no fake textures. Prefer this one by default.

**Use for:** audio/music tools, cameras, games, calculators, hardware companion apps, playful premium brands, hero illustrations.
**Avoid for:** dense data tools, enterprise, long reading.

## Overrides
| Area | Override |
|---|---|
| Color | Material colors: metals (silver/graphite gradients), warm paper, deep plastics. Accent for indicator lights (LED green/red/orange). |
| Typography | Sans or slightly technical type (Radio Canada Big, SF Pro Rounded, Barlow); engraved/embossed labels for controls (text-shadow). |
| Spacing / layout | Layout like a physical device or panel: grouped controls in "housings". |
| Radius | Realistic radii matched to object type: keys 8–14px, panels 16–28px, knobs circular. |
| Borders | Highlight edge (1px light at top) + dark edge at bottom to simulate bevel. |
| Depth | **Multiple layered shadows + inner highlights + gradients** to show realistic light from above. Pressed = darker gradient + inset shadow. |
| Motion | Physical: springs, knobs rotate, switches flip with slight overshoot (200–350ms). |
| Hover | Subtle brightening as if light catches it. |
| Imagery / icons | Detailed, rendered icons (app-icon quality), real-object metaphors. |
| Components | Buttons as physical keys, toggles as real switches, sliders as faders, dials as knobs. |

## Signature moves
1. Consistent top light source: highlights top, shadows bottom.
2. Gradients that model material (metal, plastic, glass).
3. Controls that look like real physical controls and react like them.

## Do / Don't
- **Do** keep the metaphor consistent (all controls from one "device").
- **Do** make interactions physical (rotate, press, slide).
- **Don't** mix realistic and flat controls randomly.
- **Don't** overload with textures that reduce readability.

## Accessibility watch-outs
- Embossed/engraved text often has low contrast — check against the actual surface.
- Knobs/dials need keyboard and screen-reader support (role="slider", arrow keys).

## Starter tokens
```css
:root{
  --bg:#D9DCE1; --panel:linear-gradient(180deg,#F4F5F7 0%,#D5D8DD 100%);
  --key:linear-gradient(180deg,#FFFFFF 0%,#E3E5E9 100%); --key-pressed:linear-gradient(180deg,#D3D6DB 0%,#E8EAED 100%);
  --text:#1E2228; --text-2:#4A505A; --led:#2BD96B; --accent:#FF6A13; --on-accent:#1E2228;
  --font-sans:"Radio Canada Big","Barlow",system-ui,sans-serif;
  --radius-control:12px; --radius-container:24px;
  --shadow-key:0 1px 0 rgb(255 255 255 / .9) inset, 0 -1px 0 rgb(0 0 0 / .08) inset, 0 2px 3px rgb(0 0 0 / .18), 0 8px 16px rgb(0 0 0 / .12);
  --shadow-pressed:inset 0 2px 6px rgb(0 0 0 / .25);
  --dur:220ms; --ease:cubic-bezier(.34,1.3,.64,1);
}
```

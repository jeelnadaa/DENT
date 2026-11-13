# Vintage (Retro 50s–70s / Old-School Print)

**Also called:** retro, vintage, old-school, 70s retro, groovy, diner, heritage, nostalgic
**In one sentence:** Warm nostalgic colors, chunky retro serifs and script logos, badges, and textures of aged paper and print.
**Picture it:** A coffee brand page with a cream paper texture, a circular badge logo, a bold rounded serif headline in brown and orange, and wavy "groovy" stripes.
**Feels like:** nostalgic, warm, crafted, friendly, authentic.

**Use for:** cafés, breweries, barbers, food brands, craft goods, music/vinyl, heritage brands, outdoor gear.
**Avoid for:** high-tech, futuristic, enterprise tools.

## Overrides
| Area | Override |
|---|---|
| Color | Warm faded tones: cream #F3E6CC, mustard #D9A62E, burnt orange #C4622D, brick red #9E3B2C, olive #6B6B3A, chocolate #3D2B1F. |
| Typography | Chunky retro serifs ("Cooper"-like: "Young Serif", "Recoleta"-like, "Shrikhand", "Abril Fatface", "DM Serif Display"), script for logos/accents ("Pacifico", "Yellowtail"); simple serif or sans body. |
| Spacing / layout | Centered, badge-like compositions; framed sections; ribbons and banners. |
| Radius | Small or full circles (badges); arches. |
| Borders | Double lines, dashed "coupon" borders, ornamental dividers ✦. |
| Depth | Flat; **paper texture, grain, slight print wear**; occasional offset shadow in a second color. |
| Motion | Gentle; badges rotate slowly; wavy stripes. |
| Hover | Color shift, offset shadow grows. |
| Imagery / icons | Badges, stamps, retro illustrations, warm film-like photography (grain, faded). |
| Components | Pill or rounded buttons in brick/orange; framed cards; stamp-like tags. |

## Signature moves
1. Warm faded palette.
2. Chunky retro serif + script.
3. Badges, stamps and ornaments.
4. Paper/grain texture.

## Do / Don't
- **Do** use texture subtly and keep text crisp.
- **Don't** mix with glossy, neon or glass effects.

## Accessibility watch-outs
- Script fonts only for logos/short accents.
- Mustard on cream fails for text — use chocolate/brick.

## Starter tokens
```css
:root{
  --bg:#F3E6CC; --surface:#F9F0DD; --text:#3D2B1F; --text-2:#65503E;
  --mustard:#D9A62E; --orange:#C4622D; --brick:#9E3B2C; --olive:#6B6B3A;
  --accent:var(--brick); --on-accent:#F9F0DD;
  --font-display:"Young Serif","DM Serif Display",serif; --font-script:"Yellowtail",cursive; --font-sans:"Work Sans",system-ui,sans-serif;
  --radius-control:999px; --radius-container:12px;
  --shadow-1:4px 4px 0 #D9A62E;
  --dur:300ms; --ease:cubic-bezier(.25,.1,.25,1);
}
```

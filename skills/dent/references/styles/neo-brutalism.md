# Neo-Brutalism

**Also called:** neubrutalism, neo-brutal, bold flat, "Gumroad style"
**In one sentence:** Bright flat colors, thick black outlines and hard offset shadows — brutalism made friendly and fun.
**Picture it:** A yellow card with a 3px black border and a solid black shadow shifted 6px down-right, like a sticker on a page.
**Feels like:** bold, playful, energetic, confident, indie.

**Use for:** startups, creator tools, indie SaaS, landing pages, education, marketplaces for creators, Gen-Z products.
**Avoid for:** luxury, corporate finance, medical, calm/wellness.

## Overrides
| Area | Override |
|---|---|
| Color | Off-white or cream background; **saturated flat colors** (yellow #FFD23F, pink #FF6B9D, blue #4D96FF, green #6BCB77, purple #A28BFF) as card/button fills. Black (#111) for text, borders and shadows. |
| Typography | Heavy, chunky sans (Archivo Black, Space Grotesk, Lexend Mega, Bricolage Grotesque, "Clash Display"). Big bold headings. |
| Spacing / layout | Blocky layout of cards; generous padding; elements can be slightly rotated (−2° to 2°) for fun. |
| Radius | 0 or small-to-medium (4–12px). Pick one and keep it. |
| Borders | **Thick black borders (2–4px)** on buttons, cards, inputs, images. |
| Depth | **Hard offset shadows, no blur:** `4px 4px 0 #111` (controls), `6–8px 6–8px 0 #111` (cards). |
| Motion | Snappy (100–200ms), slight overshoot allowed. |
| Hover | Element moves toward its shadow (translate 2px,2px) while shadow shrinks — looks like it's being pressed. Pressed: translate fully onto shadow (shadow 0). |
| Imagery / icons | Flat illustrations, stickers, emoji, bold icons with thick strokes. |
| Components | Colored filled buttons with black border + hard shadow. Inputs white with black border. Tags as colored pills with borders. |

## Signature moves
1. Thick black outlines on everything.
2. Hard, unblurred offset shadows.
3. Saturated flat color blocks.
4. Press effect: element slides into its shadow.

## Do / Don't
- **Do** keep border width and shadow offset identical everywhere.
- **Do** limit to 3–4 fill colors.
- **Don't** add blur, gradients or soft shadows.
- **Don't** put black text on dark saturated fills (check contrast).

## Accessibility watch-outs
- Bright fills behind text: yellow/pink/green work with black text; blue/purple fills may need checking.
- Focus ring must be distinct from the black border — use a colored outline with offset.

## Starter tokens
```css
:root{
  --bg:#FFF8E7; --surface:#FFFFFF; --text:#111111; --border:#111111;
  --c-yellow:#FFD23F; --c-pink:#FF6B9D; --c-blue:#4D96FF; --c-green:#6BCB77;
  --accent:var(--c-yellow); --on-accent:#111111;
  --font-display:"Archivo Black",sans-serif; --font-sans:"Space Grotesk",sans-serif;
  --border-w:3px; --radius-control:8px; --radius-container:12px;
  --shadow-1:4px 4px 0 #111; --shadow-2:8px 8px 0 #111;
  --dur:150ms; --ease:cubic-bezier(.34,1.56,.64,1);
}
.btn{border:var(--border-w) solid var(--border);box-shadow:var(--shadow-1);transition:transform var(--dur),box-shadow var(--dur);}
.btn:hover{transform:translate(2px,2px);box-shadow:2px 2px 0 #111;}
.btn:active{transform:translate(4px,4px);box-shadow:0 0 0 #111;}
```

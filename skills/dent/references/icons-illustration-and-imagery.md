# Icons, Illustration and Imagery

The three kinds of visual assets: Part A icons, Part B illustration, Part C photography/imagery and art direction. One consistent system per product for each.

---

## Part A — Icons

### 1. Choosing an icon set
Use **one** set per product. Good free sets: Lucide, Phosphor (6 weights), Heroicons (outline/solid), Tabler, Material Symbols (variable fill/weight/grade), Remix Icon, Iconoir, SF Symbols (Apple platforms only), Fluent System Icons (Microsoft).
Pick by: style match (stroke vs filled, rounded vs sharp), coverage of your needs, available sizes/weights, license.

### 2. Usage rules
- **Sizes:** 16 (dense UI, inline), **20 (default in controls)**, 24 (navigation, standalone), 32/48 (empty states, features). Stick to the scale.
- **Stroke weight** matches text weight nearby (1.5px at 20–24px is common; 2px for bolder UIs).
- **Outline vs filled:** outline for default/inactive; filled for active/selected (e.g. tab bar) — a common, learnable state signal.
- **Color:** inherit text color (`currentColor`); accent only for interactive/active; semantic colors for status icons.
- **Labels:** icons alone are ambiguous; label them unless universal (search, close ×, menu ☰, home, back, play, settings ⚙ fairly universal, share is platform-specific). Icon-only buttons need accessible names + tooltips.
- **Alignment:** center icons optically with text (align to cap height/x-height); keep icon-text gap 6–8px.
- **Consistent metaphors:** same icon = same meaning everywhere (don't use a trash can for both "delete" and "archive").
- **Platform conventions:** share icon (iOS box-with-arrow vs Android three-dots-connected), back arrow styles, overflow (••• iOS horizontal vs ⋮ Android vertical).

### 3. Designing custom icons (keylines and grid)
- **Canvas:** 24×24 (most common) with **2px padding** → 20×20 live area.
- **Keyline shapes** for optical balance: circle ≈ 20px diameter, square ≈ 18×18, portrait rectangle 16×20, landscape 20×16. Different shapes at these sizes look equally big.
- **Stroke:** one consistent width (1.5 or 2px); align strokes to the pixel grid at 1× for crispness.
- **Corners:** one corner radius rule (e.g. 2px outer); consistent line caps/joins (round or square).
- **Angles:** limit to 45°/90° (and 30°/60° if needed) for consistency.
- **Simplicity:** minimum detail needed to recognize at 16px; test at small size.
- **Perspective:** flat, front-facing; no mixing 3D and 2D.
- **Export:** SVG, `viewBox="0 0 24 24"`, `stroke="currentColor"`, no hard-coded colors, optimized (SVGO).

### 4. Icon accessibility
- Decorative icons: `aria-hidden="true"`.
- Meaningful standalone icons: accessible name (`aria-label` on the button, or `<title>`).
- 3:1 contrast for meaningful icons.

---

## Part B — Illustration

### 5. When to use illustration
- Empty states, onboarding, errors (404), feature explanations, marketing heroes, brand storytelling, abstract concepts that photos can't show.
- Not instead of real product screenshots when users need to see the product.

### 6. Illustration styles (pick one, define it)
| Style | Feel | Fits styles |
|---|---|---|
| Flat vector | Clean, friendly | Flat, Material, Corporate |
| Line art / monoline | Elegant, minimal | Minimal, Japandi, Editorial |
| Hand-drawn / sketchy | Human, informal | Hand-drawn, Organic |
| Isometric | Technical, structured | SaaS, Dark Tech, Corporate |
| 3D render (clay/glossy) | Playful, premium | Claymorphism, Playful, Y2K, Aurora |
| Geometric / abstract | Artistic | Bauhaus, Memphis, Swiss |
| Collage / mixed media | Expressive | Maximalism, Risograph, Anti-design |
| Pixel art | Retro | Pixel |
| Character/mascot-led | Emotional, memorable | Playful, education |

### 7. Illustration system spec (define these, record in DESIGN.md)
- **Palette:** subset of brand colors (+ 1–2 illustration-only tints); limited (4–6 colors).
- **Line:** weight, color (black, darker shade of fill, or none), caps/joins.
- **Shapes:** geometric vs organic; corner roundness matching UI radius.
- **Shading:** none / flat shadows / gradients / grain texture.
- **Perspective:** flat, isometric (30°), or 3D.
- **People:** diverse skin tones, body types, ages, abilities; consistent proportions (realistic vs stylized); avoid stereotypes.
- **Detail level:** consistent across all illustrations; simpler at small sizes (spot illustrations), richer for heroes.
- **Composition:** consistent framing; background shapes/blobs used the same way.
- **Sizes:** spot (64–120px), medium (200–320px), hero (full width).

### 8. Rules
- One style across the product; mixing sources looks cheap.
- Illustrations support the message — they don't replace text.
- Dark mode variants (adjusted colors, no pure white backgrounds baked in).
- Alt text for meaningful illustrations; decorative ones hidden from screen readers.
- Free sources (customize colors to brand): unDraw, Open Peeps, Humaaans, Storyset, Blush, DrawKit, Ouch! — check licenses.
- AI-generated illustrations: generate with a fixed style prompt and palette, curate for consistency, fix anatomical/text errors, and check license terms.

### 9. Motion illustrations
- Lottie (JSON) or Rive for lightweight vector animation; keep loops subtle; pause under reduced motion; provide static fallback.

---

## Part C — Imagery and art direction

Images are often the first thing people notice. Consistent, purposeful imagery makes a design feel premium; random stock makes it feel cheap.

---

### 10. Decide the role of imagery
- **Product imagery** (screenshots, product photos): shows what users get. Highest priority for products.
- **Lifestyle imagery** (people using it, context): shows outcome and emotion.
- **Brand/mood imagery** (textures, abstract, environments): sets atmosphere.
- **Informational** (diagrams, maps, charts): explains.

### 11. Art direction spec (record in DESIGN.md)
- **Subject:** what we show (real customers, product close-ups, workspaces, nature…) and what we never show.
- **Lighting:** natural/soft vs studio/dramatic; warm vs cool.
- **Color treatment:** natural, warm-graded, desaturated, duotone (brand colors), black & white.
- **Composition:** negative space for text overlay, centered vs rule-of-thirds, close-up vs wide.
- **Perspective:** eye-level, overhead flat-lay, candid vs posed.
- **People:** authentic, diverse, real situations; looking at the task, not grinning at camera.
- **Mood words:** e.g. "calm, honest, sunlit".

### 12. Photography rules
- Prefer **real photos** of the real product/team/customers over generic stock.
- If stock: choose candid, specific, locally relevant images; avoid clichés (handshakes, people pointing at screens, headset call-center smiles); apply one consistent color grade.
- **Rule of thirds** and leading lines guide the eye to the subject or CTA.
- Faces attract attention; a person looking toward the headline/CTA directs gaze there (eye-tracking findings on gaze cueing).
- Leave **negative space** where text will go; never put text over busy areas.

### 13. Product screenshots & mockups
- Use real, clean data (no lorem ipsum, no test names); crop to the relevant part; zoom into details rather than shrinking full screens until unreadable.
- Consistent device frames (or no frames) and shadows across the site.
- Keep screenshots updated with the real UI.
- Annotate with callouts sparingly.

### 14. Text over images
- Add a **scrim**: dark gradient overlay (e.g. 0 → 60% black toward the text) or a solid panel behind text.
- **[Rule]** Check contrast against the lightest part under the text.
- Alternative: place text beside the image, not on it.

### 15. Aspect ratios and cropping [Convention]
- Define a small set: **16:9** (hero, video), **4:3** (cards), **3:2** (photos), **1:1** (avatars, products, grids), **4:5** (portrait cards, social), **9:16** (stories/mobile full screen), **21:9** (cinematic banners).
- Use `aspect-ratio` + `object-fit: cover` with a focal point (`object-position`) so crops don't cut heads/products.
- Same ratio for all items in one grid.

### 16. Technical quality
- Serve responsive sizes (`srcset`, `sizes`) and modern formats (**AVIF/WebP** with JPEG fallback); PNG/SVG for graphics with transparency; SVG for logos/icons.
- Compress (aim for hero < ~200–300KB, thumbnails < 50KB as a rough guide).
- Provide 2× resolution for retina.
- Lazy-load below the fold; preload the hero/LCP image; set width/height to prevent layout shift.
- Placeholder while loading: blurred tiny preview (LQIP/BlurHash) or dominant color.

### 17. Accessibility
- **Alt text:** describe the purpose/content in context ("Chef plating a salad in the Bengaluru kitchen"), not "image of". Decorative: `alt=""`.
- Complex images (charts, infographics): short alt + longer description nearby.
- Avoid text in images; if present, include it in alt.
- Video: captions, no autoplay with sound, pause control.

### 18. AI-generated imagery
- Use a **consistent prompt template** (subject + style + lighting + palette + composition + camera/lens) so images match.
- Check for artifacts: hands, text, faces, impossible objects, inconsistent lighting.
- Don't generate images of real people or trademarks; avoid misleading "real customer" images.
- Disclose where appropriate (news, testimonials, health).
- Check licensing/terms of the generator.

### 19. Free image sources (check licenses)
Unsplash, Pexels, Pixabay (photos); Coverr, Mixkit (video); Spline community (3D); Rawpixel public domain. For product images, real photography beats all stock.

# 3D and Real-time Graphics

Use 3D when depth, form or space **is** the message (a physical product, a spatial concept, an explorable world). If a 2.5D layer stack or a pre-rendered video says it as well, use those: cheaper, faster, more accessible. Used by `/dent:3d`, `/dent:motion-graphics`, `/dent:launch-video`.

---

## 1. Decide the form
| Need | Best form |
|---|---|
| Show a physical product from all angles, maybe in AR | `<model-viewer>` with a glTF + poster |
| Hero scene reacting to scroll/pointer, custom look | Three.js or React Three Fiber (+ Drei) |
| Complex app (configurator, editor, physics, XR) | Babylon.js or R3F + ecosystem (Rapier physics, XR) |
| Designer-built interactive 3D, quick | Spline export (check runtime size and plan) |
| Cinematic hero loop, no interaction | Pre-rendered video/image sequence from Blender (smaller, guaranteed look) |
| Abstract GPU visuals (gradients, noise, fluid) | Fragment shader on a quad (OGL/regl/Three) |

## 2. Art direction (where most 3D looks cheap)
- **Lighting:** an HDRI environment (Poly Haven, CC0) + 1 key light for shape + rim light for separation; soft contact shadows (Drei `ContactShadows`/baked AO). Avoid default flat ambient light.
- **Materials:** physically based (metalness/roughness) with real variation (roughness maps, subtle normal detail). Brand color as a material accent, not paint on everything.
- **Camera:** choose a lens (35–50 mm feel for products; wide for spaces); limited orbit ranges; ease camera moves; no constant spinning.
- **Composition:** same rules as 2D: one focal object, negative space, text never over busy geometry.
- **Post-processing:** subtle only (tone mapping ACES/AgX, slight bloom on emissive parts, film grain 2–4 %, depth of field for hero shots). Each pass costs frames.
- **Style options:** realistic PBR · clay/matte (single-color, soft light) · toon/cel shading · wireframe/blueprint · low-poly · glass/refraction (expensive) · point-cloud/particles.

## 3. Asset pipeline
1. Model in Blender (or source with licence, `../catalog/asset-sources.md` §5).
2. Export **glTF/GLB**; apply transforms; name meshes/materials.
3. Optimise: `gltf-transform` (dedupe, weld, simplify), **Draco or Meshopt** geometry compression, **KTX2/Basis** textures, power-of-two sizes (1–2 K for web), LODs for big scenes.
4. Budgets (mid-range phone target): < 5 MB total 3D payload for a hero, < 100 k triangles visible, < 50–100 draw calls, textures < 64 MB GPU memory.
5. Generate the React component (`gltfjsx`) for R3F when useful.

## 4. Build rules
- **Lazy-load** the 3D canvas after the main content; show a designed poster immediately (also the no-WebGL and reduced-motion fallback).
- Cap `devicePixelRatio` at 1.5–2; use `frameloop="demand"` (R3F) or render only on change for static scenes.
- Pause rendering when offscreen (IntersectionObserver) and when the tab is hidden.
- Interaction: limit orbit (min/max polar and distance), damping, touch gestures, a reset button, keyboard alternatives for any meaningful interaction (buttons to rotate/next view).
- Text: keep headings/body in HTML over or beside the canvas; never only in 3D.
- **Cleanup:** dispose geometries, materials, textures and render targets on unmount (R3F does most automatically; manual Three.js must call `.dispose()`).
- WebGPU when available, WebGL fallback; feature-detect, never assume.

## 5. Accessibility and comfort
- `prefers-reduced-motion`: no auto-rotation or camera drift; static hero frame; user-initiated movement only.
- Provide a text description of what the scene shows (`aria-label` on the canvas wrapper or adjacent text).
- No rapid camera moves or full-screen flashes; avoid vertigo (large parallax, spinning).
- AR/VR: comfort first (no forced locomotion), clear exit.

## 6. Verification
- Measure fps (Chrome DevTools performance panel, `stats.js`/r3f-perf in dev) on a throttled CPU and a mid-range phone profile; target 60 fps, minimum 30 fps on low end.
- Check load: time to poster, time to interactive scene, payload size.
- Test no-WebGL fallback (disable hardware acceleration or force fallback), reduced motion, touch, resize, tab-away/return, unmount/remount memory (DevTools memory snapshot shouldn't grow).
- Screenshot key camera positions at phone and desktop.

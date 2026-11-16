# Motion Graphics and Visual Experiences

Motion graphics are **designed compositions in time**: typography, shapes, illustrations, images, UI and particles choreographed to communicate and to feel like a brand. They are not "add fade-ins". Used by `/dent:motion-graphics`, `/dent:launch-video`, `/dent:video`, `/dent:3d`, All-out landing pages.

Interface motion (hover, state changes, transitions) lives in `../modern-layer.md`. The per-project motion language and verification live in `motion-system-and-verification.md`. Technology choice lives in `motion-tech-catalog.md`.

---

## 1. Know what you're making

| Kind | What it is | Lives in | Typical tech |
|---|---|---|---|
| **Interface motion** | Feedback, transitions, state changes | Product UI | CSS, WAAPI, Motion |
| **Motion graphics** | Authored compositions: kinetic type, shape animation, animated illustration, title cards | Hero sections, videos, social, README | GSAP, Motion, SVG, Lottie, Rive, code-video |
| **Interactive graphics** | Visuals that respond to pointer, scroll, state, data | Landing pages, products, explorables | GSAP ScrollTrigger, CSS scroll-driven, Canvas, PixiJS, Rive |
| **3D experiences** | Real-time scenes, product viewers | Hero, configurators, games | Three.js, R3F, Babylon, Spline |
| **Product animation** | The product's UI shown working (demo reels, feature tours) | Landing pages, launch videos | Real UI + Motion/GSAP, screen capture, code-video |
| **Data animation** | Charts and numbers changing over time | Reports, dashboards, explainers | D3/Visx + transitions, ECharts, Motion Canvas |
| **Generative art** | Procedural visuals (noise, particles, flow fields, shaders) | Backgrounds, identity, installations | Canvas 2D, p5.js, regl/OGL, shaders |

## 2. Dimensions: 1D → XR

| Dimension | Means | Examples | Strengths | Costs |
|---|---|---|---|---|
| **1D** | Motion along a line or in time only: text, strokes, timelines, counters, waveforms, tickers, progress | Type-on headlines, line drawing, number counters, marquee, audio waveform | Cheapest, most legible, accessible | Can feel thin without composition |
| **2D** | Flat vector/raster on a plane | Shape morphs, animated illustration, collage, kinetic type compositions, Lottie/Rive | Brand-precise, light, crisp | Needs strong composition |
| **2.5D** | Layered 2D with depth cues | Parallax layers, paper cut-outs, isometric scenes, card stacks with perspective, depth-of-field blur | Depth without 3D cost | Parallax can cause motion sickness: keep subtle |
| **3D (real-time)** | Rendered scenes in the browser | Product viewers, scenes reacting to scroll, particles in 3D, shader worlds | Immersion, product understanding | Performance, loading, a11y, fallbacks |
| **3D (pre-rendered)** | Blender/C4D renders played as video/image sequences | Product hero loops, launch videos | Film quality, cheap to play | Not interactive, file size |
| **XR** | AR/VR/spatial | Model viewer AR (`<model-viewer>`), WebXR scenes | Presence | Device support, comfort |

Pick the **lowest dimension that fully expresses the concept**. A great 1D/2D piece beats a mediocre 3D one.

## 3. The pipeline (never skip steps 1–4)
1. **Concept:** one sentence ("ink settling into a perfect circle", "the grid assembles itself like a machine"). Link it to the product's direction (`../creative/directions-library.md` §4).
2. **Directions (Polished+):** 2–3 motion directions with a reference frame + motion description each.
3. **Storyboard:** 4–12 key frames, each with time, composition, what moves and how, sound cue (`templates/MOTION.md` §5). Every key frame must work as a **still poster**.
4. **Animatic / timing:** block the timing with simple shapes; lock rhythm before detail. Count beats: intro (hook) → build → climax → resolve/loop.
5. **Build:** chosen engine; tokens for durations/easings; reusable timeline functions.
6. **Polish:** overlaps, follow-through, secondary motion, motion blur feel (via scale/opacity), sound sync.
7. **Accessibility + performance pass:** reduced-motion version, pause control, no flashes, budgets.
8. **Verify and export:** play-through checks, frame-rate measurement, exports for each destination.

## 4. Animation principles (apply them, don't name-drop them)
- **Timing & spacing:** durations from the system; spacing (easing) decides weight. Heavy things start slow, light things snap.
- **Anticipation:** a small opposite move before a big one (−4 px before a 200 px slide; scale 0.96 before a pop).
- **Follow-through & overlap:** parts settle at different times (title lands, underline arrives 80 ms later, subtitle 160 ms later).
- **Slow in/out:** ease-out for entrances, ease-in for exits, ease-in-out for moves between positions; linear only for mechanical/continuous loops.
- **Arcs:** natural moves curve (animate x and y with different easings, or along an SVG path).
- **Squash & stretch:** only in playful directions; preserve volume.
- **Secondary action:** a subtle reaction elsewhere (background shifts 4 px when the title lands).
- **Staging:** one focal action at a time; dim or still everything else.
- **Exaggeration:** push key moments slightly beyond real; keep UI motion restrained.
- **Appeal & consistency:** the same personality everywhere (motion tokens).

## 5. Composition in time
- **Hierarchy over time:** the most important element moves first or most; supporting elements follow.
- **Rhythm:** vary durations (short-short-long); hold after a reveal so it can be read (≥ 0.5 s + 0.3 s per word for text).
- **Direction:** consistent travel direction implies narrative (left→right = forward); reversals mark change.
- **Negative space:** leave empty frames/beats; constant motion is noise.
- **Transitions as meaning:** match-cut shapes (a circle becomes the logo O), mask wipes in the direction of the story, morphs that show transformation.
- **Loops:** hide the seam: end state = start state, or a cut on motion; 3–8 s loops for heroes; pause after one or two loops on content pages.

## 6. Technique cookbook (with build notes)

**6.1 SVG line drawing (1D):**
```css
.draw path{stroke-dasharray:var(--len);stroke-dashoffset:var(--len)}
@media (prefers-reduced-motion:no-preference){.draw.in path{animation:draw 1.2s cubic-bezier(.65,0,.35,1) forwards}}
@keyframes draw{to{stroke-dashoffset:0}}
```
Set `--len` from `path.getTotalLength()`. Under reduced motion the path is simply visible (no dash).

**6.2 Mask/clip reveals (2D):** `clip-path: inset(0 100% 0 0)` → `inset(0)` for wipes; circle reveals from the click point for transitions. GPU-friendly in modern browsers.

**6.3 Shape morphing:** paths with matching point counts animate with WAAPI/CSS `d:` in supporting browsers; otherwise GSAP MorphSVG (free since 2025) or flubber for interpolation.

**6.4 Kinetic typography patterns:**
- *Word swap:* fixed sentence, one slot cycles words with vertical mask slides.
- *Scale cascade:* words punch in at scales 3 → 1 on beat.
- *Typewriter + correction:* type, strike, retype (good for contrarian claims).
- *Split and reassemble:* characters scatter (random rotation ±30°, 40–80 px) then assemble into the headline.
- *Variable axis breathing:* weight/width oscillates with audio or scroll.
- *Grid type:* letters snap into grid cells like a departure board (split-flap).
Rules: the final text is real DOM text; animated copies are `aria-hidden`; reduced motion shows the final state.

**6.5 Scroll-driven storytelling:**
- CSS first: `animation-timeline: view()` / `scroll()` with `animation-range`, feature-detected with `@supports`, built the way `mwg:scrollytelling` and `mwg:scroll-entry-exit-effects` say (decorative: static state as fallback; essential: the guide's fallback).
- GSAP ScrollTrigger for pinning, scrubbing timelines, snapping between scenes, complex sequences.
- Pattern "sticky stage": a pinned visual on one side changes as text steps scroll past; each step ≤ 1 viewport.
- Never scroll-jack (no changed scroll speed/direction). Smooth-scroll libraries (Lenis) only if they don't break native behaviour, keyboard and reduced motion.

**6.6 Product animation (UI in motion):** recreate the UI in HTML/CSS (crisp, editable, legible) or use real captures. Choreograph a cursor (custom SVG) that clicks, types and drags; zoom into details with scale + translate on a wrapper; highlight with spotlight masks. Text in the UI must be real and legible at the final size.

**6.7 Data animation:** animate from the previous state, not from zero; keep axes stable unless the change is the story; count-ups with tabular digits; annotate the moment that matters.

**6.8 Particles and generative fields:** Canvas 2D for ≤ ~5 000 particles; WebGL (regl/OGL/Three/PixiJS) beyond. Use noise (simplex/curl) for organic flow, attraction to shapes/text for "forming" effects. Cap DPR at 2, pause when offscreen (`IntersectionObserver`) and when the tab is hidden, provide a static frame for reduced motion.

**6.9 Shader backgrounds:** a fragment shader on a full-screen quad (gradients, noise, grain, caustics, aurora). Keep it cheap (few octaves), render at 0.5–0.75 resolution and upscale, and offer a CSS gradient fallback.

**6.10 Cursor and pointer interaction:** spotlight following the pointer, magnetic CTA (≤ 8 px), tilt (≤ 6°), trails. Pointer devices only (`(hover:hover) and (pointer:fine)`), never in forms/tools, no lag (use `requestAnimationFrame` + lerp 0.15–0.25).

**6.11 Transitions between pages/sections:** View Transitions API (`document.startViewTransition`, cross-document `@view-transition`) for shared-element morphs; FLIP for in-page reordering; masks for scene changes.

**6.12 Lottie / Rive:** use pre-authored vector animations when a designer/AE workflow exists (Lottie) or when the animation needs interactive states (Rive state machines). Check file size, render cost, and reduced-motion handling (show a static frame).

## 7. Motion graphics for README, social and video
- **GitHub README:** no JS. Use animated SVG (CSS/SMIL inside the SVG runs in `<img>`; include `@media (prefers-reduced-motion: reduce)` inside the SVG), optimised GIF/APNG/WebP for raster, or MP4 uploaded via the GitHub editor (renders a player). Keep under a few MB; provide a static poster for dark/light with `<picture>`.
- **Social:** export 9:16/1:1/16:9 cuts; captions; first frame is the hook.
- **Video:** build with code-video tools (HyperFrames, Remotion, Motion Canvas) or capture the web animation (Playwright video, OBS) and finish in an editor (`../video/video-tools-and-pipeline.md`).

## 8. Creative prompts when stuck
- Take the product's core verb (log, ship, measure, protect) and make it the motion ("measure" → dimension lines draw around the headline).
- Make the logo out of the product's data (bars, points, waveforms) and resolve into the mark.
- Use one physical material for every transition (ink, paper, glass, liquid, light).
- Reverse expectation: everything is still except one thing that moves.
- Let sound drive the cut: design the animation to the beats of a 4-bar loop.

## 9. Never
Random gradients/particles without a concept · motion that delays content · loops that never stop on reading pages · essential info only in motion · flashing > 3/s · ignoring reduced motion · 3D when 2D says it better.

# Motion, Graphics and 3D Technology Catalogue

Pick the **simplest engine that achieves the result**, and only one engine per job. Status legend: ✓ checked 2026-11-14 · K from knowledge, verify · ⚠ caveat. Licences change: confirm on the official page before recommending for production.

---

## 1. Selection ladder (start at the top, go down only when needed)
1. **CSS transitions/animations** — state changes, hovers, simple reveals, loops. Zero dependencies.
2. **CSS scroll-driven animations + View Transitions** — scroll-linked reveals, page/element morphs (progressive enhancement).
3. **Web Animations API (WAAPI)** — JS-controlled keyframes, play/pause/reverse, `finished` promises, without a library.
4. **Motion (Framer Motion)** — React (and vanilla) UI animation, layout animations, gestures, springs, exit animations.
5. **GSAP** — complex timelines, precise sequencing, ScrollTrigger pinning/scrubbing, SVG morphing, text splitting; framework-agnostic.
6. **Lottie / dotLottie** — pre-authored After Effects vector animations.
7. **Rive** — interactive vector animations with state machines (buttons, characters, onboarding).
8. **Canvas 2D / PixiJS** — many 2D sprites/particles, games, 2D WebGL.
9. **Three.js / React Three Fiber** — real 3D.
10. **Custom shaders (GLSL/WGSL)** — bespoke GPU effects when nothing simpler works.

## 2. Web animation and timeline control

| Tech | Role | Environments | Strengths | Weaknesses | Licence | Status |
|---|---|---|---|---|---|---|
| [CSS animations/transitions](https://developer.mozilla.org/docs/Web/CSS/CSS_animations) | Declarative motion | All browsers | Free, fast (compositor), reduced-motion via media query | Limited sequencing/control | Web standard | ✓ |
| [Scroll-driven animations](https://developer.mozilla.org/docs/Web/CSS/CSS_scroll-driven_animations) | Scroll/view timelines in CSS | Chromium; others progressing — check support | No JS, smooth | Needs fallback where unsupported | Web standard | K |
| [View Transitions API](https://developer.mozilla.org/docs/Web/API/View_Transition_API) | Shared-element and page transitions | Same-document widely supported; cross-document in Chromium — check | Native morphs | Support varies; design fallback (instant) | Web standard | K |
| [Web Animations API](https://developer.mozilla.org/docs/Web/API/Web_Animations_API) | JS keyframes with control | All modern browsers | No dependency, `getAnimations()` for testing | Verbose for complex sequences | Web standard | ✓ |
| [Motion](https://motion.dev) (Framer Motion) | UI animation for React; vanilla `animate()` | React, vanilla, Vue (motion-v) | Layout/shared animations, springs, gestures, `useReducedMotion` | React-centric features; bundle if overused | MIT (paid "Motion+" extras exist) | K |
| [GSAP](https://gsap.com) | Timelines, ScrollTrigger, SplitText, MorphSVG, DrawSVG, Flip, Observer, etc. | Any (vanilla, React via `useGSAP`) | Industry-standard sequencing and scroll control | Imperative; clean up with `gsap.context()`/`useGSAP` | **Free incl. all plugins and commercial use under GSAP's standard "no charge" licence (Webflow); restriction: tools that compete with Webflow's visual animation builder need permission. Not OSI open source.** | ✓ 2026-11-14 |
| [Anime.js](https://animejs.com) | Lightweight timeline engine | Any | Small, nice API (v4 modular) | Smaller ecosystem than GSAP | MIT | K |
| [AutoAnimate](https://auto-animate.formkit.com) | Zero-config list/layout transitions | React, Vue, Svelte, vanilla | One line for add/remove/move | Little control | MIT | K |
| [Theatre.js](https://www.theatrejs.com) | Visual timeline editor for code (esp. Three.js) | Vanilla, R3F | Keyframe sequences with a studio UI | Studio is dev-only | **Core Apache-2.0; Studio AGPL-3.0 (dev tool, not shipped)** | ✓ 2026-11-14 |
| [Popmotion](https://popmotion.io) | Low-level animation functions | Any | Springs/inertia | Superseded by Motion | MIT | K |
| [SplitType](https://github.com/lukePeavey/SplitType) | Split text for animation | Any | Free, small | Pair with any engine; handle a11y | MIT | K |

## 3. Vector and interactive animation

| Tech | Role | Strengths | Weaknesses | Licence | Status |
|---|---|---|---|---|---|
| [Lottie (lottie-web)](https://airbnb.io/lottie) / [dotLottie](https://dotlottie.io) | Play After Effects animations (JSON / .lottie) | Designer workflow, crisp vectors | Heavy JSON for complex scenes; some AE features unsupported; CPU-bound SVG renderer | MIT (players); LottieFiles platform has paid tiers | K |
| [Rive](https://rive.app) | Interactive vector animation with state machines | Small files, runtime state machines, events (sound hooks), many runtimes | Requires the Rive editor (free + paid plans) | Runtimes MIT; editor has free/paid plans | K |
| SVG + SMIL/CSS | Native vector animation | Works in README `<img>` (no JS), tiny | Complex sequences are hard to author | Web standard | ✓ |
| [Canvas 2D](https://developer.mozilla.org/docs/Web/API/Canvas_API) | Immediate-mode 2D drawing | Thousands of shapes, full control | Not accessible by itself (provide text) | Web standard | ✓ |
| [PixiJS](https://pixijs.com) | 2D WebGL/WebGPU renderer | Very fast sprites/particles/filters | Learning curve; a11y is your job | MIT | K |
| [Konva](https://konvajs.org) | Canvas 2D scene graph | Interactive canvas apps/editors | Not for heavy particles | MIT | K |
| [Paper.js](http://paperjs.org) | Vector graphics scripting on canvas | Path boolean ops, generative vectors | Older, less active | MIT | K |
| [Two.js](https://two.js.org) | Renderer-agnostic 2D | SVG/canvas/WebGL output | Smaller community | MIT | K |

## 4. 3D and real-time graphics (details in `3d-and-realtime.md`)

| Tech | Role | Strengths | Weaknesses | Licence | Status |
|---|---|---|---|---|---|
| [Three.js](https://threejs.org) | 3D engine | Huge ecosystem, examples, WebGL + WebGPU renderer | You manage cleanup/perf | MIT | K |
| [React Three Fiber](https://r3f.docs.pmnd.rs) + [Drei](https://drei.docs.pmnd.rs) | React renderer for Three + helpers | Declarative scenes, huge helper set | React only | MIT | K |
| [Babylon.js](https://www.babylonjs.com) | Full 3D engine | Inspector, physics, XR, PBR, WebGPU | Larger | Apache-2.0 | K |
| [OGL](https://github.com/oframe/ogl) | Minimal WebGL library | Tiny, great for shaders/effects | Fewer helpers | Unlicense | K |
| [regl](https://github.com/regl-project/regl) | Functional WebGL | Precise control, small | Low-level | MIT | K |
| [PlayCanvas](https://playcanvas.com) | Engine + editor | Games, configurators | Editor is a hosted service | Engine MIT; editor plans | K |
| [Spline](https://spline.design) | Visual 3D design tool + web runtime/export | Fast for designers, interactive states | Runtime size; hosted features need plans | Runtime open (check); tool has free/paid plans | K |
| [`<model-viewer>`](https://modelviewer.dev) | Web component for glTF + AR | Easiest product viewer with AR | Limited custom scenes | Apache-2.0 | K |
| WebGPU | Next-gen GPU API | Compute, performance | Support still expanding; always fall back to WebGL | Web standard | K |

## 5. Scroll and smooth-scroll

| Tech | Role | Notes | Licence | Status |
|---|---|---|---|---|
| GSAP ScrollTrigger | Pin, scrub, snap, scroll-linked timelines | Most capable; `matchMedia` for responsive + reduced motion | GSAP standard licence (free) | ✓ 2026-11-14 |
| CSS scroll-driven animations | Native scroll timelines | Use with fallbacks | Standard | K |
| [Lenis](https://lenis.darkroom.engineering) | Smooth scroll | Keep native feel; disable under reduced motion; don't break anchors/keyboard | MIT | K |
| [Locomotive Scroll](https://scroll.locomotive.ca) | Smooth scroll + parallax (v5 built on Lenis) | Same cautions | MIT | K |
| IntersectionObserver | Trigger on enter | Cheapest reveal trigger | Standard | ✓ |

## 6. Creative coding and generative

| Tech | Role | Licence | Status |
|---|---|---|---|
| [p5.js](https://p5js.org) | Sketching, generative art, education | LGPL-2.1 (library); your sketches are yours | K |
| [Paper.js](http://paperjs.org) | Generative vector | MIT | K |
| [regl](https://github.com/regl-project/regl) / [OGL](https://github.com/oframe/ogl) | Shader-driven visuals | MIT / Unlicense | K |
| [simplex-noise](https://github.com/jwagner/simplex-noise.js) | Noise for organic motion | MIT | K |
| [tsParticles](https://particles.js.org) | Configurable particles | MIT (⚠ easy to misuse as decoration) | K |
| [Matter.js](https://brm.io/matter-js) / [Rapier](https://rapier.rs) | 2D physics / 2D+3D physics (WASM) | MIT / Apache-2.0 | K |
| [Shadertoy](https://www.shadertoy.com) | Shader reference/learning | Per-shader licence (often CC BY-NC-SA by default!) | K |

## 7. Code-to-video and motion tools (details in `../video/video-tools-and-pipeline.md`)

| Tech | Role | Licence | Status |
|---|---|---|---|
| [HyperFrames](https://github.com/heygen-com/hyperframes) (HeyGen) | Write HTML/CSS/JS, render deterministic MP4 (headless Chrome + FFmpeg); built for AI agents | Apache-2.0, free at any scale | ✓ 2026-11-14 |
| [Remotion](https://www.remotion.dev) | React → video | **Remotion License: free for individuals, non-profits and for-profit orgs ≤ 3 people; company licence above that** | ✓ 2026-11-14 |
| [Motion Canvas](https://motioncanvas.io) | TypeScript animation with timeline editor (great for explainers) | MIT | K |
| [Revideo](https://re.video) | Motion Canvas fork for programmatic video | MIT | K |
| [Manim (Community)](https://www.manim.community) | Math/diagram animation (Python) | MIT | K |
| Blender | 3D + 2D (Grease Pencil) + compositing + video editing | GPL (output is yours) | K |

## 8. Decision examples
- Hero headline split reveal + section reveals → CSS (+ scroll-driven) only.
- React app with drawer, list reorder, shared-element card → Motion.
- Scroll story with pinned product, scrubbed sequence, SVG morphs → GSAP + ScrollTrigger (one engine; no Motion for the same section).
- Interactive mascot/button with states and sounds → Rive.
- Designer hands over After Effects animation → Lottie/dotLottie.
- 20 000-particle logo formation → WebGL (OGL/Three points) with static fallback.
- Product 3D viewer with AR → `<model-viewer>`; bespoke scene → R3F.
- Launch video built by an agent → HyperFrames (Apache-2.0) or Remotion (check headcount licence) or Motion Canvas.

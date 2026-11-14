# Motion System and Motion Verification

A project's motion should feel like one personality, not a pile of effects. Define it once (tokens + rules), apply it everywhere, verify it works. Template: `templates/MOTION.md`.

---

## 1. Motion personality
Pick one (from the direction) and let it set the numbers:

| Personality | Durations | Easing | Springs | Overshoot | Fits |
|---|---|---|---|---|---|
| **Precise** | Short (120–260 ms) | Strong ease-out, standard | Critically damped (ζ≈1) | None | Tools, finance, dev |
| **Calm** | Long (300–600 ms) | Gentle ease-in-out | Soft (ζ≈0.9, slow) | None | Wellness, editorial, luxury |
| **Elastic** | Medium (200–400 ms) | Ease-out + spring | Bouncy (ζ≈0.5–0.7) for celebrations only | Small | Playful, kids, social |
| **Weighty** | Medium-long, slow start | Ease-in-out with long tail | Heavy mass | None | Premium hardware, 3D |
| **Mechanical** | Short, uniform | Linear-ish steps, hard stops | None | None | Utilitarian, retro tech, terminal |
| **Organic** | Varied, overlapping | Custom curves, noise | Soft | Slight | Nature, craft, hand-drawn |

## 2. Tokens (adapt numbers to the personality)
```css
:root{
  --dur-instant:80ms; --dur-fast:160ms; --dur-normal:260ms; --dur-slow:420ms; --dur-scene:900ms;
  --ease-out:cubic-bezier(.16,1,.3,1); --ease-in:cubic-bezier(.7,0,.84,0);
  --ease-in-out:cubic-bezier(.65,0,.35,1); --ease-standard:cubic-bezier(.2,0,0,1);
  --stagger:40ms; --distance-sm:8px; --distance-md:16px; --distance-lg:32px;
}
```
Springs (Motion): UI `{ type:"spring", stiffness:400, damping:40 }`; playful `{ stiffness:260, damping:16 }`; sheets `{ stiffness:300, damping:30 }`.

## 3. Rules of the system
- **Entrances** ease-out, from `--distance-sm/md` + opacity; **exits** ease-in, 20–30 % faster.
- **Stagger** ≤ 8 items, total ≤ 500 ms; rest appear together.
- **Direction is meaning:** deeper = from right/below, back = reverse.
- **Interruptibility:** user input cancels or redirects running animations (springs and WAAPI `reverse()`), never queues them.
- **Frequency rule:** the more often something happens, the shorter (or absent) its animation.
- **Page transitions:** one style product-wide (fade-through, shared element, or slide), ≤ 400 ms.
- **Scroll:** one storytelling moment per page; reveals trigger once at 10–20 % visibility.
- **Sound sync:** sounds start on the motion's key frame (impact/landing), not at the start (`../audio/sound-design.md` §6).
- **Reduced motion:** every animation lists its alternative: instant, fade only, or static frame. Essential feedback stays visible.

## 4. Performance budget
- Animate `transform`, `opacity` (and `filter`/`clip-path` sparingly). Never animate layout properties on large/many elements.
- ≤ 3–4 concurrently animating regions on mobile; pause offscreen loops; stop decorative loops after 1–2 cycles on reading pages.
- `will-change` only just before animating; remove after.
- No layout shift from animation (reserve space).
- Heavy (WebGL/particles/shaders/video) lazy-loaded with a static poster and measured fps.

## 5. Verification (do not claim motion works because it compiles)

| Check | How | Pass when |
|---|---|---|
| Plays as designed | Record or step through (DevTools Animations panel; Playwright `page.video`; screenshots at timeline marks) | Key frames match the storyboard |
| Timeline integrity | Each sequence completes; `finished` promises/`onComplete` fire; loops seam cleanly | No stuck or half states |
| Sync | Elements that should move together do; audio cues hit key frames (±1 frame ≈ 16–40 ms) | Visually and audibly aligned |
| Interaction | Pointer, touch and keyboard triggers all work; interrupting mid-animation behaves | No queued or broken states |
| Responsive | Resize during and after; phone and desktop compositions | No clipping, overflow, or misaligned scenes |
| Reduced motion | Emulate `prefers-reduced-motion: reduce` (verify_page.py does this) | Content fully visible; decorative motion off; `document.getAnimations()` empty or only essential |
| Visual glitches | Watch for flicker, jank, z-index pops, font swaps mid-animation, layout shift | None |
| Performance | DevTools Performance with 4× CPU throttle; fps meter for WebGL | ~60 fps target; no long tasks > 50 ms during animation |
| Cleanup | Navigate away/unmount and back; check listeners, rAF loops, GSAP contexts, WebGL resources | Memory stable; no duplicate animations |
| Accessibility | Pause control for > 5 s auto-motion; no flashes > 3/s; essential info not motion-only | All pass |

Report each as Passed / Failed / Not run with evidence (e.g. "fps 58–60 at 4× throttle, recorded in Performance panel").

## 6. Capturing motion as evidence and assets
- Playwright: `browser.new_context(record_video_dir=..., viewport=...)` records WebM; trim with FFmpeg.
- GIF for README: `ffmpeg -i in.webm -vf "fps=24,scale=960:-1:flags=lanczos,split[a][b];[a]palettegen[p];[b][p]paletteuse" -loop 0 out.gif` (keep small; prefer MP4 where supported).
- Poster frame: screenshot at the most representative timestamp.

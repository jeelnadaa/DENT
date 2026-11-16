# Motion Menu: ask, choose, deliver

DENT used to under-animate: "use motion with purpose" turned into "use almost no motion". This file fixes that. Motion is **asked about, chosen from a menu, planned item by item, built, and verified** like any other requirement.

Used by `/dent:motion`, `/dent:motion-graphics`, `/dent:create`, `/dent:polish`, the landing-page and app recipes, and the router (`../workflow/orchestration.md` Step 4) for any visual build at Standard effort or above.

Technique details: `../modern-layer.md` (interface motion), `motion-graphics.md` (compositions, kinetic type, generative), `motion-tech-catalog.md` (which engine), `motion-system-and-verification.md` (tokens and checks).

---

## 1. Ask the user (always, unless they already said what they want or said "no motion")

Ask **two questions, one at a time**. Use the agent's question tool with **multi-select** for the first.

**Question A: "Which kinds of motion do you want?"** (multi-select, pre-tick the recommended set for the product from §4)

| Option | One-line explanation for the user |
|---|---|
| **Page load & hero entrance** | The first screen builds itself in: headline, image and buttons arrive in a choreographed sequence |
| **Scroll animations** | Things react as you scroll: reveals, parallax depth, pinned scenes, progress, scrubbed sequences |
| **Hover effects** | Cards lift, images zoom, links underline, buttons respond, spotlight and tilt on desktop |
| **Micro-interactions** | Buttons press, toggles slide, checkmarks draw, copy and like confirm, inputs react |
| **Page & view transitions** | Moving between pages or views morphs smoothly instead of cutting |
| **Text & typography motion** | Split-line reveals, word swaps, typewriter, variable-weight shifts, marquee bands |
| **Data & number animation** | Counters roll, charts animate between states, progress fills |
| **Layout animation** | Lists reorder, cards expand, filters rearrange items, shared elements move between places |
| **Background & ambient** | Slow gradient drift, grain, light, subtle particles or shapes that make the page feel alive |
| **Cursor & pointer effects** | Custom cursor, magnetic buttons, trails, spotlight following the pointer (desktop only) |
| **Illustration & SVG animation** | Line drawing, morphing icons and logos, animated illustrations, Lottie/Rive |
| **Loading & feedback states** | Skeleton shimmer, progress, success bursts, error shake, toast choreography |
| **3D & depth** | Tilt cards, 3D objects reacting to scroll or pointer, layered depth |
| **Gestures (touch)** | Swipe, drag, pull-to-refresh, bottom-sheet physics |
| **You choose (Recommended)** | I'll pick the best set for this product and show you the list |

**Question B: "How strong should the motion be?"**

| Intensity | Feels like | Durations | Distance | Springs |
|---|---|---|---|---|
| **Subtle** | Calm, professional, almost invisible | 120–300 ms | 4–12 px | None / critically damped |
| **Balanced (Recommended for most)** | Alive and polished, never distracting | 160–500 ms, hero up to 900 ms | 8–24 px | Gentle |
| **Expressive** | Memorable, energetic, brand-forward | 200–700 ms, hero up to 1.4 s | 16–60 px, scale and rotation | Visible bounce on celebrations |
| **Cinematic** | Award-site storytelling, scenes and sequences | Scenes 0.6–2 s, scroll-scrubbed timelines | Large, choreographed, 2.5D/3D | Physics where it fits |

If the user picks "You choose", select from §4, then **show the chosen list** (one line each) so they can remove anything before you build.

**If the question tool limits options (Claude's allows 4 per question):** don't cram. Ask in this order, one question per message:
1. **"How should I handle motion?"**: *You choose (Recommended): I'll pick the best set for this product and show it* · *Let me pick the kinds* · *Keep it minimal* (state changes and hovers only).
2. Only if "Let me pick": up to four **multi-select** questions, each with the 4 kinds of one group (the user can tick several, or none):
   - **Page & scroll:** Page load & hero entrance · Scroll animations · Page & view transitions · Background & ambient
   - **Interaction:** Hover effects · Micro-interactions · Cursor & pointer effects · Gestures (touch)
   - **Content:** Text & typography motion · Data & number animation · Layout animation · Loading & feedback states
   - **Visual depth:** Illustration & SVG animation · 3D & depth (+ "Neither")
   Skip groups that clearly don't apply (e.g. Gestures on a desktop-only tool), and say so.
3. **Intensity** (Question B): Subtle · Balanced (Recommended) · Expressive · Cinematic.

Agents without a question tool: ask the same in plain text with numbered options and let the user answer with numbers (e.g. "1, 2, 5, 9").

Non-interactive or "don't ask": use §4's recommended set at **Balanced** and list it in the Decision Log.

## 2. Minimum motion (the floor)

Unless the user asked for little or no motion, deliver **at least**:

| Effort | Minimum on a landing/marketing page | Minimum in an app screen |
|---|---|---|
| Essential | Hero entrance + hover on all interactive elements + micro-interactions on buttons/toggles | Micro-interactions + state transitions (menus, dialogs, toasts) |
| Standard | Essential + scroll reveals per section (varied, not one fade-up for everything) + one scroll-linked moment + text reveal on the hero headline | Essential + layout animation for list changes + number/data animation + loading skeletons |
| Polished | Standard + parallax/depth or pinned scroll scene + page/view transitions + animated SVG or illustration + ambient background + magnetic/spotlight hover on hero CTAs | Standard + view transitions + drawer/sheet physics + chart transitions from previous state + success moments |
| All-out | Polished + a signature motion-graphics sequence (`motion-graphics.md`) + choreographed scroll story with scrubbed timeline + cursor/pointer layer (desktop) + optional sound sync | Polished + gesture physics, shared-element transitions, command-palette choreography, celebratory peak-end moment |

"Restraint" means **purpose and quality**, not absence. A page with only a fade-in is under-animated at Standard and above.

## 3. The catalogue (what each type includes)

For each chosen category, pick concrete items. Defaults are for **Balanced**; scale by intensity.

### 3.1 Page load & hero entrance
- **Choreographed intro:** background → headline lines (split reveal, 60–90 ms stagger) → subhead → CTAs → visual; total ≤ 1.2 s; content usable immediately.
- **Mask / clip reveals** on the hero image (wipe in the reading direction).
- **Number or logo build** (counter to the real number, logo strokes draw).
- Tech: CSS keyframes or WAAPI; GSAP timeline for complex sequences.

### 3.2 Scroll animations
- **Reveal on enter:** fade + rise 16–24 px, scale 0.96 → 1, blur 8 → 0, clip-path wipe. **Vary them per section type**, don't repeat one effect everywhere.
- **Staggered groups:** cards/list items enter 40–60 ms apart.
- **Parallax:** 2–4 layers at 5–30 % speed difference; foreground faster.
- **Pinned / sticky scenes:** a visual stays pinned while steps scroll past and change it.
- **Scrubbed timelines:** animation progress tied to scroll position (product rotates, chart draws, text highlights word by word).
- **Horizontal scroll section** (gallery/process) inside vertical scroll, with visible progress.
- **Scroll progress:** reading bar, section dots, chapter indicator.
- **Header behaviour:** shrink, gain background, hide on scroll down / show on up.
- **Text highlight on scroll:** words light up as they pass the centre.
- **Image sequence / frame scrub** (product turntable from rendered frames).
- **Counters on enter**, **SVG path drawing on scroll**, **scroll-snap** for full-screen chapters (not for reading pages).
- Tech: CSS `animation-timeline: view()/scroll()` first, built per the matching MWG guide (`mwg:scroll-entry-exit-effects`, `mwg:parallax-scroll-effects`, `mwg:scroll-progress-indicator`, `mwg:shrinking-header-on-scroll`); GSAP ScrollTrigger for pinning/scrubbing the platform can't express; IntersectionObserver only for non-animation triggers and guide fallbacks; Lenis only if it keeps native feel. Never scroll-jack.

### 3.3 Hover effects (pointer devices only)
- **Cards:** lift 2–6 px + shadow change, border/tint shift, inner image zoom 1.03–1.06, content reveal (description slides up).
- **Buttons:** background shift, arrow nudge 2–4 px, fill sweep, shine sweep, subtle scale 1.02.
- **Links:** underline grows from left, thickness change, highlight sweep.
- **Images:** zoom, duotone → colour, caption reveal, tilt.
- **Spotlight:** radial light follows the pointer inside cards/borders.
- **3D tilt:** card rotates ≤ 6–8° toward the pointer with a glare layer.
- **Magnetic:** CTAs move ≤ 6–10 px toward the pointer.
- **Nav:** pill/indicator slides to the hovered item.
- Tech: CSS transitions inside `@media (hover:hover) and (pointer:fine)`; small JS for spotlight/tilt/magnetic (rAF + lerp).

### 3.4 Micro-interactions
Button press (scale 0.97), toggle thumb slide with squash, checkbox tick drawing, radio dot pop, input focus label float/underline grow, copy → check morph, like/favourite pop + burst, add-to-cart fly-to-cart, stepper +/– bump, tab indicator slide, accordion chevron rotate + height animation, tooltip fade-scale, dropdown/menu scale from trigger origin, password show/hide eye morph.

### 3.5 Page & view transitions
Cross-fade, slide in navigation direction, shared-element morph (thumbnail → detail), card expands into page, route progress bar. Tech: View Transitions API (same- and cross-document) per `mwg:same-document-transitions`, `mwg:cross-document-transitions`, `mwg:directional-navigation-transitions`; Motion `layoutId` or FLIP only where the platform can't do it.

### 3.6 Text & typography motion
Split-line or word reveal, word swap carousel, typewriter with correction, scramble/decode, variable-font weight/width shift, marquee/ticker band (pausable), highlight sweep, gradient sweep on one word, kinetic headline sequence. Rules: `../creative/hero-typography.md` §6–7.

### 3.7 Data & number animation
Counters (NumberFlow-style tabular digits), chart draw-in, transitions from previous values, progress fills, sparkline draw, map routes drawing, live ticks.

### 3.8 Layout animation
List add/remove/reorder (FLIP / AutoAnimate / Motion layout), filter shuffles, expand/collapse cards, masonry rearrange, shared element between list and panel, drag reorder with springs.

### 3.9 Background & ambient
Gradient/mesh drift (60 s loops), grain/noise, soft light or caustics, aurora, slow-moving shapes, particle field (only with a concept), video loop (muted, pausable). Pause offscreen and on tab hidden; static under reduced motion.

### 3.10 Cursor & pointer
Custom cursor with contextual labels ("View", "Drag"), trails, blend-mode cursor, spotlight reveal, image reveal following the cursor on list hover. Never in forms or tools; never hide the real cursor without a visible replacement.

### 3.11 Illustration & SVG
Line drawing, icon morphs (menu ↔ close, play ↔ pause), logo reveal, animated illustration scenes, Lottie (designer files), Rive (interactive state machines).

### 3.12 Loading & feedback
Skeleton shimmer matched to layout, progress with easing, optimistic insert, success check + burst (peak-end), error shake (±4–6 px) + message, toast stack choreography, empty-state illustration idle loop (paused after one cycle).

### 3.13 3D & depth
Tilt cards, layered parallax, 3D object rotating with scroll or pointer, depth-of-field blur, perspective card stacks. See `3d-and-realtime.md`.

### 3.14 Gestures (touch)
Swipe-to-dismiss, swipe actions on rows, drag with inertia, pull-to-refresh, bottom-sheet snap points, pinch zoom on images. Always with a visible non-gesture alternative.

## 4. Recommended sets by product (for "You choose")

| Product | Recommended categories | Intensity |
|---|---|---|
| Marketing / launch page | Hero entrance, scroll, hover, text, micro, illustration/SVG, background (+ cursor at Polished+) | Balanced → Expressive |
| SaaS / dashboard | Micro, data & numbers, layout, loading & feedback, page/view transitions, hover | Subtle → Balanced |
| E-commerce | Hover (image zoom, card), micro (add-to-cart), layout (filters), page transitions, loading | Balanced |
| Portfolio / agency | Hero entrance, scroll (pinned + scrubbed), text, cursor, page transitions, 3D/depth | Expressive → Cinematic |
| Mobile app | Micro, gestures, layout, view transitions, loading & feedback | Balanced |
| Wellness / calm | Hero entrance, scroll reveals, ambient background, breathing/illustration loops | Subtle → Balanced |
| Kids / playful | Micro (bouncy), hover, illustration, feedback bursts, layout | Expressive |
| Dev tools / docs | Micro, layout, view transitions, data, loading (fast and precise) | Subtle |
| Data story / report | Scroll (scrubbed), data & numbers, text, pinned scenes | Balanced → Cinematic |

## 5. Write the motion plan (before building)
List every motion item in a table (in PLAN.md or `templates/MOTION.md` §3):

| # | Category | Element | Trigger | Effect | Duration / easing | Reduced-motion version | Tech |
|---|---|---|---|---|---|---|---|
| M-01 | Hero entrance | Headline lines | Load | Split reveal, 80 ms stagger | 900 ms, ease-out | Shown instantly | CSS |
| M-02 | Scroll | Feature cards | Enter 15 % | Rise 20 px + fade, 50 ms stagger | 500 ms | Visible | CSS view() |
| M-03 | Hover | Product cards | Pointer hover | Lift 4 px, image zoom 1.04, shadow | 220 ms | n/a (hover) | CSS |

Every chosen category has **at least one** item; Standard+ meets the floor in §2. Treat each M-ID like a requirement: it must be built and checked.

## 6. Build rules (quality, not timidity)
- Durations, easings and distances come from motion tokens (`motion-system-and-verification.md` §2), scaled by the chosen intensity.
- Vary effects by element role; never one identical fade-up for the whole page.
- Content is readable immediately; motion never blocks clicks, never delays prices/CTAs/forms by more than ~300 ms.
- Animate transform, opacity, filter, clip-path; avoid layout properties on large areas.
- Every item has a reduced-motion version (instant, fade only, or slowed for progress indicators), coded per item the `mwg:motion` way: opt in under `prefers-reduced-motion: no-preference`, or soften parameters under `reduce`; never a global `*` reset.
- Hover-only effects live inside `(hover:hover) and (pointer:fine)`; touch gets tap feedback instead.
- Loops pause offscreen and after a few cycles on reading pages; anything auto-moving > 5 s has a pause control.

## 7. Verify motion was delivered
- Tick every M-ID: **built and observed** (screen recording, Playwright video, or stepping through the DevTools Animations panel).
- `scripts/verify_page.py` prints a **motion inventory** (keyframe animations, transition rules, scroll-driven animations, hover rules, motion libraries detected) and checks reduced motion. Compare it against the plan: a Standard+ page whose inventory shows almost nothing is under-delivered.
- Report: "Motion: 14 items planned, 14 built, reduced-motion verified, 60 fps at 4× CPU throttle on the hero."

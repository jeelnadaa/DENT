# The Modern Layer: typography craft, motion, hover, scroll, depth

Moved from SKILL.md §7 in DENT 2.0. This is **interface** motion and finish. For motion graphics, kinetic compositions, 3D and generative visuals read `motion/motion-graphics.md`; for the per-project motion language read `motion/motion-system-and-verification.md`. Section numbers (7.0–7.11) are kept from DENT 1.x.

---

## §7 The modern layer — what makes a design feel modern

A modern design is not a style; it is **craft on top of solid foundations**. Every technique here is a multiplier: on a good structure it makes the product feel premium, on a weak structure it makes the problems louder. Apply this layer last.

### 7.0 Ground rules for the whole modern layer
- **Purpose first [Law: aesthetic-usability effect cuts both ways].** Every effect must do at least one job: show hierarchy, explain a change, give feedback, guide attention, or express the brand. If it does none, remove it.
- **Restraint is the signature of modern design.** One or two "hero" moments per page or screen. Everything else is quiet and fast.
- **Consistency [Law: similarity].** Motion, hover and typography behaviors are tokens too. The same kind of thing always moves and reacts the same way.
- **[Rule] Performance:** effects never block input or drop frames. Animate only `transform` and `opacity` (and `filter` sparingly). Never animate `width`, `height`, `top`, `left`, `margin` or `box-shadow` directly on large or many elements.
- **[Rule] Reduced motion:** every non-essential animation has a reduced-motion version (fade or no motion). See §7.9.
- **Progressive enhancement:** the product works and looks good with effects off. Effects are added on top, never required to read or use content.

---

### 7.1 Custom and expressive typography

Typography is the single biggest driver of a modern look. Most of a screen is text.

**Choosing typefaces**
- Pair a **characterful display face** (headings, hero, numbers) with a **highly readable text face** (body, UI). Or use one well-designed family with wide weight range for both.
- Prefer **variable fonts**: one file, every weight/width, smooth weight animation, better performance than many static files.
- Choose fonts with good **tabular figures** for data, real **italics**, and enough weights (at least 400, 500, 600/700).
- Avoid the default-everywhere choice when the product needs identity; a distinctive font choice is the cheapest way to not look templated.

**Craft details that read as "modern"**
- **Large type, tight tracking:** big headings (40px+) usually need negative letter-spacing (about −1% to −3%); small text (≤ 13px) and all-caps labels need positive tracking (+2% to +8%).
- **Tight heading line-height:** 1.0–1.2 for display sizes; body stays 1.4–1.6.
- **Strong scale contrast:** a big jump between hero/heading and body creates hierarchy at a glance (Von Restorff). Don't use many sizes that are only slightly different.
- **Weight contrast** instead of extra sizes: e.g. 600 heading vs 400 body.
- **Balanced line breaks:** `text-wrap: balance` for headings (no single orphaned word); `text-wrap: pretty` for paragraphs.
- **Tabular numbers** in tables, prices, timers, counters: `font-variant-numeric: tabular-nums` so digits don't jitter.
- **Optical sizing:** use `font-optical-sizing: auto` when the font supports it.
- **Correct typographic characters:** real quotes (" "), apostrophes ('), en/em dashes (– —), ellipsis (…), × for dimensions.

**Fluid type (scales smoothly with screen width)**
```css
/* min size, preferred (viewport-relative), max size */
h1   { font-size: clamp(2.25rem, 1.5rem + 3vw, 4.5rem); }
body { font-size: clamp(1rem, 0.95rem + 0.25vw, 1.125rem); }
```
- **[Rule]** Always include a `rem` part so text still scales with the user's zoom/font settings (WCAG 1.4.4). Never pure `vw`.

**Font loading**
- Use `font-display: swap` (or `optional` for non-critical fonts), preload the 1–2 critical files, subset to needed characters (OFL fonts only; the ITF/Fontshare licence forbids subsetting), and set fallback font metrics (`size-adjust`) so text doesn't jump when the font loads (layout shift).

**Typography as a visual element**
- Oversized headings, outline or mixed-weight words, text masked over images, and kinetic (animated) type can be hero moments. Use for **one** headline per page, never for body content, and keep it readable.

---

### 7.2 Motion system (fluid motion)

Motion that feels "fluid" comes from three things: **the right easing, the right duration, and continuity** (things move from where they were to where they go, rather than appearing/disappearing).

**Why motion helps [Law]:** animated transitions help people track what changed and where things went (object constancy), reducing the cognitive cost of a change. Badly used, motion distracts and slows people down.

**Duration tokens** [Convention]
| Token | Duration | Used for |
|---|---|---|
| instant | 50–100ms | color/opacity on hover, press feedback |
| fast | 150–200ms | small elements: toggles, checkboxes, tooltips, icon swaps |
| normal | 250–300ms | menus, dropdowns, cards expanding, tab indicators |
| slow | 350–500ms | modals, drawers, large panels, page sections |
| page | 400–700ms | full-page / route transitions, hero entrances |

- Bigger distance or bigger element → longer duration. Small UI never takes longer than ~300ms.
- Exits are ~20–30% faster than entrances (people want the old thing gone quickly).
- Frequent actions get the shortest (or no) animation; rare, meaningful moments get more.

**Easing tokens** [Convention]
```css
--ease-out:       cubic-bezier(0.16, 1, 0.3, 1);   /* entering, expanding — fast start, soft landing */
--ease-in:        cubic-bezier(0.7, 0, 0.84, 0);   /* exiting — gentle start, quick finish */
--ease-in-out:    cubic-bezier(0.65, 0, 0.35, 1);  /* moving between two on-screen positions */
--ease-standard:  cubic-bezier(0.2, 0, 0, 1);      /* general UI default */
```
- **Never `linear`** for UI movement (only for spinners, progress, and continuous loops).
- Real objects don't start or stop instantly; easing is what makes motion feel physical.

**Springs** (for drag, gestures, playful/premium feel)
- Springs feel more natural than fixed curves for interactive motion because they keep the user's velocity (a flick continues smoothly).
- Typical: quick, almost no bounce for UI (damping ratio ~0.8–1.0, response ~0.3–0.5s); a small bounce (~0.6–0.75) only for playful, celebratory or physical elements.
- Use springs for: dragging, swiping, sheets, reordering, pull-to-refresh, toggles on mobile. Use curves for: fades, color changes, simple reveals.

**Choreography**
- **Stagger** lists and grids: 20–50ms between items, max ~8–10 items staggered (then show the rest together), total under ~500ms.
- **Order:** container first, then content; the most important element arrives first.
- **Direction is meaning:** forward/deeper = from right or from below; back/up a level = reverse. Keep it consistent across the product.
- **Small distances:** entrances move 8–24px, not across the screen. Combine with opacity (fade + slight move) for the classic modern reveal.
- **Scale subtly:** pop-ins from 0.95–0.98 to 1, not from 0.

**Continuity techniques**
- **Shared-element transitions:** a thumbnail grows into the detail view instead of the screen cutting. On web: View Transitions API (`view-transition-name`); in apps: shared element / matched geometry; libraries: FLIP technique.
- **Layout animation:** when items are added, removed or reordered, the others slide to their new places instead of jumping.
- **Morphing:** a button expanding into a panel, an icon morphing (play ↔ pause, menu ↔ close).
- **Animate numbers:** counters roll to the new value; charts animate from previous to new data, not from zero every time.

---

### 7.3 Micro-interactions

Small responses to user actions; they make a product feel alive and confirm that something happened [Law: visibility of system status].

Structure every micro-interaction as **trigger → rules → feedback → loop/end**.

Good uses:
- **Press feedback:** buttons scale to ~0.97–0.98 on press (fast, 100ms) and return on release.
- **Toggle/checkbox:** check mark draws in, thumb slides with a slight squash.
- **Success moments:** a check mark animation or subtle confetti at the *end* of meaningful flows (Peak-end rule) — not on every save.
- **Copy to clipboard:** icon morphs to a check for ~1.5s.
- **Like/favourite:** quick scale bounce + color fill.
- **Inline validation:** a gentle shake (±4–6px, 2–3 cycles, ~300ms) on wrong input, plus the text message **[Rule: not motion alone]**.
- **Optimistic UI:** show the result instantly (item appears, like count increments) and reconcile with the server after; roll back with a message if it fails. Feels faster than any spinner (Doherty threshold).

---

### 7.4 Hover animations (pointer devices)

**[Rule]** Hover is an enhancement, never the only way to see information or reach an action (touch devices have no hover). Wrap hover effects so they only apply to real pointers:
```css
@media (hover: hover) and (pointer: fine) {
  .card:hover { transform: translateY(-2px); }
}
```

**Good hover effects** (pick a small set and use them consistently):
| Element | Effect | Timing |
|---|---|---|
| Buttons | background shift (~8%), optional tiny lift or icon nudge (→ moves 2–4px) | 100–150ms |
| Cards (clickable) | lift 2–4px + slightly stronger shadow, or border/tint change; image inside zooms to ~1.03–1.05 with overflow hidden | 200–300ms |
| Links | underline grows/slides in, or thickness change | 150–200ms |
| Icons/icon buttons | tinted circular background appears | 100–150ms |
| Images/media | subtle zoom, overlay with title/action fades in (action must also be reachable without hover) | 250–400ms |
| Nav items | indicator/pill slides to hovered item | 200–250ms |

**Expressive hover (use sparingly, hero areas only):**
- **Spotlight/glow:** a soft radial highlight follows the cursor inside a card or border.
- **Magnetic buttons:** button moves a few px toward the cursor (max ~6–10px).
- **Tilt/3D:** card rotates a few degrees toward the cursor (max ~5–8°).
- **Custom cursor:** only on creative/portfolio sites; never hide the system cursor in apps or forms, and keep it fast (no lag).

Rules:
- Hover-in can be a bit slower than hover-out; hover-out should feel instant (~100ms).
- Don't move the element away from the cursor or change its size enough to cause flicker at the edges.
- Add a short delay (~100–200ms) before hover opens menus/previews, so passing over things doesn't trigger them.

---

### 7.5 Scroll animations

Scroll is the main interaction on websites and long app screens. Used well, it tells a story; used badly, it fights the user.

**[Rule] Never scroll-jack:** don't override scroll speed, direction or distance, or force snapping through content the user wants to skim. The user controls the scroll.

**Good scroll techniques**
- **Reveal on enter:** sections/items fade in and rise 16–24px when they enter the viewport. Trigger once, early (when ~10–20% visible), duration 400–600ms, stagger children. Content must be readable even if the animation never runs.
- **Scroll-linked progress:** reading progress bar, header that shrinks/condenses or gains a background after scrolling, step indicators.
- **Sticky storytelling:** a pinned visual on one side changes as text sections scroll past (product tours, features). Keep each step short.
- **Subtle parallax:** background layers move at a slightly different speed (10–30% difference). Large parallax causes motion sickness — keep it subtle and disable under reduced motion.
- **Horizontal scroll sections:** only for galleries/carousels the user expects to swipe; always show that more content exists (peek the next item).
- **Scroll snap:** for carousels, onboarding pages, full-screen media — not for regular reading pages.
- **Hide/reveal header:** header hides on scroll down and returns on scroll up (more space for content, always reachable).
- **Back-to-top** button appears after ~2 screens of scroll on long pages.

**Implementation**
- Prefer **CSS scroll-driven animations** (`animation-timeline: view()` / `scroll()`) or **IntersectionObserver** over scroll event listeners (better performance).
```css
@media (prefers-reduced-motion: no-preference) {
  .reveal {
    animation: reveal linear both;
    animation-timeline: view();
    animation-range: entry 10% cover 30%;
  }
}
@keyframes reveal { from { opacity: 0; translate: 0 24px; } to { opacity: 1; translate: 0 0; } }
```
- Don't animate everything that enters: headings and key visuals yes; every paragraph and every icon no.
- Never delay important content (prices, CTAs, form fields) behind long animations.

---

### 7.6 Depth, surface and texture

Modern designs use **soft, layered depth** instead of hard lines.

- **Layered shadows:** combine 2–3 shadows (a tight one for contact + a large soft one for ambient) at low opacity for realistic elevation. Shadows tinted with the background hue look better than pure black.
- **Subtle borders on dark mode:** shadows are hard to see on dark backgrounds; use a 1px light border at low opacity (~6–12%) and lighter surfaces for elevation.
- **Inner highlights:** a 1px top inner light line on raised elements (buttons, cards) adds a premium "lit from above" feel.
- **Background blur (glass):** `backdrop-filter: blur()` for nav bars, sheets and overlays above content. **[Rule]** Text on glass must still meet contrast — add a semi-opaque tint behind it. Use on a few surfaces, not everywhere (expensive to render).
- **Gradients:** soft, low-contrast gradients (mesh or radial) for hero backgrounds and accents; gradient text only on short display headings. Use smooth color spaces (`in oklch`) to avoid muddy middles.
- **Grain/noise:** a very subtle noise overlay (2–5% opacity) removes the flat "digital" look and hides gradient banding.
- **Radius hierarchy:** nested radii are concentric (inner = outer − padding), containers rounder than controls (see `foundations-and-components.md` §4.1).

---

### 7.7 Layout patterns that read as modern

- **Generous whitespace** and a clear max width; let content breathe [Law: proximity].
- **Bento grids:** content in a grid of differently sized rounded tiles; size reflects importance. Keep consistent gaps and radii.
- **Big, confident hero:** one clear headline, one supporting line, one primary CTA, one strong visual. Not five messages.
- **Asymmetry with a grid underneath:** offset layouts look dynamic but still snap to the column grid.
- **Edge-to-edge media** mixed with contained text columns.
- **Fluid, intrinsic layouts:** `clamp()` for spacing, CSS grid with `auto-fit/minmax`, **container queries** so components adapt to their container, not just the screen.
- **Sticky, context-aware UI:** sticky headers, sticky action bars on mobile (primary action always reachable — Fitts's Law), sticky table headers.

---

### 7.8 Modern interaction patterns

- **Command palette (⌘K / Ctrl+K):** search-everything + actions for power users (heuristic 7: flexibility and efficiency).
- **Keyboard shortcuts** for frequent actions, discoverable in tooltips and menus.
- **Instant search / filter-as-you-type** with debounced queries (~150–300ms).
- **Inline editing** instead of separate edit pages where possible.
- **Undo instead of "Are you sure?"** for reversible actions (heuristic 3: user control and freedom).
- **Skeleton loading + optimistic UI** instead of full-page spinners.
- **Smart defaults and autofill** (Tesler's Law: take the complexity onto the system).
- **Gestures on mobile:** swipe actions on rows, pull to refresh, swipe-to-dismiss sheets — always with a visible alternative.
- **Dark mode + system theme** support, switching smoothly (no flash of the wrong theme on load).

---

### 7.9 Reduced motion and accessibility for the modern layer [Rule]

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```
- Under reduced motion: replace movement with simple fades or instant changes; remove parallax, auto-playing motion, zoom and large slides. Keep essential feedback (state changes) visible.
- **[Rule]** Anything that moves automatically for more than 5 seconds (carousels, background video, looping animations) needs a pause/stop control (WCAG 2.2.2).
- **[Rule]** No flashing more than 3 times per second (WCAG 2.3.1).
- Motion never carries meaning alone — pair with text/icon change.
- Focus states stay visible during and after animations; animations must not move focused elements off-screen.

---

### 7.10 Performance budget for the modern layer

- Target **60fps** (16ms per frame); interactions respond within ~100ms (and INP < 200ms on web).
- Animate `transform` and `opacity` only; use `will-change` only on elements about to animate, then remove it.
- Limit simultaneous animations; pause off-screen animations and videos.
- Avoid layout shift (CLS): reserve space for images, fonts and late content.
- Heavy effects (WebGL, 3D, large videos, many blurs) only where they are the point of the page, lazy-loaded, with a static fallback.
- Test on a mid-range phone, not only a fast laptop.

---

### 7.11 Anti-patterns (things that look "modern" but hurt)

- Everything fades/slides in on scroll — the page feels slow and the user waits for content.
- Long or bouncy animations on frequent actions (opening a menu 50 times a day).
- Scroll-jacking, forced smooth-scroll overrides, or sections that trap the scroll.
- Hover-only actions or information.
- Low-contrast "aesthetic" grey text, or text on busy glass/gradients.
- Too many fonts, sizes or effects competing; multiple "hero" moments on one screen.
- Custom cursors or loading screens that delay usage.
- Motion that ignores reduced-motion settings.
- Effects that drop frames on normal phones.

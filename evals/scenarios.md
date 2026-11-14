# DENT Scenario Suite

Realistic projects for comparing conditions A/B/C (`protocol.md`). Each scenario has: the prompt, **scripted answers** to the questions DENT is expected to ask (answer any other question briefly and record it), must-haves, hard failures, and what to measure. Scenarios marked ★ are the showcase pieces for the README.

---

### S1. SaaS analytics dashboard from scratch
**Prompt:** `/dent Build a responsive analytics dashboard for a small online store owner: revenue, orders, top products, traffic sources, and a recent orders table. React + Tailwind.`
**Scripted answers:** effort → Standard · style → you choose · light/dark → both · density → comfortable.
**Must:** hero KPI row with hierarchy (not 8 equal cards), chart per question, orders table with sort/filter/empty/loading states, realistic varied data, dark/light, no overflow at 320–1440, keyboard path.
**Hard fail:** invented "AI insights" claims; overflow; unlabeled filters.
**Measure:** gates, independent /50, requirement coverage.

### S2. Complex data-heavy application
**Prompt:** `/dent Admin tool to manage 50,000 support tickets: list with filters, bulk assign, ticket detail side panel, keyboard shortcuts. Vue 3.`
**Scripted answers:** effort → Polished · library preference → whatever fits Vue.
**Must:** component selection for Vue (TanStack Table Vue / PrimeVue / AG Grid with licence notes), virtualisation, bulk actions bar, side-panel editing, shortcuts + cheat sheet, states.
**Measure:** library rationale quality, performance with 50k rows (scroll fps), a11y.

### S3. Responsive marketing website
**Prompt:** the Brewlog prompt (`benchmark/PROMPT.md`).
**Must:** landing-page recipe gates L1–L11. **Hard fail:** invented stats/testimonials, overflow.

### S4. Multi-step onboarding / checkout with failure recovery
**Prompt:** `/dent Multi-step checkout for a furniture store: cart review, shipping address, delivery slot, payment, confirmation. Handle validation errors and a declined payment.`
**Scripted answers:** effort → Standard · platform → web, mobile-first.
**Must:** stepper, saved progress, back keeps input, inline validation timing, declined-payment recovery path, order summary always visible, guest checkout, transparent total.
**Hard fail:** dark patterns (pre-checked insurance, hidden fees).

### S5. Feature in a product with an existing design system
**Setup:** a Next.js project with shadcn/ui `components.json` and custom tokens (fixture repo of your choice).
**Prompt:** `/dent Add a team members settings page (invite, roles, remove).`
**Must:** detects and reuses existing components/tokens; role comparison; invite flow; destructive confirmation; no new color palette/component duplicates.
**Hard fail:** second design system; hard-coded hex values.

### S6. Unfamiliar framework
**Prompt:** `/dent Build a settings screen with toggles, a theme picker and a danger zone in SolidJS.`
**Must:** framework-appropriate primitives (Kobalte/Ark) or careful native semantics; honest about any uncertainty; tokens; states.

### S7. Highly interactive app (drawers, command palette, tables, charts, animation)
**Prompt:** `/dent A project management app screen: kanban board with drag and drop, a command palette (Cmd+K), a slide-over task drawer, a burndown chart, smooth animations. React.`
**Must:** dnd-kit (keyboard DnD), cmdk, drawer with focus management, chart with table alternative, Motion layout animations, reduced motion, one library per job.

### S8. Strict accessibility and performance constraints
**Prompt:** `/dent Government benefits application form. Must meet WCAG 2.2 AA, work on a 3G phone, and support screen readers.`
**Must:** plain language, error summary, field-level errors announced, no unnecessary JS, measured performance (Lighthouse), every criterion checked listed honestly.

### S9. Marketing site with motion graphics and scroll storytelling
**Prompt:** `/dent go all out: a launch page for "Tidal", an app that helps freelancers smooth irregular income, with a scroll story that shows money flowing from spiky to steady.`
**Scripted answers:** effort → All-out · sound → no · directions → pick the one you recommend.
**Must:** All-out sweep 2.1 + 2.6; storyboard; data-shaped motion (spiky → steady); reduced-motion version; fps measured; no scroll-jacking.

### S10. Interactive 3D product showcase
**Prompt:** `/dent A product page for a modular desk lamp with an interactive 3D viewer (rotate, change finish), with a fallback for low-end phones.`
**Must:** 3D justified; glTF pipeline + budgets; poster fallback; reduced motion = no auto-rotate; finish switcher accessible; fps measured.

### S11. Animated data visualisation with complex timelines
**Prompt:** `/dent An animated "year in review" data story for a cycling app: distance by month, elevation records, and a map of rides, with a play/pause timeline.`
**Must:** animations from previous state, annotations, play/pause/scrub control, table alternative, reduced motion, honest axes.

### S12. Audiovisual product experience
**Prompt:** `/dent A meditation timer web app with a breathing animation, optional ambient soundscapes and a gentle sonic identity.`
**Scripted answers:** effort → Polished · sound → yes, opt-in.
**Must:** SOUND.md, opt-in audio, mute/volume, no autoplay (verify_page G11), animation synced to breath timing on the audio clock, visual-only mode complete.

### S13. Redesign without breaking functionality
**Setup:** any small existing app.
**Prompt:** `/dent Redesign this app to feel modern. Keep everything working.`
**Must:** baseline screenshots, inventory, "must not break" list, migration plan, regression classification.

### S14. Fix a bug while protecting other routes
**Prompt:** `/dent The header menu overlaps the logo on iPhone SE and the page scrolls sideways.`
**Must:** root cause, smallest fix, overflow check at 320–1440 on every route sharing the header.

### S15. AI application with streaming and tool states
**Prompt:** `/dent Chat UI for a research assistant: streaming answers, citations, tool-use steps, stop/retry, and errors.`
**Must:** visible states, stop button, citations, retry/edit, error recovery, uncertainty language.

### S16. Launch video
**Prompt:** `/dent launch-video for a note-taking app called Quill, 45 seconds, for X and LinkedIn.`
**Scripted answers:** generative access → No · narration → no, music + captions · sub-type → reveal.
**Must:** VIDEO.md brief + script + storyboard; hook in 2 s; real-looking UI recreated in HTML (no invented features); 16:9 + 1:1 cuts; captions; licensed music; ffprobe + loudness QA.

### S17. Explainer video with narration
**Prompt:** `/dent video: a 60-second explainer of how end-to-end encryption works, with a calm narrator.`
**Scripted answers:** voice → free TTS engine · style → kinetic type + simple diagrams.
**Must:** script ≈ 150 words, pronunciation notes, TTS licence noted, captions synced, analogy visuals, loudness −14 LUFS.

### S18. Sonic identity
**Prompt:** `/dent sound: create a sonic identity for a banking app: logo sound, confirm, error, notification.`
**Must:** direction, palette, sonic logo + variations, loudness, licences (synthesised or licensed), opt-in behaviour.

---

## Showcase pieces (★ built with DENT 2.0 and published on the README)

### ★ S19. DENT's landing page
**Prompt:** `benchmark/PROMPT-DENT-LANDING.md` (content-only prompt, questions allowed).
**Record:** every question and answer. **Must:** landing-page recipe gates; All-out sweep 2.1; no invented proof.

### ★ S20. DENT motion-graphics piece
**Prompt:** `/dent motion-graphics: a 15–20 second kinetic-typography piece that introduces DENT ("Make a dent with your product's design"), showing a generic AI template being rebuilt into a distinctive design. Deliver an MP4 and a GIF/animated SVG for the README.`
**Must:** concept, storyboard, timing sheet, technology rationale, reduced-motion/poster, exports, verification.

### ★ S21. DENT explainer video with narration
**Prompt:** `/dent video: a 60–75 second explainer of what DENT is and how it works (orchestration, planning, directions, verification, scoring), with narration, music and captions. 16:9 for the README and 9:16 for social.`
**Must:** VIDEO.md, script approved, narration (licence recorded), captions, two cuts, QA table.

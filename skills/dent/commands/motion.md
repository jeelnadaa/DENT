# /dent:motion

Add rich, purposeful motion: ask which kinds (scroll, hover, hero entrance, micro-interactions, transitions, text, data, layout, ambient, cursor, SVG, 3D, gestures) and how strong, then build and verify every item.

**Usage:** `/dent:motion <area or page>` (also `/dent motion …` or `dent motion …`)
**Default depth:** Standard. Effort level and the gates in SKILL.md §3 always apply.

## Load
- `references/motion/motion-menu.md (the menu, intensities, minimums, recommended sets)`
- `references/modern-layer.md`
- `references/motion/motion-system-and-verification.md`
- `references/motion/motion-tech-catalog.md`
- `templates/MOTION.md`

## Steps
1. Ask which kinds of motion the user wants, following motion-menu.md §1: first 'You choose (Recommended) / Let me pick the kinds / Keep it minimal'; if they pick, ask the grouped MULTI-SELECT questions (Page & scroll, Interaction, Content, Visual depth; 4 kinds each). Skip only if the user already listed the kinds.
2. Ask Question B: intensity (Subtle / Balanced (Recommended) / Expressive / Cinematic).
3. Pick concrete items for every chosen kind from the catalogue (§3) and meet the minimum for the effort level (§2). If the user chose 'You choose', show the list and let them remove items.
4. Write the motion plan table with an M-ID per item (§5): element, trigger, effect, duration/easing scaled to the intensity, reduced-motion version, tech.
5. Build every M-ID with motion tokens and the right engine (CSS first, GSAP/Motion only where needed). Vary effects by element role; never one fade-up for everything.
6. Verify: observe every M-ID working (recording or Animations panel), run verify_page.py (motion inventory + reduced motion), check smoothness; report planned vs built.

## Output
Motion plan (M-IDs) + implementation + verification (planned vs built, reduced motion, smoothness).

## Never
- Deliver only a fade-in and call it motion.
- Skip the motion question.
- Ignore reduced motion or hover-only on touch.

Close with the scorecard summary, attribution (DENT / user / agent judgment / overrides) and a one-line next step (SKILL.md §8).

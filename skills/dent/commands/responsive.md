# /dent:responsive

Make layout and interaction work at every size, designed rather than shrunk.

**Usage:** `/dent:responsive <page or screens>` (also `/dent responsive …` or `dent responsive …`)
**Default depth:** Standard. Effort level and the gates in SKILL.md §3 always apply.
**Web code:** if this command writes, changes or reviews HTML, CSS or client-side JS, Google's Modern Web Guidance is the primary authority for how it is built: run `references/modern-web-guidance.md` §2 (search → retrieve → apply → verify → disclose) before coding; MWG wins any implementation conflict with DENT.

## Load
- `references/platforms-and-devices.md §3`
- `references/workflow/verification.md §4`
- `references/foundations-and-components.md §3 (grid)`
- `references/modern-web-guidance.md (mwg:responsive-design, mwg:size-aware-styling, mwg:fluid-scaling)`

## Steps
1. Screenshot at 320, 375, 390, 768, 1024, 1440 and any breakpoint in between.
2. Fix overflow first (header actions, wide tables, fixed widths, long words, 100vw elements) the MWG way: container queries for components, dvh for full-height, fluid type with max ≤ 2.5× min.
3. Re-compose for small screens: simplify mockups, stack with intent, sticky primary action, readable type.
4. Check touch targets, hover-only actions, safe areas, landscape.

## Output
Fixed layout + screenshots per width + overflow report.

## Never
- Just scale the desktop layout down.

Close with the scorecard summary, attribution (DENT / MWG / user / agent judgment / overrides), the `### Modern Web Guidance` disclosure if guides shaped the code, and a one-line next step (SKILL.md §8).

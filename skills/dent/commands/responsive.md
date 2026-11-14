# /dent:responsive

Make layout and interaction work at every size, designed rather than shrunk.

**Usage:** `/dent:responsive <page or screens>` (also `/dent responsive …` or `dent responsive …`)
**Default depth:** Standard. Effort level and the gates in SKILL.md §3 always apply.

## Load
- `references/platforms-and-devices.md §3`
- `references/workflow/verification.md §4`
- `references/foundations-and-components.md §3 (grid)`

## Steps
1. Screenshot at 320, 375, 390, 768, 1024, 1440 and any breakpoint in between.
2. Fix overflow first (header actions, wide tables, fixed widths, long words, 100vw elements).
3. Re-compose for small screens: simplify mockups, stack with intent, sticky primary action, readable type.
4. Check touch targets, hover-only actions, safe areas, landscape.

## Output
Fixed layout + screenshots per width + overflow report.

## Never
- Just scale the desktop layout down.

Close with the scorecard summary, attribution (DENT / user / agent judgment / overrides) and a one-line next step (SKILL.md §8).

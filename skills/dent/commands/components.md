# /dent:components

Choose, install and customise the right component/UI libraries for this project.

**Usage:** `/dent:components <need, e.g. data table + command palette>` (also `/dent components …` or `dent components …`)
**Default depth:** Standard. Effort level and the gates in SKILL.md §3 always apply.
**Web code:** if this command writes, changes or reviews HTML, CSS or client-side JS, Google's Modern Web Guidance is the primary authority for how it is built: run `references/modern-web-guidance.md` §2 (search → retrieve → apply → verify → disclose) before coding; MWG wins any implementation conflict with DENT.

## Load
- `references/catalog/component-selection.md`
- `references/catalog/components-primitives-and-systems.md`
- `references/catalog/components-collections-and-specialized.md`

## Steps
1. Detect framework, language, styling, existing libraries and browser-support policy.
2. List functional needs and the visual direction. For each need, search Modern Web Guidance first: if the platform covers it natively (dialog, popover, menu, tooltip, accordion, switch, select, tabs, drawer, toast, carousel), recommend the native build instead of a library (references/modern-web-guidance.md §5).
3. Shortlist 2–3 options per need from the catalogue; compare compatibility, accessibility, customisation, performance, licence, maintenance, design fit.
4. Recommend one per job with trade-offs; run the dependency checklist (component-selection.md §4b) and check the licence from the official source.
5. Install, theme to DESIGN.md tokens, and verify keyboard/a11y behaviour.

## Output
Comparison table, recommendation with reasons, install + integration, verification.

## Never
- Pick by popularity.
- Install two libraries that do the same job.
- Add a dependency for something the web platform does natively.

Close with the scorecard summary, attribution (DENT / MWG / user / agent judgment / overrides), the `### Modern Web Guidance` disclosure if guides shaped the code, and a one-line next step (SKILL.md §8).

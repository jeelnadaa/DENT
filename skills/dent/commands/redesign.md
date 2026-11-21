# /dent:redesign

Redesign an existing product while preserving the behaviour users rely on.

**Usage:** `/dent:redesign <product or screens>` (also `/dent redesign …` or `dent redesign …`)
**Default depth:** Advanced. Effort level and the gates in SKILL.md §3 always apply.
**Web code:** if this command writes, changes or reviews HTML, CSS or client-side JS, Google's Modern Web Guidance is the primary authority for how it is built: run `references/modern-web-guidance.md` §2 (search → retrieve → apply → verify → disclose) before coding; MWG wins any implementation conflict with DENT.

## Load
- `references/modes-existing-products.md` §3
- `references/workflow/execution-and-scope.md`
- `references/workflow/planning-and-plan-audit.md`
- `references/workflow/verification.md` §8

## Steps
1. Inventory screens, flows, components and drift; screenshot the current version as a baseline.
2. List what must stay (navigation, terminology, key positions, features) and ask what is sacred.
3. Plan the redesign + migration (incremental by default) and audit it.
4. Build in phases; never drop a feature because it wasn't in the screenshot you were given.
5. Bring every redesigned screen to the floor for the effort level: built-in surfaces (commands/surfaces.md) and motion (commands/motion.md), unless the user scoped them out.
6. Compare before/after per screen; classify every difference; run the three independent evaluators at Polished+.

## Output
Before/after comparison with reasons, migration plan, updated DESIGN.md, regression results.

## Never
- Remove existing features silently.
- Introduce a second design system.

Close with the scorecard summary, attribution (DENT / MWG / user / agent judgment / overrides), the `### Modern Web Guidance` disclosure if guides shaped the code, and a one-line next step (SKILL.md §8).

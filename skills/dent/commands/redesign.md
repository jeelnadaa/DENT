# /dent:redesign

Redesign an existing product while preserving the behaviour users rely on.

**Usage:** `/dent:redesign <product or screens>` (also `/dent redesign …` or `dent redesign …`)
**Default depth:** Advanced. Effort level and the gates in SKILL.md §3 always apply.

## Load
- `references/modes-existing-products.md §3`
- `references/workflow/execution-and-scope.md`
- `references/workflow/planning-and-plan-audit.md`
- `references/workflow/verification.md §8`

## Steps
1. Inventory screens, flows, components and drift; screenshot the current version as a baseline.
2. List what must stay (navigation, terminology, key positions, features) and ask what is sacred.
3. Plan the redesign + migration (incremental by default) and audit it.
4. Build in phases; never drop a feature because it wasn't in the screenshot you were given.
5. Compare before/after per screen; classify every difference.

## Output
Before/after comparison with reasons, migration plan, updated DESIGN.md, regression results.

## Never
- Remove existing features silently.
- Introduce a second design system.

Close with the scorecard summary, attribution (DENT / user / agent judgment / overrides) and a one-line next step (SKILL.md §8).

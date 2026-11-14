# /dent:extend

Add a feature or screen that fits the existing product and design system.

**Usage:** `/dent:extend <feature>` (also `/dent extend …` or `dent extend …`)
**Default depth:** Standard. Effort level and the gates in SKILL.md §3 always apply.

## Load
- `DESIGN.md (project)`
- `references/workflow/execution-and-scope.md §1–2`
- `references/modes-existing-products.md §2`

## Steps
1. Read DESIGN.md and inspect existing components/tokens.
2. Find the integration points and the screens that share components.
3. Build the feature with existing tokens/components; add new ones only in the existing convention.
4. Verify the new feature and the neighbouring screens; update DESIGN.md changelog.

## Output
The feature, verification results, DESIGN.md changelog line.

## Never
- Redesign unrelated parts.
- Add a new library for something an existing one already does.

Close with the scorecard summary, attribution (DENT / user / agent judgment / overrides) and a one-line next step (SKILL.md §8).

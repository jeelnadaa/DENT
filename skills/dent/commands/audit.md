# /dent:audit

Audit an existing interface, codebase or screenshot and report findings. Change nothing.

**Usage:** `/dent:audit <URL, screenshot or path>` (also `/dent audit …` or `dent audit …`)
**Default depth:** Standard. Effort level and the gates in SKILL.md §3 always apply.

## Load
- `references/modes-existing-products.md §4`
- `templates/AUDIT.md`
- `references/quality-review.md`
- `references/accessibility.md`

## Steps
1. Establish scope, goal and main user task.
2. Look first: render/screenshot, run verify_page.py and drift measures when possible.
3. Evaluate: task success, heuristics, [Rule] failures, hierarchy, consistency, content, deceptive patterns, distinctiveness.
4. Write findings with evidence, severity, impact, recommendation and effort; separate verified defects from opinions.

## Output
templates/AUDIT.md filled in; offer to fix the top items in one line.

## Never
- Silently redesign or fix things.
- Give vague feedback without evidence.

Close with the scorecard summary, attribution (DENT / user / agent judgment / overrides) and a one-line next step (SKILL.md §8).

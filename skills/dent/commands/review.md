# /dent:review

Deep review of a result: visual quality, UX, accessibility, responsiveness, function, consistency, performance.

**Usage:** `/dent:review <what to review>` (also `/dent review …` or `dent review …`)
**Default depth:** Standard. Effort level and the gates in SKILL.md §3 always apply.

## Load
- `references/workflow/verification.md`
- `references/quality-review.md`
- `templates/REVIEW.md`
- `references/creative/anti-slop.md`

## Steps
1. Run the automated pass and look at every screenshot.
2. Walk the main user journey; trigger states; tab through.
3. Check gates G1–G12 that apply.
4. Prioritise issues by severity; mark each as verified defect or subjective recommendation.

## Output
templates/REVIEW.md + prioritised issue list.

## Never
- Report checks you didn't run as passed.

Close with the scorecard summary, attribution (DENT / user / agent judgment / overrides) and a one-line next step (SKILL.md §8).

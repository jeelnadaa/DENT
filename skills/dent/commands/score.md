# /dent:score

Score the work against the request with evidence; list the top 3 improvements if below target.

**Usage:** `/dent:score <optional target, e.g. 9>` (also `/dent score …` or `dent score …`)
**Default depth:** —. Effort level and the gates in SKILL.md §3 always apply.

## Load
- `references/workflow/scoring-and-closeout.md`
- `templates/SCORECARD.md`

## Steps
1. Rebuild the requirement list from the original request.
2. Add the quality lines relevant to this deliverable.
3. Score 0–10 with evidence; apply the caps (unverified ≤ 6, failed gate ≤ 4, missing Must → overall ≤ 6).
4. If below target, list the 3 highest-impact improvements and offer /dent:improve. Include the attribution summary.

## Output
Filled SCORECARD.md.

## Never
- Give 9–10 without evidence.

Close with the scorecard summary, attribution (DENT / user / agent judgment / overrides) and a one-line next step (SKILL.md §8).

# /dent:score

Score the work against the request with evidence; list the top 3 improvements if below target.

**Usage:** `/dent:score <optional target, e.g. 9>` (also `/dent score …` or `dent score …`)
**Default depth:** —. Effort level and the gates in SKILL.md §3 always apply.
**Web code:** if this command writes, changes or reviews HTML, CSS or client-side JS, Google's Modern Web Guidance is the primary authority for how it is built: run `references/modern-web-guidance.md` §2 (search → retrieve → apply → verify → disclose) before coding; MWG wins any implementation conflict with DENT.

## Load
- `references/workflow/scoring-and-closeout.md`
- `templates/SCORECARD.md`

## Steps
1. Rebuild the requirement list from the original request.
2. Add the quality lines relevant to this deliverable.
3. Score 0–10 with evidence; apply the caps (unverified ≤ 6, failed gate ≤ 4, missing Must or open Blocker → overall ≤ 6). List open Blockers above the overall score.
4. At Polished+ use the independent evaluators' reports (scoring-and-closeout.md §3b); where an evaluator differs by 2+ points, use theirs unless you have new evidence.
5. If below target, list the 3 highest-impact improvements and offer /dent:improve. Include the attribution summary.

## Output
Filled SCORECARD.md.

## Never
- Give 9–10 without evidence.

Close with the scorecard summary, attribution (DENT / MWG / user / agent judgment / overrides), the `### Modern Web Guidance` disclosure if guides shaped the code, and a one-line next step (SKILL.md §8).

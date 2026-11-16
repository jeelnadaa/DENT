# /dent:improve

Apply the highest-impact improvements from the last scorecard and re-score.

**Usage:** `/dent:improve <optional focus>` (also `/dent improve …` or `dent improve …`)
**Default depth:** Standard. Effort level and the gates in SKILL.md §3 always apply.
**Web code:** if this command writes, changes or reviews HTML, CSS or client-side JS, Google's Modern Web Guidance is the primary authority for how it is built: run `references/modern-web-guidance.md` §2 (search → retrieve → apply → verify → disclose) before coding; MWG wins any implementation conflict with DENT.

## Load
- `references/workflow/scoring-and-closeout.md §3`
- the previous SCORECARD.md

## Steps
1. Take the top 3 improvements (or the user's focus).
2. Apply them in order; re-run the affected gates.
3. Re-score only with new evidence; show before → after per line.
4. Stop at target, or when the remaining gap needs the user (real content, assets, budget).

## Output
Changes + updated scorecard with deltas.

## Never
- Loop endlessly; after two rounds without progress, propose a direction change.

Close with the scorecard summary, attribution (DENT / MWG / user / agent judgment / overrides), the `### Modern Web Guidance` disclosure if guides shaped the code, and a one-line next step (SKILL.md §8).

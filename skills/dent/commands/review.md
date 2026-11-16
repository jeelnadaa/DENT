# /dent:review

Deep review of a result: visual quality, UX, accessibility, responsiveness, function, consistency, performance.

**Usage:** `/dent:review <what to review>` (also `/dent review …` or `dent review …`)
**Default depth:** Standard. Effort level and the gates in SKILL.md §3 always apply.
**Web code:** if this command writes, changes or reviews HTML, CSS or client-side JS, Google's Modern Web Guidance is the primary authority for how it is built: run `references/modern-web-guidance.md` §2 (search → retrieve → apply → verify → disclose) before coding; MWG wins any implementation conflict with DENT.

## Load
- `references/workflow/verification.md`
- `references/quality-review.md`
- `templates/REVIEW.md`
- `references/creative/anti-slop.md`

## Steps
1. Run the automated pass and look at every screenshot.
2. Walk the main user journey; trigger states; tab through.
3. Check gates G1–G13 that apply (G13: the web code against the Modern Web Guidance guides for what it builds).
4. Prioritise issues by severity; mark each as verified defect or subjective recommendation.

## Output
templates/REVIEW.md + prioritised issue list.

## Never
- Report checks you didn't run as passed.

Close with the scorecard summary, attribution (DENT / MWG / user / agent judgment / overrides), the `### Modern Web Guidance` disclosure if guides shaped the code, and a one-line next step (SKILL.md §8).

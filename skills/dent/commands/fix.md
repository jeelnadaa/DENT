# /dent:fix

Diagnose and fix one specific UI/UX problem with the smallest correct change.

**Usage:** `/dent:fix <the problem>` (also `/dent fix …` or `dent fix …`)
**Default depth:** Quick (Critical if risky area). Effort level and the gates in SKILL.md §3 always apply.
**Web code:** if this command writes, changes or reviews HTML, CSS or client-side JS, Google's Modern Web Guidance is the primary authority for how it is built: run `references/modern-web-guidance.md` §2 (search → retrieve → apply → verify → disclose) before coding; MWG wins any implementation conflict with DENT.

## Load
- `references/workflow/verification.md`
- `references/foundations-and-components.md` (if a component is involved)

## Steps
1. Reproduce or precisely understand the problem (screenshot, steps, viewport).
2. Find the root cause, not the symptom.
3. Make the smallest correct fix using existing tokens/components.
4. Verify the fix and nearby regressions (other screens using the same component).

## Output
Cause, fix, before/after evidence, what else was checked.

## Never
- Refactor unrelated code while you're there.

Close with the scorecard summary, attribution (DENT / MWG / user / agent judgment / overrides), the `### Modern Web Guidance` disclosure if guides shaped the code, and a one-line next step (SKILL.md §8).

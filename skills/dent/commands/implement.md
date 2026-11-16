# /dent:implement

Implement an approved PLAN.md or DESIGN.md accurately.

**Usage:** `/dent:implement <path to PLAN.md or DESIGN.md>` (also `/dent implement …` or `dent implement …`)
**Default depth:** As in the plan. Effort level and the gates in SKILL.md §3 always apply.
**Web code:** if this command writes, changes or reviews HTML, CSS or client-side JS, Google's Modern Web Guidance is the primary authority for how it is built: run `references/modern-web-guidance.md` §2 (search → retrieve → apply → verify → disclose) before coding; MWG wins any implementation conflict with DENT.

## Load
- the plan/spec itself
- `references/design-tokens-and-code.md Part 2`
- `references/workflow/execution-and-scope.md`
- `references/workflow/verification.md`

## Steps
1. Read the plan/spec fully. Check the repository still matches its assumptions; list stale ones.
2. If anything material changed, update the plan and re-audit before building.
3. Implement phase by phase; tokens first; update the traceability matrix as you go.
4. Verify every requirement against its acceptance criterion; record deviations.

## Output
Implementation + traceability matrix with statuses + verification report.

## Never
- Mark a requirement Verified because the code exists.

Close with the scorecard summary, attribution (DENT / MWG / user / agent judgment / overrides), the `### Modern Web Guidance` disclosure if guides shaped the code, and a one-line next step (SKILL.md §8).

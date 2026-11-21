# /dent

The main entry point: understand any design, front-end or media request, pick the right sub-commands, chain them and deliver the best result.

**Usage:** `/dent <anything you want designed, built, fixed, reviewed or produced>`
**Default depth:** decided by the router. Effort level and the gates in SKILL.md §3 always apply.
**Web code:** if this command writes, changes or reviews HTML, CSS or client-side JS, Google's Modern Web Guidance is the primary authority for how it is built: run `references/modern-web-guidance.md` §2 (search → retrieve → apply → verify → disclose) before coding; MWG wins any implementation conflict with DENT.

## Load
- `references/workflow/orchestration.md` (the router: follow it step by step)
- SKILL.md §1.0 and §3 (already loaded)

## Steps
1. Fill the signal card from orchestration.md Step 1 (deliverable, state, verb, media, effort, risk, constraints).
2. Map the signals to a main command + companions with the table in Step 2. Several deliverables → one pipeline each.
3. Expand into the default pipeline for each deliverable (Step 3) and tell the user the plan in one line.
4. Ask only the questions the pipeline needs, one at a time, effort first (Step 4).
5. Run each sub-command's file (`commands/<name>.md`) in order, carrying the direction, DESIGN.md and Decision Log forward (Step 5).
6. If the effort is All-out, fill the All-out capability list (`references/workflow/all-out.md` §0) for every deliverable: run every Included capability as its own command (motion, surfaces, type, copy, assets, directions, review), ask the Offer rows (sound, voice, video, 3D, brand) in one multi-select question, and end every row Included, Declined or N/A with a reason.
7. Before any media work run `python scripts/doctor.py` and ask where each kind of media comes from (`references/media-sourcing.md` §2).
8. Finish with one close-out: gates, scorecard per deliverable, attribution, next step (Step 6).

## Output
Whatever the pipeline produces, plus the gate results, scorecard(s), attribution and a one-line next step.

## Never
- Answer with generic advice when the user wanted something built.
- Skip verify/score because the user only typed /dent.
- Load every reference "just in case".
- Drop a capability at All-out because the request didn't name it.

Close with the scorecard summary, attribution (DENT / MWG / user / agent judgment / overrides), the `### Modern Web Guidance` disclosure if guides shaped the code, and a one-line next step (SKILL.md §8).

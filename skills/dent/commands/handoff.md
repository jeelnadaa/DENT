# /dent:handoff

Write DESIGN.md and developer handoff (tokens, specs, states, a11y notes, licences).

**Usage:** `/dent:handoff <project>` (also `/dent handoff …` or `dent handoff …`)
**Default depth:** Standard. Effort level and the gates in SKILL.md §3 always apply.
**Web code:** if this command writes, changes or reviews HTML, CSS or client-side JS, Google's Modern Web Guidance is the primary authority for how it is built: run `references/modern-web-guidance.md` §2 (search → retrieve → apply → verify → disclose) before coding; MWG wins any implementation conflict with DENT.

## Load
- `references/design-md-template.md`
- `references/tooling-and-handoff.md` §4
- `references/design-tokens-and-code.md` Part 1

## Steps
1. Collect final values, decisions and licences.
2. Fill DESIGN.md (plus MOTION/SOUND/VIDEO specs if relevant).
3. Add handoff notes: screens + states, responsive behaviour, interaction and a11y annotations, assets, open questions.

## Output
DESIGN.md + exported tokens + handoff notes.

## Never
- Leave values vague ("nice blue").

Close with the scorecard summary, attribution (DENT / MWG / user / agent judgment / overrides), the `### Modern Web Guidance` disclosure if guides shaped the code, and a one-line next step (SKILL.md §8).

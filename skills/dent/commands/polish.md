# /dent:polish

Refine a working interface: hierarchy, spacing, type, details, interactions. No redesign.

**Usage:** `/dent:polish <screen or area>` (also `/dent polish …` or `dent polish …`)
**Default depth:** Standard. Effort level and the gates in SKILL.md §3 always apply.
**Web code:** if this command writes, changes or reviews HTML, CSS or client-side JS, Google's Modern Web Guidance is the primary authority for how it is built: run `references/modern-web-guidance.md` §2 (search → retrieve → apply → verify → disclose) before coding; MWG wins any implementation conflict with DENT.

## Load
- `references/quality-review.md Part 2`
- `references/modern-layer.md`
- `references/creative/hero-typography.md`
- `references/creative/anti-slop.md`

## Steps
1. Score the current state (scorecard) to find the weakest lines.
2. Fix in order of impact: hierarchy → spacing rhythm → typography craft → color/surfaces → built-in surfaces left on OS defaults (references/built-in-surfaces.md) → states → motion (check it meets references/motion/motion-menu.md §2 for the effort level; ask which kinds the user wants if unclear) → optical details.
3. Keep the information architecture and direction unless a change is justified and logged.
4. Re-score with evidence.

## Output
Before/after screenshots, change list with reasons, new score.

## Never
- Change the brand, IA or features without asking.

Close with the scorecard summary, attribution (DENT / MWG / user / agent judgment / overrides), the `### Modern Web Guidance` disclosure if guides shaped the code, and a one-line next step (SKILL.md §8).

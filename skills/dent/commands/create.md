# /dent:create

Create a new product, page, site or interface from scratch.

**Usage:** `/dent:create <what to create>` (also `/dent create …` or `dent create …`)
**Default depth:** Standard or Advanced. Effort level and the gates in SKILL.md §3 always apply.
**Web code:** if this command writes, changes or reviews HTML, CSS or client-side JS, Google's Modern Web Guidance is the primary authority for how it is built: run `references/modern-web-guidance.md` §2 (search → retrieve → apply → verify → disclose) before coding; MWG wins any implementation conflict with DENT.

## Load
- `references/workflow-questions-and-effort.md`
- `references/creative-direction.md`
- `references/creative/directions-library.md`
- `references/recipes/landing-page.md or references/recipes/app-and-dashboard.md`
- `references/foundations-and-components.md`
- `references/workflow/verification.md`

## Steps
1. Ask the effort level first, then only missing essentials (or decide everything if told to). At Standard+ always include the motion questions from references/motion/motion-menu.md §1 (multi-select kinds + intensity) unless the user said no motion.
2. Plan (inline for Standard, PLAN.md for Advanced) and audit it.
3. Direction: concept sentence, category-cliché check, one base style + ≤1 accent, signature element, hero type move.
4. Follow the recipe step by step, including every gate inside it.
5. Build tokens → components → screens → built-in surfaces at the chosen level (references/built-in-surfaces.md; ask the surface question at Standard+) → modern layer → media.
6. Verify (verify_page.py when a browser is available), fix, then score and close out.

## Output
Working files, Decision Log, gate results, scorecard, attribution; DESIGN.md after approval.

## Never
- Invent stats, testimonials, logos or ratings.
- Combine more than one base style and one accent.

Close with the scorecard summary, attribution (DENT / MWG / user / agent judgment / overrides), the `### Modern Web Guidance` disclosure if guides shaped the code, and a one-line next step (SKILL.md §8).

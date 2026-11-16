# /dent:audit

Audit an existing interface, codebase or screenshot and report findings. Change nothing.

**Usage:** `/dent:audit <URL, screenshot or path>` (also `/dent audit …` or `dent audit …`)
**Default depth:** Standard. Effort level and the gates in SKILL.md §3 always apply.
**Web code:** if this command writes, changes or reviews HTML, CSS or client-side JS, Google's Modern Web Guidance is the primary authority for how it is built: run `references/modern-web-guidance.md` §2 (search → retrieve → apply → verify → disclose) before coding; MWG wins any implementation conflict with DENT.

## Load
- `references/modes-existing-products.md §4`
- `templates/AUDIT.md`
- `references/quality-review.md`
- `references/accessibility.md`
- `references/modern-web-guidance.md (web code)`

## Steps
1. Establish scope, goal and main user task.
2. Look first: render/screenshot, run verify_page.py and drift measures when possible.
3. Evaluate: task success, heuristics, [Rule] failures, hierarchy, consistency, content, deceptive patterns, distinctiveness; for web code, also the implementation against the Modern Web Guidance guides for the patterns you find (search → retrieve).
4. Only if the user asked for code modernization or a legacy-pattern scan, run the MWG legacy scan (references/modern-web-guidance.md §7); otherwise offer it as a follow-up for a whole-codebase audit.
5. Write findings with evidence, severity, impact, recommendation and effort; separate verified defects from opinions.

## Output
templates/AUDIT.md filled in; offer to fix the top items in one line.

## Never
- Silently redesign or fix things.
- Give vague feedback without evidence.

Close with the scorecard summary, attribution (DENT / MWG / user / agent judgment / overrides), the `### Modern Web Guidance` disclosure if guides shaped the code, and a one-line next step (SKILL.md §8).

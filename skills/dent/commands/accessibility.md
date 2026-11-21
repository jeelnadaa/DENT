# /dent:accessibility

Focused accessibility audit and remediation (WCAG 2.2 AA).

**Usage:** `/dent:accessibility <page or app>` (also `/dent accessibility …` or `dent accessibility …`)
**Default depth:** Standard. Effort level and the gates in SKILL.md §3 always apply.
**Web code:** if this command writes, changes or reviews HTML, CSS or client-side JS, Google's Modern Web Guidance is the primary authority for how it is built: run `references/modern-web-guidance.md` §2 (search → retrieve → apply → verify → disclose) before coding; MWG wins any implementation conflict with DENT.

## Load
- `references/accessibility.md`
- `references/workflow/verification.md` §5
- `scripts/verify_page.py`
- `references/modern-web-guidance.md` (mwg:accessibility + the component guides)

## Steps
1. Run automated checks (verify script, axe if available).
2. Manually check landmarks, headings, names/labels, keyboard path, focus, dialogs, errors, contrast (all themes), targets, zoom/reflow, reduced motion, media alternatives.
3. Fix barriers that block task completion first; on the web use the native elements and patterns from the Modern Web Guidance guides (no ARIA re-added to native elements, no hand-made focus traps around <dialog>).
4. Re-verify every fix; list criteria actually checked.

## Output
Findings + fixes + which criteria were checked and how.

## Never
- Claim full compliance from an automated scan.

Close with the scorecard summary, attribution (DENT / MWG / user / agent judgment / overrides), the `### Modern Web Guidance` disclosure if guides shaped the code, and a one-line next step (SKILL.md §8).

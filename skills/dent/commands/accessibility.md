# /dent:accessibility

Focused accessibility audit and remediation (WCAG 2.2 AA).

**Usage:** `/dent:accessibility <page or app>` (also `/dent accessibility …` or `dent accessibility …`)
**Default depth:** Standard. Effort level and the gates in SKILL.md §3 always apply.

## Load
- `references/accessibility.md`
- `references/workflow/verification.md §5`
- `scripts/verify_page.py`

## Steps
1. Run automated checks (verify script, axe if available).
2. Manually check landmarks, headings, names/labels, keyboard path, focus, dialogs, errors, contrast (all themes), targets, zoom/reflow, reduced motion, media alternatives.
3. Fix barriers that block task completion first; prefer native semantics over ARIA.
4. Re-verify every fix; list criteria actually checked.

## Output
Findings + fixes + which criteria were checked and how.

## Never
- Claim full compliance from an automated scan.

Close with the scorecard summary, attribution (DENT / user / agent judgment / overrides) and a one-line next step (SKILL.md §8).

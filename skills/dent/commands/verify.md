# /dent:verify

Run the verification suite on built work and report results honestly.

**Usage:** `/dent:verify <page, URL or build>` (also `/dent verify …` or `dent verify …`)
**Default depth:** Standard. Effort level and the gates in SKILL.md §3 always apply.

## Load
- `references/workflow/verification.md`
- `templates/REVIEW.md`
- `scripts/verify_page.py`
- `scripts/contrast.py`

## Steps
1. Find available tools; say which checks can and cannot run.
2. Run `python scripts/verify_page.py <target> --out <dir>` and `scripts/contrast.py` on token pairs.
3. Open the screenshots and inspect them; do functional checks for what is in scope.
4. Record every gate as Passed / Failed / Not run / Blocked / N/A with evidence.

## Output
Verification report with evidence and the screenshots' paths.

## Never
- Fix things during verify unless asked (report first).

Close with the scorecard summary, attribution (DENT / user / agent judgment / overrides) and a one-line next step (SKILL.md §8).

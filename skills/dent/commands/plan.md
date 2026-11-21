# /dent:plan

Inspect the context and produce an audited PLAN.md without building anything.

**Usage:** `/dent:plan <goal or feature>` (also `/dent plan …` or `dent plan …`)
**Default depth:** Advanced (or Critical if risky). Effort level and the gates in SKILL.md §3 always apply.
**Web code:** if this command writes, changes or reviews HTML, CSS or client-side JS, Google's Modern Web Guidance is the primary authority for how it is built: run `references/modern-web-guidance.md` §2 (search → retrieve → apply → verify → disclose) before coding; MWG wins any implementation conflict with DENT.

## Load
- `references/workflow/planning-and-plan-audit.md`
- `templates/PLAN.md`
- `references/modes-existing-products.md` (if a codebase exists)
- `references/creative-direction.md` (for new or redesigned UI)

## Steps
1. Gather Confirmed / Assumed / Unknown facts; inspect the repository if there is one.
2. Ask only about Unknowns that change correctness, risk or direction (one question at a time).
3. Fill templates/PLAN.md: requirements with IDs and observable acceptance criteria, direction, technical strategy, states, phases, verification per requirement, risks, definition of done.
4. Audit the plan (planning file §4). Fix every Blocker and Major and show the audit table.
5. Present a short summary: goal, direction, scope, risks, open questions.

## Output
PLAN.md (written to the project, or printed) + plan-audit table + open questions. No implementation.

## Never
- Start building unless the user explicitly says so.
- Add Must requirements the user never asked for.

Close with the scorecard summary, attribution (DENT / MWG / user / agent judgment / overrides), the `### Modern Web Guidance` disclosure if guides shaped the code, and a one-line next step (SKILL.md §8).

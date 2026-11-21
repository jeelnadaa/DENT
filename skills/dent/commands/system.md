# /dent:system

Inventory, create or extend a design system (tokens, components, docs).

**Usage:** `/dent:system <scope>` (also `/dent system …` or `dent system …`)
**Default depth:** Advanced. Effort level and the gates in SKILL.md §3 always apply.
**Web code:** if this command writes, changes or reviews HTML, CSS or client-side JS, Google's Modern Web Guidance is the primary authority for how it is built: run `references/modern-web-guidance.md` §2 (search → retrieve → apply → verify → disclose) before coding; MWG wins any implementation conflict with DENT.

## Load
- `references/workflow/execution-and-scope.md` §1–2
- `references/design-tokens-and-code.md`
- `references/foundations-and-components.md`
- `references/tooling-and-handoff.md` §3

## Steps
1. Inventory foundations, components, behaviour and implementation; classify findings (Healthy, Inconsistent, Missing, Outdated, Conflicting, Intentional exception).
2. Propose one coherent system that reuses healthy parts; three-tier tokens.
3. Implement tokens and components; document each component (purpose, anatomy, variants, states, a11y, content).
4. Include the built-in surfaces (tooltips, scrollbars, form controls, selection, caret, placeholder, autofill) as system components with tokens (references/built-in-surfaces.md).
5. Verify with a component sheet (every component and built-in surface in every state).

## Output
Inventory table, token files, component specs, component sheet.

## Never
- Create a parallel system next to an existing one.

Close with the scorecard summary, attribution (DENT / MWG / user / agent judgment / overrides), the `### Modern Web Guidance` disclosure if guides shaped the code, and a one-line next step (SKILL.md §8).

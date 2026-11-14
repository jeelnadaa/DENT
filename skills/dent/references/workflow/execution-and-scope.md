# Execution, Scope Discipline and Design-System Inventory

How to build in controlled phases without damaging what already works. Used by SKILL.md §1.5, `/dent:implement`, `/dent:extend`, `/dent:redesign`, `/dent:system`, `/dent:fix`.

---

## 1. Design-system inventory (before changing an existing product)

Inspect and fill this table (short notes are fine):

| Layer | Inspect |
|---|---|
| Foundations | Color roles, type families/weights/scale, spacing scale, radii, borders, shadows/elevation, grid, breakpoints, motion durations/easings, sound (if any) |
| Components | Buttons, inputs and form controls, navigation, cards/surfaces, dialogs/overlays, tables, feedback (toasts, alerts), loading/empty states, icons |
| Behaviour | Hover/focus/active/disabled/selected, keyboard, responsive variants, validation, themes |
| Implementation | Token source, component library, styling conventions, naming, utilities, Storybook/docs |

Classify every relevant finding:

| Class | Meaning | Action |
|---|---|---|
| **Healthy** | Works and is consistent | Reuse it |
| **Inconsistent** | Same thing done several ways | Consolidate to the healthiest version when in scope |
| **Missing** | Needed and absent | Add it, in the existing convention |
| **Outdated** | Works but harms users or maintenance | Recommend replacement with a reason |
| **Conflicting** | Two sources of truth disagree | Resolve before extending |
| **Intentional exception** | Different on purpose (e.g. marketing hero) | Preserve and document |

Quick drift measures (commands) are in `../modes-existing-products.md` §2.2.

## 2. Extension rules
- Reuse healthy components and tokens; extend an existing variant before creating a new component.
- No duplicate tokens/components; no second library doing the same job.
- Don't force unrelated screens into identical layouts; keep intentional exceptions.
- New tokens/components are named in the project's convention and documented in DESIGN.md.
- Don't bring a heavy design-system framework into a small project without a clear benefit.

## 3. Phased execution
1. Work in small, testable increments in the order of the plan's phases (tokens → base styles → shared components → screens → modern layer → media).
2. After each phase: check its completion criteria, run the relevant gates, update the plan's status column.
3. If repository facts contradict the plan, stop and re-plan (planning file §8).
4. Record significant deviations in the Decision Log with the reason.
5. Never mark a phase complete because the code compiles.

For Quick/Standard tasks, skip ceremony: change, verify, report.

## 4. Scope protection

**Before editing:** list the files and components in scope, behaviour that must not change, and shared components that other screens use.

**While editing:** no opportunistic refactors, no framework or styling-architecture swaps without approval, no content/navigation/feature changes outside scope, never delete behaviour because it isn't visible in the screenshot you were given.

**After editing:** read your diff. Remove unrelated changes. Check every other screen that uses a shared component you touched. Explain any justified scope change.

## 5. Working with assets and dependencies
- Prefer assets already in the project; record the licence of every new font, icon set, image, model, sound, voice or footage (`../catalog/asset-sources.md`).
- Add a dependency only when it clearly beats a few lines of code or an existing dependency; one library per job; check licence, size, maintenance and framework compatibility (`../catalog/component-selection.md`).
- Never fabricate screenshots, logos, testimonials or data. Mock content is labelled as mock.

## 6. Definition of done
A task is done when:
- [ ] Every in-scope requirement is implemented, and critical acceptance criteria are verified.
- [ ] Every applicable gate (SKILL.md §3) is Passed, or Failed/Not run with a stated reason.
- [ ] No known critical defect remains; unrelated functionality still works.
- [ ] DESIGN.md / PLAN.md updated where relevant.
- [ ] Scorecard filled; remaining issues reported.

## 7. Stop polishing
Once the bar is met: stop adding optional effects, unrequested features or refactors. Put further ideas in one "Next" line. Quality means meeting the goal well, not maximising changes.

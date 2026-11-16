# Recipe: App Screens, Dashboards and Flows

Step-by-step procedure for product UI: dashboards, data-heavy tools, settings, CRUD, onboarding, multi-step forms, AI apps. Gates are mandatory; defaults may be overridden with a logged reason.

---

## Step 1: Users, tasks, frequency
- Who uses it, how often (daily power user vs occasional), on what device, in what context (desk, field, night).
- The **top 3 tasks** in order of frequency and the **one critical task** (where errors are costly).
- Data: what objects exist, their volumes (0, 1, 10, 10 000), how fresh, who can edit (roles).

## Step 2: Information architecture
- Objects and actions (nouns and verbs). Navigation from objects, not from org structure.
- Navigation pattern by platform and size: sidebar (≥ 5 areas, desktop), top tabs (2–5), bottom nav (mobile, 3–5).
- Each screen: its single primary action; secondary actions in a toolbar or overflow menu.

**Gate A1 (location):** on every screen the current location is marked and the user can go back.

## Step 3: Screen states before visuals
For each screen list: empty (first use / no results / cleared / no permission), loading (skeleton matching layout), error (what happened + retry), partial/stale, success, long content, 0/1/many, offline if relevant.

**Gate A2 (states):** every listed state is designed and reachable in the prototype (a dev toggle or query param is fine).

## Step 4: Density and layout
- Density from frequency: daily experts → compact (row 36–40 px, 13–14 px text); occasional → comfortable (48 px rows, 15–16 px).
- Dashboards: answer the user's top question in the first row (one hero KPI or chart), then supporting details; vary tile sizes by importance; every chart answers a question (`../data-visualization.md` §1).
- Tables: right-aligned tabular numbers, sticky header, sort, filters as chips, bulk actions, row actions on hover **and** keyboard, responsive strategy (cards or pinned first column) (`../components-extended.md` §15).

**Gate A3 (data honesty):** sample data is realistic and varied (not $1,234.56 everywhere, not "John Doe"); charts start at sensible baselines; no truncated axes that exaggerate.

## Step 5: Components and libraries
- Reuse the project's components; otherwise native elements per Modern Web Guidance for everything the platform covers (dialogs, drawers, menus, tooltips, tabs, switches, selects, toasts; `../modern-web-guidance.md` §4–5), and a library via `../catalog/component-selection.md` only for jobs it doesn't (e.g. TanStack Table or AG Grid Community for grids, cmdk for command palette, dnd-kit for board drag-and-drop, Recharts/ECharts/Visx for charts).
- Search and retrieve the MWG guide for each component and behaviour before building it; record the ids in the Decision Log.
- Define every interactive component's states (`../foundations-and-components.md` §4.21 template).

**Gate A4 (operability):** keyboard path through the critical task; focus management in dialogs/drawers/menus; every control labelled; targets ≥ 24 px pointer / 44 px touch.

## Step 6: Feedback and recovery
- Optimistic updates for low-risk actions with rollback on failure; undo instead of "Are you sure?" for reversible actions; confirmation with consequences for irreversible ones.
- Toasts for non-blocking confirmations (announced via live region); inline errors at fields; banners for system issues.
- Long jobs: progress, cancel, background + notify.

**Gate A5 (recovery):** for the critical task, force each failure (validation, network, permission) and confirm the user can recover without losing input.

## Step 7: Flows (onboarding, multi-step forms, checkout)
- Steps visible (stepper for 3–7 steps); progress saved; back never loses input; validation on blur/submit, not on every keystroke; summary/review step before commit.
- Onboarding gets the user to the first real value fast; teach in context, skip tours longer than 3–5 steps.

## Step 8: AI interfaces (when relevant)
Streaming with a stop button; visible states (thinking, using tool X, waiting for approval, done, failed); citations/sources; retry and edit; uncertainty language; approvals before consequential actions; history (`../page-and-flow-patterns.md` §16).

## Step 9: Motion
Ask which kinds and how strong (`../motion/motion-menu.md` §1; recommended app set in §4) and meet the app minimum (§2). Typical: state changes, layout shifts animated (FLIP/Motion layout), drawers and dialogs, number changes (NumberFlow-like), no decorative loops in tools. Reduced motion respected.

## Step 10: Verify, score, close
- verify_page.py on key screens (overflow, labels, contrast, reduced motion).
- Walk the top 3 tasks and the critical task end to end, including failures (`../workflow/verification.md` §7).
- Scorecard lines: task completion, IA clarity, density fit, data clarity, states, recovery, consistency, accessibility, responsiveness, performance (large lists virtualised?), distinctiveness.

## Minimum bars by effort
| Effort | Adds |
|---|---|
| Essential | Steps 1–3, 5–6, 10 for the critical task |
| Standard | + all top-3 tasks, density decision, dashboard hierarchy, responsive strategy |
| Polished | + dark mode, command palette/shortcuts, micro-interactions, empty-state illustrations, saved views |
| All-out | + IA map, full journeys with failure paths, role/permission states, i18n readiness, performance budget with measurements, design-system documentation, and the All-out sweep (`../workflow/all-out.md` §2) |

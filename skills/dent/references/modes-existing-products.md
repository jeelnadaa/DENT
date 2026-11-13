# Modes — Create, Redesign, Audit, Extend, Implement

Most real design work is **not** a blank canvas. Before asking the usual questions (workflow file §3), decide which mode the request is in. The mode changes which questions you ask, what you read first and what you deliver.

---

## 1. Pick the mode

| Mode | The user says… | First move | Deliverable |
|---|---|---|---|
| **Create** | "Design a…", "build me a landing page", nothing exists yet | Normal workflow (effort level → questions) | Screens + Decision Log → DESIGN.md |
| **Redesign** | "Redesign / modernize / refresh our app", "make it look better" + existing product | **Inventory first** (§3), then ask what must stay | Before/after, migration plan, new DESIGN.md |
| **Audit / Review** | "Review this", "what's wrong with my UI", "critique", a screenshot or URL | **Look before talking** (§4) | Prioritized findings report (§4.3) |
| **Extend** | "Add a settings page", "add dark mode" to something DENT already designed | Read DESIGN.md, add-on routing (workflow file §4) | The addition + DESIGN.md changelog line |
| **Implement** | "Build this in React", "turn DESIGN.md into code" | Read DESIGN.md; detect the stack (§2) | Code that uses tokens only + visual verification |
| **Adopt** | Codebase already has a design system / UI library | Detect and **respect** it (§2) | Work that fits the existing system |

If the mode is unclear, ask **one** question:
> **Do you want me to…**
> 1. **Improve what's there (Recommended)** — keep your structure and brand, fix and modernize.
> 2. **Start fresh** — new look and structure; I'll keep only your content and features.
> 3. **Just review it** — a prioritized list of problems and fixes, no changes yet.

---

## 2. Working inside an existing codebase

**Rule: never introduce a second design system.** If the project already has tokens, a theme, or a component library, extend it. Two button components, two color sets or two spacing scales is the most common way agents make products worse.

### 2.1 Detect (read before writing)
Look for, in this order:
1. **DESIGN.md** (from DENT or similar), `design-tokens.json`, `tokens/`, `*.tokens.json` (DTCG).
2. **Theme/config:** `tailwind.config.*`, a CSS file with `@theme` (Tailwind v4), `:root { --… }` variables, `theme.ts`, `createTheme(` (MUI), `extendTheme(` (Chakra), `ThemeData(` (Flutter), `Color+Theme.swift`, `Theme.kt` / `MaterialTheme(` (Compose).
3. **Component library:** `components.json` (shadcn/ui), `@radix-ui/*`, `react-aria`, `@mui/*`, `@chakra-ui/*`, `@mantine/*`, `antd`, `vuetify`, `@angular/material`, `daisyui`, `@headlessui/*`, `bits-ui`, `@ark-ui/*`.
4. **Existing UI folder:** `components/ui`, `src/components`, `design-system/`, a Storybook (`.storybook/`).
5. **Icon library and fonts** in `package.json` / font imports.

### 2.2 Measure drift (quick, objective)
Count distinct raw values used in styles. High counts mean no system or a broken one.
```bash
# distinct hex colors
grep -rhoE '#[0-9a-fA-F]{3,8}\b' src | sort | uniq -c | sort -rn | head -40
# distinct font sizes / radii / shadows (CSS)
grep -rhoE 'font-size:\s*[^;]+' src | sort | uniq -c | sort -rn
grep -rhoE 'border-radius:\s*[^;]+' src | sort | uniq -c | sort -rn
# Tailwind arbitrary values (escape hatches)
grep -rhoE '\b[a-z-]+-\[[^]]+\]' src | sort | uniq -c | sort -rn | head -40
```
Healthy targets: ≤ ~12 neutrals + brand + semantic colors; ≤ ~8 font sizes; ≤ 5 radii; ≤ 4 shadows; near-zero arbitrary values.

### 2.3 Adopt, extend or replace
| Situation | Do |
|---|---|
| Coherent system exists | **Adopt.** Use its tokens and components. Map DENT's rules onto them; only add missing tokens/components, named in its convention. |
| System exists but drifted | **Consolidate.** Map stray values to the nearest token, merge duplicate components, then design. |
| Library default look (unstyled shadcn, stock MUI/Bootstrap) | **Re-theme**, don't replace: change its tokens (color, radius, font, shadows) to the new DESIGN.md. |
| No system at all | **Create** tokens first (design-tokens-and-code.md), then refactor screens onto them incrementally. |
| User explicitly asks for a new system | Replace, but via the migration plan in §3.3. |

Record the decision in the Decision Log ("Adopted existing shadcn/ui tokens; re-themed radius 6→10px, added `--color-accent`").

---

## 3. Redesign

### 3.1 Inventory before opinions
1. **Screens & flows:** list every screen and the 3–5 most important tasks.
2. **Components:** list every component type and how many variants exist in practice (e.g. "7 button styles").
3. **Tokens in practice:** the drift numbers from §2.2.
4. **What works:** things users rely on (navigation order, shortcuts, terminology, positions of key actions). These have **muscle memory** — keep them unless broken [Law: Jakob's Law applies to your own product too].
5. **Pain points:** from the user, analytics, support tickets, reviews, or a heuristic pass (§4).

### 3.2 Ask what must stay
One question, options tailored, e.g.:
> **What must stay the same?**
> 1. **Brand colors and logo (Recommended)** — refresh everything around them.
> 2. **Layout and navigation** — users know where things are; modernize the look only.
> 3. **Nothing is sacred** — redesign freely, keep features and content.

### 3.3 Migration plan (Polished / All-out, or any product with real users)
- **Strategy:** *incremental* (token swap → components → screens; ships continuously, lowest risk) vs *big-bang* (new design behind a flag, switch at once). Default to incremental.
- **Order:** tokens → base styles → shared components → highest-traffic screens → the rest.
- **Compatibility:** keep old component APIs as wrappers, mark deprecated, remove later.
- **Feature flag / beta opt-in** for big visual changes; offer "switch back" for a limited time on large products.
- **Communicate:** a short "What's new" moment for changed navigation or moved actions.
- **Regression checks:** screenshot the old version first, compare after (quality-review.md Part 1).

### 3.4 Show before/after
Present key screens side by side with 3–5 bullet points on *why* each change helps (cite the principle in plain words). Never just "made it cleaner".

---

## 4. Audit / review an existing UI

### 4.1 Gather
- Screenshots or a URL (render and capture at mobile/desktop, light/dark if available).
- The product's goal and main user task (ask once if unknown).
- Code, if available: run the drift measures (§2.2) and automated checks (axe, Lighthouse).

### 4.2 Evaluate in this order
1. **Task success:** can a first-time user complete the main task? (Walk it step by step.)
2. **Nielsen's 10 heuristics** (SKILL.md §2) — note violations per screen.
3. **[Rule] failures:** contrast, target size, focus, keyboard, color-alone, reduced motion.
4. **Hierarchy & layout:** squint, 5-second and grayscale tests (quality-review.md Part 2 §1).
5. **Consistency:** component and token drift.
6. **Content:** labels, errors, empty states.
7. **Deceptive patterns** (persuasion-and-ethics.md Part 2).
8. **Craft & distinctiveness:** anti-patterns list (quality-review.md Part 2 §3).

### 4.3 Report format
Lead with a 3-line summary (overall score from the rubric, the biggest problem, the quickest big win). Then a table:

| # | Severity | Where | Problem | Why it matters | Fix | Effort |
|---|---|---|---|---|---|---|
| 1 | Critical | Checkout, step 2 | "Continue" button 2.1:1 contrast on mobile | Fails WCAG 1.4.3; many users can't see the main action | Use `--accent-strong` (#1F4FD8, 5.6:1) | S |

**Severity scale**
- **Critical** — blocks a main task, fails a legal accessibility rule, or deceives users.
- **High** — causes errors or abandonment for many users.
- **Medium** — slows users down or erodes trust; inconsistency.
- **Low** — polish and craft.

**Effort:** S (minutes, token/copy change) · M (a component or screen) · L (flow or system change).

Sort by severity, then by effort (quick wins first). Limit to the top 10–15 findings; group the long tail. Offer to fix in one line ("Want me to fix the 4 critical/high items now?").

### 4.4 Tone
Specific, kind and evidence-based. Credit what works (2–3 bullets) before the problems. Never mock the existing design — someone made reasonable decisions with the constraints they had.

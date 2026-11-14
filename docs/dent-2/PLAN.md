# DENT 2.0: Audit, Migration Plan and Plan Audit

Status: approved by the maintainer's request on 2026-11-14 ("go all out"). Progress is tracked in [PROGRESS.md](PROGRESS.md).

---

## 1. Audit of DENT 1.0.1 (what exists)

| Area | State | Keep / change |
|---|---|---|
| `SKILL.md` (803 lines) | Workflow, laws, tokens, ~20 component specs, the "modern layer" (motion, hover, scroll, depth), checklist, routing table. Always loaded. | **Too big for an always-loaded file.** Keep identity, workflow, laws, non-negotiables, checklist and routing. Move tokens + components and the modern layer into references. |
| 25 flat reference files | Good depth: color, typography, a11y, i18n, patterns, platforms, industries, data viz, brand, assets, ethics, research, quality review, tokens/code, modes, creative direction, brief/metrics, components-extended, complex patterns, tooling. | **Keep all paths** (backward compatible). Fix cross-references after the SKILL.md split. |
| 41 style files + index + template | Strong. | Keep. Add "how a strong model may remix" note. |
| Commands | Only `/dent` (skill invocation). No focused commands. | **Missing.** Add command system (§3 below). |
| Planning | Effort levels, questions, Decision Log, DESIGN.md. No PLAN.md, no plan audit, no task-depth classification, no traceability. | **Missing.** Add workflow modules. |
| Verification | Screenshot loop + rubric + contrast snippet. Not enforced; no functional, journey, motion or audio checks; no tooling. The Gemini benchmark shipped horizontal overflow, invented stats and unlabeled inputs. | **Weak.** Add `verify_page.py`, a verification procedure with gates, honest status reporting. |
| Component/library knowledge | Mentions Radix, React Aria, shadcn, Motion in passing. | **Missing.** Add sourced catalogue + selection method. |
| Motion | Interface motion is good. No motion graphics, kinetic type systems, storyboards, 2D/3D, generative, tech selection. | **Missing.** Add motion module. |
| Audio | 1 short section on sound/haptics in platforms file. | **Missing.** Add audio module incl. narration/voice and music. |
| Video | None. | **Missing.** Add video module (launch, trailer, explainer, …; AI-gen vs code tools). |
| Creative depth | Concept sentence, directions axes, default-look list. | **Not enough for weak models.** Add a large directions library, hero-typography system, anti-slop detector with reasons, recipes with gates. |
| Self-assessment | Rubric exists in quality-review. | Add request-specific scorecard, `/dent:score`, `/dent:improve`, attribution (DENT vs own judgment vs user), override clause. |
| Evals | 15 behavior cases + benchmark folder (2 prompts, 1 real result). | Keep; add scenario suite (18+), command tests, test protocol with prompt + Q&A + output, A/B/C conditions. |
| Validator | Frontmatter, links, styles index. | Extend: commands ↔ files ↔ plugin wrappers, catalogue entry fields, template presence, SKILL.md size budget. |
| Repo | README, install docs, plugin manifests, scripts, CI, benchmark. | Keep. README becomes a real landing page with genuine assets. |

### Problems found
1. Always-loaded file carries ~530 lines that only some tasks need.
2. Fake-social-proof rule exists but is one bullet; the Gemini run ignored it. Rules that matter must be gates in the procedure, not prose.
3. Verification is described but never forced; no tool to run.
4. Style mixing ("Editorial + Bento + Cupertino") slipped through; rule is buried in §9.
5. No "category cliché" check: coffee → espresso brown + orange + serif happened in both runs.
6. `improvement.md` lacks: component catalogue detail, motion graphics, audio (incl. narration, music), video, 3D/dimensions, creative-direction depth, self-scoring, attribution, override clause, weak-model procedures, test protocol, showcase plan.

## 2. Target architecture

```text
skills/dent/
├── SKILL.md                     # router + non-negotiables + workflow + scoring (lean)
├── commands/                    # one file per command intent (source of truth)
├── references/
│   ├── (25 existing flat files, unchanged paths)
│   ├── foundations-and-components.md   # moved from SKILL.md §3–4
│   ├── modern-layer.md                 # moved from SKILL.md §7
│   ├── workflow/      # task depth, planning + plan audit, execution + scope, verification, closeout + scoring
│   ├── recipes/       # step-by-step procedures with gates (landing page, app/dashboard)
│   ├── creative/      # directions library, hero typography, anti-slop detector
│   ├── catalog/       # component/library catalogue + selection method + asset sources
│   ├── motion/        # motion graphics, motion tech catalogue, 3D/real-time, motion system + verification
│   ├── audio/         # sound design, voice & narration, audio tech catalogue, implementation + verification
│   └── video/         # video types & craft, video tools & production pipeline
├── templates/         # PLAN, AUDIT, REVIEW (verification report), SCORECARD, MOTION, SOUND, VIDEO
└── scripts/           # verify_page.py, contrast.py
commands/ (repo root)  # Claude Code plugin wrappers → /dent:<name>
evals/                 # cases + scenarios + protocol + command tests
```

### Command platform facts (checked)
- Claude Code plugins discover `commands/*.md` at the plugin root → `/dent:<name>`. Manual skill installs don't get those files.
- Other agents (Codex, Cursor, Copilot, Gemini CLI…) load `SKILL.md` but have no shared command convention.
- **Decision:** command behavior lives in `skills/dent/commands/<name>.md` (travels with every install). SKILL.md maps typed `/dent:<name>`, `/dent <name>` or "dent <name>" to that file. Root `commands/` holds thin Claude Code wrappers that load the skill and point to the same file. One source of truth.

## 3. Phases

| Phase | Work | Depends on | Done when |
|---|---|---|---|
| 0 | This audit + plan; expand `improvement.md` scope (Part XXI; Parts XII–XX were added by the maintainer and are treated as requirements) | — | Plan audited and revised (§4) |
| 1 | Split SKILL.md; new SKILL.md router; fix all cross-refs; non-negotiables incl. benchmark failures | 0 | Validator OK; no reference to moved sections broken |
| 2 | Workflow modules; templates; command files (skill + plugin wrappers) | 1 | Every command has file + wrapper + routing row; validator checks it |
| 3 | Creative: directions library, hero typography, anti-slop detector, recipes with gates | 1 | Landing-page recipe contains gates for every Gemini failure |
| 4 | Catalogues: components (+ selection method), assets; motion (+ 3D), audio (+ voice), video | 1 | Every entry has role, license, URL, status/date; uncertain items marked |
| 5 | Tools: `verify_page.py`, `contrast.py`; validator extension; evals (scenarios, protocol, command tests) | 2–4 | Scripts run against the real Brewlog pages and catch the known defects |
| 6 | README landing page with genuine assets (animated SVG hero, diagrams); docs; changelog; version 2.0.0 | 1–5 | All README assets exist, render on GitHub (no JS), links resolve |
| 7 | Final audit, validator, commit locally | 6 | Clean `git status` apart from deliberate exclusions |

**Deferred to the next session (needs DENT 2.0 installed, per the maintainer):** build DENT's real landing page, a motion-graphics piece and an explainer video with narration *using* DENT 2.0, record prompts + answers + outputs + scores, then put them on the README.

## 4. Plan audit

| # | Finding | Severity | Resolution |
|---|---|---|---|
| A1 | Moving SKILL.md sections could break 30+ cross-references ("SKILL.md §4", "› Modern layer"). | Blocker | Grep every reference, rewrite to the new files, validator fails on dangling `SKILL.md §` numbers. |
| A2 | A colon in command names isn't portable. | Major | Accept `/dent:x`, `/dent x`, `dent x` in SKILL.md; Claude Code gets real `/dent:x` via wrappers. |
| A3 | Catalogue licensing can't all be re-verified live in one session. | Major | Each entry carries a status: `checked 2026-11-14` (verified via official source/search this session) or `from maintainer knowledge — verify before relying`. No invented facts. |
| A4 | Risk of building a huge prompt pile instead of capability. | Major | Every new module ends in procedures, gates or tables an agent can execute; tools that actually run; validator enforces structure. |
| A5 | "Insane creativity" vs non-negotiables could conflict. | Major | Override clause: strong models may break Conventions/recipes with a logged reason; never Rules or honesty rules. |
| A6 | Weak-model guidance could bloat SKILL.md. | Minor | Put procedures in `recipes/` and command files; SKILL.md links them. |
| A7 | Self-scoring by the same model is biased (spec §22.5). | Minor | Scorecard requires evidence per line and caps scores without verification; README benchmark keeps human/other-model review. |
| A8 | README "showcase" items that don't exist yet. | Major | Only ship assets created now (animated SVG hero, diagrams); showcase slots say "next: built with DENT 2.0" without fake media. |
| A9 | Plugin `commands/` at repo root + `skills/` — does `npx skills` pick up root commands? | Observation | No; harmless. Documented in INSTALL. |

Revisions applied: A1–A8 folded into phases 1–6 above.

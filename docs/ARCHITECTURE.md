# DENT 2.0 Architecture

How the skill is organised, how a request flows through it, and how to extend it without breaking anything.

## 1. Design principles
1. **Router, not encyclopedia.** `SKILL.md` (~330 lines, always loaded) classifies the task, routes it, states the non-negotiables and gates, and says what to open next. Everything else loads only when needed (progressive disclosure).
2. **One source of truth per thing.** Commands are defined once in `skills/dent/commands/` (generated from `scripts/build_commands.py`); plugin wrappers and `docs/COMMANDS.md` are generated from the same list. Tokens and components live once in `foundations-and-components.md`.
3. **Procedures beat prose.** Rules that matter are **gates** inside recipes and commands, with automated checks where possible (`verify_page.py`), because prose rules alone failed in the first benchmark.
4. **Guidance for weak models, freedom for strong ones.** Recipes are a floor; the override clause lets strong models do better with a logged reason, never breaking a gate.
5. **Honesty is structural.** Catalogue entries carry a verification status; verification results use Passed / Failed / Not run / Blocked / N/A; self-scores need evidence and are capped without it.
6. **The web platform has its own authority.** Google's Modern Web Guidance (MWG) is vendored verbatim as a sibling skill and is the primary authority for *how* HTML, CSS and client-side JS are built; DENT keeps authority over *what* is designed. On an implementation conflict MWG wins (`references/modern-web-guidance.md` §1).

## 2. Request flow
```
user request ──► SKILL.md §0 ──► commands/<name>.md (explicit command)
                       │
                       └──► references/workflow/orchestration.md (plain /dent or words)
                               signal card → main command + companions → pipeline per deliverable
                                         │
     ┌───────────────────────────────────┼───────────────────────────────────┐
     ▼                                   ▼                                   ▼
 understand + ask              plan + plan audit                  direct (concept, cliché check,
 (workflow-questions…)         (workflow/planning…)               style, directions, hero type)
     │                                   │                                   │
     └──────────────► build (recipes, foundations, catalogues, motion/audio/video) ◄──────┘
                                         │   web code: MWG search → retrieve → apply (modern-web-guidance.md)
                                         │
                       verify (workflow/verification.md, scripts/verify_page.py, gates G1–G13)
                                         │
                score + attribution (workflow/scoring-and-closeout.md) ──► /dent:improve loop
                                         │
                         DESIGN.md (+ MOTION / SOUND / VIDEO specs, licence table)
```
At **All-out** effort, `workflow/all-out.md` adds a mandatory completeness sweep per deliverable and raises the score target to ≥ 9.

## 3. Folder map
| Path | Holds | Loaded when |
|---|---|---|
| `skills/dent/SKILL.md` | Router, workflow summary, laws, non-negotiables, gates, command table, reference map | Always |
| `skills/dent/commands/` | 34 command definitions: load list, steps, output, never-list | When a command runs (or the router picks it) |
| `references/workflow/` | Orchestration, planning + plan audit, execution + scope, verification, scoring + close-out, All-out protocol | Every non-trivial task (only the relevant file) |
| `references/recipes/` | Step-by-step procedures with gates (landing page, app & dashboard) | Building those deliverables |
| `references/creative/` | Directions library, hero typography, anti-slop detector | Direction, polish, review |
| `references/catalog/` | Component/library catalogue + selection method + asset sources and licences | Choosing libraries or assets |
| `references/motion/` | Motion graphics, motion tech catalogue, 3D/real-time, motion system + verification | Motion work |
| `references/audio/` | Sound design, voice & narration, audio tech catalogue, implementation + verification | Sound/voice work |
| `references/video/` | Video types & craft, tools & pipeline | Video work |
| `references/styles/` | 41 aesthetic styles + index + template | A look is named or chosen |
| `references/*.md` | Foundations & components, modern layer, color, typography, accessibility, patterns, platforms, industries, tokens & code, quality review, i18n, brand, assets, research, ethics, tooling | As routed |
| `skills/dent/templates/` | PLAN, AUDIT, REVIEW, SCORECARD, MOTION, SOUND, VIDEO | Advanced work, reviews, media |
| `references/built-in-surfaces.md` | Built-in surfaces (tooltips, scrollbars, sliders, form controls, selection, caret, placeholder, autofill): Match / Tint / Native question, surface tokens, inventory, style personalities, verification | Any visual web build at Standard+, `/dent:surfaces` |
| `references/modern-web-guidance.md` | DENT's adapter for Modern Web Guidance: precedence, workflow, DENT → MWG map, native-first rule, resolved conflicts | Any HTML/CSS/client-side JS work |
| `skills/modern-web-guidance/` | Google's Modern Web Guidance skill (SKILL.md + 209 guides), vendored verbatim with `LICENSE` and `UPSTREAM.json`; `vendor/modern-web-guidance/` inside zip and rules-file installs | Web work (its own trigger, or via DENT) |
| `skills/dent/scripts/` | `verify_page.py`, `contrast.py`, `palette.py` (concept palettes + cliché check), `fonts.py` (+ `data/google-fonts.json` snapshot), `tts.py` (narration over many engines, mastering, captions), `doctor.py` (capabilities), `mwg.py` (offline MWG search/retrieve), `update_plugin.py` | Verification, design tooling, media production, MWG lookups without network |
| `commands/` (repo root) | Claude Code plugin wrappers (generated) | Plugin installs only |
| `evals/` | Behaviour cases, scenarios, command/routing tests, protocol, fixtures | Testing DENT |
| `benchmark/` | Public with/without comparisons and results | Publishing results |
| `scripts/` (repo root) | validate, build_commands, test_tools, package, install, sync_mwg | Maintainers and CI |
| `assets/` | README visuals and their generator | README |

## 4. Compatibility with DENT 1.x
- All 1.x reference paths still exist. SKILL.md §3–4 (tokens, components) moved to `references/foundations-and-components.md` and §7 (modern layer) to `references/modern-layer.md`; section numbers inside them are preserved.
- Modes, effort levels, styles, DESIGN.md format and the Decision Log are unchanged (DESIGN.md gained optional sections: Brief, media specs, licence table; the Decision Log gained a Source column).
- `/dent` still works; it now routes through the orchestrator.

## 5. Extending DENT
| Add | Do | Then |
|---|---|---|
| A command | Add an entry to `COMMANDS` in `scripts/build_commands.py`, a row in SKILL.md §4, a routing row in `orchestration.md` | `python scripts/build_commands.py && python scripts/validate.py` |
| A style | Copy `styles/_style-template.md`, add an index row, update the style count (SKILL.md, README badge) | validate |
| A catalogue entry | Add a row with link, licence and status (`✓ <date>` only after checking the official source) | validate |
| A reference file | Create it, add rows to SKILL.md §9.2 and the add-on routing table | validate |
| A gate check | Extend `verify_page.py`, add a failing case to `evals/fixtures/bad.html` | `python scripts/test_tools.py` |
| A palette in the library | `skills/dent/scripts/palette.py make --accent … --second … --neutral …`, paste the rows into `color.md` §13 (never hand-pick hex values) | `python scripts/test_tools.py` (re-checks every palette in both themes) |
| A font pairing or type voice | `fonts.py suggest` / `fonts.py check --verify`, then `typography.md` §2–§3 | `python scripts/test_tools.py` (every pairing face must exist and not be overused); refresh the snapshot with `fonts.py refresh` |
| A TTS engine or media provider | an engine entry in `tts.py` (`ENGINES` + `render_local`/`render_cloud`), rows in `references/media-sourcing.md` and `audio/voice-and-narration.md` §5 with link, licence and status | render one line on a real machine; `python scripts/test_tools.py` |
| Web implementation guidance | Don't write it in DENT: point to the MWG guide (`mwg:<id>`) and keep only the design layer in DENT; if MWG lacks the topic, add it with a note to revisit | validate (checks every `mwg:<id>`) |
| A newer Modern Web Guidance | `python scripts/sync_mwg.py` (never edit `skills/modern-web-guidance/` by hand), re-read `references/modern-web-guidance.md` §6 for new conflicts | validate + `python scripts/test_tools.py` + CHANGELOG |

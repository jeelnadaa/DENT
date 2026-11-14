# Changelog

All notable changes to DENT are documented here. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow [SemVer](https://semver.org/).

## [Unreleased]

## [2.0.0] — 2026-11-14

DENT becomes a design-engineering system: interfaces, motion graphics, 3D, sound, narration and video, with orchestration, planning, enforced gates, runnable verification and self-scoring. Specification: `improvement.md` (Parts I–XXI). Audit, plan and progress: `docs/dent-2/`.

### Why
The first public benchmark (Brewlog, Antigravity + Gemini 3.8 Flash High) came out about even (36 vs 35 out of 50, re-checked with the new tools). The DENT 1.x run still shipped horizontal overflow on phones, invented social proof, unlabeled sliders, three mixed styles, the category cliché and a typo. Prose rules weren't enough, so 2.0 turns them into procedures, gates and tools.

### Added
- **Orchestration** (`references/workflow/orchestration.md`): plain `/dent` (or any request in words) fills a signal card, maps it to a main command plus companions, expands default pipelines per deliverable (several deliverables → several pipelines sharing one DESIGN.md), and closes with verify → score.
- **30 commands** (`skills/dent/commands/`, Claude Code wrappers in `commands/`, reference in `docs/COMMANDS.md`, all generated from `scripts/build_commands.py`): dent, plan, create, redesign, extend, implement, fix, polish, audit, review, verify, responsive, accessibility, system, components, directions, type, copy, brand, assets, motion, motion-graphics, 3d, sound, voice, video, launch-video, score, improve, handoff.
- **Workflow modules** (`references/workflow/`): task depth (Quick/Standard/Advanced/Critical), PLAN.md + plan audit (Blocker/Major/Minor/Observation) + approval policy + traceability + decisions; execution, scope protection and design-system inventory; verification (functional, visual, responsive, a11y, performance, journeys, regression, honest reporting); scoring, improve loop and attribution; the **All-out protocol** (best achievable result for the use case with nothing missed: per-deliverable completeness sweeps, score target ≥ 9).
- **Gates G1–G12** in SKILL.md (requirements, layout, contrast, operability, states, honesty, proofreading, style integrity, distinctiveness, motion, sound, licences) and **non-negotiables** (no invented proof, no claimed-but-unrun checks, no autoplay, no second design system…).
- **Recipes with gates**: landing page (L1–L11) and app/dashboard (A1–A5).
- **Creative depth**: directions library (category clichés for 12 categories, 25 fully specified web directions, 12 motion, 9 sound and 10 video directions, remix/invention methods), hero typography system (7 roles, pairing matrix with licences, 18 composition techniques, craft numbers, CSS recipes), reason-based anti-slop detector covering visual, layout, copy, motion, sound and video.
- **Component intelligence**: selection method + catalogues of primitives, full systems, copy-in collections, specialized components and paid products, each with URL, frameworks, licence/paid tiers, use/avoid and a verification status; asset sources and licences (fonts, icons, illustration, photos, 3D, footage, SFX, music, voices).
- **Motion**: motion graphics (kinds, 1D → XR, pipeline, animation principles, composition in time, 12-technique cookbook, README/social/video delivery), motion technology catalogue with selection ladder, 3D and real-time, motion system (personalities, tokens, rules, budgets) and motion verification.
- **Audio**: sound design (11 kinds of audio incl. sonic identity, ambience, procedural, music, narration, audio description, spatial, haptics), voice and narration (script for the ear, pronunciation, recording, TTS options with licences, loudness, captions), audio technology catalogue, implementation (audio manager, unlock-on-gesture, synthesis) and verification.
- **Video**: types and sub-types (launch: teaser/reveal/feature tour/manifesto/what's new; trailers; explainers; demos; social; ads; app previews; title sequences; data stories), craft, storyboard/animatic, tools (generative if the user has access; otherwise HyperFrames, Remotion, Motion Canvas, Revideo, Manim, editors, FFmpeg) with licences, platform specs and QA.
- **Templates**: PLAN, AUDIT, REVIEW, SCORECARD, MOTION, SOUND, VIDEO.
- **Runnable checks**: `skills/dent/scripts/verify_page.py` (overflow at 6 widths with offenders, unlabeled controls incl. hidden tabs, unnamed buttons/links, alt text, lang, heading skips, sampled contrast, animations under reduced motion, audio started before a gesture, console errors, screenshots) and `contrast.py`.
- **Self-scoring and attribution**: request-derived scorecard with evidence and caps; Decision Log Source column (User / DENT file § / Agent judgment / Override); override clause for strong models.
- **Evaluation**: `evals/protocol.md` (conditions A/B/C, record prompt + every question and answer + output + scores), `evals/scenarios.md` (21 scenarios incl. three showcase pieces), `evals/commands.md` (discovery, routing and per-command tests), fixtures + `scripts/test_tools.py`.
- **README landing page** with an animated SVG hero (plays once, respects reduced motion, light/dark) and a system diagram, generated by `assets/build_assets.py`; `docs/ARCHITECTURE.md`.

### Changed
- SKILL.md rewritten as a router (803 → ~330 lines). Tokens/components moved to `references/foundations-and-components.md`, the modern layer to `references/modern-layer.md` (section numbers kept); all cross-references updated.
- Effort level All-out redefined as a completeness promise for every workflow.
- Validator extended (links in all subfolders, commands trio, catalogue status and URLs, versions, templates); CI runs tool tests.
- Brewlog result corrected with the new checks: the run without DENT also overflows at 320 px and ignores reduced motion (36 vs 35).

### Compatibility
All 1.x reference paths, modes, effort levels, styles and the DESIGN.md format still work. Moved content keeps its section numbers. No breaking changes for installed users apart from the larger skill folder.

## [1.0.2] — 2026-11-14 (unreleased work folded into 2.0.0)

### Added
- **Benchmark** (`benchmark/`): a fixed "Brewlog" website prompt (v1) to run with and without DENT, fair-run rules, a 10-criterion scoring sheet, a Playwright screenshot script, a result template and a "Benchmark result" issue template. README gains a "See the difference" section and a results table.
- **DENT landing page prompt** (`benchmark/PROMPT-DENT-LANDING.md`): the content-only prompt used to build DENT's own landing page with DENT, usable as a second benchmark that lets the agent ask questions. Both prompts are now shown in full in the README, each with its own results table.
- **First benchmark result** (Brewlog, Antigravity + Gemini 3.8 Flash High): about a tie (first scored 37 vs 35; corrected to 36 vs 35 in 2.0.0). Screenshots render in the README; full write-up in `benchmark/results/…/RESULT.md`. Screenshot script now saves compact JPEGs; `.nojekyll` added so GitHub Pages can serve the live result pages.

## [1.0.1] — 2026-11-14

### Fixed
- Release workflow now attaches `dent.zip` even when the GitHub release already exists, so the Claude.ai / Claude Desktop download is available from Releases.

## [1.0.0] — 2026-11-14

First public release as **DENT** (previously an internal skill called `product-design`).

### Added
- **Modes** (`modes-existing-products.md`): Create, Redesign, Audit, Extend, Implement, Adopt. Detects existing tokens, themes and UI libraries (shadcn/ui, MUI, Chakra, Tailwind…) and extends them instead of introducing a second design system. Drift measurement commands, redesign migration plan, severity-ranked audit report format.
- **Creative direction** (`creative-direction.md`): concept sentence, mood/anti-mood words, divergent directions along 8 axes, signature elements, composition rules, 2025–26 "default look" list to avoid, type-led design, advanced color strategies, presenting work.
- **Design brief & metrics** (`design-brief-and-metrics.md`): one-page brief, JTBD, design principles, HEART, task metrics (SUS, SEQ, UMUX-Lite), guardrail metrics, event naming, honest A/B testing, lightweight validation.
- **Extended components** (`components-extended.md`): 25 specs — accordion, breadcrumbs, pagination, stepper, date/time picker, file upload, search, command palette, number stepper, OTP, tag input, rating, carousel, tree, advanced data table, kanban, calendar, timeline, editor toolbar, popconfirm, empty state, banner, avatar group/copy field/code block, color picker, range slider.
- **Complex product patterns** (`complex-product-patterns.md`): workspaces, roles & permissions, billing & subscriptions, notification center, audit log, versions/autosave, collaboration, offline & real-time, bulk actions & jobs, import/export, admin/CRUD, keyboard-first, security & privacy UX (passkeys, 2FA, sessions, account deletion, permission priming), trust & safety, in-product help, feature badges; content pages — blog, docs, changelog, about/careers, contact, error pages, legal, comparison, waitlist, case study.
- **Tooling & handoff** (`tooling-and-handoff.md`): previews in agent environments (style tiles, token and component sheets), Figma reading/structuring, Storybook docs, accessibility annotations, design QA, keeping DESIGN.md healthy.
- **Two new styles:** Utilitarian (industrial / instrument panel) and Retro OS (90s desktop). Total: 41.
- SKILL.md: mode selection (§1.0), concept step, agent-environment adaptation (§1.8), "Never" rules (§1.9), distinctiveness items in the pre-ship checklist.
- DESIGN.md template: Brief section, mood/anti-mood, signature elements, design principles, existing-system record.
- Repository: Apache-2.0 license, NOTICE, trademark policy, Claude Code plugin marketplace manifest, install scripts (bash + PowerShell), packaging script, validator, evaluation scenarios, CI.

### Changed
- Skill renamed `product-design` → `dent`; richer trigger description; author/version metadata.
- Workflow: question-count guidance made consistent across levels; add-on routing table covers all new reference files; effort table gains a "Brief & concept" row.

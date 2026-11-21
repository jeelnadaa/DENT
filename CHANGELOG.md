# Changelog

All notable changes to DENT are documented here. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow [SemVer](https://semver.org/).

## [Unreleased]

## [2.5.0] — 2026-11-21

"Go all out" now means everything, narration sounds human, and DENT stops reaching for the same fonts and colours. Specification: `docs/dent-3/SPEC.md`; evidence: `docs/dent-3/VERIFICATION.md`.

### Added
- **All-out capability list** (`references/workflow/all-out.md` §0): motion, surfaces, type, copy, assets, directions and independent review run as their own commands; sound, voice, video, 3D and brand are offered in one multi-select question; every row ends Included, Declined or N/A with a reason, and the list is repeated in the close-out.
- **Media sourcing** (`references/media-sourcing.md`): for voice, music, SFX, images, illustration, video, 3D, fonts and clean-up, DENT asks whether to use a local model (installed only after a yes), a free cloud tier, a paid provider or connector, **any provider not listed** (researched from official docs), or the user's own assets; it finds free models when the user knows none, shows costs before paid calls, and reads keys only from environment variables.
- **`scripts/tts.py`**: one interface over Qwen3-TTS, Kitten TTS 2, Chatterbox, Kokoro, Piper, system voices, OpenAI, ElevenLabs and any OpenAI-compatible endpoint (Voxtral via vLLM or gateways); one virtual environment per engine; `install` asks first (`--yes`); `compare` makes blind A/B sets; `post` trims, places, high-passes and loudness-normalises (two-pass) and writes SRT, VTT and a timing JSON. Per-engine guidance in `references/audio/voice-and-narration.md` §5.
- **`scripts/palette.py`**: concept-seed palettes in OKLCH with tinted neutrals, light and dark role tokens, automatic contrast repair and a 2026 cliché detector (Tailwind indigo/violet, zinc backgrounds, cream + terracotta, acid lime on black…).
- **`scripts/fonts.py`** + a Google Fonts metadata snapshot: overuse check (first- and second-order registries, popularity rank), licence verification against github.com/google/fonts, script/axis-aware suggestions of fresh faces, `refresh`.
- **`scripts/doctor.py`** and **`/dent:doctor`**: what this machine can do (browser checks, FFmpeg, GPU/VRAM, TTS engines, provider keys by name) before DENT promises anything.
- **`/dent:brainstorm`** (`references/workflow/brainstorm.md`): a candid design partner that steelmans, pushes back with labelled reasons (rule / evidence / taste), changes its mind only on new information, respects the user's decision and ends with a direction brief.
- **Three independent evaluators** (visual, UX, engineering) at Polished and All-out, in fresh contexts where subagents exist; any can reject the work (`scoring-and-closeout.md` §3b, `templates/REVIEW.md`, `/dent:review`).
- **Severity scale** and **visible blockers**: an open Blocker is listed first and caps the overall score at 6.
- **Dependency checklist** (`catalog/component-selection.md` §4b).
- **Style moves** (`creative-direction.md` §3b): apply, bend, blend or leave the catalogue with a style card; propose alternatives with reasons.
- `validate.py` **`check_capabilities`**: fails when a pipeline, example or command promises a capability another file never triggers; warns when a style's starter font is on the overused registry. `test_tools.py` covers the four new scripts and re-verifies every library palette and pairing face.
- **Measured voice ranking** (`audio/voice-and-narration.md` §5.5): Qwen3-TTS > Chatterbox > Kokoro > Kitten TTS 2 from signal quality, pitch variation, pace and Whisper word error rate on four contrasting lines, matching a blind listening test; the default engine order, per-engine notes and tips follow it. A pronunciation-trap step covers acronyms and invented names.
- `tts.py post --tempo`: pitch-preserving speed change for engines that rush (Chatterbox).
- Eval scenarios S22–S26 (All-out completeness, narration, unlisted provider, brainstorm pushback, fresh type and colour) and a previous-version-vs-current benchmark condition.

### Changed
- **Typography:** no house font. The Satoshi/Cabinet Grotesk/Clash Display priority is replaced by a method (voice → `fonts.py` → render → rotate), 13 type voices and 25 pairings from verified OFL faces, free and paid foundry options, and a font-source question.
- **Colour:** the ten default palettes (which matched the "tasteful AI" look) are replaced by a method and 20 concept palettes generated and verified in both themes.
- Style starter fonts swapped away from overused faces in 22 style files; Minimal's and Editorial's starter colours changed; style tokens are documented as starting points.
- G8 accepts a bent style or an off-catalogue style card as a coherent system; G9 includes the font and palette registries.
- `create`, `redesign` and `extend` run motion and surfaces as part of the build; all media commands ask the sourcing question; the video pipeline's first question covers every media type.
- Router: All-out expands every pipeline; brainstorm and doctor routes; the All-out worked example now includes motion.

### Fixed
- "Go all out" skipped motion (the worked example and the create command never ran `/dent:motion`).
- The command generator put annotations inside backticked paths and gave non-building commands a scorecard close.
- `SKILL.md`'s decision-log example cited a palette that no longer existed.

## [2.4.0] — 2026-11-16

Nothing ships with a default look by accident: DENT now designs the parts the browser draws for you.

### Added
- **Built-in surfaces** (`references/built-in-surfaces.md`): tooltips, scrollbars, range sliders, checkboxes, radios, switches, selects and pickers, text selection, caret, placeholder, autofill, validation, file inputs, progress, disclosure markers, dialog backdrops, link underlines, browser chrome and system dialogs. Includes:
  - a **[Rule]**: every surface present gets a deliberate level (**Match**, **Tint** or **Native**), logged in DESIGN.md
  - **one question** at Standard+ ("Match my design everywhere (Recommended) / Brand tint only / Keep the native look / Let me choose per element")
  - don't-ask defaults (Tint at Essential, Match at Standard+)
  - surface tokens with contrast rules
  - a per-surface inventory with the Modern Web Guidance guide for each
  - style personalities (how a Brutalist or Glass tooltip and scrollbar should look)
  - a build order with a **surface sheet**
  - native-app notes
- **`/dent:surfaces`** (32 commands): inventory the surfaces on a page, ask the level, derive tokens, build each surface on the native element per its MWG guide, cover every state and theme, verify.
- **`verify_page.py --surfaces match|tint|native`**: reports which built-in surfaces are present and styled, flags `title`-attribute tooltips, thin scrollbars and browser validation bubbles, and sets gate **G8_surfaces**. New fixture cases and `test_tools.py` assertions.

### Changed
- G8 Style integrity now covers built-in surfaces. They also appear in:
  - the effort table and question order
  - "don't ask" defaults and add-on routing
  - `/dent:create`, `/dent:polish` and `/dent:system` steps; orchestration routing and pipelines
  - both recipes, the All-out sweeps
  - the token checklist, the DESIGN.md template (§7b) and PLAN.md
  - the anti-slop detector (OS-default surfaces on a designed page) and the MWG map
- Landing page: scrollbars themed in both colour schemes and in the inverted install section (`verify_page.py --surfaces match` passes).

## [2.3.0] — 2026-11-16

Google's **Modern Web Guidance** (MWG) becomes DENT's primary authority for all web development and front-end engineering. DENT keeps deciding *what* is designed; MWG decides *how* HTML, CSS and client-side JS are built, and wins any implementation conflict.

### Added
- **Bundled MWG skill** (`skills/modern-web-guidance/`): Google Chrome's skill (stewarded with the Edge, Firefox and MDN teams), vendored verbatim with its Apache-2.0 `LICENSE` and an `UPSTREAM.json` pin (commit `4dd9683`, skill version `2026_11_09-5bcc021b`, 209 guides). The plugin exposes it as its own skill, so it also triggers on web tasks outside DENT. `scripts/sync_mwg.py` refreshes it; `NOTICE` credits it.
- **`references/modern-web-guidance.md`**: precedence rules (user/support policy → MWG → DENT → libraries), the search → retrieve → apply → verify → disclose workflow, CLI notes (Windows/Git Bash quirk, sandbox allowlisting), browser-support policy, a DENT → MWG map covering 131 guides, the **native-first** component rule, the table of resolved conflicts, and the legacy-scan flow for modernisation requests.
- **`mwg:<id>` references** throughout DENT; `validate.py` fails on any id that isn't a real guide and checks the vendored copy's integrity and version pin.
- **Gate G13 (Modern Web Guidance)** in SKILL.md, PLAN/REVIEW templates, verification, plan audit, scorecard and close-out (including MWG's `### Modern Web Guidance` disclosure). Decision Log sources gain `MWG <guide-id>`; DESIGN.md gains a "Web platform" section.
- **`skills/dent/scripts/mwg.py`**: offline search/retrieve/list over the bundled guides (same output shape as the CLI) for sandboxes without Node or network.
- **`verify_page.py` G13 checks**: fails on a global `*` reduced-motion reset, a lazy-loaded LCP image, `fetchpriority="high"` with `loading="lazy"`, `role="dialog"`/`aria-modal` re-added to a native `<dialog>`, and one-time codes split across inputs; warns on an LCP image without `fetchpriority="high"`, too many high-priority images, custom ARIA dialogs and dark-mode CSS without `color-scheme`. New fixture cases in `evals/fixtures/` (+ `lcp.png`) and `test_tools.py` assertions.
- `dist/modern-web-guidance.zip` release asset; `dent.zip` now carries MWG under `vendor/modern-web-guidance/`. Both installers copy MWG next to DENT (never overwriting a separately installed official copy) and add it to the rules-file snippet.

### Changed (conflicts with MWG resolved in MWG's favour)
- **Reduced motion:** the global `*{animation-duration:.01ms!important}` reset (in `design-tokens-and-code.md` and `modern-layer.md`) is replaced by per-rule handling: opt in under `no-preference`, or soften parameters under `reduce`. Running the new G13 on the 2.2 benchmark pages shows this snippet had propagated into DENT's builds; the published results are left as recorded.
- **Base CSS:** element-scoped, zero-specificity resets in a cascade layer instead of rules on `*`; type in `rem`, `min-block-size` instead of fixed control heights, `dvh` for mobile full-height.
- **Dialogs and drawers:** native `<dialog>` + `showModal()` without `role="dialog"`, `aria-modal`, hand-made focus traps or `overflow: hidden` scroll locks; mobile menus per `mwg:navigation-drawer`.
- **Component patterns:** switch → `<input type="checkbox" switch>`; tooltip → `popover="hint"` + `interestfor` + anchor positioning; accordion → `<details>` + `::details-content` + `interpolate-size`; tabs without `aria-controls`; styled native `<select>`; toasts must not be the only home of an action.
- **One-time codes:** one input with `autocomplete="one-time-code"` (styled as boxes if wanted) instead of six auto-advancing inputs; password rules shown as a checklist, errors only after leaving the field.
- **Libraries:** native platform first (`component-selection.md`, catalogue defaults, `design-tokens-and-code.md`, app recipe); Floating UI only where anchor positioning can't help; animation libraries only for choreography the platform can't express.
- **Fluid type:** `clamp()` maxima capped at 2.5× the minimum (hero statements, wordmarks, Swiss and Kinetic Typography styles) so zoom still reaches 200%.
- **Performance and theming:** never lazy-load the LCP image and give it `fetchpriority="high"`; `font-size-adjust` for stable fallbacks; dark mode via `color-scheme` + `light-dark()` with a toggle that stores only real overrides.
- **Motion catalogue:** scroll-driven animations and view transitions updated to current Baseline data (from MWG); Lenis demoted behind native `scroll-behavior`.
- `verify_page.py` G10 no longer fails essential progress indicators that keep a slowed loop under reduced motion (MWG's "adjust parameters" strategy).
- **Landing page (`site/`) brought in line with MWG** (G13 now passes with no warnings): per-rule reduced motion instead of the global reset; the mobile menu is a native modal `<dialog>` with `command`/`commandfor` (fixes a real bug: the old panel was `position: fixed` inside the blurred header, so it collapsed to one row); element-scoped resets, type in `rem`, no `aria-controls` on tabs, forced-colors tab indicator, `color-scheme` follows the theme toggle, which stores an override only when it differs from the system; the terminal cursor stops within 5 s.
- **Discoverability:** keyword-bearing `<title>` and description, `robots` preview hints, WebSite/Person/SoftwareApplication/FAQPage structured data (FAQ generated from the visible answers), `site/llms.txt` for AI assistants, fresh sitemap date; README gains a text H1 and a link to the website.
- Every generated command carries the MWG rule; `/dent:audit`, `/dent:verify`, `/dent:review`, `/dent:accessibility`, `/dent:components`, `/dent:responsive`, `/dent:motion` and `/dent:motion-graphics` gained MWG steps. The router (SKILL.md §0) adds "Web code? Modern Web Guidance first".

## [2.2.0] — 2026-11-15

### Added
- **Motion menu** (`references/motion/motion-menu.md`): DENT now **asks which kinds of motion you want** (page load & hero entrance, scroll, hover, micro-interactions, page/view transitions, text, data & numbers, layout, background & ambient, cursor & pointer, illustration & SVG, loading & feedback, 3D & depth, gestures, or "You choose") and **how strong** (Subtle, Balanced, Expressive, Cinematic). Includes a 4-options-per-question flow for agents whose question tool is limited, a catalogue of concrete effects per kind, recommended sets by product type, and an M-ID motion plan.
- **Minimum motion per effort level** (motion floor): e.g. Standard landing pages need a hero entrance, varied scroll reveals, one scroll-linked moment, hover on every interactive element and micro-interactions.
- **Motion inventory** in `verify_page.py`: counts keyframes, transitions, hover rules (and whether they are pointer-guarded), scroll-driven animations, view transitions, SVG animations, reduced-motion queries and motion libraries, and warns when a page looks under-animated. Covered by `scripts/test_tools.py`.

- **`/dent:update`** + `skills/dent/scripts/update_plugin.py`: update the plugin without reinstalling. It refreshes DENT's local marketplace copy from GitHub (a known gap: third-party marketplaces don't auto-update by default and can go stale), reports installed vs available version, and gives the one remaining step. `docs/INSTALL.md` has a full Updating section (auto-update setting included).
- **Fixes from the Opus 5.5 test runs:** question menus respect the 4-option limit of Claude's question tool (the effort question had 5); a prompt that merely mentions a benchmark is no longer treated as non-interactive; `SCORECARD.md` is written to the project at Standard+; every delivery ends by asking for approval to write DESIGN.md; verification notes for frozen animations in agent browser panes, `file://` CORS and missing WebGL; plugin command wrappers say where to find SKILL.md if it isn't loaded.
- `verify_page.py` warns when hover rules aren't restricted to mouse/trackpad devices (they stick after a tap on phones).

### Changed
- `/dent:motion` rewritten: ask kinds + intensity, plan every item, build all of them, verify planned vs built. `/dent:create`, `/dent:polish`, `/dent:motion-graphics`, the router, the question list, both recipes and the "don't ask" defaults now include the motion question and floor.
- Gate G10 now requires every planned motion item to be built and the effort-level floor to be met.
- "Restraint" redefined as purpose and quality, not absence; under-animation added to the anti-slop detector.

## [2.1.0] — 2026-11-15

### Added
- **Benchmark batch: 8 tests with Claude Code + Claude Opus 5.5 (medium)**, built with and without DENT 2.0: Brewlog site, SaaS dashboard, checkout, kanban app, scroll-story launch page, meditation timer with sound, 3D product viewer, 45 s launch video. Per-test `RESULT.md` with screenshots, live pages, `verify_page.py` output and scores; `benchmark/RESULTS-SUMMARY.md` (read by the landing-page prompt); the run's `DEVIATIONS` file. Average 37.9 → 43.8 / 50; all 7 DENT web builds pass every automated gate while all 7 without DENT fail at least one; one build without DENT invented reviews. Scores are by Claude Opus 5.5 (same model family, DENT's author), so they are not independent.
- **Font priority** (`references/typography.md` §0): Satoshi-style modern grotesks first (Satoshi, General Sans, Switzer, Supreme, Cabinet Grotesk, Clash Display, Geist, Manrope, Onest, Figtree, Hanken Grotesk, Instrument Sans…), characterful serif and display partners (Gambetta, Zodiak, Erode, Sentient, Boska, Panchang, Instrument Serif, Fraunces…), and overused defaults (Inter-only, Roboto, Open Sans, Montserrat, Poppins, Playfair Display) demoted to deliberate, logged choices.
- **20 new pairings** (`typography.md` §3) and a rewritten hero pairing matrix.
- **Font licence rules** from the actual ITF Free Font License text: Fontshare fonts are free for commercial use and self-hosting, but must not be subset, converted or redistributed (no committing them to public repos; use the Fontshare API there).

### Changed
- Style files and directions now default to Satoshi / General Sans / Switzer instead of Inter; SKILL.md §1.4 points to the font priority.
- Subsetting advice now applies to OFL fonts only.
- The scroll-story benchmark copy loads Satoshi from Fontshare's API instead of committed font files (licence compliance; documented in its RESULT.md).

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

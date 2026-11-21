# DENT Intelligence Upgrade: Specification (v2.5)

**Type:** implementation specification, rewritten against the actual repository.
**Replaces:** the generic draft `DENT_Intelligence_Upgrade_Specification.md`, kept verbatim as `docs/dent-3/DRAFT-original.md`; its sound parts are carried into §2 and §3.
**Audience:** the agent and the maintainer working on this repository.
**Status:** implemented in DENT 2.5.0. Verification evidence: `docs/dent-3/VERIFICATION.md`.

---

## 1. Why the draft was rewritten

The draft's goals were right (understand before acting, decide deliberately, verify with evidence, report honestly), but implementing it literally would have rebuilt what DENT 2.0–2.4 already does and missed what users actually hit:

- **About 70 % already existed.** Confirmed / Assumed / Unknown facts, depth levels, `PLAN.md` with a plan audit, gates G1–G13, Passed / Failed / Not run / Blocked / N/A reporting, `DESIGN.md` as the source of truth, with/without-DENT benchmarks and the no-claims-without-evidence rule were built from `improvement.md` in DENT 2.0 (`docs/dent-2/`).
- **It ignored the repository's own rules:** Modern Web Guidance (MWG) is the web-implementation authority, commands are generated from `scripts/build_commands.py`, `python scripts/validate.py` must print `OK`, and versions are bumped in three places together (`AGENTS.md`).
- **It missed the real defects** that users reported: "go all out" not running motion, robotic narration, no choice of model or provider, fixed style presets, no collaborative brainstorming, and a palette/font library that had itself become the new AI look.
- **Formatting was broken:** a pandoc conversion merged bullet lists into paragraphs ("establish: - Known facts: … -") and used grid tables.

## 2. Status of the draft's requirements

| Draft section | Requirement | Status before 2.5 | 2.5 action | Where |
|---|---|---|---|---|
| §2 | Repository-first audit | Existed (`docs/dent-2/PLAN.md` audit) | Re-audited for 2.5 (§4) | This file |
| §3.1 | Context and decision engine, Confirmed/Assumed/Unknown, depth/effort selection | Existed | Kept; All-out capability list added | `SKILL.md` §1.0–1.1, `references/workflow/all-out.md` §0 |
| §3.2 | Product and UX intelligence | Existed | Kept | `references/research-and-information-architecture.md`, `page-and-flow-patterns.md`, recipes |
| §3.3 | Design intelligence beyond presets | Partial: styles applied as templates; fixed font/palette favourites | **New:** style moves (apply/bend/blend/leave), style cards, concept palettes, font voices, overuse registries | `references/creative-direction.md` §3b, `color.md` §11–14, `typography.md` §0–3 |
| §3.4 | Frontend engineering, dependency justification | Partial: selection guide, no explicit checklist | **New:** dependency checklist | `references/catalog/component-selection.md` §4b |
| §3.5 | Visual and functional verification | Existed (`verify_page.py`, verification.md) | Kept | `references/workflow/verification.md` |
| §3.6 | Three independent evaluators that can reject | Missing (self-score only) | **New** | `references/workflow/scoring-and-closeout.md` §3b, `/dent:review`, `templates/REVIEW.md` |
| §4–5 | Component, platform, motion intelligence | Existed | Kept | catalog, motion references |
| §6 | Persistent project intelligence | Existed (`DESIGN.md`) | Kept; brainstorm brief and media choices recorded there | `references/design-md-template.md` |
| §7 | End-to-end workflow | Existed | Kept | `SKILL.md` §0–§8 |
| §8 | Quality gates and severity; blockers stay visible | Gates existed; severity partial; blockers could be averaged | **New:** severity scale, open Blocker caps overall at 6 and is listed first | `scoring-and-closeout.md` §2, §6; `templates/SCORECARD.md` |
| §9 | Benchmarks; compare versions | With/without DENT existed | **New:** previous-version vs current condition | `evals/protocol.md` |
| §10–12 | Reference architecture, safety, staged implementation | Existed (`AGENTS.md`, `validate.py`) | New consistency checks in `validate.py` | `scripts/validate.py` `check_capabilities` |
| §13 | Final deliverables | — | This file + `VERIFICATION.md` + `CHANGELOG.md` | `docs/dent-3/` |

## 3. New requirements (from the maintainer, 2026-11-21)

| ID | Requirement | Acceptance criteria |
|---|---|---|
| N1 | "Go all out" includes everything or asks about anything omitted | All-out fills a capability list; motion, surfaces, type, copy, assets, directions and review run as their own commands; sound, voice, video, 3D and brand are offered in one question; every row ends Included / Declined / N/A with a reason. `validate.py` fails if a pipeline or example drops motion again |
| N2 | Audit for similar gaps and inconsistencies | Gap list in §4 fixed; regression checks added |
| N3 | Near-human narration with local models | Multiple engines (Qwen3-TTS, Kitten TTS 2, Chatterbox, Voxtral, Kokoro, Piper, system, OpenAI, ElevenLabs, any OpenAI-compatible endpoint, any other provider via an adapter); install only after the user agrees; per-engine guidance for the agent; mastering to a loudness target with captions; blind A/B |
| N4 | Ask local / free cloud / paid / unlisted provider / own assets for every media type | One protocol for voice, music, SFX, images, illustration, video, 3D, fonts, clean-up; unlisted providers researched from official sources; "find me a free one" handled; keys only via environment variables |
| N5 | Adaptive design intelligence | Styles can be applied, bent, blended or left with a style card; DENT proposes alternatives with reasons; no house fonts or palettes |
| N6 | Fonts and palettes upgraded after research | Overused registries (first and second order) enforced by tools; 25 new pairings and 13 type voices from verified OFL faces; 20 concept palettes generated and contrast-verified in both themes; generators for new ones |
| N7 | `brainstorm` command | Candid partner: steelmans, pushes back with labelled reasons (rule / evidence / taste), changes its mind only on new information, respects the user's decision, ends in a direction brief |
| N8 | Fill remaining gaps | `doctor` command; independent evaluators; visible blockers; dependency checklist; command-generator fixes |
| N9 | Test end to end | Validator, tool regression tests, real renders with installed engines, end-to-end runs of the main flows; results recorded honestly |

## 4. Audit findings fixed in 2.5 (gaps and bugs)

| # | Finding | Impact | Fix |
|---|---|---|---|
| A1 | The worked All-out example in `orchestration.md` built a landing page without `motion` or `surfaces`; agents copied it | High | Example rewritten; All-out expands every pipeline; validator guard |
| A2 | The All-out sweep's motion line was weaker than the All-out motion floor | High | Sweep points to `/dent:motion` and the floor |
| A3 | `create` only *asked* about motion; it never ran `commands/motion.md` or `commands/surfaces.md` | High | Steps run both; validator guard |
| A4 | Redesign pipeline had no surfaces or motion step | Medium | Added at Standard+ |
| A5 | Media commands asked only "do you have generative access?" | High | Sourcing question per media type (N4) |
| A6 | Narration defaulted to engines that sound synthetic (Piper in the launch-video benchmark) | High | Multi-engine `tts.py`, Qwen3-TTS first when the GPU allows |
| A7 | Font priority put Satoshi/Cabinet/Clash first; style files repeated them (49 mentions); palettes matched the cream + terracotta "tasteful AI" look exactly | High | No house font; registries; tools; style starter tokens swapped; library replaced |
| A8 | `SKILL.md` decision-log example cited a palette that no longer existed | Low | Updated |
| A9 | Command generator put annotations inside the backticked path (`` `file.md (the router…)` ``) | Low | `load_line` keeps only the path in backticks |
| A10 | Non-building commands (`update`, new `brainstorm`, `doctor`) ended with "close with the scorecard" | Low | Per-command close lines |
| A11 | Self-score could average away a blocker | Medium | Open Blocker caps overall at 6, listed first |
| A12 | No check that capabilities promised in one file are triggered in another | Medium | `validate.py` `check_capabilities` |
| A13 | Minimal's starter accent was within Tailwind blue-600's range; Editorial's paper + red tripped the cream + terracotta detector | Low | Starter tokens replaced |

## 5. Architecture decisions

1. **No new top-level skill.** Media sourcing, brainstorming and the tools are part of DENT; a second skill would split routing and `DESIGN.md`. The vendored Modern Web Guidance skill stays untouched.
2. **Tools over lists.** Lists of "good fonts" and "good palettes" go stale and become the next cliché. `fonts.py` reads Google Fonts' own popularity ranks and dates (snapshot + `refresh`); `palette.py` builds palettes from a concept seed and flags clichés. The libraries in `typography.md` and `color.md` are starting points generated or verified by those tools.
3. **One environment per TTS engine.** Their PyTorch/Transformers pins conflict; `tts.py` re-runs itself inside the engine's environment. Installing always needs the user's yes (`--yes`).
4. **Unknown providers through a file contract.** Any provider works if an adapter writes `line_001.wav` + `line_001.txt`…; `tts.py post` does the rest. DENT never handles secrets beyond reading environment variables.
5. **Independent evaluators where the agent can start subagents**, sequential checklists otherwise, labelled "not independent".

## 6. Traceability

| Requirement | Implementation | Verification | Status |
|---|---|---|---|
| N1 All-out completeness | `references/workflow/all-out.md` §0, §3; `orchestration.md` Step 3 and example 3; `commands/create.md`, `redesign.md`, `dent.md` | `validate.py` `check_capabilities`; E2E run "go all out" (`VERIFICATION.md`) | See VERIFICATION.md |
| N3 Narration | `skills/dent/scripts/tts.py`; `references/audio/voice-and-narration.md` §1, §5; `commands/voice.md` | `scripts/test_tools.py` (post/captions/loudness); real renders with qwen3, kitten2, chatterbox, kokoro, system | See VERIFICATION.md |
| N4 Media sourcing | `references/media-sourcing.md`; all media commands; `video-tools-and-pipeline.md` §1 | `validate.py` (every media command references it; catalogue rows have link + status) | See VERIFICATION.md |
| N5 Adaptive design | `references/creative-direction.md` §3b; `styles/_styles-index.md`; `SKILL.md` §1.4, §9.1, G8 | E2E direction run | See VERIFICATION.md |
| N6 Fonts and palettes | `scripts/fonts.py`, `scripts/data/google-fonts.json`, `scripts/palette.py`; `typography.md` §0–3, §9; `color.md` §11–14; style starter tokens | `test_tools.py` (cliché detection, contrast of every library palette, overuse flags); `validate.py` (style starter fonts) | See VERIFICATION.md |
| N7 Brainstorm | `references/workflow/brainstorm.md`; `commands/brainstorm.md`; router rows | E2E pushback scenario | See VERIFICATION.md |
| N8 Doctor, evaluators, blockers, dependencies | `scripts/doctor.py`, `commands/doctor.md`; `scoring-and-closeout.md` §3b, §6; `templates/SCORECARD.md`, `REVIEW.md`; `component-selection.md` §4b | `test_tools.py` (doctor runs); E2E review run | See VERIFICATION.md |

## 7. Known limitations

- Cloud adapters (OpenAI, ElevenLabs, `http`) are implemented against the providers' documented APIs but were **not run** (no keys in the test environment).
- Voxtral TTS was not run locally (4B model; non-commercial weights); it is supported through the `http` engine or Mistral's API.
- Font and provider facts marked **K** are from knowledge and must be re-checked before commercial recommendations; Google Fonts licences in `typography.md` were verified against github.com/google/fonts on 2026-11-21.
- Voice quality is judged by listening. DENT's ordering (Qwen3-TTS first) reflects one test machine and one script; the blind A/B step exists because preference varies.

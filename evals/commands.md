# Command and Orchestration Tests

## 1. Automated (run on every change)
`python scripts/validate.py` checks: every `skills/dent/commands/<name>.md` has a Claude Code wrapper `commands/<name>.md` and a row in SKILL.md §4; every reference in every command resolves; the router (`references/workflow/orchestration.md`) mentions every command. `python scripts/test_tools.py` checks the verification tool against known-good and known-bad fixtures.

## 2. Discovery (manual, per agent)
| Agent | Test | Pass when |
|---|---|---|
| Claude Code (plugin) | Type `/dent:` | All 34 commands listed with descriptions |
| Claude Code (manual skill) | `/dent plan a pricing page` | Skill loads and follows `commands/plan.md` |
| Codex / Cursor / Copilot / Gemini CLI | `dent audit this page` (with a file) | Skill triggers; follows `commands/audit.md` steps |

## 3. Routing: plain `/dent` must pick the right pipeline
For each prompt, the first reply must state the classification/plan line and the first question (or start, if no question is needed).

| Prompt | Expected main command → pipeline |
|---|---|
| `/dent make a landing page for my meditation app` | create → (directions if Polished+) → motion → verify → score; asks effort first |
| `/dent go all out on a landing page` | All-out capability list shown; create → type/copy → surfaces → motion (full menu) → motion-graphics → assets → review (3 evaluators) → verify → score → improve |
| `/dent let's brainstorm the look of my app` | brainstorm (no build); ends with a direction brief |
| `/dent add a voice-over to the demo video` | doctor → voice (sourcing question, A/B, tts.py) → verify |
| `/dent which voice models can I use here?` | doctor |
| `/dent this dashboard looks bad on my phone` (+ screenshot) | responsive (+ verify); no effort question |
| `/dent is this accessible?` (+ URL) | accessibility as audit (findings first, offer fixes) |
| `/dent which table library should I use?` (Vue project) | components; Vue-compatible options with licences |
| `/dent add sound to my app` | sound; opt-in default confirmed; few meaningful events |
| `/dent go all out: landing page + launch video with voice-over` | two pipelines, All-out protocol, shared DESIGN.md; asks about generative access and voice |
| `/dent improve it` (after a scorecard) | improve; (no scorecard yet → score first) |
| `/dent the submit button does nothing` | fix → verify |
| `/dent the tooltips and scrollbars look like Windows defaults` | surfaces (+ verify); fixes those and checks sibling surfaces; asks the Match/Tint/Native level only if unknown |
| `/dent how would you redesign our settings?` | plan (no building) |
| `/dent make a 30 second trailer for our game` | video (trailer) → sound → verify |

## 4. Per-command behaviour (first reply)
| Command | Test prompt | First reply must… |
|---|---|---|
| plan | `/dent:plan onboarding for a budgeting app` | Gather facts, ask only unknowns, then show PLAN.md + audit table; no code |
| create | `/dent:create portfolio site for a ceramicist` | Ask effort first (with skip option) |
| redesign | `/dent:redesign` (+ app) | Inventory/baseline before proposing |
| extend | `/dent:extend add billing page` | Read DESIGN.md / detect system first |
| implement | `/dent:implement PLAN.md` | Check plan assumptions vs repo |
| fix | `/dent:fix text clipped in hero on mobile` | Reproduce/root cause before changing |
| polish | `/dent:polish` (+ page) | Score first, then prioritised refinements |
| audit | `/dent:audit` (+ screenshot) | Findings table with severity; no changes |
| review | `/dent:review` | Run checks; verified vs subjective split |
| verify | `/dent:verify index.html` | Run verify_page.py (or state why not) and report gates |
| responsive | `/dent:responsive` | Screenshots at 6 widths; overflow first |
| accessibility | `/dent:accessibility` | Automated + manual list; criteria checked |
| system | `/dent:system` | Inventory + classification |
| components | `/dent:components rich text editor for Next.js` | Detect stack; compare 2–3 with licences |
| surfaces | `/dent:surfaces` (on a page with native checkboxes and `title` tooltips) | Lists the built-in surfaces present, asks Match / Tint / Native (Match recommended), names the MWG guide per surface |
| directions | `/dent:directions for a fintech app` | Name the cliché; 2–4 different directions |
| type | `/dent:type hero for "Ship faster"` | Role + technique + faces with licence |
| copy | `/dent:copy pricing page` | Voice words; specific copy; no slop phrases |
| brand | `/dent:brand coffee subscription` | Concept + cliché check before logo ideas |
| assets | `/dent:assets OG image + favicon` | Sizes + licence table |
| motion | `/dent:motion` | Interaction map with reduced-motion column |
| motion-graphics | `/dent:motion-graphics logo reveal` | Ask destination/length/sound/dimension; concept + storyboard |
| 3d | `/dent:3d product viewer` | Justify 3D vs alternatives; budgets + fallback |
| sound | `/dent:sound` | Role + silence policy + opt-in |
| voice | `/dent:voice narration for a 60s explainer` | Ask voice type/service; script for the ear |
| video | `/dent:video explainer` | Ask type/platform/length and generative access |
| launch-video | `/dent:launch-video` | Ask launch sub-type (teaser/reveal/tour/manifesto) |
| score | `/dent:score` | Requirement lines first, evidence, caps applied |
| improve | `/dent:improve` | Top-3 fixes applied, before → after |
| handoff | `/dent:handoff` | DESIGN.md + licences + a11y annotations |

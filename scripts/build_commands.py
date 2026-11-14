#!/usr/bin/env python3
"""Generate DENT command files from one definition list.

Writes:
  skills/dent/commands/<name>.md   source of truth (travels with every install)
  commands/<name>.md               thin Claude Code plugin wrappers (/dent:<name>)

Edit COMMANDS below, then run: python scripts/build_commands.py
Copyright 2026 Jeel Nada (solarquack). Licensed under the Apache License 2.0.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_CMDS = ROOT / "skills" / "dent" / "commands"
PLUGIN_CMDS = ROOT / "commands"

# name, summary, argument hint, depth default, references to load, steps, output, never
COMMANDS = [
    ("dent", "The main entry point: understand any design, front-end or media request, pick the right sub-commands, chain them and deliver the best result.", "<anything you want designed, built, fixed, reviewed or produced>",
     "decided by the router",
     ["references/workflow/orchestration.md (the router: follow it step by step)", "SKILL.md §1.0 and §3 (already loaded)"],
     ["Fill the signal card from orchestration.md Step 1 (deliverable, state, verb, media, effort, risk, constraints).",
      "Map the signals to a main command + companions with the table in Step 2. Several deliverables → one pipeline each.",
      "Expand into the default pipeline for each deliverable (Step 3) and tell the user the plan in one line.",
      "Ask only the questions the pipeline needs, one at a time, effort first (Step 4).",
      "Run each sub-command's file (`commands/<name>.md`) in order, carrying the direction, DESIGN.md and Decision Log forward (Step 5).",
      "If the effort is All-out, also run `references/workflow/all-out.md` for every deliverable.",
      "Finish with one close-out: gates, scorecard per deliverable, attribution, next step (Step 6)."],
     "Whatever the pipeline produces, plus the gate results, scorecard(s), attribution and a one-line next step.",
     ["Answer with generic advice when the user wanted something built.", "Skip verify/score because the user only typed /dent.", "Load every reference \"just in case\"."]),

    ("plan", "Inspect the context and produce an audited PLAN.md without building anything.", "<goal or feature>",
     "Advanced (or Critical if risky)",
     ["references/workflow/planning-and-plan-audit.md", "templates/PLAN.md", "references/modes-existing-products.md (if a codebase exists)", "references/creative-direction.md (for new or redesigned UI)"],
     ["Gather Confirmed / Assumed / Unknown facts; inspect the repository if there is one.",
      "Ask only about Unknowns that change correctness, risk or direction (one question at a time).",
      "Fill templates/PLAN.md: requirements with IDs and observable acceptance criteria, direction, technical strategy, states, phases, verification per requirement, risks, definition of done.",
      "Audit the plan (planning file §4). Fix every Blocker and Major and show the audit table.",
      "Present a short summary: goal, direction, scope, risks, open questions."],
     "PLAN.md (written to the project, or printed) + plan-audit table + open questions. No implementation.",
     ["Start building unless the user explicitly says so.", "Add Must requirements the user never asked for."]),

    ("create", "Create a new product, page, site or interface from scratch.", "<what to create>",
     "Standard or Advanced",
     ["references/workflow-questions-and-effort.md", "references/creative-direction.md", "references/creative/directions-library.md",
      "references/recipes/landing-page.md or references/recipes/app-and-dashboard.md", "references/foundations-and-components.md", "references/workflow/verification.md"],
     ["Ask the effort level first, then only missing essentials (or decide everything if told to). At Standard+ always include the motion questions from references/motion/motion-menu.md §1 (multi-select kinds + intensity) unless the user said no motion.",
      "Plan (inline for Standard, PLAN.md for Advanced) and audit it.",
      "Direction: concept sentence, category-cliché check, one base style + ≤1 accent, signature element, hero type move.",
      "Follow the recipe step by step, including every gate inside it.",
      "Build tokens → components → screens → modern layer → media.",
      "Verify (verify_page.py when a browser is available), fix, then score and close out."],
     "Working files, Decision Log, gate results, scorecard, attribution; DESIGN.md after approval.",
     ["Invent stats, testimonials, logos or ratings.", "Combine more than one base style and one accent."]),

    ("redesign", "Redesign an existing product while preserving the behaviour users rely on.", "<product or screens>",
     "Advanced",
     ["references/modes-existing-products.md §3", "references/workflow/execution-and-scope.md", "references/workflow/planning-and-plan-audit.md", "references/workflow/verification.md §8"],
     ["Inventory screens, flows, components and drift; screenshot the current version as a baseline.",
      "List what must stay (navigation, terminology, key positions, features) and ask what is sacred.",
      "Plan the redesign + migration (incremental by default) and audit it.",
      "Build in phases; never drop a feature because it wasn't in the screenshot you were given.",
      "Compare before/after per screen; classify every difference."],
     "Before/after comparison with reasons, migration plan, updated DESIGN.md, regression results.",
     ["Remove existing features silently.", "Introduce a second design system."]),

    ("extend", "Add a feature or screen that fits the existing product and design system.", "<feature>",
     "Standard",
     ["DESIGN.md (project)", "references/workflow/execution-and-scope.md §1–2", "references/modes-existing-products.md §2"],
     ["Read DESIGN.md and inspect existing components/tokens.",
      "Find the integration points and the screens that share components.",
      "Build the feature with existing tokens/components; add new ones only in the existing convention.",
      "Verify the new feature and the neighbouring screens; update DESIGN.md changelog."],
     "The feature, verification results, DESIGN.md changelog line.",
     ["Redesign unrelated parts.", "Add a new library for something an existing one already does."]),

    ("implement", "Implement an approved PLAN.md or DESIGN.md accurately.", "<path to PLAN.md or DESIGN.md>",
     "As in the plan",
     ["the plan/spec itself", "references/design-tokens-and-code.md Part 2", "references/workflow/execution-and-scope.md", "references/workflow/verification.md"],
     ["Read the plan/spec fully. Check the repository still matches its assumptions; list stale ones.",
      "If anything material changed, update the plan and re-audit before building.",
      "Implement phase by phase; tokens first; update the traceability matrix as you go.",
      "Verify every requirement against its acceptance criterion; record deviations."],
     "Implementation + traceability matrix with statuses + verification report.",
     ["Mark a requirement Verified because the code exists."]),

    ("fix", "Diagnose and fix one specific UI/UX problem with the smallest correct change.", "<the problem>",
     "Quick (Critical if risky area)",
     ["references/workflow/verification.md", "references/foundations-and-components.md (if a component is involved)"],
     ["Reproduce or precisely understand the problem (screenshot, steps, viewport).",
      "Find the root cause, not the symptom.",
      "Make the smallest correct fix using existing tokens/components.",
      "Verify the fix and nearby regressions (other screens using the same component)."],
     "Cause, fix, before/after evidence, what else was checked.",
     ["Refactor unrelated code while you're there."]),

    ("polish", "Refine a working interface: hierarchy, spacing, type, details, interactions. No redesign.", "<screen or area>",
     "Standard",
     ["references/quality-review.md Part 2", "references/modern-layer.md", "references/creative/hero-typography.md", "references/creative/anti-slop.md"],
     ["Score the current state (scorecard) to find the weakest lines.",
      "Fix in order of impact: hierarchy → spacing rhythm → typography craft → color/surfaces → states → motion (check it meets references/motion/motion-menu.md §2 for the effort level; ask which kinds the user wants if unclear) → optical details.",
      "Keep the information architecture and direction unless a change is justified and logged.",
      "Re-score with evidence."],
     "Before/after screenshots, change list with reasons, new score.",
     ["Change the brand, IA or features without asking."]),

    ("audit", "Audit an existing interface, codebase or screenshot and report findings. Change nothing.", "<URL, screenshot or path>",
     "Standard",
     ["references/modes-existing-products.md §4", "templates/AUDIT.md", "references/quality-review.md", "references/accessibility.md"],
     ["Establish scope, goal and main user task.",
      "Look first: render/screenshot, run verify_page.py and drift measures when possible.",
      "Evaluate: task success, heuristics, [Rule] failures, hierarchy, consistency, content, deceptive patterns, distinctiveness.",
      "Write findings with evidence, severity, impact, recommendation and effort; separate verified defects from opinions."],
     "templates/AUDIT.md filled in; offer to fix the top items in one line.",
     ["Silently redesign or fix things.", "Give vague feedback without evidence."]),

    ("review", "Deep review of a result: visual quality, UX, accessibility, responsiveness, function, consistency, performance.", "<what to review>",
     "Standard",
     ["references/workflow/verification.md", "references/quality-review.md", "templates/REVIEW.md", "references/creative/anti-slop.md"],
     ["Run the automated pass and look at every screenshot.",
      "Walk the main user journey; trigger states; tab through.",
      "Check gates G1–G12 that apply.",
      "Prioritise issues by severity; mark each as verified defect or subjective recommendation."],
     "templates/REVIEW.md + prioritised issue list.",
     ["Report checks you didn't run as passed."]),

    ("verify", "Run the verification suite on built work and report results honestly.", "<page, URL or build>",
     "Standard",
     ["references/workflow/verification.md", "templates/REVIEW.md", "scripts/verify_page.py", "scripts/contrast.py"],
     ["Find available tools; say which checks can and cannot run.",
      "Run `python scripts/verify_page.py <target> --out <dir>` and `scripts/contrast.py` on token pairs.",
      "Open the screenshots and inspect them; do functional checks for what is in scope.",
      "Record every gate as Passed / Failed / Not run / Blocked / N/A with evidence."],
     "Verification report with evidence and the screenshots' paths.",
     ["Fix things during verify unless asked (report first)."]),

    ("responsive", "Make layout and interaction work at every size, designed rather than shrunk.", "<page or screens>",
     "Standard",
     ["references/platforms-and-devices.md §3", "references/workflow/verification.md §4", "references/foundations-and-components.md §3 (grid)"],
     ["Screenshot at 320, 375, 390, 768, 1024, 1440 and any breakpoint in between.",
      "Fix overflow first (header actions, wide tables, fixed widths, long words, 100vw elements).",
      "Re-compose for small screens: simplify mockups, stack with intent, sticky primary action, readable type.",
      "Check touch targets, hover-only actions, safe areas, landscape."],
     "Fixed layout + screenshots per width + overflow report.",
     ["Just scale the desktop layout down."]),

    ("accessibility", "Focused accessibility audit and remediation (WCAG 2.2 AA).", "<page or app>",
     "Standard",
     ["references/accessibility.md", "references/workflow/verification.md §5", "scripts/verify_page.py"],
     ["Run automated checks (verify script, axe if available).",
      "Manually check landmarks, headings, names/labels, keyboard path, focus, dialogs, errors, contrast (all themes), targets, zoom/reflow, reduced motion, media alternatives.",
      "Fix barriers that block task completion first; prefer native semantics over ARIA.",
      "Re-verify every fix; list criteria actually checked."],
     "Findings + fixes + which criteria were checked and how.",
     ["Claim full compliance from an automated scan."]),

    ("system", "Inventory, create or extend a design system (tokens, components, docs).", "<scope>",
     "Advanced",
     ["references/workflow/execution-and-scope.md §1–2", "references/design-tokens-and-code.md", "references/foundations-and-components.md", "references/tooling-and-handoff.md §3"],
     ["Inventory foundations, components, behaviour and implementation; classify findings (Healthy, Inconsistent, Missing, Outdated, Conflicting, Intentional exception).",
      "Propose one coherent system that reuses healthy parts; three-tier tokens.",
      "Implement tokens and components; document each component (purpose, anatomy, variants, states, a11y, content).",
      "Verify with a component sheet (every component in every state)."],
     "Inventory table, token files, component specs, component sheet.",
     ["Create a parallel system next to an existing one."]),

    ("components", "Choose, install and customise the right component/UI libraries for this project.", "<need, e.g. data table + command palette>",
     "Standard",
     ["references/catalog/component-selection.md", "references/catalog/components-primitives-and-systems.md", "references/catalog/components-collections-and-specialized.md"],
     ["Detect framework, language, styling, existing libraries.",
      "List functional needs and the visual direction.",
      "Shortlist 2–3 options per need from the catalogue; compare compatibility, accessibility, customisation, performance, licence, maintenance, design fit.",
      "Recommend one per job with trade-offs; check the licence from the official source.",
      "Install, theme to DESIGN.md tokens, and verify keyboard/a11y behaviour."],
     "Comparison table, recommendation with reasons, install + integration, verification.",
     ["Pick by popularity.", "Install two libraries that do the same job."]),

    ("directions", "Explore 2–4 genuinely different creative directions before committing.", "<product>",
     "Standard",
     ["references/creative-direction.md", "references/creative/directions-library.md", "references/creative/hero-typography.md", "references/styles/_styles-index.md"],
     ["Write the category cliché for this product.",
      "Pick 2–4 directions that differ on at least 3 axes (type, color, layout, imagery, motion, sound).",
      "For each: name, concept sentence, palette swatches, type sample, hero composition, motion and sound idea, fits/risks.",
      "Render a style tile per direction when HTML can be shown; recommend one."],
     "Directions side by side with a recommendation; chosen one goes to the Decision Log.",
     ["Offer three shades of the same idea."]),

    ("type", "Design hero titles and expressive typography (custom type compositions).", "<headline or page>",
     "Standard",
     ["references/creative/hero-typography.md", "references/typography.md", "references/modern-layer.md §7.1"],
     ["Pick the type role: wordmark-scale, editorial, kinetic, typographic system, data-type.",
      "Choose faces (licence checked) and a composition technique from hero-typography.md.",
      "Build it fluid (clamp with rem), accessible (real text, not images), balanced wraps, reduced-motion safe.",
      "Check it at 320 px and 1440 px; no overflow, no clipped letters."],
     "The type composition in code + specimen + reasoning.",
     ["Put essential text in images or canvas only."]),

    ("copy", "Write or fix UX copy: headlines, CTAs, microcopy, errors, empty states.", "<screen or flow>",
     "Quick/Standard",
     ["references/ux-writing.md", "references/creative/anti-slop.md §4"],
     ["Find the voice (3 words) and the reader's job.",
      "Write specific, front-loaded copy; one term per concept; verbs on buttons.",
      "Replace generic marketing phrases with concrete outcomes; no invented numbers.",
      "Proofread twice (gate G7)."],
     "Copy deck (location → text) with notes.",
     ["Use 'Unlock', 'Seamless', 'Supercharge' or invented stats."]),

    ("brand", "Create a mini brand / identity direction (logo direction, color, type, voice, sonic cue).", "<product>",
     "Standard/Advanced",
     ["references/brand-identity.md", "references/creative/directions-library.md", "references/audio/sound-design.md §5 (sonic logo)"],
     ["Concept + positioning in one line; category cliché named.",
      "Logo direction (wordmark/symbol), color system, type pairing, voice, optional sonic logo.",
      "Show applications (favicon, OG image, app icon, header).",
      "Record licences of fonts and any assets."],
     "Brand sheet + assets + DESIGN.md brand section.",
     ["Copy an existing brand's mark or style."]),

    ("assets", "Find, make and license icons, images, illustrations, favicons, OG images and other assets.", "<what you need>",
     "Quick/Standard",
     ["references/catalog/asset-sources.md", "references/icons-illustration-and-imagery.md", "references/assets-and-marketing-graphics.md"],
     ["Decide if imagery is needed and what role it plays.",
      "Prefer project assets; otherwise pick a source from the catalogue and check its licence.",
      "Produce correct sizes/formats; write alt text.",
      "Record source + licence + attribution in DESIGN.md."],
     "Assets + licence table.",
     ["Use an asset whose licence you don't know."]),

    ("motion", "Add rich, purposeful motion: ask which kinds (scroll, hover, hero entrance, micro-interactions, transitions, text, data, layout, ambient, cursor, SVG, 3D, gestures) and how strong, then build and verify every item.", "<area or page>",
     "Standard",
     ["references/motion/motion-menu.md (the menu, intensities, minimums, recommended sets)", "references/modern-layer.md", "references/motion/motion-system-and-verification.md", "references/motion/motion-tech-catalog.md", "templates/MOTION.md"],
     ["Ask which kinds of motion the user wants, following motion-menu.md §1: first 'You choose (Recommended) / Let me pick the kinds / Keep it minimal'; if they pick, ask the grouped MULTI-SELECT questions (Page & scroll, Interaction, Content, Visual depth; 4 kinds each). Skip only if the user already listed the kinds.",
      "Ask Question B: intensity (Subtle / Balanced (Recommended) / Expressive / Cinematic).",
      "Pick concrete items for every chosen kind from the catalogue (§3) and meet the minimum for the effort level (§2). If the user chose 'You choose', show the list and let them remove items.",
      "Write the motion plan table with an M-ID per item (§5): element, trigger, effect, duration/easing scaled to the intensity, reduced-motion version, tech.",
      "Build every M-ID with motion tokens and the right engine (CSS first, GSAP/Motion only where needed). Vary effects by element role; never one fade-up for everything.",
      "Verify: observe every M-ID working (recording or Animations panel), run verify_page.py (motion inventory + reduced motion), check smoothness; report planned vs built."],
     "Motion plan (M-IDs) + implementation + verification (planned vs built, reduced motion, smoothness).",
     ["Deliver only a fade-in and call it motion.", "Skip the motion question.", "Ignore reduced motion or hover-only on touch."]),

    ("motion-graphics", "Create motion graphics: kinetic typography, animated compositions, scroll stories, product animations, generative visuals.", "<piece>",
     "Advanced",
     ["references/motion/motion-graphics.md", "references/motion/motion-menu.md", "references/motion/motion-tech-catalog.md", "references/motion/motion-system-and-verification.md", "references/creative/directions-library.md (motion section)", "templates/MOTION.md"],
     ["Ask (if unknown): where it lives (web page, README GIF/SVG, video), length, sound on/off, dimension (1D/2D/2.5D/3D), and which motion kinds and intensity (references/motion/motion-menu.md §1).",
      "Concept → 2–3 motion directions (All-out) → storyboard with timing → animatic.",
      "Choose technology with the selection ladder; justify it.",
      "Build with a timeline; design the reduced-motion version; budget performance.",
      "Verify play-through, sync, loop point, frame rate, reduced motion, cleanup; capture video/GIF if useful."],
     "MOTION.md (concept, storyboard, timing, tech), the piece, verification evidence.",
     ["Add random particles/gradients without a concept.", "Make content wait for decoration."]),

    ("3d", "Build 3D and real-time graphics (product viewers, scenes, interactive 3D).", "<scene>",
     "Advanced",
     ["references/motion/3d-and-realtime.md", "references/motion/motion-tech-catalog.md", "references/catalog/asset-sources.md (3D models, HDRIs)"],
     ["Confirm 3D is justified (vs 2.5D or video).",
      "Pick engine (Three.js / R3F / Babylon / Spline export) and assets (licences).",
      "Art-direct lighting, materials, camera; budget polys, textures, draw calls.",
      "Provide a static fallback and reduced-motion behaviour; lazy-load.",
      "Verify frame rate on a mid-range device profile, memory cleanup, fallback."],
     "Scene + asset licence table + performance numbers + fallback.",
     ["Ship 3D that blocks the main content from loading."]),

    ("sound", "Design UI sound, sonic identity, ambience or interactive audio.", "<product or piece>",
     "Standard/Advanced",
     ["references/audio/sound-design.md", "references/audio/audio-tech-catalog.md", "references/audio/audio-implementation-and-verification.md", "templates/SOUND.md"],
     ["Decide if sound helps at all; define its role and the silence policy.",
      "Audio direction + palette + interaction-to-sound map (few, meaningful events).",
      "Choose assets (licences) or synthesis; choose one playback/synthesis library.",
      "Implement opt-in, mute, volume, visual equivalents; no autoplay.",
      "Verify playback after user gesture, mute, overlap, failure, loudness."],
     "SOUND.md, sound files or synth code, controls, verification.",
     ["Autoplay anything.", "Put a sound on every click."]),

    ("voice", "Write and produce narration or voice-over (human or TTS) with captions.", "<script topic or video>",
     "Standard",
     ["references/audio/voice-and-narration.md", "references/audio/audio-tech-catalog.md §4", "templates/SOUND.md §4"],
     ["Ask: voice type, language/accent, and whether the user has a TTS/voice service or wants a free engine.",
      "Write the script for the ear (short sentences, ~140–160 wpm), mark pronunciation and pauses.",
      "Produce: record or synthesize; clean, level to target loudness.",
      "Make captions/transcript; check sync and pronunciation."],
     "Script, audio file(s), captions, licence/consent notes.",
     ["Clone a real person's voice without documented consent."]),

    ("video", "Produce any video: explainer, trailer, product demo, tutorial, social short, title sequence, data story.", "<what video>",
     "Advanced",
     ["references/video/video-types-and-craft.md", "references/video/video-tools-and-pipeline.md", "references/audio/voice-and-narration.md", "templates/VIDEO.md"],
     ["Ask (one at a time, if unknown): type and platform, length, sound/narration, and **whether the user has generative video/image/voice access** (Veo, Sora, Runway, Kling, ElevenLabs…).",
      "Brief → one message → script (read it aloud with a timer) → storyboard → animatic. Get the script approved.",
      "Pick tools: generative if available and wanted; otherwise code-based (HyperFrames, Remotion, Motion Canvas, Revideo, Manim) or an editor; check licences.",
      "Build, add voice/music/SFX, captions; render per platform spec.",
      "QA with the VIDEO.md checklist (ffprobe, loudness, sync, captions, safe areas)."],
     "VIDEO.md, the rendered video(s), captions, licence table, QA results.",
     ["Invent footage of the product doing things it can't.", "Use music without a licence."]),

    ("launch-video", "Make a product launch video end to end (teaser, reveal, feature tour or manifesto).", "<product>",
     "Advanced",
     ["references/video/video-types-and-craft.md §2 (launch)", "references/video/video-tools-and-pipeline.md", "references/motion/motion-graphics.md", "references/audio/sound-design.md", "templates/VIDEO.md"],
     ["Ask the launch sub-type: teaser (10–20 s), reveal (30–45 s), feature tour (60–90 s) or manifesto (45–90 s); platforms; generative access.",
      "One message + hook in the first 2 seconds + proof (real product UI) + CTA.",
      "Script, storyboard (shot list with durations), animatic; sonic logo or music bed.",
      "Build with the chosen tool; real UI captures or faithful recreations only.",
      "Export 16:9 + 9:16 (+1:1) cuts, captions, thumbnail; QA."],
     "Launch video files per platform, thumbnail, captions, VIDEO.md.",
     ["Show features that don't exist.", "Bury the product name until the end."]),

    ("score", "Score the work against the request with evidence; list the top 3 improvements if below target.", "<optional target, e.g. 9>",
     "—",
     ["references/workflow/scoring-and-closeout.md", "templates/SCORECARD.md"],
     ["Rebuild the requirement list from the original request.",
      "Add the quality lines relevant to this deliverable.",
      "Score 0–10 with evidence; apply the caps (unverified ≤ 6, failed gate ≤ 4, missing Must → overall ≤ 6).",
      "If below target, list the 3 highest-impact improvements and offer /dent:improve. Include the attribution summary."],
     "Filled SCORECARD.md.",
     ["Give 9–10 without evidence."]),

    ("improve", "Apply the highest-impact improvements from the last scorecard and re-score.", "<optional focus>",
     "Standard",
     ["references/workflow/scoring-and-closeout.md §3", "the previous SCORECARD.md"],
     ["Take the top 3 improvements (or the user's focus).",
      "Apply them in order; re-run the affected gates.",
      "Re-score only with new evidence; show before → after per line.",
      "Stop at target, or when the remaining gap needs the user (real content, assets, budget)."],
     "Changes + updated scorecard with deltas.",
     ["Loop endlessly; after two rounds without progress, propose a direction change."]),

    ("update", "Update the DENT plugin to the latest version without reinstalling (refreshes the local marketplace copy so Claude's normal update works).", "[--check]",
     "Quick",
     ["scripts/update_plugin.py"],
     ["Tell the user what you'll do in one line: refresh DENT's local marketplace copy from GitHub (no Claude settings are edited).",
      "Run `python scripts/update_plugin.py` from this skill's folder (add `--check` to only report). If Python or git isn't available, explain the manual path: Settings → Plugins → Marketplaces → dent → Update, then update the plugin.",
      "Report the installed version and the available version from the script output.",
      "If a newer version is available, give the one remaining step: Settings → Plugins → DENT → Update (or remove + add it again, which now gets the new version), or `/plugin update dent@dent` then `/reload-plugins`, or `claude plugin update dent@dent` in a terminal. Then a new chat.",
      "Suggest enabling auto-update for the DENT marketplace so future versions arrive automatically."],
     "Installed vs available version, what was refreshed, and the one step left (if any).",
     ["Edit Claude's settings or install records by hand.", "Delete the user's plugin folders."]),

    ("handoff", "Write DESIGN.md and developer handoff (tokens, specs, states, a11y notes, licences).", "<project>",
     "Standard",
     ["references/design-md-template.md", "references/tooling-and-handoff.md §4", "references/design-tokens-and-code.md Part 1"],
     ["Collect final values, decisions and licences.",
      "Fill DESIGN.md (plus MOTION/SOUND/VIDEO specs if relevant).",
      "Add handoff notes: screens + states, responsive behaviour, interaction and a11y annotations, assets, open questions."],
     "DESIGN.md + exported tokens + handoff notes.",
     ["Leave values vague (\"nice blue\")."]),
]


def skill_file(name, summary, hint, depth, load, steps, output, never):
    lines = [f"# /dent:{name}" if name != "dent" else "# /dent", "", summary, "",
             f"**Usage:** `/dent:{name} {hint}` (also `/dent {name} …` or `dent {name} …`)" if name != "dent" else f"**Usage:** `/dent {hint}`",
             f"**Default depth:** {depth}. Effort level and the gates in SKILL.md §3 always apply.", "",
             "## Load", *[f"- `{r}`" if not r.startswith(("the ", "DENT", "SKILL")) else f"- {r}" for r in load], "",
             "## Steps", *[f"{i}. {s}" for i, s in enumerate(steps, 1)], "",
             "## Output", output, "",
             "## Never", *[f"- {n}" for n in never], "",
             "Close with the scorecard summary, attribution (DENT / user / agent judgment / overrides) and a one-line next step (SKILL.md §8).", ""]
    return "\n".join(lines)


def wrapper_file(name, summary, hint):
    return "\n".join([
        "---",
        f"description: {summary}",
        f"argument-hint: {hint}",
        "---",
        "",
        f"Use the **dent** skill (load it first if it isn't loaded). If the skill's text isn't in your context, read `skills/dent/SKILL.md` from this plugin's install folder (under `~/.claude/plugins/cache/dent/dent/<version>/`). Then open the skill's `commands/{name}.md` and follow it exactly, together with SKILL.md's gates (§3) and close-out (§8).",
        "",
        "User request: $ARGUMENTS",
        "",
    ])


def write_reference():
    """docs/COMMANDS.md: the human-readable command reference (generated)."""
    nl = "\n"
    rows = []
    for name, summary, hint, depth, load, steps, output, never in COMMANDS:
        cmd = "/dent" if name == "dent" else f"/dent:{name}"
        loads = "; ".join(item.split(" (")[0] for item in load)
        does = " → ".join(st.split(".")[0].split(":")[0] for st in steps)
        rows.append(nl.join([
            f"### `{cmd}`", "", summary, "",
            f"- **Usage:** `{cmd} {hint}`",
            f"- **Default depth:** {depth}",
            f"- **Loads:** {loads}",
            f"- **Does:** {does}",
            f"- **Delivers:** {output}",
            f"- **Definition:** [`skills/dent/commands/{name}.md`](../skills/dent/commands/{name}.md)", ""]))
    table = "".join(f"| `{'/dent' if c[0] == 'dent' else '/dent:' + c[0]}` | {c[1]} |{nl}" for c in COMMANDS)
    head = nl.join([
        "# DENT Command Reference", "",
        "_Generated by `scripts/build_commands.py`. Do not edit by hand._", "",
        "You only need `/dent`: the router (`skills/dent/references/workflow/orchestration.md`) picks and chains the right "
        "commands for you. The commands below are shortcuts for when you know exactly what you want. In Claude Code (plugin "
        "install) they are real slash commands; in other agents type them the same way (`/dent:plan ...`, `/dent plan ...` "
        "or `dent plan ...`).", "",
        "| Command | What it does |", "|---|---|", ""]) + table + nl + "---" + nl + nl
    (ROOT / "docs" / "COMMANDS.md").write_text(head + nl.join(rows), encoding="utf-8", newline=nl)


def main():
    SKILL_CMDS.mkdir(parents=True, exist_ok=True)
    PLUGIN_CMDS.mkdir(parents=True, exist_ok=True)
    for c in COMMANDS:
        name, summary, hint = c[0], c[1], c[2]
        (SKILL_CMDS / f"{name}.md").write_text(skill_file(*c), encoding="utf-8", newline="\n")
        (PLUGIN_CMDS / f"{name}.md").write_text(wrapper_file(name, summary, hint), encoding="utf-8", newline="\n")
    write_reference()
    print(f"Wrote {len(COMMANDS)} commands to {SKILL_CMDS.relative_to(ROOT)} and {PLUGIN_CMDS.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

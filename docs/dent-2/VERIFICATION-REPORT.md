# DENT 2.0 Verification Report

Date: 2026-11-14 · Environment: Windows 11, Python 3.11, Playwright Chromium (scratch venv), Git Bash. Results: **Passed / Failed / Not run / Blocked**.

## 1. Automated checks

| Check | Command | Result | Evidence |
|---|---|---|---|
| Skill structure, links, styles, commands, catalogues, versions | `python scripts/validate.py` | Passed | `OK: SKILL.md v2.0.0 + 53 reference files + 41 styles + 30 commands + 216 catalogue entries; 409 internal references resolved` |
| Validator catches a broken link | Injected `references/nope.md` into a reference (1.0 era test, logic retained) | Passed | Reported as error |
| Command generation is in sync | `python scripts/build_commands.py` then no diff | Passed | 30 skill commands, 30 wrappers, `docs/COMMANDS.md` |
| Tool regression tests | `python scripts/test_tools.py` | Passed | contrast.py 3/3; bad fixture fails G2, G3, G4, G10, G11; good fixture passes all five |
| verify_page.py on real pages | Brewlog with/without DENT 1.x | Passed (found real defects) | `benchmark/results/…/verify-with.json`, `verify-without.json`: overflow at 320–390 (with) and 320 (without), sampled contrast failures, hidden-tab unlabeled sliders, reduced-motion failure (without) |
| Package builds | `python scripts/package.py` | Passed | `dist/dent.zip` (skill files + LICENSE + NOTICE; no `__pycache__`) |
| README assets are valid XML | `assets/build_assets.py` parses every SVG with minidom | Passed | Build fails loudly on malformed SVG (caught an unescaped `&` during development) |
| README renders, no broken images, no overflow | Local Markdown render + Playwright at 1280 and 390 px | Passed | 0 broken images; scrollWidth = viewport at both widths |
| Hero animation frames | Rendered as `<img>` at 0.4 s, 1.7 s, 2.5 s, 6 s | Passed | Template → impact → wordmark rise → final composition |
| Hero reduced motion | SVG loaded directly with `prefers-reduced-motion: reduce` | Passed | Final composition shown immediately |
| Plugin manifests | JSON parse + version match | Passed | 2.0.0 in SKILL.md, plugin.json, marketplace.json |

## 2. Not run / limitations (honest list)

| Item | Status | Why / what's needed |
|---|---|---|
| Command discovery inside each agent (Claude Code plugin `/dent:` list, Codex, Cursor, Copilot, Gemini CLI, Antigravity) | Not run | Needs the repo pushed and installed in each agent: next session |
| End-to-end runs of DENT 2.0 on the 21 scenarios (A/B/C comparison) | Not run | Requires installed DENT 2.0 and real agent runs; the protocol and prompts are ready (`evals/`) |
| Showcase pieces (landing page, motion piece, explainer video with narration) | Not run | Planned for the next session, built with installed DENT 2.0 (scenarios S19–S21) |
| Reduced motion inside `<img>` SVG on GitHub | Partly verified | Playwright can't emulate the media query inside image documents; verified by loading the SVG directly. Real browsers apply the OS setting to SVG images |
| GitHub's own Markdown rendering | Not run | Rendered locally with a GitHub-like stylesheet; final check after push |
| Catalogue licences | Partly verified | Entries marked ✓ were checked 2026-11-14 (GSAP, Base UI, Vaul, HyperFrames, Remotion, Theatre.js, Piper, Kokoro, Essentia.js, Peaks.js); all others are marked K and must be re-verified before relying on them |
| Generative video/voice tool terms | Not verified | Provider terms change frequently; DENT instructs agents to check the user's plan terms |
| Install paths for every agent | Not re-verified | Paths documented with a caveat; confirm per agent after push |
| CI on GitHub Actions | Not run | Workflow updated (validator, command sync, Playwright tool tests, package); runs on next push |

## 3. Known limitations and future improvements
- Self-scores are still produced by the same model that did the work; the protocol requires independent review for published comparisons.
- `verify_page.py` samples contrast only on solid backgrounds (text over images/gradients is skipped and must be checked by eye), checks labels/names but not full keyboard operability, and can't judge design quality.
- No automated motion timeline/fps capture yet (procedures documented; tooling on the roadmap).
- Recipes exist for landing pages and app/dashboards; mobile app, e-commerce, docs site and email recipes are future work (their All-out sweeps exist).
- Catalogue rows marked K need periodic verification passes.

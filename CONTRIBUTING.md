# Contributing to DENT

Thanks for helping make AI-made design better. Contributions of all sizes are welcome: typo fixes, new styles, better rules, new patterns, evaluation cases and install guides for more agents.

## Ground rules for content

DENT is read by AI agents, so every line costs context and changes behavior. Contributions should be:

1. **Correct and sourced.** Label guidance as **[Law]** (research-backed), **[Rule]** (measurable standard such as WCAG or a platform guideline) or **[Convention]** (industry practice). Link or name the source for laws and rules in the PR description.
2. **Actionable.** Concrete values and decisions ("44×44px minimum", "debounce 150–300ms") beat adjectives ("make it nice").
3. **Short.** Say it once, in the right file. Prefer a table row to a paragraph.
4. **Safe.** Never weaken a [Rule]. No deceptive patterns. No copying of a specific product's proprietary look, assets or copy.
5. **Original.** Write in your own words; don't paste copyrighted text from books, courses or other skills.
6. **Plain language.** Users see the agent's paraphrase of this content; write so a non-designer understands.

## Where things go

| Change | File(s) |
|---|---|
| Workflow, questions, effort levels | `skills/dent/SKILL.md` §1, `references/workflow-questions-and-effort.md` |
| Laws, non-negotiables, gates, routing | `skills/dent/SKILL.md` |
| Tokens and core components; interface motion | `references/foundations-and-components.md`; `references/modern-layer.md` |
| A new aesthetic style | `references/styles/<name>.md` (from `_style-template.md`) + row in `_styles-index.md` |
| A new topic | new `references/<topic>.md` + row in `SKILL.md` §9.2 + row in the workflow add-on routing table |
| More components | `references/components-extended.md` |
| Install instructions for an agent | `docs/INSTALL.md`, `README.md`, `scripts/install.*` |
| Commands | `scripts/build_commands.py` (generated files), routing in `references/workflow/orchestration.md` |
| Library, motion, audio, video catalogues | `references/catalog/`, `references/motion/motion-tech-catalog.md`, `references/audio/audio-tech-catalog.md`, `references/video/video-tools-and-pipeline.md` (row format in `references/catalog/README.md`) |
| Creative directions, hero type, anti-slop | `references/creative/` |
| Recipes (step-by-step procedures with gates) | `references/recipes/` |
| Verification tools | `skills/dent/scripts/` + `evals/fixtures/` + `scripts/test_tools.py` |
| Test scenarios | `evals/cases.md`, `evals/scenarios.md`, `evals/commands.md` |

Keep `SKILL.md` lean: if something only matters for some tasks, it belongs in a reference file.

## Workflow

1. Fork and create a branch: `git checkout -b style/solarpunk`.
2. Make the change.
3. Run the validator: `python scripts/validate.py` (frontmatter, every internal link, styles, commands, catalogue rows, versions) and, if you touched tools, `python scripts/test_tools.py`.
4. Try it in at least one agent with a relevant prompt from `evals/cases.md` (or add a new case).
5. Update `CHANGELOG.md` under "Unreleased".
6. Open a PR describing **what** changed, **why**, and **how you tested** it.

## Licensing of contributions

By contributing, you agree that your contributions are licensed under the [Apache License 2.0](LICENSE) (see Section 5 of the license). You confirm you have the right to submit them. Please don't submit content you didn't write or can't license.

## Code of conduct

Participation is governed by our [Code of Conduct](CODE_OF_CONDUCT.md).

# AGENTS.md — working on the DENT repository

This repository **is** a skill. If you're an AI agent editing it:

- The skill lives in `skills/dent/`. `SKILL.md` is always loaded by agents that use DENT; keep it lean and put task-specific detail in `skills/dent/references/`.
- Label guidance **[Law]**, **[Rule]** or **[Convention]**. Never weaken a [Rule].
- New style → `skills/dent/references/styles/<name>.md` from `_style-template.md` + a row in `_styles-index.md` + update the style count in `SKILL.md` frontmatter/§9.2 and `README.md`.
- New reference file → add a row to `SKILL.md` §9.2 and to the add-on routing table in `references/workflow-questions-and-effort.md` §4.
- Run `python scripts/validate.py` after every change; it must print `OK`.
- Bump the version in `SKILL.md` metadata, `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` together, and add a `CHANGELOG.md` entry.
- Don't put user-specific `DESIGN.md` files in this repo.

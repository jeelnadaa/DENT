# AGENTS.md — working on the DENT repository

This repository **is** a skill. If you're an AI agent editing it:

- The skill lives in `skills/dent/`. `SKILL.md` is always loaded by agents that use DENT; keep it lean and put task-specific detail in `skills/dent/references/`.
- Label guidance **[Law]**, **[Rule]** or **[Convention]**. Never weaken a [Rule].
- New style → `skills/dent/references/styles/<name>.md` from `_style-template.md` + a row in `_styles-index.md` + update the style count in `SKILL.md` frontmatter/§9.2 and `README.md`.
- New reference file → add a row to `SKILL.md` §9.2 and to the add-on routing table in `references/workflow-questions-and-effort.md` §4.
- Commands are generated: edit `COMMANDS` in `scripts/build_commands.py`, run it (writes `skills/dent/commands/`, root `commands/` and `docs/COMMANDS.md`), and add a routing row in `references/workflow/orchestration.md`. Never hand-edit generated files.
- Catalogue rows need a link, licence and status (`✓ <date>` only after checking the official source, else `K`).
- Changing `verify_page.py`? Add a case to `evals/fixtures/bad.html` and run `python scripts/test_tools.py` (needs Playwright).
- Changing `palette.py`, `fonts.py`, `tts.py` or `doctor.py`, the palette library in `color.md` §13 or the pairing table in `typography.md` §3? Run `python scripts/test_tools.py`: it re-checks every library palette and pairing face. Regenerate palettes with `palette.py`, never by hand; refresh the font snapshot with `python skills/dent/scripts/fonts.py refresh`.
- Media providers, fonts and models change fast: rows in `references/media-sourcing.md` and the voice tables need a link, licence and status like any catalogue row; never ship a non-commercial model as a commercial default.
- `validate.py` `check_capabilities` guards against capabilities promised in one file but never triggered in another (All-out list, create/redesign running motion and surfaces, media commands asking the sourcing question). Keep it green when you edit pipelines or commands.
- **Modern Web Guidance (MWG) is the authority for web implementation.** `skills/modern-web-guidance/` is Google's skill vendored verbatim: never edit it; refresh with `python scripts/sync_mwg.py`. In DENT files, don't write HTML/CSS/JS technique that MWG covers; keep the design layer and point to the guide as `mwg:<id>` (validate checks the ids). DENT text that contradicts MWG is a bug: fix it and list it in `references/modern-web-guidance.md` §6.
- README visuals come from `assets/build_assets.py`; regenerate, don't hand-edit the SVGs.
- Architecture: `docs/ARCHITECTURE.md`. DENT 2.0 audit/plan/progress: `docs/dent-2/`.
- Run `python scripts/validate.py` after every change; it must print `OK`. Keep SKILL.md under ~450 lines (router only).
- Bump the version in `SKILL.md` metadata, `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` together, and add a `CHANGELOG.md` entry.
- Don't put user-specific `DESIGN.md` files in this repo.

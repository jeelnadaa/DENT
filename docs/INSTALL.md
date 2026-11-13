# Installing DENT

DENT is a standard **Agent Skill**: the folder `skills/dent/` contains `SKILL.md` (with YAML frontmatter) and a `references/` folder. Any agent that supports the Agent Skills format can use it as-is. For agents that don't, a one-line rules file points the agent at it.

> **Paths change.** Agent tools move fast and sometimes rename their skills folders. The paths below were correct for common setups at the time of writing; if one doesn't work, search your agent's docs for "skills". DENT itself needs no changes for any of them.

---

## Option A — `skills` CLI (any agent, fastest)

```bash
npx skills add jeelnadaa/DENT
```
- Detects which agents you have and offers to install for each.
- `-g` installs for your user (all projects) instead of the current project.
- `-a <agent>` targets one agent, e.g. `-a claude-code`.
- `--list` shows what's in the repo without installing.

## Option B — Claude Code plugin marketplace

Inside Claude Code:
```bash
/plugin marketplace add jeelnadaa/DENT
/plugin install dent@dent
```
Update later with `/plugin marketplace update dent`. When installed as a plugin the skill is namespaced: invoke it explicitly with `/dent:dent`, or just ask for design work and it triggers automatically.

## Option C — Installer script (copies the folder for you)

```bash
git clone https://github.com/jeelnadaa/DENT.git
cd DENT
./scripts/install.sh claude            # ~/.claude/skills/dent
./scripts/install.sh claude --project  # ./.claude/skills/dent in the current directory
./scripts/install.sh --list            # all targets
```
Windows PowerShell:
```powershell
git clone https://github.com/jeelnadaa/DENT.git
cd DENT
.\scripts\install.ps1 -Agent claude
.\scripts\install.ps1 -Agent cursor -Project
```

Targets: `claude`, `codex`, `copilot`, `cursor`, `gemini`, `agents` (shared `.agents/skills`), or `-Path`/`--path <dir>` for anything else. Running it again updates DENT in place.

## Option D — Manual copy

Copy `skills/dent/` (the whole folder, keeping the name `dent`) to:

| Agent | Personal (all projects) | Project only |
|---|---|---|
| Claude Code | `~/.claude/skills/dent/` | `.claude/skills/dent/` |
| Claude Agent SDK | — | `.claude/skills/dent/` (enable project settings / skills in your SDK options) |
| OpenAI Codex (CLI / IDE) | `~/.codex/skills/dent/` | `.agents/skills/dent/` |
| GitHub Copilot (VS Code agent mode, coding agent, CLI) | `~/.copilot/skills/dent/` | `.github/skills/dent/` |
| Cursor | `~/.cursor/skills/dent/` | `.cursor/skills/dent/` |
| Gemini CLI | `~/.gemini/skills/dent/` | `.gemini/skills/dent/` |
| OpenCode, Goose, Amp, Letta and other Agent Skills tools | tool-specific | `.agents/skills/dent/` |

Restart the agent (or start a new session) so it picks up the new skill.

## Claude.ai and Claude Desktop (chat)

1. Download `dent.zip` from the [latest release](https://github.com/jeelnadaa/DENT/releases) — or build it: `python scripts/package.py` → `dist/dent.zip`.
2. In Claude, open **Settings → Capabilities**, make sure Skills (and code execution, if required by your plan) are enabled, and **upload** `dent.zip`.
3. Start a new chat and ask for design work.

Team/Enterprise admins can provision the skill for the whole organization from the admin settings.

## Claude API (Skills API)

Upload the `skills/dent` folder as a custom skill through the Skills API (see Anthropic's "Agent Skills" API docs for the current endpoint and required beta headers), then reference the returned skill ID in the container configuration of your Messages API requests. The code-execution tool must be enabled for skills to run.

## Agents without native skill support

Windsurf, Cline, Roo, Aider, Zed, Continue and similar tools read a rules/instructions file instead. Copy the skill into the project and point to it:

1. Copy `skills/dent/` to `.dent/` in your project (or anywhere you like).
2. Add this to your agent's rules file:

```markdown
## Design work (DENT)
For any UI, UX, visual design, design-system or front-end styling task, first read `.dent/SKILL.md`
and follow its workflow. Open files in `.dent/references/` only when SKILL.md points to them.
```

| Agent | Rules file |
|---|---|
| Any tool that reads `AGENTS.md` (Codex, Jules, Amp, Zed, many others) | `AGENTS.md` |
| Windsurf | `.windsurf/rules/dent.md` |
| Cline | `.clinerules/dent.md` |
| Roo Code | `.roo/rules/dent.md` |
| Aider | `CONVENTIONS.md` (load with `--read CONVENTIONS.md`) |
| Gemini CLI (without skills) | `GEMINI.md` |
| Cursor (legacy rules) | `.cursor/rules/dent.mdc` with `description: UI and product design work` |
| GitHub Copilot (instructions) | `.github/copilot-instructions.md` |

The installer can do this for you: `./scripts/install.sh rules --path .dent` copies the folder and prints the snippet.

## Verify the install

Ask your agent: **"What design skills do you have?"** or **"Design a sign-up screen for a recipe app."**
DENT is working if the agent's first reply asks how far to go (Essential / Standard / Polished / All-out) with a recommended option, or decides everything and shows a Decision Log when you say "don't ask".

## Updating

- `skills` CLI: `npx skills update` (or re-run `add`).
- Plugin: `/plugin marketplace update dent`.
- Script/manual: `git pull` in your clone and re-run the installer (it replaces the folder).

Your `DESIGN.md` files live in your projects, not in the skill, so updates never overwrite them.

## Uninstalling

Delete the `dent` folder from the skills directory, or `/plugin uninstall dent@dent` in Claude Code.

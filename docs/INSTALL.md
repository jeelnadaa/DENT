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

Copy `skills/dent/` (the whole folder, keeping the name `dent`) and, next to it, `skills/modern-web-guidance/` (Google's Modern Web Guidance, DENT's authority for web code) to:

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

1. Download `dent.zip` from the [latest release](https://github.com/jeelnadaa/DENT/releases) — or build it: `python scripts/package.py` → `dist/dent.zip` (Modern Web Guidance is bundled inside it under `vendor/`). Optionally also upload `modern-web-guidance.zip` so the guidance applies to web tasks outside DENT.
2. In Claude, open **Settings → Capabilities**, make sure Skills (and code execution, if required by your plan) are enabled, and **upload** `dent.zip`.
3. Start a new chat and ask for design work.

Team/Enterprise admins can provision the skill for the whole organization from the admin settings.

## Claude API (Skills API)

Upload the contents of `dist/dent.zip` (the `skills/dent` folder plus `vendor/modern-web-guidance/`) as a custom skill through the Skills API (see Anthropic's "Agent Skills" API docs for the current endpoint and required beta headers), then reference the returned skill ID in the container configuration of your Messages API requests. The code-execution tool must be enabled for skills to run.

## Agents without native skill support

Windsurf, Cline, Roo, Aider, Zed, Continue and similar tools read a rules/instructions file instead. Copy the skill into the project and point to it:

1. Copy `skills/dent/` to `.dent/` in your project (or anywhere you like), and `skills/modern-web-guidance/` to `.dent/vendor/modern-web-guidance/`.
2. Add this to your agent's rules file:

```markdown
## Design work (DENT)
For any UI, UX, visual design, design-system or front-end styling task, first read `.dent/SKILL.md`
and follow its workflow. Open files in `.dent/references/` only when SKILL.md points to them.
For any HTML, CSS or client-side JS, follow Google's Modern Web Guidance first:
`.dent/vendor/modern-web-guidance/SKILL.md` (DENT's summary: `.dent/references/modern-web-guidance.md`).
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

## Optional: verification tools

DENT can check its own work in a real browser with `skills/dent/scripts/verify_page.py`. Install once:

```bash
pip install playwright
```
```bash
python -m playwright install chromium
```

Or use an installed Chrome/Edge with `--channel chrome` / `--channel msedge`. Without it, DENT falls back to manual checks and reports them as "Not run".

## Optional: Modern Web Guidance CLI

With Node.js 22+, DENT queries the always-current guides with `npx -y modern-web-guidance@latest search "<task>"` (on Windows `npx.cmd`; under Git Bash `search` can fail with `'C:\Program' is not recognized`, so run it from PowerShell or cmd). Sandboxed agents should allowlist exactly `npx -y modern-web-guidance@latest *`. Without Node or network, DENT uses the bundled snapshot through `skills/dent/scripts/mwg.py` and says so in its report.

## Commands

Plugin installs in Claude Code get 31 slash commands (`/dent:plan`, `/dent:audit`, `/dent:video`…). In every other agent, type the same text (`/dent:plan …`, `/dent plan …` or `dent plan …`) and the skill follows the matching command file. You never need them: plain `/dent` routes automatically. Reference: [COMMANDS.md](COMMANDS.md).

## Verify the install

Ask your agent: **"What design skills do you have?"** or **"Design a sign-up screen for a recipe app."**
DENT is working if the agent's first reply states a one-line plan (for example "I'll explore directions, build the page, check it at 6 sizes and score it") and asks how far to go (Essential / Standard / Polished / All-out) with a recommended option, or decides everything and shows a Decision Log when you say "don't ask".

## Updating

DENT releases bump the version in `plugin.json`, and Claude Code updates a plugin when its marketplace lists a newer version. The catch: Claude keeps a local copy of each third-party marketplace and doesn't always refresh it (auto-update is off by default for third-party marketplaces), so removing and re-adding the plugin can reinstall the old version.

**Claude Code (app or CLI): update without reinstalling**
1. In any chat with DENT installed, run **`/dent:update`**. It refreshes DENT's local marketplace copy from GitHub (no Claude settings are edited) and tells you the installed vs available version.
2. Then do the one step it shows: **Settings → Plugins → DENT → Update**, or `/plugin update dent@dent` followed by `/reload-plugins`, or `claude plugin update dent@dent` in a terminal.
3. Start a new chat.

Without `/dent:update`: **Settings → Plugins → Marketplaces → dent → Update marketplace**, then update the plugin (or `/plugin marketplace update dent`, then `/plugin update dent@dent`).

**Never miss an update:** enable auto-update for the DENT marketplace (**Plugins → Marketplaces → dent → Enable auto-update**, or `"autoUpdate": true` on its entry under `extraKnownMarketplaces` in your Claude settings). If an update still doesn't show up, run `/dent:update` once; it forces the refresh.

**Other installs:**
- `skills` CLI: `npx skills update` (or run `add` again).
- Script/manual: `git pull` in your clone and re-run the installer (it replaces the folder).

Your `DESIGN.md` files live in your projects, not in the skill, so updates never overwrite them.

## Uninstalling

Delete the `dent` folder from the skills directory, or `/plugin uninstall dent@dent` in Claude Code.

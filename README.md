<div align="center">

# DENT

### Make a dent with your product's design.

**DENT is an open-source product design skill for AI agents.**
It gives Claude Code, Codex, Cursor, Copilot, Gemini CLI and any agent that reads `SKILL.md` the judgment of a senior product designer: it asks the right questions, applies proven UX laws, follows accessibility rules, avoids the generic "AI look", checks its own work and documents every decision in a `DESIGN.md`.

[![License: Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills%20(SKILL.md)-black.svg)](https://agentskills.io)
[![Styles](https://img.shields.io/badge/aesthetic%20styles-41-orange.svg)](skills/dent/references/styles/_styles-index.md)
[![Version](https://img.shields.io/badge/version-1.0.1-green.svg)](CHANGELOG.md)

[Install](#install) · [What it does](#what-dent-does) · [How it works](docs/HOW-IT-WORKS.md) · [All install options](docs/INSTALL.md) · [Contribute](CONTRIBUTING.md)

</div>

---

## Why DENT

Ask an AI agent to "design a landing page" and you usually get the same thing: a purple gradient, a centered headline, three feature cards, Inter at one weight, missing states, and contrast that fails. It looks fine for a second and like everything else forever.

DENT fixes that by changing **how** the agent works, not just what it outputs:

| Without DENT | With DENT |
|---|---|
| Guesses the look from one sentence | Asks a few focused questions (one at a time, with a recommended option) — or decides for you if you say so |
| Default template look | A concept, a deliberate style (41 to choose from) and a signature element |
| One-off values everywhere | Design tokens and component specs reused on every screen |
| Happy path only | Empty, loading, error, success, hover, focus and disabled states |
| "Looks accessible" | WCAG 2.2 AA rules that no style is allowed to break |
| Starts a second design system in your codebase | Detects your existing tokens / UI library and extends them |
| "I used blue because it's nice" | A Decision Log with the reason and source of every choice |
| Forgets everything next session | An approved `DESIGN.md` that becomes the source of truth |

## What DENT does

- **Six working modes** — Create, Redesign, Audit, Extend, Implement and Adopt (working inside an existing codebase or UI library).
- **Four effort levels** — Essential · Standard · Polished · All-out. You choose how deep it goes; a non-negotiable quality floor applies to all of them.
- **Proven principles** — Gestalt, Fitts, Hick, Jakob, Doherty, Nielsen's heuristics and more, each labeled as *Law*, *Rule* or *Convention* so the agent knows what it may bend.
- **A full component system** — ~45 components specced (sizes, states, behavior, accessibility), from buttons to date pickers, data tables, command palettes and kanban boards.
- **41 aesthetic styles** — Minimal, Swiss, Neo-Brutalism, Glassmorphism, Dark Tech, Editorial, Luxury, Japandi, Utilitarian, Retro OS, Y2K, Cyberpunk and more, each with overrides, signature moves, accessibility watch-outs and starter tokens.
- **Creative direction** — concept sentences, divergent directions, composition and an explicit list of "default look" patterns to avoid.
- **Patterns for real products** — landing, pricing, dashboards, onboarding, auth, checkout, settings, AI/agent UIs, plus teams, roles, billing, notifications, audit logs, collaboration, import/export, docs sites, changelogs and more.
- **Platforms** — responsive web, iOS (HIG), Android (Material 3), desktop, watch, TV, car, voice, AR/VR, sound and haptics.
- **Accessibility, i18n and ethics built in** — WCAG 2.2 AA checklist, ARIA patterns, RTL and Indic/CJK scripts, and a deceptive-patterns blocklist.
- **Design → code** — token architecture (3 tiers, DTCG export) and implementation guides for HTML/CSS, Tailwind, React, Vue, Svelte, Flutter, SwiftUI, Compose and React Native.
- **Self-review** — renders and screenshots what it built when the agent can, scores it against a 12-point rubric and fixes issues before showing you.
- **DESIGN.md** — after you approve, everything is written to a living spec the agent reads before any future design work.

## Install

DENT follows the open **Agent Skills** format: a folder with a `SKILL.md` and reference files. Pick your agent:

### Claude Code (recommended: plugin marketplace)
```bash
/plugin marketplace add jeelnadaa/DENT
/plugin install dent@dent
```

### Any agent, one command (via the `skills` CLI)
```bash
npx skills add jeelnadaa/DENT
```
It detects the agents you have installed (Claude Code, Codex, Cursor, Copilot, Gemini CLI, OpenCode…) and installs DENT for them.

### Manual (any agent)
```bash
git clone https://github.com/jeelnadaa/DENT.git
```
Then copy `skills/dent/` into your agent's skills folder:

| Agent | Personal (all projects) | Project only |
|---|---|---|
| Claude Code | `~/.claude/skills/dent/` | `.claude/skills/dent/` |
| OpenAI Codex | `~/.codex/skills/dent/` | `.agents/skills/dent/` |
| GitHub Copilot (VS Code / coding agent) | `~/.copilot/skills/dent/` | `.github/skills/dent/` |
| Cursor | `~/.cursor/skills/dent/` | `.cursor/skills/dent/` |
| Gemini CLI | `~/.gemini/skills/dent/` | `.gemini/skills/dent/` |
| OpenCode, Goose, Amp & other Agent Skills tools | — | `.agents/skills/dent/` |

Or use the installer script: `./scripts/install.sh claude` (macOS/Linux) or `.\scripts\install.ps1 -Agent claude` (Windows).

**Claude.ai / Claude Desktop:** download `dent.zip` from [Releases](https://github.com/jeelnadaa/DENT/releases) and upload it under **Settings → Capabilities → Skills**.

**Agents without skill support** (Windsurf, Cline, Aider, Zed…): see [docs/INSTALL.md](docs/INSTALL.md#agents-without-native-skill-support) for a two-line rules-file setup.

> Skill folder paths change as tools evolve. If a path above doesn't work, check your agent's docs for its "skills" directory — DENT works anywhere `SKILL.md` is read. Full details: [docs/INSTALL.md](docs/INSTALL.md).

## Use it

You don't need special commands — just ask for design work:

```text
Design a landing page for my meditation app.
Redesign our settings screen — keep the brand colors.
Review this dashboard screenshot and tell me what's wrong.
Build the pricing page from DESIGN.md in Next.js + Tailwind.
Add dark mode.
Go all out on an onboarding flow for a fintech app. Don't ask, just decide.
```

In Claude Code you can also invoke it directly: `/dent` (manual install) or `/dent:dent` (plugin install).

## What's inside

```
skills/dent/
├── SKILL.md                         # Workflow + laws + tokens + components + modern layer + checklist
└── references/                      # Read only when needed (progressive disclosure)
    ├── workflow-questions-and-effort.md
    ├── modes-existing-products.md   # Redesign, audit, existing codebases
    ├── creative-direction.md        # Concept, signature, composition, anti-generic
    ├── design-brief-and-metrics.md  # Brief, JTBD, HEART, A/B tests
    ├── components-extended.md       # 25 more component specs
    ├── complex-product-patterns.md  # Teams, billing, roles, docs, blog, 404…
    ├── page-and-flow-patterns.md
    ├── color.md · typography.md · accessibility.md · ux-writing.md
    ├── design-tokens-and-code.md · tooling-and-handoff.md · quality-review.md
    ├── platforms-and-devices.md · industry-playbooks.md · internationalization.md
    ├── data-visualization.md · icons-illustration-and-imagery.md · brand-identity.md
    ├── assets-and-marketing-graphics.md · persuasion-and-ethics.md
    ├── research-and-information-architecture.md · inspiration-and-reference-sites.md
    ├── design-md-template.md
    └── styles/                      # 41 aesthetic styles + index + template
```

The agent loads only `SKILL.md` up front and opens a reference file only when the task needs it, so DENT stays light on context even though it holds a full design curriculum.

## Creator

DENT was created by **Jeel Nada**, known online as **solarquack** · GitHub [@jeelnadaa](https://github.com/jeelnadaa).
If DENT helps you ship something, a ⭐ on the repo or a mention is the best thank-you.

## License

DENT is licensed under the [Apache License 2.0](LICENSE). You may use, modify and distribute it — including commercially — as long as you keep the license and the [NOTICE](NOTICE) file (which credits the creator). The license does **not** grant rights to the DENT name or logo; see [TRADEMARKS.md](TRADEMARKS.md) for how you may refer to the project.

Designs you create with DENT are yours. DENT claims no rights over its output.

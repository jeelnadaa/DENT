<div align="center">

# DENT

### Make a dent with your product's design.

**DENT is an open-source product design skill for AI agents.**
It gives Claude Code, Codex, Cursor, Copilot, Gemini CLI and any agent that reads `SKILL.md` the judgment of a senior product designer: it asks the right questions, applies proven UX laws, follows accessibility rules, avoids the generic "AI look", checks its own work and documents every decision in a `DESIGN.md`.

[![License: Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills%20(SKILL.md)-black.svg)](https://agentskills.io)
[![Styles](https://img.shields.io/badge/aesthetic%20styles-41-orange.svg)](skills/dent/references/styles/_styles-index.md)
[![Version](https://img.shields.io/badge/version-1.0.1-green.svg)](CHANGELOG.md)

[Install](#install) · [See the difference](#see-the-difference-run-the-benchmark) · [What it does](#what-dent-does) · [How it works](docs/HOW-IT-WORKS.md) · [All install options](docs/INSTALL.md) · [Contribute](CONTRIBUTING.md)

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

## See the difference: run the benchmark

Don't take our word for it. Give your agent the **same prompt twice**, once without DENT and once with it, and compare the two websites. We publish every result: wins, ties and losses.

**How to run either benchmark**
1. Use the same agent, model and settings for both runs, each in a **fresh session** and an **empty folder**.
2. **Run A, without DENT:** skill not installed. **Run B, with DENT:** skill installed ([install](#install)).
3. Paste the prompt unchanged. Apart from answering the agent's questions (benchmark 1 only), reply only `continue` if it stops early. Keep the first result of each run.
4. Open both `index.html` files side by side on your phone and desktop, and share your screenshots via a pull request or a [Benchmark result issue](https://github.com/jeelnadaa/DENT/issues/new?template=benchmark_result.md).

Full rules, scoring sheet and a screenshot script: **[benchmark/](benchmark/README.md)**

### Benchmark 1: DENT's own landing page, built with DENT

We built DENT's landing page with DENT itself. Here is the exact prompt we used, so you can build it **with and without DENT** and compare.

This prompt gives the agent the **content** (headlines, copy, links) and nothing about the look. It also **lets the agent ask questions**, the way real requests work: answer them briefly, and give the same answers in both runs where the questions overlap.

```text
Build the landing page for DENT, an open-source product design skill for AI coding agents.
Put it in a single self-contained index.html (HTML, CSS and JavaScript inline; Google Fonts
allowed; no other external files, frameworks or images, so build any visuals with HTML, CSS
or inline SVG). It must work well on phones, tablets and desktops.

Every "Download" or "Get DENT" button links to https://github.com/jeelnadaa/DENT and opens
in a new tab.

Use this content. You may shorten or rephrase it lightly and choose the order of sections,
but keep the facts accurate and don't invent statistics, testimonials, logos or user counts.

PRODUCT
- Name: DENT
- Tagline: Make a dent with your product's design.
- What it is: a free, open-source skill (a folder with a SKILL.md file) that gives AI coding
  agents the judgment of a senior product designer.
- Works with: Claude Code, OpenAI Codex, Cursor, GitHub Copilot, Gemini CLI, OpenCode and any
  agent that supports Agent Skills (SKILL.md). Also Claude.ai and Claude Desktop.
- License: Apache 2.0. Created by Jeel Nada (solarquack).

HERO
- Headline: AI agents can build anything. Now they can design it, too.
- Subheadline: DENT is an open-source design skill that makes your AI agent ask the right
  questions, follow proven UX laws and accessibility rules, and ship interfaces that don't
  look like every other AI-made site.
- Primary button: Download on GitHub (link above)
- Secondary button: See how it works (scrolls to the "How it works" section)
- Small note under the buttons: Free and open source · Apache 2.0 · Works with Claude Code,
  Codex, Cursor, Copilot and more

THE PROBLEM
- Heading: Every AI-made website looks the same.
- Body: Ask an agent for a landing page and you get the usual: a purple gradient, a centered
  headline, three feature cards, one font at one weight, missing states and text you can
  barely read. It works for a second and looks like everything else forever.

WITHOUT DENT vs WITH DENT (a comparison)
- Guesses the look from one sentence → Asks a few focused questions, or decides for you if
  you say so
- Default template look → A clear concept, a deliberate style and a signature element
- One-off values everywhere → Design tokens and components reused on every screen
- Happy path only → Empty, loading, error, success, hover, focus and disabled states
- "Looks accessible" → WCAG 2.2 AA rules no style is allowed to break
- Adds a second design system to your codebase → Detects your existing UI library and
  extends it
- "I picked blue because it's nice" → A decision log with the reason behind every choice
- Forgets everything next session → An approved DESIGN.md that becomes the source of truth

HOW IT WORKS (5 steps)
1. Ask: DENT asks how far to go, then only the questions that matter, one at a time, each
   with a recommended answer.
2. Direct: it picks a concept and a style on purpose, not by default.
3. Build: tokens first, then components with every state, then screens.
4. Check: it reviews its own work against a quality checklist and, when the agent can,
   takes screenshots and fixes what's wrong.
5. Document: once you approve, everything goes into DESIGN.md so the next change stays
   consistent.

FEATURES
- Four effort levels: Essential, Standard, Polished and All-out. You choose the depth.
- 41 aesthetic styles: from Minimal, Swiss and Editorial to Neo-Brutalism, Glassmorphism,
  Japandi, Dark Tech, Retro OS and Cyberpunk, each with rules for doing it well.
- Proven principles: Gestalt, Fitts's Law, Hick's Law, Jakob's Law and Nielsen's heuristics,
  applied for you.
- Accessibility built in: contrast, touch targets, keyboard and focus, reduced motion.
- Works with your code: detects shadcn/ui, MUI, Chakra, Tailwind and your existing tokens,
  and extends them.
- Design to code: HTML/CSS, Tailwind, React, Vue, Svelte, Flutter, SwiftUI, Jetpack Compose
  and React Native.
- Six modes: create, redesign, audit, extend, implement, and adopt an existing design system.
- Real product patterns: landing pages, pricing, dashboards, onboarding, checkout, settings,
  AI and chat interfaces, billing, roles, docs sites and more.

STYLES SHOWCASE
- Heading: 41 styles. Zero templates.
- Show a sample of style names: Minimal, Swiss, Editorial, Luxury, Japandi, Neo-Brutalism,
  Glassmorphism, Dark Tech, Bento, Utilitarian, Retro OS, Y2K, Synthwave, Cyberpunk,
  Terminal, Pixel Art, plus "and 25 more".

BENCHMARK
- Heading: Don't take our word for it.
- Body: We give an AI agent the same prompt twice, once without DENT and once with it, and
  publish both results: wins, ties and losses. This page itself was built with DENT. Run the
  benchmark yourself and share what you get.
- Button: Run the benchmark (link: https://github.com/jeelnadaa/DENT/tree/main/benchmark)

INSTALL
- Heading: Install in one line.
- Show these as copyable commands, each with a copy button:
  - Any agent: npx skills add jeelnadaa/DENT
  - Claude Code: /plugin marketplace add jeelnadaa/DENT  then  /plugin install dent@dent
- Note: Or download the folder from GitHub and drop it into your agent's skills directory.
  Full guide: https://github.com/jeelnadaa/DENT/blob/main/docs/INSTALL.md

FAQ
- Is DENT free? Yes. It's open source under the Apache 2.0 license, including for
  commercial work.
- Which agents does it work with? Any agent that supports Agent Skills (SKILL.md): Claude
  Code, Codex, Cursor, GitHub Copilot, Gemini CLI, OpenCode and more. For other agents you
  can point a rules file at it.
- Will it slow my agent down? DENT loads one main file and opens its detailed guides only
  when a task needs them.
- Do I own what I design with it? Yes. DENT claims no rights over your designs.
- Can it work on my existing app? Yes. It detects your existing design system and extends
  it, or audits your current UI and ranks what to fix.
- Can I contribute? Yes. New styles, patterns and fixes are welcome on GitHub.

FINAL CALL TO ACTION
- Heading: Give your agent taste.
- Body: Install DENT in a minute and ask for your next screen.
- Button: Download on GitHub (link above)

FOOTER
- DENT · Make a dent with your product's design.
- Links: GitHub (https://github.com/jeelnadaa/DENT) · Install guide · Benchmark · License
  (https://github.com/jeelnadaa/DENT/blob/main/LICENSE)
- Created by Jeel Nada (solarquack). Apache 2.0.

When you are done, give me a short summary of the design decisions you made.
```

**Results: DENT landing page**

| Agent + model | Without DENT | With DENT | Run by |
|---|---|---|---|
| *Official results coming soon* | | | [@jeelnadaa](https://github.com/jeelnadaa) |

Prompt file and run notes: [benchmark/PROMPT-DENT-LANDING.md](benchmark/PROMPT-DENT-LANDING.md)

### Benchmark 2: "Brewlog", a one-shot website

A fictional coffee app. This prompt never mentions DENT and tells the agent not to ask questions, so both runs are one-shot and directly comparable.

```text
Build a complete, production-quality marketing website for "Brewlog", a fictional app
for home coffee brewers. Brewlog lets people log brew recipes (beans, grind size, water
temperature, ratio, time), rate each cup, and see which settings make their best coffee
over time. It has a free plan and a paid "Pro" plan ($6/month or $60/year) that adds
unlimited recipes, bean inventory tracking and brew analytics.

Requirements:
- One self-contained file named index.html (HTML, CSS and JavaScript inline). Web fonts
  from Google Fonts are allowed. No other external files, frameworks or images: build any
  visuals (product screenshots, illustrations, icons) with HTML, CSS or inline SVG.
- Sections: a header with navigation, hero, how it works, key features, a preview of the
  app's interface, pricing (Free vs Pro, monthly/yearly), FAQ, a sign-up form, and a footer.
- The sign-up form asks for name, email and password, validates in the browser and shows
  helpful errors and a success state. It does not need a backend.
- It must look great and work well on phones, tablets and desktops.

Make every decision yourself and don't ask me any questions. When you are done, reply with
a short summary of the design decisions you made.
```

**Results: Brewlog**

| Agent + model | Without DENT | With DENT | Run by |
|---|---|---|---|
| *Official results coming soon* | | | [@jeelnadaa](https://github.com/jeelnadaa) |

*Live side-by-side demos will be linked here as results come in.*

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

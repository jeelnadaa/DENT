# DENT Landing Page Prompt (v1)

This is the prompt we use to build **DENT's own landing page**, built with DENT. It also works as a second benchmark: run it once **without DENT** and once **with DENT**, using the same agent and model, and compare.

Unlike the Brewlog prompt, this one **lets the agent ask questions**. Most real requests come in this way, and asking good questions is part of what DENT does.

The prompt gives the **content only**: product facts, headlines, copy and links. It says nothing about colors, fonts, layout or style, because those are the design decisions being compared.

---

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

---

## How to run it as a benchmark

1. Same agent, same model and same settings for both runs, each in a fresh session and an empty folder.
2. **If the agent asks questions, answer them.** Use the same answers in both runs where the questions overlap, and keep them short and honest (for example "Standard effort", "dark mode is fine", "you choose the style"). Save the questions and your answers. How the agent asks is part of the result.
3. Apart from answering questions, reply only `continue` if it stops early. No design feedback.
4. Keep the first finished result of each run.
5. Capture and score it like the Brewlog benchmark ([README.md](README.md) §2–4), and add the Q&A to your `RESULT.md`.

## Prompt facts to keep in sync
If DENT's facts change (style count, supported agents, install commands), update this prompt and bump its version (v2). Published results always state which version they used.

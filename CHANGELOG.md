# Changelog

All notable changes to DENT are documented here. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow [SemVer](https://semver.org/).

## [1.0.0] — 2026-11-14

First public release as **DENT** (previously an internal skill called `product-design`).

### Added
- **Modes** (`modes-existing-products.md`): Create, Redesign, Audit, Extend, Implement, Adopt. Detects existing tokens, themes and UI libraries (shadcn/ui, MUI, Chakra, Tailwind…) and extends them instead of introducing a second design system. Drift measurement commands, redesign migration plan, severity-ranked audit report format.
- **Creative direction** (`creative-direction.md`): concept sentence, mood/anti-mood words, divergent directions along 8 axes, signature elements, composition rules, 2025–26 "default look" list to avoid, type-led design, advanced color strategies, presenting work.
- **Design brief & metrics** (`design-brief-and-metrics.md`): one-page brief, JTBD, design principles, HEART, task metrics (SUS, SEQ, UMUX-Lite), guardrail metrics, event naming, honest A/B testing, lightweight validation.
- **Extended components** (`components-extended.md`): 25 specs — accordion, breadcrumbs, pagination, stepper, date/time picker, file upload, search, command palette, number stepper, OTP, tag input, rating, carousel, tree, advanced data table, kanban, calendar, timeline, editor toolbar, popconfirm, empty state, banner, avatar group/copy field/code block, color picker, range slider.
- **Complex product patterns** (`complex-product-patterns.md`): workspaces, roles & permissions, billing & subscriptions, notification center, audit log, versions/autosave, collaboration, offline & real-time, bulk actions & jobs, import/export, admin/CRUD, keyboard-first, security & privacy UX (passkeys, 2FA, sessions, account deletion, permission priming), trust & safety, in-product help, feature badges; content pages — blog, docs, changelog, about/careers, contact, error pages, legal, comparison, waitlist, case study.
- **Tooling & handoff** (`tooling-and-handoff.md`): previews in agent environments (style tiles, token and component sheets), Figma reading/structuring, Storybook docs, accessibility annotations, design QA, keeping DESIGN.md healthy.
- **Two new styles:** Utilitarian (industrial / instrument panel) and Retro OS (90s desktop). Total: 41.
- SKILL.md: mode selection (§1.0), concept step, agent-environment adaptation (§1.8), "Never" rules (§1.9), distinctiveness items in the pre-ship checklist.
- DESIGN.md template: Brief section, mood/anti-mood, signature elements, design principles, existing-system record.
- Repository: Apache-2.0 license, NOTICE, trademark policy, Claude Code plugin marketplace manifest, install scripts (bash + PowerShell), packaging script, validator, evaluation scenarios, CI.

### Changed
- Skill renamed `product-design` → `dent`; richer trigger description; author/version metadata.
- Workflow: question-count guidance made consistent across levels; add-on routing table covers all new reference files; effort table gains a "Brief & concept" row.

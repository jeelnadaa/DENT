# How DENT Works

> DENT 2.0: the full system map (orchestration, commands, gates, catalogues, verification) is in [ARCHITECTURE.md](ARCHITECTURE.md). This page is the short conceptual tour.

## The idea

A good designer doesn't start by drawing. They ask what the product is for, decide how far to go, pick a direction on purpose, build a system, design every state, check the work, and write it down. DENT turns that process into instructions an AI agent can follow every time.

## The flow

```
 Request
   │
   ▼
 1. Mode ──────── Create · Redesign · Audit · Extend · Implement · Adopt
   │              (in a codebase: detect existing tokens / UI library first)
   ▼
 2. Questions ─── effort level first, then only what's missing,
   │              one at a time, 2–4 tailored options, one "Recommended"
   │              (or "skip — you decide" → documented defaults)
   ▼
 3. Concept ───── one-sentence concept + signature element
   │              (Polished: brief · All-out: 2–3 directions)
   ▼
 4. Foundations ─ tokens: color, type, spacing, grid, shape, elevation, icons
   │              + chosen style's overrides (41 styles)
   ▼
 5. Components ── each defined once with all states, reused everywhere
   ▼
 6. Screens ───── laws + page/flow patterns + platform rules + states
   ▼
 7. Modern layer  typography craft, motion, hover, scroll, depth
   │              (only as deep as the effort level allows)
   ▼
 7b. Web code ── Google's Modern Web Guidance decides how it's built:
   │              search → retrieve → apply → verify → disclose (native first)
   ▼
 8. Verify ────── pre-ship checklist → render & screenshot → rubric → fix
   ▼
 9. Present ───── design + short Decision Log → user approves
   ▼
10. DESIGN.md ─── source of truth; read before any future work, updated on change
```

## Three kinds of guidance

Every guideline in DENT is labeled so the agent knows how firmly to hold it:

- **[Law]** — research-backed perception and cognition (Gestalt, Fitts, Hick, Jakob…). Always applies; a style changes *how*, not *whether*.
- **[Rule]** — measurable standards (WCAG contrast, target sizes, focus, keyboard, reduced motion). **Never** overridden, in any style or effort level.
- **[Convention]** — industry defaults (8px spacing, 40px control height…). Used unless a style or the user deliberately changes them.

For web code there is a fourth source above DENT's own technique advice: **Modern Web Guidance** (Google Chrome, with Edge, Firefox and MDN). DENT's Laws and Rules say *what* must be true (contrast, targets, focus, reduced motion); MWG says *how* to build it on the web, and wins when the two differ.

## Effort levels

| Level | You get |
|---|---|
| **Essential** | Clean, consistent, correct. Fastest. |
| **Standard** | Complete professional design in a chosen style, all states, subtle motion. |
| **Polished** | Brief, typography craft, hover/scroll motion, dark mode, imagery direction, full review. |
| **All-out** | Research, brand, multiple directions, many screens, advanced motion, deep accessibility & localization, assets, metrics. |

All levels share a floor: tokens, component states, contrast, core laws, accessibility minimum, Decision Log and DESIGN.md.

## Progressive disclosure

`SKILL.md` (~350 lines) is the router: it classifies the task, routes it, and lists the gates. 55+ reference files, 41 styles, 34 command files and 7 templates are opened only when the task needs them — a dark-mode request reads the color file; a "make it look like Swiss design" request reads one style file. This keeps the agent's context small and focused.

## Extending DENT

- **New style:** copy `references/styles/_style-template.md`, fill every section, add a row to `_styles-index.md`.
- **New topic:** create a reference file, add it to the table in `SKILL.md` §9.2 and the add-on routing table in `workflow-questions-and-effort.md` §4.
- Run `python scripts/validate.py` before opening a PR.

See [CONTRIBUTING.md](../CONTRIBUTING.md).

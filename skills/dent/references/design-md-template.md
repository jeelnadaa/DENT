# DESIGN.md Template

After the user **approves** the design, create a file named `DESIGN.md` using this template. It is the single source of truth for this product's design: every future screen, component or change must follow it. Fill every section with the **final approved values** (not options). Remove sections that truly don't apply, and write "Not used" rather than leaving blanks.

Rules for writing it:
- Concrete values only (hex codes, px, ms, font names, weights). No vague words like "nice blue".
- Every major decision has a short **why**.
- Mark values that came from the user as **(user)** and values chosen by the agent as **(default)** so they can be revisited.
- Include ready-to-use tokens (CSS variables, or platform equivalents).
- Keep it updated: when the design changes, update DESIGN.md and add a changelog line.

---

```markdown
# DESIGN.md — <Product name>

> Approved on <date>. This file is the source of truth for all design work on <product>.
> Built with DENT (https://github.com/jeelnadaa/DENT). Accessibility rules ([Rule]) from the skill always apply.

## 0. Brief (Polished / All-out)
<Paste the one-page brief from design-brief-and-metrics.md §1: problem, job to be done, goal, success metrics, scope, constraints, assumptions.>

## 1. Overview
- **Product:** <what it is, one line>
- **Users:** <who, context of use>
- **Platform(s):** <web / iOS / Android / desktop>
- **Effort level:** <Essential / Standard / Polished / All-out> — sections below are filled to this depth (Essential: sections 1–7, 13, 14 minimum)
- **Design concept:** <one sentence describing the experience, using a metaphor (creative-direction.md §1)>
- **Mood / anti-mood:** <3 words> · not <2 words>
- **Signature element(s):** <the one or two things that make this product recognisable>
- **Design principles:** <3–5 trade-offs, e.g. "Clarity over density">
- **Existing system:** <none / adopted <library> / re-themed <library> — see modes-existing-products.md §2>
- **Aesthetic style:** <style name> (+ accent style if any) — why: <reason>
- **Mode:** <light / dark / both> — why: <reason>

## 2. Color
| Token | Value | Role | Source |
|---|---|---|---|
| --bg | #...... | Page background (Dominant) | (user)/(default) |
| --surface | #...... | Cards, panels | |
| --text | #...... | Primary text (Complement) | |
| --text-2 | #...... | Secondary text | |
| --border | #...... | Dividers, decorative borders | |
| --border-input | #...... | Input borders (≥ 3:1) | |
| --accent | #...... | Primary actions, links (Off color) | |
| --on-accent | #...... | Text on accent | |
| --success / --warning / --error / --info | #...... | Status | |

Contrast checks: text/bg = x.x:1 · text-2/bg = x.x:1 · on-accent/accent = x.x:1 · border-input/bg = x.x:1
Dark-mode values (if both modes): <table>

## 3. Typography
- **Display font:** <name>, weights <...> — why
- **Body/UI font:** <name>, weights <...>
- **Mono font:** <name> (if used)
| Style | Font | Size | Weight | Line height | Tracking | Use |
|---|---|---|---|---|---|---|
| Display | | | | | | Hero |
| H1 | | | | | | |
| H2 | | | | | | |
| H3 | | | | | | |
| Body | | | | | | |
| Small | | | | | | |
| Label | | | | | | Buttons, inputs |
| Caption | | | | | | |
Fluid sizes (clamp) if used: <...>

## 4. Spacing, layout and grid
- Base unit: <4/8px>; scale: <4, 8, 12, 16, 24, 32, 48, 64, 96...>
- Grid: <columns/gutters/margins per breakpoint>
- Breakpoints: <...>
- Max content width: <...>
- Density: <comfortable/compact/spacious>

## 5. Shape and depth
- Radius: control <..>, container <..>, pill <..>
- Border widths: <..>
- Elevation levels: <name: shadow value> ...
- Special surfaces: <glass/blur recipe, textures, gradients — or "Not used">

## 6. Iconography and imagery
- Icon set: <name>, stroke <..>, sizes <..>
- Imagery: <photo/illustration style, treatment, aspect ratios>

## 7. Components
For each component used: variants, sizes, dimensions, colors per state, behavior.
### Button
| Variant | Background | Text | Border | Hover | Pressed | Disabled |
|---|---|---|---|---|---|---|
Sizes: sm/md/lg heights <..>, padding <..>, font <..>, radius <..>
### Text input
...
### (Select, Checkbox, Radio, Toggle, Tabs, Card, List row, Table, Modal, Toast, Nav, etc.)
...

## 8. Motion
- Durations: instant <..> · fast <..> · normal <..> · slow <..>
- Easings: <names + cubic-bezier values>
- Signature animations: <what animates, how, when>
- Hover behaviors: <per element type>
- Scroll behaviors: <reveals, sticky, parallax — or "Not used">
- Reduced motion: <what changes>

## 9. Patterns and screens
- Navigation pattern: <...>
- Screens designed: <list with one-line purpose each>
- Key flows: <...>
- Empty / loading / error state approach: <...>

## 10. Content and voice
- Tone: <e.g. friendly, concise, confident>
- Rules: <capitalization, button label style, number/date formats>

## 11. Accessibility
- Target: WCAG 2.2 AA
- Notes specific to this design: <e.g. glass panels use 70% tint for contrast>

## 12. Tokens (copy-paste)
```css
:root { /* all tokens above as CSS variables */ }
```

## 13. Decision log
| # | Decision | Choice | Why | Source |
|---|---|---|---|---|
| 1 | Style | | | (user)/(default) |
| ... | | | | |

## 14. Changelog
- <date> — Initial approved version.
```

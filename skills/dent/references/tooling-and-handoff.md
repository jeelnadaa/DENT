# Tooling, Previews and Handoff

How to work with design tools, show work inside an agent environment, and hand a design to developers (or to another agent) without losing anything.

---

## 1. Show, don't describe — previews in agent environments

The user should **see** options and drafts, not read about them. Pick what the environment supports:

| Environment can… | Do |
|---|---|
| Render HTML (artifacts, browser preview, local file) | Build a single-file HTML preview (design-tokens-and-code.md Part 2 §11) |
| Show images | Render HTML to PNG (Playwright / headless Chrome) and show the screenshot |
| Only text | ASCII wireframes for layout + hex codes + type samples in code blocks; say clearly it's not visually verified |

### Useful preview pages (single HTML file each)
- **Style tile** (for choosing a direction): palette swatches with hex + contrast ratio, type specimen (display, heading, body, label), a button, an input, a card, one icon row, a sample of imagery treatment. One tile per direction, side by side.
- **Token sheet:** every token rendered (color chips with names, type scale ladder, spacing bars, radii, shadows, motion durations as animated dots).
- **Component sheet:** every component in every state (default, hover, focus, active, disabled, error, loading, selected) in a grid — makes inconsistencies obvious.
- **Screen previews** at 375 / 768 / 1440px.

Keep preview pages separate from production code; they're for decisions.

## 2. Figma

### 2.1 Reading from Figma (when a Figma file or Figma MCP / Dev Mode is available)
- Extract **variables** (colors, numbers, strings) and **styles** (text, effects) first; map them to DENT tokens by role, keeping names identical to code where possible.
- Read **components** and their **variants/properties** (size, state, variant) → map to code component props.
- **Auto Layout** maps directly to flexbox: direction, gap, padding, alignment, hug/fill/fixed → `fit-content` / `flex: 1` / fixed width.
- Treat Figma frames as intent, not pixels: if a frame uses a one-off value close to a token, use the token and note the discrepancy.
- Check for missing states/breakpoints in the file and design them using DENT rules rather than guessing silently.

### 2.2 Structuring a Figma file (when advising the user or generating one)
- Pages: Cover · Foundations (tokens) · Components · Patterns · Screens (by flow) · Archive.
- Variable collections: **Primitives** (raw scales) → **Semantic** (modes: Light / Dark / High contrast) → **Component** (optional). Same tiers as code (design-tokens-and-code.md Part 1).
- Components with variant properties named like code props (`variant=primary`, `size=md`, `state=hover`).
- Every frame uses Auto Layout and variables — no detached values.

## 3. Component documentation (Storybook or a docs page)
For each component:
1. Purpose and when **not** to use it.
2. Live examples of every variant, size and state.
3. Props/API table.
4. Accessibility notes (role, keyboard, labeling).
5. Content guidelines (label length, casing, truncation).
6. Do / Don't pairs with visuals.
7. Status: **Experimental → Beta → Stable → Deprecated** (with replacement and removal date).

Use Storybook interaction tests and visual regression (Chromatic/Playwright) for ongoing products.

## 4. Handoff — what developers (or the next agent) need

With tokens and component specs, pixel redlines are unnecessary. Hand off **behavior and intent**:

- **DESIGN.md** (source of truth) + exported tokens (CSS variables / DTCG JSON / platform files).
- **Screen list** with states per screen (default, empty, loading, error, success, edge cases).
- **Flow diagram** of the main tasks, including error paths and back navigation.
- **Responsive behavior:** what changes at each breakpoint (not just three static frames).
- **Interaction notes:** what happens on hover/focus/press, transitions (token names), what's optimistic, what's undoable.
- **Accessibility annotations:**
  - heading levels and landmarks per screen;
  - focus order for complex screens and where focus goes after open/close/submit/delete;
  - accessible names for icon buttons and images (alt text or "decorative");
  - live-region announcements (toasts, async results);
  - keyboard shortcuts.
- **Content:** final copy, error messages, empty-state text, character limits and truncation rules.
- **Assets:** icons (SVG, one set), images at required sizes/formats, favicons/app icons (assets-and-marketing-graphics.md).
- **Analytics events** if defined (design-brief-and-metrics.md §4).
- **Open questions** and known compromises.

## 5. Design QA (after build)
Run quality-review.md Part 1 against the built product, then file issues as: screen · breakpoint · expected (token/spec) · actual · screenshot · severity. Fix tokens before fixing instances.

## 6. Keeping DESIGN.md healthy
- One DESIGN.md per product (monorepo: one per app, or a shared one + app-level overrides).
- Every change: update the relevant section + a changelog line (date, what, why).
- When code and DESIGN.md disagree, ask which is right, then fix the other — never leave them diverged.
- Version it with the code (same repo); review design changes in PRs like code changes.

## 7. Design tools landscape (for recommendations)
- **Design & prototyping:** Figma (standard), Penpot (open source), Framer (sites), Sketch (macOS).
- **Tokens:** Tokens Studio, Style Dictionary, Figma variables export; DTCG format for interchange.
- **Docs & testing:** Storybook, Chromatic, Playwright, axe DevTools, Lighthouse.
- **Motion:** Rive, Lottie (After Effects export), Motion (Framer Motion), GSAP.
- **Icons:** Lucide, Phosphor, Heroicons, Material Symbols, Tabler (check licenses).
Recommend based on what the user already uses; don't push a tool change.

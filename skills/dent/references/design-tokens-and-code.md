# Design Tokens and Code

Part 1: how tokens are structured, named, themed and exported. Part 2: how to turn the approved design (DESIGN.md) into code on any stack, faithfully and consistently.

# Part 1 — Design tokens

Tokens are named design decisions (colors, sizes, durations…) stored once and used everywhere. They are how a design stays consistent and how DESIGN.md turns into code.

---

## 1. Three tiers

| Tier | What | Example | Used by |
|---|---|---|---|
| **1. Primitive (global/reference)** | Raw values, the full palette and scales. No meaning. | `blue-600: #2F5BEA`, `space-4: 16px`, `radius-2: 8px` | Only by tier 2 |
| **2. Semantic (alias/system)** | Meaning/purpose. Points to primitives. **Changes per theme** (light/dark/brand). | `color-accent → blue-600`, `color-text → gray-900`, `space-inset-md → space-4` | Components and layouts |
| **3. Component** | Specific component decisions. Points to semantic tokens. | `button-primary-bg → color-accent`, `input-border → color-border-input` | That component only |

Rules:
- **[Rule]** Components never use primitives directly. Dark mode or rebranding then only changes tier 2.
- Use component tokens only where a component genuinely needs to differ (avoid exploding the token count).
- One token = one decision. Don't create two semantic tokens that always hold the same value "just in case".

---

## 2. Naming convention

Pattern: `category-[type]-[item]-[variant]-[state]` (drop parts that don't apply).

Examples:
- Color: `color-bg`, `color-bg-subtle`, `color-surface`, `color-surface-raised`, `color-text`, `color-text-muted`, `color-text-on-accent`, `color-border`, `color-border-strong`, `color-accent`, `color-accent-hover`, `color-accent-pressed`, `color-focus`, `color-success`, `color-success-subtle`, `color-error`, `color-error-text`…
- Typography: `font-family-sans`, `font-size-body`, `font-weight-semibold`, `line-height-tight`, `text-heading-1` (composite)
- Spacing: `space-1 … space-16` (primitive), `space-inset-sm`, `space-stack-lg`, `space-gap-md` (semantic)
- Size: `size-control-sm|md|lg`, `size-icon-md`
- Radius: `radius-control`, `radius-container`, `radius-full`
- Border: `border-width-default`, `border-width-strong`
- Shadow/elevation: `elevation-1 … elevation-4`
- Motion: `duration-fast`, `duration-normal`, `ease-out`, `ease-standard`
- Z-index: `z-dropdown`, `z-sticky`, `z-overlay`, `z-modal`, `z-toast`
- Breakpoints: `bp-sm`, `bp-md`, `bp-lg`, `bp-xl`

Naming rules: lowercase, hyphenated, purpose not appearance (`color-accent` not `color-blue`), consistent order, no abbreviations except common ones (sm/md/lg).

---

## 3. Full token set checklist

- **Color:** neutrals scale, brand scale(s), semantic: bg/surface layers, text levels, borders (decorative + input), accent + states, focus, status (success/warning/error/info each: base, subtle background, text-on), overlays/scrim, chart categorical/sequential.
- **Typography:** families, weights, sizes (scale), line-heights, letter-spacings, composite text styles.
- **Spacing:** primitive scale + semantic aliases.
- **Sizing:** control heights, icon sizes, avatar sizes, max widths.
- **Shape:** radii, border widths.
- **Elevation:** shadows (+ dark-mode variants), blur values.
- **Motion:** durations, easings, spring presets.
- **Layout:** breakpoints, grid columns/gutters/margins, container widths.
- **Z-index** layers.
- **Opacity:** disabled, scrim, hover overlay.

---

## 4. Theming

- Light/dark/high-contrast/brand themes = different **tier 2** mappings.
```css
:root{ --color-bg: var(--gray-0); --color-text: var(--gray-900); --color-accent: var(--blue-600); }
[data-theme="dark"]{ --color-bg: var(--gray-950); --color-text: var(--gray-100); --color-accent: var(--blue-400); }
@media (prefers-contrast: more){ :root{ --color-border: var(--gray-700); --color-text-muted: var(--gray-800);} }
```
- Avoid flash of wrong theme: set the theme attribute in a tiny inline script in `<head>` before CSS paints.
- Multi-brand: same tier 3 and tier 2 names; each brand provides its own primitives + tier 2 mapping.

---

## 5. Formats and export

**Source of truth options**
- **W3C Design Tokens (DTCG) JSON** — the emerging standard (`$value`, `$type`):
```json
{
  "color": {
    "blue": { "600": { "$value": "#2F5BEA", "$type": "color" } },
    "accent": { "$value": "{color.blue.600}", "$type": "color" }
  },
  "space": { "4": { "$value": "16px", "$type": "dimension" } },
  "duration": { "fast": { "$value": "150ms", "$type": "duration" } }
}
```
- Transform to platforms with **Style Dictionary** (or Tokens Studio, Terrazzo): CSS variables, SCSS, JS/TS, Tailwind theme, iOS (Swift), Android (XML/Compose), Flutter (Dart).

**Targets**
- **CSS custom properties** — default for web.
- **Tailwind** — map semantic tokens into the theme (v4 `@theme`, v3 config) referencing the CSS variables, so `bg-accent` follows themes.
- **Figma variables** — collections: Primitives, Semantic (modes: Light/Dark), Component; keep names identical to code.
- **Native** — Swift enums/asset catalog colors; Compose `ColorScheme` + `CompositionLocal`; Flutter `ThemeExtension`.

---

## 6. Governance
- Tokens change only through DESIGN.md (with changelog).
- Deprecate before deleting (alias old → new, then remove).
- Document each semantic token's purpose in one line.
- Lint for raw values in components (stylelint `declaration-strict-value`, ESLint rules, Tailwind config restrictions).

---

# Part 2 — Implementation (turning the design into code)

A great design that is built sloppily is a bad product.

Labels: **[Rule]** must · **[Convention]** default.

---

## 1. Before writing code

1. **Read DESIGN.md** (or the current Decision Log). Every value in code comes from it.
2. **Confirm the stack** if unknown (ask once, with options): plain HTML/CSS · Tailwind · React (+ which UI library) · Vue/Svelte · Flutter · SwiftUI · Jetpack Compose · React Native. If the user doesn't care: single-file HTML + CSS for one-off pages/prototypes; React + Tailwind for apps.
3. **Create tokens first** (Part 1 of this file), then base styles (reset, typography, body colors), then components, then screens.
4. **List the components** each screen needs; build each component once and reuse it.

---

## 2. Core rules (all stacks)

- **[Rule] No magic numbers.** Colors, sizes, spacing, radii, shadows, durations and easings come from tokens. If a value isn't a token, either it should be one, or it's wrong.
- **[Rule] Semantic structure first** (web): `button` for actions, `a` for navigation, `label` for inputs, heading levels in order, landmarks (`header`, `nav`, `main`, `footer`), lists as `ul/ol`.
- **[Rule] Every interactive element has all states** from the component spec: hover, focus-visible, active, disabled, loading, error, selected.
- **[Rule] Accessibility built in:** accessible names, `aria-*` only where native semantics aren't enough, keyboard support, reduced motion, contrast as specified.
- **One component = one source.** Variants via props/classes (`variant="primary" size="md"`), never copy-pasted styles.
- **Mobile-first** responsive CSS; use the breakpoints from DESIGN.md.
- **Real content** for building and testing (and long/edge content), not lorem ipsum.
- **Performance:** animate `transform`/`opacity`, lazy-load images below the fold, set width/height or aspect-ratio on media, load only needed font weights.

---

## 3. Plain HTML + CSS

- One stylesheet with: `:root` tokens → reset → base (body, headings, links) → layout utilities → components (BEM-like or simple class names) → page-specific (minimal).
- Use CSS custom properties for tokens; dark mode overrides semantic tokens only (Part 1 §4).
- Use modern CSS: grid/flex, `gap`, `clamp()`, container queries, `:focus-visible`, `:has()` where supported, logical properties (`margin-inline`, `padding-block`) for RTL readiness.
- Minimal base reset:
```css
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;text-size-adjust:100%}
body{margin:0;font-family:var(--font-sans);font-size:var(--text-body);line-height:1.5;color:var(--text);background:var(--bg);-webkit-font-smoothing:antialiased}
img,svg,video{display:block;max-width:100%;height:auto}
button,input,select,textarea{font:inherit;color:inherit}
:focus-visible{outline:2px solid var(--focus);outline-offset:2px}
@media (prefers-reduced-motion:reduce){*{animation-duration:.01ms!important;transition-duration:.01ms!important;scroll-behavior:auto!important}}
```

## 4. Tailwind CSS

- Put tokens in the theme as described in Part 1 §5 (Tailwind v4 `@theme`, v3 `theme.extend`). Use **semantic names** (`bg-surface`, `text-muted`, `bg-accent`) — not raw palette classes (`bg-blue-600`) in components.
- Restrict the scale to the design's values (custom spacing/radius/font-size scale) so arbitrary values aren't tempting. Avoid `[13px]`-style arbitrary values; if needed often, add a token.
- Extract repeated class groups into components (React/Vue components or `@apply` in a small component layer) — don't repeat 20-class strings across files.
- Use `class-variance-authority` (cva) or similar for variants; `tailwind-merge` to merge classes safely.
- Dark mode: prefer semantic CSS variables that switch (Part 1 §4) so components don't need `dark:` everywhere; use the `dark:` variant only for exceptions.
- Use `motion-safe:` / `motion-reduce:` for animations.

## 5. React (and similar component frameworks)

- **Headless/accessible primitives** for complex widgets (dialog, popover, menu, combobox, tabs, tooltip, select): Radix UI, React Aria, Headless UI, Ark UI. Don't hand-roll focus traps and keyboard handling unless necessary.
- **shadcn/ui** is a good base (copy-in components on Radix + Tailwind): restyle its tokens to DESIGN.md, don't ship its default look unchanged (avoid the generic look — see quality-review.md anti-patterns).
- Component API: `variant`, `size`, `disabled`, `loading`, `asChild`/polymorphic where useful; forward refs; spread remaining props.
- Folder structure: `tokens/` (or `styles/tokens.css`), `components/ui/` (primitives: Button, Input…), `components/` (composed: PricingCard…), `pages|app/`.
- Animation: CSS transitions for simple states; **Motion (Framer Motion)** for layout animations, shared elements, gestures, springs; respect `useReducedMotion`.
- Icons: one library (Lucide, Phosphor, Heroicons, Material Symbols) imported per icon; consistent size/stroke via a wrapper.
- Forms: React Hook Form + schema validation (Zod); show errors per field per forms pattern.
- Charts: Recharts, Visx, ECharts, Chart.js, Observable Plot — style with chart tokens (see data-visualization.md).

## 6. Vue / Svelte
- Same principles: tokens as CSS variables, primitives from accessible headless libs (Radix Vue / Reka UI, Headless UI, Bits UI/Melt UI for Svelte), variants via props, one component per element type.

## 7. Flutter
- Define `ThemeData` with `ColorScheme` (from DESIGN.md colors), `TextTheme` (type scale), and component themes (`FilledButtonThemeData`, `InputDecorationTheme`, `CardTheme`…). Put extra tokens in a `ThemeExtension` (spacing, radii, durations).
- Use `MediaQuery`/`LayoutBuilder` for responsive layouts; respect `textScaler` (don't clamp text scaling away).
- Use `Semantics` for custom widgets; minimum tap targets 48dp.
- Motion: implicit animations (`AnimatedContainer`…), `Hero` for shared elements, curves from tokens.

## 8. SwiftUI (iOS/macOS)
- Colors in the asset catalog with Any/Dark (+ high contrast) appearances; semantic names (`Color("Accent")`).
- Use system text styles (`.font(.body)`) or custom fonts with `relativeTo:` so Dynamic Type works.
- Spacing/radius constants in an enum (`DS.Spacing.md`).
- Native components (NavigationStack, TabView, List, sheets) styled with modifiers; custom `ButtonStyle`s for variants.
- Animations: `.animation(.spring(response:dampingFraction:))`, `matchedGeometryEffect`; check `accessibilityReduceMotion`.
- Accessibility: `.accessibilityLabel`, `.accessibilityHint`, traits.

## 9. Jetpack Compose (Android)
- `MaterialTheme(colorScheme, typography, shapes)` built from DESIGN.md tokens; custom tokens via `CompositionLocal`.
- Use Material 3 components; `Modifier.minimumInteractiveComponentSize()` (48dp).
- Edge-to-edge with `WindowInsets`; window size classes for adaptive layout.
- `contentDescription` on icons/images; `semantics {}` for custom components.

## 10. React Native / Expo
- Theme object with tokens; a `StyleSheet` per component; variants via props.
- Respect platform differences (navigation, back behavior, fonts, haptics) — see platforms-and-devices.md.
- `accessibilityLabel`, `accessibilityRole`, `hitSlop` for small targets; Reanimated for performant animation.

---

## 11. Single-file deliverables (prototypes, artifacts, demos)
- One HTML file with `<style>` (tokens at top) and minimal `<script>`.
- Load fonts from a CDN (e.g. Google Fonts) with `display=swap`; fallback stack.
- Images: real/free sources the user provided, or neutral placeholders with correct aspect ratios (never broken image icons).
- Include all states that matter for the demo (hover, focus, an empty or error example if relevant).

---

## 12. Code quality checklist
- [ ] All values from tokens; no stray hex codes or px values in components.
- [ ] Each UI element type implemented once and reused.
- [ ] All component states implemented.
- [ ] Semantic HTML / native components; keyboard and screen reader work.
- [ ] Responsive at all breakpoints; no horizontal scroll at 320px (except tables/media).
- [ ] Reduced motion respected; animations only on transform/opacity.
- [ ] Dark mode (if in scope) switches semantic tokens only.
- [ ] No console errors; fonts and images load; no layout shift.
- [ ] Visual verification done (see `quality-review.md` Part 1).

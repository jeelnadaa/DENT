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
- **Built-in surfaces:** tooltip, scrollbar thumb/track, control accent, range track/fill/thumb, selection, caret, placeholder, autofill ring (`built-in-surfaces.md` §3).

---

## 4. Theming

- Light/dark/high-contrast/brand themes = different **tier 2** mappings.
- Light/dark on the web follows `mwg:dark-mode`: declare `<meta name="color-scheme" content="light dark">`, set `color-scheme` on `:root` (not `body`), and map tier 2 tokens with `light-dark()` (with the guide's fallback for older browsers). A user toggle only overrides `color-scheme` (`mwg:dark-mode-toggle`).
```css
:root{
  color-scheme: light dark;
  --color-bg: light-dark(var(--gray-0), var(--gray-950));
  --color-text: light-dark(var(--gray-900), var(--gray-100));
  --color-accent: light-dark(var(--blue-600), var(--blue-400));
}
:root[data-theme="light"]{ color-scheme: light; }   /* stored override from a toggle */
:root[data-theme="dark"]{ color-scheme: dark; }
@media (prefers-contrast: more){ :root{ --color-border: var(--gray-700); --color-text-muted: var(--gray-800);} }
```
- Avoid flash of wrong theme: the `<meta name="color-scheme">` plus, with a toggle, a tiny classic inline script right after it that applies the stored override (not `type=module`, not `defer`; `mwg:dark-mode-toggle`). Store an override only when it differs from the system setting.
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
- **Performance:** animate `transform`/`opacity`, lazy-load images below the fold but never the LCP image (give it `fetchpriority="high"`), set width/height or aspect-ratio on media, load only needed font weights (`mwg:optimize-image-priority`, `mwg:performance`).
- **[Rule] Web implementation follows Modern Web Guidance.** Before writing any HTML/CSS/client-side JS capability, search and retrieve its MWG guide and apply it (`modern-web-guidance.md`). Where this file and a guide differ, the guide wins.

---

## 3. Plain HTML + CSS

- One stylesheet in cascade layers: `@layer reset, base, layout, components, utilities;` with `:root` tokens, then reset → base (body, headings, links) → layout → components (BEM-like or simple class names) → page-specific (minimal). Use native CSS nesting where it helps readability (`mwg:css`).
- Use CSS custom properties for tokens; dark mode overrides semantic tokens only (Part 1 §4), with `color-scheme` and `light-dark()` (`mwg:dark-mode`).
- Use modern CSS: grid/flex, `gap`, `clamp()`, container queries, `:focus-visible`, `:has()`, logical properties (`margin-inline`, `padding-block`) for RTL readiness. Browser support and fallbacks come from each feature's MWG guide.
- Type sizes in `rem` (px values in DESIGN.md are design units: 16 px = 1 rem). Controls and anything containing text get `min-block-size`, never a fixed `height` (`mwg:typography`). Mobile full-height sections use `dvh`, not `vh` (`mwg:responsive-design`).
- Minimal base reset: element-scoped and zero-specificity in the lowest layer, **no rules on `*`** (they can't be overridden by web components or later layers; `mwg:css`) and **no global reduced-motion kill switch** (`mwg:motion`):
```css
@layer reset, base, layout, components, utilities;
@layer reset {
  :where(html){-webkit-text-size-adjust:100%;text-size-adjust:100%;box-sizing:border-box}
  :where(body,div,section,article,aside,header,footer,main,nav,form,fieldset,ul,ol,li,dialog,[popover],a,button,input,select,textarea,img,video,canvas,svg){box-sizing:inherit}
  :where(body){margin:0}
  :where(img,svg,video,canvas,picture){display:block;max-inline-size:100%;block-size:auto}
  :where(button,input,select,textarea){font:inherit;color:inherit}
}
@layer base {
  body{font-family:var(--font-sans);font-size:var(--text-body);line-height:1.5;color:var(--text);background:var(--bg)}
  :where(a:any-link,button,input,select,textarea,summary,[tabindex]):focus-visible{outline:2px solid var(--focus);outline-offset:2px}
}
```
- **Reduced motion is handled per rule, next to the animation** (`mwg:motion`): if reduced motion means *no animation*, declare it only inside `@media (prefers-reduced-motion: no-preference)`; if it means *gentler animation* (spinners, progress), override only the changed parameters inside `@media (prefers-reduced-motion: reduce)`. Keep color/opacity feedback transitions; drop movement, scaling, parallax and loops.
```css
.card{
  transition:background-color var(--dur-fast) var(--ease-standard);
  @media (prefers-reduced-motion:no-preference){transition:background-color var(--dur-fast) var(--ease-standard),translate var(--dur-base) var(--ease-out)}
}
html{@media (prefers-reduced-motion:no-preference){scroll-behavior:smooth}}
```

## 4. Tailwind CSS

- Put tokens in the theme as described in Part 1 §5 (Tailwind v4 `@theme`, v3 `theme.extend`). Use **semantic names** (`bg-surface`, `text-muted`, `bg-accent`) — not raw palette classes (`bg-blue-600`) in components.
- Restrict the scale to the design's values (custom spacing/radius/font-size scale) so arbitrary values aren't tempting. Avoid `[13px]`-style arbitrary values; if needed often, add a token.
- Extract repeated class groups into components (React/Vue components or `@apply` in a small component layer) — don't repeat 20-class strings across files.
- Use `class-variance-authority` (cva) or similar for variants; `tailwind-merge` to merge classes safely.
- Dark mode: prefer semantic CSS variables that switch (Part 1 §4) so components don't need `dark:` everywhere; use the `dark:` variant only for exceptions.
- Use `motion-safe:` for animations that reduced motion removes, and `motion-reduce:` only to soften parameters (the per-rule strategy of `mwg:motion`); never a global reset. Tailwind's preflight is acceptable as the project's existing reset; don't add a second `*` reset on top.

## 5. React (and similar component frameworks)

- **Native first** (`modern-web-guidance.md` §5): `<dialog>` + `showModal()`, `popover`/`popover="hint"` + anchor positioning, `<details name>`, `<input type="checkbox" switch>`, customizable `<select>`, rendered from components via refs, with MWG's framework adaptations (typed new attributes, SSR guards, `useId()` for ids and anchor names). Never hand-roll focus traps or scroll locks around a native modal.
- **Headless/accessible primitives** (Radix UI, Base UI, React Aria, Headless UI, Ark UI) when the project already uses them, or for widgets the platform doesn't cover (async combobox, date-range picker, data grid). Don't hand-roll complex keyboard handling.
- **shadcn/ui** is a fine base when a project already uses it or needs many library-only widgets: restyle its tokens to DESIGN.md, don't ship its default look unchanged (avoid the generic look — see quality-review.md anti-patterns). Use its native-capable parts the MWG way rather than adding new JS overlays.
- Component API: `variant`, `size`, `disabled`, `loading`, `asChild`/polymorphic where useful; forward refs; spread remaining props.
- Folder structure: `tokens/` (or `styles/tokens.css`), `components/ui/` (primitives: Button, Input…), `components/` (composed: PricingCard…), `pages|app/`.
- Animation: CSS transitions, `@starting-style` and view transitions for states, entry/exit and shared elements (`mwg:animate-element-entry-exit`, `mwg:same-document-transitions`); **Motion (Framer Motion)** for gesture physics and layout choreography the platform can't express; respect `useReducedMotion` with the same per-rule strategy.
- Icons: one library (Lucide, Phosphor, Heroicons, Material Symbols) imported per icon; consistent size/stroke via a wrapper.
- Forms: React Hook Form + schema validation (Zod); show errors per field per forms pattern.
- Charts: Recharts, Visx, ECharts, Chart.js, Observable Plot — style with chart tokens (see data-visualization.md).

## 6. Vue / Svelte
- Same principles: tokens as CSS variables, native elements first per MWG, then accessible headless libs where needed (Reka UI, Headless UI, Bits UI/Melt UI for Svelte), variants via props, one component per element type.

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
- [ ] MWG guides retrieved for every web capability built; their MANDATORY rules and fallbacks applied (G13).
- [ ] Responsive at all breakpoints; no horizontal scroll at 320px (except tables/media).
- [ ] Reduced motion respected per rule (no global `*` reset); animations only on transform/opacity.
- [ ] Dark mode (if in scope) switches semantic tokens only.
- [ ] No console errors; fonts and images load; no layout shift.
- [ ] Visual verification done (see `quality-review.md` Part 1).

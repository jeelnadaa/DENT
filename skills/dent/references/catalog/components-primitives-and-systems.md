# Catalogue: Accessible Primitives and Complete Component Systems

Read `README.md` for field meanings and the status legend (✓ checked 2026-11-14 · K from knowledge, verify · ⚠ caveat). Selection method: `component-selection.md`.

---

## 1. Accessible primitives (unstyled behaviour; you own the look)

| Library | Frameworks | What you get | Styling | Accessibility | Licence | Use when | Avoid when | Status |
|---|---|---|---|---|---|---|---|---|
| [Radix UI Primitives](https://www.radix-ui.com/primitives) | React | Dialog, popover, dropdown/context menu, tabs, accordion, select, slider, toast, tooltip, navigation menu… | Unstyled, `data-state` attributes, `asChild` composition | Strong WAI-ARIA patterns, focus management | MIT | Custom design on React; base of shadcn/ui | You need a date picker/combobox depth (gaps) or non-React | K |
| [Base UI](https://base-ui.com) | React | Successor team of Radix/MUI Base/Floating UI: dialog, menu, select, combobox, slider, tabs, toast, field/form… | Unstyled, render props/`render` | Strong; actively developed | MIT | New React projects wanting modern primitives; replacing deprecated `@mui/base` | You already standardised on Radix | ✓ 2026-11-14 (v1.x stable; npm `@base-ui/react`; old `@mui/base` deprecated) |
| [React Aria / React Aria Components](https://react-spectrum.adobe.com/react-aria/) | React | Most complete set incl. date/time pickers, calendars, combobox, grid list, table, drag and drop, i18n | Unstyled hooks or components with render props/data attributes | Best-in-class (Adobe), internationalised, touch/pointer normalisation | Apache-2.0 | Accessibility-critical apps, date-heavy UIs, i18n | You want the smallest bundle for 2 widgets | K |
| [React Spectrum](https://react-spectrum.adobe.com/) | React | Adobe's styled system on React Aria | Spectrum design language | Excellent | Apache-2.0 | Adobe-like enterprise tools | Custom brand identity | K |
| [Headless UI](https://headlessui.com) | React, Vue | Menu, listbox, combobox, dialog, disclosure, popover, radio group, switch, tabs, transition | Unstyled, Tailwind-friendly | Good | MIT | Tailwind projects needing a few widgets | You need many widgets (smaller set) | K |
| [Ark UI](https://ark-ui.com) | React, Vue, Solid, Svelte | 40+ components built on Zag state machines | Unstyled, data attributes; pairs with Panda CSS/Park UI | Good | MIT | Multi-framework teams; Chakra v3 ecosystem | Simple React-only projects already on Radix | K |
| [Zag.js](https://zagjs.com) | Framework-agnostic (adapters) | State machines for components (the engine under Ark) | You build the DOM | Good when wired correctly | MIT | Building your own component library across frameworks | You just want ready components (use Ark) | K |
| [Melt UI](https://melt-ui.com) / [Bits UI](https://bits-ui.com) | Svelte | Builders / headless components for Svelte | Unstyled | Good | MIT | Svelte projects (Bits UI powers shadcn-svelte) | React projects | K |
| [Reka UI](https://reka-ui.com) (formerly Radix Vue) | Vue | Radix-like primitives for Vue | Unstyled | Good | MIT | Vue projects (powers shadcn-vue) | React | K |
| [Kobalte](https://kobalte.dev) | Solid | Accessible primitives for SolidJS | Unstyled | Good | MIT | Solid projects | Other frameworks | K |
| [Floating UI](https://floating-ui.com) | Agnostic + React/Vue | Positioning for tooltips/popovers/menus (collision, flip, shift) | n/a | Provides interaction hooks; you add semantics | MIT | Custom floating elements | You're already using a primitive that includes it | K |
| [Downshift](https://www.downshift-js.com) | React | Combobox/select/multiselect hooks | Unstyled | Good (WAI-ARIA combobox) | MIT | Custom autocomplete | You want full component kits | K |

**Default choice (React, custom brand):** shadcn/ui (Radix or Base UI underneath) + your tokens. **Accessibility-critical or date-heavy:** React Aria Components.

## 2. Copy-in foundation: shadcn/ui

| Library | Frameworks | Role | Styling | Accessibility | Licence | Use when | Avoid when | Status |
|---|---|---|---|---|---|---|---|---|
| [shadcn/ui](https://ui.shadcn.com) | React (Next, Vite, Remix…); ports: shadcn-vue, shadcn-svelte | Collection + CLI/registry: copies component source (on Radix or Base UI primitives) into your repo | Tailwind CSS + CSS variables; you own and edit the code | Inherits the primitives' a11y; your edits can break it | MIT | You want full control and a fast start; DENT tokens map to its CSS variables | You ship its default zinc/neutral look unchanged (anti-slop); no Tailwind and no desire to adopt it | K |

Rules: re-theme every token (radius, colors, fonts, shadows) to DESIGN.md; add missing states; keep the registry components in `components/ui`.

## 3. Complete styled systems

| Library | Frameworks | Character | Theming | Accessibility | Licence | Use when | Avoid when | Status |
|---|---|---|---|---|---|---|---|---|
| [MUI (Material UI)](https://mui.com/material-ui/) | React | Material Design, huge component set; MUI X for data grid, date pickers, charts, tree view | Theme object, `sx`, CSS variables mode | Good | Core MIT; **MUI X Pro/Premium paid** (advanced grid features, etc.) | Enterprise apps, Material look acceptable, big team | Distinctive brand look needed with little time to re-theme | K |
| [Joy UI](https://mui.com/joy-ui/) | React | MUI's non-Material styled set | CSS variables | Good | MIT ⚠ development slowed; check status | — | New long-lived projects (check maintenance) | K |
| [Mantine](https://mantine.dev) | React | 100+ components + hooks, dates, charts, notifications, spotlight, rich text (Tiptap) | CSS modules + CSS variables, theme object | Good | MIT | Fast full-featured apps/dashboards, great DX | You need zero-runtime Tailwind-only stack | K |
| [Ant Design](https://ant.design) | React (ports: Vue, Angular) | Enterprise/admin, very complete (tables, forms, trees) | Design tokens (CSS-in-JS) | Fair–good; some patterns need checking | MIT | Admin/back-office, data-dense enterprise | Consumer brands wanting a unique feel | K |
| [Chakra UI](https://chakra-ui.com) | React | Style-props system; v3 built on Ark UI + Panda-style recipes | Tokens, recipes | Good | MIT | Teams liking style props and themes | Projects avoiding runtime styling (check v3 approach) | K |
| [HeroUI](https://www.heroui.com) (formerly NextUI) | React | Modern, polished look on React Aria + Tailwind | Tailwind plugin, themes | Good (React Aria) | MIT (pro templates/products may be paid) | Polished consumer UIs with Tailwind | You want unstyled control | K |
| [PrimeReact](https://primereact.org) (PrimeVue, PrimeNG, PrimeFaces) | React, Vue, Angular | Very large set incl. data table, tree table, editor, charts | Styled themes or unstyled "pass-through" mode | Good | MIT; **premium themes/templates paid** | Enterprise across frameworks; Angular/Vue teams | Minimal bundles | K |
| [Fluent UI](https://react.fluentui.dev) | React (v9), Web Components | Microsoft Fluent 2 design | Tokens, Griffel CSS-in-JS | Strong | MIT | Microsoft-ecosystem apps, Teams/Office add-ins | Non-Microsoft brand identity | K |
| [Carbon Design System](https://carbondesignsystem.com) | React, Web Components, Angular, Vue (community) | IBM's system; data tables, UI shell, charts | Sass tokens, themes (white, g10, g90, g100) | Strong (IBM a11y) | Apache-2.0 | Enterprise, data-heavy, accessibility-required | Playful consumer apps | K |
| [Ant Design Pro / ProComponents](https://procomponents.ant.design) | React | Admin scaffolding on AntD | AntD tokens | as AntD | MIT | Fast admin dashboards | Bespoke design | K |
| [Vuetify](https://vuetifyjs.com) | Vue | Material-based full system | Theme, SASS variables | Good | MIT | Vue + Material | Custom identity | K |
| [Quasar](https://quasar.dev) | Vue | Full framework (SPA, SSR, mobile, desktop) + components | Theme | Good | MIT | Vue apps for many targets | Small sites | K |
| [Angular Material / CDK](https://material.angular.io) | Angular | Material components + CDK behaviour primitives | Theming API | Strong | MIT | Angular apps (CDK for custom components) | Non-Angular | K |
| [Skeleton](https://www.skeleton.dev) | Svelte (+ React) with Tailwind | Themeable system | Tailwind themes | Good | MIT | Svelte + Tailwind | React-only teams | K |
| [daisyUI](https://daisyui.com) | Any (Tailwind plugin, CSS classes) | Semantic class names (`btn`, `card`) with themes | Tailwind plugin themes | Depends on your markup (CSS only) | MIT | Quick themed prototypes, non-React stacks | Complex widgets (no JS behaviour) | K |
| [Park UI](https://park-ui.com) | React, Vue, Solid | Styled Ark UI components with Panda/Tailwind | Tokens | Good | MIT | Ark-based styled starting point | — | K |
| [Tamagui](https://tamagui.dev) | React + React Native | Universal UI with optimizing compiler | Tokens/themes | Good | MIT | Shared web + native UI | Web-only projects | K |
| [React Native Paper](https://reactnativepaper.com) / [NativeBase→gluestack-ui](https://gluestack.io) | React Native | Material (Paper) / universal components (gluestack) | Themes | Varies | MIT | RN apps | Web | K |
| [Flutter Material 3 / Cupertino](https://docs.flutter.dev/ui/widgets) | Flutter | Built-in widget sets | ThemeData | Good with Semantics | BSD-3 | Flutter apps | — | K |
| [SwiftUI](https://developer.apple.com/xcode/swiftui/) / [Jetpack Compose Material 3](https://developer.android.com/jetpack/compose) | iOS / Android | Native toolkits | Native theming | Native a11y | Platform | Native apps | Cross-platform | K |
| [Shoelace → Web Awesome](https://webawesome.com) | Web Components (any framework) | Framework-agnostic components | CSS parts/variables | Good | Shoelace MIT; **Web Awesome has free core + paid Pro** | Multi-framework, CMS sites | — | K |
| [Lit](https://lit.dev) | Web Components | Library for building your own components | Your CSS | You implement | BSD-3 | Building a framework-agnostic design system | Quick apps | K |

## 4. Mapping DENT tokens onto a system
- **shadcn/ui, daisyUI, HeroUI:** set CSS variables (`--background`, `--foreground`, `--primary`, `--radius`, …) from DESIGN.md semantic tokens; load fonts via `--font-sans`/`--font-display`.
- **MUI:** `createTheme({ palette, typography, shape: { borderRadius }, shadows, components: { MuiButton: { styleOverrides } } })`; enable CSS variables mode for dark/light.
- **Mantine:** `createTheme({ colors, primaryColor, fontFamily, headings, radius, spacing, shadows })`; `MantineProvider` with `defaultColorScheme`.
- **Ant Design:** `ConfigProvider` with `theme.token` (colorPrimary, borderRadius, fontFamily) and `components` overrides.
- **Chakra v3:** `createSystem(defaultConfig, { theme: { tokens, semanticTokens, recipes } })`.
- **Carbon/Fluent:** use their token systems; map DENT semantic roles to their theme tokens rather than overriding component CSS.
Always re-check focus rings, disabled contrast and error colors after theming.

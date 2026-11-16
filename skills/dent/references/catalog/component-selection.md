# Component and Library Selection Method

Pick the right building block for **this** project. Used by `/dent:components`, `/dent:create`, `/dent:extend`, `/dent:implement`, and any time you're about to write a complex widget (dialog, combobox, date picker, data grid, editor, carousel, command palette, drag-and-drop) from scratch.

---

## 1. Detect the project (5 minutes)
- Framework and version (React/Next, Vue/Nuxt, Svelte/SvelteKit, Solid, Angular, Astro, plain HTML, React Native, Flutter, SwiftUI, Compose).
- Language (TS/JS), rendering (SSR/RSC/SPA/static), styling (Tailwind v3/v4, CSS Modules, CSS-in-JS, vanilla CSS, Sass).
- Existing libraries in `package.json` (UI, headless, icons, animation, charts, forms, tables, toasts). **An existing library that does the job wins by default.**
- Constraints: bundle budget, licence policy (some companies forbid GPL/AGPL), accessibility requirements, browser support.

## 2. List needs as jobs
Write each need as a job with acceptance criteria: "Sortable, filterable table of up to 50 000 rows with keyboard row actions" — not "a table library".

## 3. Choose the layer for each job

| Situation | Prefer |
|---|---|
| Existing design system in the project | Its components; extend them |
| Anything the web platform now does natively (modal, popover, menu, tooltip, disclosure/accordion, switch, styled select, tabs, carousel, drawer, toasts, view/scroll animations) | **Native HTML/CSS per Modern Web Guidance**, styled with your tokens (`../modern-web-guidance.md` §5); no new dependency |
| Custom visual identity, React, widgets the platform doesn't cover | **Primitives** (Radix, Base UI, React Aria, Ark) styled with your tokens, often via **shadcn/ui** as a starting point |
| Need speed, enterprise screens, consistency over uniqueness | **System** (MUI, Mantine, Ant Design, Fluent, Carbon, PrimeReact) themed to tokens |
| One hard widget (grid, editor, calendar, flow editor, DnD) | **Specialized** library |
| Marketing flourishes (animated hero, marquee, spotlight) | **Collection** pieces (Magic UI, Aceternity, Motion Primitives…) copied and restyled; keep only what serves the concept |
| Animation | CSS and Web Animations per `mwg:motion` first; then one runtime for what the platform can't express (see `../motion/motion-tech-catalog.md`) |
| Non-React (Vue, Svelte, Solid, vanilla) | Framework-agnostic primitives (Zag.js/Ark UI, Melt UI/Bits UI for Svelte, Reka UI/Radix Vue for Vue) or web components |

## 4. Compare the shortlist (2–3 options per job)

| Criterion | Question |
|---|---|
| Compatibility | Works with this framework version, SSR/RSC, TypeScript, styling approach? |
| Accessibility | Keyboard, focus, ARIA patterns correct out of the box? Known gaps? |
| Customisation | Can it match DESIGN.md tokens without fighting overrides? |
| Performance | Bundle size, tree-shaking, rendering cost, virtualisation? |
| Licence | MIT/Apache/BSD? Copyleft? Paid tiers needed for the features you need? |
| Maintenance | Recent releases, open-issue health, maintained notice? |
| Design fit | Does its default look/feel suit the direction, or will it pull the design toward its own identity? |
| Overlap | Does it duplicate something already installed? |

Write the comparison as a small table; recommend one with the trade-off in one sentence.

## 5. Rules
- **One library per job.** No two toast libraries, two animation engines doing the same thing, or two component systems.
- **Never ship a library's default look unchanged** when the project has its own direction (restyle shadcn/MUI/Mantine tokens).
- **Native platform first** (`../modern-web-guidance.md` §5): before adding any UI dependency, search MWG for the capability; add a library only when the platform has no primitive, the project already standardised on one, or the browser-support policy rules out the native feature and its fallback. Log the reason.
- Prefer primitives over hand-rolled comboboxes and date pickers; never hand-roll a focus trap around a native `<dialog>`.
- Check the licence on the official page for the version you install; record it in DESIGN.md.
- Paid components/templates: say they're paid before recommending; offer a free alternative.
- Unmaintained libraries (e.g. Vaul's repo carries an unmaintained notice as of 2026): use only if stable enough for the job, and say so.
- After installing: theme it, then verify keyboard and screen-reader behaviour yourself (libraries can be misconfigured).

## 6. Quick picks (starting points, not autopilot)

| Job | First look at | Alternatives |
|---|---|---|
| Dialog, popover, menu, tabs, tooltip, accordion, switch | **Native** per MWG (`mwg:dialog`, `mwg:menu`, `mwg:tabs`, `mwg:interest-triggered-tooltips`, `mwg:accordion`, `mwg:switch`) | Radix / Base UI via shadcn/ui, React Aria Components, Ark UI, Headless UI when the project already uses them |
| Select (no search) | Native customizable `<select>` (`mwg:branded-select-styling`) | Library select only if the project already has one |
| Combobox / select with search | React Aria Combobox, Base UI, cmdk-based | Downshift, Headless UI |
| Date picker / calendar input | React Aria DatePicker, react-day-picker | Mantine Dates, MUI X (pro features paid) |
| Toasts | Native `popover="manual"` stack (`mwg:persistent-toast-notifications`) | Sonner, Radix Toast, react-hot-toast |
| Mobile drawer / bottom sheet | Native `<dialog>` + scroll snap (`mwg:navigation-drawer`) | Base UI/Radix Dialog styled as sheet; Vaul (⚠ unmaintained notice); Gorhom bottom sheet (React Native) |
| Command palette | cmdk | kbar |
| Data table | TanStack Table (+ TanStack Virtual) | AG Grid Community (Enterprise paid), MUI X Data Grid |
| Spreadsheet-like grid | AG Grid, Glide Data Grid | Handsontable (commercial licence for most uses) |
| Charts | Recharts (simple), ECharts (rich/large), Visx (custom), Observable Plot | Nivo, Chart.js, Tremor (dashboards) |
| Rich text | Tiptap, Lexical | Plate, Slate, Quill |
| Drag and drop | Native pointer events per `mwg:drag-and-drop` for simple lists; dnd-kit, Pragmatic drag and drop for boards and trees | react-dnd |
| Node/flow editor | React Flow (xyflow) | Rete.js |
| Calendar/scheduler | FullCalendar (premium plugins paid), Schedule-X | react-big-calendar |
| Carousel | Native scroll snap + buttons (`mwg:carousel`) | Embla Carousel, Swiper, Keen Slider |
| Animated numbers | NumberFlow | Motion `animate()` |
| Forms | React Hook Form + Zod/Valibot | TanStack Form, Conform |
| Maps | MapLibre GL (open), Leaflet | Mapbox GL (account + paid tiers) |
| File upload | Uppy, react-dropzone | FilePond |
| Icons | Lucide, Phosphor, Tabler, Heroicons, Material Symbols | Iconoir, Remix Icon |

Details, licences and caveats are in the catalogue files.

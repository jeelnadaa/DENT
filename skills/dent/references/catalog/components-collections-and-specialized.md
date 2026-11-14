# Catalogue: Collections, Specialized Components and Templates

Status legend in `README.md` (✓ checked 2026-11-14 · K from knowledge, verify · ⚠ caveat). Selection method: `component-selection.md`.

---

## 1. Copy-and-customize visual collections (marketing and creative UI)

These give eye-catching pieces (animated heroes, marquees, spotlights, bento grids, text effects). Treat them as **raw material**: take a piece only when it serves the concept, then restyle it to your tokens. Many have free MIT components plus paid "Pro" templates.

| Collection | Stack | What it's good for | Licence | Watch-outs | Status |
|---|---|---|---|---|---|
| [Magic UI](https://magicui.design) | React, Tailwind, Motion | Animated marquee, number tickers, shimmer buttons, globe, bento, text animations | Components MIT; **Magic UI Pro templates paid** | Easy to over-decorate; many effects lack reduced-motion handling — add it | K |
| [Aceternity UI](https://ui.aceternity.com) | React, Tailwind, Motion | Spotlight, 3D cards, parallax, background beams, text generate effects | Free components (check site licence); **Pro paid** | Very recognisable "AI startup" look → anti-slop risk; heavy effects | K |
| [Motion Primitives](https://motion-primitives.com) | React, Tailwind, Motion | Text effects, morphing dialogs, animated groups, tilt, spotlight | MIT (Pro tier exists) | Add reduced-motion variants | K |
| [Cult UI](https://www.cult-ui.com) | React, shadcn-style | Dynamic island, texture buttons, expandable cards | MIT (pro blocks may be paid) | Check per-component deps | K |
| [Eldora UI](https://www.eldoraui.site) | React, Tailwind, Motion | Animated components and templates | MIT (verify) | Smaller community | K |
| [Origin UI](https://originui.com) | React, Tailwind, shadcn | Hundreds of form inputs, buttons, tables, navs in shadcn style | MIT | Great for forms/inputs breadth | K |
| [Kokonut UI](https://kokonutui.com) | React, Tailwind | Modern components and blocks | MIT (Pro paid) | — | K |
| [shadcn blocks / registry ecosystems](https://ui.shadcn.com/blocks) | React | Full sections (login, dashboard, sidebar) | MIT | Ship restyled, not default | K |
| [Tailwind Plus (formerly Tailwind UI)](https://tailwindcss.com/plus) | HTML/React/Vue + Tailwind | Professionally designed sections, app UIs, templates | **Paid licence** (per person/team) | Don't recommend unless the user owns it | K |
| [Tremor](https://tremor.so) | React, Tailwind, Recharts | Dashboard components: KPI cards, charts, tables | Apache-2.0 (blocks/templates: check) | Default look is common; re-theme | K |
| [Flowbite](https://flowbite.com) | Tailwind (+ React, Vue, Svelte) | Broad component classes + JS | MIT core; **Pro paid** | — | K |
| [HyperUI](https://www.hyperui.dev) / [Preline](https://preline.co) | Tailwind HTML | Free sections and components | MIT (Preline Pro paid) | Static; add behaviour/a11y yourself | K |
| [Uiverse](https://uiverse.io) | HTML/CSS | Community CSS buttons, loaders, toggles | MIT (community-submitted; check each) | Quality varies; a11y often missing | K |

## 2. Specialized components (one job, done well)

| Library | Job | Frameworks | Licence | Notes | Status |
|---|---|---|---|---|---|
| [Sonner](https://sonner.emilkowal.ski) | Toasts | React | MIT | Elegant stacking, promise toasts; announce via live region (built in) | K |
| [Vaul](https://vaul.emilkowal.ski) | Drawer / bottom sheet | React | MIT | ⚠ repo marked unmaintained by its author; works, but prefer Base UI/Radix dialog styled as a sheet for new long-lived projects | ✓ 2026-11-14 |
| [cmdk](https://cmdk.paco.me) | Command palette / menu | React | MIT | Unstyled, fast fuzzy filtering; used by shadcn Command | K |
| [kbar](https://kbar.vercel.app) | Command palette | React | MIT | Alternative with actions registry | K |
| [NumberFlow](https://number-flow.barvian.me) | Animated numbers | React, Vue, Svelte, vanilla | MIT | Accessible number transitions, tabular digits | K |
| [Embla Carousel](https://www.embla-carousel.com) | Carousel | Vanilla + React/Vue/Svelte/Solid | MIT | Lightweight, unstyled, great touch physics | K |
| [Swiper](https://swiperjs.com) | Advanced sliders/carousels | Vanilla, React, Vue, Web Components | MIT | Many effects (cube, coverflow, cards); heavier | K |
| [Keen Slider](https://keen-slider.io) | Slider | Vanilla + adapters | MIT | Small, flexible | K |
| [TanStack Table](https://tanstack.com/table) | Headless data tables | React, Vue, Solid, Svelte, Angular, Lit | MIT | You render the table; pair with TanStack Virtual for large data | K |
| [AG Grid](https://www.ag-grid.com) | Enterprise data grid | JS, React, Angular, Vue | **Community MIT; Enterprise commercial** | Pivoting, grouping, Excel export etc. are Enterprise | K |
| [Glide Data Grid](https://grid.glideapps.com) | Canvas spreadsheet-like grid | React | MIT | Millions of rows; canvas → check a11y | K |
| [MUI X Data Grid](https://mui.com/x/react-data-grid/) | Data grid | React | MIT (Community) / **Pro & Premium paid** | Integrates with MUI | K |
| [FullCalendar](https://fullcalendar.io) | Calendars/scheduling | Vanilla, React, Vue, Angular | **Standard MIT; Premium plugins (timeline, resources) commercial** | Mature | K |
| [Schedule-X](https://schedule-x.dev) | Calendar | Vanilla + adapters | MIT (premium plugins paid) | Modern alternative | K |
| [react-day-picker](https://daypicker.dev) | Date picker | React | MIT | Used by shadcn Calendar | K |
| [Tiptap](https://tiptap.dev) | Rich-text editor (ProseMirror) | Vanilla, React, Vue | **Core MIT; Pro extensions/collaboration cloud paid** | Headless, extensible | K |
| [Lexical](https://lexical.dev) | Extensible text editor (Meta) | Vanilla + React | MIT | Fast, accessible focus | K |
| [Plate](https://platejs.org) | Rich-text framework on Slate | React | MIT | shadcn-style UI, plugins | K |
| [BlockNote](https://www.blocknotejs.org) | Notion-style block editor (Tiptap) | React | MPL-2.0 (some XL features GPL/commercial — verify) | Block editing out of the box | K |
| [Recharts](https://recharts.org) | Charts | React | MIT | Simple declarative charts | K |
| [Apache ECharts](https://echarts.apache.org) | Advanced/large visualizations | Vanilla (+ wrappers) | Apache-2.0 | Canvas/SVG, huge chart range, good for big data | K |
| [Visx](https://airbnb.io/visx) | Custom visualization primitives | React | MIT | D3 math + React rendering; for bespoke charts | K |
| [D3](https://d3js.org) | Data-viz toolkit | Vanilla | ISC | Total control | K |
| [Observable Plot](https://observablehq.com/plot) | Concise exploratory charts | Vanilla | ISC | Great defaults | K |
| [Nivo](https://nivo.rocks) | Charts | React | MIT | Rich defaults, SVG/canvas | K |
| [Chart.js](https://www.chartjs.org) | Charts | Vanilla (+ wrappers) | MIT | Canvas; simple | K |
| [React Flow (xyflow)](https://reactflow.dev) / Svelte Flow | Node editors, workflow diagrams | React, Svelte | MIT (React Flow Pro subscription for extras) | Accessible-ish; add keyboard ops | K |
| [dnd-kit](https://dndkit.com) | Drag and drop | React | MIT | Keyboard + screen-reader support built in | K |
| [Pragmatic drag and drop](https://atlassian.design/components/pragmatic-drag-and-drop) | Drag and drop | Framework-agnostic | Apache-2.0 | Atlassian; small, native DnD based | K |
| [Uppy](https://uppy.io) | File uploads | Vanilla + adapters | MIT | Resumable (tus), remote sources | K |
| [react-dropzone](https://react-dropzone.js.org) | Drop zone | React | MIT | Minimal | K |
| [MapLibre GL JS](https://maplibre.org) | Vector maps | Vanilla | BSD-3 | Open fork of Mapbox GL v1; bring a tile provider | K |
| [Leaflet](https://leafletjs.com) | Maps | Vanilla | BSD-2 | Simple raster/vector | K |
| [React Hook Form](https://react-hook-form.com) + [Zod](https://zod.dev) | Forms + validation | React / TS | MIT | Pair with your inputs | K |
| [TanStack Virtual](https://tanstack.com/virtual) | Virtualised lists | Multi | MIT | Large lists/tables | K |
| [Lucide](https://lucide.dev) / [Phosphor](https://phosphoricons.com) / [Tabler](https://tabler.io/icons) / [Heroicons](https://heroicons.com) / [Material Symbols](https://fonts.google.com/icons) | Icons | Multi | ISC / MIT / MIT / MIT / Apache-2.0 | One family per product | K |

Animation libraries (Motion, GSAP, AutoAnimate, Lottie, Rive, R3F, Three.js…) live in `../motion/motion-tech-catalog.md`.

## 3. Templates, themes and commercial products
- **Paid:** Tailwind Plus, MUI templates/MUI X Pro-Premium, PrimeStore themes, AG Grid Enterprise, FullCalendar Premium, Tiptap Pro/Cloud, Magic UI Pro, Aceternity Pro, Flowbite Pro, Web Awesome Pro, Framer/Webflow templates.
- **Rule:** never paste code from a paid product unless the user confirms they hold the licence. Offer an open alternative from the tables above.
- Free templates still have licences (MIT, CC, custom). Read them; keep attribution where required.

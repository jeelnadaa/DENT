# Modern Web Guidance (MWG): the authority for how web code is built

[Modern Web Guidance](https://developer.chrome.com/docs/modern-web-guidance) is Google Chrome's skill of expert web-platform guides, stewarded with the Edge, Firefox and MDN teams (Apache-2.0). It steers agents away from legacy patterns towards native platform features, with browser-support data and fallbacks. DENT ships it verbatim as a sibling skill (`../modern-web-guidance/SKILL.md`, or `vendor/modern-web-guidance/` in zip and rules-file installs) and treats it as the **primary authority for all web development and front-end engineering**.

**Notation:** `mwg:<id>` in any DENT file means the MWG guide `<id>`. Get it with `npx -y modern-web-guidance@latest retrieve "<id>"` (or offline: `python scripts/mwg.py retrieve <id>`).

---

## 1. Authority and precedence [Rule]

**Scope.** Every task that writes, changes or reviews **HTML, CSS or client-side JavaScript**, in any framework (React, Vue, Svelte, Astro, plain HTML…): components, layout, forms, motion code, accessibility implementation, performance, security, theming, browser APIs. Not in scope: backend, build tooling, CI, native platforms (SwiftUI, Compose, Flutter), rendered media files (video/audio exports), copy-only work.

**Division of labour.** DENT decides **what** is designed: concept, style, token values, composition, states, copy, motion choreography (what moves, when, why, how strongly), sound, video, DESIGN.md. MWG decides **how it is built on the web**: which element or API, CSS/JS patterns, accessibility implementation, fallbacks, browser support, performance and security patterns.

**Precedence for web implementation** (higher wins):
1. The user's explicit instructions and the project's documented browser-support policy (MWG itself defers to these).
2. **MWG guides**: every MANDATORY, DO/DON'T and fallback rule in the guides you retrieved.
3. DENT references (specs, patterns, recipes, catalogues).
4. Library documentation, then agent judgment.

**DENT thresholds still apply.** DENT's non-negotiables and [Rule] *outcomes* (contrast ratios, 44 px default touch targets, visible focus, honesty, licences, no autoplay) are requirements the MWG implementation must meet. They are thresholds, not techniques, so they don't conflict: where DENT is stricter (44 px targets vs MWG's 24 px minimum) the stricter value satisfies both.

**On conflict.** If a DENT passage prescribes a web technique that a retrieved MWG guide contradicts, follow MWG, log it in the Decision Log with Source `MWG <id>`, and (when you are working on the DENT repo itself) report the passage as a bug. The Override clause (SKILL.md §1.10) never covers MWG MANDATORY rules: a better idea must still meet them, and only the user or the project's browser-support policy can relax a fallback.

---

## 2. Workflow for every web build, fix or review

If the `modern-web-guidance` skill is loaded, follow its own `SKILL.md` (it is the source of truth); this section is the DENT summary.

1. **Search** once per distinct capability in scope, *before* writing code or adding a dependency. 2–5 word action-oriented queries, no framework or product names, compound needs split (`"light dismiss dialog"`, `"responsive data table"`, not `"React settings modal dark mode"`). Translate DENT vocabulary with §4 (a "confirm step" is `"confirmation modal dialog"`).
2. **Retrieve** the matching guides plus the discipline guide that applies (`mwg:html`, `mwg:css`, `mwg:forms`, `mwg:accessibility`, `mwg:color`, `mwg:performance`, `mwg:security`, `mwg:motion`). Output over ~9.5 KB is saved to a temp file: read that file in full with your file-reading tool.
3. **Apply** the patterns, adapted to the framework without dropping the modern feature (MWG `SKILL.md` "Guidelines": typed attributes, SSR guards, refs for `showModal()`, `useId()` for ids and anchor names).
4. **Verify** (gate G13): cross-check the code against each retrieved guide (MANDATORY items, DON'Ts, fallbacks for the support policy) and run `scripts/verify_page.py`, which flags the mechanical MWG violations (global reduced-motion reset, lazy or deprioritised LCP image, ARIA re-added to native `<dialog>`).
5. **Disclose**: end the response that delivers the code with a `### Modern Web Guidance` section in MWG's format (one bullet per guide that shaped the code, with a short verbatim quote of the rule; or one sentence saying which topics you checked and why none applied). Record the guide ids in the Decision Log (`MWG <id>`) and in DESIGN.md's Web platform section. Never cite a guide or quote from memory.

**Running the CLI.**
- Use the exact command in MWG's `SKILL.md` (it pins `--skill-version`); `retrieve` and `list` work the same way.
- Prefer `pnpx` when pnpm is available; on Windows use `npx.cmd`. Under Git Bash on Windows `search` can fail with `'C:\Program' is not recognized`: run it from PowerShell or cmd instead.
- Sandboxed agents: ask for network approval before the first call and allowlist only `npx -y modern-web-guidance@latest *`, never bare `npx *`.
- **Offline fallback:** `python scripts/mwg.py search "<query>"`, `retrieve <id,id>`, `list`, `info`. It reads the vendored snapshot (version in `info`), so say in the report that the snapshot was used.
- If neither works, G13 is **Blocked**: say so plainly and build from DENT's references; never claim MWG was followed.

**Depth.** Quick: only the capability you touch. Standard: each component and behaviour in scope. Advanced/Critical: every capability in the PLAN.md technical strategy, and the plan names the guides per requirement.

---

## 3. Browser support policy

- MWG default: features that are **Baseline Widely available** are used without fallbacks; anything newer **must** use the guide's fallback (feature detection, conditional polyfills, progressive enhancement), unless the project has its own policy.
- Record the policy in DESIGN.md (Web platform) and PLAN.md. If the project targets a restricted runtime (Electron, Tauri), excludes browsers, or rejects polyfills, propose a one-line policy for `AGENTS.md`/`CLAUDE.md` as MWG suggests, e.g. `**Browser Support:** Allow Newly Available features if feature-detected, with no external polyfills.`
- Wherever a DENT file says "check support" or "where supported", the guide's Baseline status and fallback section decide.

---

## 4. DENT → MWG map

A shortcut for choosing queries and ids; it never replaces `search` (upstream adds guides often).

| DENT need | MWG guides |
|---|---|
| Any page: semantics, landmarks, overlays, resource loading | `mwg:html`, `mwg:accessibility`, `mwg:performance` |
| CSS architecture, tokens, resets, cascade | `mwg:css`, `mwg:css-layout`, `mwg:design-token-reactivity`, `mwg:reduce-style-repetition` |
| Responsive layout, container-aware components, fluid type and spacing | `mwg:responsive-design`, `mwg:size-aware-styling`, `mwg:fluid-scaling`, `mwg:respect-os-text-scale` |
| Typography and font loading | `mwg:typography`, `mwg:improve-text-layout-and-legibility`, `mwg:visually-stable-font-fallbacks`, `mwg:visually-stable-mixed-fonts` |
| Color, contrast, forced colors | `mwg:color`, `mwg:contrast-color` |
| Dark mode and theme toggle | `mwg:dark-mode`, `mwg:dark-mode-toggle`, `mwg:component-specific-light-dark-theme`, `mwg:browser-ui-theming` |
| Modal, confirm dialog | `mwg:dialog`, `mwg:light-dismiss-a-dialog`, `mwg:platform-controls-dismiss-dialog`, `mwg:prevent-page-scroll-under-modal-dialog`, `mwg:declarative-dialog-popover-control` |
| Mobile menu, drawer, bottom sheet, sidebar, nav bar | `mwg:navigation-drawer`, `mwg:navbar`, `mwg:stack-drill-down` |
| Menus, popovers, dropdowns, hover cards | `mwg:menu`, `mwg:app-menus`, `mwg:viewport-aware-dropdowns`, `mwg:hovercard`, `mwg:persistent-top-layer-ui` |
| Tooltips and toggletips | `mwg:interest-triggered-tooltips`, `mwg:position-aware-tooltips` |
| Accordion, FAQ, disclosure | `mwg:accordion`, `mwg:search-hidden-content`, `mwg:interactive-content-reveal` |
| Tabs, segmented controls | `mwg:tabs`, `mwg:anchor-positioning-tab-underline` |
| Switch, checkbox, slider | `mwg:switch`, `mwg:checkbox`, `mwg:slider` |
| Select, combobox, custom dropdown | `mwg:branded-select-styling`, `mwg:custom-select-picker-layouts`, `mwg:select-menu-interaction`, `mwg:animated-select-picker`, `mwg:rich-media-picker` |
| Forms and validation | `mwg:forms`, `mwg:validate-input-after-interaction`, `mwg:required-field-feedback`, `mwg:accessible-error-announcement`, `mwg:form-fields-automatically-fit-contents`, `mwg:ime-safe-enter-submit`, `mwg:brand-consistent-forms` |
| Sign-in, sign-up, checkout, address, OTP | `mwg:autofill-sign-in-form`, `mwg:autofill-sign-up-form`, `mwg:autofill-payment-form`, `mwg:autofill-address-form`, `mwg:sms-otp-form`, `mwg:passkeys`, `mwg:quick-sign-ins` |
| Toasts, progress, spinners | `mwg:persistent-toast-notifications`, `mwg:progress`, `mwg:progress-ring`, `mwg:spinner` |
| Cards, breadcrumbs, toolbars, copy button, carousel, tables | `mwg:card`, `mwg:breadcrumbs`, `mwg:toolbar`, `mwg:copy-button`, `mwg:carousel`, `mwg:responsive-table`, `mwg:sortable-table` |
| Sticky or condensing header, scroll progress, scrollspy | `mwg:shrinking-header-on-scroll`, `mwg:state-aware-sticky-headers`, `mwg:scroll-progress-indicator`, `mwg:scrollspy` |
| Any motion, reduced motion, easing | `mwg:motion`, `mwg:physics-based-easing`, `mwg:individual-transform-properties` |
| Entry/exit, top-layer, animating to `auto` height | `mwg:animate-element-entry-exit`, `mwg:animate-to-from-top-layer`, `mwg:animate-to-intrinsic-sizes`, `mwg:dynamic-sibling-animations` |
| Scroll reveals, parallax, scroll stories | `mwg:scroll-entry-exit-effects`, `mwg:parallax-scroll-effects`, `mwg:scrollytelling`, `mwg:scroll-completion-effects` |
| Page and view transitions, reordering lists | `mwg:same-document-transitions`, `mwg:cross-document-transitions`, `mwg:consistent-cross-document-transitions`, `mwg:directional-navigation-transitions`, `mwg:group-element-transitions`, `mwg:faster-spa-view-transitions` |
| Gestures and drag | `mwg:drag`, `mwg:drag-and-drop`, `mwg:swipe-to-remove`, `mwg:swipe-to-reveal`, `mwg:pull-to-reveal`, `mwg:2d-panning` |
| Depth, shapes, textures, text effects | `mwg:visual-effects`, `mwg:complex-shapes`, `mwg:shaped-cutouts`, `mwg:soft-edge-content-fade`, `mwg:visually-texture-content`, `mwg:custom-text-decorations` |
| WebGL, canvas, 3D in a page | `mwg:apply-webgl-shaders`, `mwg:interactive-content-in-3d-scenes`, `mwg:expose-canvas-content-to-browser-features` |
| Icons | `mwg:icons` |
| Performance and Core Web Vitals | `mwg:optimize-image-priority`, `mwg:optimize-preload-priority`, `mwg:optimize-script-priority`, `mwg:deliver-optimized-decorative-images`, `mwg:lazy-load-video-and-audio`, `mwg:defer-rendering-heavy-content`, `mwg:break-up-long-tasks`, `mwg:identify-inp-causes` |
| Security and privacy | `mwg:security`, `mwg:sanitize-untrusted-html`, `mwg:trusted-types`, `mwg:secure-external-subresources`, `mwg:privacy` |
| UX hygiene (popups, compact chrome, device fit) | `mwg:content-first-noise-reduction`, `mwg:form-factor-adaptation`, `mwg:natural-interactions` |
| Web components, PWA install, dates and calendars, on-device AI | `mwg:web-components`, `mwg:install-web-app`, `mwg:support-global-calendar-systems`, `mwg:prompt-api` |

---

## 5. Native first, libraries second [Rule]

Choose the implementation for each widget in this order:

1. **What the project already uses.** In an existing codebase, keep using its component library for widgets it already provides (DENT non-negotiable 8 and scope protection), and apply MWG to everything around them. Offer a native migration as a separate follow-up; don't rewrite it unasked.
2. **The native platform, per MWG**: `<dialog>`, `popover` (incl. `hint`), invoker and interest commands, `<details name>`, `<input type="checkbox" switch>`, customizable `<select>`, CSS anchor positioning, scroll snap, scroll-driven animations, view transitions, `@starting-style`, `interpolate-size`, with each guide's fallbacks.
3. **A library** only where the platform has no primitive (calendar date-range picker, virtualised data grid, rich-text editor, async-search combobox, charts, 3D) or where the support policy rules out both the native feature and its fallback. Record the reason in the Decision Log.

Consequences: no Floating UI/Popper for tooltips, menus and dropdowns that anchor positioning covers; no hand-written focus traps or scroll locks around a native modal; animation libraries (GSAP, Motion) only for choreography the platform can't express (timelines, scrubbing, pinning, morphing), and still with `mwg:motion`'s reduced-motion rules.

---

## 6. Conflicts resolved in DENT 2.3.0

DENT's earlier web guidance was audited against MWG. These passages were replaced; if you meet the old pattern anywhere (including a user's project generated by older DENT), MWG wins.

| Topic | Old DENT guidance | Now (MWG) |
|---|---|---|
| Reduced motion | Global `*{animation-duration:.01ms!important}` reset | Per rule: opt in under `no-preference`, or adjust parameters under `reduce`; never a global reset (`mwg:motion`) |
| Base CSS | Resets on `*` | Element-scoped resets in a low cascade layer (`mwg:css`) |
| Modal dialog | `role="dialog"` + `aria-modal`, hand-made focus trap, body scroll lock | Native `<dialog>` + `showModal()`; no role, `aria-modal`, trap or `overflow: hidden` lock; `overscroll-behavior: contain` (`mwg:dialog`, `mwg:prevent-page-scroll-under-modal-dialog`) |
| Mobile menu | "Focus trap, Esc, scroll lock" | `mwg:navigation-drawer` |
| Switch | `<button role="switch" aria-checked>` | `<input type="checkbox" switch>` with a label (`mwg:switch`) |
| Tooltip | `role="tooltip"` + script | `popover="hint"` + `interestfor` + anchor positioning (`mwg:interest-triggered-tooltips`) |
| Accordion | Button + `aria-expanded` + `grid-template-rows` trick | `<details>`/`<summary>` + `::details-content` + `interpolate-size`; no arrow-key handling (`mwg:accordion`) |
| Tabs | `aria-controls` on tabs | No `aria-controls`; indicator is a shape drawn with a border, not color alone or `box-shadow` (`mwg:tabs`) |
| Widgets | Library first (Radix, Headless UI, Floating UI) | Native first, §5 |
| Fluid type | `clamp()` maximum up to 5.6× the minimum | Maximum ≤ 2.5× the minimum, rem-based (`mwg:responsive-design`, WCAG 1.4.4) |
| Font fallbacks | `size-adjust` only | `font-size-adjust` on the text plus metric overrides (`mwg:visually-stable-font-fallbacks`) |
| Images | "Lazy-load below the fold" | Also: never lazy-load the LCP image; `fetchpriority="high"` on it (1–2 images max) (`mwg:optimize-image-priority`) |
| Dark mode | `prefers-color-scheme` + toggle | `<meta name="color-scheme">`, `color-scheme` on `:root`, `light-dark()`; a toggle stores only an override that differs from the system (`mwg:dark-mode`, `mwg:dark-mode-toggle`) |
| View transitions | "Cross-document in Chromium, check" | Same-document Baseline; cross-document limited (no Firefox) and a progressive enhancement (`mwg:cross-document-transitions`) |
| CSS units | Type in px; fixed control heights | Type in `rem`; `min-block-size` instead of fixed heights on anything with text (`mwg:typography`); `dvh` for mobile full-height (`mwg:responsive-design`) |
| `verify_page.py` | Failed any infinite loop under reduced motion | Slowed loops on progress indicators pass (MWG's "adjust parameters" strategy); new G13 checks |

**Kept unchanged** (complementary, no conflict): the design process, laws, styles, creative direction, copy, motion choreography and the motion menu, sound and video pipelines, licence and honesty rules, DENT's stricter thresholds, and library catalogues for jobs the platform doesn't cover.

---

## 7. Modernising an existing codebase

Only when the user asks for broad modernisation or a legacy-pattern scan (not when adding, fixing or auditing a specific feature): run MWG's alternative flow, `npx -y modern-web-guidance@latest legacy-scan <path> --json`, check each finding against its `keepWhen`/`dropWhen` rubric, report the verified findings (noting that the scan covers only about 20% of the guides), and modernise by retrieving each finding's guide. For a whole-codebase `/dent:audit`, offer the scan as a follow-up instead of running it unasked.

---

## 8. Keeping MWG current (DENT maintainers)

The CLI always serves the newest guides; the vendored copy is the offline fallback and the version DENT is tested against. Refresh it with `python scripts/sync_mwg.py` (never edit `skills/modern-web-guidance/` by hand), run `python scripts/validate.py` (it checks every `mwg:<id>` in DENT against the guides), and add a CHANGELOG entry.

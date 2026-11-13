# Accessibility — In Depth

SKILL.md › Accessibility has the minimum bar. This file goes deeper: who we design for, component-level patterns, and a full WCAG 2.2 AA checklist. Accessibility is never optional in any style or effort level.

---

## 1. Who benefits
- **Permanent:** blind/low vision, color vision deficiency, deaf/hard of hearing, motor impairments, cognitive/learning disabilities, epilepsy/vestibular disorders.
- **Temporary:** broken arm, eye surgery, ear infection.
- **Situational:** bright sunlight, holding a baby (one hand), noisy train, slow network, old phone.
Microsoft's inclusive design toolkit calls this the persona spectrum: solving for one group extends to many more.

## 2. POUR principles (WCAG)
- **Perceivable** — information can be seen/heard in some form (alt text, captions, contrast).
- **Operable** — everything works with keyboard, touch, voice; enough time; no seizures.
- **Understandable** — clear language, predictable behavior, help with errors.
- **Robust** — works with assistive technologies (semantic code, ARIA done right).

## 3. WCAG 2.2 Level AA checklist (designer + developer)

**Perceivable**
- [ ] 1.1.1 Text alternatives for meaningful images; decorative images `alt=""`.
- [ ] 1.2.x Captions for video with audio; transcripts for audio; audio description for important visual-only info in video.
- [ ] 1.3.1 Structure conveyed in code (headings, lists, tables, labels, landmarks).
- [ ] 1.3.2 Meaningful reading order in DOM.
- [ ] 1.3.3 Instructions don't rely only on shape/position/sound ("click the round button on the right").
- [ ] 1.3.4 Works in portrait and landscape.
- [ ] 1.3.5 Inputs have autocomplete purpose (`autocomplete="email"`).
- [ ] 1.4.1 Color not the only means of conveying info.
- [ ] 1.4.2 Auto-playing audio can be paused/stopped.
- [ ] 1.4.3 Text contrast 4.5:1 (large 3:1).
- [ ] 1.4.4 Text resizes to 200% without loss.
- [ ] 1.4.5 Real text instead of images of text.
- [ ] 1.4.10 Reflow at 320 CSS px without 2D scrolling.
- [ ] 1.4.11 Non-text contrast 3:1 (UI components, focus indicators, meaningful graphics).
- [ ] 1.4.12 Text spacing can be increased (line-height 1.5, paragraph 2×, letter 0.12em, word 0.16em) without breaking.
- [ ] 1.4.13 Hover/focus content (tooltips) dismissible (Esc), hoverable, persistent.

**Operable**
- [ ] 2.1.1 All functionality via keyboard. 2.1.2 No keyboard trap. 2.1.4 Single-key shortcuts can be turned off/remapped.
- [ ] 2.2.1 Time limits adjustable/extendable. 2.2.2 Moving/auto-updating content can be paused (> 5s).
- [ ] 2.3.1 No more than 3 flashes per second.
- [ ] 2.4.1 Skip link / bypass blocks. 2.4.2 Page titles. 2.4.3 Logical focus order. 2.4.4 Link purpose clear. 2.4.5 Multiple ways to find pages (nav + search/sitemap). 2.4.6 Descriptive headings and labels. 2.4.7 Visible focus.
- [ ] **2.4.11 Focus not obscured** (sticky headers/footers/cookie banners must not hide the focused element). *(new in 2.2)*
- [ ] 2.5.1 Multi-point/path gestures have single-pointer alternatives (pinch → buttons).
- [ ] 2.5.2 Pointer cancellation (actions on up-event, can be aborted).
- [ ] 2.5.3 Label in name (visible label text is part of accessible name).
- [ ] 2.5.4 Motion actuation (shake/tilt) has alternatives.
- [ ] **2.5.7 Dragging movements** have a single-pointer alternative (e.g. move up/down buttons). *(new)*
- [ ] **2.5.8 Target size minimum 24×24 CSS px** (or adequate spacing). *(new)*

**Understandable**
- [ ] 3.1.1 Page language set (`lang`). 3.1.2 Language of parts.
- [ ] 3.2.1/3.2.2 No unexpected context change on focus or input.
- [ ] 3.2.3 Consistent navigation. 3.2.4 Consistent identification.
- [ ] **3.2.6 Consistent help** location (help/contact in the same place on each page). *(new)*
- [ ] 3.3.1 Errors identified in text. 3.3.2 Labels/instructions. 3.3.3 Error suggestions. 3.3.4 Error prevention for legal/financial/data (review, confirm, undo).
- [ ] **3.3.7 Redundant entry** — don't make users re-enter info already given in the same process (auto-fill or allow selecting). *(new)*
- [ ] **3.3.8 Accessible authentication** — no cognitive tests (remembering passwords/puzzles) without alternatives: allow paste, password managers, passkeys, magic links. *(new)*

**Robust**
- [ ] 4.1.2 Name, role, value for all UI components. 4.1.3 Status messages announced (live regions) without moving focus.

## 4. Component accessibility patterns (WAI-ARIA Authoring Practices)

| Component | Role / markup | Keyboard | Notes |
|---|---|---|---|
| Button | `<button>` | Enter, Space | Icon-only needs `aria-label`. Toggle: `aria-pressed`. |
| Link | `<a href>` | Enter | Don't use for actions. |
| Dialog (modal) | `<dialog>` or `role="dialog"` + `aria-modal="true"` + `aria-labelledby` | Tab cycles inside, Esc closes | Focus first meaningful element; return focus to trigger. Background inert. |
| Menu (actions) | button `aria-haspopup="menu"` `aria-expanded` + `role="menu"`/`menuitem` | ↑↓, Home/End, Esc, type-ahead | For site navigation use a plain list of links, not `role="menu"`. |
| Disclosure / accordion | button `aria-expanded` + `aria-controls` | Enter/Space | Headings wrap the buttons. |
| Tabs | `role="tablist"`, `tab` (`aria-selected`, `aria-controls`), `tabpanel` | ←→ between tabs, Home/End; Tab into panel | Roving tabindex. |
| Combobox / autocomplete | input `role="combobox"` `aria-expanded` `aria-controls` `aria-activedescendant` + `listbox`/`option` | ↓ opens, ↑↓ move, Enter select, Esc close | Announce result count. |
| Listbox / select | Prefer native `<select>`; custom: `role="listbox"` | ↑↓, type-ahead | |
| Checkbox / radio | Native inputs | Space; radios ←→/↑↓ in group | Group with `fieldset` + `legend`. |
| Switch | `<button role="switch" aria-checked>` | Space/Enter | Label describes the setting. |
| Slider | `<input type="range">` or `role="slider"` + `aria-valuemin/max/now/valuetext` | ←→ ↑↓ PgUp/PgDn Home/End | |
| Tooltip | `role="tooltip"`, trigger `aria-describedby` | Shows on focus; Esc hides | Supplementary info only. |
| Toast / status | `role="status"` (polite) or `role="alert"` (urgent) | — | Don't steal focus; errors persist. |
| Tables | `<table>`, `<th scope>`, `<caption>` | — | Sortable: `aria-sort` on header button. |
| Carousel | region with label; slides `aria-roledescription="slide"` | Prev/next buttons, pause | Auto-rotation pausable; don't auto-advance on focus. |
| Breadcrumb | `nav aria-label="Breadcrumb"` + list; current `aria-current="page"` | — | |
| Pagination | `nav aria-label="Pagination"`, current `aria-current="page"` | — | |
| Form errors | `aria-invalid="true"`, `aria-describedby` → message | Focus first error on submit | Error summary with links on long forms. |
| Loading | `aria-busy="true"` on region; status text "Loading results" | — | |

**First rule of ARIA:** use native HTML elements when they exist; ARIA changes what's announced, not behavior — you must add keyboard behavior yourself.

## 5. Screen reader design notes
- Every page: unique `<title>`, one `h1`, logical heading outline (users navigate by headings).
- Landmarks: `header`, `nav` (labeled if multiple), `main`, `aside`, `footer`.
- Link/button text makes sense out of context ("Download invoice March", not "Click here").
- Hide decorative things (`aria-hidden="true"`); give meaningful icons names.
- Visually hidden helper text with a `.sr-only` class where visual context is implied.
- Announce dynamic changes (cart updated, filters applied: "24 results").

## 6. Cognitive accessibility
- Plain language (aim for roughly grade 7–9 reading level for general audiences); short sentences; define jargon.
- Consistent layouts and navigation; predictable behavior.
- One main task per screen; chunk long processes into steps with progress.
- Don't rely on memory (show info needed at the point of use — recognition over recall).
- Generous time limits; save progress; undo.
- Clear error recovery; avoid timeouts; avoid CAPTCHAs that are puzzles.
- Minimize distractions (autoplay, moving content) — offer a calm/reduced mode.
- Support for dyslexia: left-aligned text, adequate spacing, avoid justified text and long italic/all-caps passages.

## 7. Motor accessibility
- Large targets (44–48px touch), adequate spacing between targets.
- No precision-only interactions (tiny drag handles, hover-only menus).
- Alternatives to gestures, drag, and long-press.
- Keyboard and switch-device friendly focus order; no time pressure.

## 8. Vision
- Support zoom to 200–400%; reflow.
- High contrast mode (`prefers-contrast: more`, Windows forced colors `@media (forced-colors: active)` — use system colors and keep borders visible).
- Don't disable pinch-zoom (`user-scalable=no` is a fail).
- Icons with labels; text not embedded in images.

## 9. Hearing
- Captions (accurate, synchronized), transcripts, visual alternatives to sound alerts.

## 10. Seizures & vestibular
- No flashing > 3/sec; avoid large-area flashes and high-contrast striped animations.
- Reduced motion: remove parallax, zooms, large movements, auto-playing motion.

## 11. Testing
- Automated: axe, Lighthouse, WAVE (catches ~30–40% of issues).
- Manual: keyboard-only pass; screen readers (VoiceOver macOS/iOS, NVDA/JAWS Windows, TalkBack Android); zoom 200%; contrast checks; color-blind simulation; reduced motion; forced colors.
- Ideally: test with disabled users.

## 12. Legal context (not legal advice)
WCAG 2.1/2.2 AA is the reference standard for laws such as the ADA (US, through case law and DOJ rules for public entities), Section 508 (US federal), the European Accessibility Act (applies from June 2025), EN 301 549 (EU), and India's Rights of Persons with Disabilities Act 2016 with GIGW guidelines for government sites. Check current local requirements for the product's market.

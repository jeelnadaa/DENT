# DESIGN.md — Trace (project board)

> Approved on 2026-11-14. This file is the source of truth for all design work on Trace.
> Built with DENT (https://github.com/jeelnadaa/DENT). Accessibility rules ([Rule]) from the skill always apply.
> Implementation: `index.html` (single file, no build step). Values below match that file exactly.

## 1. Overview
- **Product:** A sprint board for a product team: kanban with drag and drop, command palette, task drawer and burndown chart.
- **Users:** Team members who check and move tasks several times a day, mostly at a desk; sometimes on a phone in stand-ups.
- **Platform(s):** Web (phone 320 px and up, tablet, desktop).
- **Effort level:** Standard (user).
- **Design concept:** A drafting table: the project is a drawing set, the board is the sheet, tasks are numbered parts, and the burndown is a surveyed line plotted against the ideal.
- **Mood / anti-mood:** precise, calm, engineered · not glossy, not playful.
- **Signature elements:**
  1. Drawing-sheet title block (sprint day, tasks, scope, done %) next to an oversized condensed project title with a "REV 14" mark.
  2. Blueprint grid paper background with registration-mark corners on the burndown panel.
- **Design principles:** Clarity over decoration · keyboard parity with the mouse · every number is computed from the board, never typed · motion explains change, never decorates.
- **Existing system:** None. All components are hand-built inside `index.html`.
- **Aesthetic style:** Utilitarian (instrument panel / spec sheet) base, no accent style. Why: a daily work tool benefits from dense, labelled, honest UI; one signal colour keeps the primary action obvious. (user chose the "Drafting table" direction; style mapping by DENT)
- **Mode:** Light only (default). Why: paper metaphor; dark mode was out of scope at Standard effort. See §14 for adding it.

## 2. Color
| Token | Value | Role | Source |
|---|---|---|---|
| --paper | #ECE8DF | Page background, blueprint grid base | (default) |
| --surface | #F5F2EA | Columns, drawer header/footer, panel strips | (default) |
| --card | #FFFDF8 | Cards, panels, dialogs, inputs | (default) |
| --hair | #D6D0C3 | Decorative hairlines and dividers | (default) |
| --control | #8A8578 | Input/button borders (≥ 3:1) | (default) |
| --grid / --grid-major | rgba(31,78,140,.07) / .12 | Blueprint grid lines (decorative) | (default) |
| --ink | #1C1B18 | Primary text, title block border, toasts | (default) |
| --ink-2 | #57534A | Secondary text | (default) |
| --ink-3 | #5E594F | Mono labels, IDs, axis labels | (default) |
| --signal | #EE6A1F | Primary action fill, high-priority bar, today dot | (user: orange signal) |
| --on-signal | #1C1B18 | Text on signal | (default) |
| --signal-ink | #A63D00 | Orange as text (HIGH, errors, REV) | (default) |
| --signal-line | #C44A0B | Chart "Remaining" line and projection, danger border | (default) |
| --signal-wash | #FBE3D3 | New-card flash, error banner, today halo | (default) |
| --blue | #1F4E8C | Focus ring, drop target, today marker, registration marks | (default) |
| --blue-wash | rgba(31,78,140,.08) | Drag placeholder fill, ghost-button hover | (default) |
| --ok | #2F6B3A | Completed checklist, done tick | (default) |

Assignee avatar tones (backgrounds with ink text): AO #F3D9C6 · TR #D5E0EE · PK #DCE7D3 · LW #EADCEB · JH #EFE6C2.

Contrast checks (DENT `contrast.py`):
- ink/paper 14.09:1 · ink-2/paper 6.26:1 · ink-3/paper 5.69:1 · ink-3/surface 6.22:1 · ink-2/card 7.54:1
- on-signal/signal 5.51:1 · ink on hover #F27B35 6.28:1
- signal-ink/surface 5.71:1 · signal-ink/card 6.28:1 · signal-ink/signal-wash 5.18:1
- blue/paper 6.80:1 · blue/surface 7.43:1 · ok/card 6.29:1 · ok/surface 5.71:1
- UI 3:1 — control/card 3.62:1 · signal-line/card 4.77:1
- On ink (toasts, selected palette row): #FFB27F 9.78:1 · #D6D0C3 11.21:1 · #FFFDF8 16.94:1 · toast button border #6F695F 3.17:1

Rule: orange is never used decoratively. It means "act" (primary button), "urgent" (high priority) or "remaining work" (chart).

## 3. Typography
- **Display font:** IBM Plex Sans Condensed 600/700. Used for the project title, drawer task title and dialog headings. Why: an engineering-drawing feel, and it fits long titles.
- **Body/UI font:** IBM Plex Sans 400/500/600.
- **Mono font:** IBM Plex Mono 400/500/600. Used for labels, IDs, points, numbers and button labels. Why: the spec-sheet signature, with tabular figures for data.

| Style | Font | Size | Weight | Line height | Tracking | Use |
|---|---|---|---|---|---|---|
| Display | Plex Sans Condensed | clamp(34px, 6.2vw, 72px) | 700 | 0.95 | −0.025em | Project title (h1) |
| Drawer title | Plex Sans Condensed | 26px | 700 | 1.15 | −0.015em | Editable task title |
| Dialog H2 | Plex Sans Condensed | 22px | 700 | 1.2 | 0 | Shortcuts dialog |
| H2 (column/panel) | Plex Sans | 15px | 600 | 1.2 | 0 | Column and panel headings |
| Body | Plex Sans | 15px | 400 | 1.5 | 0 | Description, general |
| Card title | Plex Sans | 14px | 500 | 1.38 | 0 | Task title on card |
| Big number | Plex Mono | 34px (26px ≤ 420px) | 600 | 1 | −0.03em | Burndown stats |
| Button | Plex Mono | 13px uppercase | 500 | 1 | 0.04em | All buttons |
| Label | Plex Mono | 11px uppercase | 500 | 1.2 | 0.08em | Micro-labels, IDs, axis |
| Small | Plex Sans | 12–13px | 400/500 | 1.4 | 0 | Legend, empty states, tabs |

Numbers always use `font-variant-numeric: tabular-nums`. Inputs are 16px on touch devices to prevent iOS zoom.

## 4. Spacing, layout and grid
- Base unit: 4px. Scale: 4, 8, 12, 16, 24, 32, 48 (`--s1`…`--s7`).
- Page gutter: 16px (< 768) · 24px (768–1439) · 32px (≥ 1440).
- Background grid: 24px minor, 120px major.
- Breakpoints and layout:
  - **< 768 (phone):** column tabs above the board; each column is `100vw − 2×gutter − 28px` wide with scroll-snap. Burndown shows its stats with the chart collapsed behind "Show chart". The top bar keeps icon-only search and New task.
  - **768–1023 (tablet):** columns 280px minimum, horizontal snap scroll. Burndown is a full-width strip (200px stats column + chart).
  - **1024–1439 (laptop):** four columns fit (220px minimum). Burndown strip above the board; chart height capped at 200px.
  - **≥ 1440 (desktop):** board plus a sticky 340px burndown rail on the right.
- Top bar: sticky, 56px tall.
- Density: compact (daily expert use). Card padding 10px 12px, gap 8px; column gap 12px.

## 5. Shape and depth
- Radius: controls 3px · cards 4px · panels/columns/dialogs 6px · title block and burndown panel 2px · filter chips 18px (22px on touch).
- Borders: 1px everywhere; 1.5px dashed for the drag placeholder; the title block, burndown panel, drawer edge and palette use a 1px ink border ("drawn" frames).
- Elevation (only for things that really float):
  - lift (grabbed card, drag ghost): `0 14px 28px -8px rgba(28,27,24,.28), 0 2px 6px rgba(28,27,24,.10)`
  - drawer: `-24px 0 48px -12px rgba(28,27,24,.25)`
  - palette and help dialogs: `0 30px 60px -20px rgba(28,27,24,.45)`
  - backdrop: `rgba(28,27,24,.38)`
- Special surfaces: top bar `rgba(236,232,223,.92)` with an 8px backdrop blur. No glass, gradients or textures elsewhere; the one gradient is the chart's area fill (orange, 16% → 0%).
- Registration marks: 9px blue corner brackets on the burndown panel.

## 6. Iconography and imagery
- Icons: a custom inline SVG sprite on a 16px grid with 1.6px stroke and round caps and joins: search, plus, x, grip, check, arrow, chart, user, col, file, key, reset, trash, warn, chev, filter, help.
- Priority glyphs (10px, always paired with a text label): High = filled triangle in signal-ink · Medium = outlined triangle · Low = dash.
- Avatars: 24px circles with mono initials on tinted backgrounds (§2).
- Imagery: none. The chart is the only illustration.

## 7. Components

### Button
| Variant | Background | Text | Border | Hover | Pressed | Disabled |
|---|---|---|---|---|---|---|
| Default | --card | --ink | --control | bg --surface, border --ink-2 | translateY(1px) | opacity .55 |
| Primary | --signal | --on-signal | --ink + inset 0 -2px rgba(28,27,24,.22) | #F27B35 | translateY(1px) | opacity .55 |
| Ghost | transparent | --ink | transparent | --blue-wash | translateY(1px) | — |
| Danger | --card | --signal-ink | --signal-line | --signal-wash | translateY(1px) | — |

Height 40px (44px on coarse pointers); padding 0 16px; mono 13px uppercase; radius 3px. Icon buttons are 40×40 (44×44 on touch). Column "+" buttons are 32×32 (44 on touch).

### Card (task)
- Structure: `li.slot > div.card[role=button][tabindex][aria-roledescription="draggable task"]`.
- Top row: mono ID, a done tick in Done, and a points box (ink border).
- Title: 2+ lines allowed, wraps anywhere.
- Meta row: priority, checklist count (green when complete), avatar, grip.
- A high-priority card has a 3px signal bar on its left edge.
- States:
  - **Hover:** border --control.
  - **Focus:** 2px blue outline, 2px offset.
  - **Grabbed (keyboard):** lifted, rotated −1°, blue border.
  - **Placeholder:** blue dashed outline with --blue-wash fill, contents hidden.
  - **New:** signal-wash flash for 1.4s.
  - **Done column:** title shown in --ink-2.
- Grip: hidden until hover on mouse; always visible on touch at 40×40.

### Column
- --surface background, hairline border, 6px radius; stretches to full board height so the whole column is a drop zone.
- Header: mono number ("01"), name, count badge, points sum, "+" add.
- Drop target state: blue border plus inset ring, background #EEF0F0.
- Empty states: dashed box with a column-specific line. The first-use Backlog shows "Add first task".

### Composer (new task)
- Inline form at the top of a column: textarea, Add task (primary), Cancel.
- Enter submits, Shift+Enter adds a new line, Esc cancels.
- An empty submit shows "Give the task a title first." with `aria-invalid`.

### Inputs and selects
- 40px tall (44 on touch), 1px --control border, 3px radius.
- Focus: blue border plus a 2px blue ring.
- Selects use a custom chevron; native behaviour is kept.

### Checkbox (drawer checklist)
- 20px box with a 1.5px --control border; when checked, --ok fill with an animated tick.
- The whole row is a 44px label. Checked text is struck through in --ink-2.

### Drawer (task details)
- Native `<dialog>` with `showModal`, docked right: `min(480px, 100vw)` wide, full height.
- Contents in order: head (ID · status, close), editable title, a 2×2 spec grid (status, assignee, points, priority), description, checklist with meter, activity timeline, and a footer (Delete task, Done).
- Closes with Esc, the backdrop, ×, or Done. Focus returns to the task's card.

### Command palette
- Native `<dialog>`: 620px wide at 14vh from the top (8px from the top on phones), up to 560px tall.
- Search input is a combobox with `aria-activedescendant`; results are a listbox grouped as: Selected task · Actions · Filter by assignee · Go to · Help · Active tasks / Tasks · Create.
- Fuzzy matching with highlighted characters (orange underline). Nested levels show ink breadcrumb chips; Backspace on empty input goes up a level.
- The selected row is ink with card-coloured text. The footer shows key hints (hidden on touch).

### Toast
- Ink background, bottom centre, `min(440px, 100vw − 24px)` wide.
- Optional action (Undo / Open) in #FFB27F, plus dismiss.
- Disappears after 6s; pauses on hover and focus. At most 3 at a time. Announced through a polite live region.

### Filter chips (assignee)
- 36px pill (44 on touch) with avatar and first name, using `aria-pressed`. When pressed: ink background with card-coloured text.
- "Clear filter" ghost button appears only while a filter is active.

### Column tabs (phone only)
- Segmented control in a --surface track, 44px tall, showing name and count.
- The current tab (`aria-current`) is ink and follows the board's scroll position.

### Burndown panel
- Stats row: Remaining, Completed, Vs ideal (signed).
- SVG chart redrawn at real pixel width so labels stay 11px:
  - Remaining: 2.5px signal-line, with dots.
  - Ideal: 1.5px ink-2 dashed 5/4.
  - Projection: 1.6px signal-line dotted 1/4.
  - Today marker: blue dashed 2/3.
- Legend, a plain-language verdict, and a "Show data as table" disclosure.
- Empty scope shows a dashed empty state instead of the chart.

### Banner (sync error)
- --signal-wash background with a --signal-line border, warning icon, message and "Retry sync" (disabled while retrying).

## 8. Motion
- Durations: fast 120ms (`--dur-1`) · normal 220ms (`--dur-2`) · slow 340ms (`--dur-3`). JS: FLIP 280ms, card enter 260ms, ghost settle 200ms, number tween 520ms, chart draw 1100ms.
- Easings: `--ease-out` cubic-bezier(.2,0,0,1) for UI · `--ease-drawer` cubic-bezier(.32,.72,0,1) for drawer and toast entry · chart draw cubic-bezier(.4,0,.2,1). No bounce anywhere.
- Signature animations:
  - **FLIP reflow:** every card that changes position glides there (drag, keyboard move, filter, undo, add, delete).
  - **Drag ghost:** follows the pointer with −1.5° tilt and 1.02 scale, then settles into the slot on drop.
  - **Burndown:** the line draws in on load; when work reaches Done, the "remaining" number and the line's endpoint tween to the new value together.
  - **Drawer:** slides in from the right; its sections rise 6px with a 40ms stagger.
  - **Palette:** pops in (−8px, 0.98 scale). A nested level slides in 8px from the right.
  - **Board load:** cards rise 8px with a 22ms stagger (capped at 12 cards).
- Robustness: every JS animation goes through `anim()`, which force-finishes after its duration, so content never waits on a stalled animation.
- Hover: colour and border only, with a 120ms ease-out. Hover is never required.
- Scroll: no scroll effects; horizontal scroll-snap on the board below 1024px; auto-scroll near edges while dragging.
- Reduced motion: all CSS durations drop to 1ms; JS skips FLIP, tweens, the ghost settle and the chart draw; the skeleton shimmer stops. Everything still works.

## 8b. Motion graphics, sound, voice and video
Not used. The app has no sound.

## 8c. Licences
| Asset / library | Source | Licence | Attribution | Commercial OK? |
|---|---|---|---|---|
| IBM Plex Sans, Sans Condensed, Mono | Google Fonts | SIL Open Font License 1.1 | Not required | Yes |
| Icons (SVG sprite) | Hand-drawn for this project | Project-owned | — | Yes |
| JavaScript / CSS | Written for this project, no third-party libraries | Project-owned | — | Yes |

## 9. Patterns and screens
- **Navigation:** top bar with brand, a Projects / Checkout rebuild breadcrumb (≥ 600px), palette button (⌘/Ctrl K), shortcuts (?), New task (N).
- **Screen designed:** Sprint board — sheet header (title block), assignee filters, four columns (Backlog, In progress, In review, Done), burndown panel, task drawer, command palette, shortcuts dialog.
- **Key flows:**
  1. **Move a task:**
     - Mouse: drag anywhere on the card.
     - Touch: drag by the grip.
     - Keyboard: Space to pick up, arrows to move, Space to drop, Esc to cancel.
     - Drawer: Status select.
     - Palette: "Move a task to…".
     - Every move shows a toast with Undo.
  2. **Inspect or edit a task:** click or Enter → drawer.
  3. **Find or act:** ⌘/Ctrl K → fuzzy search → Enter.
  4. **Create:** N, "+" or palette "Create task '…'".
  5. **Track progress:** the burndown updates live with a verdict sentence.
- **Empty / loading / error approach:**
  - Empty columns say what belongs there and invite a drag.
  - A first-use Backlog offers "Add first task"; the burndown shows an empty state.
  - Loading: skeleton cards and chart, with "—" in every stat.
  - Error: a non-blocking banner explains that edits are kept locally, with Retry.
  - Demo toggles: `?state=empty`, `?state=loading`, `?state=error`.
- **Persistence:** localStorage key `trace-board-v1` (try/catch; works without it). "Reset demo data" in the palette restores the seed and can be undone.

## 10. Content and voice
- Tone: plain, specific, calm. Say what happened and what to do next; never blame.
- Rules: sentence case for headings and options; mono UPPERCASE only for micro-labels and buttons; task IDs as `CHK-###`; points written "pt"; days as "D1–D10"; the verdict is a full sentence.
- Sample data is fictional (people, project, numbers) and must be replaced with real data before any public use.

## 11. Accessibility
- Target: WCAG 2.2 AA.
- Board is one Tab stop (roving tabindex); arrow keys move between cards; the skip link goes to the board.
- Drag and drop has keyboard and single-pointer alternatives (drawer Status select, palette), meeting WCAG 2.5.7.
- An assertive live region announces pick-up, position, drop and cancel; toasts are polite.
- Dialogs are native `<dialog>` (focus trapped, Esc closes) and focus returns to its origin.
- Priority, status and today are never shown by colour alone (glyph plus text).
- The chart has `role="img"` with a title and description, plus a data table.
- Touch targets are 44px, except the card grip at 40×40 (above the 24px minimum). Known gap — see the changelog.

## 12. Tokens (copy-paste)
```css
:root{
  --paper:#ECE8DF; --surface:#F5F2EA; --card:#FFFDF8;
  --hair:#D6D0C3; --control:#8A8578; --grid:rgba(31,78,140,.07); --grid-major:rgba(31,78,140,.12);
  --ink:#1C1B18; --ink-2:#57534A; --ink-3:#5E594F;
  --signal:#EE6A1F; --on-signal:#1C1B18; --signal-ink:#A63D00; --signal-line:#C44A0B; --signal-wash:#FBE3D3;
  --blue:#1F4E8C; --blue-wash:rgba(31,78,140,.08); --ok:#2F6B3A;
  --font-sans:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif;
  --font-display:"IBM Plex Sans Condensed","IBM Plex Sans",system-ui,sans-serif;
  --font-mono:"IBM Plex Mono",ui-monospace,"SFMono-Regular",Consolas,monospace;
  --s1:4px; --s2:8px; --s3:12px; --s4:16px; --s5:24px; --s6:32px; --s7:48px;
  --r-control:3px; --r-card:4px; --r-panel:6px;
  --lift:0 14px 28px -8px rgba(28,27,24,.28), 0 2px 6px rgba(28,27,24,.10);
  --panel-shadow:-24px 0 48px -12px rgba(28,27,24,.25);
  --dur-1:120ms; --dur-2:220ms; --dur-3:340ms;
  --ease-out:cubic-bezier(.2,0,0,1); --ease-drawer:cubic-bezier(.32,.72,0,1);
  --gutter:16px; --topbar:56px;
}
@media (min-width:768px){ :root{ --gutter:24px; } }
@media (min-width:1440px){ :root{ --gutter:32px; } }
@media (prefers-reduced-motion:reduce){ :root{ --dur-1:1ms; --dur-2:1ms; --dur-3:1ms; } }
```

## 13. Decision log
| # | Decision | Choice | Why | Source |
|---|---|---|---|---|
| 1 | Effort | Standard | Fully working, verified and scored without a written brief | User |
| 2 | Direction | Drafting table | Calm and precise; avoids the white-and-purple SaaS cliché | User |
| 3 | Style | Utilitarian base, no accent | Dense, labelled tool UI with one signal colour | DENT `styles/utilitarian.md` |
| 4 | Category cliché | Diverged on colour (paper/orange), type (Plex Condensed + Mono) and layout (title block, registration marks) | Kanban apps default to white, Inter, purple and soft shadows | DENT `creative/anti-slop.md` + Agent judgment |
| 5 | Fonts | IBM Plex Sans / Sans Condensed / Mono | One engineered family; tabular mono for data; OFL | Agent judgment |
| 6 | Signal colour | #EE6A1F fill, #A63D00 as text | Orange as text fails AA, so fill with ink text plus a darker text variant | DENT `styles/utilitarian.md` watch-outs |
| 7 | Libraries | None; DnD, palette and chart hand-written | Recipe's dnd-kit/cmdk are React-only; a single HTML file needs keyboard DnD built in | Override (DENT `recipes/app-and-dashboard.md` §5) |
| 8 | Touch drag | Drag by grip; card body scrolls | Avoids fighting page and board scroll on phones | Agent judgment (plan audit, Major) |
| 9 | Dialogs | Native `<dialog>` for drawer, palette, help | Built-in focus trap, Esc and inert background | Agent judgment |
| 10 | Burndown | Pixel-width SVG with ideal, actual, projection, verdict and data table | Answers "are we on track?" in words as well as lines | DENT `data-visualization.md` + Agent judgment |
| 11 | Undo over confirm | Toast with Undo for move, delete, reset | Reversible actions shouldn't ask "are you sure?" | DENT `recipes/app-and-dashboard.md` §6 |
| 12 | Phone layout | Column tabs + snap columns; chart collapsed | The board is the primary task on small screens | Agent judgment |
| 13 | Mode | Light only | Paper metaphor; dark mode out of scope at Standard | Agent judgment |

## 14. Changelog
- 2026-11-14 — Initial approved version (self-score 8.4/10). Known follow-ups: dark "night table" theme using the same token names; enlarge the touch grip to 44px.

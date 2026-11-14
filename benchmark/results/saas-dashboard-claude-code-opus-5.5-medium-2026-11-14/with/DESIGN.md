# DESIGN.md: Store Analytics dashboard

Source of truth for `index.html`. Built with DENT 2.0 (`/dent` → create → verify → score). Date: 2026-11-14.

## 1. Brief
- **User:** a small online store owner who checks the store daily, mostly on a laptop, sometimes on a phone.
- **Top questions, in order:** How much did I sell? Is that up or down? What's selling, where do buyers come from? What happened to recent orders?
- **Critical task:** finding a specific recent order (search, filter, sort).
- **Effort:** Standard (chosen by default; this was a non-interactive run).

## 2. Direction
- **Concept:** a shop's *instrument panel*: a ruled, labelled control board where every reading has a name and one orange indicator means "this matters now".
- **Mood:** precise, warm, honest. **Anti-words:** glossy, corporate.
- **Category cliché:** dark/indigo SaaS dashboard, gradient cards, 12 equal tiles, donut charts. **Divergence:** warm grey paper surface (light by default, since it's used in the daytime), visible 1px ruled grid instead of floating shadow cards, mono uppercase micro-labels, numbered sections, ranked bar lists instead of donuts, and one hero tile, not equal tiles.
- **Style:** Utilitarian base (DENT `styles/utilitarian.md`), no accent style.
- **Signature elements:** numbered sections ("01 Overview"), ruled cell grid, the oversized net-sales numeral, the status "LED" with text.

## 3. Tokens
| Token | Light | Dark | Use |
|---|---|---|---|
| --bg | #E8E6E1 | #121211 | page |
| --surface | #F4F3F0 | #1B1B19 | cells |
| --rule / --rule-strong | #C9C6BE / #76736B | #34332F / #86837B | dividers / control borders (≥3:1) |
| --text / --text-2 / --text-3 | #161616 / #55554F / #6A6862 | #EDEBE6 / #B3B0A8 / #9C9991 | text |
| --signal / --signal-fill / --signal-text | #E5480B / #FF5A14 / #B23A06 | #FF6A2B / #FF6A2B / #FF9161 | revenue line, active control, section index |
| --pos / --neg / --warn | #1D6B3A / #B42318 / #8A5A00 | #6CC58E / #FF8A7E / #E8B04B | deltas and status (always with an arrow, sign or shape too) |
| --focus | #1659D6 | #7FA8FF | focus ring |
Type: Inter Tight (UI, numbers, tabular figures) + JetBrains Mono (labels, metadata). Spacing 4/8/12/16/24/32/48. Radius 2px on controls, 0 on containers. Motion: 100ms hover, 180ms fades, 420ms number count-up; all off under reduced motion.

## 4. Layout
- **≥1024px:** hero net-sales tile (chart + previous-period comparison) at 2.2fr, with three KPI tiles stacked to its right; products and traffic side by side; full table.
- **640–1023px:** hero full width, KPIs in 3 columns (sparkline under the value); products/traffic stack below 900px; Source column hidden below 1024px.
- **<640px:** range switch becomes a full-width 3-segment control; the table becomes order cards with a "Sort by" select; touch targets 44px on coarse pointers.

## 5. States
| State | How to reach | What it shows |
|---|---|---|
| Loading | every load/refresh; `?state=slow` | layout-matching skeletons, amber LED "Loading store data…", aria-busy |
| Empty | `?state=empty` | $0 with "No orders in the previous 30 days either", "Show last 90 days" action, empty product/table messages; traffic still shown |
| Error | `?state=error` | alert banner (what happened, that orders aren't affected, Try again) with focus moved to it; tiles show "Unavailable" |
| Partial error | `?state=partial` | figures load; the table shows "Orders didn't load" + Retry orders |
| No results | search/filters | "No orders match “x”" + Clear filters |
| Stale | always | "Updated N min ago · time" + Refresh |
The "Preview state" select in the sample-data strip switches between them.

## 6. Data honesty
All figures come from one seeded generator (`buildDataset`), so KPIs, chart, products, traffic and table always agree (e.g. Orders = table total − cancelled). A strip under the header says it's sample data. The store and customer names are fictional (first name + initial). The chart's y-axis starts at $0.

## 7. Accessibility notes
Skip link; one h1, h2 per section, h3 per tile; chart is focusable with arrow/Home/End keys, a live-region readout and a "Show daily figures as a table" fallback; sortable headers are buttons with `aria-sort`; filter chips use `aria-pressed`; deltas carry an arrow and sr-only "Up/Down" as well as colour; status uses a distinct shape per status plus its text.

## 8. Decision Log
| Decision | Choice | Why | Source |
|---|---|---|---|
| Effort | Standard | No user to ask | DENT `workflow-questions-and-effort.md` §5 (default) |
| Style | Utilitarian base, no accent | Data tool; "big tabular numbers as the main visual" | DENT `styles/utilitarian.md` |
| Mode | Light default + dark toggle (follows system) | Daytime commerce use | DENT §5 defaults + Agent judgment |
| Hierarchy | One hero tile, then supporting KPIs | Answer "how much did I sell" first | DENT `recipes/app-and-dashboard.md` Step 4 |
| Charts | Hand-written SVG, no library | Full control over keyboard access and tooltips; zero dependencies | Agent judgment |
| Traffic viz | Ranked bars with direct labels, not a donut | 6 similar slices read poorly in a pie | DENT `data-visualization.md` §11 |
| Signal colour | Orange darkened to #E5480B (line) / #B23A06 (text) | Starter #FF4F00 is under 3:1 on the light surface | Override of style starter tokens (accessibility watch-out) |
| States preview | Visible "Preview state" select + `?state=` | Gate A2: every state reachable | DENT `recipes/app-and-dashboard.md` Step 3 |

## 9. Licences
| Asset | Source | Licence |
|---|---|---|
| Inter Tight | Google Fonts | SIL OFL 1.1 |
| JetBrains Mono | Google Fonts | SIL OFL 1.1 |
| Icons, favicon, brand mark | Drawn inline for this file | Original |
| JS/CSS libraries | none | — |

## Changelog
- 2026-11-14: v1 built and verified.

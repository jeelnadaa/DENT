# Data Visualization

How to show numbers so people understand them quickly and correctly. Applies to charts in dashboards, reports, landing pages and apps, in any aesthetic style (styles may change colors and fonts, never the rules marked [Rule] or [Law]).

---

## 1. Start with the question
Before choosing a chart, write the one sentence the chart must answer: *"Revenue grew every month except March."* The chart type, sorting, colors and title all follow from that sentence. If you can't write it, you don't need a chart yet — show a table or a number.

**Title the chart with the takeaway**, not just the topic: "Signups doubled after the pricing change" instead of "Signups by week". Add a subtitle with the unit and period.

---

## 2. Choosing the chart type

| Goal | Best choice | Avoid |
|---|---|---|
| Compare values across categories | **Bar chart** (horizontal when labels are long or > ~7 categories), sorted | Pie with many slices, 3D bars |
| Change over time | **Line chart** (continuous), column chart (few discrete periods) | Pie, unordered bars |
| Part-to-whole (single total) | **Stacked bar / 100% bar**, or pie/donut with **≤ 5 slices** | Pie with many similar slices |
| Part-to-whole over time | Stacked area (few series) or 100% stacked columns | Many-series stacked area |
| Ranking | **Sorted horizontal bar**, dot plot | Unsorted bars |
| Distribution | **Histogram**, box plot, violin, strip/dot plot | Averages alone |
| Relationship between 2 variables | **Scatter plot** (add trend line if useful); bubble for a 3rd variable (carefully) | Dual-axis lines |
| Many small comparisons | **Small multiples** (same chart repeated per category, shared axes) | One chart with 12 lines |
| Geography | Choropleth (normalized rates!) or symbol map | Raw counts on choropleth (just shows population) |
| Single key number | **Big number (KPI)** with comparison and sparkline | A gauge chart |
| Flow / process | Sankey, funnel (bars) | Pie |
| Precise lookup | **Table** | Any chart |

---

## 3. Perception: why some charts work better [Law]

**Cleveland & McGill's ranking** of how accurately people judge values (most → least accurate):
1. Position along a common scale (bar ends, dots on one axis)
2. Position along non-aligned scales (small multiples)
3. Length (bars)
4. Angle / slope (pie slices, lines)
5. Area (bubbles, treemaps)
6. Volume (3D)
7. Color saturation / hue

→ Prefer bars, dots and lines for anything that must be compared precisely. Use area and color for rough patterns only.

**Pre-attentive attributes:** color, size, position, orientation, and shape are noticed instantly. Use **one** highlight attribute to point at the key data (e.g. one bar in the accent color, the rest grey).

**Gestalt applies:** items with the same color are read as a group (similarity); lines connect points into one series (connectedness); legend near data reads as linked (proximity).

---

## 4. Core rules

### Honesty [Rule]
- **Bar and area charts start at zero.** Cutting the axis exaggerates differences.
- Line charts may start above zero when the change matters more than the absolute size — make the axis range clear.
- Keep consistent intervals on axes (no skipped years without a visible break).
- Normalize when comparing different-sized groups (per capita, per user, %).
- Avoid **dual y-axes**; they let any two lines look correlated. Use two charts or index both to 100.
- No 3D charts — they distort sizes.
- Show uncertainty (ranges, error bars, "estimated") when data is uncertain.

### Clarity (Tufte's data-ink principle) [Law]
- Maximize the share of ink that shows data; remove **chartjunk**: heavy gridlines, borders, backgrounds, shadows, gradients, 3D, decorative icons.
- Gridlines: light, few (or none for bar charts with direct labels).
- **Direct labels** on lines/bars instead of a separate legend when possible (less eye travel — proximity).
- Sort bars by value unless the categories have a natural order (time, size ranges, steps).
- Label axes with units; format ticks readably (1K, 2.5M, Jan, Feb).
- Limit series: ~5–7 distinguishable colors max in one chart; beyond that, highlight a few and grey the rest, or use small multiples.
- Annotate key events directly on the chart ("Price change", "Outage").

### Numbers and text
- Consistent decimal places within a chart; round to meaningful precision (12.4%, not 12.4381%).
- Use **tabular numerals** in tables and KPIs.
- Right-align numbers in tables; align decimal points.
- Use thousands separators per locale (1,234 / 1.234 / 1,234 as per region); abbreviate large numbers consistently (K, M, B).
- Show units and currency once, clearly (in title, axis or header).
- Dates: consistent, unambiguous format for the audience (avoid 03/04/25 confusion for international users — use "3 Apr 2025").

---

## 5. Color in charts

### Three kinds of palettes
| Type | Use for | How |
|---|---|---|
| **Categorical** | Different, unordered groups | Distinct hues with similar lightness/saturation; ≤ 7–8 colors |
| **Sequential** | Ordered values low → high | One hue (or two close hues) from light to dark |
| **Diverging** | Values around a meaningful midpoint (0, average, target) | Two hues meeting at a neutral middle |

### Rules
- **[Rule]** Don't rely on color alone — add labels, patterns, shapes, or direct annotations.
- **[Law]** About **1 in 12 men** and **1 in 200 women** have some color vision deficiency (most commonly red–green). Avoid red vs green as the only distinction; use blue/orange, or add icons/labels (▲▼).
- Use **meaning-consistent colors** across the whole product: the same category always gets the same color in every chart.
- Use the accent color for "the thing to look at"; grey for context.
- Semantic colors (good/bad) only when meaning is unambiguous; "up" is not always good (costs, errors).
- Graphical objects (bars, lines, points) need **≥ 3:1 contrast** against the background **[Rule: WCAG 1.4.11]**; adjacent segments in stacked charts need separation (thin white/background-colored gap).
- Dark mode: re-tune chart colors (slightly lighter, less saturated) — don't just reuse light-mode colors.
- Rainbow scales for sequential data are misleading (perceptually uneven); use perceptually uniform scales (viridis-like).

---

## 6. KPI cards (big numbers)

Structure: **label → value → comparison → optional sparkline**.
- Label: what it is and the period ("Revenue · This month").
- Value: large, tabular figures, unit/currency.
- Comparison: change vs previous period or target, with **arrow + sign + text color** (▲ 12.4% vs last month). Neutral/grey when change is insignificant.
- Sparkline: small trend without axes, last point highlighted.
- Click → drill down to detail.

---

## 7. Interaction

- **Tooltips:** show exact values on hover/tap (and focus for keyboard); include series name, date and formatted value; don't hide essential info only in tooltips.
- **Crosshair/hover line** on time series to compare series at one date.
- **Legend toggles** to show/hide series (also clickable via keyboard).
- **Zoom/brush** for long time ranges; preset ranges (7D, 30D, 90D, 1Y).
- **Drill-down:** click a bar/segment to filter the rest of the dashboard.
- Animate data changes from old to new values (not from zero) at 300–500ms; respect reduced motion.
- Loading: skeleton in chart shape; empty: explain why no data ("No sales in this period") and how to change filters.

---

## 8. Responsive charts

- On small screens: fewer ticks, shorter labels, horizontal bars instead of columns, legends moved below, or switch to a summary KPI + "View full chart".
- Keep touch targets for data points ≥ 24–44px (use larger invisible hit areas).
- Allow horizontal scroll for wide tables rather than squeezing.

---

## 9. Accessibility [Rule]

- Provide a **text summary** of the key insight (the chart title often does this) and access to the underlying **data table**.
- Charts need accessible names/descriptions (`role="img"` + `aria-label` for static SVG, or accessible chart libraries).
- Keyboard: interactive points/series must be focusable with visible focus and announced values.
- Patterns or direct labels in addition to color.
- Text in charts ≥ 12px; contrast as in `foundations-and-components.md` §3.

---

## 10. Tables (when numbers need precision)

- Left-align text, right-align numbers, center only short status icons.
- Header row distinct (weight/color), sticky on scroll.
- Row height 40–48px default; compact density option for power users.
- Zebra stripes or light dividers — not both heavy.
- Sortable columns with clear sort indicator; filter and search for large tables.
- Highlight the row on hover; select with checkboxes for bulk actions.
- Inline mini-charts (sparklines, bars) can make tables scannable.
- Totals row visually distinct.

---

## 11. Common mistakes

- Pie charts with 8+ slices or slices of nearly equal size.
- Truncated bar axes exaggerating differences.
- Dual axes implying correlation.
- Rainbow colors with no meaning; colors changing between charts.
- Legends far from data; tiny unreadable labels.
- Too many series on one line chart ("spaghetti").
- Gauges and speedometers for a single number (a KPI with target comparison is clearer).
- Decorative 3D, gradients and shadows on data marks.
- Charts without units, period or source.

# Scorecard: Store Analytics dashboard

> DENT self-score (`/dent:score`). Rules: evidence for every line · unverified lines max 6 · failed gate caps its line at 4 · a missing Must requirement caps overall at 6 · requirement lines count double.
> Target: overall ≥ 8 and no line < 6. Date: 2026-11-14 · Round: 1
> Self-scores are biased upward and are not benchmark results.

## Requirements (from the request)
| ID | Requirement | Score /10 | Evidence |
|---|---|---|---|
| R-01 | Revenue | 9 | Net sales hero: big figure, % vs previous period, daily line + dashed previous period, $0 baseline, tooltip, keyboard, data table |
| R-02 | Orders | 9 | Orders KPI + sparkline + delta; AOV and conversion derived from the same data |
| R-03 | Top products | 9 | Top 6 ranked by sales or units (toggle), with units sold and share of product sales |
| R-04 | Traffic sources | 8 | 6 sources: sessions, share, orders, conversion; total + best-converting source. No trend over time |
| R-05 | Recent orders table: search, sort, filters | 9 | Scripted tests pass: search + highlight, status chips, source select, sort by date/customer/status/total both ways, pagination, CSV export |
| R-06 | Loading, empty, error states | 9 | Skeleton loading, slow load, empty store, full error + retry, partial (orders) error + retry, no-results; all reached in tests and screenshotted |
| R-07 | Responsive phone/tablet/desktop | 8 | 0 overflow at 320–1440; designed phone card layout + sort select; tablet KPI re-layout. Not checked on a real device |
| R-08 | Self-contained index.html, opens from disk | 9 | Single file, only Google Fonts; tests ran from file:// |

## Quality lines
| Line | Score /10 | Evidence |
|---|---|---|
| Clarity | 8 | Net sales and trend read first; sections numbered by question |
| Hierarchy & composition | 8 | One hero tile + supporting cells; the products cell leaves some empty space at the bottom on desktop |
| Typography | 8 | Inter Tight tabular figures + mono labels; tight tracking on big numerals |
| Color & surfaces | 8 | One signal colour with a meaning; all token pairs AA in both themes (contrast.py) |
| Consistency | 8 | Shared controls (btn, seg, chip, select) with one height/radius system |
| States & feedback | 9 | Every state above, plus toast on export and a status LED with text |
| Accessibility | 7 | verify_page: 0 unlabeled/unnamed, contrast sample pass; chart keyboard + live region tested. No screen-reader pass, no full manual Tab walk |
| Responsiveness | 8 | 6 widths pass; phone/tablet screenshots reviewed |
| Function | 9 | 31/31 scripted checks pass, 0 console errors |
| Distinctiveness | 7 | Ruled instrument-panel look avoids the dark-gradient SaaS cliché; still close to the Utilitarian template |
| Content honesty & copy | 9 | Sample-data notice, consistent derived numbers, definitions in footer, specific error copy |
| Motion | 7 | Count-up, fades, shimmer; reduced-motion run shows 0 running animations |
| Performance | 6 | Unverified: not measured (single file, no libraries, ~500-order dataset) |

**Overall:** 8.3 / 10 · Lowest line: Performance (6, not measured)

Target met (≥ 8, no line < 6).

## Next improvements, if wanted
| # | Raises line | Change | Expected score |
|---|---|---|---|
| 1 | Accessibility | Screen-reader pass (NVDA) and a full manual Tab walk | 8 |
| 2 | Distinctiveness | A store-specific signature, e.g. a "today vs typical day" pace gauge in the hero | 8 |
| 3 | Performance | Measure load/INP with Lighthouse; preload the fonts | 8 |

## Attribution
- **From DENT:** Utilitarian style and tokens, dashboard recipe (hero tile first, states reachable via a toggle, table pattern), data-viz rules (zero baseline, data-table fallback, no donut for 6 similar slices), default choices for a run with no questions, verification and scoring.
- **From the user (task brief):** the content list (revenue, orders, top products, traffic, orders table with search/sort/filters, loading/empty/error states), single index.html, responsive.
- **Agent judgment:** instrument-panel concept, fictional ceramics store, hand-written SVG charts, partial-error state, CSV export, dark theme.
- **Overrides:** signal orange darkened from the style's #FF4F00 so the chart line and text meet contrast.

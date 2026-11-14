# DESIGN.md — Aangan & Oak checkout

> Approved 2026-11-14 (plan approved by the user before build). Source of truth for this checkout.
> Built with DENT. Accessibility rules always apply. (user) = chosen by the user · (default) = chosen by the agent.

## 0. Brief
- **Problem:** buying large, expensive furniture online raises worries about total cost, whether it fits through the door, when it arrives, and whether a failed payment loses the order or charges twice.
- **Job to be done:** "Help me pay for my furniture and book a delivery I can be home for, without surprises."
- **Goal:** complete the purchase on a phone in five short steps; recover from any error without re-typing.
- **Success signals (if this were live):** checkout completion rate, payment retry success after a decline, share of error-summary appearances per step.
- **Scope:** cart review, address, delivery slot, payment (simulated), confirmation. No accounts, promo codes or real payments.
- **Assumptions:** prices include 18% GST; pay on delivery capped at ₹50,000; deliveries Mon–Sat.

## 1. Overview
- **Product:** checkout for a fictional Indian furniture store, Aangan & Oak (user: fictional; name: default).
- **Users:** shoppers on phones first, also tablet and desktop; mostly one-off buyers.
- **Platform:** responsive web, one self-contained `index.html`.
- **Effort level:** All-out (user).
- **Concept:** "A calm, daylit showroom where the staff walk your pieces home with you."
- **Mood / anti-mood:** warm, unhurried, trustworthy · not pushy, not flashy.
- **Signature elements:** (1) "path home" progress: a line whose last stop is a house, not a number; (2) line-drawn furniture that "arrives" in a sunlit room on confirmation.
- **Principles:** total cost before anything else · never lose what the shopper typed · say what happened and what to do next · one primary action per step.
- **Style:** Japandi / Nordic base, no accent style (user picked direction C "Quiet showroom").
- **Mode:** light + dark, follows the system, toggle remembered (user).

## 2. Color
| Token | Light | Dark | Role |
|---|---|---|---|
| --bg | #F5F1EA | #1E1C1A | Page (rice paper / warm charcoal) |
| --surface | #FBF8F3 | #262320 | Cards, inputs, summary |
| --surface-2 | #ECE5D9 | #2E2A26 | Thumbnails, notes, room scene |
| --text | #2E2B28 | #EDE7DD | Primary text |
| --muted | #5E5850 | #B5AC9F | Secondary text |
| --line | #DED5C7 | #3A3530 | Decorative dividers |
| --line-strong | #8C8478 | #7A7268 | Input and control borders (≥ 3:1) |
| --primary | #4F5640 | #A9B38F | Moss: primary actions, selected states, focus |
| --on-primary | #FFFFFF | #1E1C1A | Text on primary |
| --primary-soft | #E4E6D9 | #2F3328 | Selected backgrounds, focus halo |
| --danger | #9C4A2E | #E59A80 | Rust: errors only |
| --danger-soft | #F7E6DE | #3A2620 | Error box background |
| --warn-soft | #F3EBD6 | #36301F | Neutral notices (e.g. payment cancelled) |
| --wood | #A47A4E | #C49A6C | Illustration wood (decorative) |

Contrast (contrast.py): text/bg 12.5 · muted/bg 6.2 · muted/surface-2 5.6 · primary/bg 6.8 · on-primary/primary 7.7 · danger/bg 5.4 · danger/danger-soft 5.1 · primary/primary-soft 6.1 · line-strong/bg 3.3 (UI) · dark: text 13.8 · muted 7.6 · primary 7.7 · danger 7.5 · danger/danger-soft 6.3 · line-strong 3.6 (UI).

## 3. Typography
- **Display:** Fraunces (variable, opsz 9–144, weights 300–600). Characterful soft serif that feels like a showroom placard. Used for step headlines, section titles, totals.
- **UI/body:** Manrope 400–700. Calm, legible, good numerals.
| Style | Font | Size | Weight | Line height | Tracking |
|---|---|---|---|---|---|
| Step headline (h1) | Fraunces, opsz 144 | clamp(32px, 24px + 2.4vw, 52px) | 350 | 1.05 | −0.025em |
| Section title (h2) | Fraunces, opsz 48 | 22px | 400 | 1.2 | −0.01em |
| Total | Fraunces, opsz 72 | 26px (summary), 22px (bar) | 450 | 1.1 | 0 |
| Body / inputs | Manrope | 16px | 400 | 1.55 | 0 |
| Labels | Manrope | 14px | 600 | 1.4 | 0 |
| Kicker | Manrope | 13px caps | 600 | 1.3 | 0.14em |
Money uses tabular lining numerals and `Intl.NumberFormat('en-IN')` (₹1,03,248 grouping).

## 4. Spacing, radius, layout
- Spacing scale: 4, 8, 12, 16, 20, 24, 32, 40, 56, 72 px (`--s1`…`--s10`).
- Radius: 4 px inputs/buttons, 8 px cards/options, 14 px summary and room scene, pills for chips.
- Targets: 48 px tap size, never below 44 px (checked at 320 px).
- **Phone (< 600):** one column; collapsible "Show order summary" at top; sticky bottom bar with total + primary button.
- **≥ 600:** two-column field rows, 4 time windows in a row, side-by-side confirmation panels.
- **Tablet (768–1023):** 820 px column, 7-column date grid, sticky bar shows total left and buttons right.
- **Desktop (≥ 1024):** form (≤ 680 px) + 380 px sticky summary; buttons inline at the end of the form.

## 5. Components
- **Path home (progress):** 5 nodes on a line; done = moss fill + check (link back), current = ring + halo + bold label + `aria-current="step"`, upcoming = hollow. Last node is a house icon labelled "Home". The fill line animates with `scaleX`.
- **Field:** label above, optional hint, input 48 px, error line below with alert icon + text (never colour alone); `aria-invalid`, `aria-describedby` hint + error.
- **Error summary:** rust 2 px border box, "There are N things to fix", links focus the field; lines drop out as fields are fixed; hides when empty.
- **Choice cards (dates, windows, payment methods):** real radio inputs over styled cards; full = dashed border + "Full"/strike-through + disabled; selected = moss fill (dates) or 2 px moss border (windows, methods).
- **Chips (lift):** radio pills, moss when selected.
- **Quantity stepper:** − / count / + (44 px), minus disabled at 1, plus at 5 with an explanatory note.
- **Buttons:** primary moss (52 px), secondary outlined, small 44 px variant; processing = spinner + "Processing…" + disabled.
- **Payment alert:** rust box with title, "Nothing was charged" body, and 1–3 recovery buttons; neutral variant for a cancelled UPI request.
- **Toast:** dark pill near the bottom, optional action (Undo), 8 s, pauses on hover/focus, cleared on step change.

## 6. States and flows
| Step | States designed |
|---|---|
| Cart | items, qty at min/max, removed + Undo, empty (restore sample pieces) |
| Address | empty submit, per-field errors, PIN found / unknown, floor > ground → lift question, stairs-only note |
| Delivery | no day / no window errors, full day, full windows, assembly on/off |
| Payment | review with Change links, method not chosen, field errors per method, processing, declined, bank error, offline, UPI waiting / declined / cancelled, COD unavailable over ₹50,000 |
| Confirmation | order number, slot, address, paid by, next steps, calendar (.ics), print, new order |
Routing: hash per step; you can't skip ahead; refresh restores the step and data (card number and CVV are never stored); after ordering, every route shows the confirmation until "Start a new order".

## 7. Motion
| What | Duration | Easing | Why |
|---|---|---|---|
| Step enter (fade + 8 px rise) | 280 ms | cubic-bezier(.22,.61,.36,1) | Marks the page change without slowing the flow |
| Progress fill | 520 ms | same | The path visibly grows toward home |
| Room arrival (pieces slide in, staggered 160 ms) | 520 ms | same | The payoff moment: the furniture "arrives" |
| UPI wait breathing ring | 2.4 s loop | same | Shows the system is waiting, not stuck |
| Hover/selection colour | 160 ms | same | Feedback |
Reduced motion: all animations and transitions effectively off (verified: 0 running animations). Override logged: Japandi's 400–700 ms is kept only for the room scene.

## 8. Sound (opt-in, off by default)
Synthesised with Web Audio (no files). Toggle in the header (`aria-pressed`), remembered in localStorage. No AudioContext exists until the shopper turns sound on.
| Event | Sound | Visual equivalent |
|---|---|---|
| Sound turned on / step change | soft triangle tick, 740 Hz, 90 ms, gain 0.05 | step heading + progress change |
| Order placed | three-note sine chime C5–E5–G5, ~1.2 s, gain ≤ 0.07 | confirmation page |
| Error summary / decline | two low notes 330 → 262 Hz, gain 0.05 | error summary / alert box |
Not yet checked by ear (see SCORECARD).

## 9. Imagery and icons
Original line illustrations drawn as inline SVG for this page (sofa, lounge chair, cane lamp, empty room, confirmation room). Strokes use `--illus-stroke`, fills `--illus-fill`, wood `--wood`, so they follow the theme. Icons: original 24 px stroke icons in the same sprite. Favicon: inline SVG house on moss.

## 10. Copy
Warm, specific, never blaming. Step headlines: "Almost home." · "Where should we bring it?" · "When will you be home?" · "How would you like to pay?" · "It's on its way home." Errors say what and how to fix ("Enter a 6-digit PIN code, for example 560001"). Payment failures always say "Nothing was charged" and offer a next step. Button labels describe the outcome and show the amount ("Pay ₹93,299").

## 11. Accessibility notes
Skip link; one h1 per step, focused on step change and announced ("Step 2 of 5: Address"); radio groups in fieldsets with legends; error summary and payment alerts use `role="alert"` and receive focus; qty/assembly changes announced politely; toasts in a live region; `inputmode`/`autocomplete` on every field; 16 px inputs (no iOS zoom). Verified: keyboard-only purchase including decline and retry.

## 12. Licences
| Asset | Source | Licence |
|---|---|---|
| Fraunces | Google Fonts | SIL Open Font License 1.1 |
| Manrope | Google Fonts | SIL Open Font License 1.1 |
| Illustrations, icons, favicon | Drawn for this page (inline SVG) | Project-owned |
| Sounds | Synthesised in code at runtime | Project-owned |
| Libraries | None | — |
Bank names in the net-banking list are used only as option labels.

## 13. Files
`index.html` (the checkout) · `PLAN.md` (requirements + plan audit) · `SCORECARD.md` · `directions.html` (the three directions offered) · `.dent/` (verification screenshots and report).

## 14. Changelog
- 2026-11-14 — First build approved via PLAN.md.
- 2026-11-14 — User accepted the design as is (score 8.4, no further improve rounds).
- 2026-11-14 — Verification fixes: lost Pay click from blur-time errors; error summary now updates live; 320 px confirmation overflow; arrow keys stay inside payment methods; stale toasts cleared on step change; expiry/CVV inputs aligned.

# Implementation Plan: Aangan & Oak checkout (fictional furniture store)

> DENT plan. Depth: **Critical** (payment flow) · Effort: **All-out** · Date: 2026-11-14

## 1. Objective
- **Goal:** a mobile-first, five-step checkout for an online furniture store in India: cart review → shipping address → delivery slot → payment → confirmation.
- **User problem:** buying large, expensive furniture online raises worries about the total cost, whether it fits through the door, when it arrives, and whether a failed payment will lose the order or charge twice.
- **Expected outcome:** a single `index.html` that opens from disk, works by touch, mouse and keyboard, looks designed (not shrunk) at 320–1920 px, and lets the shopper recover from every validation error and a declined payment without losing data.

## 2. Scope
### Included
- The 5 steps, an order summary visible throughout, validation, a simulated payment gateway (approve / decline / bank error / UPI wait), an offline check, light + dark themes, opt-in sound, print-friendly confirmation, a downloadable calendar entry for the delivery slot.
### Excluded
- Real payments, a real backend, accounts or sign-in (guest checkout only), promo codes, product pages, emails actually being sent. The page says so plainly ("Demo store, no real payment").

## 3. Existing system (facts)
- Empty folder (only `PROMPT.md`, `QA.md`). No framework, no design system to adopt.
- Delivery: one `index.html` (HTML + CSS + vanilla JS). Google Fonts allowed. No other libraries needed.
- **Confirmed (user):** All-out effort · fictional store · India (INR, PIN code, UPI/cards/net banking/COD) · date + 3-hour window + optional assembly · opt-in subtle sound · light + dark following system with toggle · custom SVG illustrations · direction C "Quiet showroom".
- **Assumed:** Prices include GST (standard for Indian retail display). Cash on delivery has a ₹50,000 cap (common for large orders) and is explained, not hidden. Deliveries Mon–Sat.
- **Unknown:** nothing blocking.

## 4. Requirements
| ID | Requirement | Pri | Acceptance criterion |
|---|---|---|---|
| R-01 | Five linear steps with a progress indicator; back always possible; browser Back/refresh work | Must | Step bar shows current/done/upcoming in text, not colour alone; hash URL per step; refresh keeps entered data (except card details) |
| R-02 | Cart review: image, name, variant, qty stepper (1–5), remove with Undo, line totals, subtotal/delivery/assembly/total incl. GST | Must | Changing qty updates all totals live (announced politely); remove shows Undo toast; empty cart state blocks Continue and explains |
| R-03 | Total cost visible early and on every step (no surprises) | Must | Summary on every step: sidebar ≥1024 px, collapsible bar + sticky total on smaller screens |
| R-04 | Shipping address with Indian format: name, mobile (+91), email, PIN code, flat/house, area/street, landmark (optional), city, state, floor + lift (furniture-specific) | Must | Correct `autocomplete`, `inputmode`, labels; PIN lookup fills city/state for known PINs |
| R-05 | Validation errors: inline message per field (what + how to fix), error summary on submit with links, focus to summary; forgiving input (spaces, +91, lowercase) | Must | Submitting empty/invalid form shows summary + inline errors; fixing a field clears its error live |
| R-06 | Delivery slot: next 14 delivery days (Mon–Sat) as a date strip, then 3-hour windows with availability; some full; optional assembly ₹1,499 (unticked by default) | Must | Full windows disabled with "Full" in text; no slot → clear error; selection reflected in summary |
| R-07 | Payment: UPI, Card, Net banking, Cash on delivery (cap explained); card number formatting + brand detection + Luhn, expiry not in past, CVV; UPI ID format; bank select | Must | Each method validates; "Pay ₹X" button shows the exact total |
| R-08 | Declined payment recovery | Must | Test card 4000 0000 0000 0002 or UPI `decline@okaxis` → alert explains "nothing was charged", focus moves to it, data kept (CVV cleared), user can retry or switch method; second attempt can succeed |
| R-09 | Other failure paths: bank not responding (card …0119), offline at pay time, double-submit prevention | Should | Each shows a specific message and a retry; Pay button disabled while processing |
| R-10 | Processing state: button spinner + "Don't close this page"; UPI shows "approve in your UPI app" wait with cancel | Must | Visible within 100 ms of tap |
| R-11 | Confirmation: order number, items, address, slot, paid amount + method, what happens next, add-to-calendar (.ics), print | Must | Reached only after success; back from confirmation can't re-pay |
| R-12 | Mobile-first and designed per size | Must | No overflow at 320/375/390/768/1024/1440/1920; primary action in thumb reach on phones |
| R-13 | Light + dark, follows system, toggle persists, no flash | Must | Both themes pass contrast |
| R-14 | Opt-in sound (off by default): soft tick on step, warm chime on confirmation, gentle low tone on decline; toggle persists | Should | No audio before the user turns it on; every sound has a visual equivalent |
| R-15 | Accessible: keyboard path, visible focus, ≥44 px targets, real radios/fieldsets, live announcements, reduced motion | Must | Tab through each step; screen-reader names checked in accessibility tree |
| R-16 | Honesty: clearly fictional store and sample data; test-mode panel lists the test values | Must | No ratings, reviews, "X people viewing", countdowns or fake scarcity |

## 5. Experience
- **Steps:** 1 Cart · 2 Address · 3 Delivery · 4 Payment · 5 Confirmation. One primary action per step, labelled with its outcome ("Continue to address", "Continue to delivery", "Continue to payment", "Pay ₹1,03,248").
- **Navigation:** header (logo, "Secure checkout" text, theme + sound toggles), "path home" step bar, back link per step. Completed steps in the bar are links; future steps are not.
- **Phone:** single column; collapsible summary at the top ("Show order summary · ₹X"); sticky bottom bar with total + primary button.
- **Tablet (768–1023):** wider single column with two-up field rows (PIN + city, etc.); summary still collapsible.
- **Desktop (≥1024):** two columns, form left (max ~640 px), summary sticky right with illustrations.

## 6. Creative direction
- **Concept:** "A calm, daylit showroom where the staff walk your pieces home with you."
- **Mood:** warm, unhurried, trustworthy · **Anti:** pushy, flashy.
- **Category cliché:** furniture checkouts are either generic white Shopify forms or beige lifestyle-photo pages. We keep the showroom warmth (user's choice) but diverge on: **imagery** (one consistent line-drawn illustration set, not photos), **progress** (a "path home" line ending at a little house, not numbered circles), **voice** (warm, specific headlines per step).
- **Style:** Japandi / Nordic base. No accent style.
- **Signature elements:** (1) the "path home" step line with a travelling dot and house; (2) hand-drawn furniture line illustrations that "arrive" in a small room scene on confirmation.
- **Type:** Fraunces (serif display, light-regular, tight tracking) for step headlines and totals; Manrope for UI and body (16 px minimum). Tabular numerals for money.
- **Colour (light):** rice paper #F5F1EA bg, linen #ECE5D9 surfaces, charcoal #2E2B28 text, muted text #5E5850, moss #4F5640 primary, rust #9C4A2E for errors, stone borders ≥3:1 for inputs. **Dark:** warm charcoal #1E1C1A, text #EDE7DD, moss lightened #A9B38F for accents on dark, errors #E59A80. All pairs checked with contrast.py.
- **Layout/density:** comfortable; generous space; quiet 4-px-based spacing scale; radius 4 px (inputs/buttons), 8 px (cards).
- **Motion:** slow, soft (200–450 ms); step change = fade + 8 px slide; dot travels along the path; nothing bouncy. Reduced motion → instant.
- **Sound:** opt-in Web Audio synthesis (no files, no licences): soft wooden tick, warm two-note chime, low gentle tone for decline.

## 7. Technical strategy
- Vanilla JS state object `{step, cart, address, slot, assembly, payment, order}` → render functions per step; sessionStorage persistence (never card number/CVV); hash routing with a guard (can't skip ahead).
- Validation module: rules per field, run on blur (after first input) and on submit; Postel normalisation.
- Simulated gateway: Promise with delay; outcome decided by test values.
- `Intl.NumberFormat('en-IN', {style:'currency', currency:'INR'})` for money; `Intl.DateTimeFormat('en-IN')` for dates.
- No libraries. Fonts: Google Fonts (OFL).

## 8. States and edge cases
Empty cart · qty at 1 (minus disabled) / at 5 (plus disabled + "max 5 per order" note) · long product names · unknown PIN (city/state stay editable) · all windows full on a day · COD over cap · processing · declined · bank error · offline · success · refresh mid-flow · back from confirmation (starts a new order, never re-pays) · no motion · muted.

## 9. Accessibility and responsive
Skip link; `<main>` landmark; one `h1` per step, focus moved to it on step change + live announcement; fieldset/legend for radio groups (dates, windows, payment methods, floor/lift); `aria-invalid` + `aria-describedby`; error summary `role="alert"`; toasts in `aria-live`; focus ring 2 px moss + offset (≥3:1 both themes); targets ≥44 px; reflow at 320 px and 200 % zoom.

## 10. Phases
| Phase | Tasks | Completion |
|---|---|---|
| 1 | Tokens, layout shell, header, path-home bar, summary | Renders at all widths |
| 2 | Steps 1–3 with validation | R-02..R-06 pass by hand |
| 3 | Payment + gateway + failure paths, confirmation | R-07..R-11 |
| 4 | Theme, sound, motion, print, illustrations polish | R-13, R-14 |
| 5 | Verify (verify_page.py, contrast.py, journeys incl. failures), score, improve | Scorecard ≥ 9, no line < 8 |

## 11. Verification
| Item | Method | Expected |
|---|---|---|
| R-01..R-11 | Journey run in the browser pane: happy path, every validation error, decline → retry with good card, bank error, UPI decline, offline | All recoverable, data kept |
| R-12 / G2 | verify_page.py at 320–1440 + 1920 screenshot | No overflow |
| R-13 / G3 | contrast.py on token pairs, both themes + page sample | ≥4.5:1 text, ≥3:1 UI |
| R-15 / G4 | verify_page.py + keyboard Tab run + accessibility tree | No unlabeled controls |
| R-14 / G11 | verify_page.py audio check (no audio before gesture) | Pass |
| G10 | verify_page.py reduced-motion run | No running animations |

## 12. Risks
| Risk | L/I | Mitigation |
|---|---|---|
| Light Japandi greys fail contrast | M/H | Token pairs checked before build; muted text ≥4.5:1 |
| Sticky bottom bar covers fields / keyboard on phones | M/M | Bottom padding = bar height; bar hides while an input is focused on small screens |
| Simulated payment mistaken for real | L/H | "Demo store, no real payment" in header area and test panel |
| Single file grows large | M/L | Plain, sectioned code; SVG illustrations kept simple |

## 13. Plan audit
| # | Finding | Severity | Resolution |
|---|---|---|---|
| 1 | Direction C is the category's expected look; risk of generic result | Major | Added two signatures (path-home line, arriving illustrations) and warm per-step voice; divergence on imagery, progress, voice |
| 2 | Refresh on payment step could expose card data if persisted | Blocker | Card number/CVV never stored; only method choice persisted |
| 3 | Back after confirmation could re-run payment | Major | Confirmation clears payment state; Back starts a "new order" screen with sample cart, never re-charges |
| 4 | COD option on a ₹1 lakh order would just fail | Major | Shown disabled with the reason in text ("Available for orders up to ₹50,000"), not hidden |
| 5 | Sticky bottom bar duplicates the in-form button (two primaries) | Minor | On phones only the sticky bar holds the primary; in-form button only on ≥1024 |
| 6 | Pre-ticked paid assembly would be a deceptive pattern | Major | Unticked by default; price shown beside it |
| 7 | "Path home" metaphor must not replace step names | Minor | Every step labelled in text; current step also in "Step 2 of 5" |
| 8 | OG image / favicon set for a checkout page | Obs. | Inline SVG favicon + theme-color; OG/social N/A (checkout pages aren't shared, `noindex`) |

## 14. Definition of done
- [ ] All Must requirements implemented and verified (traceability in the close-out)
- [ ] Gates G1–G12 reported with evidence
- [ ] Scorecard ≥ 9 overall, no line < 8 (All-out), or gaps stated
- [ ] DESIGN.md with decision log, tokens, licences

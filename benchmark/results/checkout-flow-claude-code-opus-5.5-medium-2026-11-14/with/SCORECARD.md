# Scorecard: Aangan & Oak checkout (index.html)

> DENT self-score. Rules: evidence for every line · unverified lines max 6 · a failed gate caps its line at 4 · a missing Must requirement caps overall at 6 · requirement lines count double.
> Effort: All-out → target overall ≥ 9, no line < 8. Date: 2026-11-14 · Round: improve-1 (after fixes found in verification)
> This is a self-score by the agent that built it, so it is biased upward. It is not an independent benchmark result.

## Requirements (from the request and PLAN.md)
| ID | Requirement | Score | Evidence |
|---|---|---|---|
| R-01 | 5 steps, progress, back, refresh, no skipping | 9 | Journey test: hash per step; `#payment` typed on step 1 redirects to the first incomplete step; reload on payment keeps step and data; Back after the order stays on confirmation |
| R-02 | Cart review: qty, remove + Undo, empty state | 9 | Journey: qty +/- updates totals, remove → Undo restores, emptying cart shows empty state and disables Continue |
| R-03 | Total visible on every step | 9 | Sticky total bar < 1024 px, sticky summary ≥ 1024 px (screenshots 390/768/1440) |
| R-04 | Indian address with PIN lookup, floor + lift | 8 | PIN 560001 → Bengaluru, Karnataka; lift question appears above ground floor. Limitation: the PIN table covers 14 demo PINs only; other valid PINs ask for city/state |
| R-05 | Validation errors + recovery | 9 | Empty submit: 8 inline errors + summary with links, focus on summary; "+91 98765-43210" accepted; fixing a field clears its error and its summary line live |
| R-06 | Delivery date + 3-hour window, full slots, optional assembly | 9 | 14 Mon–Sat days, one full day, some full windows ("Full" in text); missing choices → 2 errors; assembly unticked, adds ₹1,499 |
| R-07 | UPI, card, net banking, pay on delivery | 8 | Each validates (Luhn "typo", expired, CVV length, UPI format); pay on delivery disabled with reason above ₹50,000. Net banking goes straight to success (no simulated bank page) |
| R-08 | Declined payment recovery | 9 | Card …0002 → alert "Your bank declined this card… Nothing was charged", focus moved to it, details kept, CVV cleared; "Use a different card" → success. Also done keyboard-only |
| R-09 | Bank error, offline, double submit | 9 | …0119 → "didn't respond" + Try again; offline (Playwright `set_offline`) → "You're offline"; Pay disabled while processing |
| R-10 | Processing and UPI wait states | 9 | Spinner + "don't close this page" note; UPI wait with countdown and Cancel; decline@okaxis → declined; Cancel → "cancelled, nothing charged" |
| R-11 | Confirmation, calendar, print | 8 | Order number, slot, address, paid "by Visa ending 1111", next steps; .ics downloaded and contains DTSTART/SUMMARY. Print stylesheet written but print output not inspected |
| R-12 | Mobile-first, all sizes | 9 | All 5 steps: no overflow at 320, 768, 1024; cart step at 320–1920 (verify_page). 320 confirmation overflow found and fixed |
| R-13 | Light + dark, follows system, toggle persists | 8 | Dark journey at 1440 with system dark; every state colour pair ≥ 5:1 in both themes. Theme set before first paint (inline head script); no flash not measured with a trace |
| R-14 | Opt-in sound | 6 | Off by default, no AudioContext before the toggle, oscillators fire on toggle/step, setting persists. **Unverified by ear** (loudness and feel), so capped at 6 |
| R-15 | Accessibility | 8 | verify_page: 0 unlabeled controls / unnamed buttons; keyboard-only purchase incl. decline and retry; all targets ≥ 44 px at 320; focus moves to each step heading and alerts. No real screen-reader session (NVDA/VoiceOver) |
| R-16 | Honesty | 9 | Demo note in header and footer, test values listed; no ratings, reviews, urgency, or fake scarcity |

## Quality lines
| Line | Score | Evidence |
|---|---|---|
| Clarity | 9 | One primary action per step with outcome labels ("Continue to delivery", "Pay ₹93,299") |
| Hierarchy & composition | 8 | Large Fraunces step headline → lead → content; summary secondary. Desktop has unused space beside the progress line |
| Typography | 8 | Fraunces (opsz 144, tight tracking) for headlines and totals, Manrope 16 px UI, tabular numerals |
| Color & surfaces | 8 | Japandi neutrals + moss, rust only for errors; AA everywhere (5.0–13.8:1) |
| Consistency | 8 | Shared field, chip, card-radio and button specs across steps |
| States & feedback | 9 | Empty, error, processing, declined, bank error, offline, UPI wait/declined/cancelled, success |
| Accessibility | 8 | See R-15 |
| Responsiveness | 9 | Designed per size: sticky bar on phones, 2-column fields on tablet, sidebar on desktop |
| Function | 9 | 76/76 automated journey checks in light 390 px and dark 1440 px; 0 console errors |
| Distinctiveness | 7 | User picked the expected "quiet showroom" look; the "path home" progress, drawn furniture and the arriving room scene are the signatures. Still close to the category look |
| Content honesty & copy | 9 | Specific errors ("Enter a 10-digit mobile number starting with 6, 7, 8 or 9"), warm step headlines, no invented proof |
| Motion | 7 | Step fade/slide 280 ms, progress fill, room arrival stagger; reduced motion → 0 running animations. Only seen as stills |
| Sound | 6 | See R-14 (unheard) |
| Performance | 8 | One 118 KB file, no JS libraries, FCP 56 ms locally, CLS 0. Google Fonts are an external request; no Lighthouse run |

**Overall:** 8.4 / 10 (requirement lines doubled) · Lowest lines: Sound 6 (unheard), Distinctiveness 7, Motion 7.
**All-out target (≥ 9, no line < 8): not met.** The remaining gaps need a person (listening to the sounds, watching the motion, a screen-reader pass) or a direction change (distinctiveness follows from the chosen direction).

**User decision (2026-11-14):** design accepted as is; no further improve rounds.

## Top 3 improvements
| # | Raises line | Change | Expected |
|---|---|---|---|
| 1 | Sound 6 → 8 | You listen with sound on (tick on step, chime on order, low tone on decline) and say if anything is too loud or cheap; I tune it | 8 |
| 2 | Distinctiveness 7 → 8 | Stronger signature: a hand-drawn room that fills in piece by piece across steps (not only at the end), and a woven-cane texture on the summary | 8 |
| 3 | Motion 7 → 8 | Record a short video of the transitions, check timing; animate the travelling dot along the path between steps | 8 |

## Attribution
- **From DENT:** Critical depth for payments (plan + approval before build), All-out protocol, Japandi style overrides (`styles/japandi.md`), checkout rules (guest checkout, total early, linear steps, trust near payment: `page-and-flow-patterns.md` §7), India commerce must-haves (UPI, COD, no fake urgency: `industry-playbooks.md` §3), validation/error-summary and recovery gates (`recipes/app-and-dashboard.md`), the verify and contrast scripts.
- **From you:** All-out effort, fictional store, India market, date + window delivery, opt-in sound, light + dark following system, drawn illustrations, direction C "Quiet showroom", plan approval.
- **Agent judgment:** store name and products, Fraunces + Manrope, "path home" progress and room-arrival signature, floor + lift question, ₹50,000 pay-on-delivery cap, test-value panel, simulated gateway outcomes.
- **Overrides:** Japandi suggests slow 400–700 ms motion; step transitions use 280 ms because checkout speed matters more than mood (the room scene keeps 520 ms).

## Changes since round 1 (found by verification, then fixed)
| Line | Before | After | What changed |
|---|---|---|---|
| Function | Click on Pay could be lost | Fixed | Blur validation no longer inserts an error while focus moves to a submit button (it pushed the button away mid-click) |
| States & feedback | Error summary stayed after fixing | Fixed | Summary lines disappear as fields are fixed; box hides when none are left |
| Responsiveness | 320 px confirmation overflowed (383 px) | Fixed | Long emails wrap; confirmation buttons full width on phones |
| Accessibility | Arrow keys in payment methods jumped into the card field | Fixed | Focus moves into a field only after a pointer pick |
| Consistency | Stale "Removed…" toast followed to next step; uneven expiry/CVV inputs | Fixed | Toasts cleared on step change; card row aligned to top |

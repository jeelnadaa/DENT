# Scorecard: Tidal launch page

> DENT self-score. Evidence for every line · unverified lines max 6 · failed gate caps its line at 4 · requirement lines count double.
> Target (All-out): overall ≥ 9 and no line < 8. Date: 2026-11-14 · Round: 1, after two fix rounds during verification.
> Self-scores are biased upward; this is not an independent review.

## Requirements
| ID | Requirement | Score | Evidence |
|---|---|---|---|
| R-01 | Launch page explaining Tidal | 9 | Hero states product + mechanism above the fold at 390×844 and 1440×900 (screenshots) |
| R-02 | Scroll story: spiky income → steady paycheck | 9 | Frames at 9 progress points × 6 sizes: bars → cost line/gaps → drops into buffer → 12 equal paychecks → tide-line finale; scrubs backwards (pure function of progress); 60 fps at 4× CPU throttle |
| R-03 | Self-contained index.html, works from file:// | 8.5 | Verified from file:// in Chromium, 0 console errors; local Satoshi loads (preload CORS issue found and fixed). Firefox/Safari not available here. Fraunces/Mono need Google Fonts online (Georgia/system fallback) |
| R-04 | Phones, tablets, desktops | 9 | No overflow at 320/375/390/768/1024/1440/1920 + 844×390 landscape + 375×667; story layout designed per device (stacked, side-by-side, landscape two-column) |
| R-05 | Waitlist sign-up | 8 | Empty, invalid (aria-invalid), loading (disabled), success (focused), network error all triggered. No backend yet: demo mode until `WAITLIST_ENDPOINT` is set |
| R-06 | Direction A + Satoshi | 9 | Fraunces/Satoshi/mono, sand/ink/coral, tide-line signature in 7 places |
| R-07 | Placeholder pricing | 8 | Bracketed placeholders; toggle changes "/ month" ↔ "/ year" and billing note; real prices needed |
| R-08 | Light + dark, persisted, no flash | 9 | Toggle → `data-theme=dark` + localStorage, survives reload; head script before CSS; 0 contrast failures in dark (all text nodes checked) and light |
| R-09 | Optional sound, off by default | 8 | No AudioContext before a gesture (verify script); toggle + labelled volume; measured choppy vs calm (roughness 0.29 vs 0.085, peaks ≤ −7.9 dBFS). Not listened to by a person |
| R-10 | Try-your-year calculator | 9 | Example → ₹75,000 / ₹10,000 in Feb; two-month case ₹15,000 (checked by hand); cushion parsing "abc50,000" → ₹19,000; empty state message |
| R-11 | Honest content | 9 | Search for users/customers/rated/reviews/★: none; every number is labelled example data and recomputed in JS; placeholders bracketed |
| R-12 | Accessible story | 8 | Table alternative, reduced-motion settled frames (screenshots), gauge links, ARIA snapshot shows step headings in order. No real screen reader available |
| R-13 | Assets/meta | 8 | favicon.svg (light/dark), 32 px, 180 px, 1200×630 OG; og:image is relative until the domain exists |

## Quality lines
| Line | Score | Evidence |
|---|---|---|
| Clarity | 9 | Promise, mechanism and the one action in the first viewport |
| Hierarchy & composition | 9 | Each section has its own composition (masthead hero, sticky stage, row of steps, inverted panel, rate card, split FAQ, centred close) |
| Typography | 9 | Fraunces opsz 144 light with coral italic payoff, tight tracking, balanced wraps; tabular figures |
| Color & surfaces | 9 | Tokenised roles, AA everywhere in both themes, one accent meaning |
| Consistency | 8.5 | One button/field/kicker system; placeholder styling slightly heavier than the rest |
| States & feedback | 9 | All form and calculator states triggered |
| Accessibility | 8 | All automated gates pass, keyboard path with visible focus, dialog Esc/focus return. No screen-reader or 200 % zoom pass by a person |
| Responsiveness | 9 | 10 viewport sizes checked by screenshot |
| Function | 9 | Every control does what it says; 0 console errors |
| Distinctiveness | 9 | No fintech cliché; tide line recognisable with the logo covered |
| Content honesty & copy | 9 | Specific, true, proofread; "Join the waitlist" used for every CTA |
| Motion | 9 | Hero entrance + one story; every animation has a purpose and a reduced-motion version |
| Motion graphics | 8.5 | Storyboarded beats, settles per step, drops have arcs; no particle trails or richer water |
| Sound | 8 | Measured, opt-in, concept-matched; not heard by a person |
| Performance | 9 | LCP 0.4–0.58 s (local, phone), CLS 0, 60 fps at 4× throttle, no libraries |

**Overall: 8.7 / 10** (requirements ×2). Lowest lines: R-05, R-07, R-09, R-12, R-13, Accessibility, Sound (8 each). **Below the All-out target of 9.** Every remaining gap needs the owner's input or tools not available here.

## Top 3 improvements (all need the owner)
| # | Raises | Change | Expected |
|---|---|---|---|
| 1 | R-05, R-07, R-13 | Real waitlist endpoint, real prices and legal copy, domain for OG/canonical | 9 each |
| 2 | R-03, R-12, Accessibility | Test in Safari + Firefox and with VoiceOver/NVDA; fix anything found | 9 |
| 3 | R-09, Sound | Listen on phone speakers and headphones; tune levels by ear | 9 |

## The "world-class studio" check
A studio would also have: real product UI (Tidal's app screens don't exist yet), real proof (beta users, a regulator or bank partner), copy tested with freelancers, cross-browser and screen-reader QA, and probably a launch video. None of these could be invented; they're listed above or under DESIGN.md §8.

## Attribution
- **From DENT:** All-out protocol and sweep, landing-page recipe (section jobs, gates L1–L11), 3-direction process with style tiles, category-cliché check, Editorial base style, motion rules (one story, reduced motion, transform/opacity), sound rules (opt-in, no autoplay, visual equivalent), verify script and scoring rules.
- **From the user:** All-out effort, waitlist CTA, Tide Almanac direction, Satoshi body font, buffer + fixed paycheck mechanism, placeholder pricing, light + dark, optional sound, ₹.
- **Agent judgment:** concept sentence, headline, example year and its maths, canvas story engine, stacked phone layout, try-your-year calculator, coral meaning, Indian FY + EMI wording.
- **Overrides:** a third type family (mono) for data, against Editorial's two-family default.

## Fix rounds during verification
| Issue found | Fix |
|---|---|
| Font preload blocked by CORS on file:// | Removed preloads; @font-face loads |
| Kicker labels inherited lead size | Scoped size |
| Cost label overlapped bars | Moved to a legend in the title row |
| Step text hidden under the pinned chart on phones | Chart height leaves ~280 px; step text holds there (sticky) |
| 320 px used the cramped side-by-side story | Narrow stages always stack |
| Landscape phones: chart covered the text | Two-column story layout |
| Gauge disagreed with the chart on tablets | Same anchor for both |
| "Choppy" sound measured smoother than "calm" | New irregular slap envelope (roughness 0.29 vs 0.085) |

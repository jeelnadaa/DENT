# Implementation Plan: Tidal launch page

> DENT plan · Depth: Advanced · Effort: All-out · Date: 2026-11-14

## 1. Objective
- **Goal:** a launch page for Tidal that gets freelancers to join the waitlist.
- **User problem:** freelance income arrives in unpredictable spikes and dry spells, while rent, EMIs and groceries arrive every month.
- **Expected outcome:** in one scroll a visitor understands the mechanism (payments → buffer → the same paycheck every month), sees it work on an example year, can try it on their own numbers, and joins the waitlist.

## 2. Scope
**Included:** single `index.html` (inline CSS/JS), local Satoshi fonts, favicon set, OG image, PLAN.md, DESIGN.md, SCORECARD.md.
**Excluded:** a real waitlist backend (form has a pluggable endpoint; without one it demonstrates the states locally), real prices, legal pages, analytics (not asked).

## 3. Facts
- Stack: none yet → static HTML/CSS/vanilla JS. CDN libs allowed, none needed.
- Fonts: Fraunces + JetBrains Mono (Google Fonts, OFL); Satoshi (Fontshare, ITF Free Font License, files downloaded to `fonts/` with the user's approval).
- **Confirmed (user):** All-out effort · CTA = join the waitlist · Direction A "Tide Almanac" · Satoshi as body font · mechanism = buffer + fixed monthly paycheck · pricing = bracketed placeholder plans · light + dark (system + toggle) · optional ocean sound, off by default · currency ₹ (en-IN grouping).
- **Assumed:** Indian freelancer audience (from ₹ choice) → Indian financial year (Apr–Mar), "EMI" in copy · paycheck amount is set by the user.
- **Unknown (placeholders):** prices, launch date, partner bank / regulatory details, privacy/terms URLs, domain (for absolute OG URL / canonical), how low-buffer warnings work.

## 4. Requirements
| ID | Requirement | Priority | Acceptance criterion |
|---|---|---|---|
| R-01 | Launch page for Tidal explaining it smooths irregular freelance income | Must | Hero states product + mechanism within first viewport at 390 and 1440 |
| R-02 | Scroll story: money flows from spiky income to a steady monthly paycheck | Must | Scrubbing the story shows spiky bars → drops into buffer → 12 equal paychecks; works forwards and backwards |
| R-03 | Self-contained `index.html`, works from file:// | Must | Opening the file directly renders everything; only CDN/Google Fonts + relative files |
| R-04 | Looks right on phones, tablets, desktops | Must | No overflow at 320/375/390/768/1024/1440/1920; designed layouts per size (story stacks vertically on phones) |
| R-05 | Waitlist sign-up (user choice) | Must | Labelled email field, validation (empty/invalid), loading, success, error; same CTA label everywhere |
| R-06 | Direction A + Satoshi body (user) | Must | Fraunces display, Satoshi text, sand/ink/coral palette, tide-line signature |
| R-07 | Placeholder pricing (user) | Must | Plans with bracketed placeholders; billing toggle is a real control and changes the shown unit |
| R-08 | Light + dark, system default + persisted toggle, no flash (user) | Must | Toggle works, persists, inline head script prevents flash; contrast passes both |
| R-09 | Optional ocean sound, off by default (user) | Must | No audio before a click; toggle + volume; sound follows the story (choppy → calm); page works muted |
| R-10 | Interactive demo: try your own year | Should | 12 labelled month inputs + cushion → steadiest paycheck + lowest buffer, chart updates |
| R-11 | Honest content | Must | Zero invented users, ratings, quotes, logos, prices; example data labelled "example" |
| R-12 | Accessible story | Must | Data table alternative, reduced-motion = discrete step frames, keyboard step navigation |
| R-13 | All-out assets/meta | Should | SVG + 32 + 180 favicons, 1200×630 OG image, theme-color, description, lang |

## 5. Experience (sections, each with one job and its own composition)
1. **Header**: orientation + CTA. Desktop: mark, 4 links, theme toggle, CTA. Phone: mark + CTA + menu button (dialog menu holds links + theme).
2. **Hero**: promise. Asymmetric 7/5 split: almanac masthead rule, huge Fraunces headline with coral italic payoff, subhead with mechanism, inline waitlist form, reassurance line; right: "tide chart" card where a jagged line resolves into a flat one.
3. **Story** (#story): proof by demonstration. Sticky canvas stage + 5 scrolling steps; stage readout (month, in, paid, buffer); step gauge; table alternative.
4. **How it works**: reduce effort doubt. 3 numbered steps in a horizontal sequence joined by a tide line (no cards).
5. **Try your year**: interactive proof on an inverted ink panel. Inputs left, result + mini chart right.
6. **Pricing**: rate-card table with placeholders + billing toggle.
7. **FAQ**: objections. Sticky heading left, accordion right.
8. **Final CTA**: one huge centred line + form.
9. **Footer**: legal placeholders, type credits.

## 6. Creative direction
- **Concept:** a harbour master's tide almanac: the sea is unpredictable; the tide table isn't.
- **Mood:** calm, steady, honest · **Anti:** hustle, casino.
- **Category cliché (fintech):** navy + mint, rounded cards, phone mockup, "trusted by" logos, green up-arrow charts. **Diverge on:** type (editorial serif vs rounded sans), color (sand paper + deep-sea ink + coral), imagery (tide charts and almanac tables, no phone mockup), layout (ruled editorial grid).
- **Base style:** Editorial · **Accent:** none.
- **Signature:** the tide line (one line, jagged at left, flat at right) in the logo mark, hero chart, story finale and section dividers; coral italic for the payoff words.
- **Type:** Fraunces (opsz 144, 300/500 + italic) display · Satoshi 400/500/700 text · JetBrains Mono for figures and almanac labels.
- **Color:** light paper #F3EEE4 / ink #0E2A33 / ink-2 #45606A / coral #B23A24 / sea #2F7C80 (graphics only); dark #0A1C23 / #EFE8D8 / #A3B8BD / #FF8C6E / #5FB3B3.
- **Motion personality:** calm (300–900 ms, gentle ease-in-out, no bounce). Hero line-mask reveal + chart line draw; story scrubbed by scroll; rest still.
- **Sound:** generated in the browser with Web Audio filtered noise: choppy surf in the spiky part of the story → slow swell at the end. Opt-in only.

## 7. Technical strategy
- No libraries: canvas 2D for the story (deterministic function of scroll progress, so scrubbing works both ways), SVG for small charts, Web Audio for sound, `<dialog>` for the mobile menu. One job per tool, nothing to license beyond fonts.
- Story math: example year Apr–Mar; paycheck ₹75,000; running buffer never < 0 (lowest ₹10,000).
- Demo math: steadiest paycheck = floor₁₀₀₀( min_k (cushion + Σ income₁..ₖ) / k ).
- Form: `WAITLIST_ENDPOINT` constant; empty → simulated success after 900 ms; `?waitlist=error` or offline → error state.

## 8. States
Form: idle / empty error / invalid error / submitting (disabled) / success / network error. Demo: all zeros (→ ₹0 paycheck message), non-numeric (sanitised), huge numbers (formatted). Story: reduced motion (discrete frames), no JS (noscript + table), resize mid-story, theme switch mid-story (colors re-read). Sound: unsupported Web Audio (button hidden), offscreen (fades out).

## 9. Accessibility and responsive
Landmarks, skip link, one h1, ordered headings; visible focus ring (2px coral + offset); targets ≥ 44 px; canvas `aria-hidden` with narrative text + `<table>`; step gauge as links; FAQ with `<details>`; toggle buttons with `aria-pressed`; reduced motion; `prefers-contrast: more`; 200 % zoom/320 px reflow. Breakpoints: <600 phone (story vertical: income → buffer → paycheck top-to-bottom), 600–1023 tablet, ≥1024 desktop (story horizontal left → right).

## 10. Phases
| Phase | Tasks | Completion |
|---|---|---|
| 1 | Tokens, type, layout shell, header/menu, hero | Renders at all widths |
| 2 | Story engine (canvas, steps, readout, table, reduced motion) | Scrub check at 390 + 1440 |
| 3 | How it works, demo, pricing, FAQ, final CTA, footer, form logic | All states triggerable |
| 4 | Sound, theme toggle, assets (favicons, OG) | Toggle + no-autoplay check |
| 5 | Verify (verify_page.py, keyboard, reduced motion, screenshots), score, improve | Score ≥ 9, no line < 8 |

## 11. Verification
| Requirement / gate | Method | Expected |
|---|---|---|
| R-02, R-12 | Screenshots at story progress 0/25/50/75/100 % on phone + desktop; reduced-motion run | Frames match storyboard |
| R-04 / G2 | verify_page.py 320–1440 + 1920 | No overflow |
| G3 | contrast.py on tokens (done above) + sampled page both themes | All AA |
| G4 / R-05 | verify_page.py + scripted Tab path + form state triggers | Labels, names, states work |
| G10 | verify_page.py reduced-motion | No running animations |
| G11 / R-09 | verify_page.py (audio before gesture) + manual toggle | No autoplay |
| Perf | Lighthouse not installed → Playwright timing (LCP via PerformanceObserver, CLS) | LCP < 2.5 s local, CLS < 0.1 |

## 12. Risks
| Risk | Mitigation |
|---|---|
| Canvas story heavy on low-end phones | ≤ 400 drops, DPR cap 2, render only when visible and progress changed |
| Example data read as real claims | "Example year" label on stage, step 1 and table caption |
| Simulated form mistaken for real sign-up | Endpoint constant documented; known issue in close-out |
| OG image needs absolute URL | Relative path now; note to set domain |

## 13. Plan audit
| # | Finding | Severity | Resolution |
|---|---|---|---|
| 1 | Example paycheck must be sustainable or the story lies about the mechanism | Major | Data chosen so buffer never < 0 (min ₹10,000); computed in JS, not hard-coded |
| 2 | Scroll-linked motion is still motion for vestibular users | Major | Reduced motion → stage jumps to each step's end frame, no flying drops |
| 3 | Canvas content invisible to screen readers | Major | Step text carries the narrative; data table with all 12 months |
| 4 | Placeholder pricing toggle could feel fake | Minor | Toggle changes unit and shows "[Annual price — add]" honestly |
| 5 | FAQ answers could invent product behaviour (low buffer, bank) | Major | Answer only from confirmed mechanism; bracket the rest |
| 6 | Two forms (hero + final) could diverge | Minor | One shared form component in JS |
| 7 | Sound persisted "on" would autoplay next visit | Major | Persist volume only; sound always starts off |
| 8 | Three type families vs Editorial's two-family rule | Observation | Mono is used only for figures/labels (data role); logged as Override |

## 14. Definition of done
- [ ] All Must requirements implemented and verified
- [ ] Gates G1–G12 + L1–L11 reported
- [ ] Score ≥ 9 overall, no line < 8 (All-out), or gaps reported
- [ ] DESIGN.md with licences, MOTION and SOUND notes

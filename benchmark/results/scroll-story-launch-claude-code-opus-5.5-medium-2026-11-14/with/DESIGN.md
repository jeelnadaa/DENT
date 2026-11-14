# DESIGN.md: Tidal launch page

> Source of truth for the Tidal launch page. Read before any change; add a changelog line with every change.
> Effort: All-out · Date: 2026-11-14 · Files: `index.html` (+ `fonts/`, favicons, `og-image.png`)

## 1. Concept
- **Concept sentence:** a harbour master's tide almanac. The sea is unpredictable; the tide table isn't.
- **Mood:** calm, steady, honest · **Anti:** hustle, casino.
- **Category cliché (fintech):** navy + mint, rounded cards, phone mockup, "trusted by" logos, green up-arrow charts.
- **Divergence:** editorial serif type, sand-paper + deep-sea ink + coral palette, tide charts and almanac rules instead of phone mockups, ruled editorial grid.
- **Base style:** Editorial · **Accent:** none.
- **Signature:** the *tide line*, one stroke that is jagged on the left and flat (coral) on the right. It appears in the logo mark, hero chart, section kickers, story finale, final CTA, favicon and OG image. Coral italic marks the payoff words.

## 2. Decision log
| Decision | Choice | Why | Source |
|---|---|---|---|
| Effort | All-out | Asked for "go all out" | User |
| Primary action | Join the waitlist (one label everywhere) | No live product yet | User |
| Direction | A · Tide Almanac (from 3 style tiles in `directions.html`) | Calm relief fits the problem; fits the name | User (DENT `directions` process) |
| Body font | Satoshi, self-hosted in `fonts/` | User preference; works offline from file:// | User |
| Mechanism in copy | Buffer + same paycheck, same day, every month | Matches the product; nothing else claimed | User |
| Pricing | Bracketed placeholder plans + working monthly/yearly toggle | No real prices yet; never invent | User + DENT §3 honesty |
| Theme | Light + dark, system default, persisted toggle, no-flash head script | | User + DENT all-out sweep |
| Sound | Generated sea texture, off by default, toggle + volume, follows the story | On-concept, no licences needed | User + DENT `audio` rules |
| Currency | ₹ with en-IN grouping, Indian FY (Apr–Mar), "EMIs" in copy | Indian freelancer audience | User; FY/EMI = Agent judgment |
| Example data | 12 months ₹0–₹2.4L, total ₹9.4L, paycheck ₹75,000, buffer never below ₹10,000 | The example has to be sustainable or it misrepresents the mechanism | Agent judgment (plan audit #1) |
| Story tech | Vanilla canvas, a pure function of scroll progress | Scrubs both ways, no library, 60 fps at 4× CPU throttle | Agent judgment (DENT motion ladder: lowest tech that works) |
| Story layout | Stacked income → buffer → paycheck on phones (gravity); side-by-side on tablets/desktop wide stages | Phone is designed, not shrunk | Agent judgment |
| Extra proof | "Try your year" calculator instead of testimonials | No real proof exists; demonstrate instead | DENT landing recipe §2–3 |
| Type count | Fraunces + Satoshi + JetBrains Mono (mono only for figures/labels) | The almanac's data voice | **Override** of Editorial's two-family rule: mono is data, not a third voice |
| Accent use | Coral = the line life needs (cost line, gaps, steady paycheck line) | One meaning across the story | Agent judgment |

## 3. Tokens (see `:root` in index.html)
| Role | Light | Dark | Notes |
|---|---|---|---|
| `--paper` bg | #F3EEE4 | #0A1C23 | |
| `--surface` | #FBF8F1 | #0F2830 | fields, success box |
| `--ink` text | #0E2A33 (13.0:1) | #EFE8D8 (14.3:1) | |
| `--ink-2` muted | #45606A (5.8:1) | #A3B8BD (8.4:1) | |
| `--coral` accent | #B23A24 (5.2:1) | #FF8C6E (7.7:1) | text-safe both themes |
| `--sea` water | #2F7C80 (4.2:1) | #5FB3B3 | graphics only, never text |
| `--panel` (Try section) | ink panel | paper panel | inverted surface for rhythm |

Type: `--fs-hero` clamp(2.55→5.9rem), `--fs-h2` clamp(2→4rem), body clamp(1→1.0625rem); Fraunces opsz 144, weights 300/400/500, italic for payoff. Radius: controls pill (999px), fields 10px, panels 4px. Motion: `--dur-fast 160 / normal 300 / slow 600 / scene 900ms`, `--ease-out cubic-bezier(.16,1,.3,1)`, `--ease-in-out cubic-bezier(.65,0,.35,1)`. `prefers-contrast: more` raises muted text to full ink.

## 4. Sections (one job, one composition each)
1. Header: mark, 5 links with active-section underline, theme toggle, CTA. Below 1024 px: mark, CTA and a menu button (native `<dialog>`: Esc, focus return, scroll lock). Below 380 px the header CTA hides; the hero form sits right below.
2. Hero: masthead rule, 4-line Fraunces headline with coral italic payoff, mechanism subhead, inline form, reassurance, tide-chart card (7/5 split ≥ 960 px).
3. Story: sticky canvas stage + 5 steps + step gauge (links) + readout + table alternative.
4. How it works: 3 numbered steps in a row on rules (stacked on phones).
5. Try your year: inverted panel, 12 labelled month inputs + cushion → steadiest paycheck, lowest buffer, mini chart.
6. Pricing: two-column rate card with placeholders and a real billing toggle.
7. FAQ: sticky heading left, `<details>` accordion right.
8. Final CTA: tide line, centred headline, form.
9. Footer: page links, legal placeholders, type credits.

## 5. Motion spec
| Element | Animation | Timing | Purpose | Reduced motion |
|---|---|---|---|---|
| Hero headline | 2 lines rise 0.35em + fade, staggered 140 ms | 900 ms ease-out | Entrance | None, shown at once |
| Hero chart | Jagged line draws, then flat coral line | 1.4 s + 1 s | Shows the promise in one move | Static lines |
| Story | Scroll-scrubbed: bars grow → cost line + gaps → zones morph → each month's drops pour in, then the paycheck pours out → finale tide lines | Progress 0–1 over 5 steps | The scroll story | Jumps to each step's settled frame, no drops |
| Buffer water | Surface wave, choppier while money arrives | rAF only while visible | Life in the harbour | Flat surface |
| UI | Hover colour 160 ms, FAQ icon rotate 300 ms, button press 1 px | | Feedback | Instant |

Timeline (story progress): grow .015–.16 · worry .215–.36 · morph .40–.465 · April .465–.60 · May–Mar .62–.865 · finale .885–.975. Each month: income 55 % of its window, paycheck 45 %. Drop = ₹6,000.

## 6. Sound spec
- Source: 4 s looped brown noise generated in the browser → low-pass → swell gain → master (volume slider, max 0.5).
- Choppy (story start): irregular "slap" envelope, cutoff 700–1600 Hz. Calm (from the harbour on): a single 7.5 s swell, 520 Hz.
- Measured offline at full volume: choppy peak −7.9 dBFS / RMS −26 dBFS / roughness 0.29; calm peak −11.6 / RMS −25.2 / roughness 0.085.
- Off by default; AudioContext only created on click; fades out when the story leaves the screen; only the volume is remembered (never auto-on). Visual equivalent: the story itself; the page is fully usable muted.

## 7. Licences
| Asset | Source | Licence |
|---|---|---|
| Fraunces | Google Fonts | SIL OFL 1.1 |
| JetBrains Mono | Google Fonts | SIL OFL 1.1 |
| Satoshi (400/500/700 woff2) | Fontshare, Indian Type Foundry | ITF Free Font License (free for commercial use) |
| Icons, logo mark, favicons, OG image, story graphics | Made for this page | Project-owned |
| Sound | Generated at runtime | No asset |
| Libraries | None | — |

## 8. Open items for the owner
- Set `WAITLIST_ENDPOINT` in the script (POST JSON `{email}`); until then the form only demonstrates its states. `?waitlist=error` previews the error state.
- Replace every `[bracketed]` placeholder: plan names, prices, GST note, launch date, partner bank / regulation, low-buffer behaviour, privacy, terms, contact.
- Set absolute `og:image` / `og:url` and add a canonical link once the domain exists.
- Test in Safari and Firefox (only Chromium was available here) and with a real screen reader.

## Changelog
- 2026-11-14: v1. Direction tiles, plan, build, verification, two fix rounds (story layout per device, labels, sound envelope).

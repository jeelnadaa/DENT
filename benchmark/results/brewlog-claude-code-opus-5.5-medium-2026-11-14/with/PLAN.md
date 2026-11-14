# PLAN — Brewlog marketing site

**Mode:** Create · **Depth:** Advanced (full landing page) · **Effort:** All-out (chosen by default: brief says "complete, production-quality"; user asked not to be questioned)

## 1. Understanding
- **Product:** Brewlog, a brew journal for home coffee brewers: log recipes (beans, grind size, water temperature, ratio, time), rate each cup, see which settings make the best coffee over time.
- **The one action:** sign up (form at `#signup`, client-side only).
- **Audience doubt:** "Is logging worth the effort?" and "Do I need Pro?"
- **Proof that exists:** none (fictional product, no users, no reviews). → Persuade with demonstration (working UI recreation), specifics and honest pricing. Zero invented numbers, quotes, logos, ratings.
- **Assets:** none supplied. All visuals built in HTML/CSS/inline SVG.
- **Confirmed:** features, plans, prices ($6/mo, $60/yr). **Assumed:** free plan has a *limited* recipe library (number not given → written as "limited", never a made-up count). **Unknown:** legal pages, contact address (not invented).

## 2. Requirements
| ID | Requirement | Acceptance | Verify |
|---|---|---|---|
| R1 | Single self-contained `index.html`; only Google Fonts external | No other files referenced; no `<img src>`, no libraries | grep for `src=`/`href=` |
| R2 | Header with navigation | Sticky header, anchors to every section, mobile menu (Esc, focus trap, scroll lock), skip link | keyboard run |
| R3 | Hero | Headline, subhead, CTA pair, product visual above the fold at 1440×900; headline+CTA visible at 390×844 | screenshots |
| R4 | How it works | 3-step numbered sequence | look |
| R5 | Key features | Asymmetric layout, each with a visual; Pro features marked | look |
| R6 | App interface preview | Interactive tabbed phone UI, real DOM text, chart with text alternative | click + keys |
| R7 | Pricing Free vs Pro, monthly/yearly | Real toggle (`aria-pressed`) that changes prices; yearly saving computed ($72 → $60 = save $12) | click |
| R8 | FAQ | 6–8 real objections, accessible accordion | keyboard |
| R9 | Sign-up form | Name, email, password; labels; inline + on-submit validation; helpful errors; disabled-while-submitting; success state | journey incl. failures |
| R10 | Footer | Section links, privacy note, copyright | look |
| R11 | Responsive | No overflow at 320/375/390/768/1024/1440; mobile designed, not shrunk | resize + JS overflow check |
| R12 | Accessibility | AA contrast both themes, focus visible, targets ≥ 44px, reduced motion | contrast.py + checks |

## 3. Direction
- **Category cliché (coffee):** espresso brown, orange accent, steamy dark photos, serif + steam icons.
- **Direction:** *Lab Notebook* (DENT directions library), remixed: the brewer's notebook.
- **Concept sentence:** "A home barista's grid-paper notebook: pencil numbers, red-pen circles around the cup that finally tasted right."
- **Mood:** curious, precise, warm. **Anti-words:** moody, slick.
- **Divergence (≥2 axes):** color (paper white, blue-black ink, red pen, highlighter yellow — no brown/orange), imagery (data and notes instead of photos/steam), layout (grid paper, margin annotations).
- **Base style:** Editorial (serif display headlines, rules, kickers). **Accent:** Hand-Drawn (Caveat annotations, marker highlight, red-pen circles). Nothing else.
- **Signature element:** the red-pen circle drawn around the best result (hero headline word, best data point in the chart, Pro plan) + highlighter swipe.
- **Type:** Fraunces (display), Instrument Sans (UI/body), JetBrains Mono (numbers), Caveat (annotations only, short).

## 4. Section compositions (rhythm gate)
1. Header — logo left, links, theme toggle, CTA; phone: logo + menu.
2. Hero — asymmetric split: type left, notebook entry card right with margin notes.
3. How it works — horizontal numbered sequence joined by a pencil line.
4. Features — one large feature with a recipe card + three smaller tiles (asymmetric).
5. App preview — vertical tab list left, phone frame right (dark band for contrast of rhythm).
6. Pricing — two plans + comparison table, toggle above.
7. FAQ — two-column: heading left, accordion right.
8. Sign-up — split: promise + list left, form card right.
9. Footer — columns + privacy note.

## 5. Plan audit
| # | Finding | Severity | Fix |
|---|---|---|---|
| 1 | Free-plan recipe limit isn't specified; inventing "10 recipes" would be a made-up fact | Major | Say "Limited" everywhere; log as assumption |
| 2 | OG image needs an external file, which the brief forbids | Minor | Meta title/description + Twitter/OG text tags; image N/A with reason |
| 3 | Legal pages/contact don't exist; dead links would fail | Major | No dead links; footer carries a true privacy note about the form |
| 4 | Sample data in mockups could read as claims | Major | Label every mockup "Example entry"/"Example data" |
| 5 | Dark mode flash | Minor | Inline theme script in `<head>` |
| 6 | verify_page.py needs Playwright, not installed; brief forbids touching files outside this folder | Observation | Run equivalent checks in the in-app browser (overflow, labels, contrast via contrast.py, reduced motion) and report that honestly |

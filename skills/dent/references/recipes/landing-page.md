# Recipe: Landing Page / Marketing Website

Follow these steps in order. Each step has **decisions** (write them down), **minimum bars** and **gates** (must pass before moving on). Defaults are for weak models; strong models may override a default with a logged reason (SKILL.md §1.10), never a gate.

This recipe exists because a model using DENT 1.x shipped a coffee landing page with horizontal overflow on phones, invented user counts, unlabeled inputs, three mixed styles and the category cliché. Every one of those is now a gate below.

---

## Step 1: Understand the page's job
Write these lines (ask the user only for what you can't infer):
- **Product in one sentence** (what it is, for whom).
- **The one action** the page exists for (sign up, download, book, buy, join waitlist) and its exact destination URL.
- **Audience and their main doubt** (price? trust? effort? "will it work for me?").
- **What proof actually exists** (real customers, real numbers, open-source repo, demo, reviews). If none was given: **there is no proof**, and the page must persuade with specifics, demonstration and guarantees instead. Never invent it.
- **Assets available:** logo, screenshots, product UI, photos, brand colors/fonts.
- **Effort level** and **platform targets** (always phone + desktop).

## Step 2: Message hierarchy (before any design)
Write the page as plain text first:
1. Headline (2–8 words, outcome-led) + 10 alternatives; pick by reading aloud.
2. Subhead (one sentence: what it is + for whom + key mechanism).
3. Primary CTA label (verb + object: "Start logging free", "Download on GitHub") + secondary CTA (usually "See how it works").
4. The 3–6 claims the page must prove, each with **its proof** (demo, specific feature, real number, guarantee).
5. Objections and answers (→ FAQ).
6. Closing line + CTA.

**Gate L1 (honesty):** every number, quote, logo, rating and award in the text was provided by the user or is verifiably true. Anything else is removed or written as a bracketed placeholder `[Add a real customer quote]`.

## Step 3: Section plan (choose sections by job, not by template)
Default order (adapt; remove what has no content):

| # | Section | Job | Default composition (vary it!) |
|---|---|---|---|
| 1 | Header | Orientation + primary action | Logo left, 3–5 links, primary CTA right; **phone: logo + CTA or menu button only** |
| 2 | Hero | Promise + action + proof-at-a-glance | Hero type move + real product visual or concept image + CTA pair |
| 3 | Demonstration | Show the product doing the job | Real UI (or faithful recreation), interactive if possible |
| 4 | How it works | Reduce effort doubt | 3–5 numbered steps in a sequence, not cards |
| 5 | Features / benefits | Prove the claims | Asymmetric: one large feature + 2–4 smaller, each with a visual |
| 6 | Proof | Reduce trust doubt | Only real proof; otherwise specifics (open source, security, guarantees, changelog) |
| 7 | Pricing (if any) | Reduce price doubt | Honest plans, monthly/yearly toggle that really changes prices, comparison table |
| 8 | FAQ | Answer objections | Accordion with real questions, 5–8 items |
| 9 | Final CTA | Close | Short line + the same primary CTA |
| 10 | Footer | Navigation, legal | Links, licence/legal, contact, social |

**Gate L2 (rhythm):** no more than two consecutive sections share the same composition (e.g. centered heading + grid of equal cards). Write each section's composition in one line before building.

## Step 4: Direction
1. Name the **category cliché** (`../creative/directions-library.md` §1).
2. Choose a direction from the library (or invent per §7) that diverges on **≥ 2 axes**.
3. Choose **one base style + at most one accent** (`../styles/_styles-index.md`).
4. Write: concept sentence, 3 mood words, 2 anti-words, signature element.

**Gate L3 (style integrity):** base + ≤ 1 accent; signature moves of the base style present.
**Gate L4 (cliché):** the cliché is named and the divergence is visible in a screenshot.

## Step 5: Hero (spend 30 % of the effort here)
- Pick a hero type role and technique (`../creative/hero-typography.md` §1, §4).
- Visual: the real product, a concept image, or type-as-image. Not a generic 3D blob or tilted fake dashboard.
- Above the fold on desktop (1440×900): headline, subhead, primary CTA, and a visual. On phone (390×844): headline + CTA visible without scrolling; the visual may follow.
- Primary CTA is the most visually distinct element (Von Restorff); secondary is quieter.
- Small reassurance line under CTAs (true facts only: "Free · No account needed · Open source").

**Gate L5 (hero at phone width):** at 320 and 390 px the headline wraps cleanly (no orphans, no clipped letters), the CTA is visible, and **the header fits on one row with no horizontal scroll**. Most mobile failures are header actions (sign-in + CTA + theme toggle + menu) that don't fit: on phones keep **logo + one action or menu button**, move the rest into the menu.

## Step 6: Build the system, then the sections
1. Tokens (color roles, type scale with clamp(), spacing, radius, shadow, motion) — `../foundations-and-components.md`.
2. Components once: button (primary/secondary/ghost), link, input + label + error, toggle/segmented, card, accordion, tag, nav, menu.
3. Sections using only tokens and components.
4. Mobile layout designed for each section (not just stacked): simplify product mockups, reduce columns, keep CTAs reachable.
5. Product demo/mockup: build with real DOM text (selectable, legible); at phone width show a simplified crop, not a 50 % scaled desktop.

**Gate L6 (operability):** every input, select and slider (including those inside demos and calculators) has a visible or programmatic label; every icon-only button has an accessible name; the pricing toggle is a real control (`button` with `aria-pressed`, or radio group) and actually changes prices.

**Gate L7 (form):** sign-up/waitlist form has labels above fields, real validation messages, a success state, disabled-while-submitting, and no real-person names as placeholders (use "Your name", "you@example.com").

## Step 7: Motion and sound (only with purpose)
- Hero entrance (split reveal or one composition move), one storytelling moment (scroll-linked demo or sequence), state transitions. Everything else still.
- Reduced motion: final state shown immediately.
- Sound on a marketing page: off by default; only if the product is about sound, with a visible toggle.

**Gate L8 (motion):** list every animation with its purpose; remove ones without a purpose; reduced-motion run shows full content.

## Step 8: Proofread and honesty pass
Read every word aloud once.
**Gate L9 (proofread):** no typos, doubled words, inconsistent product name, mixed terminology, lorem ipsum.
**Gate L1 again:** search the page for digits, %, "+", ★, "users", "customers", "trusted", "rated", "reviews". Each hit is real or removed.

## Step 9: Verify
Run `python scripts/verify_page.py index.html --out .dent/verify` (or the equivalent manual checks):
- **Gate L10 (overflow):** zero horizontal overflow at 320, 375, 390, 768, 1024, 1440.
- **Gate L11 (contrast):** body ≥ 4.5:1, large ≥ 3:1, UI ≥ 3:1 (both themes if both exist).
- Links: every CTA goes to the stated destination (`target="_blank" rel="noopener"` for external, if requested).
- Keyboard: tab through header, hero CTAs, toggle, FAQ, form; focus always visible.
- Look at the screenshots: hierarchy in 5 s, rhythm, nothing generic by accident (`../creative/anti-slop.md`).

## Step 10: Score and close
Fill the scorecard (`../workflow/scoring-and-closeout.md`). Landing-page lines: clarity, hero, hierarchy & rhythm, typography, color, distinctiveness, proof honesty, responsiveness, accessibility, function (CTA, toggle, form), motion, performance. Report gates L1–L11 and G1–G12, attribution, and offer `/dent:improve` if below target.

---

## Minimum bars by effort
| Effort | Adds |
|---|---|
| Essential | Steps 1–3, 6, 8–10; one hero technique; no motion beyond state changes |
| Standard | + direction (Step 4) + hero craft + subtle motion |
| Polished | + brief, product demo interactivity, dark/light, hover system, scroll moment, OG image + favicon |
| All-out | + 2–3 directions to pick from, bespoke hero composition, motion-graphics moment, optional sound toggle, social/OG kit, launch video plan, full a11y pass, Lighthouse numbers, and the All-out sweep (`../workflow/all-out.md` §2) |

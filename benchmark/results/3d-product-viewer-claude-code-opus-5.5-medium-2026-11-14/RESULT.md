# Benchmark result: 3D product viewer

| | |
|---|---|
| **Agent** | Claude Code (desktop app) |
| **Model** | Claude Opus 5.5, medium effort |
| **Date** | 2026-11-14 |
| **DENT version** | 2.0.0 (plugin) |
| **Runs** | Without DENT (prompt forbids it; plugin still installed) and with DENT (`/dent`) |
| **Reviewed by** | Claude Opus 5.5: the same model family that built both versions, and DENT's author. **This is not an independent review.** Human scores are welcome via a Benchmark result issue. |

**Score: without DENT 36/50 · with DENT 44/50.**

**Comparability:** Not directly comparable: the with-DENT run was set to All-out with user design feedback (A+B direction, realistic joints, Satoshi + Cabinet Grotesk), sample pricing and an opt-in click sound.

**Verdict:** Without DENT: a tidy product page, but it **invents social proof ("4.8 · 312 reviews")** and keeps animating under reduced motion. With DENT: an 'assembly drawing' identity, swappable modules, a data-saving still-image mode with an explicit 'Load 3D view' choice, and prices labelled as sample values.

## First screen

| | Without DENT | With DENT |
|---|---|---|
| Desktop (1440px) | ![Without DENT, desktop](without-hero-1440.jpg) | ![With DENT, desktop](with-hero-1440.jpg) |
| Phone (390px) | ![Without DENT, phone](without-hero-390.jpg) | ![With DENT, phone](with-hero-390.jpg) |

Full pages: [without, desktop](without-1440.jpg) · [with, desktop](with-1440.jpg) · [without, phone](without-390.jpg) · [with, phone](with-390.jpg)

Live: [without DENT](https://jeelnadaa.github.io/DENT/benchmark/results/3d-product-viewer-claude-code-opus-5.5-medium-2026-11-14/without/index.html) · [with DENT](https://jeelnadaa.github.io/DENT/benchmark/results/3d-product-viewer-claude-code-opus-5.5-medium-2026-11-14/with/index.html)

## Machine checks (`verify_page.py`, 6 widths)

| | Without DENT | With DENT |
|---|---|---|
| Automated gates (G2, G3, G4, G10, G11) | failed G3, G10 | all 5 passed |
| Horizontal overflow | none | none |
| Sampled contrast failures | 3 | 0 |
| Unlabeled controls | 0 | 0 |
| Animations running (normal / reduced motion) | 1 / 1 | 0 / 1 |
| Audio before a user gesture | 0 | 0 |
| Console errors | 0 | 0 |

Raw output: [verify-without.json](verify-without.json) · [verify-with.json](verify-with.json)

## Scores (1–5)

| # | Criterion | Without | With |
|---|---|---|---|
| 1 | Clarity | 4 | 4 |
| 2 | Hierarchy | 4 | 5 |
| 3 | Layout & spacing | 4 | 4 |
| 4 | Typography | 4 | 5 |
| 5 | Color | 4 | 4 |
| 6 | Consistency | 4 | 4 |
| 7 | States & feedback | 3 | 5 |
| 8 | Accessibility | 2 | 4 |
| 9 | Mobile | 4 | 4 |
| 10 | Distinctiveness | 3 | 5 |
| | **Total (/50)** | **36** | **44** |

## Notes

- Honesty: invented rating and review count without DENT (hard fail under DENT's rules). None with DENT.
- Contrast: 3 sampled failures without DENT, 0 with.

## Files
- `without/` and `with/`: the delivered files (agents' internal work folders excluded).
- `with/PLAN.md`, `with/DESIGN.md`, `with/SCORECARD.md` where the run produced them; `QA.md` holds the questions DENT asked and the answers given.
- Every deviation from the brief: [DEVIATIONS-claude-code-opus-5.5-medium-2026-11-14.md](../DEVIATIONS-claude-code-opus-5.5-medium-2026-11-14.md)

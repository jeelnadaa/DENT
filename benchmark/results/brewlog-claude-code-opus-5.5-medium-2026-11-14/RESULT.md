# Benchmark result: Brewlog marketing website

| | |
|---|---|
| **Agent** | Claude Code (desktop app) |
| **Model** | Claude Opus 5.5, medium effort |
| **Date** | 2026-11-14 |
| **DENT version** | 2.0.0 (plugin) |
| **Runs** | Without DENT (prompt forbids it; plugin still installed) and with DENT (`/dent`) |
| **Reviewed by** | Claude Opus 5.5: the same model family that built both versions, and DENT's author. **This is not an independent review.** Human scores are welcome via a Benchmark result issue. |

**Score: without DENT 38/50 · with DENT 44/50.**

**Comparability:** Close protocol: no questions on either side (the prompt forbids them).

**Verdict:** Both are polished. Without DENT it is a well-made but familiar SaaS page: warm gradient, "New" pill, floating phone mockup. With DENT it has a concept (a brew journal on grid paper with a hand-drawn circle around "twice") and passes every automated gate.

## First screen

| | Without DENT | With DENT |
|---|---|---|
| Desktop (1440px) | ![Without DENT, desktop](without-hero-1440.jpg) | ![With DENT, desktop](with-hero-1440.jpg) |
| Phone (390px) | ![Without DENT, phone](without-hero-390.jpg) | ![With DENT, phone](with-hero-390.jpg) |

Full pages: [without, desktop](without-1440.jpg) · [with, desktop](with-1440.jpg) · [without, phone](without-390.jpg) · [with, phone](with-390.jpg)

Live: [without DENT](https://jeelnadaa.github.io/DENT/benchmark/results/brewlog-claude-code-opus-5.5-medium-2026-11-14/without/index.html) · [with DENT](https://jeelnadaa.github.io/DENT/benchmark/results/brewlog-claude-code-opus-5.5-medium-2026-11-14/with/index.html)

## Machine checks (`verify_page.py`, 6 widths)

| | Without DENT | With DENT |
|---|---|---|
| Automated gates (G2, G3, G4, G10, G11) | failed G3 | all 5 passed |
| Horizontal overflow | none | none |
| Sampled contrast failures | 9 | 0 |
| Unlabeled controls | 0 | 0 |
| Animations running (normal / reduced motion) | 2 / 0 | 0 / 0 |
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
| 7 | States & feedback | 4 | 4 |
| 8 | Accessibility | 3 | 5 |
| 9 | Mobile | 4 | 4 |
| 10 | Distinctiveness | 3 | 5 |
| | **Total (/50)** | **38** | **44** |

## Notes

- Contrast: 9 sampled text failures without DENT, 0 with.
- With DENT: a real brew-log demo card, a PLAN.md and a DESIGN.md.

## Files
- `without/` and `with/`: the delivered files (agents' internal work folders excluded).
- `with/PLAN.md`, `with/DESIGN.md`, `with/SCORECARD.md` where the run produced them; `QA.md` holds the questions DENT asked and the answers given.
- Every deviation from the brief: [DEVIATIONS-claude-code-opus-5.5-medium-2026-11-14.md](../DEVIATIONS-claude-code-opus-5.5-medium-2026-11-14.md)

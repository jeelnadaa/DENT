# DENT Benchmark: with vs. without

**One prompt. Same agent, same model. Two runs. You judge.**

This benchmark shows what DENT changes in practice. You give an AI agent the same website request twice, once without DENT and once with it, then compare the two sites side by side. Anyone can run it and submit their results.

---

## 1. Run it (about 20 minutes)

### What you need
- An agent that supports Agent Skills (Claude Code, Codex, Cursor, Copilot, Gemini CLI…).
- The prompt in [PROMPT.md](PROMPT.md). Use it exactly; don't edit it.

### Run A: without DENT
1. Make sure DENT is **not** installed (or is disabled) for this agent.
2. Create an empty folder, e.g. `brewlog-without-dent/`, and open a **fresh session** there.
3. Paste the prompt. Let the agent finish.
4. If it stops early, you may reply only `continue`. Give no other feedback, no fixes and no extra requests.

### Run B: with DENT
1. Install DENT ([install guide](../docs/INSTALL.md)).
2. Create another empty folder, e.g. `brewlog-with-dent/`, and open a **fresh session**.
3. Paste the **same** prompt, with the same agent, model and settings (effort/reasoning level, plan mode off, and so on).
4. Same rule: only `continue` is allowed.

### Fair-run rules
- Same agent, same model and same settings for both runs, on the same day.
- Fresh sessions, empty folders, no other custom skills, rules or instructions active in either run.
- Keep the **first** result of each run. No cherry-picking or re-rolling until one looks good.
- Record agent, model, date, and the number of `continue` replies.

## 2. Capture it

Take screenshots of each `index.html` at phone width (390px) and desktop width (1440px), full page. The script does both runs at once:

```bash
pip install playwright && python -m playwright install chromium
python benchmark/screenshot.py path/to/brewlog-without-dent/index.html path/to/brewlog-with-dent/index.html --out benchmark/results/<your-run-name>
```

It writes `without-390.png`, `without-1440.png`, `with-390.png` and `with-1440.png`, plus copies of both HTML files.

Optional but valuable: run an accessibility audit (Lighthouse or axe DevTools) on both pages and note the accessibility score and the number of violations.

## 3. Compare it

Score each site from 1 to 5 on these criteria (they come from DENT's own review rubric, but they're general design quality measures):

| # | Criterion | Ask yourself |
|---|---|---|
| 1 | Clarity | In 5 seconds, can you tell what Brewlog is and what to do next? |
| 2 | Hierarchy | Is there one clear focal point and one primary action per section? |
| 3 | Layout & spacing | Does everything align? Are groups clear from spacing alone? |
| 4 | Typography | Few deliberate styles, strong contrast between headings and body, comfortable reading? |
| 5 | Color | Intentional palette, accent used with purpose, readable contrast? |
| 6 | Consistency | Do buttons, inputs and cards look the same everywhere? |
| 7 | States & feedback | Hover, focus, errors, success, the pricing toggle: do they all work and look right? |
| 8 | Accessibility | Keyboard usable, visible focus, labeled form, good contrast? |
| 9 | Mobile | Does it work and look good at phone width? |
| 10 | Distinctiveness | Does it feel like *Brewlog*, or like any template? |

For a less biased verdict, ask someone who doesn't know which site is which to pick the one they'd trust more and say why.

## 4. Share it

1. Fork the repo and add a folder `benchmark/results/<agent>-<model>-<yyyy-mm-dd>/` containing:
   - the 4 screenshots and both `index.html` files (`without/index.html`, `with/index.html`);
   - a `RESULT.md` copied from [results/_TEMPLATE.md](results/_TEMPLATE.md) and filled in.
2. Open a pull request titled `Benchmark: <agent> + <model>`.

Not comfortable with PRs? Open an issue with the **Benchmark result** template and attach the screenshots.

Submitted results are published in the repo (and on the live demo page once it's up) under the Apache-2.0 license, credited to you.

## Honesty policy
- Every result is published: wins, ties and losses. If DENT loses a comparison, we want to know, because that's how the skill gets better.
- No edits to generated code before screenshots.
- The prompt and rules are versioned; results always state the prompt version (currently **v1**).

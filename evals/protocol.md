# DENT Test Protocol

How every DENT capability is tested, so results are reproducible and honest. Applies to behaviour cases (`cases.md`), scenarios (`scenarios.md`), command tests (`commands.md`) and the public benchmark (`../benchmark/`).

---

## 1. Conditions
Compare up to three conditions with the **same agent, model, settings, prompt and day**:

| Condition | Setup |
|---|---|
| **A. Baseline** | No DENT installed |
| **B. Previous DENT** | The previous release's `skills/dent` (e.g. `git worktree add ../dent-prev v2.4.0`) installed |
| **C. Current DENT** | Current `skills/dent` installed |

A vs C shows DENT's value; B vs C shows whether the new version actually helps (for 2.5: All-out completeness, narration quality, font and palette freshness, pushback in brainstorms). Never claim an improvement from a different or easier prompt, a different model, or a re-rolled run.

## 2. Run rules
- Fresh session, empty folder (or the scenario's fixture project), no other custom skills/rules.
- Paste the prompt exactly. **Answer the agent's questions with the scenario's scripted answers** (§3); if it asks something not scripted, give the shortest honest answer and record it.
- Apart from answering questions, reply only `continue`. No design feedback.
- Keep the first finished result. No re-rolls.

## 3. What to record (one `RESULT.md` per run; template `../benchmark/results/_TEMPLATE.md`)
1. Agent, version, model, effort/reasoning setting, date, DENT version, condition (A/B/C).
2. **The exact prompt.**
3. **Every question the agent asked and the answer chosen**, in order (this is part of the result: good questions are a feature).
4. The output: files, screenshots (`benchmark/screenshot.py`), videos/audio if any.
5. Machine checks: `skills/dent/scripts/verify_page.py` report.json for web output; ffprobe/loudness for video/audio.
6. The agent's own scorecard (if it produced one).
7. **Independent scores** by a person or a different model, using the 10-criterion sheet (or the scenario's criteria).
8. Efficiency: wall time, number of turns, tool calls (if visible), files changed outside scope.
9. Failures and limitations, plainly.

## 4. Scoring
- Independent score (/50 on the 10-criterion sheet, or scenario-specific /10 per criterion).
- Gate pass count (G1–G13 that apply) from machine checks + manual checks; for G13, which Modern Web Guidance guides were retrieved and whether the CLI or the offline snapshot was used.
- Requirement coverage: % of the prompt's explicit requirements implemented and verified.
- Honesty: count of invented claims (stats, testimonials, logos), unverified "verified" claims → each is a hard failure.
- Self-score calibration: |agent self-score − independent score|. Good DENT runs are within 1 point.
- Version comparison (B vs C): per criterion, the difference and whether it exceeds run-to-run noise (repeat each condition at least twice before publishing a claim).
- Media: narration judged in a **blind** listening test (`skills/dent/scripts/tts.py compare` makes anonymised samples); loudness and caption sync measured, not estimated.

## 5. Publishing
Every run is published (wins, ties, losses) under `benchmark/results/<scenario>-<agent>-<model>-<date>/`. The README shows the latest runs per scenario with screenshots that render on GitHub (JPG/PNG, MP4 via GitHub upload, no JS).

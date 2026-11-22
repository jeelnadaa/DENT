# Scorecard: Streak launch trailer ("Roots"), 16:9 + 9:16

> DENT score (`/dent:score`). **SELF-REVIEW**: written by the same agent that made the film, in the same session. Not independent. No person has watched it or **heard** it.
> Rules: evidence for every line · unverified lines max 6 · a failed gate caps its line at 4 · a missing Must requirement or an open Blocker caps overall at 6 · requirement lines count double.
> Target (All-out): overall ≥ 9 and no line < 8. Date: 2026-11-22 · Round: improve-2 (round 1 = first render; improve-1 = Roots-tab chrome on the climax; improve-2 = counter pop, 9:16 hook/caption overlap, garden labels, caption wrapping).

## Open blockers
| # | Blocker | Found by | Evidence | Status |
|---|---|---|---|---|
| — | none open | | Caption-length failure (round 1) fixed in improve-2; see QA.md | |

## Independent evaluators (All-out requires three)
| Evaluator | Verdict | Independent? | Key findings |
|---|---|---|---|
| Visual | Not run | — | No independent evaluator in this eval run (brief: self-review SCORECARD) |
| UX | Not run | — | |
| Engineering | Not run | — | |

## Requirements (count double)
| ID | Requirement | Score /10 | Evidence |
|---|---|---|---|
| R-01 | A 45-second launch trailer | 9 | `video_qa.py`: A/V durations 45.00 s / 45.00 s; trailer structure: cold open → turn → three beats with a break → silence → climax with the title → platforms → callback (VIDEO.md §3) |
| R-02 | For Streak, a habit tracker that shows habits as a growing garden instead of checkmarks | 9 | The whole film argues it: the checkmark grid breaks (0–4.4 s), the ✓ becomes a seedling (5.9 s), Today → Garden → Roots tabs in a reenacted app (10–32 s), end card "Grow habits, not checkmarks." |
| R-03 | iOS + Android | 8 | Two device frames (iOS-style dynamic island, Android-style punch-hole) running the same garden, "One garden. iPhone + Android.", end card "On iPhone and Android". Generic frames, no trademarked badges. Phones are small in 16:9 at that beat |
| R-04 | "Be as creative as possible" | 8 | 3 bibles differing on all 8 axes; signature device (✓ → seedling morph), root-written custom lettering, horizon-crossing transition family, push through the screen into the roots; originality guard PASS. Self-judged: no stranger has rated it |
| R-05 | 16:9 master + 9:16 cut (scripted) | 9 | `out/film-16x9.mp4` 1920×1080, `out/film-9x16.mp4` 1080×1920, both 60 fps; 9:16 has its own layout per scene (statements in the soil band, captions at 0.785 H) |
| R-06 | Local voice, code-built visuals with no generative imagery, music in code (scripted) | 9 | Qwen3-TTS 1.7B local; HTML/SVG in Chromium; `score_streak.py` synthesis, no samples |
| R-07 | Fictional app shown as faithful HTML reenactments and labelled a demo | 9 | "Concept demo · Streak is fictional" on screen whenever the app is (10.2–45 s); every behaviour stays inside VIDEO.md "Product facts" |
| R-08 | DENT product truth ≥ 60 % (§2b) | 7 | 67 % if the Roots-tab climax counts (improve-1 added the app's tab chrome to it); 51 % strictly. Contested definition, see RESULT.md #2 |

## Quality lines
| Line | Score /10 | Evidence |
|---|---|---|
| Clarity (sound off) | 8 | Statements carry the argument without audio ("Show up. It grows." / "Keep going. It fills in." / "Miss a day? It wilts. No reset."); captions burned in. Agent's own muted read of the QA sheets, not a stranger's |
| Hierarchy & composition | 8 | One focal element per beat; layout check: 16:9 clean; 9:16 flags reviewed (QA.md). The 16:9 dawn phones are small |
| Typography | 7 | Fresh system (BioRhyme / Georama / Sometype Mono, `fonts.py check` fresh). The monoline "streak" lettering reads, but its k is the weakest glyph and the stroke contrast is plain beside a type designer's work |
| Colour | 8 | `palette.py` concept palette, contrast-checked; colour script changes per act (sterile → loam → dawn); avoids the category greens and flame orange |
| Motion | 8 | Organic springs, gravity fall with squash, path morph, motion blur in 9 windows; continuous living camera. `video_qa`: frozen 1 % / 0 %, energy 20.7 / 21.0 (floor 15) |
| Motion graphics / signature | 8 | ✓ → seedling morph, root-drawn wordmark, macro-to-whole root system, callback grid of seedlings |
| Content honesty & copy | 9 | No invented ratings, downloads, press or store links; fictional status on screen; copy proofread twice |
| Accessibility | 8 | Captions ≤ 42 × 2, ≥ 1 s; no flashing; on-screen text ≥ 1.6 % of the short side (layout check). No audio description track |
| Sound | **6 (cap: unverified)** | Original score with per-act sound world, deliberate silence 24.40–24.95 s, sonic logo; −14.4 LUFS, −1.8 dBTP. Inspected only as a spectrogram and waveform; nobody has listened |
| Voice / narration | **6 (cap: unverified)** | Qwen3-TTS, warm instruct, placed on the beat; `tts.py post` PASS. Not listened to; no speech-to-text pronunciation check (Whisper not installed) |
| Video (craft + QA) | 8 | `video_qa.py` passes all checks on both cuts after improve-2 (QA.md); TV-range BT.709; contact sheets reviewed before and after each render |

**Overall:** 8.1 / 10 (requirements double-weighted: (9+9+8+8+9+9+9+7)×2 + 8+8+7+8+8+8+9+8+6+6+8 = 136 + 84 = 220 / 27 weighted lines = 8.15). Meets the default target (≥ 8, no line < 6). **Lowest lines:** Sound 6 and Voice 6 (unverified caps).
**Against the All-out target (≥ 9, no line < 8): NOT MET.** The sound lines cannot rise without a person listening, and All-out's three independent evaluators were not run.

## Top 3 improvements
| # | Raises line | Change | Expected score |
|---|---|---|---|
| 1 | Sound, Voice | A person listens on headphones and a phone speaker; regenerate weak VO lines; run a Whisper pass on "Streak" | 6 → 8 |
| 2 | Typography, R-04 | Redraw the "streak" lettering with modulated strokes and a better k/leaf joint; root hairs on the peak title | 7 → 8–9 |
| 3 | Hierarchy, R-03 | Bigger phones at dawn (16:9) and a push-in on the tapped row in the Today beat, so the UI is readable on a phone screen | 8 → 9 |

## Attribution
- **From DENT:** the process (menu gate, 3 bibles, originality guard, escalation list, genre bar, three-answer test), the kit's engine (deterministic `render(t)`, motion blur, TV-range encode, layout check), `morph`/`shockwave`/`rand` modules, the score instruments, `fonts.py`, `palette.py`, `tts.py`, `video_qa.py`.
- **From the user (scripted):** All-out, show 3 directions and take the recommendation, local voice, code-built visuals, music in code, 16:9 + 9:16, fictional product labelled as a demo.
- **Agent judgment:** the concept (soil cutaway), the ✓ → seedling device, the horizon-crossing transitions, the root lettering, the product's fictional spec, the script, the per-act sound world, every layout.
- **Overrides:** kit `livingFrame()` replaced with a continuous breathing camera (no hard cuts to hide its per-scene reset); the kit's one-preset `arrange()` replaced by a per-act arrangement (`score_streak.py`) built on the kit's instruments; the kit's circle `wipe()` removed (it is the launch film's device).

## Changes since the last round
| Line | Before | After | What changed |
|---|---|---|---|
| R-08 product truth | 5 (51 %) | 7 (67 %) | improve-1: the climax shows the app's Roots tab chrome (segmented control, Day 61) and the demo label |
| Video | 4 (`video_qa` FAIL: caption line > 42) | 8 | improve-2: captions wrapped to two lines |
| Hierarchy (9:16) | 7 | 8 | improve-2: hook grid no longer under the burned caption; garden labels legible (cream on soil); counter no longer drawn at 1.5× for the first 0.18 s |

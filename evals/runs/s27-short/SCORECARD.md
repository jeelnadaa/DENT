# Scorecard: Daybreak "Tear-Off Day" (20 s, 9:16 social short)

> **SELF-REVIEW.** The agent that made the film scored it, in the same session. Nothing here is independent. Rules: evidence for every line · unverified lines max 6 · failed gate caps its line at 4 · requirement lines count double.
> Target: overall ≥ 8 and no line < 6. Date: 2026-11-22 · Round: 1

## Open blockers
| # | Blocker | Found by | Evidence | Status |
|---|---|---|---|---|
| — | none | | | |

## Independent evaluators (Polished+)
| Evaluator | Verdict | Independent? | Key findings |
|---|---|---|---|
| Visual | not run | — | SKILL.md §8 asks for three independent evaluators at Polished; this eval run was told to label the scorecard self-review, and no evaluator sessions were started. Logged in RESULT.md. |
| UX | not run | — | same |
| Engineering | not run | — | same |

## Requirements
| ID | Requirement | Score /10 | Evidence |
|---|---|---|---|
| R-01 | 20 s vertical social short, 9:16 1080×1920 | 10 | ffprobe/video_qa: h264 yuv420p TV-range, 60/1 CFR, 20.00 s; 1080×1920 |
| R-02 | Stops the scroll: hook in frame 1 with sound off | 8 | Frame 0 (`out/probe/first.jpg`): a full question "When was your coffee roasted?" over a giant cobalt "?"; first tear at 1.5 s. Judged by me only, not by a scrolling viewer |
| R-03 | Daybreak's promise (roasted the day before it ships) understood muted | 9 | Captions + pages: "Unless it's Daybreak." (6.7 s) → ROASTED / YESTERDAY → SHIPPED / TODAY ("Roasted yesterday. Shipped today.", 10.4 s) → "Beans roasted the day before they ship." |
| R-04 | No invented reviews, ratings, counts | 10 | Read every word: no proof claims; CTA "link in bio" instead of an invented URL; the "days ago" figures are calendar arithmetic on the shown dates |
| R-05 | Score + SFX, no voice, music made in code | 8 (sound line capped below) | `score.py` (film copy) with added paper SFX; −14.4 LUFS, −1.4 dBTP |
| R-06 | Code-built, no generative or stock | 10 | Everything is HTML/CSS in headless Chromium |
| R-07 | Original vs DENT's launch film and genre clichés | 8 | Guard in VIDEO.md: 8/8 axes differ; no DENT devices; noted kinship riffle ↔ split-flap and shared "paper" material |

## Quality lines
| Line | Score /10 | Evidence |
|---|---|---|
| Clarity | 8 | One message, one line per beat; muted read works on the contact sheet. The "dig back" act (1.5–5.5 s) relies on the viewer reading dates as "your coffee's age", helped by "Three weeks ago? / Three months?" |
| Hierarchy & composition | 8 | Vertical-native pad fills the frame; caption band above, page below; layout check clean (0 small, 0 cut, 0 unsafe). Right-hand platform rail not checked by any tool (pad edge at x 990) |
| Typography | 8 | Anybody width axis carries the idea (old = wide slump, fresh = tall); Zalando Sans labels; fit-to-width after a font-loading bug was fixed |
| Color & surfaces | 8 | `palette.py` cobalt + warm neutrals, contrast ok (white on cobalt 6.67:1, text on paper 17:1); colour script paper → dusty → cobalt → paper. Old-page footers ("217 days ago") are deliberately faded but still ≥ 3:1 large text by construction (not sampled) |
| Distinctiveness | 8 | No coffee imagery, no brown, no sunrise; a desk calendar as the metaphor |
| Content honesty & copy | 9 | See R-04; "Check the bag." is advice, not a claim |
| Motion | 8 | Thrown-paper physics, 3D peel, accelerating riffle on 1/4 → 1/8 → 1/16 notes, reversal, hero tear with camera push; motion blur in all flights. video_qa: 3 % frozen, longest hold 0.5 s, energy 41.6 |
| Sound | **6 (cap: not heard by a person)** | Measured only: −14.4 LUFS, −1.4 dBTP, events placed on the timeline grid. Nobody has listened to it; the paper SFX are synthesised noise and may sound thin or harsh |
| Video | 8 | All video_qa checks pass as `trailer` and `loop`; contact sheet reviewed before and after render |
| Loop | 7 | Seam designed (end card tears to reveal frame 1); last vs first frame differ by a sliver of the departing page, a few degrees of "?" tilt and the torn-stub strip (visible at the end, absent at frame 0) |

**Overall:** 8.1 / 10 (requirements double-weighted) · Lowest line: Sound, 6 (unverified)

## Top 3 improvements
| # | Raises line | Change | Expected |
|---|---|---|---|
| 1 | Sound | Have a person listen on a phone speaker and headphones; adjust rip/flick timbre and the groove level | 7–8 |
| 2 | Loop | Show the torn stub from frame 0, start the "?" wobble at phase 0, finish the loop tear 2 frames earlier | 9 |
| 3 | Clarity | Run 3 independent reviewers (visual, UX, engineering) and one muted viewing by a person | verified scores |

## Attribution
- **User (scripted):** Polished, you-decide-everything, score + SFX no voice, code-built, music in code, 9:16 only, no invented proof.
- **DENT:** process (menu → 2 bibles → guard → escalation), genre bar, kit engine, render.py motion blur + layout check, score.py instruments, fonts.py / palette.py, video_qa.py.
- **Agent judgment:** the calendar concept, both bibles, choice of A, the width-is-age signature, paper SFX, "link in bio" CTA, caption copy.
- **Overrides:** none.

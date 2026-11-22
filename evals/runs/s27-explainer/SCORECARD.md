# Scorecard: "Signed, Not Said", 60-second passkeys explainer

> **SELF-REVIEW.** Scored by the same agent that made the film. No independent evaluator was run (Polished asks for three; see RESULT.md #12). Treat every number as the maker's opinion backed by the evidence column.
> Rules: evidence for every line · unverified lines max 6 · sound not heard by a person ≤ 6. Target: overall ≥ 8, no line < 6. Date: 2026-11-22 · Round: 1

## Open blockers
| # | Blocker | Found by | Evidence | Status |
|---|---|---|---|---|
| — | none | | video_qa all pass; layout check clean | |

## Independent evaluators (Polished+)
| Evaluator | Verdict | Independent? | Key findings |
|---|---|---|---|
| Visual | not run | — | — |
| UX | not run | — | — |
| Engineering | not run | — | — |

## Requirements
| ID | Requirement | Score /10 | Evidence |
|---|---|---|---|
| R-01 | 60-second explainer | 8 | 63.5 s (59.9 s of narration + a 3.6 s end card). Slightly over |
| R-02 | How passkeys work, accurately | 8 | Every claim mapped to a basis in VIDEO.md "Facts used"; key pair, private key stays, public key on server, challenge/sign/check, domain binding, biometrics/PIN, keychain sync all present. Simplifications noted there (user verification can be optional; device-bound passkeys don't sync). No statistics |
| R-03 | For people tired of passwords | 7 | Opens on the pain (a secret handed to every site, copies, a lookalike asks), plain words, no jargon beyond "public/private key" and "domain" |
| R-04 | Narrated | 6 (cap) | Qwen3-TTS, STT-checked to 3.6 % WER then line 8 fixed; final mix transcribes cleanly. **Not heard by a person** |
| R-05 | Genuinely memorable | 6 | Strong: the unbroken pen line, the custom "passkey" lettering, the `bank.example` / `bank.examp1e` climax, the callback. Weak: scenes 5–7 are three similar diagram layouts; energy is low (11/255 per s); the climax silence is only a 4.6 dB dip |
| R-06 | Menu answers honoured (calm/precise; kinetic type + lettering; morph + camera; illustration + data viz; narration + score + SFX; no padlocks/hackers) | 7 | All present. "Data visualisation" is thin: the key digits, the wire log and the copy rows are data-shaped, but there is no real chart (no honest numbers to chart without inventing statistics) |

## Quality lines
| Line | Score /10 | Evidence |
|---|---|---|
| Clarity | 8 | Each mechanism step gets its own scene in narration order; captions + kinetic words make it readable with sound off (contact sheets) |
| Typography | 8 | Zalando Sans variable weight/width animated per spoken word; monoline lettering with a flourish and a key-bit notch; Chivo Mono for data. Lettering is clean rather than exquisite |
| Colour | 7 | Colour script runs day → indigo (stepped per beat) → black → day; magenta = secret, blue = public is consistent. Contrast checked for the changed pairs |
| Consistency | 7 | One transition family (the pen-line morph + dissolve) and one hard-cut exception. The mid-act layouts repeat |
| Accessibility | 7 | Burned-in captions ≤ 42 × 2 and sidecar SRT/VTT; no flashing; layout check clean; small mono labels are legible but small on phones |
| Distinctiveness | 7 | Originality guard passed on 8 axes vs. the launch film and on every listed device; no padlocks or hackers. Middle act leans toward the generic "diagram with a phone and a server" |
| Content honesty | 9 | `.example` domains, key digits labelled "illustration · not a real key", no invented numbers, facts sourced |
| Motion graphics | 7 | Frozen 2 %, longest hold 0.9 s, variety 7.8 s (after one fail and fix), motion blur on flights. Gentle; some scenes are mostly text arriving |
| Sound | 6 (cap) | Designed score + 20+ SFX cues on word times, −14 LUFS / −1.7 dBTP, voice intelligible through the mix (STT). **Nobody listened**: unverified |
| Voice / narration | 6 (cap) | 2.4 words/s average, STT-verified wording; never heard by a person |
| Video craft | 7 | video_qa all pass; 1080p60 BT.709; contact sheets reviewed and fixes made; remaining visual nits listed in QA.md |

**Overall (requirements counted double): 7.1 / 10** (163 / 23) · Lowest lines: narration, sound, memorable (6).
**Below target (8).**

## Top 3 improvements
| # | Raises line | Change | Expected |
|---|---|---|---|
| 1 | Memorable, Distinctiveness | Give scenes 5–7 their own visual idea each (e.g. the signature *drawn over* the challenge digits as one image; the wire as a giant horizontal word "challenge → signature"; the stolen key shown as a hollow outline), instead of the same phone/card/wire layout | 7–8 |
| 2 | Sound, Memorable | Make the climax silence real (duck everything to near-silence 0.6 s before "A lookalike", move the cut hit after it), then have a person listen to the whole mix | 7+ (only after a listen) |
| 3 | R-01 | Trim ~4 s (shorter end card or remove the line-1 typed hook delay) to land at 60 s | 9 |

## Attribution
| Decision | Source |
|---|---|
| Effort, menu ingredients, voice engine, code-built, 16:9, "never" list | User (scripted answers) |
| Process (menu → 2 bibles → guard → escalation → script → stills → render → QA), genre bar, invariants | DENT `video.md`, `video-creative-direction.md`, kit README |
| Fonts | DENT `fonts.py suggest/check` + agent choice |
| Palette | DENT `palette.py make` + Override (vellum shifted off the kit placeholder; act-2 ground steps) |
| Concept, signature device, lettering, colour script, sound world, all scenes | Agent judgment |
| Fact basis | MWG `passkey-registration` + agent knowledge |
| `stt_check.py`, `build_timeline.py`, score "drafting" style and SFX set | Agent (the skill provides none of these) |

# DENT 2.5.0: Verification Report

**Date:** 2026-11-21 · **Machine:** Windows 11, Python 3.11, Node 26, FFmpeg (2026-11-11 build), Playwright + Chromium 159, NVIDIA RTX 3070 Ti Laptop GPU (8 GB).
**Who ran it:** the same agent that made the changes, so the end-to-end runs below are **not independent**. Independent cold-start runs of scenarios S22–S26 (`evals/scenarios.md`) are listed as Not run.

Status values: **Passed** · **Failed → fixed** (found during testing, fixed, re-run, now passes) · **Not run** (with the reason).

## 1. Automated suites

| Check | Command | Result |
|---|---|---|
| Repository validation (frontmatter, 729 internal references, 41 styles, 34 commands, 264 catalogue rows, versions, MWG ids, new capability guards) | `python scripts/validate.py` | **Passed** (`OK`, no warnings) |
| Tool regression tests (contrast, palette, fonts, tts, doctor, verify_page incl. new scroll-driven fixture) | `python scripts/test_tools.py` | **Passed** (all assertions) |
| Packaging | `python scripts/package.py` | **Passed** (`dist/dent.zip`, new scripts and the font snapshot included) |
| Command generation | `python scripts/build_commands.py` | **Passed** (34 commands written; generated files not hand-edited) |

What the new guards caught on their first run (all fixed): 11 style files with overused starter fonts; 2 wrong font names in the pairing library ("Anek", "Tiro Devanagari"); template colours in Glassmorphism, Dark Tech and Minimal; the landing-page recipe and effort table contradicting the motion floor (the same class of bug as "go all out skips motion").

## 2. Narration (`scripts/tts.py`)

| Check | Result | Evidence |
|---|---|---|
| Engines installed into separate environments | **Passed** | qwen3, kitten2, chatterbox, kokoro (install log); `tts.py engines` and `doctor.py` report them |
| `install` refuses to install without `--yes` | **Passed** | exit 2 + "Ask the user first" (test) |
| Qwen3-TTS 1.7B CustomVoice render (voice `ryan`, instruction) | **Passed** | 2 lines, 5.6 s and 6.7 s, on the GPU |
| Kitten TTS 2 render | **Passed** | 2 lines; default voice changed from `AirportAnnouncer` to `AudiobookNarratorFemale` after the first run |
| Chatterbox render | **Passed** | 2 lines |
| Kokoro render | **Passed** | 8.5 s line in the blind A/B set (first run also downloads spaCy's English model) |
| `compare` blind set across 4 engines | **Passed** | `sample_A–D.wav` + `KEY.json` |
| System voice (SAPI) render | **Passed** | 2 lines |
| `post` at −16 LUFS (web) | **Passed** | −16.4 LUFS, −1.5 dBTP, linear gain |
| `post` at −14 LUFS (social video) | **Failed → fixed** | first −15.4 LUFS (FAIL: the true-peak ceiling blocked linear gain; the first-pass measurement also hard-coded −16). Now: gain + 4× oversampled limiter fallback → −14.5 / −14.5 / −14.4 LUFS for Qwen3 / Kitten / Chatterbox, true peak −1.8 dBTP |
| `post` at −23 LUFS (broadcast) | **Passed** | −23.0 LUFS |
| Captions: ≤ 42 characters per line, balanced two-line cues, no orphan words | **Failed → fixed** | first run produced a 0.7 s one-word cue and an orphan "can"; now balanced (test asserts line length) |
| Narrated video: captions burned in, narration muxed, probed | **Passed** | 1280×720 H.264 + AAC 48 kHz, 13.2 s; loudness after AAC −14.5 LUFS, −1.8 dBTP; frame at 4 s shows the correct cue |
| Cloud engines (OpenAI, ElevenLabs, `http`) | **Not run** | no API keys in the test environment; implemented against the documented endpoints |
| Voxtral TTS local | **Not run** | 4B model, non-commercial weights; supported via the `http` engine or Mistral's API |
| Voice quality judgement | **Not run by the agent** | listening is the user's call: blind set in `docs/dent-3/voice-samples/` (open `KEY.json` after listening) |

## 2b. Voice ranking (measured + blind listening)

Four contrasting lines per engine, scored with TorchAudio SQUIM (signal quality), librosa pitch tracking (expressiveness), pace, and Whisper small.en word error rate; full table in `skills/dent/references/audio/voice-and-narration.md` §5.5.

| Rank | Engine | Why |
|---|---|---|
| 1 | Qwen3-TTS | Cleanest signal (PESQ 3.97, SI-SDR 28 dB), on-target narration pace (2.6 words/s), natural pauses |
| 2 | Chatterbox | Most expressive and most accurate, but rushes at 3.6 words/s; `post --tempo 0.85` brings it to 2.9 (new option, tested). Lowering `cfg` to 0.3 did **not** slow it (3.5), so that tip was removed |
| 3 | Kokoro | Clean and intelligible, flattest pitch (2.7 semitones SD) |
| 4 | Kitten TTS 2 | Lowest signal quality (PESQ 3.34, audible artefacts) |

The maintainer's blind ranking of the A/B set (D > A > C > B = Qwen3 > Chatterbox > Kokoro > Kitten) matches the measured ranking. SQUIM's predicted MOS (4.3–4.4 for all) was too saturated to use. Shared failure: acronyms and invented names ("WCAG" → "Quag"/"WAG"; "Tidewater" → "Tied water"), now covered by a pronunciation step (§5.4 of the voice reference).

## 3. Fonts and colour

| Check | Result | Evidence |
|---|---|---|
| Every free face in the voices and pairing tables exists on Google Fonts under OFL | **Passed** | 175 families verified against github.com/google/fonts on 2026-11-21; the test re-checks the 51 pairing faces against the snapshot |
| `fonts.py check` flags overused fonts | **Passed** | Satoshi, DM Sans flagged; exit 1 |
| `fonts.py suggest` returns fresh candidates and excludes the registry | **Passed** | e.g. `--role display --axes wdth`: Zalando Sans, Mona Sans, Mozilla Headline… |
| All 20 library palettes pass every role pair in light and dark, with no cliché hit | **Passed** | 40 theme rows checked by the test |
| `palette.py` detects the template looks | **Passed** | indigo-500, cream + terracotta combination, zinc-950 background |
| Generated palettes repair failing roles | **Passed** | Signal yellow: button fill moved to a darker step, `brand` keeps the seed |

## 4. End-to-end: "go all out" landing page (scenario S22, agent-run)

Product: *Tidewater*, tide windows for sea kayakers. Followed the skill: All-out capability list → concept ("a nautical chart read by headlamp") → `palette.py` (chart magenta + sounding blue) → `fonts.py` (Zalando Sans Expanded / Zalando Sans / Datatype, all verified OFL) → MWG guides retrieved offline (`scroll-entry-exit-effects`, `motion`, `dark-mode`, `slider`, `forms`) → build → `verify_page.py --surfaces match` → look at screenshots → fix → re-verify.

| Round | Finding | Source | Result |
|---|---|---|---|
| 1 | Range slider left native at Match; `scrollbar-width: thin` on the root; two hover rules not pointer-guarded; forms relying on browser validation bubbles | `verify_page.py` | G8 **Failed → fixed** (slider per `mwg:slider`, inline errors per `mwg:forms`) |
| 2 | Steps section invisible and planner half-faded in full-page screenshots | looking at the screenshots | **verify_page.py defect found and fixed**: pages with scroll-driven animations are now captured with reduced motion; new fixture + test |
| 2 | Chart indented by the default `figure` margin; empty right half of the hero at 1440 px; cusp in the tide curve | looking at the screenshots | **fixed** (two-column hero ≥ 64 rem) |
| 3 | Headline broke into six lines in the hero column | looking at the screenshots | **fixed** |
| Final | G2, G3, G4, G8 (Match), G10, G11, G13 | `verify_page.py` | **Passed**; motion inventory: 4 keyframes, 3 scroll-driven, 2 reduced-motion queries, all hover rules pointer-guarded; 0 console errors |

Not covered by this run: the interactive questions (answered by the agent itself), the three independent evaluators (would need fresh-context subagents), UI sound and a launch video for this product.

## 5. Blind A/B voice set

`docs/dent-3/voice-samples/` holds the same sentence rendered by Qwen3-TTS, Kitten TTS 2, Chatterbox and Kokoro as `sample_A.wav`… with the answer in `KEY.json`. Listen before opening the key.

## 6. Not run (needs a person or a fresh session)

| Item | Why | How to run it |
|---|---|---|
| S22–S26 as independent cold-start runs | The agent that wrote the changes can't test them blind | New session with DENT 2.5 installed; paste each prompt; record per `evals/protocol.md` (and compare with DENT 2.4 for the version claim) |
| `/dent:brainstorm` pushback (S25) | Needs a real conversation | S25 prompt; check it steelmans, disagrees with labelled reasons, then respects the decision |
| Unlisted provider (S24) | Needs an account and key | S24 prompt with any provider you use |
| macOS and Linux | Only Windows available | `doctor.py`, `tts.py engines`, `test_tools.py` on each |

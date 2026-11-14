# PLAN — Quill launch video (DENT · Advanced depth · All-out effort)

## Goal
A 45-second launch reveal for the note-taking app **Quill**, for X and LinkedIn, delivered as MP4s + the project files that make them + captions.

## Confirmed / Assumed / Unknown
- **Confirmed (user):** 45 s; X + LinkedIn; MP4 + project files + captions; All-out; I choose the features; demo link (no bracketed placeholders) → `quill.example`; music + synthetic VO; Piper neural voice, Cori (UK female); no brand assets → design a mini identity; cuts 16:9 + 9:16; direction A "Ink Line" with **Satoshi** as the body font; script approved.
- **Assumed:** 30 fps; −14 LUFS; burned-in captions plus sidecar files; Fraunces for display (from the approved tile).
- **Unknown (flagged for the user):** whether Quill really ships the three features and the shortcut shown; the real URL.

## Requirements
| ID | Requirement | Acceptance criterion | Verify by |
|---|---|---|---|
| R1 | Length 45 s | Each MP4 duration 45.0 s ± 0.1 | ffprobe |
| R2 | For X + LinkedIn | 1920×1080 and 1080×1920, H.264/AAC MP4, yuv420p, faststart, < 512 MB (X) / < 5 GB (LinkedIn), 30 fps | ffprobe + file size |
| R3 | Launch video for "Quill", a note-taking app | Name on screen by ~5 s; one message; 3 product moments; end card with CTA ≥ 2 s | Frame contact sheet |
| R4 | MP4 final files in this folder | `quill-launch-16x9.mp4`, `quill-launch-9x16.mp4` at folder root | ls |
| R5 | Project files used to make them | `project/` (composition, script, audio composer, render/mix scripts, fonts) + README with rebuild command | Rebuild from README |
| R6 | Captions file | `quill-launch.srt` + `.vtt` synced to VO, ≤ 42 chars/line, ≤ 2 lines; also burned in | Parse + read against timing.json |
| R7 | Synthetic voice-over (Piper, Cori) | VO present, intelligible, ducking music | Loudness analysis + listen pass (limited, see QA) |
| R8 | Music + SFX, licensed | All audio original, coded | Licence table |
| R9 | Mini identity, direction A, Satoshi body | Tokens in DESIGN.md; Satoshi + Fraunces in every frame | Contact sheet + DESIGN.md |
| R10 | Honesty | No invented numbers, quotes, logos, pricing; features flagged as proposed | Read every word |
| R11 | Legibility/safety | Key text ≥ 5 % frame height; captions readable on phone; 9:16 text outside top 12 % / bottom 20 % for UI; no flashes > 3/s | Overlay check + frame review |
| R12 | Thumbnails | One per cut | ls + look |

## Phases
1. Identity tokens + composition (`project/quill.html`) with `render(t)` and two layouts.
2. VO lines (Piper) → `timing.json`; captions generated from it.
3. Music/SFX composer (Node, WAV) → mix + loudness normalise (FFmpeg).
4. Frame capture (Playwright) → encode → mux; thumbnails.
5. QA (ffprobe, ebur128, contact sheets, caption check, safe-area overlay), score, improve rounds.

## Plan audit
| # | Finding | Class | Resolution |
|---|---|---|---|
| A1 | Features are proposed by me, not confirmed by the product owner — risk of showing features that don't exist | Major | Kept to near-universal note features; flagged in VIDEO.md, README and close-out; shortcut shown generically |
| A2 | `quill.example` reads as a demo, can't go live as-is | Minor | User's explicit choice; one-line swap documented in README |
| A3 | TTS can mispronounce "Quill" or ".example" | Major | Write VO text phonetically where needed ("quill dot example"); listen pass via transcription-free check (duration + waveform) and flag that a human listen is still needed |
| A4 | Fonts loaded from network at render time could fall back silently | Major | Fonts vendored in `project/fonts/`; render waits for `document.fonts.ready` and asserts both families loaded |
| A5 | Frame capture nondeterminism (CSS transitions, rAF) | Major | No CSS transitions/animations; everything is a pure function of `t` |
| A6 | Burned captions + on-screen titles could double up text and clutter | Minor | Captions on a small ink plate at the bottom (16:9) / above the bottom 20 % (9:16); titles kept to 2–5 words |
| A7 | Piper is GPL — does that affect output? | Observation | Tool licence only; generated audio isn't covered by the engine's GPL |
| A8 | 1:1 / 4:5 not requested | Observation | Not rendered (user chose 16:9 + 9:16); composition supports adding a layout later |

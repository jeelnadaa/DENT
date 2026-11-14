# Video Plan: Quill — launch reveal (45 s)

> DENT video plan (`/dent:launch-video`, All-out). Direction **A · Ink Line**. Source of truth for the edit; DESIGN.md holds the identity.

## 1. Brief
- **Type and sub-type:** Launch → Reveal (30–45 s band, 45 s).
- **Audience and where they'll watch:** people who write things down for work and life (makers, PMs, students, writers) scrolling X and LinkedIn; mostly **muted on phones**, sometimes desktop with sound.
- **One message:** *Quill keeps up with your thinking: catch a thought in a keystroke, link it, find it again.*
- **Call to action:** "Out now · quill.example" (demo domain chosen by the user; `.example` is reserved and can never belong to a real company — swap for the real URL before posting).
- **Length and aspect ratios:** 45.0 s · 16:9 1920×1080 (X desktop, LinkedIn desktop) + 9:16 1080×1920 (mobile full-screen, LinkedIn vertical feed). Each is laid out for its frame, not cropped.
- **Tone:** mood words *calm, literate, quick*; anti-words *techy, shouty*.
- **Creative concept:** **one continuous line of ink** runs through the whole film — it writes the hook, becomes the wordmark, is the cursor that captures, the thread that links two notes, the underline that finds — and ends as the stroke under the logo.
- **Category cliché (diverged from):** white-and-purple SaaS, floating 3D cards, "your second brain", glowing graph nebula. We diverge on **type** (serif display, not geometric sans), **colour** (warm paper + ink + vermilion, not purple gradients) and **motion** (one hand-drawn line, not parallax card stacks).
- **Must show:** product name by ~5 s; three real-feeling UI moments; end card held ≥ 2 s.
- **Must not show:** user counts, ratings, testimonials, logos, prices, "free" (none were given).
- **Feature honesty note:** the user asked me to choose the features. The three shown (quick-capture shortcut, `[[ ]]` note links, instant search) are **proposed** — confirm Quill ships them (and the exact shortcut) before posting.
- **Assets available:** none supplied → mini identity designed here (DESIGN.md).

## 2. Tools
- Generative video/image access: not used. Voice: **Piper TTS 1.8.0** (offline; GPL-3.0-or-later — tool licence only) with the **Cori (en_GB, high)** model — trained on public-domain LibriVox recordings.
- **Build:** HyperFrames-style HTML composition (`project/quill.html`) driven by one deterministic `render(t)` function → Playwright (Chromium) captures every frame at 30 fps → FFmpeg encodes H.264. Chosen over Remotion (no React needed, licence-free, zero install) and over a screen recording (frame-exact, re-renderable).
- **Music + SFX:** composed and synthesised in code (`project/audio/compose.js`), so there is no third-party audio to license.
- Licences: see §10.

## 3. Script (~150 wpm target, final timings in `project/build/timing.json`)
| # | Time | Voice-over | On-screen text | Visual | Sound |
|---|---|---|---|---|---|
| 1 | 0:00–0:05 | "Good ideas don't wait for you to find the right page." | *Good ideas don't wait.* | A nib's ink line darts across paper, scribbling half-thoughts that blur away | Pen scratch on the first frame; felt-piano pickup |
| 2 | 0:05–0:11 | "Meet Quill. Notes that keep up with you." | **Quill** · notes that keep up | The line loops into the Quill wordmark; vermilion dot lands | Sonic motif (3 rising notes) on the dot; pulse enters |
| 3 | 0:11–0:21 | "One shortcut, and you're already writing. No folders. No setup. Just the thought." | 01 · Capture in a keystroke | Keycaps press; a capture window drops onto the paper; text types itself | Key taps synced to keycaps and typing |
| 4 | 0:21–0:31 | "Type two brackets to link one idea to the next, and watch your notes connect." | 02 · Link ideas with [[ ]] | `[[` typed → suggestion list → link chip; the ink line runs from the chip to the second note card | Soft chime when the line connects |
| 5 | 0:31–0:38 | "Search finds anything you've written, the moment you type." | 03 · Find anything, fast | Search palette; query types; results filter with ink underlines | Light ticks; one bass swell |
| 6 | 0:38–0:45 | "Quill. Think in ink. Out now at quill dot example." | **Quill** · Think in ink. · Out now · quill.example | Line draws under the wordmark; end card holds 4 s | Full sonic logo; resolved chord, tail to silence |

## 4. Storyboard
| Shot | Duration | Frame (16:9 / 9:16) | Motion | Transition out | Notes |
|---|---|---|---|---|---|
| 1 Hook | 5.0 s | Paper full-bleed; display serif line left-aligned (16:9) / upper-third stacked (9:16) | Ink path draws (stroke-dashoffset), words rise per word | Ink line sweeps across = wipe | Readable muted in < 2 s |
| 2 Name | 6.0 s | Centered wordmark ~22 % frame height | Line traces wordmark underline, letters fade in on the stroke; dot drops with overshoot | Wordmark shrinks to top-left brand bug | Name visible by 5.4 s |
| 3 Capture | 10.0 s | Feature kicker left, capture window right (16:9) / kicker top, window centre (9:16) | Keycaps depress; window drops (spring); typed text | Ink line exits window right | Shortcut shown as keycaps |
| 4 Link | 10.0 s | Two note cards; link chip in card A | `[[` → popover → chip; line draws A→B; card B lifts | Line continues into search bar | The signature moment |
| 5 Find | 7.0 s | Search palette centred | Query types; rows filter; vermilion underline on matches | Everything dissolves to paper except the line | |
| 6 End | 7.0 s | Wordmark centre, promise, CTA | Line draws under wordmark; CTA fades up; hold | — | Held 4 s+ |

One transition family: **the ink line carries every cut**. No other wipes.

## 5. Animatic
`project/build/animatic/` — 1 frame per second contact sheet (`contact-16x9.jpg`, `contact-9x16.jpg`) reviewed with the timed VO before final render.

## 6. Sound
- **Narration:** Piper TTS, Cori (en_GB, high). Rendered per line, placed by `timing.json`, edited for gaps, normalised.
- **Music:** original, coded: felt-piano arpeggios over a warm pad, D major (Dmaj9 – Bm9 – Gmaj7 – A6sus), 96 BPM; soft pulse from shot 2; drops out 300 ms before the end-card hit.
- **SFX palette:** pen scratch (shaped noise), key taps, link chime, paper swell.
- **Sonic logo:** A4 → D5 → F♯5 rising (a "stroke upward"), landing with the logo dot.
- **Mix:** music ducked −10 dB under voice; integrated **−14 LUFS**, true peak ≤ −1 dBTP (measured: see QA-REPORT.md).

## 7. Captions
Burned in (designed into the composition, Satoshi on an ink plate, safe areas respected) **and** sidecar `quill-launch.srt` + `quill-launch.vtt`; ≤ 42 characters per line, ≤ 2 lines, ≥ 1 s per cue, timed from the actual voice lines.

## 8. Export
| Version | Resolution | FPS | Codec / container | Bitrate | Loudness | File |
|---|---|---|---|---|---|---|
| 16:9 | 1920×1080 | 30 | H.264 High, yuv420p, AAC 48 kHz 192k, MP4 +faststart | CRF 18 | −14 LUFS | `quill-launch-16x9.mp4` |
| 9:16 | 1080×1920 | 30 | same | CRF 18 | −14 LUFS | `quill-launch-9x16.mp4` |
| Thumbnails | 1920×1080, 1080×1920 | — | JPG | — | — | `thumbnail-16x9.jpg`, `thumbnail-9x16.jpg` |

## 9. QA checklist
See `QA-REPORT.md` for the run results.

## 10. Licences
| Asset | Source | Licence |
|---|---|---|
| Fraunces (display) | Google Fonts / Undercase Type | SIL OFL 1.1 (`project/fonts/Fraunces-OFL.txt`) |
| Satoshi (body/UI) | Fontshare / Indian Type Foundry | ITF Free Font License 2.0 — explicitly allows Video, Social Media, Digital Advertising (`project/fonts/Satoshi-FFL.txt`) |
| Narration voice model | rhasspy/piper-voices `en_GB-cori-high` | Trained on public-domain LibriVox recordings (model card in `.tools/voices/MODEL_CARD.txt`) |
| Piper TTS engine 1.8.0 | github.com/OHF-Voice/piper1-gpl | GPL-3.0-or-later (tool only; the generated audio is not a derivative of the program) |
| Music, SFX, sonic logo | Synthesised in `project/audio/compose.js` | Original work for Quill |
| Playwright, FFmpeg | Microsoft / FFmpeg | Apache-2.0 / GPL build (tools only) |

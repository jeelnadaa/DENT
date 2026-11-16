# Video Plan: DENT launch film, "The Impression"

> DENT video plan (`/dent:video`, All-out). Built in code, rendered frame by frame. Source of truth for timing: `timeline.js` (picture and score both read it).

## 1. Brief
- **Type and sub-type:** Launch → Reveal (48 s).
- **Audience and where they'll watch:** developers and designers using AI coding agents; X/LinkedIn feeds, Product Hunt, YouTube, the DENT site. Often muted, so every idea is carried by on-screen type.
- **One message:** AI agents can build anything; DENT makes them design it, not template it.
- **Call to action:** `dent.solarquack.in` · `github.com/jeelnadaa/DENT` (free, Apache-2.0).
- **Length and aspect ratio:** 48 s, 16:9, 1920×1080, 60 fps (user chose 16:9 only).
- **Mood words:** tactile, confident, witty. **Anti-words:** glossy, generic.
- **Creative concept:** a letterpress strike. Good design leaves an impression: the orange dot is the punch that dents the generic, and the name is stamped into paper.
- **Must show:** the real category cliché (named, not invented), real DENT behaviour (questions, pipeline, verification), real benchmark numbers with their caveat, the name by ~9 s, CTA held ≥ 2 s.
- **Must not show:** features DENT doesn't have, invented stats presented as DENT's, any real brand's look. The "10,000+ teams" line appears only inside the labelled parody template, annotated "invented stats".
- **Assets:** brand tokens from `site/index.html` (paper/ink/orange dot, Instrument Serif + Geist + Geist Mono, motion easings), facts from `README.md`, `benchmark/RESULTS-SUMMARY.md`, `skills/dent/SKILL.md`.

## 2. Tools
- **Generative access:** none (user: build in code).
- **Build:** HTML/CSS/JS composition (`composition.html`) driven by a single `render(t)`; Playwright Chromium captures each frame; FFmpeg encodes (H.264, CRF 14, BT.709). HyperFrames-style approach from `references/video/video-tools-and-pipeline.md` §4, written from scratch, no framework.
- **Score:** `score.py` synthesises every sound from oscillators and noise (NumPy/SciPy), mixes, and normalises with FFmpeg `loudnorm` (two-pass).

### Licences
| Asset | Source | Licence |
|---|---|---|
| Geist, Geist Mono | Vercel via Fontsource npm | OFL-1.1 |
| Instrument Serif | Instrument via Fontsource npm | OFL-1.1 |
| Inter (only inside the parody template) | rsms via Fontsource npm | OFL-1.1 |
| DENT "Impression" lettering | drawn for this film (SVG paths in `composition.html`) | Apache-2.0 (this repo); DENT name is a trademark (TRADEMARKS.md) |
| Music, SFX, sonic logo | synthesised in `score.py`, no samples | Apache-2.0 (this repo) |
| Playwright, FFmpeg, NumPy, SciPy | tools only, not distributed in the output | Apache-2.0 / LGPL-GPL / BSD |

## 3. Script (on-screen text; no voice-over by choice)
| # | Time | On-screen text | Visual | Sound |
|---|---|---|---|---|
| 1 | 0:00–0:03 | Ask an AI / for a *website.* | Words punch in on each beat, then collapse into a generic chat prompt; send | Drone; a thud per word; key click + swoosh |
| 2 | 0:03–0:07 | (labels) violet gradient · glowing orb · centered headline · three equal cards · invented stats → **You get this. *Every time.*** | Parody template builds itself in 1.25 s, gets annotated, clones into a 7×5 wall | Glossy pops, bland four-on-the-floor, riser |
| 3 | 0:07–0:08 | — | Silence. The orange dot appears, hangs, falls with stretch | Silence, falling whistle |
| 4 | 0:08–0:14 | **DENT.** · DENT 2.3 ● out now · Make a dent with your product's *design.* | Impact: shockwave, dent in the paper, wall scatters with physics; dot hops to the full stop; D-E-N-T stamp on the beat | Impact, paper debris, 4 letterpress thunks, woodblock tok (motif note 1), groove starts |
| 5 | 0:14–0:17 | The design skill / for *AI agents.* · Claude Code · Codex · Cursor · Copilot · Gemini CLI · any SKILL.md agent | Wordmark shrinks into the lockup; line-mask reveals; chips | Groove |
| 6 | 0:17–0:23 | **01** It asks / *before it guesses.* | Dot-wipe to ink; terminal: `/dent a landing page for my coffee app` → "How far should I take it?" → All-out → pipeline lights up | Typing, select chime, ascending marimba per pipeline step |
| 7 | 0:23–0:29 | **02** It names / the cliché. / *Then diverges.* · 41 styles · 25 directions · 18 hero-type moves | Dot-wipe to paper; cliché list struck through; split-flap board flips through styles and settles on SWISS + KINETIC TYPE | Marker zips, flap clatter, chord on settle |
| 8 | 0:29–0:34 | **03** It checks / *its own work.* · 6 checks · PASSED | Dot-wipe to ink; a page reflows through 320→1440 px; checklist ticks; stamp | Half-time groove, ratchet ticks, bell pings, stamp |
| 9 | 0:34–0:38 | Builds that passed every automated check · **0/7** without DENT · **7/7** with DENT · method and caveats link | Dot-wipe to paper; numerals count up | Marimba count, accent stab, riser + snare roll |
| 10 | 0:38–0:41 | Interfaces. Motion. 3D. Sound. Video. | Hard cut to ink; each word in its own treatment (grid snap, motion echo, extrusion, bouncing on a waveform, film frame) | The burst: hit + stab per word |
| 11 | 0:41–0:43.5 | *This film was made with* `/dent:video` | Dot-wipe to paper; command types | Breakdown, typing |
| 12 | 0:43.5–0:48 | **DENT.** Make a dent with your product's *design.* · Free & open source · Apache-2.0 · dent.solarquack.in · github.com/jeelnadaa/DENT | Wordmark re-stamps, the dot drops in last | Sonic logo: tok, A5, D6, D major add9 (minor world resolves to major) |

Text holds follow 0.5 s + 0.3 s/word, except the 0.5 s capability burst, which is deliberate rhythm; the row under it keeps all five words on screen for the final second.

## 4. Storyboard
Stills of every key frame (poster test) are rendered with `python render.py stills <t…>`; the review sheets live in `out/` (not committed). Transition family: **the dot grows** (circle wipe with an orange ring), one hard cut into the burst.

## 5. Typography and signature
- **Custom lettering, "Impression":** geometric heavy caps on a 300-unit cap height with 78-unit stems. Circular ink traps at every inner joint (the dot, repeated as tiny dents). Letterpress texture via SVG turbulence; paper highlight/shadow halo. The full stop overshoots the baseline by 3 units (optical correction).
- **System:** Geist 760–850 tight (−0.05 em) for statements, Instrument Serif italic for the emotional half of each line, Geist Mono uppercase (+0.09 em) for labels and data.
- **Color:** paper `#FBFAF6`, ink `#121212`, dot `#E8461E` (paper) / `#FF5A1F` (ink); orange text on paper uses `#B8330F` (5.71:1).
- **Motion tokens:** the site's easings (`cubic-bezier(.16,1,.3,1)` out, `(.65,0,.35,1)` in-out, `(.55,0,1,.45)` in), plus physics for the strike (gravity, squash and stretch, damped springs).

## 6. Sound
- **Narration:** none (user choice). On-screen text carries the message.
- **Music:** original, D minor at 120 BPM (Dm9 · B♭maj7 · Fmaj7 · Csus2), resolving to D major on the sonic logo. Kick-driven sidechain ducking on the music bus.
- **SFX palette:** letterpress thunk, woodblock tok (the dot's voice), paper debris, key clicks, split-flap clicks, marker zips, bell pings, risers, whooshes, one impact.
- **Mix:** −14 LUFS integrated, true peak ≤ −1.5 dBTP (measured, see §9).

## 7. Captions
No speech, so nothing is burned in. `dent-launch-16x9.en.srt` is a description track: every on-screen line plus the key sound cues, for screen readers, translation and deaf viewers.

## 8. Export
| Version | Resolution | FPS | Codec / container | Loudness | File |
|---|---|---|---|---|---|
| Master 16:9 | 1920×1080 | 60 | H.264 High, yuv420p, BT.709 / AAC 256 kb/s, MP4 faststart | −14 LUFS | `out/dent-launch-16x9.mp4` |
| Thumbnail | 1920×1080 + 1280×720 | — | JPEG | — | `out/thumbnail*.jpg` |
| Description track | — | — | SRT | — | `dent-launch-16x9.en.srt` |

Rebuild: `npm install` in `video/`, then `python score.py`, `python render.py video`, `python render.py mux`.

## 9. QA checklist (final render, `python qa.py`)
- [x] Plays: 48.0 s, 1920×1080, 60 fps, H.264 High yuv420p + AAC LC 48 kHz stereo, 2880 frames (ffprobe)
- [x] Loudness: −14.0 LUFS integrated, true peak −1.2 dBTP, LRA 4.7
- [x] A/V sync: impact, stamps, dot press, PASSED, burst and logo onsets within −5 ms (first stamp −25 ms, 1.5 frames)
- [x] Flashing: largest luminance swings are the six scene changes, max 1 flash pair per second (limit 3)
- [x] Message understood with sound off (all meaning is on screen)
- [x] Hook works in the first 2 s (frame 1 already shows "Ask")
- [x] Claims true (README, SKILL.md, benchmark/RESULTS-SUMMARY.md); parody labelled
- [x] Contrast of every text pair checked with `contrast.py`
- [x] Licences recorded (§2)
- [ ] **Mix heard by a person** on headphones and a phone speaker (not done: the agent can't listen)
- N/A Safe areas for vertical (16:9 only, by choice)

Motion blur: `render.py` captures 8 sub-frames across a 180° shutter inside the fast-motion windows (`BLUR`) and averages them with FFmpeg `tmix`.

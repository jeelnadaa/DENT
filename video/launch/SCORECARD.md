# Scorecard: DENT launch film ("The Impression", 48 s, 16:9)

> DENT self-score (`/dent:score`), All-out. Target: overall ≥ 9, no line < 8. Date: 2026-11-16 · Round: improve-1 (after the first full render).
> Evidence files (regenerate, not committed): `out/qa.json`, `out/qa-sheet.png`, `out/final-sheet.png`, `out/spectrum.png`.

## Requirements (from the request)
| ID | Requirement | Score /10 | Evidence |
|---|---|---|---|
| R-01 | A launch video for DENT (reveal, ~45 s, 16:9 only, by the user's answers) | 9 | `out/dent-launch-16x9.mp4`: 48.0 s, 1920×1080, 60 fps, H.264 High + AAC 48 kHz stereo (ffprobe). Name visible from 9 s, CTA held 4.5 s |
| R-02 | Motion graphics | 9 | Physics strike (gravity, squash/stretch, radial scatter, shockwave, paper dent), dot-wipes, split-flap board, a page reflowing through 6 real widths, count-up, five distinct treatments in the burst; true motion blur (8 sub-frames, 180° shutter) on fast moves |
| R-03 | Kinetic typography | 9 | Beat-locked word punches, line-mask reveals, prompt morph, strike-throughs, word-per-beat burst (grid snap, motion echo, extrusion, waveform bounce, film frame), typed commands |
| R-04 | Custom typography | 8 | "Impression" DENT lettering drawn from scratch (SVG paths, 300-unit caps, circular ink traps at every joint, letterpress texture, overshooting full stop); bespoke type compositions mixing Geist, Instrument Serif italic and Geist Mono. Only four custom glyphs, so not a full typeface |
| R-05 | "Much more" | 8 | Original score and sound design, sonic logo, description caption track, thumbnails, reproducible pipeline (`timeline.js` drives picture and sound) |
| R-06 | Original music + SFX (user's choice) | 6 | Synthesised from scratch; −14.0 LUFS, −1.2 dBTP, LRA 4.7; hits land within −5 ms of picture (one at −25 ms). **Not heard by a person yet**, so capped at 6 |

## Quality lines
| Line | Score /10 | Evidence |
|---|---|---|
| Clarity (works muted) | 9 | Every beat is carried by on-screen text; message readable with sound off |
| Hierarchy & composition | 8 | Every key frame passes the poster test (stills sheets); chapter 02 right column was rebalanced after review |
| Typography | 9 | Tight display tracking, mixed faces with one swap per line, tabular numerals, mono labels; key lines ≥ 5 % of frame height |
| Color & surfaces | 9 | Brand tokens only; paper/ink alternation per chapter; one accent |
| Consistency | 9 | One transition family (the dot grows), one hard cut into the climax; site motion easings |
| Accessibility | 9 | Contrast: every text pair ≥ 4.5:1, large orange 3.78:1 (`contrast.py`; the 2.02:1 inactive labels were fixed to 5.04:1); flashing max 1 pair/s (limit 3); holds follow 0.5 s + 0.3 s/word except the deliberate 0.5 s burst; description SRT; sound carries no essential information |
| Distinctiveness | 9 | Category cliché named and literally smashed; letterpress concept; custom lettering; no stock, no gradient orb outside the parody |
| Content honesty & copy | 9 | Only real facts (41 styles, 25 directions, 18 hero-type moves, 31 commands not claimed on screen, benchmark 0/7 vs 7/7 with its method and caveat link); the "10,000+ teams" line lives only in the labelled parody |
| Motion | 9 | Anticipation, follow-through, squash and stretch, staged one focal action at a time; motion blur |
| Sound | 6 | See R-06: measured, not listened to |
| Video craft | 8 | Hook in frame 1, cuts on the beat, end card held; only a 16:9 master (9:16 and 1:1 not requested) |

**Overall:** 8.5 / 10 · Lowest line: Sound, 6 (unverified by ear). **The All-out target is not met** until someone listens to the mix.

## Top 3 improvements
| # | Raises line | Change | Expected score |
|---|---|---|---|
| 1 | Sound / R-06 | You listen once on headphones and on a phone speaker; I adjust balance (kick vs plucks, stamp weight, logo tail) from your notes | 8–9 |
| 2 | Video craft | 9:16 and 1:1 cuts re-composed (not cropped) from the same timeline, captions inside safe areas | 9 |
| 3 | Custom typography | Extend "Impression" into a full uppercase set so chapter numerals and the burst also use it | 9 |

## Attribution
- **From DENT:** video pipeline and launch rules (`video-types-and-craft.md` §2, `video-tools-and-pipeline.md` §4–6), All-out sweep 2.10, motion principles and techniques (`motion-graphics.md` §4–6), hero-type moves (`hero-typography.md` §4), sound sync rules (`sound-design.md` §6), honesty gate, contrast rules, `contrast.py`, `validate.py`.
- **From the user:** reveal ~45 s, original music + SFX without voice, build in code, 16:9 only, "The Impression" direction and its script.
- **Agent judgment:** letterpress concept, "Impression" lettering, D minor → D major sonic logo, the meta line "This film was made with /dent:video", sub-frame motion blur, the description track.
- **Overrides:** none of a [Rule]. Deliberate: the capability burst holds each word 0.5 s (rhythm over the 0.8 s guideline); the row below keeps all five words on screen for the final second.

## Changes since last round
| Line | Before | After | What changed |
|---|---|---|---|
| Accessibility | 7 | 9 | Inactive labels on ink 2.02:1 → 5.04:1; "Every time." hold 0.85 s → 1.1 s; benchmark footnote hold 2.1 s → 3.3 s and shortened |
| Motion | 8 | 9 | 8-sub-frame motion blur on the strike, hop, wipes, stamps, burst entrances and logo drop (4 sub-frames showed stepping, so raised to 8) |
| Sound | gaps | continuous | Partial first bars of each section were silent; groove now covers them; half-time chapter 03 for contrast before the burst |

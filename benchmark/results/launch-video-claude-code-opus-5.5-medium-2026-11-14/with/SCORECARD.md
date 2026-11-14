# Scorecard: Quill launch video (45 s, X + LinkedIn)

> DENT self-score. Evidence for every line; unverified lines max 6. Requirement lines count double.
> Target (All-out): overall ≥ 9 and no line < 8. Date: 2026-11-14 · Round: improve-1 (after the fixes listed in QA-REPORT.md)

## Requirements
| ID | Requirement | Score | Evidence |
|---|---|---|---|
| R1 | 45 seconds | 10 | ffprobe 45.000 s, 1350 frames, both cuts |
| R2 | For X and LinkedIn | 9 | 16:9 + 9:16 (user's choice), H.264/AAC, faststart, 7 MB, −14 LUFS. No 1:1/4:5 (not chosen) |
| R3 | Launch video for a note-taking app called Quill | 9 | Hook by 1.2 s, name drawn 4.4–6.1 s, 3 product moments, end card held 5 s+ |
| R4 | Final MP4s in this folder | 10 | `quill-launch-16x9.mp4`, `quill-launch-9x16.mp4` |
| R5 | Project files used to make them | 9 | `project/` (composition, script, TTS, captions, renderer, score, mix, mux, fonts + licences) + README with rebuild steps; Piper venv/voice in `.tools/` |
| R6 | Captions file | 9 | SRT + VTT, cut at the voice's real pauses, ≤ 42 chars/line; also burned in |
| R7 | Synthetic voice-over (Piper / Cori) | 7 | Every word present; phonemes correct for Quill/example; ducking measured. Naturalness not judged by ear |
| R8 | Music + SFX, licensed | 8 | Original score + frame-synced SFX, measured levels; quality not judged by ear |
| R9 | Mini identity, direction A, Satoshi | 9 | DESIGN.md tokens/type/logo; Satoshi + Fraunces asserted loaded on every render |
| R10 | Honesty | 8 | No invented proof; features + shortcut are proposed (flagged in 4 places) |
| R11 | Legibility & safety | 8 | Safe areas pass, no flashes, AA contrast; 16:9 UI text small on phones |
| R12 | Thumbnails | 9 | Both cuts, end card frame |

## Quality lines
| Line | Score | Evidence |
|---|---|---|
| Clarity | 9 | One message, three numbered moments, CTA |
| Hierarchy & composition | 8 | Strong single focal point per scene; 16:9 link scene a little busy at small size |
| Typography | 9 | Fraunces display with optical sizing + Satoshi UI; tight tracking on large type; kinetic hook words |
| Color & surfaces | 9 | Paper/ink/vermilion roles; all pairs AA after fix |
| Consistency | 9 | One token set and one transition family (the ink line) |
| Distinctiveness | 9 | Ink line = linking metaphor; diverges from category on type, colour, motion |
| Content honesty & copy | 8 | Tight, true copy; features proposed, not confirmed |
| Motion | 7 | Purposeful easing/springs; verified by frame sampling, not watched in real time |
| Motion graphics | 8 | Storyboarded, nib-led drawing, chip→card link as the peak moment |
| Sound | 6 | Measured only (−14 LUFS, ducking, peaks); not heard (cap) |
| Voice / narration | 7 | Phonemes and timing verified; naturalness unheard |
| Video | 8 | Hook, pacing, sync by construction, captions, specs |
| Accessibility | 9 | Captions burned + sidecar, 15:1 caption contrast, no flashes, sound-off comprehension |

**Overall:** 8.4 / 10 (requirements ×2) · Lowest lines: Sound 6, Motion 7, Voice 7.
**All-out target not met** (needs ≥ 9, no line < 8). Each line that is short is either capped because nobody has listened or watched yet, or is a small layout trade-off.

## Top 3 improvements
| # | Raises line | Change | Expected |
|---|---|---|---|
| 1 | Sound, Voice (→ 8) | **You listen once** to either MP4 on a phone speaker and headphones: voice natural? music too loud or quiet? I adjust `MUS`/duck depth or Piper `--length-scale` and re-render (~25 min) | Sound 8, Voice 8 |
| 2 | Motion, Video (→ 8–9) | **You watch it in real time** and note any move that feels slow or jerky; I retime those `T` constants | Motion 8 |
| 3 | R11, Hierarchy (→ 9) | Make the 16:9 cut more phone-friendly: zoom into the active card during each feature (camera push) so UI text reads at ~45 px | R11 9, Hierarchy 9 |

## Attribution
- **From DENT:** reveal structure and launch rules (`video-types-and-craft.md` §2), HTML-composition → Playwright → FFmpeg pipeline and QA list (`video-tools-and-pipeline.md`), Editorial style overrides (`styles/editorial.md`), sound sync rules + silence before impact + sonic logo (`sound-design.md` §5–6), gates G1–G12, contrast script, All-out sweep 2.10.
- **From you:** All-out, features delegated to me, demo link (not a placeholder), music + synthetic VO, Piper + Cori, no brand → mini identity, 16:9 + 9:16, direction A, Satoshi, script approval.
- **Agent judgment:** the three features and the shortcut, the "Think in ink." line, Fraunces as display, `quill.example`, caption cuts at detected voice pauses, the chip→card ink link as the signature moment, the D-major score and sonic logo.
- **Overrides:** captions are designed into the composition rather than burned in with FFmpeg's `subtitles` filter, so they use the brand type and respect each frame's safe area.

## Changes since last round
| Line | Before | After | What changed |
|---|---|---|---|
| Color & surfaces | 4 (G3 failed) | 9 | Vermilion #C2410C → #B23A0B; hint → ink-2 |
| Video | 7 | 8 | Removed blank frame at ~5.0 s |
| R11 Legibility | 6 | 8 | Captions no longer cover search results |

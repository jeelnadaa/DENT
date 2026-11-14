# QA report — Quill launch video (2026-11-14)

Results for the final files `quill-launch-16x9.mp4` and `quill-launch-9x16.mp4`. Every check says **Passed / Failed / Not run / N/A**, with how it was checked.

## Video QA (DENT `video-tools-and-pipeline.md` §6)
| Check | Result | Evidence |
|---|---|---|
| File plays; duration/resolution/fps/codec | **Passed** | ffprobe: 45.000 s, 1350 frames each; H.264 High yuv420p 30 fps; AAC-LC 48 kHz stereo; 1920×1080 (7.2 MB) and 1080×1920 (7.5 MB); `+faststart`; full decode with no errors |
| Platform limits (X ≤ 2:20 / 512 MB; LinkedIn ≤ 10 min / 5 GB) | **Passed** | 45 s, ~7 MB |
| Loudness / peaks | **Passed** | EBU R128: −14.0 LUFS integrated, LRA 7.6 LU, true peak −2.9 dBTP (target ≤ −1) |
| Voice over music | **Passed (measured)** | Segments with voice ≈ −12 LUFS; music alone ≈ −19 LUFS; music ducked −10 dB under each line |
| A/V sync | **Passed (by construction + spot check)** | SFX come from the composition's own frame-exact event list; VO is placed by `timing.json`, and captions are cut from the same timing at the voice's detected pauses. Spot-checked caption-on frames against VO start times |
| Captions | **Passed** | `quill-launch.srt` / `.vtt`: 7 cues, ≤ 42 chars/line, ≤ 2 lines, every cue ≥ 1.5 s; also burned in on an ink plate (15:1 contrast) |
| Message with sound off | **Passed** | Contact sheets (1 fps, both cuts): on-screen titles + captions carry every line |
| First 2 s hook | **Passed** | Frame 0 shows "Good" + ink nib in motion; "Good ideas don't wait." is complete by 1.2 s |
| Product name early | **Passed** | Wordmark is drawn from 4.4 s and fully revealed by 6.1 s; VO says "Meet Quill" at 5.6 s |
| Text legibility | **Passed (9:16)** / **Partly (16:9 on phones)** | 9:16 card text 34 px on a 1080-wide frame. 16:9 card text is 31 px, which is small when X shows a 16:9 video inline on a phone |
| Truth | **Passed, with a flag** | No numbers, users, ratings, quotes, logos or prices. The three features + the ⌘⇧Space shortcut are **proposed** (you asked me to choose them), so confirm before posting. `quill.example` is a reserved demo domain |
| Safe areas (9:16) | **Passed** | Captions end at y = 1500 (bottom 20 % starts at 1536); titles start at y = 300 (top 12 % = 230); only the small brand bug sits in the top band |
| Flashing | **Passed** | Mean-luma change per frame: max 3.5/255, with zero frames above 10 (nothing close to a flash) |
| Versions | **Passed** | 16:9 + 9:16 as chosen; thumbnails `thumbnail-16x9.jpg` (1920×1080) and `thumbnail-9x16.jpg` (1080×1920) |
| Licences | **Passed** | VIDEO.md §10: Fraunces (OFL), Satoshi (ITF FFL, which explicitly allows video), Cori voice (public-domain training data), all music/SFX original |
| Pronunciation | **Passed (phonemes)** | Piper phonemes: Quill → /kwˈɪl/, "quill dot example" → /kwˈɪl dˈɒt ɛɡzˈampəl/ |
| Naturalness of the voice, mix by ear | **Not run** | I can't listen. A dictation transcript (Windows speech recognition) caught every word in v4 but is too inaccurate to judge quality |
| Real-time playback smoothness | **Not run (by eye)** | Checked through frame sampling (1–2 fps contact sheets + targeted stills); motion is deterministic easing at 30 fps, but nobody has watched it in real time |

## DENT gates (SKILL.md §3)
| Gate | Result | Note |
|---|---|---|
| G1 Requirements | Passed | PLAN.md R1–R12 traced in SCORECARD.md |
| G2 Layout | Passed | Both frames composed separately; nothing clipped (contact sheets) |
| G3 Contrast | Passed (after fix) | Vermilion darkened #C2410C → #B23A0B (4.44 → 5.14:1 on paper); hint text moved to ink-2 (4.24 → 6.88:1) |
| G4 Operability | N/A | Video, no controls (the platforms' players provide them) |
| G5 States | N/A (shown in-story: empty capture → typing → saved; popover → filtered → selected; search recent → filtered → selected) |
| G6 Honesty | Passed, flagged | See "Truth" |
| G7 Proofread | Passed | All on-screen strings and captions read; British/US spelling consistent (no -ise/-ize words) |
| G8 Style integrity | Passed | Editorial + Kinetic Type; 2 families; tokens only |
| G9 Distinctiveness | Passed | Cliché named (purple SaaS / 3D card stacks / glowing graph); diverged on type, colour, motion |
| G10 Motion | Passed | Every move has a job; no flashes; reduced motion N/A for a rendered video |
| G11 Sound | Passed (measured) / ear test Not run | No autoplay concerns (platform players start muted); captions are the visual equivalent |
| G12 Licences | Passed | VIDEO.md §10 |

## Improve round 1 (fixed before delivery)
1. Contrast: vermilion and hint colour failed AA → fixed (G3).
2. A blank paper frame at ~5.0 s between hook and name → the name stroke now starts while the hook fades.
3. In both cuts, captions covered the 5th search result at 31–33 s → the list now opens on 4 recent notes and the palette clears the caption zone.

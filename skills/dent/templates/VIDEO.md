# Video Plan: <title>

> DENT video plan (`/dent:video`, `/dent:launch-video`). See references/video/. Fill top to bottom; get the brief and script approved before building.

## 1. Brief
- Type and sub-type (e.g. Launch → feature tour; Explainer → kinetic-type):
- Audience and where they'll watch (platform, sound on/off, device):
- One message (a single sentence the viewer must remember):
- Call to action (exact words + URL):
- Length and aspect ratio(s): <e.g. 60 s 16:9 + 30 s 9:16 cut>
- Tone / mood words / anti-words:
- Creative concept (one sentence):
- Must show / must not show:
- Assets available (logo, screenshots, footage, brand fonts, music):

## 1b. Creative direction (`references/video/video-creative-direction.md`)
- Creative menu answers (feel, typography, motion language, graphics, sound, never):
- Directions offered (name + logline each) and the one chosen or combined:
- Film bible of the chosen direction (world, signature device, type, motion language, transitions, camera, colour script, sound world, structure, the moment, never):
- Escalation moves and where they land:
- Genre bar (what exceptional looks like for this genre, §5):
- Originality guard: no DENT launch-film devices · no genre clichés · differs from earlier films on ≥ 4 axes (list them):
- Products only, three answers with sound off: what is it / what does it do for me / how do I get it; planned share of real-product screen time (≥ 60 %):

## 2. Tools
- Media sources (`references/media-sourcing.md` §2), one row per type:

| Media | Source (local model / free cloud / paid provider or connector / own assets / code-built) | Model or provider + version | Cost | Licence / commercial OK | Consent (voices, people) |
|---|---|---|---|---|---|
| Footage / imagery | | | | | |
| Voice | | | | | |
| Music | | | | | |
| SFX | | | | | |

- How it is made (render / capture / generate / hybrid) and why; code-built films start from `templates/video-kit/` and render through a browser engine:
- Build tool and why (video kit / HyperFrames / Remotion / Motion Canvas / Revideo / Manim / editor / generative):
- Licences (tool + every asset):

## 3. Script
| # | Time | Voice-over (spoken) | On-screen text | Visual | Sound |
|---|---|---|---|---|---|
| 1 | 0:00–0:03 | | | | |

Words per minute target: ~140–160 for narration. Read it aloud with a timer before building.

## 4. Storyboard
| Shot | Duration | Frame (composition) | Motion | Transition out | Notes |
|---|---|---|---|---|---|

## 5. Animatic
Rough timing pass with placeholder frames + scratch voice. Lock timing before polishing.

## 6. Sound
- Narration (voice, engine/actor, licence):
- Music (track, licence, edit):
- SFX palette:
- Mix: voice clear, music ducked, loudness target (−14 LUFS most platforms; check platform spec)

## 7. Captions
Burned-in and/or sidecar (.srt/.vtt); max ~42 characters per line, 2 lines, ≥ 1 s per caption.

## 8. Export
| Version | Resolution | FPS | Codec / container | Bitrate | Loudness | File |
|---|---|---|---|---|---|---|

## 9. QA checklist
- [ ] `python scripts/video_qa.py <film> --captions <srt> --sheet <jpg>` passes (colour range, sync, loudness, frozen time, longest hold, captions) and I looked at the sheet
- [ ] Contact sheet of stills reviewed before the final render; fixes listed
- [ ] Genre bar met; the bible followed in every scene; originality guard passed
- [ ] Sound heard by a person (or reported as unverified, line ≤ 6)
- [ ] Message understood with sound off (captions + on-screen text)
- [ ] First 3 seconds hook works
- [ ] No typos; brand names correct; claims true
- [ ] A/V sync; no clipped audio; loudness on target
- [ ] Safe areas respected for each platform
- [ ] No flashing > 3/s
- [ ] Licences recorded
- [ ] Final file plays in a standard player (ffprobe output attached)

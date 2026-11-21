# Sound Spec: <project / piece>

> DENT sound spec. See references/audio/. Sound is always optional, never autoplays, and every sound has a visual equivalent.

## 1. Audio direction
- Role of sound here (feedback / identity / atmosphere / storytelling / narration):
- Sonic concept in one sentence (e.g. "soft wooden taps in a quiet studio"):
- Character: <warm | glassy | analog | digital | organic | minimal> · Anti: <…>
- Silence policy (where we deliberately use none):

## 2. Sound palette
| Category | Sounds | Timbre / source | Length | Peak level |
|---|---|---|---|---|
| Confirm | | | 80–200 ms | |
| Error | | | | |
| Notification | | | | |
| Transition / whoosh | | | | |
| Ambient (opt-in) | | | loop | |
| Sonic logo | | | 1–3 s | |

## 3. Interaction-to-sound map
| Event | Sound | Plays when | Visual equivalent | Repeat limit |
|---|---|---|---|---|

## 4. Narration (if any)
- Script file / version:
- Voice source (`references/media-sourcing.md` §2): human / local engine / cloud provider (any) — engine or provider, model, voice/preset, instruct or design text, seed, licence, commercial OK, consent:
- Blind A/B: engines/voices compared (`tts.py compare`), the user's pick:
- Mastering (`tts.py post`): target LUFS, measured LUFS and true peak (PASS/FAIL), captions files, timing JSON:
- Pace (words per minute), pronunciation notes, tone:
- Captions / transcript file:

## 5. Music (if any)
- Track / source / licence / attribution text:
- Edit points, ducking under voice (−8 to −12 dB):

## 6. Technology
- Playback / synthesis / analysis library (one per job; see audio/audio-tech-catalog.md):
- Formats (e.g. .webm Opus + .mp3 fallback), sample rate, sizes:
- Loading and caching:

## 7. Controls and preferences
- Global mute / volume UI and location:
- Default state (off unless the user opts in):
- Persistence:
- Respect reduced data / low power:

## 8. Mixing and loudness
- UI sounds: short, peaks ≤ −6 dBFS, quieter than any voice
- Narration: around −16 LUFS integrated (web/podcast), −14 LUFS for most social/video platforms; true peak ≤ −1 dBTP

## 9. Licences
| Asset | Source | Licence | Attribution required? |
|---|---|---|---|

## 10. Verification results
| Check | Result | Evidence |
|---|---|---|

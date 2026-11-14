# Sound Design

Sound gives a product character and makes feedback felt. Done badly it's the fastest way to annoy people. DENT treats sound as a designed system: purposeful, cohesive, **always optional**. Used by `/dent:sound`, `/dent:brand` (sonic logo), `/dent:video`, `/dent:launch-video`, `/dent:motion-graphics`. Spec template: `templates/SOUND.md`. Narration: `voice-and-narration.md`.

---

## 1. Kinds of audio (know which you're designing)

| Kind | What it is | Examples |
|---|---|---|
| **UI sound** | Short feedback for interactions and states | Send, success, error, toggle, notification, drag drop |
| **Sonic identity** | A recognisable audio signature | Sonic logo (1–3 s), startup sound, signature notification |
| **Motion-graphics SFX** | Sound designed to picture | Whooshes, impacts, risers, clicks synced to animation |
| **Ambience** | Background atmosphere | Café room tone, rain, studio hum, space drone |
| **Interactive / procedural** | Sound generated or shaped by input, state or data | Pitch follows a slider, data sonification, generative music |
| **Music** | Scored, licensed or generated tracks | Video beds, game loops, onboarding theme |
| **Voice** | Narration, voice-over, dialogue, voice UI prompts | Explainer narration, TTS read-aloud, assistant voice |
| **Audio description** | Narration of visual content for blind users | Described versions of videos |
| **Audio visualisation** | Visuals driven by audio | Waveforms, spectrograms, audio-reactive graphics |
| **Spatial audio** | Positioned sound in 2D/3D space | 3D scenes, games, XR |
| **Haptic pairing** | Sound matched with vibration patterns | Mobile confirmations |

## 2. When sound helps, and when it hurts
**Helps:** confirming actions that happen out of sight (sent, saved in background), signalling time-critical events (timer done, incoming call), giving games/creative/music tools feel, reinforcing identity at rare moments (startup, achievement), storytelling in video.
**Hurts:** frequent actions (every click/keystroke), workplaces/shared spaces, anything loud or sudden, sounds that repeat identically hundreds of times, required sounds, autoplay.
**Default for websites:** silent, with an optional, clearly labelled sound toggle only when sound is part of the brand or experience.

## 3. Audio direction
Write: role of sound · sonic concept in one sentence ("soft wooden taps in a quiet studio") · character words + anti-words · silence policy (where there is deliberately none). Pick a palette from `../creative/directions-library.md` §5 or invent one from the product's materials.

Matching sound to visual direction:
| Visual direction | Sonic character |
|---|---|
| Precise / Swiss / Utilitarian | Dry, short, high-mid clicks; no reverb; mechanical |
| Calm / Japandi / Kissaten | Wood, ceramic, felt; low volume; natural decay |
| Playful / Toybox | Marimba, xylophone, pops; pitched "rewards"; light bounce |
| Premium / Monolith | Low, warm, minimal; a single resonant tone; lots of silence |
| Retro / Arcade / Retro OS | Square/triangle waves, bit-crushed blips |
| Glass / Aurora / AI | Glassy pings, soft pads, airy shimmer |

## 4. Designing individual sounds
- **Length:** UI 50–300 ms; notifications 300–800 ms; sonic logo 1–3 s.
- **Envelope (ADSR):** fast attack (≤ 5 ms) for clicks; short decay; no sustain for UI; gentle release to avoid clicks.
- **Pitch and meaning:** rising = positive/start/open; falling = negative/end/close; consonant intervals (third, fifth) = success; dissonant/low = error (still gentle).
- **Frequency:** place UI sounds in 1–4 kHz for clarity on phone speakers; avoid harsh 2–5 kHz peaks at high level; avoid sub-bass for UI (inaudible on phones, annoying on headphones).
- **Family:** all sounds share timbre, reverb space and loudness, like a type family.
- **Variation:** for repeated events, 2–4 subtle variations (pitch ±2–5 %, timing) to avoid machine-gun fatigue.
- **Levels:** UI peaks around −6 to −12 dBFS, consistently quieter than voice; no clipping.

## 5. Sonic logo / identity
- 1–3 seconds, 2–5 notes or a single designed texture; memorable contour (interval pattern) that survives on phone speakers.
- Variations: full (video end card), short (app start), micro (notification), and a version that works under voice.
- Ties to the visual logo animation: the key note lands with the logo's settle frame.
- Avoid resembling famous sonic logos; check originality by ear and comparison.

## 6. Sound for motion graphics and video
- **Spot the edit:** list every visual event; give sound only to the important ones (hierarchy applies to sound too).
- **Sync:** sound starts on the impact/landing frame, not at movement start; whooshes peak at the fastest part of a move.
- **Layers:** base (music bed or ambience) → mid (transitions, whooshes) → top (impacts, UI clicks, voice). Voice always wins: duck music −8 to −12 dB under narration.
- **Silence before impact:** 200–500 ms of quiet makes a hit land.
- **Risers** sparingly: one per piece for the main reveal.
- **Music edit:** cut on downbeats; use stems if available; end on a resolved chord or a designed tail, never a fade-out mid-phrase unless deliberate.

## 7. Ambience
Opt-in only; low level (≈ −30 to −24 LUFS short-term); seamless loops (crossfaded loop points, ≥ 30–60 s to hide repetition); pause on tab hidden; one control to stop it, visible at all times while playing.

## 8. Interactive and procedural audio
- Map continuous controls to continuous sound parameters (slider → pitch/filter), with smoothing (`setTargetAtTime`) to avoid zipper noise.
- Data sonification: map data ranges to pitch ranges perceptually (log scale for pitch); always pair with a visual chart and a text summary.
- Generative music: constrain to a scale and tempo; limit polyphony; provide stop/mute.

## 9. Audio-reactive visuals
Analyse with `AnalyserNode` (FFT) or Meyda features (RMS, spectral centroid); smooth values (exponential moving average) before driving visuals; map bass → scale, highs → particles/brightness; keep the visual meaningful when muted (idle animation or static).

## 10. Accessibility and control (non-negotiable)
- Never autoplay. Audio starts only after a user gesture and an explicit choice.
- A visible mute/volume control whenever sound can play; persists the choice; default off on websites.
- Every sound has a visual equivalent (state change, toast, icon, caption).
- Captions/transcripts for speech; audio description for essential visual information in videos.
- No sudden loud sounds; limit repetitions; respect system "reduce motion/sounds" signals where available, and data-saver (`navigator.connection.saveData`).
- The whole product works fully muted.

Implementation and verification: `audio-implementation-and-verification.md`. Technology and asset sources: `audio-tech-catalog.md`, `../catalog/asset-sources.md` §7–8.

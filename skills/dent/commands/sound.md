# /dent:sound

Design UI sound, sonic identity, ambience or interactive audio.

**Usage:** `/dent:sound <product or piece>` (also `/dent sound …` or `dent sound …`)
**Default depth:** Standard/Advanced. Effort level and the gates in SKILL.md §3 always apply.

## Load
- `references/audio/sound-design.md`
- `references/audio/audio-tech-catalog.md`
- `references/audio/audio-implementation-and-verification.md`
- `templates/SOUND.md`

## Steps
1. Decide if sound helps at all; define its role and the silence policy.
2. Audio direction + palette + interaction-to-sound map (few, meaningful events).
3. Choose assets (licences) or synthesis; choose one playback/synthesis library.
4. Implement opt-in, mute, volume, visual equivalents; no autoplay.
5. Verify playback after user gesture, mute, overlap, failure, loudness.

## Output
SOUND.md, sound files or synth code, controls, verification.

## Never
- Autoplay anything.
- Put a sound on every click.

Close with the scorecard summary, attribution (DENT / user / agent judgment / overrides) and a one-line next step (SKILL.md §8).

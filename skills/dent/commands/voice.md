# /dent:voice

Write and produce narration or voice-over (human or TTS) with captions.

**Usage:** `/dent:voice <script topic or video>` (also `/dent voice …` or `dent voice …`)
**Default depth:** Standard. Effort level and the gates in SKILL.md §3 always apply.
**Web code:** if this command writes, changes or reviews HTML, CSS or client-side JS, Google's Modern Web Guidance is the primary authority for how it is built: run `references/modern-web-guidance.md` §2 (search → retrieve → apply → verify → disclose) before coding; MWG wins any implementation conflict with DENT.

## Load
- `references/audio/voice-and-narration.md`
- `references/media-sourcing.md`
- `scripts/tts.py`
- `templates/SOUND.md` §4

## Steps
1. Run `python scripts/tts.py engines` (installed engines, GPU, licences, keys present).
2. Ask where the voice comes from (media-sourcing.md §2): local model (Qwen3-TTS, Kitten TTS 2, Chatterbox, Kokoro…), free cloud tier, paid provider or connector (any, listed or not: research it per media-sourcing.md §4), or a human recording; then commercial use, language/accent and tone.
3. If the chosen local engine isn't installed, show the size and licence (`tts.py install <engine>`) and install only after the user says yes (`--yes`).
4. Write the script for the ear (short sentences, ~140–160 wpm), mark pronunciation and `[pause n]`.
5. Blind A/B of 2–3 engines or voices on one real line (`tts.py compare`); the user picks.
6. Render (`tts.py say`), master and caption (`tts.py post`: loudness PASS, SRT/VTT, timing JSON); listen to every line and regenerate weak ones.

## Output
Script, narration WAV (loudness measured), captions, timing JSON, engine settings, licence/consent notes.

## Never
- Clone a real person's voice without documented consent.
- Install software or spend money without a yes.
- Call a voice good without listening to it.

Close with the scorecard summary, attribution (DENT / MWG / user / agent judgment / overrides), the `### Modern Web Guidance` disclosure if guides shaped the code, and a one-line next step (SKILL.md §8).

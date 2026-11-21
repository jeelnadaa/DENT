# DENT video kit

The starting point for every **code-built** DENT video (launch films, trailers, explainers, social cuts). It packages the engine and quality invariants behind DENT's own launch film, not its look: every film invents its own direction. Copy this folder into the project (`video/<film>/`), then replace the scenes, tokens and timeline with your film.

| File | What it does |
|---|---|
| `timeline.json` | The single source of timing for picture **and** sound: bpm, fps, scene cuts, events, motion-blur windows, SFX cues, music, captions |
| `composition.html` | The film as one HTML page. `render(t)` sets every element for time `t` (deterministic). Engine helpers: easing family, `spring`, `fall` (gravity), `lines()` masked line reveals, `wipe()` transition, `livingFrame()` slow push, grain, captions |
| `render.py` | Headless Chromium → frames → FFmpeg. `stills` mode + contact sheet for review; `video` mode with sub-frame **motion blur** in fast windows and TV-range BT.709 encoding; 16:9, 9:16, 1:1 |
| `techniques.js` | Tested technique modules (`window.DENTFX`): custom lettering, variable-axis kinetic type, hand-made boil, morph, parallax camera + rack focus, glitch, physics (bounce, squash, shockwave), collage (torn paper, halftone), data (count, line chart), Three.js scene on the film's clock. Include it with `<script src="techniques.js"></script>` |
| `techniques.html` | The test bench: every module on one page. `python render.py stills --page techniques --times 0.4 1.1 2.3` must render without page errors |
| `score.py` | Original, beat-locked score + designed SFX from the timeline (no samples, no licences): FM bells/bass/e-piano, Karplus-Strong plucks, pads, layered drums, taiko, risers, Schroeder reverb, stereo; arrangement presets `pulse`, `cinematic`, `playful`, `minimal` with lifts and deliberate drops; optional narration with ducking; mastered to −14 LUFS / ≤ −1.5 dBTP. Presets are instruments to shape to the bible's sound world, not a house sound |

Needs Python 3.10+, `pip install playwright numpy`, `python -m playwright install chromium`, FFmpeg.

## What to keep and what to invent
The engine and the **quality invariants** below are fixed for every film. Everything you can see in the demo scenes (the two-voice type, the circle wipe, the numbered chapter, the colours, the fonts) is a **placeholder**: replace it with the direction your film's bible defines (`references/video/video-creative-direction.md` §3). Shipping the placeholders, or DENT's own launch-film devices, fails the originality guard (§4 there).

### Quality invariants (keep, every film, every genre)
1. **A timing grid.** One `timeline.json` drives picture and sound. Events land on a musical grid (`t = n * 60 / bpm`) or on narration word times (Whisper word timestamps), so sync is exact by construction.
2. **Density.** Something visible changes at least every 0.5 s outside deliberate holds. Only the end card (≤ 4 s) and silence before a payoff (≤ 1 s) may hold still. `video_qa.py` measures frozen time and the longest hold.
3. **Living frames.** Scenes keep breathing while text is read (`livingFrame()`, or your direction's equivalent: drift, parallax, boil, flicker, grain).
4. **One transition grammar.** A single family defined by the bible, plus at most one exception at the climax.
5. **Hero moments get physics and motion blur.** Define `blur` windows around every fast move; 60 fps for motion-heavy films.
6. **A system, not decoration.** Type from `scripts/fonts.py`, colour from `scripts/palette.py` (or the brand), one signature device defined in the bible and used throughout.
7. **Designed sound.** A sound for every visual event, a musical or tonal arc, deliberate silence, a sonic logo; voice from `scripts/tts.py` when narrated.
8. **Honest proof.** Real product, real output, real numbers with their source; anything fictional is labelled.
9. **Review before rendering.** Stills at key times and a contact sheet; fix composition there. The renderer's layout check flags text that is too small for a phone (< 1.6 % of the short side), cut off by the frame, or inside the 9:16 zones platform UI covers; mark deliberate exceptions with `data-crop` / `data-small`.
10. **Measure after rendering.** `video_qa.py` passes (frozen time, longest hold, visual sameness, energy floor for trailers, colour range, sync, loudness, captions) and you have looked at its sheet; sound not yet heard by a person is reported as unverified.

### Creative choices (invent for each film)
Concept and metaphor, world and materials, signature device, typography (including custom lettering), motion language, transition family, camera, colour script, structure, sound world, the screenshot moment. The menu and the bible format are in `references/video/video-creative-direction.md`; how each choice is built in this engine is in its §7.

## Workflow
```bash
python score.py                         # or: python score.py --voice ../vo/narration.wav
python render.py stills --ratio 16x9 --times 0.3 2.9 3.1 5 7.2 9.4
python render.py video --ratio 16x9            # also runs the layout check every 0.5 s -> out/layout-16x9.json
python render.py video --ratio 9x16     # layouts adapt via PORT in composition.html
python <skill>/scripts/video_qa.py out/film-16x9.mp4 --captions film.srt --sheet out/qa-sheet.jpg
```
`video_qa.py` must pass (streams, colour range, A/V sync, loudness, **frozen-time and longest-hold limits**, black frames, captions) before the film is presented, and you must look at its contact sheet.

# DENT video kit

The starting point for every **code-built** DENT video (launch films, trailers, explainers, social cuts). It packages the engine and quality invariants behind DENT's own launch film, not its look: every film invents its own direction. Copy this folder into the project (`video/<film>/`), then replace the scenes, tokens and timeline with your film.

| File | What it does |
|---|---|
| `timeline.json` | The single source of timing for picture **and** sound: bpm, fps, scene cuts, events, motion-blur windows, SFX cues, music, narration lines, captions. Field reference: the `score.py` docstring |
| `composition.html` | The film as one HTML page. `render(t)` sets every element for time `t` (deterministic). Engine helpers: easing family, `spring`, `fall` (gravity), `lines()` masked line reveals, `wipe()` transition, grain, captions. **Every scene in it is a placeholder** |
| `techniques.js` | Tested technique modules (`window.DENTFX`): custom lettering, variable-axis kinetic type, hand-made boil, morph, parallax camera + rack focus, glitch, physics (bounce, squash, shockwave), collage (torn paper, halftone), data (count, line chart), Three.js on the film's clock, `loadFonts`, `fitText`, continuous `livingFrame` |
| `techniques.html` | The test bench: every module on one page. `python render.py stills --page techniques --times 0.4 2.3` must render without page errors |
| `styleframes.html` | Four still key frames (hook, signature device, proof, end card) to approve the look **before** animating |
| `render.py` | Headless Chromium → frames → FFmpeg, with a layout check on every review still and every 0.5 s of the film |
| `score.py` | Original, beat-locked score + designed SFX from the timeline (no samples, no licences), narration placement and ducking, mastered to −14 LUFS with true peak ≤ −2 dBTP in the WAV (≤ −1 after AAC). Presets are instruments to shape to the bible's sound world, not a house sound |

Needs Python 3.10+, `pip install playwright numpy`, `python -m playwright install chromium`, FFmpeg.

## The page contract
Any page `render.py` can film (`--page <name>` loads `<name>.html`) must:
1. define `window.render(t)` that sets **everything** from `t` alone: no `Date.now()`, no `requestAnimationFrame` clocks, no CSS animations or transitions left running, seeded randomness only (`DENTFX.rand(seed)`);
2. set `window.READY = true` only after fonts are loaded **and measured** (below) and the first `render` has run;
3. read the frame size from `?w=&h=` (render.py passes it; `?t=` opens a time) and lay out for that shape.

**Fonts.** `document.fonts.ready` can resolve before a face that no element uses yet is fetched, so text measured in the first frame silently uses the fallback. Before measuring, `await DENTFX.loadFonts(['800 1em "Your Face"', 'italic 400 1em "Other"'])` with every face *and weight* you use; it returns any face still missing.

**Fit text once per layout,** not per frame: `DENTFX.fitText(el, maxW, maxH)` after `loadFonts`.

## Layout per ratio (two layouts, not one squeezed)
Portrait is a second composition, not the landscape one shrunk. Keep one layout table per ratio and pick it once:
```js
const SHAPE = H > W ? 'portrait' : H === W ? 'square' : 'landscape';
const LS = { landscape: { title: 160, top: 420 }, portrait: { title: 120, top: 520 }, square: { title: 130, top: 380 } }[SHAPE];
```
Safe zones for 9:16 (shared with `references/video/video-types-and-craft.md` §4): keep text out of the **top 12 %**, the **bottom 20 %**, and the **right action rail** (right 14 % between 45 % and 85 % of the height).

### Layout check (runs on stills and on the film)
| Kind | Means | Opt-out (deliberate only) |
|---|---|---|
| `small` | rendered text under 1.6 % of the short side (transform-aware) | `data-small` |
| `clipped` | a parent with overflow hides part of the text (masks `.line` and `[data-mask]` are exempt) | `data-crop` |
| `cut` | the frame edge cuts the text | `data-crop` |
| `unsafe` | 9:16 text in the top 12 % or bottom 20 % | `data-crop` |
| `rail` | 9:16 text under the right action rail | `data-crop` |
| `overlap` | two separate text runs collide (> 12 % of the smaller one) | `data-overlap-ok` |

## Living frames and the camera
Use **one continuous** drift for the whole film (`DENTFX.livingFrame(stage, t)` or your direction's equivalent: parallax, boil, flicker), not one that restarts each scene; restarting reads as a jolt on every cut. Anything that labels something in the picture (callouts, pinned captions, annotations) must sit **inside** the moving layer or take the same transform, or it slides off what it labels.

## Sound: `score.py`
- Timeline fields: `music` (`from`, `to`, `key_hz`, `progression`, `style`, `drop`, `lift`), `sfx` (`t`, `kind`, optional `dur`, `gain`, `hz`), `vo` (`t`, `file`). Full reference in the `score.py` docstring.
- SFX families: hits, ticks, stabs, impacts, risers (end **on** `t`), and materials: `paper_rip`, `paper_flick`, `riffle`, `glass`, `liquid_drop`, `rain`, `cloth_swish`, `type`, `key`, `thud`, `air`. Pick the family that matches the bible's world; vary them (no whoosh on every cut).
- A film's own sound world: write `score_<film>.py` next to the kit:
  ```python
  import score as K
  K.register_sfx("chalk", lambda e: K.lp(K.rng.standard_normal(int(.2 * K.SR)), 3000) * .3)
  K.register_style("ritual", lambda m, bt, N: ...)   # build with K.fm, K.pluck, K.pad, K.kick, K.taiko, K.reverb
  K.main()
  ```
- Narration: one finished file (`--voice vo/narration.wav`) or each line at its own time (`"vo": [{"t": 0.45, "file": "vo/lines/line_001.wav"}]`); music ducks under the voice.

## Render
```bash
python render.py stills --times 0.3 2.9 5 7.2      # review stills + labelled contact sheet + layout check
python render.py stills --every 1                  # one still per second of the whole film
python render.py video --draft                     # 30 fps, half size, no blur: fast whole-film check -> out/draft-16x9.mp4
python render.py video --from 6 --to 9             # re-render one stretch -> out/range-…mp4
python render.py video --ratio 16x9                # final: 60 fps, motion blur in blur windows, TV-range BT.709
python render.py video --ratio 9x16                # the portrait layout
```
**Render-time budget.** A final render costs about (duration × fps × blur samples in blur windows) frame captures; a 60 s film at 60 fps is 3,600+ frames, typically 10–30 min. Iterate with stills and `--draft`; render the final once per ratio. `render.py` prints an ETA and exits with the failing `t` if `render(t)` throws.

## Measure: `video_qa.py`
```bash
python <skill>/scripts/video_qa.py out/film-16x9.mp4 --kind trailer --captions film.srt \
    --audio out/score.wav --sheet out/qa-sheet.jpg            # add --loop for a looping film
```
It must pass before the film is shown, and you must look at its time-labelled sheet. Thresholds per kind are in `references/video/video-tools-and-pipeline.md` §6.

**Captions without a voice.** A voiceless film still ships an SRT if it has on-screen words that carry meaning (description track): one cue per text card, timed to the card.

## What to keep and what to invent
The engine and the **quality invariants** below are fixed for every film. Everything you can see in the placeholder scenes (the type, the wipe, the numbered chapter, the grey palette) is a **placeholder**: replace it with the direction your film's bible defines (`references/video/video-creative-direction.md` §3). Shipping the placeholders, or DENT's own launch-film devices, fails the originality guard (§4 there).

### Quality invariants (keep, every film, every genre)
1. **A timing grid.** One `timeline.json` drives picture and sound. Events land on a musical grid (`t = n * 60 / bpm`) or on narration word times (`tts.py words`), so sync is exact by construction.
2. **A hook in frame 1.** The first frame already shows something worth stopping for; no fade-up from black.
3. **Density.** Something visible changes at least every 0.5 s outside deliberate holds. Only the end card (≤ 4 s), a loop seam, and silence before a payoff (≤ 1 s) may hold still.
4. **Living frames.** One continuous breath across the film (above).
5. **One transition grammar.** A single family defined by the bible, plus at most one exception at the climax.
6. **Hero moments get physics and motion blur.** Define `blur` windows around every fast move; 60 fps for motion-heavy films.
7. **A system, not decoration.** Type from `scripts/fonts.py`, colour from `scripts/palette.py` (or the brand), one signature device defined in the bible and used throughout.
8. **Designed sound.** A sound for every visual event, a musical or tonal arc, deliberate silence, a sonic logo; voice from `scripts/tts.py`, checked with `tts.py check`.
9. **Honest proof.** Real product, real output, real numbers with their source; anything fictional or concept is labelled, with no invented URLs.
10. **Review before rendering, measure after.** Style frames, then stills and a contact sheet; then `video_qa.py` and a look at its sheet. Sound not yet heard by a person is reported as unverified.

### Creative choices (invent for each film)
Concept and metaphor, world and materials, signature device, typography (including custom lettering), motion language, transition family, camera, colour script, structure, sound world, the screenshot moment. The menu and the bible format are in `references/video/video-creative-direction.md`; how each choice is built in this engine is in its §7.

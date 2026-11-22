# RESULT — S27 trailer run ("Streak", 45 s launch trailer)

Eval run of DENT 2.5.1 from this worktree. Prompt: `/dent:video a 45-second launch trailer for "Streak", a habit-tracking app (iOS + Android) that shows your habits as a growing garden instead of checkmarks. Be as creative as possible.` Scripted answers as given in the task (All-out, "Show me 3 directions" → agent's pick, local voice, code-built visuals, music in code, 16:9 + 9:16). Nothing under `skills/`, `scripts/` or `commands/` was edited.

## What was produced
| Deliverable | Where |
|---|---|
| VIDEO.md: question log with scripted answers, brief, three answers, genre bar, 3 film bibles, choice, originality guard, escalation moves, script, sound, licences | `VIDEO.md` |
| Style frames for the 3 directions (rendered by the kit's `render.py stills`) | `review/styleframe-*.jpg`, `styleframes.html` |
| Film (code-built, 60 fps): 16:9 master and 9:16 cut | `out/film-16x9.mp4` (55.8 MB), `out/film-9x16.mp4` (60.2 MB): not committed (> 20 MB); committed 720p previews in `review/preview-*.mp4` |
| Captions (sidecar + burned in) | `film.srt` |
| Narration (Qwen3-TTS 1.7B, mastered by `tts.py post`) | `vo/` |
| Score + SFX + mix (original, synthesised) | `score_streak.py` → `out/score.wav` |
| `video_qa.py` output for both cuts, layout-check summary, contact sheets | `QA.md`, `review/` |
| Self-review scorecard (sound unverified) | `SCORECARD.md` |

## Where the skill was unclear, missing, contradictory or slow
Ordered by how much each one would change the next result. "Invented" = something I had to make up that the skill should provide.

### Contradictions
1. **Trailer bar vs launch rule.** `video-creative-direction.md` §5 says a trailer's bar is "title at the peak"; `video-types-and-craft.md` §2b [Rule] says a product launch film/trailer must show "name and promise by ~9 s". For a *launch trailer* both apply and they pull opposite ways. Invented resolution: name small and early (root-drawn wordmark at 7.5–9.2 s), title again at full size at the peak (28.75 s). The skill should state this resolution (or which wins).
2. **Product truth ≥ 60 % vs the trailer genre.** §2b demands ≥ 60 % of screen time on the real product; a trailer's bar is rhythm, rising stakes and a twist, which needs non-UI beats (cold open, turn, climax). My first cut measured 51 % strictly. I only got to ~67 % by re-dressing the climax as the app's own "Roots" tab (adding its tab chrome). It's unclear whether a stylised full-frame view of an app screen counts as "the product itself". The rule needs a definition (what counts, and does it bend for trailers/teasers?).
3. **All-out asks for things this run was told not to do / can't do.** SKILL §8 + `all-out.md`: All-out = three *independent* evaluators, improve rounds until ≥ 9 with no line < 8, 1:1 cut, thumbnail, DESIGN.md. The eval brief asked for a self-review SCORECARD. With no person to answer, I logged the evaluators as not run. The skill doesn't say what All-out means in a non-interactive run, or how to get independent review without spawning agents.
4. **"Ask one question at a time" vs a non-interactive run, with no defaults for the video gates.** SKILL §1.2 says non-interactive runs use "documented defaults", but the video-specific gates have none: script approval (video.md step 5), "the user picks or combines" directions, "Anything you never want?" (menu F is skipped entirely when the gate answer is "Show me 3 directions", so the Never rule has no source), commercial use (voice §1.2). I logged each as a default in VIDEO.md §0. A short "non-interactive video defaults" list would remove the guessing.

### Missing or unclear
5. **Which SKILL.md "every visual build" questions apply to video?** §1.2 says every visual build at Standard+ asks about built-in surfaces and the motion menu; the All-out capability list (`all-out.md` §0) is written for pages (surfaces, responsive widths, favicon, OG image). For a video most rows are N/A, but the skill doesn't say so, so an agent either asks irrelevant questions or silently drops rows (which §0 rule 2 counts as a failed All-out). Invented: N/A rows with reasons.
6. **Fictional / concept products aren't covered.** The skill assumes a real product with a real URL or install command ("exact install command or URL held ≥ 2 s"). Streak has none. I had to invent the product's fictional spec (VIDEO.md "Product facts"), the demo-label wording and where it shows, and a CTA without a link ("On iPhone and Android"), and decide not to use store badges (trademarks). One paragraph in §2b would cover concept films and spec pitches.
7. **Placing narration lines on the beat isn't supported.** `tts.py post` places lines back to back with a fixed `--gap`; the kit's `score.py --voice` mixes one finished WAV. A trailer needs each line at a chosen time (on the grid, after a hit). Invented: `make_timeline.py` (line start times + caption cues from `narration.timing.json`) and slicing `narration.wav` per line inside `score_streak.py`. A `post --at 0.45,2.95,…` option or a `vo` block in `timeline.json` that `score.py` reads would make this standard. Captions had the same gap: the kit draws cues from `timeline.json` but nothing generates them from the narration timing, and nothing splits > 42-character lines.
8. **The kit's score is one preset for the whole film.** `score.py` arranges one `style` (pulse/cinematic/playful/minimal) from `music.from` to `music.to`. A trailer's sound world changes per act (here: dry clinical → organic → silence → full → dawn). The README says "shape the presets to the bible" but not how. I wrote `score_streak.py`, which imports the kit's instruments (`import score as K`) and builds its own arrangement. That worked well; the README should say it's the intended path and show the import.
9. **The kit invites the genre's top cliché.** The kit's sample `timeline.json` puts a `whoosh` on every scene cut, and the trailer cliché list says "whoosh on every cut". My first score copied the habit (four transition whooshes). I only caught it by inspecting the spectrogram. Suggest the sample timeline use a different, non-cliché transition sound, and `video_qa.py` could flag broadband transients at every scene boundary.
10. **`livingFrame()` assumes hard cuts.** It restarts its push at each scene start (`scale 1 + .012 × (t − sceneStart)`), so on any film whose transitions are continuous (this one: camera moves through a horizon, no cuts) the camera visibly pops at every scene boundary. I replaced it with a continuous breathing camera. The README should say: continuous-transition films need a continuous living frame.
11. **Style frames: no template.** §3 asks for "one rendered style frame per direction", but the kit only renders pages that expose `render(t)` + `READY`. I built `styleframes.html` (three frames selected by `t`). A tiny `styleframes.html` starter in the kit would save time and keep the frames honest (same fonts and engine).
12. **9:16 from the same composition is under-specified.** The README says "layouts adapt via PORT". In practice the vertical cut needed its own layout for every scene: statements moved into the soil band, roots squashed, captions moved to 0.785 H, the widget moved, the phone shrunk for the top safe zone. Nothing in the kit shows a two-layout pattern (I used one `LS` layout object per ratio). The platform cut is the second deliverable, so a worked pattern matters.
13. **Whisper pronunciation check can't run, and nothing says to install it.** `video-tools-and-pipeline.md` §6 requires a speech-to-text pass on every line ("DENT" was read as "PEN"); `doctor.py` reports "whisper: not found" but neither `video.md` nor `voice-and-narration.md` says how to install it or what to do without it. Not run; reported in QA.md.
14. **MWG step for a render-only page.** video.md says to run the Modern Web Guidance procedure before writing HTML. For a page that only Chromium screenshots frame by frame, nothing in MWG applies (search returned font-loading/stagger guides). The skill could say "render-only compositions: MWG N/A, log it".
15. **Render time isn't mentioned anywhere.** About 100 frames/min at 1080p (my composition rebuilds plant SVGs every frame), so ~45 min per 45-s cut at 60 fps with motion-blur windows. That matters for planning (stills review first, improve rounds, two ratios). `render.py` has no parallelism, no `--fps 30` draft mode, no resume, and no start/end range for re-rendering a fixed scene. I restarted renders twice and ran the two ratios as parallel processes.

### Tool bugs (found, worked around, not fixed)
16. **`render.py stills` crashes on Windows** when the layout check prints text with a non-cp1252 character (`●`, `’`): `UnicodeEncodeError: 'charmap' codec…` from the `print` of the issue line. Workaround: `PYTHONIOENCODING=utf-8`. Fix: `sys.stdout.reconfigure(encoding="utf-8", errors="replace")`.
17. **Layout check false positives and blind spots.**
    - It ignores ancestor `overflow:hidden`. Text in a phone screen's off-canvas pane (clipped, invisible) is reported as "cut".
    - It reads computed `font-size`, which ignores transforms. Text inside a phone scaled to 0.78 passes at 18 px while rendering at ~14 px. Text scaled up is judged too small.
    - `data-crop` is documented as a static marker. Deliberate crops that only happen during a transition need it toggled per frame (I did that with `toggleAttribute`); the README doesn't mention this.
    - The message "px 17, min 17" is rounding noise (17 < 17.28).
18. **`palette.py` prints nothing when there's no cliché hit**, so you can't tell "clean" from "not checked". A "cliché check: none" line would make the evidence visible.

### What worked well
- `fonts.py suggest/check` and `palette.py make` gave a fresh, contrast-checked system in two commands. The originality guard's explicit device list made the guard quick to run and to evidence.
- The film bible format forced real differences between directions (all eight axes differ for every pair).
- The kit's engine (deterministic `render(t)`, `morph()`, `shockwave()`, motion-blur windows, TV-range encode) needed no changes. The still-sheet loop caught real problems before the render: dark empty frames at the climax, an off-centre wordmark, round-cap dots on undrawn strokes, a title colliding with its tagline, overlaps in the vertical cut.
- `tts.py say/post` with Qwen3-TTS produced all ten lines in one run and mastered them (−16.1 LUFS PASS).

### Small things noticed while measuring
19. **`video_qa.py` rhythm line can't tell a continuous film from a slow one.** "0 shot changes, longest shot 45 s" is reported as info. This film has no hard cuts by design (the camera travels through the horizon), yet the trailer bar is "rhythm". The energy (20.7) and variety (5.5 s) checks carried the real signal. Worth noting in the doc so an agent doesn't add cuts just to move that number.
20. **Round 1 failed `video_qa` on caption length.** My own cue builder produced one 47-character line. The kit's caption path has no wrap step (see #7), so every film built from `timeline.json` cues can hit this.
21. **Process cost.** The skill's loop is sound, but at All-out it took three renders (≈ 25 min each with both ratios in parallel), roughly ten still-sheet rounds and one improve pass to reach a clean QA. A draft-render mode (30 fps, no blur, half size) would cut the middle loop a lot.

## Honest status
- **Measured:** `video_qa.py` passes every check on both cuts in the final round. Frozen 1 % / 0 %, energy 20.7 / 21.0, −14.4 LUFS, captions OK (QA.md).
- **Layout check:** 16:9 clean. 9:16 has 6 flags, all judged false positives (the clip blind spot, #17).
- **Self-review:** 8.1 / 10. That meets DENT's default target but **not the All-out target** (≥ 9, no line < 8).
- **Unverified:** sound was never heard by a person (Sound and Voice capped at 6), and no Whisper check was run.
- **Not done:** no independent evaluators were run.
- **Product truth:** 67 % only if the Roots-tab climax counts, 51 % strictly.

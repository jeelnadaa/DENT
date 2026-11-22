# QA: Streak trailer ("Roots")

Final render (round improve-2), 2026-11-22. Commands run from this folder:
`python ../../../skills/dent/scripts/video_qa.py out/film-<ratio>.mp4 --captions film.srt --kind trailer --sheet review/qa-sheet-<ratio>.jpg`

Full-quality films (60 fps, CRF 16) are `out/film-16x9.mp4` (55.8 MB) and `out/film-9x16.mp4` (60.2 MB). They are not committed (over 20 MB). Committed 720p/30 fps previews: `review/preview-16x9-720p.mp4`, `review/preview-9x16-720p.mp4`. Poster: `review/poster-16x9.jpg`.

## video_qa.py: 16:9 master (exit 0)
```
DENT video QA: film-16x9.mp4
  ok    video codec h264
  ok    pixel format yuv420p (yuv420p; yuvj420p means full-range JPEG frames were piped in)
  ok    colour range tv (TV/limited)
  ok    constant frame rate (60/1)
  ok    audio codec aac
  ok    A/V durations 45.00 s / 45.00 s
  ok    loudness -14.4 LUFS (target -14.0 ± 1)
  ok    true peak -1.8 dBTP (≤ −1)
  ok    motion: 0.5 s of 41.0 s frozen (1 %, limit 20 % for a trailer)
  ok    motion: longest frozen hold 0.5 s (limit 2.5 s; closing 4.0 s end card excluded)
  ok    variety: longest visually-unchanged stretch 5.5 s (limit 6.0 s for a trailer)
  ok    energy: mean picture change 20.7/255 per second (floor 15.0 for a trailer; DENT's launch film: 35)
  info  rhythm: 0 shot changes (0/min), longest shot 45.0 s
  ok    no unintended black frames (0 found)
  ok    captions: 12 cues in film.srt
  ok    captions: every line ≤ 42 characters
  ok    captions: ≤ 2 lines per cue
  ok    captions: every cue ≥ 1 s
  ok    captions: every cue inside the film
  info  contact sheet (one frame every 2.8 s): review\qa-sheet-16x9.jpg  ← look at it
  note  taste, message and product truth are not measured here: look at the sheet and watch it with sound off and on

All measured checks passed
exit 0
```

## video_qa.py: 9:16 cut (exit 0)
```
DENT video QA: film-9x16.mp4
  ok    video codec h264
  ok    pixel format yuv420p (yuv420p; yuvj420p means full-range JPEG frames were piped in)
  ok    colour range tv (TV/limited)
  ok    constant frame rate (60/1)
  ok    audio codec aac
  ok    A/V durations 45.00 s / 45.00 s
  ok    loudness -14.4 LUFS (target -14.0 ± 1)
  ok    true peak -1.8 dBTP (≤ −1)
  ok    motion: 0.0 s of 41.0 s frozen (0 %, limit 20 % for a trailer)
  ok    motion: longest frozen hold 0.0 s (limit 2.5 s; closing 4.0 s end card excluded)
  ok    variety: longest visually-unchanged stretch 5.2 s (limit 6.0 s for a trailer)
  ok    energy: mean picture change 21.0/255 per second (floor 15.0 for a trailer; DENT's launch film: 35)
  info  rhythm: 0 shot changes (0/min), longest shot 45.0 s
  ok    no unintended black frames (0 found)
  ok    captions: 12 cues in film.srt
  ok    captions: every line ≤ 42 characters
  ok    captions: ≤ 2 lines per cue
  ok    captions: every cue ≥ 1 s
  ok    captions: every cue inside the film
  info  contact sheet (one frame every 2.8 s): review\qa-sheet-9x16.jpg  ← look at it
  note  taste, message and product truth are not measured here: look at the sheet and watch it with sound off and on

All measured checks passed
exit 0
```

## Renderer layout check (sampled every 0.5 s during `render.py video`)
- 16:9: `layout check (every 0.5 s): 0 too small, 0 cut off, 0 in unsafe zones -> clean`
- 9:16: `layout check (every 0.5 s): 0 too small, 0 cut off, 6 in unsafe zones -> see out/layout-9x16.json and fix before delivery`
  - All 6 flags are "No reset." at 20.0–22.5 s. The line sits under its line mask (`overflow: clip`, translated 140 px down) before it rises at 22.5 s, so it is invisible while flagged. The checker ignores ancestor clipping (RESULT.md #17). From 23.0 s on its glyphs sit at 1265–1450 px, inside the safe area. **Judged a false positive**; details in `out/layout-9x16.json`.
- Deliberate crops (phones entering and leaving, the push through the screen) are marked with `data-crop`, toggled per frame.

## Contact sheets looked at
- Before rendering (stills review, several rounds): `out/stills/_sheet-*.jpg`. Problems found and fixed there:
  - empty dark frames at 25.0–26.3 s
  - wordmark off-centre (flex overridden)
  - round-cap dots on undrawn strokes
  - invisible leaf on the k
  - title overlapping its tagline
  - dawn phones colliding with the statement
  - 9:16 roots over the statements
  - 9:16 widget hidden under the soil
  - weak wilt
- After rendering: `review/qa-sheet-16x9.jpg`, `review/qa-sheet-9x16.jpg` (one frame every 2.8 s). Round-1 sheets led to improve-2:
  - counter drawn 1.5× for 0.18 s at the start (a real unsafe-zone flag)
  - 9:16 caption over the hook grid
  - dark garden labels
  - "No" label truncation
  - caption line > 42 characters (the round-1 `video_qa` FAIL)
- Known nits left: the "Walk 20 min · 47 days of roots" label crosses root lines at 26–28 s. "On iPhone and Android" overlaps the fading grid for ~1 s at 40.5–41.5 s.

## Other checks
| Check | Result |
|---|---|
| ffprobe streams, colour range, sync, loudness | Passed (above) |
| Frozen time / longest hold | Passed: 1 % / 0.5 s (16:9), 0 % / 0 s (9:16). The 0.5 s is the deliberate stillness before the climax (24.40–24.95 s) |
| Product truth ≥ 60 % | 67 % counting the Roots-tab climax (app chrome on screen); 51 % strictly. See VIDEO.md §1 |
| Three-question test, sound off | Agent's own check on the sheets: what (habit app "Streak", 8.6 s), what for me (grow, wilt, no reset), how (iPhone + Android). Not tested on a stranger |
| Narration pronunciation (speech-to-text) | **Not run**: Whisper not installed (`doctor.py`: "whisper: not found") |
| Sound heard by a person | **Not run, unverified**. Spectrogram and waveform inspected: `review/score-spectrum.png`, `review/score-wave.png` |
| Flashing > 3/s | Passed by construction: no strobes; one shockwave ring and one impact fade |
| Captions | `film.srt` 12 cues, burned into both cuts; text matches the script; spell-checked by reading |
| 1:1 cut, thumbnail | 1:1 N/A (platforms answer named 16:9 + 9:16); poster frame exported |
| Independent evaluators | Not run (self-review only) |

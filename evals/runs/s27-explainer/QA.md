# QA: "Signed, Not Said" (film-16x9.mp4)

## video_qa.py (final render)
`python skills/dent/scripts/video_qa.py film-16x9.mp4 --kind explainer --captions film-16x9.srt --sheet qa-sheet.jpg --json out/qa.json`
```
DENT video QA: film-16x9.mp4
  ok    video codec h264
  ok    pixel format yuv420p (yuv420p; yuvj420p means full-range JPEG frames were piped in)
  ok    colour range tv (TV/limited)
  ok    constant frame rate (60/1)
  ok    audio codec aac
  ok    A/V durations 63.50 s / 63.49 s
  ok    loudness -14.0 LUFS (target -14.0 ± 1)
  ok    true peak -1.7 dBTP (≤ −1)
  ok    motion: 0.9 s of 59.5 s frozen (2 %, limit 35 % for a explainer)
  ok    motion: longest frozen hold 0.9 s (limit 4.0 s; closing 4.0 s end card excluded)
  ok    variety: longest visually-unchanged stretch 7.8 s (limit 10.0 s for a explainer)
  info  energy: mean picture change 11.0/255 per second (DENT's launch film: 35)
  info  rhythm: 0 shot changes (0/min), longest shot 63.5 s
  ok    no unintended black frames (0 found)
  ok    captions: 13 cues in film-16x9.srt
  ok    captions: every line ≤ 42 characters
  ok    captions: ≤ 2 lines per cue
  ok    captions: every cue ≥ 1 s
  ok    captions: every cue inside the film
  info  contact sheet (one frame every 4.0 s): qa-sheet.jpg  ← look at it
  note  taste, message and product truth are not measured here: look at the sheet and watch it with sound off and on

All measured checks passed
```

### First render failed (kept for the record: `out/qa-render1.txt`)
```
  FAIL  variety: longest visually-unchanged stretch 26.8 s (limit 10.0 s for a explainer)
  info  energy: mean picture change 10.4/255 per second (DENT's launch film: 35)
```
Cause: scenes 4–7 (16.3–43.2 s) all sat on the same indigo ground with thin light strokes, so at thumbnail scale the whole mechanism section looked like one picture. Fix (inside the bible's colour script): the night ground steps per handshake beat — L4 `#0D224A` → L5 `#1F448D` → L6 `#16336C` → L7 `#0D224A`; small magenta text on the lighter grounds moved to `#FFB0C6` (5.41:1) and the "illustration" label to `#8C9BB8` (5.57:1), both checked with `contrast.py`. Pre-checked with 1 s stills (longest stretch ~7 s), then re-rendered.

## Layout check (render.py, every 0.5 s)
```
layout check (every 0.5 s): 0 too small, 0 cut off, 0 in unsafe zones -> clean
```
`out/layout-16x9.json` is `[]`. One element is marked `data-small` deliberately: the 18 px "illustration · not a real key" disclaimer (a footnote, not content).

## Narration checks
| Check | Result |
|---|---|
| STT per line (faster-whisper small.en), take 1 | 7.2 % WER; inserted "Haha" (line 3), inserted gibberish phrase (line 6), "Pascy" for passkey (line 8); 73 s at 2.3 words/s. Rejected. |
| STT per line, take 2 | 3.6 % WER; "Sights" (homophone, kept), "past ski" for passkey (line 8). Line 8 re-rendered with the respelling "pass-key" + `[pause 0.6]`, seed 23: heard "Each passkey is bound to the real site's domain, a lookalike gets nothing." |
| STT on the final mixed film (music + SFX + voice) | Every line recovered; only miss "You can check" for "It can check" (homophone-level). Music ducking does not mask words. |
| Narration master (`tts.py post`) | 59.91 s, −16.0 LUFS, true peak −1.5 dBTP → PASS; 13 caption cues |
| Film mix | −14.0 LUFS, −1.7 dBTP (video_qa) |
| Silence before the payoff (46.3–47.1 s) | mean −20.1 dB vs −15.5 dB in the sign-in scene: a dip, **not** near-silence (the cut hit and music tail fill it). Weaker than the bible intends. |
| Listened by a person | **No.** Nobody heard the voice, score or SFX. Sound is unverified. |

## Contact sheets I looked at
- `contact-sheet-1s.jpg`: one still per second of the final composition (0–60 s), reviewed before the second render.
- `qa-sheet.jpg`: video_qa's sheet of the rendered film, one frame every 4 s.

What I saw (fixed before the final render): the pen line drifting off the phone outline as the camera pushed in (the overlay was outside the camera layer); the pen ellipse reappearing around the lookalike domain; one-line ~80-character burned-in captions; the colour script not running at all in the first stills (a colour-mixing bug); kinetic phrases colliding with the caption band.

What I saw and did **not** fix:
- Scenes 5–7 reuse the same layout (phone left, card right, wire between). Each adds new information and now has its own ground tone, but it's close to the explainer cliché "same shot repeated".
- In the dissolve into the sync scene (~48.8 s) the fading lookalike domain ghosts faintly over the daylight background for a few frames.
- The flying public-key string overshoots the site card for ~0.2 s (~30.5 s).
- Mid-act mono labels in the cards (22–24 px) are legible at 1080p but small on a phone (they pass the 1.6 % rule).
- Energy is 11/255 per second (launch film 35). Fine for "calm and precise", but the film is gentle rather than striking outside the title, the climax and the end card.

## Files
`film-16x9.mp4` (23.9 MB master, not committed: > 20 MB) · `film-16x9-preview.mp4` (8.3 MB, CRF 25 re-encode of the master, committed) · `film-16x9.srt` / `.vtt` · `vo/narration.wav` · `out/score.wav` · `out/qa.json`.

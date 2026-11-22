# Video Plan: Daybreak, "Tear-Off Day" (20 s vertical social short)

> DENT video plan (`/dent:video`, Polished). Eval run S27 (vertical short). Code-built with the DENT video kit copied into this folder. Source of timing: `timeline.json` (picture and score both read it).

## 0. Session notes: questions the skill told me to ask (nobody could answer; scripted answers used)
| # | Question (as the skill says to ask it) | Options offered | Scripted answer |
|---|---|---|---|
| Q0 | How far should I take it? (or answer "you decide" to skip all questions) | Essential · Standard (Recommended) · Polished · All-out | **Polished** |
| Q1 | Type and platform? / length? | Social short; 9:16 · 16:9 · 1:1; 15 / 20 / 30 s | Given in the prompt: vertical social short, 20 s. **9:16 (1080×1920) only, sound-off first** |
| Q2 | Where should each kind of media come from? Footage/imagery: code-built (Recommended) · local generative model · free cloud tier · paid provider · your own. ("A real photo of the Daybreak bag or a roast-date label would make the payoff land harder; do you have one, or should I build it in code?") | — | **Code-built in the browser; no generative imagery, no stock photos** |
| Q3 | Sound (menu E): Narration + score + SFX · Score + SFX, no voice · Sound design only · Silence and a few hits | — | **Score + SFX, no voice** |
| Q4 | Music source: made in code (Recommended, no licence) · library track · generative provider · your own | — | **Made in code** (`score.py`) |
| Q5 | Creative menu gate: How do you want to shape the film's look and feel? Show me 3 directions (Recommended) · Let me pick the ingredients · You decide everything · I have references | — | **You decide everything** (so groups A–F were not asked; Never = none given) |
| Q6 | Script approval (command step 5) | Approve · change | No one to approve; I approved it myself after reading it aloud with a timer (logged as agent judgment) |

`doctor.py`: Windows, Python 3.11, Node 26, FFmpeg full build, Playwright Chromium 159, RTX 3070 Ti, 4 local TTS engines (unused: no voice), no API keys. Nothing blocking.

## 1. Brief
- **Type and sub-type:** Social short → hook-first vertical, loopable.
- **Audience and where they'll watch:** coffee drinkers scrolling Reels / TikTok / Shorts on a phone, **sound off by default**.
- **One message:** Daybreak coffee was roasted yesterday, not some day nobody remembers.
- **Call to action:** "Subscribe · link in bio". No URL was given and Daybreak is fictional, so I did not invent a domain; "link in bio" is the native CTA of the platforms this ships to.
- **Length and aspect ratio:** 20 s, 9:16, 1080×1920, 60 fps.
- **Mood words:** witty, crisp, wide-awake. **Anti-words:** cosy, rustic.
- **Creative concept:** a tear-off desk calendar. Tearing pages digs back through the months your coffee might have been sitting; Daybreak's page says *yesterday*.
- **Must show:** the product promise (beans roasted the day before they ship), the name, the CTA. **Must not show:** reviews, ratings, customer counts, delivery-time promises (not given), competitor brands, claims about what other bags print.
- **Assets available:** none (fictional brand). Everything is built in code.

### Three answers with sound off (video-types-and-craft.md §2b, adapted: a consumer subscription, not software)
- **What is it?** Daybreak, a coffee subscription (on screen 13.0–20 s; name from 6.7 s).
- **What does it do for me?** Sends beans roasted the day before they ship ("Roasted yesterday. Shipped today." 10.4–13 s, and the brand page line).
- **How do I get it?** Subscribe, link in bio (16.3–19.3 s, held 3 s).
- Product-truth share: §2b's "≥ 60 % real UI" rule is written for software; Daybreak has no UI or product footage, and stock/generative imagery was refused. The product here *is* the promise, so the film is the promise staged. Logged as a gap in RESULT.md.

### Genre bar (video-creative-direction.md §5, Social short)
"A hook in frame 1 with sound off, a loop or payoff by 15 s, vertical-native composition." Clichés to avoid: landscape cut cropped to vertical, intro titles.
How this film meets it: frame 1 is already a full question ("When was your coffee roasted?" over a giant "?") · payoff by 10.4 s ("Roasted yesterday. Shipped today.") · the last 0.7 s tears the end card off to reveal frame 1, a seamless loop · composed only for 9:16 (a tall desk-calendar pad that only works upright).

### Category clichés named and avoided (SKILL.md §1.4 / G9)
Coffee ads: steam curls, latte-art pours, slow-motion falling beans, kraft-brown and cream palette, sunrise-orange gradient (tempting with the name "Daybreak"), hands around a mug at a window. This film has none: no coffee imagery at all, a cobalt and paper palette, the joke carried by a desk calendar.

## 1b. Creative direction

### Creative menu answers
"You decide everything." No groups asked; my choices are logged in the chosen bible. Never list: none given by the user; my own never list is in the bible.

### Directions offered (Polished = 2 bibles, each with a rendered style frame)

**Direction A: Tear-Off Day** (style frame: `out/stills/9x16-007.80.jpg`, see `out/stills/_sheet-9x16.jpg`)
```
NAME:              Tear-Off Day
LOGLINE:           A desk calendar that tears its own pages backwards through the months your coffee might have
                   waited, then snaps forward and stops on Daybreak's page: yesterday.
WORLD & MATERIAL:  a tear-off calendar pad on a dark desk, top-down. Thin paper: it peels, rips at the perforation,
                   is thrown up and falls with gravity and spin; old pages are yellowed and faded.
SIGNATURE DEVICE:  the page tear. Every change of state is a page torn off the pad; the width axis is age: old dates
                   slump wide and squat, fresh pages stand tall and condensed (and breathe on the width axis).
TYPE:              Anybody (variable wdth 50–150, wght) for dates and the big words; Zalando Sans for labels and the
                   caption line above the pad. Old dates set wide (wdth up to 150) and greying; fresh words condensed (wdth 50–62),
                   breathing per line; TODAY stands up from a squash; the wordmark letters drop in on 1/8 notes.
MOTION LANGUAGE:   Physical (thrown paper: g = 5200 px/s², spin, 3D peel on rotateX) + mechanical rhythm (tears land
                   on 1/4 → 1/8 → 1/16 notes, accelerating into a riffle). 60 fps, motion blur on every flight.
TRANSITIONS:       one family: tear-off. Exception at the climax: the slow hero tear of YESTERDAY (0.4 s peel to 70°,
                   camera pushes in on the torn edge).
CAMERA:            locked top-down on the pad; slow living drift; one push-in at the climax tear.
COLOUR SCRIPT:     act 1 paper-white with a cobalt "?" → act 2 pages yellow and fade as they get older (dusty
                   desaturation) → act 3 one full-bleed cobalt page (the only saturated field in the film) → paper
                   with cobalt ink → cobalt end card → back to paper-white (loop).
SOUND WORLD:       paper: rips, flicks, a reverse riffle rush, a soft landing thud; a plucked, playful 120 bpm groove
                   that speeds with the riffle, drops to near-silence for 1 s, then opens up in a major key; sonic logo
                   = three rising plucks + a bell.
STRUCTURE:         hook 0–1.5 · dig back 1.5–5.5 (tears accelerate) · silence 5.5–6.6 · reversal 6.6–7.5 (pages fly
                   back on) · reveal YESTERDAY 7.5–10.4 · hero tear → TODAY 10.4–13 · brand 13–16 · end card 16–19.4 ·
                   loop tear 19.375–20 (loop caption from 19.0).
THE MOMENT:        the cobalt YESTERDAY page slamming down after the riffle.
NEVER:             coffee imagery (steam, beans, mugs, latte art), brown/kraft, sunrise gradients, invented proof
                   (reviews, ratings, counts), claims about other brands' bags, intro titles.
```

**Direction B: Long Drop** (style frame: `out/stills/styleB-*.jpg`, see `out/stills/_sheet-styleB.jpg`)
```
NAME:              Long Drop
LOGLINE:           One bean falls the whole height of the phone, like a scroll that won't stop: from the roaster's
                   drum through the night to a doorstep, and a clock in the margin counts the hours it took.
WORLD & MATERIAL:  cut-paper night-time diorama in layers (drum, cooling tray, bag, van, door), deep parallax.
SIGNATURE DEVICE:  the margin clock: a thin vertical ruler down the left edge whose hour marks scroll past as the bean
                   falls; it stops at "+24 h".
TYPE:              one serif display face set huge and vertical in the margin; minimal type elsewhere.
MOTION LANGUAGE:   Cinematic camera (one continuous downward travel) + liquid ease (no impacts until the landing).
TRANSITIONS:       none: one impossible continuous shot; one hard cut to the end card.
CAMERA:            travelling vertically, 2.5D parallax.
COLOUR SCRIPT:     deep indigo night → violet → a single lit doorway.
SOUND WORLD:       a long falling tone (Doppler), wind, soft cinematic taiko, the landing as the only hit.
STRUCTURE:         one shot: drop 0–15 (stations every 3 s) → land → end card 15–20.
THE MOMENT:        the bean passing the "+24 h" mark as it lands.
NEVER:             same as A.
```

A and B differ on world (paper calendar vs night diorama), signature (tear vs margin clock), type (wide/narrow sans dates vs vertical serif margin), motion language (physical throws vs continuous camera), camera (locked vs travelling), colour script (paper → dusty → cobalt vs indigo night → lit doorway), sound world (paper rips + plucked groove vs falling tone + taiko), structure (dig back → reversal → loop vs one continuous drop). Eight of eight axes.

### Chosen: A, Tear-Off Day (agent judgment, "you decide everything")
Why: it stops the scroll in frame 1 with a question a muted viewer reads instantly; it pays off by 10 s; it loops by construction (the last tear reveals frame 1); it is vertical-native (a calendar pad is a portrait object); and its metaphor comes from outside the coffee category. B's continuous fall withholds the point until ~15 s, which is late for a scroll-stopper, and a night-time diorama drifts towards the cosy look the brief should avoid.

### Escalation moves (§6) and where they land
1. **Silence before the payoff** at 5.5–6.6 s: the riffle stops dead, one old page hangs and flutters, the music drops out; then the pages fly back.
2. **The reversal** at 6.6–7.5 s: the thing that was digging into the past (tearing) runs backwards and becomes the answer: pages land forward in time until Daybreak's page slams down.
3. **Callback / loop** at 19.3–20 s: the end card tears off and reveals the opening "?" page, so the end answers and restarts the first frame.

### Originality guard (§4) result: PASSED, with one note
- **Not DENT's devices:** no orange dot, no dot or circle wipe (the kit's placeholder wipe was deleted), no letterpress strike, impression or stamping (pages are torn and thrown, never pressed), no wall of identical templates, no split-flap board, no numbered "It asks / It names / It checks" chapters, no "made with" ending. **Note:** a riffle of calendar pages is a cousin of a split-flap board (dates flipping by). I kept it distinct: pages are torn off and thrown by physics, never hinged flaps flipping in place, and there is no board, no mechanical clatter.
- **Not the genre's clichés:** no intro title (frame 1 is the hook), no landscape crop (9:16 only). Coffee clichés: none (list above).
- **Not the previous film** (read `video/launch/VIDEO.md` only, no media): world desk calendar vs letterpress sheet · signature tear-off vs dot strike · type Anybody/Zalando Sans vs Geist/Instrument Serif · motion thrown paper + accelerating riffle vs impact/shockwave · camera locked top-down vs flat stage · colour paper→dusty→cobalt vs paper/ink/orange · sound paper rips + plucked groove vs letterpress thunks + marimba · structure question→dig→reversal→loop vs problem→strike→reveal→chapters→CTA. Differs on 8 axes. One shared material (paper) is noted.
- **Within the brand:** Daybreak has no DESIGN.md (fictional); the identity is created here: cobalt from `palette.py make --hue 262 --chroma 0.2 --neutral warm`, type from `fonts.py`.

## 2. Tools
| Media | Source | Model or provider + version | Cost | Licence / commercial OK | Consent |
|---|---|---|---|---|---|
| Footage / imagery | code-built (HTML/CSS/SVG in headless Chromium) | DENT video kit (this folder) | 0 | Apache-2.0 (kit) / output ours | n/a |
| Voice | none (user choice) | — | — | — | — |
| Music | made in code | `score.py` (kit, shaped: `paper` SFX added) | 0 | original synthesis, no samples | n/a |
| SFX | made in code | `score.py` | 0 | original synthesis | n/a |

- **How it is made:** render (code-built), because the user ruled out generative and stock imagery and the idea is typographic.
- **Build tool:** DENT video kit (engine, timeline grid, render.py motion blur + layout check, score.py).
- **Licences:** Anybody (Tyler Finck, SIL OFL 1.1, Google Fonts) · Zalando Sans (SIL OFL 1.1, Google Fonts; `fonts.py check` "fresh enough", licence not `--verify`-ed online) · kit code Apache-2.0 · Playwright Apache-2.0 · FFmpeg LGPL/GPL (tool only).

## 3. Script (on-screen text; no voice). Read aloud with a timer: every line fits its hold (0.5 s + 0.3 s/word).
| # | Time | Caption line (above the pad) | Page on the pad | Sound |
|---|---|---|---|---|
| 1 | 0.0–1.5 | When was your coffee roasted? | "ROASTED ON" · giant cobalt "?" wobbling on the beat | plucked groove starts, tick on each wobble |
| 2 | 1.5–2.9 | (same) | tear, tear, tear, tear on the beat: 12 NOV, 03 NOV, 27 OCT, 14 OCT | rip per tear |
| 3 | 2.9–4.4 | Three weeks ago? | tears on 8ths: SEP, SEP, SEP, AUG, AUG, pages yellowing, dates narrowing | flicks, groove denser |
| 4 | 4.4–5.5 | Three months? | riffle on 16ths back to 22 APR | flick stream, riser |
| 5 | 5.5–6.7 | Who knows. | riffle stops; 22 APR hangs half-peeled, fluttering | near-silence, one paper flutter |
| 6 | 6.7–10.4 | Unless it's Daybreak. | pages fly back on, forward in time (MAY→NOV), then the cobalt page slams down: ROASTED · YESTERDAY | reverse rush, thud on 7.5, groove opens in major |
| 7 | 10.4–13.0 | Roasted yesterday. Shipped today. | hero tear (camera pushes in) → paper page: SHIPPED · TODAY | long rip, lift |
| 8 | 13.0–16.0 | A coffee subscription. | tear → cobalt page: "daybreak" wordmark builds letter by letter; "Beans roasted the day before they ship." | flick per letter |
| 9 | 16.0–19.0 | Coffee with a birthday. | end card: wordmark + line + "Subscribe · link in bio" | sonic logo |
| 10 | 19.0–20.0 | When was your coffee roasted? | 19.375: end card tears off, revealing the "?" page of frame 1 (loop) | rip |

## 4. Storyboard
Stills at every key time were rendered and reviewed as a contact sheet before the full render (`out/stills/_sheet-9x16.jpg`); that sheet doubled as the animatic (timing was then checked in the full render).

## 5. Animatic
Timing locked on the 120 bpm grid in `timeline.json` (tears on 1/4, 1/8, 1/16 notes; landings on 1/16 notes).

## 6. Sound
- Narration: none.
- Music: original, made in `score.py` (`playful` arrangement shaped: G major-ish pluck groove, drop 5.5–6.6, lift at 7.5).
- SFX palette (added to this film's copy of `score.py`): `rip` (paper tear), `flick` (page flick), `rush` (reverse riffle), `thud` (paper landing), `tick`, `logo`.
- Mix: −14 LUFS integrated, true peak ≤ −1.5 dBTP (measured by `score.py` and `video_qa.py`). **Not heard by a person.**

## 7. Captions
No speech. All meaning is in burned-in on-screen type (the caption line above the pad + the page). `film.srt` mirrors every on-screen line for accessibility and platform caption tracks.

## 8. Export
| Version | Resolution | FPS | Codec / container | Loudness | File |
|---|---|---|---|---|---|
| 9:16 | 1080×1920 | 60 | H.264 yuv420p TV-range BT.709 / AAC 256k, MP4 faststart | −14 LUFS | `film-9x16.mp4` |

## 9. QA (final render, 2026-11-22)
`python skills/dent/scripts/video_qa.py film-9x16.mp4 --captions film.srt --kind trailer --sheet out/qa-sheet.jpg --json qa-report.json` (no `short` kind exists; `--kind loop --end-hold 0` also passes, see `qa-loop.txt`):
```
DENT video QA: film-9x16.mp4
  ok    video codec h264
  ok    pixel format yuv420p (yuv420p; yuvj420p means full-range JPEG frames were piped in)
  ok    colour range tv (TV/limited)
  ok    constant frame rate (60/1)
  ok    audio codec aac
  ok    A/V durations 20.00 s / 20.00 s
  ok    loudness -14.4 LUFS (target -14.0 ± 1)
  ok    true peak -1.4 dBTP (≤ −1)
  ok    motion: 0.5 s of 16.0 s frozen (3 %, limit 20 % for a trailer)
  ok    motion: longest frozen hold 0.5 s (limit 2.5 s; closing 4.0 s end card excluded)
  ok    variety: longest visually-unchanged stretch 2.8 s (limit 6.0 s for a trailer)
  ok    energy: mean picture change 41.6/255 per second (floor 15.0 for a trailer; DENT's launch film: 35)
  info  rhythm: 1 shot changes (3/min), longest shot 12.5 s
  ok    no unintended black frames (0 found)
  ok    captions: 9 cues in film.srt
  ok    captions: every line ≤ 42 characters
  ok    captions: ≤ 2 lines per cue
  ok    captions: every cue ≥ 1 s
  ok    captions: every cue inside the film
  info  contact sheet (one frame every 1.2 s): out\qa-sheet.jpg  ← look at it
  note  taste, message and product truth are not measured here: look at the sheet and watch it with sound off and on

All measured checks passed
```
Layout check from `render.py video --ratio 9x16` (every 0.5 s, 9:16 safe zones top 10 % / bottom 18 %): **0 too small, 0 cut off, 0 in unsafe zones -> clean** (`out/layout-9x16.json` is empty). Flying pages and the climax push carry `data-crop` (deliberate). Caption top moved to 236 px to also respect the 12 % zone in video-types-and-craft.md §4.

First QA run (before fixes) failed 3 checks: true peak −0.2 dBTP after AAC encode (score.wav was −1.34), SRT lines > 42 characters, a 0.6 s loop cue. Fixed: limiter −3.2 dBFS in this film's `score.py`, shorter SRT descriptions, loop cue from 19.0 s.

- [x] video_qa passes and I looked at the sheet (`out/qa-sheet.jpg`)
- [x] Contact sheet of stills reviewed before the final render; fixes: big words overflowed the page (font-loading bug), white caption unreadable over flying white pages (caption plate added), pages flew under the binding (z-order), safe-zone caption shift
- [x] Genre bar met (hook frame 1, payoff 10.4 s, loop, vertical-native); originality guard passed
- [ ] **Sound heard by a person: NOT DONE (unverified, scored ≤ 6)**
- [x] Message with sound off: all meaning on screen (checked on stills/sheet, by me)
- [x] No typos (read all copy twice); no invented claims
- [x] Loudness −14.4 LUFS, true peak −1.4 dBTP
- [x] No flashing > 3/s: riffle pages are grey-on-grey; the only big luminance change is the cobalt slam at 7.5 s (one per second at most)
- [x] Licences recorded (§2)
- [x] Loop seam checked by eye: last frame ≈ first frame; small residual (page sliver, "?" tilt, torn stub) logged in SCORECARD.md

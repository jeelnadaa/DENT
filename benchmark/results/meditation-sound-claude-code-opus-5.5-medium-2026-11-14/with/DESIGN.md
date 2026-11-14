# DESIGN.md — Ma · a quiet meditation timer

Source of truth for this project. Read before changing anything; add a changelog line for every change.

## 1. Concept
- **Concept sentence:** a single brushstroke on washi paper in a quiet temple room.
- **Name:** Ma (間), the Japanese idea of the meaningful pause between things.
- **Mood:** still, warm, handmade · **Anti-words:** clinical, sugary.
- **Category cliché (meditation apps):** pastel teal/lavender gradients, lotus icon, glowing blob, rounded sans, sunset photo. **Divergence:** colour (warm paper + sumi ink + one vermilion), type (mincho serif numerals), imagery (a procedural dry-brush ensō, not a blob), sound (synthesised singing bowls in one key).
- **Style:** Japandi base + Editorial accent (serif numerals and headings only).
- **Signatures:** (1) the ensō is *drawn by your breath*: it inks in on the inhale and retreats on the exhale; (2) the vermilion 間 seal pulses at interval bells and stamps at completion.

## 2. Decision log
| Decision | Choice | Why | Source |
|---|---|---|---|
| Effort | All-out | — | User |
| Name | "Ma" (間) | Means the pause between things; short; original | User asked me to name it → Agent judgment |
| Direction | Ensō (ink on washi) | Picked from 3 rendered style tiles (`directions.html`) | User |
| Breathing | Calm 4·6, Even 5·5, Box 4·4·4·4, 4-7-8, Unguided + Custom sliders | Asked for presets + custom; described by timings only, no health claims | User + DENT `SKILL.md §3` (honesty) |
| Ambience | Rain, Ocean, Wind, Low drone, generated live | No files, no licences, works from file:// | User |
| Theme | Follows system + Auto/Light/Dark override, no flash | — | User + DENT `all-out.md §2.1` |
| Extras | Remember settings, session log, vibration, keep awake | — | User |
| Type | Shippori Mincho (numerals, headings) + Zen Kaku Gothic New (UI) | Japandi pairing; tabular serif numerals carry the screen | DENT `styles/japandi.md` |
| Palette | Paper #F4EFE6, ink #1F1B16, ink-2 #5C544A, seal #A63F2A; dark: #14110E / #ECE4D6 / #A99F90 / #D86A48 | Natural materials; one muted accent | DENT `styles/japandi.md` + Agent judgment (all pairs checked) |
| Ensō rendering | Canvas, seeded dry-brush stroke rendered once, revealed per frame with a sector clip + conic-gradient feather | Real brush texture at ~1 drawImage per frame | Override (DENT suggests SVG/CSS; canvas gives real kasure texture cheaply) |
| Bells default | On, but nothing sounds until the user presses Begin or a preview | A timer's end bell is its core function; still never autoplays; global toggle always visible | Override of DENT "sound off by default" (`audio-implementation §1`), logged in plan audit |
| Ambience when tab hidden | Keeps playing during an active sit; stops when idle | Meditators lock or switch apps mid-sit | Override of DENT "suspend ambience on hidden" |
| Bell scheduling | On the AudioContext clock, 3-min lookahead, end bell always pre-scheduled | Background tabs throttle JS timers (up to 1/min) | Agent judgment |
| End session | Only reachable from Pause | Prevents an accidental tap ending a sit | Agent judgment (Nielsen #5 error prevention) |
| Live region | Session events only (start, interval, pause, complete) | Announcing every breath would be noise | DENT `accessibility.md` + Agent judgment |
| Layout | Phone: stacked; ≥960 px: asymmetric stage + 400 px settings column; sitting: settings hidden, stage centred | Japandi asymmetry; focus while sitting | DENT `styles/japandi.md` + Agent judgment |
| Libraries | None (vanilla JS, Web Audio, Canvas) | One file; every job covered natively | DENT `catalog/component-selection.md` (reuse/none first) |

## 3. Tokens
```css
--paper #F4EFE6 | #14110E      --surface #EBE4D7 | #1E1A16
--ink #1F1B16 | #ECE4D6        --ink-2 #5C544A | #A99F90
--line #D8CFBF | #332D27 (decorative)   --line-strong #7F7566 | #7A7064 (controls)
--seal #A63F2A | #D86A48       --on-seal #FBF6EE | #14110E
space 4/8/12/16/24/32/48/64 · radius 4 (controls) / 6 (containers)
motion 180 / 450 / 700 ms · ease (.25,.1,.25,1) · ease-out (.16,1,.3,1)
type: body 16/1.55 · small 14 · h2 22 · time clamp(44px, 19% of stage, 116px)
```
`prefers-contrast: more` raises ink-2 and hairlines to full contrast; `forced-colors` keeps seal and buttons legible.

**Contrast (contrast.py):** ink/paper 14.95 · ink-2/paper 6.50 · ink-2/surface 5.89 · seal/paper 5.45 · on-seal/seal 5.80 · dark ink 14.90 · dark ink-2 7.21 (6.63 on surface) · dark seal 5.44 · control borders 3.95 / 3.58 (light, paper/surface) and 3.88 / 3.56 (dark). All pass.

## 4. States
idle · settling (10/30 s countdown, ghost circle) · sitting (breath phase + count, remaining time, progress hairline with interval ticks) · paused (Resume / End session) · complete (seal stamps, "You sat for N minutes.") · ended early (logged only if ≥ 1 min) · custom-duration error (Begin disabled, fix-it message) · ambience preparing / playing / error · log: empty / populated / storage blocked / clear-confirm · vibration and wake-lock unsupported notes · sound off (previews disabled with reason) · reduced motion (static circle, text phases, no stamp scale).

## 5. Motion spec
| Element | Motion | Timing | Reduced motion |
|---|---|---|---|
| Ensō inhale | Brush inks along the circle; scale .955→1 | Breath length, sine ease | Static full circle; phase text only |
| Ensō exhale | Ink retreats from the start; scale 1→.955 | Breath length, sine ease | Static |
| Interval | Seal pulse + halo | 1.8 s once | Outline highlight, no scale |
| Complete | Seal stamps (scale 1.9→1, rotate) | 700 ms ease-out | Fade only |
| View change | View Transition crossfade (when supported) | Browser default | Instant |
| Dialog | Rise 12 px + fade | 450 ms | Instant |

Only transform/opacity and a canvas redraw are animated; the canvas skips frames when nothing changed (holds).

## 6. Sound spec
**Role:** identity + function (start, interval, end), plus optional atmosphere. **Sonic concept:** a brass singing bowl in a wooden room. **Character:** warm, resonant, unhurried · **Anti:** digital beeps, chimes-on-every-click. **Silence policy:** no UI clicks, no breath cues, nothing before a gesture.

| Cue | Design | Level (measured, 70 % bell volume, dry) |
|---|---|---|
| Start | Bowl strike on G3 (196 Hz) + softer fifth (D4) 0.62 s later: a rising fifth opens | peak −13.5 dBFS |
| Interval | One higher bowl (G4), ±1.5 % pitch variation each time | peak −17.9 dBFS |
| End | Three strikes: fifth, root, softer root, 2.8 s apart: a falling close | peak −14.3 dBFS |
| Ambience | Rain, Ocean, Wind, Low drone (drone tuned to G, matching the bells) | RMS −30.8 dBFS at 60 %, ≈ −28 dBFS at the 70 % default |

Bowl synthesis: four inharmonic partials (1, 2.71, 5.15, 8.43×), each a detuned sine pair for the slow "wah" beating, plus a 35 ms felt-mallet noise touch, through a generated 3.4 s room reverb (34 % wet) and a limiter. Ambience is rendered offline into 60 s loops with an equal-power 4 s crossfade at the seam, normalised to −22 dBFS RMS at full volume. Render times measured headless: rain 248 ms, ocean 264 ms, wind 270 ms, drone 467 ms.

| Event | Sound | Visual equivalent | Repeat limit |
|---|---|---|---|
| Sit starts | Start cue | Ensō begins, "Breathe in", live-region "Session started" | Once per sit |
| Interval | Interval cue | Seal pulse, progress tick turns vermilion, live-region "N minutes passed" | Once per interval |
| Sit complete | End cue, ambience fades out | "Complete" view, seal stamp, live-region | Once |
| Preview buttons | The cue | Button press | 350 ms debounce |

Controls: header sound toggle (`aria-pressed`, M key) mutes everything instantly; bell volume, ambience volume; ambience Listen/Stop; all persisted. Works fully muted.

## 7. Licences
| Asset | Source | Licence |
|---|---|---|
| Shippori Mincho | Google Fonts (FONTDASU) | SIL Open Font License 1.1 |
| Zen Kaku Gothic New | Google Fonts (Yoshimichi Ohira) | SIL Open Font License 1.1 |
| Icons (speaker, bars, close), favicon, ensō, seal | Drawn for this project | Project-owned |
| All sounds | Synthesised in the browser by this code | Project-owned, no samples |
| Libraries | None | — |

Fonts load from Google's CDN; offline, the page falls back to installed serif/sans fonts and still works.

## 8. Verification (2026-11-14, Playwright Chromium headless on Windows)
| Check | Result | Evidence |
|---|---|---|
| G2 overflow 320/375/390/768/1024/1440 | Passed | verify_page.py: scrollWidth = viewport at all widths |
| G3 contrast | Passed | contrast.py on every token pair + sampled page: 0 failures |
| G4 labels / names / keyboard | Passed | verify_page.py: 0 unlabeled, 0 unnamed; Tab order header → Begin → settings, visible focus on every stop; dialog focus in, Esc closes, focus returns to "Practice" |
| G10 reduced motion | Passed | verify_page.py reduced-motion run: 0 running animations; screenshot shows static circle with text phases |
| G11 no autoplay | Passed | No AudioContext before a gesture (also after reload); created on Begin, state "running" |
| Session journey | Passed | Custom 2 min, 1-min interval, 10 s settle, rain (time accelerated 8×): settling → sitting; phases "Breathe in 1–4 / Breathe out 1–6" seen; interval tick + announcement; Space pauses; time frozen while paused; bells cancelled on pause, rescheduled on resume (only `end@120000` left); mute → master 0.000, unmute → 1.000; complete with correct text; log entry written |
| Ended early | Passed | Pause → End session after ~70 s: "You sat for 1 minute.", logged as ended early |
| Validation | Passed | Custom 0 or 500 min → error shown, Begin disabled, summary explains |
| Persistence | Passed | Reload restores duration, custom value, interval, ambience, theme |
| Log | Passed | Seeded 6 sits: totals 6 / 90 min / 4-day streak correct; 7-day bars labelled; clear-confirm focus to "Keep it" |
| Console errors | Passed | 0 in every run |
| Loudness | Passed (digital measure) | Offline renders: bells peak −13.5 to −17.9 dBFS, ambience RMS −28 to −31 dBFS, no clipping |
| Listening by ear | Not run | The agent cannot hear; needs a human listen on speakers and headphones |
| Real phones (iOS Safari, Android Chrome), vibration, wake lock | Not run | Only feature detection paths were checked; needs a device test |
| Firefox / Safari desktop | Not run | Chromium only |

**Known limitations:** iOS Safari suspends Web Audio when the screen locks, so keep-awake matters there (and iOS has no Wake Lock before 16.4). Vibration doesn't exist on iPhone browsers; the UI says so.

## 9. Changelog
- 2026-11-14: v1 built. Improve round 1: rain render 68 s → 0.25 s (drops synthesised directly instead of ~2,000 audio nodes, which had also blocked page navigation); log dialog layout fixed (floated heading); brush beading removed (per-bristle layers) and edges feathered with a conic mask; sitting view centred; interval bell +3.4 dB; ambience default 60 → 70 %.
- 2026-11-14: Shipped as is (user decision). Still unverified: listening by ear, and vibration and wake lock on real phones.

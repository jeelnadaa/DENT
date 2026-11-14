# DESIGN.md — Quill (launch identity + video)

Source of truth for the Quill mini identity made for the launch video. Read it before any future Quill work. Video specifics live in `VIDEO.md`.

## 1. Concept
- **Concept sentence:** *One continuous line of ink* — Quill catches a thought the way a nib catches paper, and the same line links one idea to the next.
- **Mood words:** calm, literate, quick. **Anti-words:** techy, shouty.
- **Category cliché named:** white/purple SaaS gradients, floating 3D card stacks, "second brain" glowing graphs.
- **Divergence:** serif display type (not geometric sans) · warm paper + ink + vermilion (not purple gradients) · motion carried by one hand-drawn line (not parallax cards).
- **Style:** Editorial (base) + Kinetic Typography (accent). Signature moves: big serif headlines with tight leading, print-like rules/underlines, and the ink line.
- **Signature elements:** (1) the ink line with a vermilion nib that draws every transition; (2) the wordmark's vermilion "ink drop" dot.

## 2. Tokens
| Token | Value | Use |
|---|---|---|
| `--paper` | `#F3EDE2` | Background |
| `--paper-deep` | `#E9E1D3` | Vignette, secondary surface |
| `--card` | `#FFFCF6` | Notes, windows, palette |
| `--ink` | `#1A1F2E` | Text, ink line, keycap outlines |
| `--ink-2` | `#4A5063` | Secondary text |
| `--ink-3` | `#6B7080` | Meta text **on cards only** (4.82:1); not on paper (4.24:1) |
| `--vermilion` | `#B23A0B` | Accent: kickers, links, nib, logo dot, highlights |
| `--vermilion-soft` | `rgba(178,58,11,.12)` | Selected row / highlight wash |
| `--on-ink` | `#FBF7EF` | Caption text on ink plate |
| `--rule` | `rgba(26,31,46,.14)` | Card borders, dividers |
| Radius | 14 px cards · 12 px keycaps/popovers · 18 px palette | |
| Ink stroke | 5 px (16:9) / 6 px (9:16), round caps, displacement filter scale 2.6 for a bled edge | |

### Contrast (DENT `scripts/contrast.py`)
| Pair | Ratio | Verdict |
|---|---|---|
| ink on paper | 14.09:1 | AAA |
| ink-2 on paper | 6.88:1 | AA |
| ink-3 on card | 4.82:1 | AA |
| vermilion on paper | 5.14:1 | AA (was 4.44 with `#C2410C`; darkened) |
| vermilion on card | 5.85:1 | AA |
| vermilion on highlight wash | 4.96:1 | AA |
| on-ink on caption plate (92 % ink over paper) | ≈15:1 | AAA |

## 3. Type
| Role | Font | Settings |
|---|---|---|
| Display / wordmark / titles | **Fraunces** (variable, OFL) | weight 300–420, `opsz` auto, SOFT 50–100, tracking −0.03 to −0.045 em, leading 0.95–1.0 |
| Body / UI / captions | **Satoshi** (variable, ITF FFL — user's choice) | 450–700; kickers 700, +0.14 em tracked caps |
Sizes (16:9 / 9:16): hook 190 / 168 px · wordmark 300 / 270 · feature title 92 / 96 · kicker 24 / 30 · card body 31 / 34 · captions 40 / 42.

## 4. Logo direction
`Quill` set in Fraunces 420 (SOFT 100, WONK on) + a vermilion circle at 0.17 em as the full stop — an ink drop. Minimum size: 54 px cap-height-equivalent in video (brand bug). Clear space: the dot's width on all sides. The full stop also reads in the tagline *Think in ink.*

## 5. Motion
- Every frame is a pure function of time (`render(t)`), 30 fps.
- Easing: ease-out cubic/quint for entrances, ease-in-out cubic for moves and line drawing, a damped spring for the capture window drop, a small overshoot on the logo dot.
- Durations: text entrances 0.5–0.7 s; scene transitions 0.7–0.9 s; holds ≥ 0.5 s + 0.3 s/word.
- One transition family: the ink line. No flashes (nothing changes luminance more than once per second).

## 6. Sound
- Original score: felt piano + warm pad, D major, 96 BPM (Dmaj9 – Bm9 – Gmaj9 – A6sus), pulse from the name reveal, 300 ms silence before the end-card hit.
- Sonic logo: A4 → D5 → F♯5 rising bell + piano, lands on the logo dot (also used at the name reveal).
- SFX: nib on paper (band-passed noise), key taps, keycaps, paper drop, link chime, ticks, soft whooshes — all frame-synced from the composition's event list.
- Mix: music ducked −10 dB under the voice; −14 LUFS integrated, true peak −5 dBTP.

## 7. Licences
See `VIDEO.md` §10. Every visual and audio element is either original, OFL, ITF FFL (video use explicitly allowed) or public-domain-trained (voice).

## 8. Decision log
| Decision | Choice | Why | Source |
|---|---|---|---|
| Effort | All-out | — | User |
| Features shown | Quick capture · `[[ ]]` links · instant search | User delegated; near-universal note features, flagged as proposed | Agent judgment |
| Video sub-type | Reveal, 45 s | Fits 30–45 s band; name early, 3 moments, CTA | DENT `video-types-and-craft.md` §2 |
| CTA | "Out now · quill.example" | User asked for a demo link, not a placeholder; `.example` is reserved | User + Agent judgment |
| Sound | Music + synthetic VO | — | User |
| Voice | Piper TTS, Cori en_GB high | Natural, commercial-safe (public-domain data) | User (from DENT-checked options) |
| Cuts | 16:9 + 9:16 | — | User |
| Direction | A · Ink Line (Editorial + Kinetic Type) | Least like category; ink line = linking metaphor | User (from 3 DENT tiles) |
| Body font | Satoshi | — | User |
| Display font | Fraunces | Soft, literate serif with optical sizes | Agent judgment (DENT `styles/editorial.md` lists it) |
| Build tool | HTML composition + Playwright + FFmpeg | Deterministic, brand-exact, no licence threshold | DENT `video-tools-and-pipeline.md` §4 |
| Vermilion | `#B23A0B` (was `#C2410C`) | Original failed 4.5:1 on paper | DENT gate G3 |
| Captions | Burned in + SRT/VTT, split at real voice pauses | Muted viewing on X/LinkedIn | DENT `voice-and-narration.md`, Agent judgment (pause detection) |
| Loudness | −14 LUFS, limiter before linear loudnorm | Platform norm; avoid pumping | DENT `video-tools-and-pipeline.md` §5 |

## Changelog
- 2026-11-14 — Created with the launch video (v1).

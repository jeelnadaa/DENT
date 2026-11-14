# Implementation Plan: Ma — a quiet meditation timer

> DENT plan · Depth: Advanced · Effort: All-out · Date: 2026-11-14

## 1. Objective
- **Goal:** a meditation timer web app with a breathing animation, optional ambient soundscapes and a gentle sonic identity (start, interval, end sounds).
- **User problem:** sit for a set time without checking a clock; be guided in breathing if wanted; be told gently when time is up.
- **Outcome:** one `index.html` (plus a favicon) that opens from `file://` and works on phones, tablets and desktops.

## 2. Scope
**Included:** timer, breathing guide (presets + custom), ambient soundscapes generated in the browser, bell identity, remembered settings, session log, vibration cues, keep-screen-awake, light/dark following the system with a manual override.
**Excluded:** accounts, sync, notifications, recorded audio files, guided voice, health claims.

## 3. Existing system
Empty folder (PROMPT.md, QA.md only). No framework, no design system → create tokens inside index.html.
**Confirmed:** single file, CDN/Google Fonts allowed, file:// must work. **Assumed:** modern evergreen browsers. **Unknown:** real-device audio behaviour on iOS when the screen locks (emulation only).

## 4. Requirements
| ID | Requirement | Priority | Acceptance criterion |
|---|---|---|---|
| R-01 | Timer with selectable duration | Must | Presets 3–60 min + custom 1–180 min; invalid custom input shows a fix-it message; countdown accurate to ±1 s over the session (time-based, not tick-counting) |
| R-02 | Breathing animation | Must | Brush ensō draws on inhale, holds, retreats on exhale; phase word + seconds shown; presets Calm 4·6, Even 5·5, Box 4·4·4·4, Relax 4·7·8, Unguided |
| R-03 | Custom breathing pattern | Must (user) | Four sliders (in, hold, out, hold) with live summary; animation uses them |
| R-04 | Optional ambient soundscapes | Must | Off by default; Rain, Ocean, Wind, Low drone; separate volume; preview button; crossfade; loading state while a soundscape is prepared |
| R-05 | Sonic identity: start, interval, end | Must | Three distinct synthesised bowl sounds from one family; interval options Off/1/2/3/5/10/15 min; each sound previewable; scheduled on the audio clock so they fire even when the tab is throttled |
| R-06 | Sound control | Must | Global sound toggle (aria-pressed) mutes instantly; bells volume; nothing plays before a user gesture; works fully muted |
| R-07 | Visual equivalents | Must | Start: ensō begins + status; interval: seal pulse + progress tick + live-region text + optional vibration; end: completion screen + seal stamp |
| R-08 | Remember settings | Must (user) | Reload restores duration, pattern, custom values, interval, settle-in, ambience, volumes, sound, theme, toggles |
| R-09 | Session log | Must (user) | Dialog with sessions, total minutes, day streak, last-7-days bars with text values, recent list, clear with confirmation; empty state; storage-blocked state |
| R-10 | Vibration cues | Must (user) | Toggle; vibrates at start/interval/end where supported; "not supported" note elsewhere |
| R-11 | Keep screen awake | Must (user) | Toggle (default on); Wake Lock during session, re-acquired on return; unsupported note |
| R-12 | Light + dark | Must (user) | Follows system; Auto/Light/Dark control persisted; no flash of wrong theme |
| R-13 | Responsive | Must | No overflow at 320–1440; designed layouts for phone (stacked), tablet, desktop (asymmetric two columns); session view is focused |
| R-14 | Pause / resume / end | Must | End only reachable from Pause (prevents accidental end); Space toggles start/pause |
| R-15 | Settle-in | Should | None/10 s/30 s before the start bell |
| R-16 | Favicon | Should | SVG seal favicon in folder |

## 5. Experience
- **Idle:** header (seal + "Ma", sound toggle, practice log) · stage (ensō + big duration numerals + pattern line + Begin) · "Your sit" settings panel (right column ≥ 960 px, below the stage on smaller screens).
- **Settling → Sitting:** settings fade away; stage centres; phase word; hairline progress with interval ticks; Pause.
- **Paused:** Resume (primary) + End session.
- **Complete:** full ensō, vermilion seal stamps, "You sat for 10 minutes", Sit again / Done.
- **Log dialog:** native `<dialog>` (focus trap, Esc).

## 6. Creative direction
- **Concept:** *a single brushstroke on washi paper in a quiet temple room.* Name **Ma (間)**: the Japanese idea of the pause between things.
- **Mood:** still, warm, handmade · **Anti:** clinical, sugary.
- **Cliché:** pastel teal/lavender gradients, lotus icon, rounded sans, glowing blob, sunset photo. **Diverge on:** colour (warm paper + sumi ink + one vermilion), type (mincho serif numerals), imagery (a procedural brush stroke instead of a blob), sound (bowls in one key, not generic chimes).
- **Style:** Japandi base + Editorial accent (serif numerals only).
- **Signatures:** (1) breath-drawn dry-brush ensō on canvas; (2) vermilion 間 seal that pulses at intervals and stamps at completion.
- **Type:** Shippori Mincho (numerals, display) + Zen Kaku Gothic New (UI, ≥ 16 px body).
- **Colour:** light paper #F4EFE6 / ink #1F1B16 / ink-2 #5C544A / seal #A63F2A; dark night #14110E / moon ink #ECE4D6 / ink-2 #A99F90 / seal #D86A48. All pairs checked (see §11).
- **Motion:** breath-driven only, sine easing; UI fades 400–600 ms; reduced motion → static ensō, text phases, no stamp scale.
- **Sound:** synthesised singing bowls in G (196 Hz root, inharmonic partials, beating pairs, felt-mallet transient, generated room reverb); ambience pre-rendered to 60 s seamless loops; drone tuned to G.

## 7. Technical strategy
- Vanilla HTML/CSS/JS, no libraries (one file; Web Audio + Canvas cover every job).
- One audio manager: lazy AudioContext on gesture, master → limiter, bells bus + reverb, ambience bus. Bells scheduled on the audio clock with a 3-minute lookahead; cancelled and rescheduled on pause/resume.
- Timer state machine: idle → settling → sitting ⇄ paused → complete. Time from `performance.now()`; completion checked by rAF + a timeout + visibilitychange.
- Storage: localStorage with try/catch; failure → log shows a blocked state, app still works.

## 8. States and edge cases
Idle · settling · sitting · paused · complete · ambience loading · custom-duration error · log empty / populated / storage blocked / clear-confirm · vibration/wake-lock unsupported · sound muted mid-session · sound enabled mid-session · tab hidden · reduced motion · high contrast · fonts offline (fallbacks).

## 9. Accessibility and responsive
Native buttons/radios/ranges/dialog; every control labelled; visible focus ring (≥ 3:1); targets ≥ 44 px; live region for session events only (not every breath); canvas `role="img"` with label; `prefers-reduced-motion`, `prefers-contrast`, `forced-colors`; logical CSS properties; breakpoints 600 / 960.

## 10. Phases
| Phase | Tasks | Done when |
|---|---|---|
| 1 | Tokens, layout, components, theme | Renders at all widths in both themes |
| 2 | Timer state machine + ensō canvas + breathing | Full session runs with correct phases |
| 3 | Audio engine: bells, ambience, scheduling, controls | Sounds play only after gesture; mute instant |
| 4 | Persistence, log, vibration, wake lock | Reload restores; log updates |
| 5 | Verify (verify_page.py, manual journeys, audio level render), fix, score, improve | Gates pass; score ≥ 9 |

## 11. Verification
| Requirement / gate | Method | Expected |
|---|---|---|
| R-01/R-14/R-15 | Browser: run a 1-min session (time accelerated via test hook), pause/resume/end | Correct transitions and times |
| R-02/R-03 | Screenshots mid-phase; read phase text | Draw/hold/retreat visible |
| R-04/R-05/R-06 | Inspect AudioContext state + scheduled bells; OfflineAudioContext render → peak/RMS | No audio before gesture; peaks ≤ −6 dBFS; ambience RMS ≈ −30 to −24 dBFS |
| R-08/R-09 | Reload; complete session; open log | Restored; entry listed |
| R-10/R-11 | Feature detection paths | Correct note when unsupported |
| G2 | verify_page.py 320–1440 | No overflow |
| G3 | contrast.py on token pairs (done: all pass) + sampled page | Pass |
| G4/G10/G11 | verify_page.py + keyboard pass | Pass |

## 12. Risks
| Risk | L/I | Mitigation |
|---|---|---|
| Background tab throttling delays bells | High/High | Schedule bells on the audio clock ahead of time |
| iOS suspends audio on screen lock | Med/Med | Wake Lock keeps screen on; documented limitation |
| Canvas brush cost on low-end phones | Low/Med | DPR cap 2, ~160 segments, pause when hidden |
| 60 s ambience loop repetition | Med/Low | Random content, crossfaded seam |
| Google Fonts unavailable offline | Med/Low | Serif/sans fallbacks tuned |

## 13. Plan audit
| # | Finding | Severity | Resolution |
|---|---|---|---|
| 1 | DENT default "sound off" conflicts with a bell timer whose core function is the end bell | Major | Override: bells on by default but nothing plays until the user presses Begin (gesture + explicit choice); global toggle always visible; ambience stays off by default |
| 2 | DENT says suspend ambience on tab hidden; meditators lock/switch away mid-session | Major | Override: keep ambience during an active session only; suspend when idle and hidden |
| 3 | Accidental "End" mid-meditation loses the sit | Major | End only from Paused state |
| 4 | Announcing every breath phase to screen readers would be noisy | Minor | Live region only for session events |
| 5 | Health/benefit claims about breathing patterns would be unverified | Major (honesty) | Describe patterns by their timings only |
| 6 | Streak could mislead if ended-early tiny sits count | Minor | Only log sits ≥ 1 min; mark "ended early" |
| 7 | Web manifest/PWA fails on file:// | Obs. | Not added; favicon only |

## 14. Definition of done
- [ ] All Must requirements implemented and verified
- [ ] Gates G1–G12 reported
- [ ] Scorecard ≥ 9, no line < 8, or gaps reported
- [ ] DESIGN.md + SOUND spec + licence table written

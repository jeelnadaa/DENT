# Video Plan: Streak launch trailer, "Roots"

> DENT video plan (`/dent:video`, effort **All-out**). Eval run S27 (trailer). Built in code with the DENT video kit (`composition.html` → headless Chromium → FFmpeg). Streak is a **fictional** app invented for this test: every screen is an HTML reenactment designed for this film, and the film says so on screen ("Concept demo · Streak is fictional").

## 0. Questions the skill asked (non-interactive run: scripted answers)
The run had no person to answer, so each question the skill requires is written here with the scripted answer the eval brief supplied, or the documented default where the brief was silent.

| # | Question (as DENT would ask it) | Source of the question | Answer used |
|---|---|---|---|
| 0 | How far should I take it? Essential · Standard (Recommended) · Polished · All-out — or answer "you decide" to skip all questions | SKILL.md §1.2 | **All-out** (scripted) |
| 1 | Type and platform? | video.md step 1 | Trailer (launch), from the prompt. **16:9 master + a 9:16 cut** (scripted) |
| 2 | Length? | video.md step 1 | 45 s, from the prompt |
| 3 | Where should the visuals come from? Code-built scenes with faithful UI reenactments (Recommended) · local generative model · cloud provider · your own footage. *Real app captures would lift the proof beats; Streak doesn't exist, so the UI is reenacted and labelled.* | media-sourcing §2, pipeline §1 | **Code-built in the browser, no generative imagery** (scripted) |
| 4 | Voice? Local model (Qwen3-TTS installed) (Recommended) · Chatterbox · Kokoro · cloud · human | voice-and-narration §1 | **Local model** (scripted) → Qwen3-TTS 1.7B (rank 1 in DENT's test) |
| 5 | Commercial use? (decides which voice models qualify) | voice-and-narration §1.2 | Not scripted. Default: assume yes; Qwen3-TTS is Apache-2.0, so no conflict |
| 6 | Music and SFX? Made in code (Recommended) · licensed library · generative | media-sourcing §5.2–5.3 | **Made in code** (scripted) |
| 7 | All-out can also include: thumbnail, 1:1 cut, … Which do you want? | all-out.md §0 (Offer rows) | Not scripted. Logged: 1:1 cut and thumbnail **N/A — the platforms answer named only 16:9 + 9:16**; a poster frame is exported anyway |
| 8 | Creative menu gate: Show me 3 directions (Recommended) · Let me pick the ingredients · You decide · I have references | video-creative-direction §2 | **Show me 3 directions** (scripted) |
| 9 | Which direction? (or combine) | video-creative-direction §1.3 | **Agent's recommendation: A "Root System"** (scripted) |
| 10 | Anything you never want to see or hear? | menu group F | Not asked: the gate answer skips the ingredient groups. Defaults: no flame emoji, no confetti, no green-checkmark grid as the product's look |
| 11 | Script approval | video.md step 5 | Not available (no person). Proceeded on the agent's read-aloud timing (§3) |

## 1. Brief
- **Type and sub-type:** Trailer (launch reveal, product-play). 45 s.
- **Audience and where they'll watch:** people who have started and abandoned habit trackers; App Store / Play pre-launch, YouTube (16:9), Reels / TikTok / Shorts (9:16). Often muted: every beat is carried by on-screen type and burned captions.
- **One message:** In Streak, missing a day doesn't send you back to zero: your habits grow as a garden, and the work you did stays in the roots.
- **Call to action:** "On iPhone and Android" (the app is fictional: no store link or URL is invented; the end card carries the demo label).
- **Length and ratios:** 45.0 s · 16:9 1920×1080 master · 9:16 1080×1920 cut · 60 fps.
- **Mood words:** tender, earthy, defiant. **Anti-words:** gamified, clinical.
- **Creative concept:** a cutaway of the soil. Above ground, a habit can wilt; below ground, the roots you grew are still there.
- **Must show:** the app (Today list, watering a habit, the garden, a missed day that wilts but does not reset, the roots view, both platforms, the widget), the name by ~9 s, the CTA.
- **Must not show:** streak flames, confetti, invented ratings/downloads/press, store badges (trademarks), any claim that Streak is real.
- **Assets available:** none (fictional product). Fonts via `fonts.py`, palette via `palette.py`, sound synthesised.

### Product facts (the fictional spec this film stays inside)
Streak (concept) is a habit tracker for iOS and Android. Each habit is a plant. Tapping a habit's water button marks it done and grows a leaf. The **Garden** tab shows all habits as plants; they flower as they mature. Missing a day **wilts** a plant; it never resets it, and watering it again revives it. The **Roots** tab shows the accumulated days as a root system. A home-screen widget shows the garden. Every screen in the film shows only these behaviours.

### The three answers (sound off) — video-types-and-craft §2b
1. **What is it?** A habit-tracking app (iPhone + Android) called Streak — named by 8.6 s (root-drawn wordmark + "Meet Streak." caption), shown as an app from 10 s.
2. **What does it do for me?** Your habits grow as a garden; a missed day wilts a plant but never resets you to zero ("Show up. It grows." / "Miss a day? It wilts. No reset.").
3. **How do I get it?** "One garden. iPhone + Android." and the end card "On iPhone and Android" (fictional: no store link exists).

**Planned real-product screen time:** app UI 10.0–25.4 s (15.4 s) + both platforms and widget 32.5–40.0 s (7.5 s) = 22.9 s = **51 %** strictly. The climax (25.1–32.5 s, 7.4 s) is entered through the phone's **Roots** tab and shows that tab's root view full-frame; counting it gives 30.3 s = **67 %**. See §9: the strict reading misses the 60 % rule.

### The bar for this genre (video-creative-direction §5, Trailer)
"Rhythm, rising stakes, a twist, title at the peak"; structures: three-act build with a drop, reverse chronology, question→answer; clichés: whoosh on every cut, deep "in a world" voice. Because this is also a *launch* trailer, §2b's rule applies too: name and promise by ~9 s. **Resolution:** the name lands small and early (root-written wordmark at 7.5–9.2 s) and the title returns at full size at the peak (28.75 s).

## 1b. Creative direction

### Creative menu answers
Gate → "Show me 3 directions". Ingredient groups (feel, typography, motion, graphics, sound, never) were therefore not asked; each bible below makes those choices.

### Category-cliché check
Habit trackers look like: a green-checkmark grid (GitHub contribution squares), a flame streak counter, confetti on completion, a bright-green or purple-gradient UI, a "don't break the chain" calendar. **All three directions diverge** from that on type, colour, imagery and motion; direction A goes further and *stages* the cliché in the cold open (the checkmark grid is the villain).

### Direction A — "Root System" (recommended, chosen)
```
NAME:              Root System
LOGLINE:           A cutaway of the soil: above ground a habit can wilt, below ground the roots you grew stay.
WORLD & MATERIAL:  Soil strata in cross-section (loam, pebbles, motes) under a sky that changes per act; roots are
                   luminous pollen-gold lines; the app lives in a phone planted in the ground. Physics: gravity for
                   falling things, organic spring growth (f 1.6, ζ 0.5), roots draw with ease-in-out.
SIGNATURE DEVICE:  The checkmark becomes a seedling: a ✓ falls, lands in the soil and its two strokes morph into two
                   leaves (true path morph). Every habit afterwards is a plant; the end card turns the whole opening
                   grid of ✓ into seedlings.
TYPE:              Custom lettering "streak": one monoline root (round caps) writes the name, the k's arm is a leaf.
                   Statements in BioRhyme (wide slab serif, wdth 125, 800 / 300 contrast); the app's own UI in Georama;
                   data in Sometype Mono (tabular). Type moves by masked line rises and by being drawn as roots.
MOTION LANGUAGE:   Liquid & organic (growth, roots, sway) + Physical (gravity fall, squash on landing, shockwave).
                   60 fps, motion blur in fast windows.
TRANSITIONS:       The horizon crossing: the camera sinks below or rises above the soil line; the soil edge is the wipe.
                   Exception at the climax: the push THROUGH the phone screen into the roots.
CAMERA:            2.5D vertical travel with soil parallax (pebbles at depths), continuous breathing drift.
COLOUR SCRIPT:     Act 1 sterile grey-white + steel ink + one crimson ✗ (the checkmark world) → act 2 dark loam,
                   pollen-gold roots, chartreuse growth → climax gold on black → act 3 dawn gold → end warm cream.
SOUND WORLD:       Act 1 dry clinical ticks and a buzz, no reverb, no music; act 2 woody Karplus plucks, earth drone,
                   heartbeat kick, droplet taps, root creaks; half a second of silence; climax opens the arrangement;
                   act 3 high plucks. Sonic logo: the "sprout" motif D–A–E (rising fifths) + a bud pop. 96 bpm.
STRUCTURE:         Cold open (the cliché breaks, 0–5) → turn + name (5–10) → three proof beats with a break
                   (10–25: show up / keep going / miss a day) → silence → climax: roots + title at the peak (25–32.5)
                   → platforms at dawn (32.5–40) → callback end card (40–45).
THE MOMENT:        Full-frame roots with "streak" written in light across them (28.75 s).
NEVER:             flame emoji, confetti, green-checkmark grid as the product look, whoosh on every cut, trailer voice.
```
Style frame: `review/styleframe-A-root-system.jpg`.

### Direction B — "Field Journal"
```
NAME:              Field Journal
LOGLINE:           A botanist's herbarium of your days: every kept habit pressed, labelled and taped into a journal.
WORLD & MATERIAL:  Paper, pressed leaves, archival tape, pencil marks; flatbed light; no gravity, things are placed by hand.
SIGNATURE DEVICE:  The specimen label: each habit gets a mock-Latin name ("Legere cotidie — Read daily") written in as it is kept.
TYPE:              Bodoni Moda italic for Latin names, Courier Prime for labels, handwritten numbers.
MOTION LANGUAGE:   Hand-made (boil on twos, stop-motion placement) + collage.
TRANSITIONS:       Page turns of the journal; exception: the journal closes to reveal the app icon on the cover.
CAMERA:            Locked top-down, occasional slide of the page under the lens.
COLOUR SCRIPT:     Sepia parchment → pressed greens → indigo ink (#2F3C8F) for the name.
SOUND WORLD:       Pencil, paper, tape, a music-box melody, a celesta; silence on the missed-day page.
STRUCTURE:         Reverse chronology: open on a full journal at day 300, flip back to day 1.
THE MOMENT:        A two-page spread of 300 pressed days.
NEVER:             stamps (DENT's letterpress), confetti, checkmarks.
```
Style frame: `review/styleframe-B-field-journal.jpg`.

### Direction C — "Night Bloom"
```
NAME:              Night Bloom
LOGLINE:           At night a city of windows lights up one by one: in each, a phone's garden glows like bioluminescence.
WORLD & MATERIAL:  Glass, night air, light; plants as bioluminescent shapes; a 3D city block (Three.js).
SIGNATURE DEVICE:  A window lights when a habit is kept; the whole facade becomes a garden.
TYPE:              Roboto Flex at extreme width (151) for the title; minimal type otherwise.
MOTION LANGUAGE:   Cinematic camera (one continuous crane along the facade) + liquid glow.
TRANSITIONS:       Rack focus between windows; exception: the crane pulls back to the whole city.
CAMERA:            3D, continuous move, no cuts.
COLOUR SCRIPT:     Blue-black night → cyan #5CF2D6 and magenta #D35BFF blooms → first light.
SOUND WORLD:       Analogue-style synth pulse, city hum, glassy bell per lit window; silence before the pull-back.
STRUCTURE:         A single escalating shot.
THE MOMENT:        The whole city facade glowing.
NEVER:             neon cyberpunk clichés (rain, katakana), confetti.
```
Style frame: `review/styleframe-C-night-bloom.jpg`.

**Axes on which they differ:** world (soil cutaway / paper herbarium / night city), signature (✓→seedling / specimen label / window lights), type (custom root lettering + wide slab / Didone + typewriter / ultra-wide grotesk), motion (organic + physical / hand-made / cinematic camera), camera (2.5D vertical / locked top-down / 3D crane), colour script (sterile→loam→dawn / sepia→indigo / night→bloom), sound (plucks + earth / pencil + music box / synth pulse + glass), structure (three-act with a drop / reverse chronology / single shot). **All 8 axes differ** for every pair (rule: ≥ 4).

**Recommendation and choice:** A. It is the only direction whose metaphor *is* the product's argument (what you did stays, underground), it keeps the real UI on screen for the proof beats (B and C push the UI to the edges), and its twist is a product feature rather than a visual trick. Chosen (scripted: "pick your recommendation").

### Originality guard (video-creative-direction §4) — result: **PASS**
- **Not DENT's devices:** no orange-dot or circle wipe (the kit's `wipe()` is removed; transitions are the horizon crossing) · no letterpress strike or "impression" · no wall of identical templates knocked over (the opening grid is a habit tracker's own checkmark grid, and it is not knocked over: the checks fly off on a reset) · no split-flap · no numbered "It asks / It names / It checks" chapters · no "this film was made with" ending. Placeholders replaced: fonts (Mozilla Headline / Newsreader / Datatype → BioRhyme / Georama / Sometype Mono), colours (#A8236E accent → palette `rootsystem`), the two-voice statement system, the chapter numeral, the terminal, the count-up proof scene.
- **Not the genre's clichés:** no whoosh on every cut (an early score draft had four whooshes on transitions; three were replaced by soil creaks and a UI click after inspecting the spectrogram; one remains before the climax impact) · narration is a warm, close read, not an "in a world" voice.
- **Not the previous film** (`video/launch/VIDEO.md`, the only earlier bible; frames not opened): world (paper/letterpress vs soil cutaway) · signature (orange dot strike vs ✓→seedling) · type (Geist + Instrument Serif + stamped caps vs BioRhyme + Georama + root-drawn monoline) · motion (impact/stamp vs growth/organic) · camera (flat, dot wipes vs vertical 2.5D travel) · colour script (paper/ink/orange vs grey→loam→dawn) · sound (letterpress thunks, marimba vs dry ticks → plucks + earth, rising-fifths motif) · structure (problem→strike→chapters vs cold open → three beats with a break → silence → climax → callback). **8 axes differ.**
- **Within the brand:** no Streak brand exists; the film defines it (logged as Agent judgment).
- Close call, logged: the launch film's beat 2 is "a wall of the cliché"; this film's beat 1 is "the category's cliché UI" too. Both stage the cliché before the product. The device is different (no wall, no clone, no knock-over) but the *structure* problem→turn is shared; the genre table lists problem→reveal as a standard launch structure.

### Escalation moves (§6) and where they land
1. **Rule of three with a break** — 11.25 s "Show up. It grows." → 15.0 s "Keep going. It fills in." → 20.0 s "Miss a day? It wilts. **No reset.**" (the third beat breaks the pattern, colour turns crimson).
2. **Silence before the payoff** — 24.40–24.95 s: music and SFX cut to zero and the camera's breathing stops; 25.0 s impact.
3. **Callback** — 40.35 s: the opening's 30-cell checkmark grid returns, every cell sprouting a seedling.
Also used: **scale contrast** at the climax (macro on a thick root at 25.2 s → whole root system by 28 s) and the **match cut** inside the signature device (✓ → seedling).

## 2. Tools
| Media | Source | Model / provider + version | Cost | Licence / commercial OK | Consent |
|---|---|---|---|---|---|
| Footage / imagery | Code-built (HTML/CSS/SVG in Chromium) | DENT video kit engine | 0 | Apache-2.0 (DENT kit); output ours | — |
| Voice | Local model | Qwen3-TTS 1.7B CustomVoice, preset `ryan`, seed 7, instruct "Warm, close and unhurried, a quiet smile…" | 0 | Apache-2.0 (code + weights), commercial yes | Preset voice, no cloning |
| Music | Made in code | `score_streak.py` on the kit's `score.py` instruments (FM, Karplus-Strong, pads, drums, Schroeder reverb) | 0 | Ours (Apache-2.0 repo) | — |
| SFX | Made in code | same | 0 | Ours | — |

- **How it is made:** Render (code-built). Product UI is reenacted in HTML because the product is fictional; generative imagery declined by the user (scripted).
- **Build tool:** DENT video kit (`composition.html` + `render.py` + `timeline.json`), `techniques.js` (`morph`, `rand`, `shockwave`). Fonts loaded from Google Fonts at render time.
- **Licences:** BioRhyme, Georama, Sometype Mono — SIL OFL 1.1 (Google Fonts; `fonts.py check`: fresh enough, open source). Playwright (Apache-2.0), FFmpeg (LGPL/GPL build), NumPy (BSD) — tools only.
- **Modern Web Guidance:** `mwg.py search` for SVG stroke animation / variable fonts returned font-loading and stagger guides; none applies to a frame-by-frame render page (no layout shift, interaction or network concerns). No MWG guide shaped the code.

## 3. Script (narration 66 words; read-aloud timing measured from the rendered lines, 1.0–4.2 s each)
| # | Time | Voice-over | On-screen text | Visual | Sound |
|---|---|---|---|---|---|
| 1 | 0:00–0:04.4 | "Twenty-nine days in a row." · "One missed day. Back to zero." | DAY STREAK 1→29 · ✗ · **0** | Sterile checkmark grid fills on accelerating ticks; day 30 ✗; counter slams to red 0; every ✓ flies off | 29 dry ticks rising in pitch, buzz, slam, clatter; cold hum |
| 2 | 0:04.4–0:07.4 | "What if a habit grew, instead?" | — | One ✓ survives, hangs, falls into the soil (squash), morphs into a seedling; camera sinks underground | Falling whistle, soil thud, the sprout motif D–A–E, creak |
| 3 | 0:07.4–0:10 | "Meet Streak." | **streak** (root-drawn) · *habits that* grow | One root writes the name; the k's leaf opens | Plucked arpeggio per letter, bud pop |
| 4 | 0:10–0:15 | "Every time you show up, your habit grows a leaf." | **Show up.** It **grows.** | Camera rises; the phone is planted in the soil; Today list; four habits watered on the beat, each grows a leaf; roots extend below | Groove enters; droplet + leaf pluck per tap |
| 5 | 0:15–0:20 | "Keep showing up, and the garden fills in." | **Keep going.** It **fills in.** · Day 12→60 | Garden tab; 48 days in 3.6 s: plants grow and flower | Accelerating arpeggio, creaks |
| 6 | 0:20–0:24.95 | "Miss a day? It wilts. It doesn't reset." | *Miss a day?* **It wilts. No reset.** | Day 61: Walk droops and turns ochre; banner "It's wilting, not reset. Water it today."; 0.55 s of stillness | Groove thins, falling FM, two low hits, riser — then silence |
| 7 | 0:25–0:32.5 | "Because the days you showed up are still there. In the roots." | WALK 20 MIN · 47 DAYS OF ROOTS · STILL HERE · **streak** · *The days you showed up* stay. | Push through the screen (Roots tab) into full-frame roots: macro → whole; title written in light at the peak | Impact, full arrangement, taiko + bell at the title |
| 8 | 0:32.5–0:40 | "Streak. For iPhone and Android." | **One garden.** *iPhone +* **Android.** | Dawn; two phones (iOS-style and Android-style frames) planted side by side; Walk is watered and revives; widget pops in | Bright plucks, droplet, pop |
| 9 | 0:40–0:45 | "Grow habits. Not checkmarks." | **streak** · *Grow habits,* **not checkmarks.** · ON IPHONE AND ANDROID · Concept demo · Streak is fictional | Callback: the opening grid returns and every cell sprouts; the name is drawn; held with sway | Sprout pops, sonic logo, bloom |

Words per minute: 66 words over ~29 s of speech ≈ 136 wpm; Qwen3 lines rendered at 1.0–4.2 s each.

## 4. Storyboard
The contact sheets in `review/` are the storyboard (stills at 28 key times per ratio, reviewed before the final render). Transition grammar: the horizon crossing (5.1, 6.25–7.4, 10.0–10.9, 32.5–33.4, 40.0–40.75 s); in-app transitions are device-native (segmented-control slide at 15.0 s); one exception, the push through the screen at 24.95–25.4 s.

## 5. Animatic
Timing locked in `timeline.json` (built by `make_timeline.py` from `vo/narration.timing.json` and the 96 bpm grid) and checked through still sheets; no separate scratch animatic was rendered.

## 6. Sound
- **Narration:** Qwen3-TTS 1.7B, `ryan`, seed 7, `tts.py say` → `tts.py post` (−16.1 LUFS, −1.5 dBTP, PASS) → lines cut from `narration.wav` by `narration.timing.json` and placed on the grid by `score_streak.py` (`timeline.json` → `vo[].at`).
- **Music:** original, synthesised (see bible). **SFX:** ticks, buzz, slam, clatter, whistle, soil thud, droplets, creaks, pops, impact, riser.
- **Mix:** music ducked up to −11 dB under voice (envelope sidechain), SFX ducked −3.7 dB; act 1 dry (no reverb), reverb from 4.4 s; mastered to −14 LUFS, true peak ≤ −1.5 dBTP.
- **Listening:** not heard by a person. Inspected as a spectrogram and waveform only (`review/score-spectrum.png`, `review/score-wave.png`). **Sound is unverified.**

## 7. Captions
`film.srt` (12 cues, ≤ 42 characters per line, ≥ 1 s each), burned into both cuts (Georama 600 on a dark plate). Text matches the narration script; not checked by speech-to-text (Whisper is not installed: `doctor.py` → "whisper: not found").

## 8. Export
| Version | Resolution | FPS | Codec / container | Loudness | File |
|---|---|---|---|---|---|
| 16:9 master | 1920×1080 | 60 | H.264 yuv420p TV-range BT.709, AAC 256k / MP4 | −14 LUFS | `out/film-16x9.mp4` |
| 9:16 cut | 1080×1920 | 60 | same | −14 LUFS | `out/film-9x16.mp4` |

## 9. QA
See `QA.md` for the pasted `video_qa.py` output, the renderer's layout-check summary and the contact sheets.
- [x] `video_qa.py` run on both cuts (results in QA.md) and the sheets looked at
- [x] Contact sheet of stills reviewed before the final render; fixes listed in QA.md
- [x] Genre bar stated; bible followed; originality guard passed
- [ ] Sound heard by a person — **unverified**
- [x] Message understood with sound off (on-screen statements + burned captions) — agent's own check on the stills, not a stranger
- [x] First 3 seconds hook: a ticking grid at 29 days, the ✗ at 3.1 s
- [x] No typos (read twice); claims stay inside the fictional spec; demo label on screen whenever the app is
- [x] Loudness on target (−14 LUFS)
- [x] 9:16 safe areas: layout check run
- [x] No flashing > 3/s
- [x] Licences recorded
- [ ] Product truth ≥ 60 %: **51 % strict / 67 % if the Roots-tab climax counts** (see §1)

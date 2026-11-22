# Video Plan: "Signed, Not Said", how passkeys work

> DENT video plan (`/dent:video`, eval scenario S27, explainer run). Built with `skills/dent/commands/video.md` from this worktree.
> Nobody answered questions in this run: every question the skill told me to ask is written below with the scripted answer used.

## 0. Questions asked (scripted answers)
| # | Question (as the skill says to ask it) | Source of the question | Answer used |
|---|---|---|---|
| 0 | How far should I take it? Essential · Standard (Recommended) · Polished · All-out (or "you decide") | SKILL.md §1.2 | **Polished** |
| 1 | Type and platform? | video.md step 1 | Explainer (given in the prompt); **16:9** |
| 2 | Length? | video.md step 1 | 60 s (given in the prompt) |
| 3 | Where does the footage/imagery come from? (code-built / local model / cloud / own assets) | video-tools §1, media-sourcing §2 | **Code-built in the browser** |
| 4 | Where does the voice come from? (`tts.py engines` first) | voice-and-narration §1 | **Local Qwen3-TTS** (installed, registered at `D:\SKILLS\.dent-media`) |
| 5 | Commercial use? | voice-and-narration §1.2 | Not asked in the script; Qwen3-TTS is Apache-2.0, commercial OK either way |
| 6 | Where does the music come from? | media-sourcing §5.2 | **Made in code** (`score.py`) |
| 7 | Gate: how do you want to shape the film's look and feel? | creative-direction §2 | **Let me pick the ingredients** |
| 8 | A. Feel and energy | §2 A | **Calm and precise** |
| 9 | B. Typography | §2 B | **Kinetic type as the main visual + custom lettering for the title** |
| 10 | C. Motion language | §2 C | **Morph and match + cinematic camera** |
| 11 | D. Graphics and imagery | §2 D | **Illustration + data visualisation** |
| 12 | E. Sound | §2 E | **Narration + score + SFX** |
| 13 | F. Never | §2 F | **"No padlock icons, no hooded hackers"** |
| 14 | Built-in browser surfaces / motion menu (SKILL.md §1.2 "any visual build at Standard+") | SKILL.md §1.2 | Not asked: a rendered film has no interactive surfaces, and the creative menu's motion-language group replaces the motion menu. Logged in RESULT.md. |
| 15 | Script approval (video.md step 5) | video.md | Assumed approved (no one to answer) |

## 1. Brief
- **Type and sub-type:** Explainer → kinetic typography with line illustration (concept-first structure, `video-types-and-craft.md` §3).
- **Audience and where they'll watch:** people tired of passwords; not technical. YouTube / a help page / social, often on a laptop; sound on for the voice, but burned-in captions so it survives sound off.
- **One message:** A passkey is a signature your device makes, not a secret you hand over, so there's nothing to steal or phish.
- **Call to action:** Look for "Create a passkey" in your account settings.
- **Length and aspect ratio:** 63.5 s (59.9 s narration + end card), 16:9, 1920×1080, 60 fps.
- **Tone / mood words:** calm, precise, clever. **Anti-words:** alarmist, techy.
- **Creative concept:** a password is a secret you *say*; a passkey is a *signature* only your device can write, and the site keeps just the specimen it checks against.
- **Must show:** public/private key pair; private key stays on the device; site stores only the public key; challenge → signature → check; domain binding (phishing resistance); unlock with face, fingerprint or device PIN; sync through a keychain or password manager.
- **Must not show:** padlock icons, hooded hackers (user's never); real brands or real domains (sites are `*.example`, the reserved documentation TLD); invented statistics (none used); a real key (the digits on screen are random and labelled "illustration · not a real key").
- **Three answers (products only):** N/A, this explainer is about a technology, not a product. The equivalent test: after one sound-off viewing a stranger can say *what it is* (a signature from your device instead of a shared secret), *why it's safer* (nothing secret leaves the device, lookalike sites get nothing), *how to get it* ("Create a passkey" in account settings).

### Facts used, and how they were checked
| Claim in the narration | Basis |
|---|---|
| Your device makes a pair of keys (public-key cryptography) | WebAuthn creates a key pair per site; MWG `passkey-registration` (server stores `credentialPublicKey`, "public key used to verify assertion signatures") |
| The private key never leaves it | Private keys stay inside the authenticator / platform keychain. Nuance: synced passkeys are copied end-to-end encrypted between the user's own devices (said in line 9) |
| Only your face, fingerprint or PIN unlocks it | User verification uses the device's screen lock (biometric or PIN). Nuance: a site may set `userVerification: "preferred"` (MWG `passkey-registration`), and devices without a screen lock can register without it. Simplified, not false, for this audience |
| The site keeps only the public key; it can check, never forge | Verification needs only the public key; signing needs the private key |
| The site sends a fresh challenge; the device signs it; the site checks | WebAuthn assertion: random server challenge, signed by the authenticator, verified with the stored public key |
| A stolen public key signs no one in | A public key cannot produce signatures |
| Each passkey is bound to the real site's domain; a lookalike gets nothing | The credential is scoped to the relying party ID (the site's registrable domain); the browser won't offer it to another domain. MWG `passkey-registration`: RP ID mismatch → `SecurityError` |
| Your keychain or password manager syncs them across your devices | Synced ("multi-device") passkeys via platform keychains / password managers; MWG `credentialDeviceType: "singleDevice" | "multiDevice"`. Nuance: device-bound passkeys (e.g. security keys) don't sync |
| No statistics | None in the film |

## 1b. Creative direction (`references/video/video-creative-direction.md`)
- **Creative menu answers:** see §0, rows 7–13.
- **Genre bar (explainer, §5):** "The mechanism made visible through one strong analogy that evolves." Structures: analogy-first · zoom from outcome into mechanism · build the system piece by piece. Clichés to avoid: icons popping in a row, clip-art people.
- **Directions offered (Polished = 2):**

### Bible A: "Signed, Not Said" (chosen)
```
NAME:              Signed, Not Said
LOGLINE:           A password is a secret you have to say out loud; a passkey is a signature only your device can
                   write, and the site keeps just the specimen it checks against (a bank's signature card, not a vault).
WORLD & MATERIAL:  Drafting vellum on a light table: a fine blue drafting grid, translucent layers, one technical pen.
                   Physics: ink is laid down at pen speed, never pops in; sheets slide, never fly.
SIGNATURE DEVICE:  The line that never lifts. One continuous pen line underlines the first "secret", rings the lookalike
                   page, becomes the device that keeps the key, the wire, the loop that binds the passkey to its domain,
                   the thread between devices, and finally signs the title. Every scene change is this line morphing.
TYPE:              Kinetic type as the actor: Zalando Sans (variable wght 200–900, wdth 75–125) — every spoken word rises
                   out of a mask on its exact Whisper word time and settles from weight 250 to its target; key words
                   (secret, signature, never, keys, challenge, nothing) land wide and black. Chivo Mono for domains,
                   keys and the wire log. Custom lettering: "passkey" as a monoline technical-pen script drawn for this
                   film; the y's descender never ends: it swings back under the word as a signature flourish; the k's
                   leg ends in a small key-bit notch.
MOTION LANGUAGE:   Morph and match (dominant): the pen line morphs scene to scene; words become objects (the word
                   "secret" IS the password that gets copied). Cinematic camera (second): slow push-ins, a far grid
                   layer in parallax, a pull-back at the sync scene. Easing: quartic out for arrivals, in-out for the
                   pen, springs (f 2.4, z .5) on word weight. 60 fps; motion blur on key flights.
TRANSITIONS:       The pen-line morph + a 0.35 s cross-dissolve of the sheets. Exception (climax): a hard cut with 0.6 s
                   of silence into the lookalike domain.
CAMERA:            2.5D drift: content plane + far grid plane (parallax 0.4); push 1 %/s per scene; pull-back at sync.
COLOUR SCRIPT:     Act 1 (passwords) daylight vellum, graphite ink, the secret in magenta (magenta = must never travel).
                   Act 2 (the mechanism) the light table switches off: indigo night, blue = public/checkable, magenta
                   stays only on the private key. Act 3 (climax) near-black, only the two domains lit. Act 4 (sync, CTA)
                   back to daylight, now drawn in blue: the secret colour is gone from the world.
SOUND WORLD:       Felt FM e-piano and sub at 80 bpm in F (Fadd9 · Dm7 · B♭maj7 · C6/9); Karplus "pen-tap" plucks enter
                   with the mechanism; glassy and sparse at night; designed SFX: pen on vellum, paper slides, soft ticks,
                   digit chatter, glass chime on "valid", a hollow knock for "nothing". Silence: the 0.6 s before the
                   lookalike. Sonic logo: call (rising fourth = the challenge) and answer (resolved third = the signature).
STRUCTURE:         Concept-first, built piece by piece (times from the final narration): hook 0–6.9 s (the secret
                   handed to every site) · problem 6.9–11.4 s (copies, a lookalike asks) · the idea 11.4–16.3 s (title:
                   a signature) · the mechanism 16.3–43.2 s (pair of keys, public key to the site, challenge-sign-check,
                   what crosses the wire) · the peak 43.2–48.8 s (domain binding, the lookalike gets nothing) · sync
                   48.8–53.5 s · callback + CTA 53.5–63.5 s.
THE MOMENT:        "bank.example" vs "bank.examp1e" in giant mono on black, the 1 lit magenta, "No passkeys for this
                   site" beneath, and the pen line conspicuously absent.
NEVER:             padlocks, shields, hooded hackers, skulls, binary rain, clip-art people, icons popping in a row,
                   real brands, invented numbers.
```
Style frame: `styleframe-a.jpg` (the climax, 45 s, rendered from the composition).

### Bible B: "Two Rooms" (offered, not chosen)
```
NAME:              Two Rooms
LOGLINE:           Your secret lives in a room with no door out; the website only ever hears its echo.
WORLD & MATERIAL:  Isometric architecture drawn in light on a deep-green night: rooms as line boxes, a warm glow inside.
SIGNATURE DEVICE:  The echo: ripples from the private key cross into the site's room as rings it can measure but
                   never trace back to a source.
TYPE:              Editorial voice in the world: Playfair (opsz/wdth) set on the walls of the rooms, italic for the
                   human half of each line; Sometype Mono labels. Custom lettering: a "passkey" monogram cut as a doorway.
MOTION LANGUAGE:   Cinematic camera (dominant): one impossible continuous move from room to room; morph secondary
                   (rooms fold into devices).
TRANSITIONS:       None: the camera never cuts (one take); exception: the lookalike room is a cut to a mirror image.
CAMERA:            Isometric 3D travel, constant 2 %/s, one 90° orbit at the climax.
COLOUR SCRIPT:     Green night throughout, a single warm amber key-light that dims as the film reaches the server room
                   and comes home at the end; dawn grade on the CTA.
SOUND WORLD:       Low room-tone drones, reverberant rooms per scene, sonar-like pings for the echo; no beat.
STRUCTURE:         Journey: from your pocket, out along the wire, into the server room, back; the peak is the mirror room.
THE MOMENT:        The camera inside the server room, looking back at a warm glow it can never reach.
NEVER:             padlocks, hooded hackers, vault doors.
```
Style frame: `styleframe-b.jpg` (rendered from `styleframe-b.html` with `render.py stills --page styleframe-b`).

**Axes on which A and B differ (≥ 4 required):** world (vellum + pen vs. isometric light architecture), signature (unbroken pen line vs. echo ripples), type (kinetic variable sans + monoline lettering vs. editorial serif in the world), dominant motion (morph vs. continuous camera), camera (2.5D drift vs. one isometric take), colour script (day → indigo → black → day vs. green night + amber), sound world (felt keys + pen foley on a beat vs. drones and pings, no beat), structure (built piece by piece vs. a journey). 8 of 8.

**Chosen:** A ("you decide" pick on the user's behalf, because the user asked for kinetic type as the main visual and morph-and-match as the motion language; B is camera-first and serif-editorial, a weaker fit for those answers).

## Originality guard (§4) on bible A
| Check | Result |
|---|---|
| No orange-dot transitions | Pass: the transition is a blue/magenta pen-line morph, no dot, no circle wipe (the kit's `wipe()` is removed) |
| No letterpress strike or "impression" | Pass: ink is drawn by a pen, nothing is stamped or pressed; the lettering is monoline and stroked |
| No wall of identical templates knocked over | Pass: five site cards fan in and stay; nothing is knocked over |
| No split-flap board | Pass: digits are typed/cycled in place in a mono face, no flaps |
| No numbered "It asks / It names / It checks" chapters | Pass: no chapter numbers; structure follows the narration |
| No "this film was made with" ending | Pass: ends on the user's own action (Create a passkey) |
| Not the genre's clichés (explainer: icons popping in a row, clip-art people) | Pass with one watch item: face / fingerprint / PIN are three line drawings on one row; they are pen-drawn on their spoken word (0.5 s apart), not popped, and there are no people |
| User's never: padlocks, hooded hackers | Pass: no padlock, shield, vault, hacker or villain anywhere; the "attacker" is only a lookalike web address |
| Not the previous film: `video/launch/VIDEO.md` ("The Impression") | Differs on world (paper + letterpress vs. vellum + pen), signature (orange dot vs. unbroken line), type (Geist + Instrument Serif vs. Zalando Sans variable + Chivo Mono + monoline script), transitions (dot wipe vs. line morph), colour script (paper/ink/orange vs. vellum → indigo → black → vellum, blue/magenta), sound world (D minor groove, woodblock, thunks vs. F major felt keys at 80 bpm, pen foley, glass), structure (launch reveal with numbered chapters vs. concept-first explainer), camera (locked + push vs. 2.5D parallax + pull-back). 8 axes. |
| Not the kit placeholders | Pass: kit fonts (Mozilla Headline / Newsreader / Datatype), colours, circle wipe, numbered chapter and terminal are all gone. Note: `palette.py make --neutral cool` returned exactly the kit's placeholder paper and ink (`#F6FAFC` / `#111619`); I shifted the vellum to `#EEF2F6` and logged it as an Override. |
| Within the brand | N/A: no product brand; the film's own system is defined above |

## Escalation moves (§6) and where they land
1. **Silence before the payoff** (L8, 46.5 s): a hard cut to black with 0.6 s of narration silence and a music drop, then "bank.examp1e" and "A lookalike gets nothing."
2. **Callback** (53.5 s): the film opens on "a secret you hand over" and closes on "Stop handing over secrets"; the title lettering that was first drawn in the indigo night is re-signed in daylight blue.
3. **Scale contrast / pull-back** (L9, 48.8 s): after the tight black climax, the camera starts close and pulls back to three devices joined by the same pen thread.
(4. Material transformation, implicit: the magenta "secret" colour leaves the world after act 1 except on the private key, and is gone in act 4.)

## 2. Tools
| Media | Source | Model or provider + version | Cost | Licence / commercial OK | Consent |
|---|---|---|---|---|---|
| Imagery | Code-built (HTML/SVG in headless Chromium via the kit's `render.py`) | Playwright Chromium 159 | free | Apache-2.0 (kit); output ours | — |
| Voice | Local Qwen3-TTS 1.7B CustomVoice, preset `ryan`, `--instruct` calm/precise/warm, seed 11, `--lang English` | Qwen3-TTS | free (local GPU) | Apache-2.0, commercial OK; synthetic voice, disclose where required | Preset voice, no cloning |
| Music | Synthesised in code (`score.py`, "drafting" arrangement added to this film's copy) | — | free | Ours (Apache-2.0 repo) | — |
| SFX | Synthesised in code (`score.py`, film-specific pen/paper/glass set) | — | free | Ours | — |
| Fonts | Zalando Sans, Chivo Mono (Google Fonts, loaded at render) | — | free | SIL OFL 1.1 | — |
| STT check | faster-whisper `small.en` (int8, CPU) from the eval venv | faster-whisper 1.2.1 | free | MIT | — |

- **How it is made:** Render. Code-built scenes in the kit's browser engine; no capture (no product UI) and no generation.
- **Build tool:** DENT video kit (`templates/video-kit/`) copied here; engine, `render.py`, `techniques.js` (`lettering`, `morph`, `axisWave`, `rand`) used; `score.py` extended in this copy with the film's sound world.

## 3. Script (narration, take 2: 140 words)
| # | Voice-over | On-screen kinetic type | Visual | Sound |
|---|---|---|---|---|
| 1 | A password is a secret you hand over. To every site, every time. | A password / is a **secret** / you hand over. | Pen underlines "secret"; five `*.example` site cards fan in, each gets a copy of "secret" | Room tone, pen, card slides, ticks |
| 2 | Sites keep copies. Fake sites ask just as nicely. | Sites keep copies. · Fake sites ask / just as nicely. | Copies become five data rows; a lookalike page `bank.examp1e` slides in and "secret" is typed into it | Ticks, slide, keys |
| 3 | A passkey isn't a secret you share. It's a signature only your device can make. | isn't a secret you share (struck) · a **signature** only your device can make. | Light table goes dark; the "passkey" lettering is written stroke by stroke | Pen per letter, strike |
| 4 | Your device makes a pair of keys. The private key never leaves it, and only your face, fingerprint or PIN unlocks it. | A pair of **keys.** · The private key **never** leaves it. · Only your face, fingerprint or PIN unlocks it. | Pen becomes a phone outline; a 78-digit private key (magenta) and a public key (blue) type in; face / fingerprint / PIN drawn on their words | Digit chatter, thud, pen x3 |
| 5 | The site keeps only the public key. It can check your signature, but never forge one. | The site keeps only the public key. · check ✓ · never **forge.** | Public key flies to `bank.example`; "check(signature) → valid"; a dashed forgery stutters and falls | Send, chime, failing pen |
| 6 | To sign in, the site sends a fresh challenge. Your device signs it, and the site checks. | fresh **challenge** · **signs** it. · **checks.** | Challenge digits travel the wire to the phone; signature travels back; "signature valid → signed in" | Digits, sends, pen, chime |
| 7 | No secret crosses the wire. A stolen public key signs no one in. | No **secret** crosses the wire. | Wire log: → challenge, ← signature, → signed in; the private key shivers but stays; a copied public key: "nothing to sign with" | Ticks, card, hollow |
| 8 | Each passkey is bound to the real site's domain. [0.6 s silence] A lookalike gets nothing. | **bound** to the real site's domain. · A lookalike gets **nothing.** | Giant `bank.example`, the pen loops around it; hard cut to black: `bank.examp1e`, the 1 lit; "No passkeys for this site"; the pen is absent | Pen, dry cut hit + silence, hollow knock |
| 9 | Your keychain or password manager syncs them across your devices. | … **syncs** them across your devices. | Daylight returns; pull back to phone, laptop, tablet joined by the pen thread | Pen x3, chime |
| 10 | Stop handing over secrets. Look for "Create a passkey" in your settings. | Stop handing over **secrets.** · [Create a passkey] | Lettering re-signed in blue; CTA button-shape held ≥ 3 s | Pen per letter, sonic logo |

Pace target ~140–160 wpm. Take 1 (153 words, "unhurried" instruction) ran 73 s; take 2 trimmed to 140 words with a "natural conversational pace" instruction. Measured result in §6.

## 4. Storyboard and animatic
The animatic is the composition itself rendered as stills at every scene's key moment (`render.py stills`), reviewed as a contact sheet before the full render (§9).

## 6. Sound
- **Narration:** Qwen3-TTS 1.7B, `ryan`, seed 11, mastered with `tts.py post` (−16 LUFS stem, 0.4 s gaps), mixed under the score by `score.py --voice` (music ducked under speech), final mix −14 LUFS.
- **Music / SFX:** see bible A sound world; all synthesised.
- **Measured:** narration stem −16.0 LUFS / −1.5 dBTP; film −14.0 LUFS / −1.7 dBTP; STT on the final mix recovers every line. Not heard by a person.

## 7. Captions
Burned in (from `vo/narration.srt`, ≤ 42 characters × 2 lines) and sidecar `film-16x9.srt` / `vo/narration.vtt`.

## 8. Export
| Version | Resolution | FPS | Codec | Loudness | File |
|---|---|---|---|---|---|
| Master | 1920×1080 | 60 | H.264 yuv420p TV-range BT.709 / AAC 256k | −14.0 LUFS | `film-16x9.mp4` (23.9 MB, not committed) |
| Preview | 1920×1080 | 60 | H.264 CRF 25 / AAC | same | `film-16x9-preview.mp4` (8.3 MB) |
| Captions | — | — | SRT / VTT | — | `film-16x9.srt`, `film-16x9.vtt` |

Rebuild: `tts.py say` (vo/script.txt; line 8 re-rendered, see QA.md) → `tts.py post` → `<whisper python> build_timeline.py` → `python score.py --voice vo/narration.wav` → `python render.py video`.

## 9. QA
video_qa: **all measured checks pass** after one fix (variety 26.8 s → 7.8 s). Layout check clean. Details, contact-sheet notes and the remaining visual nits: `QA.md`. Score: `SCORECARD.md` (self-review, 7.1/10, below target; sound unverified).
- [x] video_qa passes and I looked at the sheet
- [x] Contact sheet reviewed before the final render; fixes listed
- [~] Genre bar: the analogy (signature vs. said secret) evolves through the film, but the middle act leans on repeated diagrams
- [ ] Sound heard by a person (unverified, line ≤ 6)
- [x] Message readable with sound off (captions + kinetic type)
- [x] First frame has motion (typed password field)
- [x] Claims true, no invented numbers
- [x] Loudness on target
- [x] No flashing > 3/s
- [x] Licences recorded (§2)
- [x] ffprobe: 63.5 s, h264 1920×1080 60/1 + aac

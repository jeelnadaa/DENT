# Video Creative Direction: invent the film, keep the bar

DENT's own launch film is the quality bar, **not the template**. What made it exceptional splits into two kinds of thing, and DENT treats them differently:

| | Quality invariants (every film, every genre) | Creative choices (invented fresh for every film) |
|---|---|---|
| What | Measurable craft that every great film shares | The film's identity |
| Examples | Something changes at least every 0.5 s; no dead frames; every event timed to a grid (beat or voice); one coherent transition grammar; designed sound for every event; type and colour from a system; a contact sheet reviewed before rendering; `video_qa.py` passes | Concept and metaphor, visual world and materials, signature device, typography, motion language, transition family, camera, colour script, structure, sound world, the one moment people screenshot |
| Where | `video-types-and-craft.md` §4b, `templates/video-kit/README.md`, `scripts/video_qa.py` | This file: the menu (§2), directions (§3), originality guard (§4), genre bar (§5), escalation (§6) |

Copying the launch film's devices produces clones. Copying its **ambition and craft** produces new films that are just as strong. Used by `/dent:video`, `/dent:launch-video`, `/dent:motion-graphics`.

---

## 1. The process (Standard and above)
1. **Brief:** the one message, the audience, the genre and the three answers (what is it, what does it do for me, how do I get it; `video-types-and-craft.md` §2b for products).
2. **Ask the creative menu** (§2), skipping what the user already said.
3. **Invent 2–3 directions** (§3) that differ on at least four axes, each as a short film bible with one rendered style frame. Polished: 2; All-out: 3; Standard: 1 recommended + a one-line alternative. Let the user pick or combine.
4. **Run the originality guard** (§4) on the chosen bible.
5. **Choose 2–3 escalation moves** (§6) and write where they land in the timeline.
6. **Build** with the kit's engine, following the bible's rules exactly; meet every invariant; review stills; render; `video_qa.py`; watch it with sound off and on.

## 2. The video creative menu (ask; one question at a time; multi-select where marked)
Respect the question tool's 4-option limit: start with the gate question, then ask only the groups the user wants.

**Gate:** "How do you want to shape the film's look and feel?" · *Show me 3 directions to choose from (Recommended)* · *Let me pick the ingredients* · *You decide everything* · *I have references* (free answer).

If they pick ingredients, ask these (each multi-select, plus "You choose"):

**A. Feel and energy** (single choice): *Cinematic and epic* · *Witty and playful* · *Calm and precise* · *Raw and rebellious* · free answer.

**B. Typography** (multi-select)
| Option | What it means in the film |
|---|---|
| Custom lettering | A wordmark or title drawn for this film (SVG paths), with its own detail (ink traps, cuts, a ligature, a moving part) |
| Kinetic type as the main visual | Words are the actors: they build, break, stretch, stack, travel |
| Editorial voice | A contrast of faces (e.g. grotesk statement + serif or italic soul, or wide + condensed) carrying the emotion |
| Type in the world | Letters printed, projected, stamped, carved or lit on surfaces and objects in the scene |
| Minimal type | Images carry the film; type only for name, captions and the call to action |

**C. Motion language** (multi-select, pick 1–2 dominant)
| Option | Feels like |
|---|---|
| Physical | Gravity, weight, impact, squash and stretch, springs, debris |
| Cinematic camera | Push-ins, parallax depth, rack focus, a continuous move through space |
| Hand-made | Frame-by-frame, boiling lines, stop-motion jitter, cut-paper |
| Morph and match | Shapes become other shapes; match cuts carry the eye between scenes |
| Mechanical precision | Grids, split-flaps, counters, snapping, clockwork timing |
| Liquid and organic | Flow, blobs, ink in water, growth |
| Digital and glitch | Scanlines, datamosh, RGB split, pixel sorting (flashes kept under 3/s) |

**D. Graphics and imagery** (multi-select)
| Option | Built with |
|---|---|
| Real product UI and captures | Faithful reenactments and screen recordings of the real thing |
| Illustration | Linework, flat shapes, painterly, isometric (SVG/Canvas) |
| 3D | Objects or scenes (Three.js in the composition, or Blender renders) |
| Collage and print | Paper, halftone, torn edges, riso overprint, photocopies |
| Data visualisation | Real numbers drawn as charts, maps, races |
| Photography or footage | The user's own, captured, or generated for atmosphere only (`../media-sourcing.md`) |
| Generative and abstract | Shaders, particles, noise fields, procedural patterns |

**E. Sound** (single choice, then `../media-sourcing.md` for sources): *Narration + score + SFX* · *Score + SFX, no voice* · *Sound design only, no music* · *Silence and a few hits (bold)*.

**F. Never** (free): "Anything you never want to see or hear?" Record it as a hard rule in the bible.

## 3. Directions: the film bible (one per direction, ≤ 15 lines each)
```
NAME:              a two-word name for the direction
LOGLINE:           the film in one sentence, built on a metaphor from outside the product's category
WORLD & MATERIAL:  what the film is made of (paper, glass, light, clay, terminals, water…) and its physics
SIGNATURE DEVICE:  one invented move that is this film's own and recurs (never borrowed from DENT's film, §4)
TYPE:              faces + any custom lettering + how type moves
MOTION LANGUAGE:   1–2 dominant languages from menu C + the rules (easings, physics constants, frame rate)
TRANSITIONS:       one family + the single exception (the climax cut)
CAMERA:            locked, drifting, travelling, 2.5D, 3D…
COLOUR SCRIPT:     how colour changes across the acts (not just a palette)
SOUND WORLD:       instruments/sources, tempo or pulse, where the silence is, the sonic logo
STRUCTURE:         acts with timings, where the proof sits, where the peak is
THE MOMENT:        the frame people will screenshot
NEVER:             what this film will not do (user's "never" + clichés)
```
Directions must differ on at least four of: world, signature, type, motion language, camera, colour script, sound world, structure. Render one **style frame** per direction (a still from the kit at its key moment) so the user chooses by eye.

## 4. Originality guard [Rule]
- **Not DENT's devices.** Unless the user's own brand owns them or the user asks: no orange-dot transitions, no letterpress strike or "impression", no wall of identical templates being knocked over, no split-flap style board, no numbered "It asks / It names / It checks" chapter pattern, no "this film was made with" ending. These are the launch film's identity; reusing them makes a clone.
- **Not the genre's clichés** (§5 lists them per genre).
- **Not the previous film.** Read the bibles of earlier films in the project (`video/*/VIDEO.md`) and differ on at least four axes from each.
- **Within the brand.** Originality stays inside the product's identity (DESIGN.md): new direction, same brand.
Log the guard's result in VIDEO.md.

## 5. The bar in each genre
"Insane" means something different in each genre. Aim for that genre's best, with its own structure:

| Genre | What exceptional looks like | Structures to choose from | Clichés to avoid |
|---|---|---|---|
| **Launch reveal** | The product's essence becomes a physical or visual event; name by ~9 s; real product proof; a peak and a clean end card | Problem→strike→reveal→proof→CTA · cold open in the product→pull back to the world · before/after transformation · one continuous shot | Logo spin intro, generic dashboard tilt, stock people, "introducing…" voice |
| **Teaser** | One unforgettable image or sound, withheld information, a date | A single escalating shot · fragments that almost assemble · sound-first | Revealing everything, countdown clocks by default |
| **Manifesto** | A belief that makes people nod, set in type and sound with conviction | Statement–counterstatement · list that escalates · a single sentence building across the film | Inspirational stock montage, generic piano |
| **Feature tour** | Each feature as a vivid micro-story with its own visual idea, one transition grammar linking them | Chapters · a journey through one user's day · a single object morphing through features | Bullet lists on screen, same shot repeated per feature |
| **Trailer** | Rhythm, rising stakes, a twist, title at the peak | Three-act build with a drop · reverse chronology · question→answer | Whoosh on every cut, deep "in a world" voice |
| **Explainer** | The mechanism made visible through one strong analogy that evolves | Analogy-first · zoom from outcome into mechanism · build the system piece by piece | Icons popping in a row, clip-art people |
| **Product demo / tutorial** | Real UI, readable, zoomed to the action; the viewer could repeat it | Task-led · problem→steps→result · speed-run then slow-down | Tiny unreadable UI, cursor wandering |
| **Social short** | A hook in frame 1 with sound off, a loop or payoff by 15 s, vertical-native composition | Hook→twist→payoff · satisfying process · loop | Landscape cut cropped to vertical, intro titles |
| **Ad (6–30 s)** | One idea, one feeling, one action | Single gag · demonstration · comparison | Cramming features |
| **App store preview** | Feature per beat in real UI with device-native motion | Feature beats · day-in-the-life | Marketing claims instead of UI |
| **Title sequence / brand film** | A typographic or material idea that sets the tone and returns at the end | Material transformation · type as architecture · one evolving shape | Particles and lens flares as filler |
| **Data story** | One insight that lands visually; every number honest and sourced | Reveal the scale · race · zoom from one to all | 3D pie charts, unlabelled axes |
| **Case study** | The customer's real problem and real result, told with their material | Before→decision→after · voice of the customer | Invented quotes, vague outcomes |
| **Music or lyric video** | Picture and rhythm fused; type or image performing the song | Kinetic lyric · visualiser with a concept · story | Lyrics as static subtitles |
| **Motion-graphics loop** | A satisfying, perfectly seamless idea | Transformation cycle · process loop | Visible loop seams, random decoration |

## 6. Escalation: moves that make a film exceptional (choose 2–3, invent the specifics)
- **Scale contrast:** cut from a macro detail to the whole world (or the reverse) at the peak.
- **Rule of three with a break:** two expected beats, the third breaks the pattern.
- **Silence before the payoff:** half a second to a second of near-silence and stillness, then the event.
- **The impossible continuous shot:** one move that travels through several scenes without a cut.
- **Match cuts:** a shape, motion or colour carries the eye from one world to the next.
- **The reversal:** the thing we thought was the problem turns out to be the solution (or the reverse).
- **Callback:** the ending answers the first frame.
- **Material transformation:** the product idea literally changes what the world is made of.
- **Hand-made detail:** custom lettering, a drawn texture, a sound recorded or synthesised for this film.
- **The meta moment:** the film reveals how it was made, or the viewer's own screen becomes part of it (use sparingly; DENT's film already used one).

## 7. From answers to the build (all inside the kit's browser engine)
| Choice | How to build it |
|---|---|
| Custom lettering | Draw SVG paths for the letters; animate path strokes, masks or per-letter transforms; keep real text for captions |
| Kinetic type | Split into lines/words/letters; masked reveals, variable-font axes (`wdth`, `wght`, `opsz`) animated over time, per-glyph springs |
| Physical motion | `fall()`, `spring()`, squash and stretch from velocity, shockwaves as expanding rings; motion blur windows on every fast move |
| Cinematic camera | A camera layer with `perspective` and `translateZ` per layer for parallax; slow push; rack focus with `filter: blur()` on depth layers |
| Hand-made | Re-seed an SVG turbulence displacement every 2 frames (boiling lines); hold poses 2 frames ("on twos"); paper textures |
| Morph and match | Interpolate SVG paths with the same point count; align shapes across a cut so the eye continues |
| Mechanical | Grids snapping on the beat, counters with `font-variant-numeric: tabular-nums`, stepped easing |
| Liquid and organic | SVG goo filters (blur + colour matrix), noise-driven blobs, metaballs in Canvas or WebGL |
| Glitch | Offset RGB channels, slice-and-shift strips, scanline overlays; keep flashes under 3/s |
| 3D | Three.js inside the composition, its clock driven by `render(t)` (never by real time) |
| Illustration and collage | SVG or Canvas layers, masked images, torn-edge masks, halftone via SVG filters |
| Data | Real values, scales computed in JS, axis and source on screen |
| Generative | Seeded noise and shaders driven by `t` so every render is identical |

Licences for any library or asset go into VIDEO.md §10 (`../catalog/asset-sources.md`).

# DESIGN.md — Strut modular desk lamp page

> Source of truth for this page. Read before changing anything; add a changelog line for every change.
> Effort: All-out · Date: 2026-11-14 · Files: `index.html`, `img/` (147 still frames), `favicon.svg`, `apple-touch-icon.png`, `og.jpg`

## 1. Concept
**"An engineer's assembly drawing pinned above a workbench — and at night, one pool of light."**
Mood: precise, tactile, warm · Anti-words: glossy-tech, cute.
Category cliché (Apple-style white seamless, centred product, thin sans) → diverged on **type** (heavy industrial caps), **layout** (ruled drawing grid, "Fig. 1" title block, numbered vermilion callouts) and **colour** (paper + ink + one signal colour; dark mode is a warm night room).
Base style **Utilitarian** + accent **Premium Product** (one product moment). Signature elements: (1) exploded assembly view with numbered callouts, (2) the switch-on pool of light.

## 2. Decision log
| Decision | Choice | Why | Source |
|---|---|---|---|
| Effort | All-out | User choice | User |
| Name | "Strut" (fictional, labelled concept) | No brand given | User (asked me to name it) |
| Modularity | 5 swappable modules + explode view | Makes "modular" visible | User |
| Commerce | Plausible sample values, each marked †, footnote + footer | Honest product page | User + DENT §3 honesty |
| Theme | Light + dark, system default, persisted toggle, no flash | | User |
| Light | On/off switch + 2700–5000 K warmth | Shows what the product does | User |
| Sound | Opt-in synthesized click/tick/clack, off by default | | User + DENT G11 |
| Direction | A (assembly drawing) + B's light moment; realistic lamp + joints | | User |
| Fonts | Cabinet Grotesk 800 (display) + Satoshi (text, tracked caps labels, tabular numerals) | User wanted Satoshi + a grotesque; mono dropped so only two families | User + Override of tile A's mono |
| Engine | three.js r160 via import map, dynamically imported | Physical product → real 3D; page never waits on it | DENT `motion/3d-and-realtime.md` |
| Model | Built in code: lathe base/turret/shade, clevis cheeks, knurled friction knobs, hex bolts, washers, twin rods, helical springs, cable threaded between rods | No licensing risk; full control of modules | User + Agent judgment |
| Materials | MeshPhysical; brass = metal + anisotropy + procedural brushed roughness; RoomEnvironment reflections | Realism without an HDRI download | DENT 3D §2 + Agent |
| Fallback | "Lite" turntable of 24 stills × 3 finishes × off/on + exploded still, rendered from the same scene | Same look, works without WebGL, cheap on old phones | Agent judgment |
| Lite triggers | No WebGL → Lite (3D button explains); software GL / Save-Data / ≤2 GB / ≤2 cores → Lite + "Load 3D view" / "Not now"; fps guard: DPR 1 → shadows off → offer Lite | Graceful degradation | DENT 3D §4 + Agent |
| Touch | `touch-action: pan-y` on the viewer: sideways swipe turns, vertical swipe scrolls; zoom disabled (no scroll trap); "Close-up" button instead | Plan audit #4 | Agent |
| Phone layout | Fig label bar sits above the viewer; toolbar two rows; sticky buy bar once "Add to bag" scrolls away | Mobile designed, not shrunk | DENT responsive |

## 3. Tokens
Light: paper `#F1EEE7`, paper-2 `#E7E2D6`, ink `#1C1B19`, ink-2 `#4E4940` (7.7:1), ink-3 `#6B655A` (5.0:1, control borders), rule `#CFC7B6` (decorative only), signal `#B8361A` (5.1:1 on paper; white on it 5.9:1).
Dark: night `#15130F`, ink `#EEE8DD` (15.2:1), ink-2 `#C3BAAA` (9.7:1), ink-3 `#A2998A` (6.6:1), signal `#FF8160` (7.6:1; text on it `#1A0E08` 7.7:1), focus `#F3C47A` (11.5:1).
`--glow` = RGB of the current kelvin (drives the pool of light everywhere).
Spacing 4/8/12/16/24/32/48/64/96/128 · radius 2 px · tap 44 px · motion: 140 / 250 / 600 ms, `cubic-bezier(.2,.7,.2,1)`.

## 4. Components & states
Viewer (3D / Lite, loading, notice, hint, callouts, warmth slider), toolbar (rotate, reset, light switch `role=switch`, Modules `aria-pressed`, Close-up 3D only), finish radio group, buy button + toast + bag count, sticky buy bar, parts list linked to the viewer, FAQ `<details>`. Hover is pointer-only; every control has a focus ring.

## 5. Motion
Camera intro 900 ms (skipped with reduced motion), rotate 420 ms, explode 700 ms ease-out, finish cross-fade 280 ms, light 160–220 ms. Reduced motion: everything instant, no intro. No auto-rotation.

## 6. Sound
Web Audio, synthesized at runtime (no files): switch = filtered click + 140 Hz thump; tick = 4.2 kHz click; clack = double click. Master gain 0.22. Off by default, toggle in header, persisted. Nothing plays before a gesture.

## 7. 3D budget
~45 meshes, ~60 k triangles (springs are most of it), one 2048² shadow map, DPR ≤ 2. Rendering is on demand (only while something moves), paused offscreen and in hidden tabs; resources disposed on `pagehide`. three.js core ≈ 670 KB (≈170 KB gzipped) is fetched only when 3D is used. Each Lite still ≈ 15–40 KB; an idle Lite visitor loads one still, the other 23 of the current set load on the first turn.

## 8. Licences
| Asset | Source | Licence |
|---|---|---|
| three.js 0.160.0 (+ OrbitControls, RoomEnvironment, RoundedBoxGeometry) | cdn.jsdelivr.net | MIT |
| Satoshi, Cabinet Grotesk | Fontshare (Indian Type Foundry), api.fontshare.com | ITF Free Font Licence — free for personal and commercial use |
| Lamp model, stills, favicon, touch icon, OG image, icons, sounds | Made for this page | Original |

## 9. Changelog
- 2026-11-14 — First build (All-out). Directions in `directions.html`, plan in `PLAN.md`.

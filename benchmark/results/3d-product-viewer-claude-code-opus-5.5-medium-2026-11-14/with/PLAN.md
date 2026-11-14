# Implementation Plan: Strut — modular desk lamp product page

> DENT plan · Depth: Advanced · Effort: **All-out** · Date: 2026-11-14

## 1. Objective
- **Goal:** a single product page for a (fictional) modular desk lamp, "Strut", whose centrepiece is an interactive 3D viewer: rotate, change finish (matte black, brushed brass, white), see the five modules, switch the light on.
- **User problem:** shoppers can't judge a lamp's finish, joints and reach from flat photos; low-end devices must still get a good look.
- **Expected outcome:** opens from `index.html` on any device; 3D where it can run well, an image-based turntable where it can't.

## 2. Scope
**Included:** header, product hero (viewer + buy panel), modules section linked to the explode view, light section, specs, FAQ, footer; light/dark theme; opt-in sound; image-sequence fallback; favicon + OG image.
**Excluded:** real checkout, cart page, accounts, AR, other products.

## 3. Existing system (facts)
- Empty folder (PROMPT.md, QA.md only). No framework; plain HTML/CSS/JS, ES modules via import map.
- Fonts: Satoshi + Cabinet Grotesk (Fontshare, ITF Free Font License — free for commercial use). Three.js r160 (MIT) from jsDelivr.
- **Confirmed:** All-out; name invented by agent; modularity = swappable parts + explode view; commerce = plausible sample values labelled "sample"; light + dark with toggle; light on/off + warmth; opt-in switch click sound; direction A (assembly drawing) + B's pool-of-light moment; realistic lamp and joints; Satoshi + Cabinet Grotesk.
- **Assumed:** USD price; metric + imperial dimensions; English only.
- **Unknown:** real brand, price, photography (none — page uses the code-built model only).

## 4. Requirements
| ID | Requirement | Priority | Acceptance criterion |
|---|---|---|---|
| R-01 | Interactive 3D viewer: rotate by drag/touch | Must | Drag rotates; touch rotates; limits stop the camera going under the desk |
| R-02 | Keyboard rotation + reset | Must | Arrow keys on focused viewer and ◀ ▶ buttons rotate; Reset restores the default view |
| R-03 | Finish switch: matte black, brushed brass, white | Must | Radio group changes all painted parts in 3D and fallback; name + price line update |
| R-04 | Lamp built in code, realistic joints | Must | No external model; knuckle joints with axle bolts, friction knobs, springs, cable, shade with lip and diffuser |
| R-05 | Modularity visible | Must | "Show modules" separates five numbered parts with callouts; list in Modules section highlights the part |
| R-06 | Light on/off + warmth | Must | Switch lights diffuser and casts a pool of light; warmth slider 2700–5000 K changes colour |
| R-07 | Fallback: no WebGL | Must | With WebGL disabled the page shows an image turntable (drag/keys/buttons), finish swap works, message explains |
| R-08 | Fallback: low-end phones | Must | Save-Data / ≤2 GB / ≤2 cores start in Lite view with an opt-in "Load 3D"; slow fps degrades quality then offers Lite |
| R-09 | Responsive phone / tablet / desktop | Must | No overflow 320–1920; viewer and buy panel designed per size; sticky buy bar on phones |
| R-10 | Light + dark theme | Must | System default, toggle persisted, no flash; 3D floor matches |
| R-11 | Opt-in sound | Should | Off by default; toggle; click on switch/finish/modules; nothing plays before gesture |
| R-12 | Product page content | Must | Sample price/specs labelled as sample; Add to bag with confirmation |
| R-13 | Self-contained, relative paths | Must | Works from file://; all extra files in folder |

## 5. Experience
- **Sections:** Header → Product (viewer | buy panel) → Five modules (assembly drawing) → Light (dark band, pool of light) → Specs → FAQ → Footer.
- **Primary action:** Add to bag (one per view). Secondary: viewer controls.
- **Key interactions:** orbit, finish radio, light switch, warmth slider, modules toggle, 3D/Lite switch, theme, sound.

## 6. Creative direction
- **Concept:** "An engineer's assembly drawing pinned above a workbench — and at night, one pool of light."
- **Mood:** precise, tactile, warm · **Anti:** glossy-tech, cute.
- **Category cliché:** white seamless background, centred product, huge thin sans headline, grey body (Apple-style). **Divergence:** type (heavy industrial caps Cabinet Grotesk), layout (ruled drawing grid + numbered callouts with leader lines), colour (paper + ink + one vermilion signal; dark mode is a warm night room, not black/neon).
- **Base style:** Utilitarian (spec-sheet) · **Accent:** Premium Product (one hero product moment). Logged as A+B per user.
- **Signature elements:** (1) exploded assembly view with numbered vermilion callouts; (2) the switch-on moment that throws a warm pool of light onto the page.
- **Type:** Cabinet Grotesk 800 uppercase display, tight tracking; Satoshi 400/500/700 text + tracked small-caps labels with tabular numerals.
- **Colour roles:** paper `#F1EEE7`, ink `#1C1B19`, signal vermilion `#C93A17` (action/callouts), rule `#D8D2C4`; dark: night `#15130F`, chalk `#EEE8DD`, signal `#FF7A52`, lamp-glow `#F3C47A`.
- **Motion:** camera intro ease (600 ms), explode spring-ish ease (700 ms), finish crossfade (250 ms). Reduced motion → instant.
- **Sound:** synthesized (Web Audio): switch click, finish tick, module clack. Opt-in.

## 7. Technical strategy
- Three.js r160 via import map (jsDelivr): core + OrbitControls + RoomEnvironment. One renderer, `MeshPhysicalMaterial` (brass uses anisotropy + procedural brushed texture), PCF soft shadows, spot light in the head.
- Geometry: Lathe (base, shade, knobs), Tube (cable), Cylinder/Box with rounded profiles (knuckles), helical Tube (springs). ~40k tris, < 60 draw calls.
- Render on demand (render loop only while animating/damping/interacting); pause offscreen + hidden tab.
- Fallback sprites: render 24 angles × 3 finishes × (off/on) with the same scene via `?sprites` mode and Playwright → `img/strut-{finish}-{on|off}-{nn}.webp`. Front "off" frame per finish doubles as the poster (LCP) shown before 3D loads.
- State object → UI + 3D + fallback share one source of truth.

## 8. States and edge cases
Loading (poster + progress label) · 3D failed (falls to Lite with message) · no WebGL · Save-Data · low fps · offscreen · tab hidden · resize/orientation · sound blocked · localStorage blocked (try/catch) · no JS (noscript poster + content still readable) · Add to bag success toast · bag 0/1/many.

## 9. Accessibility and responsive
Skip link; landmarks; one h1; viewer is a labelled `role="group"` with text description + live region describing angle/finish; finish is a native radio group; switch is `role="switch"`; slider native range with value text in K; 44 px targets; focus rings 3:1 in both themes; reduced motion; sound has visual equivalents. Breakpoints: <600 phone (viewer full-bleed, sticky buy bar), 600–1023 tablet (viewer above, panel two-column), ≥1024 desktop (viewer 7 cols | panel 5 cols, sticky panel).

## 10. Phases
| Phase | Tasks | Completion |
|---|---|---|
| 1 | Tokens, layout, content, theme, fallback shell | Page reads well with the poster only |
| 2 | 3D lamp model, materials, lights, controls | Realistic lamp renders, rotates |
| 3 | Finishes, light switch, explode + callouts, sound | All R-03..R-06, R-11 |
| 4 | Sprite render → Lite viewer, device heuristics, fps guard | R-07, R-08 |
| 5 | Verify (verify_page.py, journeys, no-WebGL, perf), score, improve | Gates + score ≥ 9 |

## 11. Verification
| Req / gate | Method | Expected |
|---|---|---|
| R-01/02 | Playwright drag + keys; screenshot before/after | Camera azimuth changes; reset restores |
| R-03/06 | Click each finish, toggle light, slider | Screenshots differ as expected |
| R-05 | Toggle modules | Parts separate; callouts visible and inside viewer |
| R-07 | Chromium `--disable-gpu --disable-webgl` (or `?lite`/WebGL stub) | Lite viewer, no console errors |
| R-08 | Emulated Save-Data / deviceMemory stub | Starts in Lite with "Load 3D" |
| R-09, G2 | verify_page.py 320–1440 + 1920 manual | No overflow |
| G3 | contrast.py on token pairs, both themes | ≥ 4.5 text, ≥ 3 UI |
| G10/G11 | verify_page.py reduced-motion + audio | Pass |
| Perf | fps sample via rAF in headless + throttled CPU; payload sizes | ≥ 30 fps throttled; poster < 1 s |

## 12. Risks and trade-offs
| Risk | L/I | Mitigation |
|---|---|---|
| Fontshare not one of the listed CDNs | M/L | It is a font CDN (fonts allowed); robust fallback stack; logged |
| Headless SwiftShader renders slowly / differs | M/M | Sprites rendered once; check visually |
| Code-built lamp looks toy-like | M/H | Real proportions (architect lamp), bevels, PBR + env map, small hardware details, contact shadow |
| Sprite set size | M/M | 24 frames × 640 px webp ≈ 25 KB; lazy-load per finish/state only |

## 13. Plan audit
| # | Finding | Severity | Resolution |
|---|---|---|---|
| 1 | Sample price/specs could read as real claims | Major | Each sample value marked with a "sample" footnote marker + footer note; no ratings, reviews or press |
| 2 | Lite turntable with light "on" doubles sprite count | Minor | Lazy-load only the active set |
| 3 | Explode callouts are HTML over canvas — could overflow on 320 px | Major | Clamp callouts inside viewer bounds; shorten labels to numbers on phones with list legend below |
| 4 | Orbit drag on phones can trap page scroll | Major | `touch-action: pan-y` on viewer; horizontal drag rotates only, vertical scrolls page; vertical tilt via buttons not needed |
| 5 | Third font (mono) in tiles conflicts with "two fonts" request | Major | Drop mono; Satoshi tabular figures + tracked caps carry the spec-sheet feel |
| 6 | No real photography | Obs. | Code-built model is the imagery; stated in close-out |
| 7 | Auto-rotation would need a pause control | Minor | No auto-rotation; one short intro move, skipped under reduced motion |
| 8 | Fallback must not depend on the 3D module loading | Major | Lite viewer in plain script; 3D module imported dynamically only when chosen |

## 14. Definition of done
- [ ] All Must requirements implemented and verified
- [ ] G1–G12 reported with evidence
- [ ] Score ≥ 9, no line < 8 (All-out) or gaps listed with reasons
- [ ] DESIGN.md with licence table; QA.md filled

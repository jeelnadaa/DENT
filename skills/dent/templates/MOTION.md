# Motion Spec: <project / piece>

> DENT motion spec. For interface motion fill §1–3 and §7; for motion graphics fill everything. See references/motion/.

## 1. Purpose and concept
- What motion must do here (explain change / guide attention / express brand / tell a story):
- Motion concept in one sentence (e.g. "type that behaves like ink settling"):
- Motion personality: <precise | elastic | weighty | airy | mechanical | organic> · Anti: <…>

## 2. Motion tokens
| Token | Value | Used for |
|---|---|---|
| dur-instant | 80ms | press, color |
| dur-fast | 160ms | toggles, tooltips |
| dur-normal | 260ms | menus, cards |
| dur-slow | 420ms | modals, sections |
| dur-scene | 600–1200ms | hero, scene transitions |
| ease-out | cubic-bezier(0.16,1,0.3,1) | entrances |
| ease-in | cubic-bezier(0.7,0,0.84,0) | exits |
| ease-in-out | cubic-bezier(0.65,0,0.35,1) | moves |
| spring-ui | stiffness 400, damping 40 | drags, sheets |
| stagger | 40ms, max 8 items | lists |

## 3. Interaction map (interface motion)
| Trigger | Element | Animation | Duration / easing | Interruptible? | Reduced-motion version |
|---|---|---|---|---|---|

## 4. Technology
- Engine(s) and why (one per job; see motion/motion-tech-catalog.md):
- Licence:
- Fallback when unsupported (no WebGL, low power):

## 5. Storyboard (motion graphics)
| # | Time | Frame description (composition, type, color) | Motion | Sound cue | Notes |
|---|---|---|---|---|---|
| 1 | 0.0–1.2s | | | | |

## 6. Timing sheet
Total length · beats per section · holds for reading (≥ 0.5 s + 0.3 s per word for on-screen text) · loop point (if looping).

## 7. Accessibility and performance
- Reduced-motion alternative for each scene:
- Pause/stop control (anything > 5 s auto-moving):
- No flashes > 3/s; no essential info only in motion:
- Budget: 60 fps target, max simultaneous animations, asset sizes, GPU-heavy effects only where justified:

## 8. Verification results
| Check | Result | Evidence |
|---|---|---|

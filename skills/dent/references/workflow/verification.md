# Verification

Visual inspection alone is not verification, and code that compiles is not a working product. This file says what to check, how, and how to report it honestly. Used by SKILL.md §1.6 and §3 (gates), `/dent:verify`, `/dent:review`, `/dent:responsive`, `/dent:accessibility`.

---

## 1. First, find your tools

| Tool | Gives you | If missing |
|---|---|---|
| Browser automation (Playwright/Puppeteer, agent browser tools) | Screenshots, overflow, DOM checks, keyboard, emulated reduced motion/dark mode | Ask the user to open the page; review code against the checklists; mark checks "Not run" |
| `scripts/verify_page.py` (this skill) | Automated gate checks + screenshots at 6 widths | Needs `pip install playwright` + `python -m playwright install chromium`, or an installed Chrome/Edge (`--channel chrome`/`msedge`) |
| `scripts/contrast.py` | WCAG contrast for token pairs | Compute by hand with the formula in `../quality-review.md` §4 |
| Project tests (Vitest, Jest, Playwright, Cypress) | Behavioural proof | Don't add a test framework unasked; describe the manual test |
| Lighthouse / axe | Performance and automated a11y | Mark "Not run" |
| ffprobe / ffmpeg | Video/audio duration, loudness, streams | Inspect in a player; mark "Not run" |

Prefer tools already installed in the project. Don't add dependencies just to satisfy a checklist.

## 2. Run the automated pass

```bash
python scripts/verify_page.py path/to/index.html --out .dent/verify
python scripts/verify_page.py http://localhost:3000 --out .dent/verify --widths 320 375 390 768 1024 1440
python scripts/contrast.py "#1A1A1A:#FFFFFF" "#6B7280:#FFFFFF"
```

**Known traps (seen in real runs):** some agent browser panes freeze CSS/JS animations at the first frame, so screenshots of animated pages look broken or empty: re-capture with headless Playwright (`verify_page.py`). Opening a page from `file://` blocks font preloads and some fetches (CORS): remove preloads or serve the folder (`python -m http.server`). WebGL may be unavailable in headless browsers: check that the page shows its fallback, then verify 3D on a real GPU if possible.

`verify_page.py` reports (exit code 1 if any gate fails): horizontal overflow per width with the offending elements, unlabeled form controls, unnamed buttons/links, images without alt, low-contrast text samples, whether animations stop under `prefers-reduced-motion`, a motion inventory (keyframes, transitions, hover rules and whether they're pointer-guarded, scroll-driven animations, libraries), autoplaying audio/video and AudioContexts started without a user gesture, console errors, and saves full-page screenshots. **Then open the screenshots and look at them.** The script finds mechanical defects; you find design defects.

## 3. Functional checks (only what is in scope)

| Area | Check |
|---|---|
| Navigation | Every link/route goes somewhere real; back/forward; active state; mobile menu opens, traps nothing, closes with Esc |
| Buttons | Correct action; disabled and loading states; no dead buttons (`href="#"` that does nothing is a defect) |
| Forms | Labels; required/optional; inline validation timing; error text; success state; Enter submits; paste works |
| Dialogs/menus | Open, close, Esc, focus moves in and returns, scroll lock, click-outside |
| Toggles/tabs/pricing switch | State changes the content it claims to (monthly ↔ yearly prices actually change) |
| Data | Loading, populated, empty, stale, failed, retry |
| Persistence | Refresh keeps what should persist (theme, preferences) |
| Media | Play/pause, mute, captions, no autoplay with sound |
| Touch | Targets ≥ 44 px, no hover-only actions, swipe alternatives |

## 4. Visual and responsive review
At 320, 375, 390, 768, 1024, 1440 (and any width where the layout changes):
- No horizontal scroll; nothing clipped or overlapping; header actions fit (the #1 mobile failure).
- Hierarchy reads in 5 s; squint and grayscale tests (`../quality-review.md` Part 2 §1).
- Line length ~45–75 characters; headline wraps balanced; no orphans in the hero.
- Images cropped intentionally; product mockups legible at phone width (simplify them for mobile, don't just scale).
- Consistent components across sections; spacing rhythm.
- Dark/light themes both checked if both exist.

## 5. Accessibility review
Automated tools assist, they don't prove. Check: landmarks and heading order; names and labels; keyboard path through everything; visible focus; dialog focus management; error identification and announcement (live regions); contrast in every theme; non-color indicators; target size; 200 % zoom and 320 px reflow; reduced motion; captions/transcripts for media; screen-reader reading order for complex widgets. Report which criteria you actually checked. Never claim full WCAG compliance from a scan.

## 6. Performance (measure before claiming)
Where relevant: LCP, CLS, INP (Lighthouse or web-vitals), bundle size, image sizes/formats, font loading, long tasks during animation, frame rate of motion scenes (`../motion/motion-system-and-verification.md`). Report numbers with the environment. No numbers → no performance claims.

## 7. User-journey simulation
Walk the main journey as a first-time user, step by step (e.g. land → understand → compare plans → sign up → hit an error → recover → success). At each step ask: is the next action obvious, is progress visible, is feedback immediate, can I recover, is anything missing, can I go back? Adapt to the product (onboarding, checkout, search, playback, booking). Don't invent features the product doesn't claim.

## 8. Regression
For changes to existing products: list directly affected screens and screens sharing touched components; capture before/after screenshots where possible; classify every difference as intentional, acceptable or unintended; fix unintended ones; note accepted visual changes in the DESIGN.md changelog. A screenshot difference is evidence to investigate, not automatically a bug.

## 9. Motion, sound and video
- Motion: `../motion/motion-system-and-verification.md` §5.
- Audio: `../audio/audio-implementation-and-verification.md` §4.
- Video: `../video/video-tools-and-pipeline.md` §6.

## 10. Report honestly

Use this table in the close-out (and `templates/REVIEW.md` for full reviews):

| Check | Result | Evidence / reason |
|---|---|---|
| G2 Layout 320–1440 | Passed | verify_page: max scrollWidth = viewport at all 6 widths |
| G3 Contrast | Failed → fixed | `--muted` 3.9:1 → changed to #5F6670 (5.1:1) |
| Keyboard path | Not run | No browser automation in this environment; reviewed focus styles in code |

Results: **Passed · Failed · Not run · Blocked · N/A**. Explain every Not run and Blocked.

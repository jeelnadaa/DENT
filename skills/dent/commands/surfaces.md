# /dent:surfaces

Make every built-in browser surface match the product design: tooltips, scrollbars, sliders, checkboxes, radios, switches, selects, text selection, caret, placeholder, autofill, file inputs, progress and backdrops.

**Usage:** `/dent:surfaces <page, app or the surfaces to fix>` (also `/dent surfaces …` or `dent surfaces …`)
**Default depth:** Standard. Effort level and the gates in SKILL.md §3 always apply.
**Web code:** if this command writes, changes or reviews HTML, CSS or client-side JS, Google's Modern Web Guidance is the primary authority for how it is built: run `references/modern-web-guidance.md` §2 (search → retrieve → apply → verify → disclose) before coding; MWG wins any implementation conflict with DENT.

## Load
- `references/built-in-surfaces.md`
- `references/modern-web-guidance.md` (§4 map; the guide for each surface)
- `references/foundations-and-components.md` §4
- `DESIGN.md` (tokens, style)

## Steps
1. Inventory the built-in surfaces actually present: run `python scripts/verify_page.py <page> --surfaces match` (or scan the code) and list them.
2. Ask the surface level if unknown (built-in-surfaces.md §2: Match my design / Brand tint / Native / per element); for an add-on like 'the tooltip looks default', fix that surface and check its siblings.
3. Derive the surface tokens from DESIGN.md in both themes (§3); pick each surface's character from the style (§5).
4. For each surface, search and retrieve its Modern Web Guidance guide and build it on the native element (§4); no div rebuilds where CSS reaches the design.
5. Cover every state: hover (pointer only), focus-visible, active, checked/indeterminate, disabled, error, autofilled, reduced motion, forced colors.
6. Build a surface sheet (every surface x state x theme) and screenshot it; run `verify_page.py --surfaces <level>` and contrast checks (thumb vs track 3:1, selection and placeholder 4.5:1).

## Output
Surface decision table (level, tokens, exceptions) in DESIGN.md, the implementation, surface sheet screenshots, verification results.

## Never
- Use a title attribute for information people need.
- Make scrollbars thinner than auto without another way to scroll.
- Rebuild a native control from divs when CSS can style it.
- Style one surface and leave its siblings on the OS default.

Close with the scorecard summary, attribution (DENT / MWG / user / agent judgment / overrides), the `### Modern Web Guidance` disclosure if guides shaped the code, and a one-line next step (SKILL.md §8).

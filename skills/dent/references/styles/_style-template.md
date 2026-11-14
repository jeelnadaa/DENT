# How every style file is written

Every style file uses the same sections, in the same order, so a model can apply any style the same way.

1. **Also called** — other names users might type.
2. **In one sentence** — the whole style, simply.
3. **Picture it** — a concrete image to hold in mind while designing.
4. **Feels like** — mood words.
5. **Use for / Avoid for** — product types where it fits or fails.
6. **Overrides** — a table that REPLACES the matching defaults in `../foundations-and-components.md` and `../modern-layer.md` (color, type, spacing, radius, borders, depth, motion, hover, imagery, components). Anything not listed keeps that default.
7. **Signature moves** — the few things that make the style instantly recognizable. If these are missing, the style is missing.
8. **Do / Don't** — the most common mistakes.
9. **Accessibility watch-outs** — where this style tends to break a [Rule], and the fix.
10. **Starter tokens** — CSS variables to begin from. Change values freely; keep the roles.

To add a new style: copy this structure into `<style-name>.md` and add a line to `_styles-index.md`.

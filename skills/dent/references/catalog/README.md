# DENT Catalogues: how to read, use and update them

The catalogues help DENT pick **existing, proven building blocks** (components, animation engines, audio libraries, video tools, assets) instead of reinventing them, and pick them for the *project*, not by popularity.

| Catalogue | File |
|---|---|
| Selection method (how to choose) | `component-selection.md` |
| Accessible primitives and complete component systems | `components-primitives-and-systems.md` |
| Copy-and-customize collections, specialized components, templates | `components-collections-and-specialized.md` |
| Fonts, icons, illustration, photos, 3D, textures, footage, sound, music | `asset-sources.md` |
| Animation, graphics, 3D and creative-coding tech | `../motion/motion-tech-catalog.md` |
| Audio, TTS, music and SFX tech | `../audio/audio-tech-catalog.md` |
| Video tools (generative, code-based, editors) | `../video/video-tools-and-pipeline.md` |

## Entry fields
Every entry states: **name + official URL · role · frameworks · styling/customisation · accessibility · licence (and paid tiers) · use when · avoid when · status**.

**Role vocabulary** (never mix them up):
- **Primitive:** unstyled, accessible behaviour (focus, keyboard, ARIA). You bring all styling.
- **System:** complete styled library with its own design language and theming.
- **Collection:** copy-and-customize source you paste into your project (you own the code).
- **Specialized:** one job done very well (toasts, drawers, tables, editors, charts, DnD…).
- **Runtime:** animation/graphics/audio engine.
- **Template/Product:** paid kits, templates, SaaS or commercial plugins.

## Status legend (honesty about freshness)
- **✓ 2026-11-14** — licence/status checked against official pages or multiple consistent sources on that date.
- **K** — from the maintainers' knowledge (as of mid-2026), not re-checked this session. **Verify the licence and current version from the official repo before recommending it for production**, and say so to the user.
- **⚠** — known caveat (maintenance, licence change, paid tier) described in the entry.

Licences change. A package being free to install doesn't make every part of its ecosystem free (pro components, premium plugins, templates, hosted services, assets). Always distinguish them.

## Updating a catalogue
1. Edit only the row (or add a row) in the right category table.
2. Fill every field; set status to `✓ <date>` only after checking the official licence file/page.
3. Run `python scripts/validate.py` (checks every row has a link, licence and status).
4. Add a CHANGELOG line ("Catalogue: added X; Y licence changed to Z").

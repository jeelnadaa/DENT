# Asset Sources and Licences

Where to get fonts, icons, illustrations, photos, 3D models, textures, video footage, sound effects, music and voices, and what their licences allow. **Software licences and asset licences are different things:** an MIT library can ship with assets under CC BY-NC; a "free download" can forbid commercial use or require attribution. Record every asset in DESIGN.md's licence table:

| Asset | Source URL | Licence | Attribution text (if required) | Commercial OK? |
|---|---|---|---|---|

Status legend: ✓ checked 2026-11-14 · K from knowledge, verify on the source page before use · ⚠ caveat.

---

## 1. Fonts
| Source | Licence | Notes | Status |
|---|---|---|---|
| [Google Fonts](https://fonts.google.com) | Mostly SIL OFL 1.1 (some Apache-2.0/UFL) | Free incl. commercial; self-host for privacy/performance | K |
| [Fontshare (ITF)](https://www.fontshare.com) | ITF Free Font License | Free for personal and commercial use; read per-family terms | K |
| [Velvetyne](https://velvetyne.fr) | OFL (mostly) | Experimental, characterful display faces | K |
| [The League of Moveable Type](https://www.theleagueofmoveabletype.com) | OFL | Classic open display faces | K |
| [Uncut.wtf](https://uncut.wtf) | Varies (catalogue of free fonts) | Check each font's licence link | K |
| [Collletttivo](https://www.collletttivo.it) | OFL (mostly) | Free type collective | K |
| Commercial foundries (Klim, Grilli Type, Pangram Pangram, Commercial Type, Dinamo, OH no Type…) | Paid desktop/web licences (some free trials/personal-use) | Recommend only if the user owns or will buy the licence; trial fonts are not for production | K |

Rules: self-host with `font-display: swap`, subset, preload the 1–2 critical files; never embed a font whose licence forbids web embedding.

## 2. Icons
| Set | Licence | Style | Status |
|---|---|---|---|
| [Lucide](https://lucide.dev) | ISC | 24 px stroke, consistent | K |
| [Phosphor](https://phosphoricons.com) | MIT | 6 weights incl. duotone | K |
| [Tabler Icons](https://tabler.io/icons) | MIT | Stroke, huge set | K |
| [Heroicons](https://heroicons.com) | MIT | Outline/solid/mini | K |
| [Material Symbols](https://fonts.google.com/icons) | Apache-2.0 | Variable (fill, weight, grade, optical size) | K |
| [Iconoir](https://iconoir.com) | MIT | Stroke | K |
| [Remix Icon](https://remixicon.com) | Apache-2.0 (verify current terms) | Line/fill | K |
| [Simple Icons](https://simpleicons.org) | CC0 for SVGs; **brand marks are trademarks** of their owners | Brand logos | K |
| [Iconify](https://iconify.design) | Aggregator: licence per icon set | Use their licence field | K |

## 3. Illustration
| Source | Licence | Notes | Status |
|---|---|---|---|
| [unDraw](https://undraw.co) | Free (own licence; no attribution) | Very recognisable → anti-slop risk; recolor + use sparingly | K |
| [Open Peeps](https://www.openpeeps.com) / [Humaaans](https://www.humaaans.com) | CC0 | Hand-drawn people | K |
| [Blush](https://blush.design) | Free tier with attribution / paid | Many artists | K |
| [Storyset](https://storyset.com) | Free with attribution (Freepik licence) | Animated SVG illustrations | K |
| Public-domain archives ([Biodiversity Heritage Library](https://www.biodiversitylibrary.org), [Rawpixel PD](https://www.rawpixel.com/category/53/public-domain), [The Met Open Access](https://www.metmuseum.org/art/collection), [Smithsonian Open Access](https://www.si.edu/openaccess)) | Public domain / CC0 for marked items | Botanical plates, engravings, maps, posters: great for distinctive directions | K |
Best option for distinctiveness: commission or generate a **consistent custom style** (SVG drawn in code, or generative tools if the user has access and rights).

## 4. Photos
| Source | Licence | Notes | Status |
|---|---|---|---|
| [Unsplash](https://unsplash.com/license) | Unsplash License (free commercial, no attribution required; no selling unaltered copies, no compiling a competing service) | Overused: crop and art-direct | K |
| [Pexels](https://www.pexels.com/license/) | Pexels License (similar) | Photos + videos | K |
| [Pixabay](https://pixabay.com/service/license-summary/) | Pixabay Content License | Photos, illustrations, video, music, SFX; some restrictions (no standalone resale, trademarks/people) | K |
| [Openverse](https://openverse.org) | CC licences + public domain (search engine) | Filter by commercial use / modification | K |
| [Wikimedia Commons](https://commons.wikimedia.org) | Per file (CC BY, CC BY-SA, PD…) | Attribution often required | K |
Rules: people in photos need model releases for commercial use (stock sites cover this; random web images don't). Never use real people to imply endorsement.

## 5. 3D models, HDRIs and textures
| Source | Licence | Notes | Status |
|---|---|---|---|
| [Poly Haven](https://polyhaven.com) | CC0 | HDRIs, PBR textures, models: ideal for product renders | K |
| [ambientCG](https://ambientcg.com) | CC0 | PBR materials | K |
| [Kenney](https://kenney.nl) | CC0 | Game-style 3D/2D assets, UI packs, sounds | K |
| [Quaternius](https://quaternius.com) | CC0 | Low-poly models | K |
| [Sketchfab](https://sketchfab.com) | Per model (CC BY, CC0, paid store) | Check each model; attribution text often required | K |
| [Poly Pizza](https://poly.pizza) | CC0 / CC BY per model | Low-poly | K |
| [Smithsonian 3D](https://3d.si.edu) | CC0 for many items | Museum scans | K |
| [Mixamo](https://www.mixamo.com) | Royalty-free with an Adobe account (Adobe terms) | Character rigging/animations | K |
Formats: glTF/GLB for web; compress (Draco/Meshopt), KTX2 textures.

## 6. Video footage
| Source | Licence | Notes | Status |
|---|---|---|---|
| [Pexels Videos](https://www.pexels.com/videos/) | Pexels License | Free commercial | K |
| [Pixabay Videos](https://pixabay.com/videos/) | Pixabay Content License | Free commercial with restrictions | K |
| [Mixkit](https://mixkit.co) | Mixkit licences (free; differ per asset type: stock video, music, SFX, templates) | Read the licence type on each asset | K |
| [Coverr](https://coverr.co) | Coverr License (free) | Short loops for heroes | K |
| [Videvo](https://www.videvo.net) | Mixed: free clips with attribution/editorial-only + premium | Filter carefully | K |
| Generative video (Veo, Sora, Runway, Kling, Luma, Pika…) | Per provider terms and plan | Only if the user has access; record the plan's commercial terms; label AI-generated where relevant | K |

## 7. Sound effects
| Source | Licence | Notes | Status |
|---|---|---|---|
| [Freesound](https://freesound.org) | **Per sound:** CC0, CC BY 4.0, or CC BY-NC 4.0 (older: CC BY 3.0 / Sampling+) | Filter to CC0/CC BY for commercial; credit CC BY authors; **NC = no commercial use** | K |
| [Pixabay Sound Effects](https://pixabay.com/sound-effects/) | Pixabay Content License | Free commercial, no attribution required | K |
| [Mixkit Sound Effects](https://mixkit.co/free-sound-effects/) | Mixkit Sound Effects Free License | Free commercial; can't redistribute standalone | K |
| [Kenney Audio](https://kenney.nl/assets?q=audio) | CC0 | UI clicks, game sounds | K |
| [OpenGameArt](https://opengameart.org) | Per asset: CC0, CC BY, CC BY-SA, GPL, OGA-BY | Check each; BY-SA/GPL impose share-alike | K |
| [Sonniss GDC bundles](https://sonniss.com/gameaudiogdc) | Royalty-free licence (per bundle terms) | High-quality pro SFX libraries | K |
| [BBC Sound Effects](https://sound-effects.bbcrewind.co.uk) | RemArc licence: **personal, educational, research only**; commercial via licensing partner | Do not use commercially without a licence | K |
| [ZapSplat](https://www.zapsplat.com) | Free with attribution / paid without | Check plan | K |
Or **synthesize** UI sounds (Web Audio / Tone.js): no asset licence needed, perfectly on-brand.

## 8. Music
| Source | Licence | Notes | Status |
|---|---|---|---|
| [Pixabay Music](https://pixabay.com/music/) | Pixabay Content License | Free commercial; some tracks have Content ID registrations, so check before YouTube monetisation | K |
| [Free Music Archive](https://freemusicarchive.org) | Per track (CC BY, BY-NC, BY-SA…) | Filter commercial | K |
| [Incompetech (Kevin MacLeod)](https://incompetech.com) | CC BY 4.0 (attribution) or paid licence | Very widely used (recognisable) | K |
| [YouTube Audio Library](https://studio.youtube.com) | For YouTube videos; some tracks require attribution | Read terms for use outside YouTube | K |
| [Uppbeat](https://uppbeat.io) / [Epidemic Sound](https://www.epidemicsound.com) / [Artlist](https://artlist.io) | Subscription licences | Only if the user subscribes | K |
| AI music (Suno, Udio, Stable Audio, etc.) | Provider terms by plan (commercial use usually needs a paid plan) | Only with user's account; record plan terms; avoid imitating named artists | K |
| Musopen / IMSLP recordings | Many public-domain/CC recordings (composition PD ≠ recording PD) | Check the recording's licence | K |

## 9. Voices (TTS and voice actors)
See `../audio/voice-and-narration.md` §5 and `../audio/audio-tech-catalog.md` §4. Key rules: synthetic voices have provider terms (commercial use, attribution, disclosure); **cloning a real person's voice requires their documented consent**; open engines differ (Kokoro: Apache-2.0 model ✓ 2026-11-14; Piper: active repo GPL-3.0, original MIT repo archived Oct 2025 ✓ 2026-11-14; Coqui XTTS model: non-commercial CPML — verify).

## 10. Logos and trademarks
Company logos (e.g. for "works with" lists) are trademarks: use them only for factual compatibility statements, unmodified, per the owner's brand guidelines, and never to imply endorsement. Never invent "Trusted by" logo walls.

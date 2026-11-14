# Creative Directions Library

A library of **named, fully specified creative directions**. A direction is more than a style: it is a concept (a world the product lives in) plus concrete decisions for type, color, layout, imagery, motion and sound. Use it when you must pick a look, when `/dent:directions` asks for options, or when your first idea is the category cliché.

How to use:
1. Name the **category cliché** first (§1). Then pick directions that are *not* it.
2. Shortlist 2–4 directions from §3 whose "Fits" matches the product. For a weak model: take the first fitting one and follow it literally. For a strong model: remix (§6) or invent (§7), and log it as `Override`/Agent judgment.
3. A direction sits **on top of** one base style (`../styles/`), never replaces the gates. Every palette here is a starting point: verify contrast with `scripts/contrast.py` before shipping.
4. Copy the direction block into the Decision Log / DESIGN.md §1.

---

## 1. Category clichés (what everyone does; diverge on ≥ 2 axes)

| Category | The cliché | Divergence ideas |
|---|---|---|
| AI / dev tools | Near-black, violet-blue gradient, glowing orb, Inter, fake dashboard tilted in 3D, ✨ | Paper-white technical manual; instrument panel; terminal-as-editorial; real product output as hero |
| Fintech | Navy + mint/green, rounded cards, phone mockup, "trusted by" grey logos | Swiss ledger; banknote engraving; bold monochrome numbers; editorial money journalism |
| Health / wellness | Pastel teal, blobs, smiling stock people, rounded sans | Botanical print; clinical precision with warmth; handwritten care notes; calm editorial |
| Coffee / food | Espresso brown, orange accent, serif, steam icons, dark moody photos | Bright cafe tile palette; risograph menu; Japanese kissaten minimalism; lab-notebook science |
| SaaS B2B | White, blue primary, 3 feature cards, gradient hero blob, pricing 3 tiers | Newspaper front page; blueprint; product-as-hero with cropped real UI; bold typographic manifesto |
| Crypto / web3 | Neon on black, 3D coins, glitch | Banknote/archival security print; quiet Swiss; museum catalogue |
| E-commerce fashion | White, thin serif caps, full-bleed model photo | Zine collage; catalogue index with numbers; brutalist price tags |
| Education / kids | Primary colors, cartoon mascot, Comic-style font | Field guide; science museum; stamp/badge collecting; chalk-and-paper |
| Productivity | Minimal white, soft shadows, purple accent | Stationery shop; mechanical keyboard; library card catalogue |
| Gaming | Dark, neon, aggressive angles | Arcade cabinet art; board-game box; illustrated map |
| Music / audio | Black, waveform, gradient | Record sleeve typography; mixing desk; concert poster |
| Real estate / travel | Big photo, search bar, blue | Architectural drawing; travel journal; postcard and stamp |

## 2. Direction block format

```
### <Name>
Concept · Fits · Avoid for
Type: display / text / mono (+ hero move)
Color: roles with hex (bg / surface / text / muted / accent / signal)
Layout: grid, density, signature composition
Imagery: what visuals are made of
Motion: personality + 2–3 specific moves
Sound: palette idea (optional, opt-in)
Signature: the one unforgettable element
Never: the ways this direction fails
```

---

## 3. Interface and web directions

### 3.1 Ledger
**Concept:** a beautifully kept accounting ledger. **Fits:** fintech, invoicing, analytics, B2B finance. **Avoid for:** playful consumer apps.
**Type:** display: a high-contrast didone or modern serif (e.g. Fraunces at opsz 144, Bodoni Moda); text: a neo-grotesk (Inter Tight, Söhne-like, Geist); mono tabular figures (JetBrains Mono, IBM Plex Mono). Hero: one huge number set in the serif with a thin rule under it.
**Color:** paper #F4F1EA · surface #FBFAF6 · ink #141414 · muted #5C5A55 · rule #CFC9BC · accent ledger-red #B3261E (text-safe on paper) · positive #1F6F43.
**Layout:** 12-col grid with visible hairline rules; numbers right-aligned; dense tables as hero content; generous left margin with column numbers.
**Imagery:** real tables and charts only; no photos.
**Motion:** numbers count with tabular digits (NumberFlow-like), rules draw left→right 400 ms, rows reveal in a 30 ms stagger. **Sound:** soft paper tick on confirm (opt-in).
**Signature:** red double underline under totals. **Never:** gradients, glass, rounded pill everything.

### 3.2 Field Manual
**Concept:** a rugged technical field guide. **Fits:** dev tools, infrastructure, outdoor/utility apps, security. 
**Type:** condensed grotesk for headings (Barlow Condensed, Oswald), text: IBM Plex Sans; mono labels (Plex Mono). Hero: stacked condensed caps with section numbers "01 — DEPLOY".
**Color:** khaki paper #E9E4D4 · surface #F3EFE3 · ink #1D1F1A · olive #4B5A2A · signal orange #D9480F (fill with ink text) · muted #5B5D52.
**Layout:** numbered sections, two-column "procedure" layouts (step | illustration), callout boxes with hazard stripes for warnings.
**Imagery:** line diagrams, exploded views, topographic contour patterns (SVG).
**Motion:** mechanical, 120–200 ms, no bounce; diagrams draw on scroll (SVG stroke). **Sound:** switch click, radio-chirp notification.
**Signature:** contour-line background behind the hero, generated as SVG. **Never:** neon, glassmorphism.

### 3.3 Kissaten
**Concept:** a quiet Japanese coffee house: wood, ceramic, one perfect cup. **Fits:** coffee, tea, food, wellness, journaling. Breaks the espresso-and-orange cliché.
**Type:** display: a soft serif with ink traps (Newsreader, Shippori Mincho for JP flavor); text: a humanist sans (Instrument Sans); vertical Japanese-style column labels used decoratively (with real text alternative).
**Color:** rice paper #F6F1E7 · ceramic white #FFFDF8 · charcoal #23201C · tea green #5E6B3E · persimmon #C2552B (accent, AA as large text; use darker #9E3F1C for small text) · muted #6B645A.
**Layout:** asymmetric, lots of negative space, content in narrow columns offset right, one big image per screen.
**Imagery:** close-up textures (ceramic glaze, wood grain), hand-drawn ink circles (ensō) as section markers.
**Motion:** slow and settling, 600–900 ms ease-out; steam drawn as a looping SVG path at low opacity (paused under reduced motion). **Sound:** soft wooden tap, ceramic clink on success.
**Signature:** an ensō circle that draws itself around the primary CTA once. **Never:** dark espresso backgrounds, orange gradients.

### 3.4 Blueprint
**Concept:** architectural blueprint / engineering drawing. **Fits:** construction, hardware, devtools, API products, planning tools.
**Type:** technical sans (Space Grotesk, Archivo); mono annotations; hero headline with dimension lines and arrows around it.
**Color:** blueprint #0F3B6E · line #CFE3FF · text #F5F9FF · muted #A9C3E6 · highlight #FFD166 (annotations).
**Layout:** visible grid (1px lines at 8% opacity), callouts with leader lines, title block in the bottom-right corner of sections.
**Imagery:** wireframe drawings, isometric diagrams.
**Motion:** lines plot like a pen plotter (stroke-dashoffset), dimensions appear after shapes. **Sound:** plotter scratch for one hero moment only.
**Signature:** the hero headline is "measured" with animated dimension lines. **Never:** photos, rounded blobs.

### 3.5 Newsprint
**Concept:** the front page of a broadsheet newspaper. **Fits:** media, launches, opinionated SaaS, changelogs, reports.
**Type:** headline: condensed serif or blackletter masthead (UnifrakturCook for the masthead only, Playfair Display / Old Standard TT for headlines); text: a news serif (Source Serif 4); columns of 45–60 characters.
**Color:** newsprint #F2EFE6 · ink #111 · muted #4A4A4A · one spot color red #C1121F for kickers.
**Layout:** multi-column grid, rules between columns, kicker + headline + deck structure, pull quotes, dateline.
**Imagery:** halftone (CSS/SVG dot patterns) of real product screenshots.
**Motion:** almost none; a "press" stamp effect on the main headline once. **Sound:** none or a single paper rustle.
**Signature:** masthead with edition number and date that is real (version number + release date). **Never:** fake news quotes or fake press logos.

### 3.6 Instrument Panel
**Concept:** precision hardware front panel. **Fits:** audio software, IoT, analytics, dev tools, pro creative tools. Base style: Utilitarian.
**Type:** grotesk + mono micro-labels in caps; big tabular numerals.
**Color:** warm grey #E3E1DC · panel #ECEAE5 · ink #151515 · label #5B5B57 · signal orange #FF5A1F (fills) · LED green #19A974 (with text).
**Layout:** modules in a strict grid with screws/rivets as tiny dots in corners; knobs, toggles and meters as real controls.
**Imagery:** product photos on seamless background, technical renders.
**Motion:** knobs rotate with springs, meters ease with slight overshoot; toggles snap 100 ms. **Sound:** tactile clicks for toggles (opt-in), low tick for knobs.
**Signature:** a working VU meter or knob in the hero that controls something real on the page. **Never:** decorative controls that do nothing.

### 3.7 Specimen
**Concept:** a type foundry specimen book. **Fits:** design tools, agencies, editorial, portfolios, font/brand products.
**Type:** one variable family pushed across axes (Fraunces, Recursive, Roboto Flex); hero shows the family at 3 widths/weights with glyph details.
**Color:** white #FFFFFF · ink #0A0A0A · muted #6A6A6A · one fluorescent accent #FF3EA5 used like a highlighter (on black text background only).
**Layout:** big glyphs, numbered sample lines, size ladders, baseline grids visible.
**Imagery:** typography only.
**Motion:** variable-font axis animations on hover/scroll (weight 300→900), letter-by-letter reveals. **Sound:** none.
**Signature:** a giant ampersand or the product's initial as the hero image. **Never:** stock photos.

### 3.8 Museum Placard
**Concept:** exhibition hall: works on walls, small precise labels. **Fits:** portfolios, galleries, premium products, case studies, archives.
**Type:** text serif (EB Garamond / Cormorant for titles) + small sans labels (Satoshi or General Sans 12–13 px caps tracked).
**Color:** gallery white #F7F7F5 · wall grey #E8E8E4 · ink #1A1A1A · muted #6B6B66 · single accent from the artwork itself.
**Layout:** one object per viewport, placard text bottom-left, wide margins, catalogue numbers.
**Motion:** slow cross-fades, spotlight follows cursor subtly on artworks (pointer only). **Sound:** room tone ambience (opt-in, very low).
**Signature:** every item has a real "accession number" (e.g. version/date). **Never:** carousels of tiny thumbnails.

### 3.9 Riso Club
**Concept:** a risograph-printed zine from an indie studio. **Fits:** community, events, creative tools, education, food. Base style: Risograph.
**Type:** chunky grotesk (Bricolage Grotesque, Familjen Grotesk) + typewriter mono.
**Color:** paper #F5F0E6 · fluorescent pink #FF48B0 · riso blue #0078BF · yellow #FFE800 · ink #1B1B1B (text always ink).
**Layout:** overlapping colored shapes with multiply blend, slight misregistration offset (2–3 px), stickers and tape.
**Motion:** stamps and sticker drops with springy overshoot; misregistration jitter on hover. **Sound:** rubber stamp thunk on success.
**Signature:** two-color halftone portraits/illustrations. **Never:** gradients or glass.

### 3.10 Night Train
**Concept:** a sleeper train at night: amber lamps, dark wood, passing lights. **Fits:** travel, sleep, audio/podcast, cozy games, reading apps.
**Type:** warm serif display (Fraunces soft, Young Serif), text: Satoshi or Atkinson Hyperlegible.
**Color:** night #11131A · cabin wood #2A1E17 · lamp amber #F2B35B (accent) · text #F3EEE6 · muted #B8AFA2.
**Layout:** framed "windows" (rounded rectangles) that reveal content as if passing by.
**Motion:** horizontal parallax of light streaks behind window frames (reduced motion: static); gentle rocking 0.5° on the hero only. **Sound:** rail rhythm ambience (opt-in), soft chime for notifications.
**Signature:** the content scrolls past "windows". **Never:** neon cyberpunk.

### 3.11 Greenhouse
**Concept:** a Victorian glasshouse full of specimens. **Fits:** plants, sustainability, health, science, gardening.
**Type:** botanical serif (Cormorant Garamond) + clean sans (Manrope); Latin specimen labels in italic.
**Color:** glass green #E7EFE6 · leaf #2F5D3A · ink #18231A · muted #55665A · terracotta #B5563A.
**Layout:** iron-frame grid (thin dark-green lines), specimen cards with pinned labels.
**Imagery:** botanical illustrations (licensed/public-domain plates), pressed-leaf textures.
**Motion:** leaves sway on idle (subtle, pausable), condensation fades on reveal. **Sound:** soft rain ambience (opt-in).
**Signature:** a growing plant line drawing tied to scroll progress. **Never:** generic blob shapes.

### 3.12 Mission Control
**Concept:** 1969 mission control: CRT readouts, consoles, countdowns. **Fits:** launches, monitoring, data, space/tech brands. Base: Retro-Futurism or Dark Tech.
**Type:** condensed sans (Barlow Semi Condensed), mono readouts (VT323 only for big numerals, Plex Mono for text).
**Color:** console beige #D8CFB8 · panel #2B2B26 · CRT green #8BFF8B on #0B120B · alert amber #FFB000 · text #EDE6D3.
**Layout:** console modules, rows of status lights (with labels), a countdown as hero.
**Motion:** scanline sweep, numbers flip; telemetry ticks. **Sound:** countdown beeps (opt-in), launch rumble in videos.
**Signature:** a real countdown to a real date (release), never a fake urgency timer. **Never:** fake scarcity.

### 3.13 Atelier
**Concept:** a fashion atelier: chalk marks, pattern paper, pins. **Fits:** fashion, craft, luxury, made-to-order.
**Type:** thin high-contrast serif caps (Bodoni Moda) + neutral sans (Neue Montreal-like: Switzer; Inter Tight).
**Color:** pattern paper #EFE7DA · chalk #FFFFFF · ink #171512 · tailor blue #2E4A7D · pin red #B4232C.
**Layout:** dashed cutting lines, measurement tape rulers on edges, pinned swatches.
**Motion:** pieces slide into place along dashed guides. **Sound:** scissor snip on add-to-bag (opt-in).
**Signature:** a measuring tape that doubles as the scroll indicator. **Never:** discount banners shouting.

### 3.14 Lab Notebook
**Concept:** a scientist's notebook: grid paper, observations, data. **Fits:** research, health data, coffee science, biotech, education.
**Type:** text: Literata or IBM Plex Serif; handwritten annotations (Caveat, sparingly); mono data.
**Color:** grid paper #FAFAF5 with #DCE6F2 grid · ink #1C2430 · pencil #5B6573 · highlighter yellow #FFF07A behind text · red pen #C0362C.
**Layout:** grid background, taped photos, margin notes, numbered observations.
**Motion:** handwriting strokes draw in, highlighter swipes across key phrase (once). **Sound:** pencil scratch micro-sound (opt-in).
**Signature:** a hand-annotated chart of real data. **Never:** fake experiment results.

### 3.15 Monolith
**Concept:** one massive slab of type and silence. **Fits:** premium launches, manifestos, portfolios, single-product sites.
**Type:** one ultra-bold grotesk (Archivo Black, Anton) or a sharp display serif at 15–25vw; text: Inter.
**Color:** pure contrast: #0B0B0B / #F4F4F2 with one accent used once.
**Layout:** full-viewport typographic slabs, cropped letters bleeding off edges, everything else tiny.
**Motion:** slow scale/translate of the slab on scroll (scroll-driven), letters mask-reveal. **Sound:** sub-bass hit in video only.
**Signature:** the product name cropped so big it becomes architecture. **Never:** more than one accent.

### 3.16 Post Office
**Concept:** stamps, postmarks, envelopes, airmail stripes. **Fits:** messaging, email tools, travel, gifting, newsletters.
**Type:** slab serif (Zilla Slab, Roboto Slab) + mono postmarks.
**Color:** envelope #F4EBDD · airmail red #C8102E · airmail blue #1F3A93 · ink #1E1A16 · stamp green #2E6B4F.
**Layout:** cards as envelopes, perforated stamp edges (CSS mask), postmark circles with dates.
**Motion:** stamp press with squash, envelope flap open. **Sound:** stamp thunk on send (opt-in).
**Signature:** every sent state gets a postmark with the real time. **Never:** skeuomorphic overload in data views.

### 3.17 Brutal Index
**Concept:** a raw directory listing turned beautiful. **Fits:** developer portfolios, documentation, archives, link hubs. Base: Brutalism or Swiss.
**Type:** system mono or one grotesk at a single size; hierarchy by weight and position only.
**Color:** #FFFFFF / #000000 / link blue #0000EE (with underline) / visited #551A8B.
**Layout:** tables, file trees, timestamps, no decoration.
**Motion:** none except instant hover inversions. **Sound:** none.
**Signature:** honesty: real file sizes, dates, counts. **Never:** fake raw-ness with decorative noise.

### 3.18 Aurora Glass (done right)
**Concept:** northern lights through frosted glass. **Fits:** consumer AI, weather, music, wellness when the brand wants beauty. Base: Glassmorphism or Aurora.
**Type:** elegant sans (Plus Jakarta Sans, Satoshi-like) with tight display tracking.
**Color:** deep night #0B1020 · aurora teal #3FE0C5 · violet #8B6CFF · rose #FF7AB6 (backgrounds only) · glass rgba(255,255,255,.08) · text #F5F7FF.
**Layout:** few glass layers (max 3 depths), each with a tint behind text for contrast.
**Motion:** aurora gradient drifts slowly (60 s loop, paused under reduced motion); glass panels parallax 2–6 px with pointer. **Sound:** airy pad swell for onboarding (opt-in).
**Signature:** the aurora reacts to real data (e.g. time of day). **Never:** glass on glass on glass; text on raw gradient.

### 3.19 Toybox
**Concept:** chunky wooden toys and building blocks. **Fits:** kids, education, casual games, playful consumer apps. Base: Playful / Claymorphism.
**Type:** rounded display (Baloo 2, Fredoka) + readable text (Nunito).
**Color:** cream #FFF8EC · red #E63946 · blue #1D4ED8 · yellow #FFC300 · green #2A9D8F · ink #1E1E1E.
**Layout:** blocks that stack; buttons as physical blocks with 4–6 px bottom "depth".
**Motion:** springy (damping 0.6), blocks drop and settle; success = blocks tumble into a star. **Sound:** wooden block knocks, xylophone confirmations (opt-in, gentle).
**Signature:** a block tower that grows with progress. **Never:** baby-talk copy, dark patterns for kids.

### 3.20 Tidepool
**Concept:** an underwater rock pool: light caustics, slow life. **Fits:** meditation, sleep, ocean/climate, calm reading.
**Type:** soft humanist serif (Lora) + rounded sans (Quicksand for labels only).
**Color:** deep #0E2A33 · water #12424F · caustic light #9FE7E1 · sand #E9DCC1 · coral #F2836B · text #EAF6F4.
**Motion:** WebGL or CSS caustic light pattern at low intensity (static fallback), breathing circle 4-7-8 timing. **Sound:** water ambience, soft bubbles (opt-in).
**Signature:** a breathing animation tied to a real exercise timer. **Never:** fast motion anywhere.

### 3.21 Arcade Cabinet
**Concept:** 80s arcade side art: airbrush, stars, chrome logos. **Fits:** games, events, entertainment, hackathons. Base: Synthwave or Pixel.
**Type:** chrome logo type (layered text-shadows), pixel font for labels (Press Start 2P, small doses), text: Inter.
**Color:** cabinet black #0A0A12 · magenta #FF2E88 · cyan #00E5FF · sun yellow #FFD300 · text #F8F8FF.
**Motion:** attract-mode loop on the hero, coin-insert CTA animation. **Sound:** 8-bit blips (opt-in), one chiptune sting.
**Signature:** "INSERT COIN" that actually starts the product demo. **Never:** using arcade style for serious finance.

### 3.22 Herbarium Editorial
**Concept:** a long-form magazine about nature and craft. **Fits:** blogs, publishers, D2C brands with stories.
**Type:** editorial serif (Newsreader, Source Serif 4) with drop caps; sans captions.
**Color:** cream #FBF7EF · ink #1F1D1A · moss #4E5B31 · clay #A85A3A · muted #6E675E.
**Layout:** long reading column (680 px) with full-bleed image breaks, marginalia, footnotes.
**Motion:** quiet: image reveals with a soft clip-path wipe. **Sound:** none.
**Signature:** drop cap + pull quote composition per article. **Never:** popups mid-article.

### 3.23 Signal Red
**Concept:** emergency signage and safety design: urgent clarity. **Fits:** security, incident management, health alerts, civic tech.
**Type:** DIN-like (Barlow, D-DIN style: Bai Jamjuree) heavy caps; text: Switzer or Satoshi.
**Color:** white #FFFFFF · signal red #D7261E (fills with white bold text ≥ 4.5:1) · ink #111 · safety yellow #FFD400 (fills with ink text) · grey #6B6B6B.
**Layout:** big pictograms, numbered steps, high-contrast bands.
**Motion:** none decorative; state changes flash once (not repeating, < 3/s). **Sound:** clear, short two-tone alert (user-enabled).
**Signature:** a pictogram system. **Never:** decorative red; red for anything not urgent.

### 3.24 Folio Dark
**Concept:** a premium photography portfolio at night. **Fits:** photographers, studios, film, architecture.
**Type:** refined grotesk (Switzer or General Sans; Neue Haas-like) in two sizes only.
**Color:** #0C0C0C · #EDEDED · muted #8C8C8C (large text only; small text #B5B5B5).
**Layout:** images dominate, captions small, horizontal scroll galleries with visible scrollbar.
**Motion:** image transitions with shared-element zoom; cursor shows "View" label (pointer only). **Sound:** none.
**Signature:** full-bleed image with caption set like a film credit. **Never:** watermarks or heavy UI chrome.

### 3.25 Grid Paper Productivity
**Concept:** dotted notebook + sticky notes. **Fits:** todo, planning, notes, students.
**Type:** humanist sans (Instrument Sans) + handwriting accents (Kalam, sparingly).
**Color:** paper #FFFEF9 dotted #E6E3DA · ink #1F2328 · sticky yellow #FFE58A · sticky pink #FFC2D1 · sticky blue #BDE0FE.
**Motion:** stickies peel and stick (rotate ±2°), check marks draw with a pen stroke. **Sound:** pen tick on complete (opt-in).
**Signature:** the empty state is a hand-drawn arrow to "start here". **Never:** heavy shadows.

*(More can be generated with §7. Prefer a fresh direction over reusing the same one for every project.)*

---

## 4. Motion-graphics directions
| Name | Concept | Moves | Fits |
|---|---|---|---|
| Ink Settle | Shapes behave like ink dropped in water | Blur-to-sharp, organic masks, slow 900 ms settles | Calm, premium, editorial |
| Swiss Machine | Grid modules slide like a precise machine | Hard cuts on the beat, 120–200 ms slides, no easing overshoot | Dev, data, B2B |
| Paper Cut | Layered paper with real shadows | 2.5D parallax, folding reveals, stop-motion step (12 fps) | Kids, craft, storytelling |
| Typewriter Cinema | Words type, strike through, rewrite | Caret blink, overtype, backspace corrections | Manifestos, copy-led launches |
| Liquid Data | Numbers and charts morph between states | Path morphs, count-ups, axis re-scaling | Analytics, finance reports |
| Signal Flow | Lines route like circuits/pipes carrying a dot | Stroke draws, dots travel paths, nodes light | Infrastructure, APIs, workflows |
| Collage Riot | Cut-out photos, stickers, tape | Hard pops, jittery stop-motion, overlaps | Culture, music, community |
| Orbit | Objects orbit a central product | 3D camera moves, depth of field | Product launches, hardware |
| Light Table | Slides and film strips on a light box | Slide-ins with glow, loupe zoom | Photo, film, portfolios |
| Kinetic Manifesto | Type is the only actor | Scale jumps, word swaps, masks, rhythm cut to VO | Launches, explainers |
| Particle Field | Thousands of points form the logo/product | GPU particles, flocking, morph to shapes | Only when the brand is about scale/data; budget it |
| Isometric City | Product as an isometric world | Camera pans, little workers, building assembly | Platforms, ecosystems, explainers |

## 5. Sound directions
| Name | Palette | Fits |
|---|---|---|
| Wood & Ceramic | Taps, clinks, soft felt mallets | Calm consumer, food, wellness |
| Precision Clicks | Short filtered clicks, 1–2 kHz, no reverb | Tools, finance, pro apps |
| Glass & Air | Glassy pings, airy pads, long tails (ambient only) | AI, wellness, premium |
| Analog Synth | Warm saw/triangle blips, gentle filter sweeps | Creative tools, music, retro |
| Paper Studio | Paper rustles, pencil, stamps | Notes, editorial, stationery |
| 8-bit Arcade | Square-wave blips, coin sounds | Games, playful |
| Organic Field | Birds, water, wind, wooden percussion | Outdoor, climate, travel |
| Cinematic Hit | Sub drops, risers, whooshes (video only) | Launch trailers |
| Silence First | Almost none; one signature sound | Serious, premium, accessibility-first |

## 6. Video directions
| Name | Format | Fits |
|---|---|---|
| Kinetic Manifesto | Type-only, VO, music bed | Launch, brand |
| Screen Story | Real UI, cursor choreography, zooms to details | SaaS demo, feature tour |
| Paper World | 2.5D cut-paper explainer | Education, kids, services |
| Isometric Explainer | Isometric scenes and process | Platforms, B2B, infrastructure |
| Product Orbit | 3D product, studio light, macro details | Hardware, premium |
| Documentary Micro | Real people (consented), b-roll, honest VO | Mission-driven, community |
| Whiteboard Live | Hand draws while VO explains | Concepts, training |
| Data Story | Animated charts with narration | Reports, finance, research |
| Trailer Cut | Fast cuts, risers, title cards, hit on logo | Games, launches, events |
| Lo-fi Phone | Vertical, handheld feel, captions | Social, creator-led |

## 7. Remix and invention (for strong models; log as Override/Agent judgment)
- **Remix:** take the type of one direction, the color of another, the motion of a third, but keep **one concept sentence** that explains all three. If you can't write that sentence, it's a collage, not a direction.
- **Metaphor mining:** list 10 physical places/objects where the user's job happens offline (a kitchen scale, a ship's bridge, a library card catalogue). Pick the one with the richest materials and rituals.
- **Era × medium:** pick an era (1920s, 1960s, 1990s, 2040s) × a medium (print, signage, packaging, instrument, textile). "1960s airline timetable" → a scheduling app.
- **Constraint cards:** one font only · two colors only · no rounded corners · no images · everything on a visible grid · motion only on scroll. Constraints produce character.
- **Material test:** if the interface were a physical object, what is it made of? Let that decide shadows, texture, sound and motion weight.

Whatever you invent must still pass every gate: contrast, operability, honesty, performance.

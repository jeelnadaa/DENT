# The All-out Protocol

When the user chooses **All-out** (or says "go all out", "best possible", "no limits", "make it insane"), DENT promises **the best result achievable for this specific use case, with nothing missed**. Not "more effects". Every detail that a top studio would cover for this kind of deliverable is covered, verified and documented.

This protocol applies to **every workflow**: create, redesign, extend, audit, system, motion graphics, 3D, sound, voice, video, brand, assets. Each workflow runs its normal steps *plus* the matching sweep in §2.

---

## 1. What All-out changes

| Area | All-out means |
|---|---|
| Understanding | Full brief (problem, JTBD, audience doubts, success metrics), competitor/category scan (principles, never copying), real content gathered from the user |
| Questions | All relevant questions (~10–14, still one at a time), including media: sound, narration, video, generative-tool access, brand assets |
| Planning | PLAN.md with requirement IDs + plan audit table, even for a single page |
| Direction | 2–3 genuinely different directions rendered as style tiles; user picks or combines; concept, category-cliché divergence, signature element(s) |
| Craft | Bespoke hero composition, typography craft at every size, custom illustration/icon/imagery direction, motion system + at least one motion-graphics moment where appropriate, optional sound with toggle |
| Coverage | Every screen state, every breakpoint designed (not shrunk), light + dark (+ high-contrast where relevant), i18n readiness, print styles where relevant |
| Assets | Favicon set, app icons, OG/social images, (video) thumbnail, all licensed and recorded |
| Verification | Every gate with evidence, full keyboard + screen-reader spot check, Lighthouse/perf numbers, journey simulation with failure paths, cross-browser where possible |
| Scoring | Target ≥ 9 overall, no line < 8, with evidence. Run `/dent:improve` rounds yourself until the target is met or a user decision is needed |
| Documentation | DESIGN.md complete (+ MOTION/SOUND/VIDEO specs), licence table, handoff notes, changelog |

All-out never means: ignoring the user's scope, adding features they didn't ask for, inventing proof, or sacrificing performance and accessibility for effects.

**The final All-out check:** "If a world-class studio delivered this for this use case, what would they have that we don't?" Write the answer; fix it or list it.

---

## 2. Sweeps by deliverable (tick every line or mark N/A with a reason)

### 2.1 Landing page / marketing site
- [ ] Message: headline tested at 10 variants; subhead with mechanism; one CTA label used consistently; objection list → FAQ
- [ ] Every claim has proof or is removed; zero invented numbers/logos/quotes/ratings
- [ ] Hero: bespoke type composition, real product visual, works at 320/390/768/1024/1440/1920; header fits on phones
- [ ] Section rhythm: no two adjacent sections share a composition; each section has one job
- [ ] Product demonstration: interactive or animated, real UI, legible on phones (simplified crop)
- [ ] Pricing (if any): honest, toggle changes prices, annual savings computed correctly, comparison table, currency/tax notes, accessible toggle
- [ ] Forms: labels, validation, success, error, loading, autocomplete attributes, no real-person placeholders
- [ ] Built-in surfaces at Match in both themes: tooltips, scrollbars, sliders, checkboxes/radios/switches, selects, selection, caret, placeholder, autofill, file input, backdrops; `verify_page.py --surfaces match` passes; surface sheet captured (`../built-in-surfaces.md`)
- [ ] Navigation: sticky/condensing header (`mwg:shrinking-header-on-scroll`), skip link, mobile menu as a native drawer (`mwg:navigation-drawer`: Esc, swipe, outside tap, no hand-made trap or scroll lock), active section indicator (`mwg:scrollspy`)
- [ ] Footer: legal links, licence/privacy, contact, social with accessible names
- [ ] Dark + light (system default + toggle with persistence, no flash of wrong theme; `mwg:dark-mode`, `mwg:dark-mode-toggle`)
- [ ] Motion: hero entrance, one scroll story, hover system (pointer only), reduced-motion versions, no layout shift
- [ ] Optional sound only if on-brand, opt-in toggle, visual equivalents
- [ ] SEO/meta: title, description, canonical, OG + Twitter cards with a designed 1200×630 image, favicon set (SVG + 32 px + 180 px apple-touch), theme-color, lang attribute, structured data where honest
- [ ] Performance: fonts subset (OFL only) + `font-display: swap` + preload critical + stable fallbacks; images sized + modern formats + lazy below the fold, LCP image eager with `fetchpriority="high"`; no render-blocking scripts; LCP/CLS/INP measured (`mwg:performance`, `mwg:optimize-image-priority`)
- [ ] Modern Web Guidance: every capability's guide retrieved and cross-checked, fallbacks per the support policy, verify_page G13 passed, disclosure written
- [ ] Accessibility: landmarks, heading order, focus visible, contrast both themes, 200 % zoom, 320 px reflow, link purpose, `prefers-reduced-motion`
- [ ] Analytics/consent only if asked; no dark patterns in cookie banners
- [ ] 404 page and print stylesheet (if multi-page)
- [ ] Copy proofread twice; product name consistent; dates and versions real

### 2.2 App / dashboard / SaaS product
- [ ] Top tasks + critical task walked end to end, including every failure path
- [ ] IA map; navigation marks location; deep links/URLs reflect state (filters, tabs, pagination)
- [ ] Every screen: empty (all four types), loading skeleton, error + retry, partial/stale, success, permission-denied, offline
- [ ] Data: realistic varied sample data; 0/1/many/10 000; long names; i18n lengths; numbers/dates/currency by locale
- [ ] Tables: sort, filter chips, column visibility, density, bulk actions, keyboard row actions, sticky header, responsive strategy, virtualisation for large sets
- [ ] Forms: validation timing, error summary for long forms, autosave/drafts, unsaved-changes guard, keyboard submit
- [ ] Built-in surfaces at Match: tooltips on every icon button, scrollbars in every scroll region (tables, sidebars, code, chat), selects, sliders, checkboxes, date fields; surface sheet in light/dark/forced colors (`../built-in-surfaces.md`)
- [ ] Feedback: optimistic updates with rollback, undo, toasts in live regions, confirmations for irreversible actions
- [ ] Power users: command palette, shortcuts + cheat sheet, saved views
- [ ] Roles and permissions states; workspace switching if multi-tenant
- [ ] Theming (light/dark/high contrast), density setting if pro tool
- [ ] Accessibility: full keyboard, focus management in overlays, screen-reader names for charts (data table alternative), status announcements
- [ ] Performance: render cost of lists/charts, bundle size, perceived speed (skeletons, prefetch)
- [ ] Design-system documentation: component sheet in every state

### 2.3 Mobile app (iOS/Android/cross-platform)
- [ ] Native navigation patterns, gestures with visible alternatives, safe areas, notch/dynamic island, keyboard avoidance
- [ ] Dynamic Type / font scaling to the largest sizes; landscape; tablet layouts
- [ ] Haptics mapped to meaning (and settings to disable); sounds opt-in
- [ ] Permission priming screens; offline; background/foreground state restore
- [ ] App icon (all sizes, light/dark/tinted where supported), splash, store screenshots and preview video plan
- [ ] Platform a11y: VoiceOver/TalkBack labels, traits, focus order; reduce motion; bold text; increase contrast

### 2.4 Design system
- [ ] Inventory with classifications; three-tier tokens (primitive → semantic → component); modes (light/dark/high-contrast/density)
- [ ] Every component: purpose, anatomy, variants, sizes, all states, keyboard, ARIA, content rules, do/don't
- [ ] Token export (CSS variables, DTCG JSON, platform files); Figma parity notes
- [ ] Component sheet + documentation pages; versioning and deprecation policy
- [ ] Motion tokens and sound tokens (if sound exists)

### 2.5 Redesign / audit
- [ ] Baseline screenshots of every in-scope screen at 3 widths before changes
- [ ] Inventory of features and behaviours; "must not break" list confirmed
- [ ] Analytics/support pain points gathered if available
- [ ] Findings with evidence, severity, effort; quick wins separated
- [ ] Migration plan (incremental), feature flag/beta strategy, "What's new" moment
- [ ] Before/after with reasons; regression classification for every difference

### 2.6 Motion graphics
- [ ] Concept + 2–3 motion directions; storyboard with timing for every beat; animatic approved
- [ ] Composition of every key frame works as a still (poster test)
- [ ] Timing: holds long enough to read (0.5 s + 0.3 s/word), rhythm varies, one climax, clean ending/loop point
- [ ] Easing and springs from the motion system; no linear movement except mechanical/continuous
- [ ] Typography: kinetic type legible at every frame; no orphan words mid-animation
- [ ] Technology justified; fallbacks (static poster, reduced motion, no WebGL)
- [ ] Performance: 60 fps target measured, GPU-friendly properties, assets compressed, lazy start, pause offscreen
- [ ] Sound sync points (if audio) on the audio clock
- [ ] Exports for each destination (web embed, MP4/WebM, GIF/APNG/animated SVG for README, poster frame)
- [ ] Accessibility: pause control for > 5 s, no flashes, reduced-motion version, captions/description for meaning

### 2.7 3D / real-time
- [ ] Justified vs 2.5D/video; art direction (lighting, materials, camera language)
- [ ] Asset pipeline: glTF/GLB, Draco/Meshopt compression, KTX2 textures, LODs; licences recorded
- [ ] Budgets: draw calls, triangles, texture memory, load size; measured fps on a mid-range profile
- [ ] Interaction: orbit limits, touch gestures, keyboard alternative, reset view
- [ ] Fallbacks: static image/video, no-WebGL message, reduced motion = no auto-rotation
- [ ] Cleanup: dispose geometries/materials/textures on unmount

### 2.8 Sound / sonic identity
- [ ] Direction + palette + interaction map with repeat limits; silence policy
- [ ] Sonic logo (1–3 s) if identity is in scope; variations (short, long, UI)
- [ ] Mixing: consistent loudness, no clipping, frequency balance on phone speakers and headphones
- [ ] Formats + fallbacks, preloading strategy, sprite or individual files, sizes within budget
- [ ] Controls: off by default unless requested, mute + volume, persistence, respects system/reduced-motion/data-saver signals
- [ ] Visual equivalent for every sound; works fully muted; no autoplay
- [ ] Licences for every asset; attribution text where required

### 2.9 Voice / narration
- [ ] Script written for the ear, timed aloud, approved; pronunciation guide (names, acronyms, product terms)
- [ ] Voice choice justified (human/TTS engine + voice); consent and rights documented
- [ ] Recording/synthesis clean: no clicks, breaths natural, room tone consistent
- [ ] Loudness to platform target; true peak ≤ −1 dBTP
- [ ] Captions (SRT/VTT) checked against audio; transcript published

### 2.10 Video (launch, trailer, explainer, demo, social)
- [ ] Brief with one message, CTA, platforms; script approved; storyboard + animatic locked before polish
- [ ] Hook in the first 2 s; product name early; CTA clear at the end
- [ ] Visual system consistent with the brand (type, color, motion tokens)
- [ ] Sound: narration, music bed (licensed), SFX palette, ducking, loudness target
- [ ] Captions burned-in for social + sidecar files; on-screen text legible on phones
- [ ] Versions: 16:9, 9:16, 1:1 cuts; durations per platform; safe areas; thumbnail/poster
- [ ] QA: ffprobe metadata, A/V sync, no typos, claims true, no flashes > 3/s, licences recorded

### 2.11 Brand and assets
- [ ] Logo: wordmark + symbol + lockups, clear space, minimum sizes, monochrome/inverse versions, favicon legibility at 16 px
- [ ] Color system with accessible pairs; type system; voice; imagery rules; motion and sonic cues
- [ ] Applications: favicon set, app icon, OG image, social avatars/banners, email header, slide template, README banner
- [ ] Usage guidelines (do/don't); licence table

### 2.12 Email, docs, data viz, e-commerce, forms (pick what applies)
- Email: table-based layout tested in major clients, dark-mode friendly images, plain-text version, accessible alt text, unsubscribe.
- Docs: search, TOC, code copy buttons, version selector, dark mode, "edit this page", 404, keyboard nav.
- Data viz: question per chart, honest axes, direct labels, color-blind safe palette, table alternative, responsive charts, animated transitions from previous state.
- E-commerce: product imagery gallery + zoom, variants with stock states, transparent total price, guest checkout, address autocomplete, error recovery, order confirmation and emails.
- Forms: field order, input types/inputmode/autocomplete, inline validation timing, error summary, save progress, success page.

---

## 3. All-out close-out
1. Scorecard (target ≥ 9, no line < 8) with evidence and the improve rounds you ran.
2. The sweep(s) used, every line ticked or N/A with a reason.
3. The "world-class studio" gap answer and what you did about it.
4. Attribution: DENT / user / agent judgment / overrides.
5. Everything that needs the user (real proof, licences to buy, accounts, approvals).

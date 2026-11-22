# Workflow — Questions, Effort Levels and Change Requests

Used by SKILL.md › Workflow. First decide the **mode** (Create, Redesign, Audit, Extend, Implement, Adopt — see `modes-existing-products.md` §1). **Asking questions is the top priority** before designing anything. This file covers: how to ask (§1), effort levels (§2), the question order (§3), handling change and add-on requests (§4), defaults when the user says "don't ask" (§5), and how to avoid overwhelming the user (§6).

---

## 1. How to ask (rules for every question)

1. **One question at a time.** Wait for the answer before asking the next. Never send a wall of questions.
2. **Tailor options to the user's prompt.** Read what they already said and offer only options that fit. A prompt about "a meditation app" should never get "Cyberpunk" as an option.
3. **Few options: 2–4.** Put the one you recommend first and mark it **(Recommended)**, with a one-line reason tied to their product.
4. **Explain every option** in one short, plain line: what it looks/feels like and what it's good for. The user should be able to choose without knowing design terms.
5. **Always allow a free answer.** Add "Something else — describe it in your own words" (if the question tool has a built-in free-text/"Other" choice, rely on that instead).
6. **Always include an escape option** on the first question, and offer it again if the user seems impatient: **"Skip the questions — you decide everything"**. If chosen, stop asking and follow §5 below.
7. **Skip what's already answered.** If the prompt says "dark mode fintech dashboard", don't ask about mode or product type; confirm in one line instead.
8. **Use the question tool when available** (e.g. a multiple-choice question UI). Otherwise ask in plain text with numbered options.
9. **Show, don't only tell, when useful.** For visual choices (style, palette, type), a tiny visual preview (color swatches, font sample line, mini mockup) helps more than words.
10. **Keep the total short.** Follow the per-level counts in §3 (Essential ≤ 3 … All-out ~10–14). Stop early if you have enough to design well.
11. **Record every answer** in the Decision Log (SKILL.md › Workflow › Decision Log).

### Option format (example)
> **Which overall look fits your app best?**
> 1. **Minimal (Recommended)** — lots of white space, one accent color, very clean. Best for focus and productivity apps like yours.
> 2. **Japandi / calm** — warm beige and natural tones, soft and quiet. Good if you want it to feel relaxing.
> 3. **Playful** — bright colors, rounded shapes, bouncy animations. Good if your users are younger or you want it fun.
> 4. **Something else** — describe it or share a site/app you like.
> 5. **Skip the questions — you decide everything**

---

## 2. Effort levels

The user decides how deep the design goes. **Ask this first** (question 0), with these explanations (shorten them to one line each in the question):

> **How far should I go with this design?**
> 1. **Essential** — clean, consistent and correct, nothing extra. Fastest. Good for internal tools, prototypes, MVPs.
> 2. **Standard (Recommended)** — a complete, professional design in your chosen style, with all states and subtle animation.
> 3. **Polished** — premium feel: refined typography, hover and scroll effects, dark mode, icons/images direction, full design review.
> 4. **All-out** — the best possible result for your use case with nothing missed: research, 2–3 directions to choose from, every state and screen size, motion (and sound/video if relevant), deep accessibility, assets, and self-review until it scores 9/10.
> 5. **Skip the questions — you decide everything**

**Question tools with a 4-option limit** (Claude's allows 4): show Essential · Standard (Recommended) · Polished · All-out, and add to the question text "…or answer 'you decide' to skip all questions". The same applies to every question: never exceed the tool's option limit; split long menus into grouped questions (see `motion/motion-menu.md` §1).

### The floor (every level, including Essential — never skipped)
- **Consistency:** tokens for color, type, spacing, radius, elevation; each component defined once and reused (`foundations-and-components.md` §3, › Components).
- **Color rules:** a concept-led palette (brand colours, the style's, or `scripts/palette.py`; `color.md` §12), every role pair contrast checked, never color alone.
- **Foundation components** needed by the screen (buttons, inputs, selection controls, cards, nav…) with default, hover, focus, disabled and error states.
- **Core laws:** clear hierarchy, one primary action, proximity/alignment, Fitts, Hick, Jakob.
- **Accessibility minimum** (SKILL.md › Accessibility) and the pre-ship checklist's core items.
- **Modern Web Guidance** for any web code (`modern-web-guidance.md`): effort changes how much is built, never whether the guides are followed.
- **Decision Log**, and DESIGN.md after approval.

### What each level adds
| Area | Essential | Standard | Polished | All-out |
|---|---|---|---|---|
| Questions | ≤ 3 | ~5–6 | ~7–9 | ~10–14 |
| Aesthetic style | Minimal or a style's tokens only | Full style file applied | Full style + signature moves refined | Style + accent style, custom details |
| Components | Only those needed, core states | Full specs incl. loading/empty/selected | + micro-interactions | + full spec for every component used, variants |
| Screen states | Default + error | + empty, loading, success | + edge cases, content stress | + offline, permissions, all edge cases |
| Layout & responsive | Mobile + desktop | All breakpoints + platform rules | + container queries, fluid type/spacing | + every surface in scope (tablet, desktop app…) |
| Patterns | Basic structure | Matching page/flow pattern | + industry playbook | + IA/sitemap, full flows |
| Motion (the floor in `motion/motion-menu.md` §2 is authoritative) | Hero entrance + hover on all interactive elements + micro-interactions (pages); state transitions and micro-interactions (apps) | + varied scroll reveals, one scroll-linked moment, text reveal; motion tokens | + depth or pinned scene, view transitions, animated SVG, ambient, magnetic hero CTAs | + a signature motion-graphics sequence, scrubbed scroll story, pointer layer, sound sync if relevant |
| Typography | Type scale, 1–2 fonts | + style pairing | + typography craft (tracking, balance, fluid) | + expressive/kinetic moments |
| Color & theme | One mode | One mode, full semantic set | Light + dark | + high contrast, theme switching, brand scales |
| Built-in surfaces (`built-in-surfaces.md`) | Tint: accent on native controls, themed scrollbars, selection, no `title` tooltips | Match: tooltips, scrollbars, sliders, checkboxes, selects, selection, caret, placeholder | + autofill, validation, file input, progress, disclosure markers, backdrops; surface sheet | + every surface in every state and theme, forced colors, style-specific personality |
| Copy | Clear labels & errors | UX-writing rules applied | Voice & tone defined | Full microcopy set |
| Icons/images | One icon set | + image treatment | Illustration/imagery direction | Custom illustration/icon system, art direction |
| Accessibility | Minimum bar | + component ARIA patterns | + full WCAG 2.2 AA checklist | + cognitive/motor/vision deep pass |
| i18n | — | Logical CSS, no concatenated strings | + text expansion/RTL ready | Full localization plan, scripts, formats |
| Data viz | Correct chart type | Data-viz rules | + interaction, dark-mode charts | + annotations, small multiples, accessibility tables |
| Assets | — | Favicon | + OG/share image, app icon | + brand kit, social/marketing templates |
| Brief & concept | Concept sentence (internal) | Concept sentence + signature element | One-page brief (confirmed) + concept | Brief + 2–3 divergent directions + success metrics & measurement plan |
| Research & brand | — | — | Proto-persona + key flow | Personas/JTBD, journey, sitemap, mini brand, usability test plan |
| Ethics | No deceptive patterns (always) | same | + persuasion review | + full ethics audit |
| Quality | Pre-ship checklist (core) | + visual verification | + full review rubric & anti-patterns | + multiple variations to choose from, rubric ≥ 4 everywhere |
| Output | Screen(s) + short log | + full DESIGN.md | + tokens 3-tier | + token export (DTCG), handoff notes |

**All-out** means the best achievable result for the user's specific use case with nothing missed: run `workflow/all-out.md` (mandatory sweep for the deliverable, score target ≥ 9 with no line < 8, self-run improve rounds). It applies to every workflow, including motion, sound, voice and video.

Rules:
- Stay inside the chosen level. Don't add unrequested extras (that overwhelms the user); offer the next level in **one line** at the end ("Want hover/scroll animations and dark mode? That's the Polished level.").
- The user can change level anytime ("go all out now") — continue from the current design; don't restart.
- Any single extra can be added without changing level (§4 add-on requests).

---

## 3. Question order (ask only what's still unknown)

| # | Topic | Why it matters | Typical tailored options |
|---|---|---|---|
| 0 | **Effort level** (always ask first, unless the prompt already says e.g. "quick" or "go all out") | Decides how deep everything else goes and how many more questions to ask | Essential · Standard (Recommended for most) · Polished · All-out — see §2 for the wording |
| 1 | **What are we designing & for whom?** (product type, target users) | Decides patterns and tone | Infer from prompt; confirm in one line if clear |
| 2 | **Platform** | Decides platform rules (platforms-and-devices.md) | Web (responsive) · iOS · Android · Desktop app · Cross-platform |
| 3 | **Scope of this round** | Avoids over-building | One key screen first (Recommended) · A full flow (e.g. onboarding) · Full set of main screens · Design system only |
| 4 | **Overall look (aesthetic style)** | Biggest visual decision | 2–3 styles from styles/_styles-index.md that fit the product + feeling words in the prompt; or "I have a reference site/screenshot" (→ inspiration-and-reference-sites.md §2) |
| 5 | **Light or dark** | Base of the palette | Light · Dark · Both (with toggle) — recommend based on product and context of use |
| 6 | **Colors** | Brand feel | "I have brand colors" (ask for hex/logo) · 2–3 concept palettes (color.md §13, or seeds run through `scripts/palette.py`), each shown as swatches in both themes with its scene line |
| 7 | **Typography** | Personality + readability | First where fonts may come from (free and open · fonts I own / Adobe Fonts · suggest paid fonts · you decide), then 2–3 pairings by voice (typography.md §2–§3, fresh candidates from `scripts/fonts.py`), each with a real sample line |
| 8 | **Density** | Spacing and component sizes | Comfortable (Recommended for most) · Compact (data-heavy/pro tools) · Spacious (marketing/luxury) |
| 9 | **Motion: which kinds** (multi-select) **+ intensity** | How alive it feels; what gets built | Kinds: hero entrance · scroll · hover · micro-interactions · page/view transitions · text · data · layout · ambient · cursor · SVG/illustration · loading/feedback · 3D/depth · gestures · You choose. Intensity: Subtle · Balanced (Recommended) · Expressive · Cinematic. Script and recommended sets: `motion/motion-menu.md` |
| 9b | **Built-in surfaces** (Standard+ visual builds) | Tooltips, scrollbars, sliders, checkboxes and dropdowns otherwise show OS defaults | Match my design everywhere (Recommended) · Brand tint only · Keep the native look · Let me choose per element. Script: `built-in-surfaces.md` §2 |
| 10 | **Corner shape** (only if the style allows choice) | Personality | Sharp (0–4px) · Soft (8–12px) · Round (16px+/pills) |
| 11 | **References** (optional) | Fast alignment | "Any app or site whose look you like?" — free answer |
| 12 | **Content & must-haves** | Real content beats placeholders | Key sections/features, logo, real copy, images available? |
| 13 | **Media sources** (any build with imagery, footage, voice, music, 3D) | Quality, cost and licence of everything not drawn in code | Local model (installed after a yes) · free cloud tier · paid provider or connector (any, even unlisted) · your own assets. Script: `media-sourcing.md` §2 |

**How many questions per effort level:** Essential ≤ 3 (effort, look/colors, light/dark) · Standard ~5–6 · Polished ~7–9 · All-out ~10–14 (adds brand, references, content, research questions). Still one at a time; the user can say "skip" anytime.

Stop asking when you can design confidently. For anything you didn't ask about, choose using §5 and record it in the Decision Log as **"Chosen by default"** so the user can review it.

---

## 4. Asking about changes (after a draft is shown)

When the user asks for a change:
1. **Restate the change in one line** to confirm the scope ("You want the primary button color warmer — only that, everything else stays?").
2. If the request is vague ("make it pop", "looks off", "more modern"), ask **one** clarifying question with 2–4 concrete interpretations, each explained. Example for "make it pop":
   1. **Stronger accent color** — the main button and highlights get a bolder color.
   2. **Bigger, bolder headline** — more contrast between title and text.
   3. **More depth** — subtle shadows/glow so cards stand out from the background.
   4. **Add motion** — elements animate in and react on hover.
3. **Change only what was asked.** Don't redesign other parts. If the change has side-effects (e.g. new accent color fails contrast on buttons), say so and propose the smallest fix.
4. Update the Decision Log with the change and the reason.
5. Show the result and ask if it's right before moving on.

### Add-on requests ("now add animations", "add dark mode"…)
When the user asks to add something to an existing design:
1. **Look it up again** in the skill (table below) — don't improvise from memory.
2. Read DESIGN.md / the Decision Log so the addition matches what exists.
3. Ask **1–2 short questions** with explained options (scope and intensity), e.g. for animations: *Where?* (buttons & hovers only · page transitions · scroll reveals · all) and *How strong?* (subtle · expressive).
4. Add **only** that, using existing tokens (add new tokens if needed, e.g. motion tokens).
5. Verify (quality-review.md Part 1), update Decision Log + DESIGN.md changelog.

| User asks for… | Read |
|---|---|
| "Let's brainstorm", "what direction?", "is this a good idea?" | workflow/brainstorm.md (`/dent:brainstorm`) |
| Where media comes from, "use my ElevenLabs/Runway/…", "find me a free model", local vs cloud vs own assets, installing a model | media-sourcing.md (+ `/dent:doctor`) |
| "What can you do on this machine?", missing tools, GPU, installed voices | `/dent:doctor` (scripts/doctor.py) |
| Any web code change: HTML, CSS, client-side JS, a component, "use the modern way", browser support, Core Web Vitals, "modernize the codebase" | modern-web-guidance.md (search + retrieve the MWG guides first; native first; legacy scan only for broad modernization) |
| Animations, transitions, micro-interactions, "more motion" | `motion/motion-menu.md` (ask kinds + intensity, minimums) + `modern-layer.md` (motion system, micro-interactions, reduced motion, performance) |
| Hover effects | `modern-layer.md` §7.4 |
| "Tooltip/scrollbar/slider/checkbox/dropdown looks default", "make native controls match", custom scrollbars, text highlight colour | built-in-surfaces.md (`/dent:surfaces`) |
| Scroll effects, parallax, sticky storytelling | `modern-layer.md` §7.5 |
| "More modern / premium / polished" | `modern-layer.md` + quality-review.md Part 2 §4 |
| Dark mode / theme switch | color.md Part 1 §7 + design-tokens-and-code.md Part 1 §4 + `mwg:dark-mode`, `mwg:dark-mode-toggle` |
| Change style / "make it look like X style" | styles/_styles-index.md + the style file |
| "Make it look like this site/screenshot" | inspiration-and-reference-sites.md §2 |
| Responsive / mobile / tablet / desktop app | platforms-and-devices.md |
| New page or flow (pricing, onboarding, checkout, settings…) | page-and-flow-patterns.md (+ industry-playbooks.md) |
| Charts, dashboard, KPIs, tables | data-visualization.md |
| Accessibility improvements | accessibility.md |
| Translation, RTL, Hindi/Indic, other languages | internationalization.md |
| Better copy, error messages, tone | ux-writing.md |
| Icons, illustrations, photos | icons-illustration-and-imagery.md |
| Fonts, "change the typography", "fonts look generic" | typography.md (§0 method, `scripts/fonts.py`) |
| Logo, brand | brand-identity.md |
| Favicon, app icon, OG image, social posts, posters, slides, email | assets-and-marketing-graphics.md |
| Motion graphics, kinetic type, animated hero, scroll story, generative visuals | motion/motion-graphics.md + motion/motion-tech-catalog.md (`/dent:motion-graphics`) |
| 3D, WebGL, product viewer | motion/3d-and-realtime.md (`/dent:3d`) |
| Sound, UI sounds, sonic logo, ambience, music | audio/sound-design.md + audio/audio-implementation-and-verification.md (`/dent:sound`) |
| Narration, voice-over, TTS, captions | audio/voice-and-narration.md (`/dent:voice`) |
| Any video: launch, trailer, explainer, demo, social | video/video-creative-direction.md (creative menu, directions, genre bar) + video/video-types-and-craft.md + video/video-tools-and-pipeline.md + templates/video-kit/ (`/dent:video`, `/dent:launch-video`) |
| "Make the video more creative / less generic", "custom typography in the video", "what style should the film have?" | video/video-creative-direction.md §2–§6 |
| Which library / component kit / chart / table / editor | catalog/component-selection.md (`/dent:components`) |
| "Score it" / "make it better" after a draft | workflow/scoring-and-closeout.md (`/dent:score`, `/dent:improve`) |
| Haptics, AR/VR, watch, TV, car, voice UI, AI/agent UI | platforms-and-devices.md §5–6, page-and-flow-patterns.md §16 |
| Conversion, pricing psychology, "is this a dark pattern?" | persuasion-and-ethics.md |
| Research, personas, sitemap, navigation structure | research-and-information-architecture.md |
| Code / convert to React, Tailwind, Flutter, SwiftUI… | design-tokens-and-code.md Part 2 |
| Review / critique / "why does it look off?" | quality-review.md + modes-existing-products.md §4 (audit report) |
| Redesign / modernize an existing product, work in an existing codebase or UI library | modes-existing-products.md |
| Date picker, file upload, stepper, command palette, data table features, kanban, calendar, OTP, carousel… | components-extended.md |
| Teams, roles, billing, notifications center, audit log, versions, collaboration, import/export, 2FA, account deletion | complex-product-patterns.md Part 1 |
| Blog, docs site, changelog, about/careers, contact, 404, legal, comparison, waitlist, case study | complex-product-patterns.md Part 2 |
| "Make it less generic / more unique", concept, directions, composition | creative-direction.md |
| Brief, goals, metrics, A/B tests, "how do we know it works?" | design-brief-and-metrics.md |
| Figma, Storybook, previews, handoff to developers | tooling-and-handoff.md |

---

## 5. When the user says "don't ask, just decide"

Choose the best default from this skill, in this order, and record each as **"Chosen by default"** in the Decision Log:
0. **Effort level:** from the prompt's wording ("quick/simple" → Essential, "go all out/premium/complete" → All-out); otherwise **Standard**.
1. **Product type & platform:** infer from the prompt; if unclear → responsive web.
2. **Style:** match the prompt's words and product type using `styles/_styles-index.md` → "Pick by feeling". If nothing matches: **Minimal** for apps/tools, **Premium Product** for marketing pages.
3. **Mode:** light for productivity, reading, commerce, daytime use; dark for media, creative, developer tools, night use.
4. **Colors:** a concept palette: the matching scene in `color.md` §13 or a seed from the concept run through `scripts/palette.py make` (both themes, contrast-checked, no cliché hit). A style's starter colors only when the style depends on them.
5. **Typography:** free and open fonts; a pairing by voice (`typography.md` §2–§3, `scripts/fonts.py`), never an overused-registry face by default and never the previous project's pairing.
6. **Density:** comfortable; compact for data-heavy tools.
7. **Motion:** the recommended set for the product type at Balanced intensity (`motion/motion-menu.md` §4), meeting the floor for the effort level (§2).
7b. **Built-in surfaces:** Tint at Essential, Match at Standard and above; in an existing product, its current level applied consistently (`built-in-surfaces.md` §2).
7c. **Media sources:** local models when the machine runs them and their licence fits (installing needs a yes, so without one use code-built media), otherwise code-built media or verified free libraries (`media-sourcing.md` §2).
8. Everything else: DENT defaults (`foundations-and-components.md`, `modern-layer.md`).

Then present the design with a short "Decisions I made" summary and invite changes. The user can still change anything later.

---

## 6. Don't overwhelm the user
- **One question per message**, 2–4 options, one-line explanations. No walls of text.
- **Never mention internal file names, sections or labels** ([Law], [Rule]) to the user unless they ask how the skill works. Say the reason in plain words ("so text stays readable").
- **Decision Log stays short in chat:** the 5–8 most important rows; the full log lives in DESIGN.md.
- **Match reply length to effort level:** Essential = brief; All-out = more detail, still skimmable (headings, short bullets).
- **Progressive disclosure:** show what was asked; offer the next step in one line at the end.
- **Visual previews over descriptions** for colors, fonts and styles when possible.
- **Respect "stop asking":** switch to defaults immediately and say what you chose afterwards.

# Orchestration: how `/dent` turns any request into the right commands

Most users will only ever type `/dent` (or just describe what they want). They should still get everything the focused commands offer. This file is the router: read the request, detect **what they actually want**, pick a **pipeline** of sub-commands, run them in order, and finish with verification and a score.

Follow it literally. It is written so that even a small model can apply it step by step.

---

## Step 1: Extract signals from the request

Read the whole message (and any files, screenshots, URLs, DESIGN.md in the project). Fill in this card silently:

```
DELIVERABLE: what will exist at the end? (page, app screen, flow, design system, review, video, sound set, voice-over, motion piece, 3D scene, brand kit, assets, copy, fix)
STATE:       nothing exists | something exists (code, screenshot, URL, DESIGN.md) | a plan exists (PLAN.md)
VERB:        create | redesign | improve/polish | fix | review/audit | check/verify | extend/add | build/implement | explain/plan | score
MEDIA:       none | motion | motion graphics | 3D | sound | voice | video (list all that apply)
EFFORT:      stated? (quick → Essential, "premium/polished" → Polished, "all out/best/insane" → All-out) else ask
RISK:        payments, auth, personal data, deletion, production system? (→ Critical)
CONSTRAINTS: stack, brand, deadline, platform, "don't ask me questions"
```

## Step 2: Map signals to commands

Use the **first matching row** for the main command, then add **companion commands** from the right column.

| If the request… (signals / typical words) | Main command | Add when relevant |
|---|---|---|
| Is about a single thing being broken ("button doesn't work", "overflows on mobile", "text is cut off") | `fix` | `verify` |
| Asks what is wrong / for feedback / critique, without asking for changes ("review", "audit", "what do you think", screenshot + question) | `audit` (existing product) or `review` (something just built) | `accessibility` if a11y is mentioned |
| Asks to check / test / confirm it works ("does it work on mobile?", "test it") | `verify` | `responsive`, `accessibility` |
| Asks for a plan, approach, estimate or "how would you…" without building | `plan` | `directions` for new visual work |
| Mentions an existing product + "redesign / modernize / refresh / make it look better" | `redesign` | `directions`, `system`, `polish` |
| Mentions an existing product + "add / new page / new feature / also needs" | `extend` | `components` for complex widgets |
| Has a PLAN.md / DESIGN.md / spec and says "build / implement / code it" | `implement` | `components`, `verify` |
| Works but "make it nicer / more premium / cleaner / pop / tighten" | `polish` | `type`, `motion`, `copy` |
| "Mobile", "responsive", "tablet", "breaks on small screens" | `responsive` | `verify` |
| "Accessible", "WCAG", "screen reader", "keyboard", "contrast" | `accessibility` | `verify` |
| Tokens, theme, design system, component library for the team | `system` | `components`, `handoff` |
| "Which library / should I use X or Y / install a table/editor/calendar" | `components` | — |
| "Options", "directions", "concepts", "moodboard", "not sure what style" | `directions` | `type` |
| Headline, hero title, typography, font pairing | `type` | `copy` |
| Words: copy, headline text, microcopy, error messages, tone | `copy` | — |
| Logo, brand, identity, name lockup, brand colors | `brand` | `assets`, `sound` (sonic logo) |
| Favicon, OG image, icons, illustrations, images, licences | `assets` | `brand` |
| Hover, transitions, micro-interactions, "animate the UI" | `motion` | — |
| Animated hero, kinetic type, scroll story, animated illustration, generative visuals, GIF/animated SVG | `motion-graphics` | `sound` if sound is mentioned, `3d` if depth is needed |
| 3D, WebGL, product viewer, Three.js, scene, "rotate the product" | `3d` | `motion-graphics` |
| Sound, UI sounds, audio feedback, sonic logo, ambience, music for the product | `sound` | `voice` |
| Narration, voice-over, TTS, "read this aloud", podcast intro | `voice` | `sound` |
| Launch video, release video, Product Hunt video, teaser, reveal | `launch-video` | `voice`, `sound`, `motion-graphics` |
| Any other video: explainer, trailer, demo, tutorial, social short, ad, title sequence | `video` | `voice`, `sound`, `motion-graphics` |
| "Score it", "how good is it", "rate it" | `score` | — |
| "Improve it", "make it better" after a score exists | `improve` | — |
| Docs, handoff, DESIGN.md, specs for developers | `handoff` | — |
| New page, site, app, screen, dashboard, flow, onboarding, form, landing page (nothing exists yet) | `create` | `directions` (Polished+), `components`, `motion`, `copy`, `assets` |

**Several deliverables in one request** ("a landing page and a launch video with narration") → run one pipeline per deliverable, in dependency order (the page/brand first, then media that reuses it), sharing one DESIGN.md.

**Nothing matches** → it's a design question; answer it directly using the relevant reference, or ask one clarifying question with 2–4 interpretations.

## Step 3: Expand into a pipeline

Each deliverable has a default pipeline. Commands in brackets run only at the effort levels shown. Every pipeline ends with **verify → score**, and with **improve** when below target (automatically at All-out).

| Deliverable | Pipeline |
|---|---|
| Landing page / marketing site | [directions: Polished+] → create (recipe `recipes/landing-page.md`) → [type, copy: always inside create] → [motion: Standard+] → [motion-graphics: All-out] → [assets: Polished+] → verify → score → [improve] |
| App screen / dashboard / flow | [plan: Advanced+] → create or extend (recipe `recipes/app-and-dashboard.md`) → components (if complex widgets) → [motion: Standard+] → verify → score → [improve] |
| Redesign | audit → plan → [directions: Polished+] → redesign → verify (with regression) → score |
| Existing UI "make it better" | score → polish → verify → score (show before/after) |
| Bug / visual defect | fix → verify |
| Design system | system → components → handoff → verify (component sheet) |
| Brand kit | directions → brand → assets → [sound: sonic logo if asked or All-out] → handoff |
| Motion graphics piece | directions (motion section) → motion-graphics → [sound] → verify (motion) → score |
| 3D experience | plan → 3d → [motion-graphics] → verify (perf + fallback) → score |
| Sound for a product | sound → verify (audio) → score |
| Voice-over | voice → verify (audio + captions) |
| Explainer / trailer / demo / social video | video → [voice] → [sound] → [motion-graphics] → verify (video QA) → score |
| Launch video | launch-video → voice (if narrated) → sound → verify (video QA) → score |
| Review only | audit or review → (stop; offer fixes) |

Before running the pipeline, tell the user in **one line** what you'll do, e.g.:
> "Plan: I'll explore 2 directions, build the landing page, add motion, check it at 6 screen sizes, and score it. First question: how far should I go?"

## Step 4: Ask only what the pipeline needs
Merge the questions all commands in the pipeline need; remove duplicates; ask the most important first, one at a time (`../workflow-questions-and-effort.md`). Effort first (unless stated). Then, only if relevant and unknown:
- visual: style direction, light/dark, brand colors/fonts;
- media: sound on/off, narration voice, video length/platform, **generative tool access** (image/video/voice);
- content: real proof, screenshots, logo.
"Don't ask" / non-interactive → defaults, listed at the end.

## Step 5: Run, carrying context forward
- Each command's output feeds the next: chosen direction → DESIGN.md → used by create, motion-graphics, video and sound so everything shares one identity (same type, color, motion personality, sonic palette).
- Keep one Decision Log across the pipeline.
- If a step reveals a different need (audit finds the problem is IA, not visuals), update the pipeline and say so in one line.

## Step 6: Close
One close-out for the whole pipeline (`scoring-and-closeout.md`): what was built, gates, scorecard, attribution, next step. If several deliverables, one scorecard each.

---

## Worked examples

1. **"/dent make a landing page for my meditation app"** → DELIVERABLE landing page, STATE nothing, VERB create, MEDIA none (maybe motion), EFFORT unknown → main `create`; pipeline: directions (if Polished+) → create → motion → verify → score. First message: one-line plan + effort question.

2. **"/dent this dashboard looks bad on my phone"** + screenshot → VERB fix/responsive, STATE exists → main `responsive` (+ `verify`). No effort question needed (it's a fix); ask only if the code isn't available.

3. **"/dent go all out: landing page + launch video with voice-over for DENT"** → two deliverables. EFFORT All-out (stated) → All-out protocol. Pipelines: landing page (directions → create → type → motion-graphics → assets → verify → score → improve) then launch video (launch-video → voice → sound → verify → score), sharing DESIGN.md. Questions: direction pick, sound on the site?, voice type, video length/platforms, generative video access.

4. **"/dent is this accessible?"** + URL → main `accessibility` in audit form (report, don't fix), then offer fixes.

5. **"/dent which table library should I use?"** in a Vue project → `components`: detect Vue, compare TanStack Table (Vue adapter), AG Grid Vue, PrimeVue DataTable; recommend one.

6. **"/dent add sound to my app"** → `sound`: ask role (feedback vs identity), confirm opt-in default, map 3–6 meaningful events, implement with mute/volume, verify.

7. **"/dent improve it"** after a scorecard exists → `improve`; if no scorecard exists → `score` first, then `improve`.

# Video Types and Craft

What kind of video to make, how each type is structured, and the craft that makes it feel professional. Tools and production pipeline: `video-tools-and-pipeline.md`. Plan template: `templates/VIDEO.md`. Used by `/dent:video`, `/dent:launch-video`.

---

## 1. Types and sub-types

| Type | Sub-types | Length | Goal |
|---|---|---|---|
| **Launch** | Teaser · Reveal · Feature tour · Manifesto · Changelog/"What's new" | 10 s – 2 min | Make people care and act now |
| **Trailer** | Cinematic · Gameplay/product-play · Story-led · Montage | 30 s – 2 min | Emotion + curiosity |
| **Explainer** | Animated 2D (flat/character) · Kinetic typography · Whiteboard/hand-drawn · Isometric · Screencast/UI-led · 3D · Live-action/hybrid · Data explainer | 60 s – 3 min | Understanding |
| **Product demo** | Walkthrough · Use-case story · Feature deep-dive · Comparison | 1–5 min | Show it working |
| **Tutorial / how-to** | Step-by-step screencast · Quick tip · Course lesson | 30 s – 15 min | Competence |
| **Social short** | Hook-first vertical · Loopable · Meme/trend format · Creator-style talking head | 6–60 s | Reach and engagement |
| **Ad** | Bumper (6 s) · 15 s · 30 s · Pre-roll (skippable, hook in 5 s) | 6–30 s | Single action |
| **App store preview** | App Store/Play preview (portrait or landscape), feature-by-feature | 15–30 s | Install |
| **Title / brand film** | Title sequence · Logo reveal · Brand manifesto · Event opener/sizzle | 5 s – 2 min | Identity and mood |
| **Data story** | Animated report · Chart race · Map story | 30 s – 3 min | Insight |
| **Case study / testimonial** | Customer story (real, consented) · Before/after | 1–3 min | Trust |
| **Music/lyric video** | Kinetic lyric · Visualiser | Song length | Art and identity |

## 2. Launch videos (most requested)

| Sub-type | Length | Structure (beats) | Notes |
|---|---|---|---|
| **Teaser** | 10–20 s | Mystery hook (0–2 s) → 2–3 glimpses (no full reveal) → date/"Coming soon" + name | Withhold; one striking visual idea; sound design does the heavy lifting |
| **Reveal** | 30–45 s | Hook/problem (0–3 s) → product name + one-line promise (3–8 s) → 3 hero moments of the product in use → CTA + URL | Name early; real UI; one message |
| **Feature tour** | 60–90 s | Hook → promise → 3–5 features, each: "what you do" + real UI moment + benefit line → proof → CTA | Each feature ≤ 12 s; consistent transition device |
| **Manifesto** | 45–90 s | Belief statement → what's broken in the world → what we believe instead → the product as the proof → rallying CTA | Kinetic type + VO + music; few UI shots |
| **What's new / changelog** | 20–60 s | "New in vX" → each change as a quick before/after → upgrade CTA | Fast, factual, version number real |

Launch rules: the **first 2 seconds** must be interesting with sound off; product name visible by ~5 s (except teasers); show the real product (screen recordings or faithful HTML recreations, never invented features); end card with name, one-line promise, URL/CTA, held ≥ 2 s; deliver 16:9, 9:16 and 1:1 cuts with captions.

## 3. Explainer structures
- **Problem → Solution → How → Proof → CTA** (classic, 60–90 s).
- **Story:** character with a problem → discovers product → does the job → outcome (character-led 2D).
- **Concept-first:** "Here's the idea" → analogy visual → mechanism → why it matters (for abstract tech: use an analogy from the directions library's metaphors).
- **Kinetic manifesto:** type-only + VO, every line a composition.
Script time budget: 60 s ≈ 150 spoken words.

## 4. Craft: what makes video look professional
- **One message.** Write it as one sentence before anything else. Cut every shot that doesn't serve it.
- **Hook:** pattern interrupt in the first frame (motion, contrast, question, surprising number that's true).
- **Shot rhythm:** vary shot lengths (2 s, 2 s, 4 s); faster during excitement, slower for comprehension; hold text long enough (0.5 s + 0.3 s/word).
- **Cuts:** cut on action or on the beat; match cuts (shape/motion continuity) for elegance; avoid gratuitous transitions (no star wipes); one transition family per video.
- **Composition:** rule of thirds or strong center; leading lines; safe margins for platform UI (vertical videos: keep text out of the bottom ~20 % and top ~12 %).
- **Typography in video:** big (≥ 5 % of frame height for key lines), high contrast, few words per card, consistent type system from DESIGN.md.
- **Color:** a grade that matches the brand direction; consistent across shots.
- **Camera in motion graphics:** slow pushes, parallax between layers, rack focus via blur; motivated moves only.
- **Sound:** designed with the picture (music bed + SFX + VO), silence before key moments, sonic logo on the end card (`../audio/sound-design.md` §6).
- **UI footage:** high resolution capture (2× scale), clean data (realistic, not "John Doe"), cursor smoothed and slowed, zoom to the detail that matters, hide personal/real data.
- **End card:** name, promise, CTA/URL, maybe QR for event screens.

## 5. Storyboard and animatic
- Storyboard: one frame per shot with duration, composition sketch/description, motion, transition out, sound (`templates/VIDEO.md` §4). Frames can be quick HTML/SVG mockups.
- Animatic: frames on a timeline with scratch VO and music to lock timing; review for clarity with sound off and on.
- Only after the animatic is approved: build high-fidelity scenes.

## 6. Video directions
See `../creative/directions-library.md` §6 (Kinetic Manifesto, Screen Story, Paper World, Isometric Explainer, Product Orbit, Documentary Micro, Whiteboard Live, Data Story, Trailer Cut, Lo-fi Phone). Pick one; keep its visual and sound grammar consistent for the whole piece.

## 7. Never
Invented footage or features · fake testimonials · stock clichés (people pointing at screens, handshakes) without a concept · 5-second logo intros · unlicensed music · tiny unreadable UI · captions missing · flashing > 3/s.

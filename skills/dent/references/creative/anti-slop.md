# Anti-Slop Detector (reason-based)

"Slop" is output that is technically fine and instantly forgettable: the average of every template. This detector finds **unjustified** patterns. A pattern is not banned; it must earn its place. For each hit, answer: *what job does this do here, for this product?* If you can't, replace it.

Used by gate G9 (SKILL.md §3), `/dent:review`, `/dent:polish`, `/dent:score`.

---

## 1. How to run it
1. Screenshot the result (desktop + phone). Read the copy.
2. Go through §2–§6. For each hit write: **pattern → why it hurts here → impact → replacement (if justified)**.
3. Three or more unjustified hits = the design is generic; go back to `../creative-direction.md` and `directions-library.md` before polishing details.

## 2. Visual slop
| Pattern | Why it's usually slop | Earns its place when… | Replace with |
|---|---|---|---|
| Violet/indigo→blue gradient brand | Default of a generation of templates | The brand truly owns it and uses it once | A palette from a direction; tinted neutrals + one signal color |
| Glowing orb / mesh blob behind headline | Decoration standing in for an idea | It's data-driven or part of a real concept (e.g. Aurora reacting to time) | Hero typography move, real product, concept imagery |
| Gradient text on every heading | Lowers contrast, says nothing | One display word, contrast verified | Weight/scale/italic contrast |
| Glass on everything | Expensive, low contrast, muddy | Few layers over rich content, tints for text | Solid surfaces with hairlines |
| Same radius + soft shadow + border on everything | No hierarchy of depth | — | Radius hierarchy; border OR shadow; elevation only for real layers |
| Pill-shaped everything | Visual monotony | It's the style's signature (Playful) | Mixed shapes per role |
| Floating random shapes/emoji/3D blobs | Fills space without meaning | They illustrate the concept | Empty space with purpose, or concept illustration |
| Fake dashboard tilted in 3D | Says "SaaS" not "this product" | It's the real UI, legible | Cropped real UI at readable size, annotated |
| Grey "Trusted by" logo row | Usually invented | Real customers with permission | Remove, or a real quote/metric the user supplied |
| ✨ sparkle icon for AI | Universal cliché | — | Describe the actual capability with a specific icon or none |
| Dark mode + neon by default | Category reflex | Product is used at night/creative/dev and brand fits | Choose mode from context of use |
| Espresso + orange for coffee, navy + mint for fintech, pastel teal for health | Category cliché | User asked for the expected look | Diverge on ≥ 2 axes (directions-library §1) |

## 3. Layout slop
- **Centered everything:** long centered text, no tension. → Left-aligned reading, asymmetric grid, one centered moment.
- **Three equal feature cards with icon + title + 2 lines** as the default section. → Varied sizes by importance, real product moments, numbered steps, comparison, a single strong demo.
- **Identical section rhythm** (eyebrow pill → centered H2 → paragraph → cards) repeated 6×. → Vary composition per section's job (statement, demo, proof, comparison, FAQ).
- **Eyebrow pill on every section** ("✦ FEATURES"). → Section numbers, kickers in small caps, or nothing.
- **Bento grid filled with fake UI fragments.** → Bento only with real content of different sizes.
- **Equal-size everything** (12 equal dashboard cards). → Hierarchy: a hero tile, then supporting.
- **Huge empty sections with tiny content.** → Spacing scale; section padding ~2–3× component spacing.

## 4. Copy slop
- Phrases: "Unlock the power of", "Supercharge", "Seamless", "Effortless", "Revolutionize", "Next-gen", "All-in-one", "Built for the future of", "Take your X to the next level", "Elevate", "Empower", "Game-changer", "In today's fast-paced world".
- **Invented proof:** user counts, ratings, uptime %, "loved by 10,000+", fake testimonials with stock names. This is a non-negotiable violation (SKILL.md §3), not just slop.
- **Real people as placeholders** (famous names in form placeholders or testimonials).
- **Vague benefits** with no mechanism ("Work smarter"). → Say what the product does and the concrete outcome.
- **Typos and doubled words** ("Target Target"). → Gate G7.
- **Three CTAs with different labels** for the same action. → One label, used consistently.

## 5. Motion slop
- **Under-animation:** one fade-in for the whole page, dead hovers, instant state changes. Feels static and unfinished. → Ask which motion kinds the user wants and meet the floor (`../motion/motion-menu.md`).
- Every section fades up on scroll. → Animate the hero, one storytelling moment, and state changes; let the rest be still.
- Bouncy springs on frequent actions. → Critically damped UI springs; bounce only for celebration.
- Random particles/gradients drifting forever. → Motion with a concept, or none; pause after one loop.
- Parallax on everything. → One depth moment; respect reduced motion.
- Cursor followers and magnetic buttons in apps. → Creative sites only, never in forms or tools.
- Loading screens that exist to show an animation. → Content first.

## 6. Sound and video slop
- A click sound on every button. → Sound only for meaningful, infrequent events.
- Stock "corporate ukulele/whistle" or generic upbeat royalty-free loop. → A music bed that fits the concept, or silence + sound design.
- Whoosh on every cut; riser before every title. → Sound design follows the edit's rhythm and emphasis; silence before the key moment.
- Robotic default TTS voice without pronunciation fixes. → Choose a voice deliberately, fix pronunciations, pace at ~140–160 wpm, add breaths/pauses.
- Video that opens with a logo animation for 5 seconds. → Hook in the first 2 seconds; logo at the end or small.
- Stock footage of people pointing at screens. → Real product, real use, or illustration with a concept.

## 7. Report format
| # | Pattern | Why it hurts here | Impact | Replacement |
|---|---|---|---|---|
| 1 | Centered H2 + 3 icon cards in 4 sections | Every section looks the same; nothing reads as primary | Users skim past features | Make "How it works" a numbered horizontal sequence; make Features a 2+1 asymmetric layout with one real demo |

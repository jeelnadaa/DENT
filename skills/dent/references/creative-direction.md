# Creative Direction — From Brief to a Design That Isn't Generic

Correct is not enough. Most AI-made and template-made designs fail the same way: they are **correct and forgettable**. This file is the process for making a design that has a point of view, without breaking any [Rule].

Use at **Standard** depth for the concept sentence and signature element, **Polished** for the full process, **All-out** for multiple directions.

---

## 1. Start with a concept sentence

Before choosing a single color, write one sentence that describes the *experience*, using a metaphor from outside software:

- "A calm Japanese stationery shop." (note-taking app)
- "Mission control for marketers." (analytics)
- "A well-lit workshop: tools on the wall, everything in reach." (developer tool)
- "A trusted neighborhood pharmacist." (health app)
- "A late-night record store." (music community)

Rules:
- Concrete nouns beat adjectives. "Clean and modern" is not a concept; everyone is clean and modern.
- The concept must justify choices: if you can't explain a color, font or motion choice through it, change the choice or the concept.
- Put the concept sentence at the top of the Decision Log and DESIGN.md §1.

## 2. Mood words and anti-words
Pick **3 mood words** and **2 anti-words** (what it must not feel like). Anti-words are often more useful:
- Mood: *precise, warm, quiet* · Anti: *corporate, playful*
- Mood: *bold, fast, irreverent* · Anti: *luxurious, cute*

## 3. Explore divergent directions (Polished / All-out)

Make **2–3 directions** that differ on real axes, not three shades of the same idea. Vary at least three of:

| Axis | One end | Other end |
|---|---|---|
| Type | Neutral grotesk | Characterful serif / display |
| Color | Monochrome + one accent | Rich multi-color palette |
| Density | Airy, large type | Dense, information-rich |
| Shape | Sharp, ruled lines | Soft, round, organic |
| Depth | Flat, borders | Layered, shadows, glass |
| Imagery | Product UI screenshots | Photography / illustration |
| Motion | Still, instant | Expressive, choreographed |
| Layout | Strict grid, symmetric | Asymmetric, editorial |

Present each direction as: name + concept sentence + a small visual (palette swatches, a type sample line, one hero or key component rendered) + "best if…" line. Let the user pick or combine **one** base. (This is the "multiple variations" item in the All-out level.)

## 4. The signature element

Every memorable product has **one or two** things that are *theirs*. Choose deliberately; everything else stays quiet.

Sources of a signature:
- **A typographic move:** an unusual display face; oversized numerals; a consistent italic for emphasis; all-caps mono labels.
- **A color move:** an unexpected accent (e.g. vermilion in a world of blue SaaS), a duotone imagery treatment, a signature gradient used in exactly one place.
- **A shape move:** a distinctive corner (cut corners, a notch, a specific radius on a specific element), a recurring graphic device (rules, brackets, a grid pattern).
- **A motion move:** one characteristic transition (how panels open, how success feels).
- **A content move:** a voice that is recognisable (dry, warm, precise); real data in the hero instead of claims.
- **An illustration or imagery system:** one consistent style, not stock.

Test: cover the logo. Could someone still tell which product this is? If not, the signature isn't strong enough.

## 5. Composition — making a screen feel designed

- **One focal point** per screen/section. Decide it first; make it the largest/highest-contrast thing; make everything else support it.
- **Scale contrast:** a strong ratio between the biggest and smallest text (display can be 4–8× body on marketing pages). Timid scale reads as amateur.
- **Visual weight balance:** large, dark, saturated and detailed things are heavy; balance a heavy element with space or several lighter ones — not with symmetry by default.
- **Rhythm with variation:** repeat a layout module, then break it once on purpose (a full-bleed image after three text sections).
- **Grid, then break it:** lock to the column grid; let one element (image, headline, number) bleed or overlap to create tension.
- **Cropping:** crop images and product screenshots boldly (show the interesting part big) instead of shrinking the whole thing.
- **Negative space as an element:** a large empty area next to a strong element is a choice, not leftover.
- **Reading paths:** F-pattern for text-heavy pages (put key words at the start of lines and headings), Z-pattern for sparse marketing sections (logo → nav → headline → CTA).
- **Alignment count:** fewer alignment lines = calmer. Count the distinct left edges on a screen; reduce them.
- **Density matches the user:** experts want more on screen (compact tables, smaller type, shortcuts); first-time and occasional users want fewer, bigger things.

## 6. The current "default look" — avoid unless chosen on purpose

These are the patterns that, in 2025–2026, instantly read as *unedited template or AI output*. They are not forbidden — but if you use one, it must be a decision written in the Decision Log, not an accident.

- Unmodified component-library defaults: zinc/slate neutrals, 6–8px radius everywhere, Inter, the stock focus ring and shadows.
- Indigo/violet-to-blue gradient as the brand, especially on gradient text in the hero.
- A glowing blurred orb or mesh behind the hero headline.
- "✨" sparkle icon for every AI feature.
- Hero: centered pill badge ("New: v2 is here →") + two-line centered headline + two buttons + a fake dashboard screenshot tilted in 3D.
- Grey logo row "Trusted by" with made-up or generic logos.
- Three (or six) equal feature cards with a line icon, bold title and two lines of text.
- Bento grid filled with fake UI fragments that don't show the real product.
- Pricing with three tiers, the middle one "Most popular" with a gradient border — by reflex.
- Testimonial carousel of avatars with five stars and generic praise.
- Emoji in headings, dark mode with pure #000 and neon accents for no reason.
- Copy: "Supercharge", "Unlock", "Seamless", "Effortless", "All-in-one", "Built for the future of…".

Alternatives: real product screenshots cropped to the key moment; a specific headline that states the outcome; one concrete number; a distinctive type pairing; a palette from `color.md` Part 2 or the chosen style; a layout that follows the content, not the template.

## 7. Type-led design (cheapest path to identity)
- A distinctive display face + a workhorse text face gives identity with zero illustration budget.
- Set the hero at a size that feels slightly too big, with tight tracking; let it carry the page.
- Use numbers as graphics (big tabular figures for stats, step numbers, prices).
- Mono or small caps labels for metadata create a "system" feel (works for tools, dev, editorial).
- See `typography.md` §3 for pairings; check licenses before shipping (OFL/Google Fonts are free for commercial use).

## 8. Color strategies beyond 60-30-10
- **Monochrome + one signal color:** neutral world; the accent only means "act here" or "important". Strong for tools.
- **Tinted neutrals:** greys tinted toward the brand hue (warm or cool) instead of pure grey — instantly less generic.
- **Dark brand surface:** a deep brand color (not black) as the dark background.
- **Duotone imagery:** map photos to two brand colors for a consistent look across mixed sources.
- **Color by category, consistently:** each product area/content type has one hue — only when users benefit from distinguishing them.
- **Brand color ≠ action color** when the brand color fails contrast or carries a semantic meaning (red brand + red errors): pick a separate accessible action color.
All still subject to the [Rule] contrast requirements.

## 9. Use references without copying
- Extract *principles* (spacing rhythm, type scale, how images are cropped), never layouts, illustrations, copy or logos (see `inspiration-and-reference-sites.md` §3).
- Mix references from **outside** the category (a bank inspired by a museum website, not by other banks).
- Never reproduce a specific existing product's look 1:1, even when asked "make it exactly like X"; offer "inspired by X's clarity and density" instead and explain why (legal risk, no differentiation).

## 10. Presenting design work
- Lead with the concept sentence and the problem it solves; then the design; then the Decision Log.
- Show the design in context (realistic content, device frames only if they help).
- Explain 3–5 key decisions in plain words tied to the user's goal; don't list every token.
- Ask for feedback on specific things ("Is the tone of the headline right? Is the dashboard density right for your users?") rather than "Thoughts?".

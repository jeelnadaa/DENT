# Quality Review — Verification, Rubric and Anti-Patterns

Run after the SKILL.md pre-ship checklist. Part 1 makes sure what was **built** matches the design (look at it). Part 2 judges whether the design is **clear, distinctive and convincing**, and catches the patterns that make designs look generic or "AI-made".

# Part 1 — Visual verification (check what you built)

Code that "should" look right often doesn't. Before showing a built design to the user, **look at it** and compare it with the design spec. This loop catches most visual bugs (overflow, misalignment, wrong colors, broken states, bad wrapping).

---

## 1. The loop

1. **Render** the page/screen (open in a browser, simulator, or render to an image).
2. **Capture screenshots** at key sizes (below).
3. **Inspect** each screenshot against DESIGN.md / the Decision Log and the checks in §3.
4. **List issues** concretely ("Card titles wrap to 3 lines at 375px; CTA is below the fold on mobile").
5. **Fix** the smallest thing that resolves each issue.
6. **Re-render and re-check** until no issues remain (max ~3–4 rounds; then report remaining issues honestly).

If no rendering tool is available, say so and do a careful code review against the checklist instead — never claim it was visually verified when it wasn't.

## 2. How to render (pick what the environment has)
- **Browser automation** (Playwright/Puppeteer): open the file/URL, set viewport, `page.screenshot({fullPage:true})`. Emulate `prefers-color-scheme: dark` and `prefers-reduced-motion: reduce` for those checks.
- **Connected browser tools** (if available in the session): navigate, resize, screenshot.
- **Headless Chrome CLI:** `chrome --headless --screenshot --window-size=375,812 file.html`.
- **Native:** iOS Simulator / Android Emulator screenshots; Flutter golden tests.
- Then view the image (the agent can read images) and inspect it.

Example (Playwright, Python):
```python
from playwright.sync_api import sync_playwright
sizes=[(375,812),(768,1024),(1440,900)]
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page()
    for w,h in sizes:
        pg.set_viewport_size({"width":w,"height":h})
        pg.goto("file:///path/index.html"); pg.wait_for_timeout(500)
        pg.screenshot(path=f"shot-{w}.png",full_page=True)
    pg.emulate_media(color_scheme="dark"); pg.screenshot(path="shot-dark.png",full_page=True)
    b.close()
```

## 3. What to check in each screenshot

**Sizes:** 320/375 (mobile), 768 (tablet), 1024–1280 (laptop), 1440+ (desktop). Plus dark mode and 200% zoom if in scope.

**Layout**
- [ ] Nothing overflows horizontally; no cut-off text or buttons.
- [ ] Alignment: edges line up to the grid; no 1–3px misalignments between neighbors.
- [ ] Spacing matches the scale; groups are visibly grouped (proximity).
- [ ] Line length of body text within ~45–75 characters.
- [ ] Headings don't leave single orphan words (balanced wrapping).

**Hierarchy**
- [ ] Exactly one primary action per section (squint, 5-second and grayscale tests: Part 2 §1).

**Consistency**
- [ ] Same component types look identical everywhere (heights, radii, fonts, colors).
- [ ] Icons from one set, same size/stroke.

**Color & contrast**
- [ ] Colors match tokens; no stray default blue links or browser default styles.
- [ ] Text readable on every background, including text over images/gradients/glass.

**States** (trigger them — hover, focus via Tab, disabled, error, loading, empty)
- [ ] Focus ring visible on every interactive element.
- [ ] Error and empty states render correctly.

**Content stress**
- [ ] Long names, long translations, missing images, 0/1/many items handled.

**Motion** (if any)
- [ ] Animations feel smooth, not too slow; nothing jumps on load (layout shift).
- [ ] With reduced motion: content fully visible, no essential info lost.

## 4. Automated checks (when available)
- **Accessibility:** axe-core (e.g. `@axe-core/playwright`), Lighthouse accessibility audit.
- **Performance:** Lighthouse (LCP, CLS, INP/TBT).
- **Contrast:** compute ratios for every text/background token pair (script below).
```python
def lum(h):
    h=h.lstrip('#'); c=[int(h[i:i+2],16)/255 for i in (0,2,4)]
    c=[x/12.92 if x<=0.03928 else ((x+0.055)/1.055)**2.4 for x in c]
    return .2126*c[0]+.7152*c[1]+.0722*c[2]
def ratio(a,b):
    l1,l2=sorted([lum(a),lum(b)],reverse=True); return (l1+.05)/(l2+.05)
```
- **Visual regression** (for ongoing projects): Playwright screenshot comparisons, Chromatic/Storybook.

## 5. Reporting
When presenting, include a short line: "Checked at 375 / 768 / 1440px, light + dark, keyboard focus and empty state — fixed 3 issues (…)." Mention anything not verifiable.

---

# Part 2 — Design review

---

## 1. Review tests (in addition to the Part 1 screenshot checks)

1. **5-second test** — look for 5 seconds, then look away. Can you say what it is, who it's for and what to do next? If not, hierarchy or copy is failing.
2. **Squint / blur test** — the most important element and the primary action stay the most visible blobs; groups visible from spacing alone.
3. **Grayscale test** — remove color; hierarchy must still work (size, weight, spacing, position).
4. **Realistic user task** — do the main task start to finish as a first-time user. Count clicks, hesitations and dead ends.
5. **Brief & style check** — does it serve the product goal, and are the chosen style's signature moves present?
(Sizes, keyboard, zoom, dark mode, reduced motion and content-stress checks are in Part 1 §3.)

---

## 2. Scoring rubric (score each 1–5)

| # | Criterion | 1 = poor | 5 = excellent |
|---|---|---|---|
| 1 | **Clarity of purpose** | Unclear what the screen is for | Purpose and next step obvious in 5s |
| 2 | **Visual hierarchy** | Everything competes | One clear focal point, clear reading order |
| 3 | **Layout & alignment** | Arbitrary placement | Everything on a grid, consistent alignment |
| 4 | **Spacing rhythm** | Random gaps | Spacing scale used; groups clear (proximity) |
| 5 | **Typography** | Many sizes/weights, poor readability | Few deliberate styles, strong scale contrast, comfortable reading |
| 6 | **Color** | Random or muddy, poor contrast | Intentional palette, accent used with purpose, AA contrast |
| 7 | **Consistency** | Same element looks different in places | Components match their specs everywhere |
| 8 | **Interaction & feedback** | Missing states, silent actions | All states designed, instant feedback |
| 9 | **Accessibility** | Fails rules | Meets all [Rule]s |
| 10 | **Content & copy** | Generic, jargon, lorem ipsum | Specific, user's language, helpful |
| 11 | **Distinctiveness** | Could be any template | Memorable, matches brand and chosen style |
| 12 | **Craft & polish** | Rough details | Optical alignment, consistent icons, refined details |

**Ship bar:** no score below 3, criteria 1, 2, 7 and 9 at 4+.

When giving feedback, write: **what** the issue is → **why** it matters (cite the law/rule) → **how** to fix it. Example: "The 'Export' and 'Delete' buttons have the same filled style (Von Restorff: nothing stands out; destructive action is too easy). Make Export the primary filled button, Delete a red text button in the overflow menu with confirmation."

---

## 3. Anti-patterns: what makes designs look generic / AI-made

Each item: **the pattern → why it hurts → what to do instead.**

### Visual identity
1. **Default purple-to-blue gradient everywhere** (hero, buttons, text) → signals "template", no brand → pick a palette deliberately (see color.md Part 2 or the style file); use gradients only where the style calls for them.
2. **One default font for everything, all at medium weight** → no hierarchy, no character → choose a display/body pairing or one family with strong weight and size contrast (`modern-layer.md` §7.1).
3. **Everything centered** → long centered text is hard to read; no tension or structure → left-align body text and most layouts; center only short hero content.
4. **Every element has the same big radius + soft shadow + border** → visual mush, no layers → choose border OR shadow, a radius hierarchy (controls < containers), and reserve elevation for things that are actually above others.
5. **Glass, glow and gradient text all at once** → noisy, cheap → pick one style and its signature moves (styles index).
6. **Random accent colors** (each card a different color for no reason) → color loses meaning → color = meaning (primary action, status, category).
7. **Low-contrast grey text for "elegance"** → unreadable, fails WCAG → text ≥ 4.5:1; create elegance with spacing and type instead.

### Layout
8. **The "three feature cards with icons" row** used for everything → says nothing, everyone does it → show real product screenshots, benefits with proof, bento with varied sizes, or alternating image/text rows.
9. **Equal-size everything** (12 equal dashboard cards, uniform grid) → no hierarchy → vary size by importance (Von Restorff, bento hero tile).
10. **Same spacing everywhere** → groups aren't visible → small gaps inside groups, large gaps between groups (proximity).
11. **Cramped content, no breathing room** or the opposite **huge empty sections with tiny content** → both feel unfinished → follow the spacing scale; section spacing ~2–3× component spacing.
12. **Too many CTAs** ("Get Started", "Try Free", "Book Demo", "Learn More" all filled) → decision paralysis (Hick's Law) → one primary action per section, same label across the page.

### Content
13. **Generic copy** ("Unlock the power of…", "Revolutionize your workflow", "Seamless", "Next-gen", "All-in-one solution") → meaningless → say what it does and the concrete outcome, with numbers if possible.
14. **Lorem ipsum / fake-looking data** (John Doe, $1,234.56 everywhere, 100% everywhere) → design isn't tested against reality → realistic, varied, edge-case content.
15. **Fake testimonials / generic avatars** → kills trust → real quotes with names/roles, or omit.
16. **Emoji as icons** in professional products → inconsistent rendering, looks unfinished → one consistent icon set.
17. **Headings with an icon on every single one** → visual noise → icons only where they aid recognition.

### Components & interaction
18. **Missing states** (no hover/focus/disabled/loading/empty/error) → feels broken in use → define all states (`foundations-and-components.md` §4).
19. **Mixed icon sets / stroke weights** → subtle but obvious sloppiness → one family, one stroke, one size scale.
20. **Inconsistent radii, button heights, input styles** across screens → not designed as a system → use component specs.
21. **Placeholder used as label** → disappears when typing, low contrast → persistent labels.
22. **Animation on everything** (every section fades in, every card bounces) → slow and distracting → motion only with purpose (`modern-layer.md` §7.0).
23. **Hamburger menu on desktop** with plenty of space → hides navigation → visible nav.
24. **Modal on page load** (newsletter, cookie wall) → blocks the user's goal → inline or compact, delayed until engagement.

---

## 4. What makes a design look *designed* (do these)

1. **A clear concept.** One sentence that describes the look and feel ("calm Japanese stationery", "mission control for marketers"). Every choice serves it.
2. **Real content first.** Design with actual copy, data and imagery; content shapes layout.
3. **Strong typographic hierarchy.** Big contrast between heading and body; few styles; tight tracking on large type; balanced headlines.
4. **Deliberate color.** Mostly neutrals, one accent with a job; or a bold palette applied with clear rules.
5. **Rhythm.** Consistent spacing scale; repeated layouts with intentional variation.
6. **One memorable element.** A distinctive hero, illustration style, interaction or typographic moment — just one or two.
7. **Purposeful asymmetry.** Off-center layouts locked to a grid feel dynamic and intentional.
8. **Real imagery.** Product screenshots, art-directed photos or a consistent illustration style — not random stock.
9. **Consistent details.** Same radii, same icon stroke, same shadow recipe, same motion curves.
10. **Optical polish** (below).

### Optical adjustments (what pros fix by eye)
- **Play icons and triangles** look off-center when mathematically centered — nudge right ~5–10% of their width.
- **Round shapes** look smaller than squares of the same size — make circles/icons with round shapes slightly larger (overshoot), like fonts do.
- **Icon + text alignment:** center icons to the text's x-height/cap height, not the line box.
- **Text in buttons** often looks low when mathematically centered (because of descender space) — check visually, adjust padding by 1px if needed.
- **Hanging punctuation:** quotes and bullets can hang outside the text edge so the text aligns cleanly (`hanging-punctuation` where supported).
- **Large headings** need tighter letter-spacing and line-height than the defaults.
- **Nested radii:** inner = outer − padding.
- **Thin lines on dark backgrounds** look thicker/brighter than on light ones; reduce opacity in dark mode.
- **Pure black (#000) on pure white** can feel harsh in large areas; slightly soften for long reading.

---

## 5. Quick self-critique prompts

Ask these before presenting:
- What is the **one** thing I want the user to notice first? Is it the most visible thing?
- If I removed 30% of the elements, would the screen be worse? If not, remove them.
- Could this screen belong to any other product? What makes it **ours**?
- Would a first-time user know what to do without reading instructions?
- Does every color, animation and decoration have a job?
- Did I design the empty, loading, error and long-content versions?
- Does it pass every [Rule] in SKILL.md?

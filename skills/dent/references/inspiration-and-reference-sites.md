# Inspiration Sources and Reference-Site Workflow

Two uses:
1. **The agent looks for inspiration** (when unsure how something should look, or at higher effort levels).
2. **The user gives a reference** ("make it look like this site/screenshot") → the agent extracts the look and rebuilds it **through this skill's rules**, so every later change can still come from the skill.

Links can change or go down; if one fails, try another in the same row. Inspiration ≠ copying (see §3).

---

## 1. Where to look (by need)

### Component libraries & design systems (how components should look and behave)
| Source | Best for |
|---|---|
| component.gallery | Same component compared across ~100 design systems — check names, variants and behavior |
| ui.shadcn.com | Clean modern React components (Radix + Tailwind) |
| radix-ui.com · react-spectrum.adobe.com/react-aria · headlessui.com | Accessible behavior for complex widgets |
| m3.material.io | Material 3 components, motion, color system |
| developer.apple.com/design/human-interface-guidelines | iOS/macOS/visionOS patterns |
| fluent2.microsoft.design | Windows/Microsoft components |
| carbondesignsystem.com (IBM) · atlassian.design · polaris.shopify.com · primer.style (GitHub) | Mature enterprise/product systems, data-dense UI |
| design-system.service.gov.uk · designsystem.digital.gov (USWDS) | Accessible public-service forms and patterns |
| ant.design · mantine.dev · heroui.com · chakra-ui.com | Broad component sets |
| tailwindcss.com/plus (Tailwind UI) · flowbite.com · daisyui.com | Ready Tailwind sections and components |
| ui.aceternity.com · magicui.design | Animated/modern landing components (use with restraint) |
| uiverse.io | Community CSS buttons, inputs, loaders, toggles |
| w3.org/WAI/ARIA/apg | Official accessible patterns (keyboard + ARIA) |
| inclusive-components.design | Accessible component write-ups |

### Real product screens & flows (how real apps solve it)
| Source | Best for |
|---|---|
| mobbin.com | Huge library of real iOS/Android/web app screens and flows (search by screen type: onboarding, paywall, settings…) |
| pageflows.com | Recorded user flows (onboarding, checkout, upgrade) |
| refero.design | Web app screens searchable by pattern |
| screensdesign.com | Mobile app screens & flows |
| saasinterface.com | SaaS app UI pages |
| collectui.com | Daily UI shots grouped by component |

### Websites & landing pages
| Source | Best for |
|---|---|
| awwwards.com | Award-winning, experimental, motion-heavy sites |
| godly.website | Modern, high-craft web design (with motion previews) |
| land-book.com · lapa.ninja · landingfolio.com | Landing pages by category/industry |
| saaslandingpage.com | SaaS landing pages by section (hero, pricing, features) |
| onepagelove.com | One-page sites |
| minimal.gallery | Minimal design |
| siteinspire.com · httpster.net | Curated general web design |
| darkmodedesign.com | Dark-mode sites |
| brutalistwebsites.com | Brutalist / raw sites |
| webflow.com/made-in-webflow · framer.com/marketplace | Templates and community sites |
| ecomm.design | E-commerce sites |
| bestfolios.com | Portfolios |
| dribbble.com · behance.net | Concepts and visual ideas (often not real/shippable — check usability) |

### Typography
fonts.google.com · fontshare.com (free quality fonts) · typewolf.com (pairings, what's trending, site examples) · fontsinuse.com (real-world usage) · typescale.com (type scale calculator) · fontpair.co (pairings)

### Color
realtimecolors.com (preview palette on a real layout) · coolors.co · huemint.com · color.adobe.com · uicolors.app (Tailwind-style scales) · radix-ui.com/colors · oklch.com · webaim.org/resources/contrastchecker

### Icons & illustration
lucide.dev · phosphoricons.com · heroicons.com · tabler.io/icons · fonts.google.com/icons (Material Symbols) · iconoir.com · undraw.co · storyset.com · openpeeps.com · blush.design

### Motion & interaction
codrops (tympanus.net/codrops) — creative effects tutorials · codepen.io · lottiefiles.com · rive.app community · easings.net · cubic-bezier.com · motion.dev (Motion docs/examples) · animista.net · hoverstat.es

### Data visualization
datavizproject.com · Financial Times "Visual Vocabulary" (chart chooser) · datawrapper.de/blog · observablehq.com · flowingdata.com

### Email
reallygoodemails.com

### UX research & rules (to justify decisions)
nngroup.com (Nielsen Norman Group) · baymard.com (e-commerce UX research) · lawsofux.com · deceptive.design · a11yproject.com · webaim.org

### Images & 3D
unsplash.com · pexels.com · spline.design (3D community)

---

## 2. When the user gives a reference (URL or screenshot)

### Step 1 — Ask what to take (one question, explained options)
> **What do you like about this reference?**
> 1. **The overall look (Recommended)** — colors, fonts, shapes and feel; your own layout and content.
> 2. **The layout/structure** — how sections are arranged; your own colors and style.
> 3. **Both look and layout** — close in spirit, but with your brand, content and our design rules.
> 4. **A specific part** — e.g. just the buttons, the hero, the pricing table, the animations.

### Step 2 — Extract (look, don't copy)
If browser tools are available: open the page, screenshot at desktop and mobile widths, and read computed styles. Otherwise analyze the screenshot the user gave.
Extract into a **Reference Profile**:
- **Colors:** background, surfaces, text levels, accent(s), borders → map to Dominant / Complement / Off + semantic tokens.
- **Typography:** font families (computed `font-family`), size scale, weights, line heights, letter-spacing, case.
- **Spacing:** base unit and rhythm (section gaps, card padding).
- **Shape:** radii, border widths, shadow recipes.
- **Layout:** grid, max width, section patterns (hero type, bento, alternating rows…).
- **Components:** button/input/card/nav looks and states.
- **Motion:** what animates (hover, scroll reveals, transitions), durations and feel.
- **Imagery & icons:** style, treatment.
- **Nearest skill style(s):** e.g. "Dark Tech + Bento" — open that style file to fill gaps.

Example extraction script (run in the page via browser tools):
```js
(() => {
  const pick = s => { const el=document.querySelector(s); if(!el) return null; const c=getComputedStyle(el);
    return {font:c.fontFamily,size:c.fontSize,weight:c.fontWeight,lh:c.lineHeight,ls:c.letterSpacing,color:c.color,bg:c.backgroundColor,radius:c.borderRadius,shadow:c.boxShadow,padding:c.padding}; };
  return { body:pick('body'), h1:pick('h1'), h2:pick('h2'), p:pick('p'), button:pick('button, a[class*="btn"], [class*="button"]'), input:pick('input'), card:pick('[class*="card"]'), nav:pick('nav') };
})()
```

### Step 3 — Show the profile and confirm
Show a compact summary (swatches + fonts + 3–5 key traits) and ask: "Keep all of this, or change anything?" Note any problems found (e.g. "their grey text fails contrast — I'll darken it slightly").

### Step 4 — Rebuild through the skill
- Turn the profile into **tokens** and component specs (`foundations-and-components.md` §3–4).
- Apply all **[Rule]s** (fix contrast, target sizes, focus states — even if the reference doesn't).
- Apply the matching **style file** for anything the reference doesn't show (e.g. error states).
- Record in the Decision Log: "Source: reference site X (look) — adapted: contrast, focus, sizes".
- Continue the normal workflow (draft → changes → approval → DESIGN.md). Later changes use the skill as usual.

---

## 3. Inspiration vs copying (rules)
- **Never copy:** logos, brand names, trademarks, proprietary illustrations/photos/icons, exact marketing copy, or a page so close it could be mistaken for the original (that's impersonation).
- **Fonts:** commercial fonts need a license; if a reference uses one, suggest the closest free alternative (e.g. Inter/Geist for neo-grotesques, Fraunces/Playfair for display serifs) unless the user owns the license.
- **OK to take:** general style direction, layout patterns (which are common conventions), color mood, spacing rhythm, motion feel, component behavior.
- Combine ideas from several references and the user's brand so the result is original.

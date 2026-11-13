# DENT Benchmark Prompt (v1)

Copy everything inside the box **exactly**, with no edits, into a **fresh session**. Use the same agent and model for both runs: once **without DENT** installed and once **with DENT** installed.

The prompt never mentions DENT on purpose. The only thing that changes between runs is whether the skill is available.

---

```text
Build a complete, production-quality marketing website for "Brewlog", a fictional app
for home coffee brewers. Brewlog lets people log brew recipes (beans, grind size, water
temperature, ratio, time), rate each cup, and see which settings make their best coffee
over time. It has a free plan and a paid "Pro" plan ($6/month or $60/year) that adds
unlimited recipes, bean inventory tracking and brew analytics.

Requirements:
- One self-contained file named index.html (HTML, CSS and JavaScript inline). Web fonts
  from Google Fonts are allowed. No other external files, frameworks or images: build any
  visuals (product screenshots, illustrations, icons) with HTML, CSS or inline SVG.
- Sections: a header with navigation, hero, how it works, key features, a preview of the
  app's interface, pricing (Free vs Pro, monthly/yearly), FAQ, a sign-up form, and a footer.
- The sign-up form asks for name, email and password, validates in the browser and shows
  helpful errors and a success state. It does not need a backend.
- It must look great and work well on phones, tablets and desktops.

Make every decision yourself and don't ask me any questions. When you are done, reply with
a short summary of the design decisions you made.
```

---

## Why this prompt

It is realistic (a typical "build me a landing page" request) and short enough to paste anywhere. It also exercises most of what a design skill should get right:

| Prompt asks for | What it reveals |
|---|---|
| A fictional product with a clear audience | Whether the design has a concept and identity, or a generic template look |
| Visuals built in code, no stock images | Imagery direction, product-preview craft, icon consistency |
| Many sections | Hierarchy, rhythm, one primary action per section, consistency |
| Pricing with a monthly/yearly toggle | Honest pricing patterns, component states, interaction |
| Sign-up form with validation | Labels, error and success states, accessibility |
| Phones to desktops | Responsive layout, touch targets, typography scaling |
| "Don't ask me any questions" | A fair one-shot comparison; DENT uses its documented defaults |
| "Summary of decisions" | Whether design choices are reasoned or arbitrary |

Changing the prompt makes results incomparable. If it ever changes, it gets a new version number (v2), and results record which version they used.

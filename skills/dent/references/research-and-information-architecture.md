# UX Research and Information Architecture

Good visuals can't fix the wrong structure. Use this for higher effort levels, new products, or when users "can't find things".

---

## Part A — Understanding users

### 1. Lightweight research the agent can do with the user
- **Ask** (via discovery questions): who uses it, their main goals, frequency, context (device, place, time pressure), skill level, top frustrations with current solutions.
- **Competitive analysis:** review 3–5 competitors/alternatives: what they do well, gaps, conventions users expect (Jakob's Law).
- **Assumptions list:** write assumptions explicitly and mark which are risky; validate the risky ones first.

### 2. Personas (lean / proto-personas)
One short card per key user type (2–4 max):
- Name & role, context, **goals** (what they want to achieve), **pain points**, behaviors/skills, devices, quote.
- Base on real research when possible; label proto-personas as assumptions.
- **Jobs To Be Done (JTBD)** framing is often more useful: "When [situation], I want to [motivation], so I can [expected outcome]."

### 3. User journey map
Stages (e.g. Discover → Evaluate → Sign up → First use → Regular use → Renew/Leave), and per stage: user actions, thoughts, emotions (high/low), pain points, opportunities. Use it to choose which screens matter most.

### 4. User flows / task flows
- Map the steps for each key task: entry point → decisions → screens → success/failure.
- Count steps; remove unnecessary ones (Tesler's Law: push complexity to the system).
- Design the **happy path** first, then errors, edge cases and empty states.

### 5. Usability testing
- **5 users** typically uncover most major usability problems in one round (Nielsen); test iteratively (several small rounds > one big round).
- Script: intro (we're testing the design, not you) → background questions → 3–5 realistic tasks ("You want to change your delivery address for tomorrow's order") → think aloud → follow-ups → wrap-up.
- Don't lead ("Click the blue button"); ask "What would you do next?"
- Measure: task success, time, errors, confidence; SUS (System Usability Scale) questionnaire for a standard score.
- Other quick methods: 5-second test, first-click test, preference test (with "why"), A/B tests (for live products with traffic), surveys, analytics/heatmaps, session recordings, interviews.

### 6. Heuristic evaluation
Review the design against Nielsen's 10 heuristics (SKILL.md › Laws), rating each issue's severity: 0 none, 1 cosmetic, 2 minor, 3 major, 4 catastrophic. Fix 3–4 first.

---

## Part B — Information Architecture (IA)

### 7. What IA covers
Organizing, structuring and labeling content so users can find it and understand where they are: **organization schemes, labeling, navigation, search**.

### 8. Organization schemes
- **Exact:** alphabetical, chronological, geographical (good when users know what they want).
- **Ambiguous:** by topic, task, audience, metaphor (needs good labels).
- Most products: **task- or topic-based** top level, matching users' mental models, not the company's org chart.

### 9. Structures
- **Hierarchy (tree):** most common; keep it **broad and shallow** rather than narrow and deep — users find content faster with more options per level than with many clicks (as long as options are well-grouped and labeled; research on menu breadth vs depth favors breadth).
- **Sequential:** step-by-step flows.
- **Hub and spoke:** home hub → tasks → back to hub (mobile apps).
- **Matrix/faceted:** filter by multiple attributes (e-commerce, catalogs).

### 10. Labeling
- Use users' words (from research, search logs, support tickets).
- Be specific and distinct ("Billing" vs "Payments" vs "Invoices" — pick one meaning each).
- Consistent grammatical form (all nouns or all verbs in a menu).
- Avoid clever/branded labels for navigation ("Explore the Universe" → "Products").

### 11. Methods
- **Content inventory/audit:** list every page/feature; decide keep/merge/delete.
- **Card sorting:** users group content cards and name groups — **open** (they create categories) to discover mental models, **closed** (predefined categories) to validate.
- **Tree testing:** users find items in a text-only hierarchy — tests findability without visual design. Target high success and directness.
- **Sitemap:** the final structure diagram; each page with purpose and key content.

### 12. Navigation design
See page-and-flow-patterns.md §13. Wayfinding rules: users always know **where they are** (title, active nav, breadcrumbs), **where they can go** (visible nav), and **how to get back** (back, home, breadcrumbs).

### 13. Deliverables (by effort level)
- Essential/Standard: list of screens + primary user flow.
- Polished: sitemap + key flows + proto-personas.
- All-out: personas/JTBD, journey map, sitemap, flows, IA validation plan (card sort/tree test), usability test script.

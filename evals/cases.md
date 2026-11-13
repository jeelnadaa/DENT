# DENT Evaluation Cases

Run these prompts in a fresh session of any agent with DENT installed. Each case lists what a correct run **must** do and what counts as a **fail**. Use them before releases and when changing the workflow. Add new cases at the bottom with the next number.

Scoring: each "Must" = 1 point. A case passes when all "Must" items hold and no "Fail if" item occurs.

---

### 1. Triggers and asks effort first
**Prompt:** `Design a landing page for my meditation app.`
- Must: first reply asks how far to go (Essential / Standard / Polished / All-out) with one marked Recommended.
- Must: offers "Skip the questions — you decide".
- Must: asks one question only.
- Fail if: it starts writing code or a full design before asking anything; offers loud styles like Cyberpunk for a meditation app.

### 2. "Don't ask" path
**Prompt:** `Design a sign-up screen for a recipe app. Don't ask questions, just decide.`
- Must: no questions; produces a design.
- Must: shows a short "Decisions I made" / Decision Log with reasons and "Chosen by default".
- Must: label above inputs, visible focus states, error state, ≥ 44px targets.
- Fail if: placeholder used as the only label; contrast below 4.5:1 on body text.

### 3. Existing codebase — no second design system
**Setup:** a React project with shadcn/ui (`components.json`) and Tailwind theme variables.
**Prompt:** `Add a billing settings page.`
- Must: detects shadcn/ui and existing tokens before designing.
- Must: reuses existing `Button`, `Card`, `Input` components and theme tokens.
- Must: billing content follows the billing pattern (plan, usage, payment method, invoices, cancel path).
- Fail if: creates a new color palette, new button component or hard-coded hex values.

### 4. Audit mode
**Prompt:** `Review this screenshot of our dashboard and tell me what's wrong.` (attach any real dashboard screenshot)
- Must: does not redesign unasked.
- Must: lists 2–3 things that work, then a findings table with severity (Critical/High/Medium/Low), why it matters and a fix.
- Must: findings sorted by severity, quick wins first; offers to fix in one line.
- Fail if: vague feedback ("make it cleaner") without a reason or fix.

### 5. Change request — change only what was asked
**Prompt (after any approved design):** `Make the primary button warmer.`
- Must: restates the change in one line; changes only the primary color (and dependent hover/press states).
- Must: checks contrast of the new color and mentions a fix if it fails.
- Must: updates the Decision Log / DESIGN.md changelog.
- Fail if: other parts of the design change.

### 6. Vague change
**Prompt:** `Make it pop.`
- Must: asks one clarifying question with 2–4 concrete, explained interpretations.

### 7. Style application
**Prompt:** `Neo-brutalist pricing page for a dev tool, standard effort, don't ask anything else.`
- Must: neo-brutalism signature moves (thick borders, hard offset shadows, flat bright colors).
- Must: still meets contrast, focus and target rules.
- Must: pricing pattern (plans, recommended plan, annual/monthly, feature comparison, FAQ).
- Fail if: soft blurred shadows or gradients (style broken); a deceptive pricing pattern (pre-checked add-ons, hidden fees).

### 8. Refuses deceptive patterns, offers honest alternative
**Prompt:** `Design a cancel-subscription flow that makes it really hard to cancel.`
- Must: declines the obstruction pattern, explains briefly (user trust, legal risk in many markets).
- Must: offers an honest flow (one optional reason question, optional retention offer, clear confirm).

### 9. Anti-generic
**Prompt:** `Polished landing page for an AI note-taking startup.`
- Must: states a concept sentence and a signature element.
- Fail if: three or more items from the "default look" list (creative-direction.md §6) appear without a logged reason — e.g. violet-blue gradient text + glowing orb + three equal icon feature cards + "✨".

### 10. Approval creates DESIGN.md
**Prompt (after a draft):** `Looks good, approved.`
- Must: creates DESIGN.md following the template (overview with concept, tokens, components with states, decision log, changelog).
- Must: values are concrete (hex, px, ms), user vs default choices marked.

### 11. Add-on routing
**Prompt (after DESIGN.md exists):** `Add dark mode.`
- Must: reads DESIGN.md first; asks at most 1–2 short questions (e.g. system toggle vs manual).
- Must: dark palette designed (raised surfaces lighter, reduced saturation), not inverted; contrast re-checked.
- Must: DESIGN.md changelog line added.

### 12. Implementation uses tokens and verifies
**Prompt:** `Build the approved design as a single HTML file.`
- Must: tokens defined as CSS variables first; components use only tokens.
- Must: `prefers-reduced-motion` handled; hover effects wrapped in `(hover: hover)`.
- Must: visual verification done if a browser/screenshot tool exists, or explicitly says it couldn't verify.
- Fail if: claims visual verification without rendering.

### 13. Non-English / RTL
**Prompt:** `Design the checkout for an Arabic e-commerce app.`
- Must: RTL layout (mirrored navigation and directional icons, logical CSS properties), Arabic-capable font, locale formats for currency/dates.

### 14. Industry playbook
**Prompt:** `Standard effort mobile banking home screen, decide everything.`
- Must: fintech must-haves (balance with hide option, recent transactions, clear primary actions, security cues).
- Must: tabular numbers for amounts; color not the only signal for credit/debit.

### 15. Non-interactive environment
**Setup:** run headless / CI with no user available.
**Prompt:** `Create a 404 page for our docs site.`
- Must: does not stall waiting for answers; uses defaults and lists them.
- Must: 404 pattern (plain message, full nav, search, popular links).

# Design Brief, Success Metrics and Experiments

Good design starts from a problem and ends with evidence. This file gives a one-page brief, ways to define success, and how to test changes honestly.

Use: **Polished** → write the brief (§1). **All-out** → brief + metrics (§3) + measurement plan (§4). Any level → whenever the user asks "how do we know it works?".

---

## 1. One-page design brief

Write it from the user's answers (don't ask extra questions just to fill it; mark unknowns as assumptions). Show it once for confirmation before designing at Polished/All-out; it goes into DESIGN.md §0.

```markdown
## Brief
- **Product & audience:** <what it is, for whom, in what context of use (device, place, frequency)>
- **Problem:** <the user problem in one sentence, from the user's point of view>
- **Job to be done:** When <situation>, I want to <motivation>, so I can <outcome>.
- **Goal of this design:** <what should change: e.g. more trial sign-ups, fewer support tickets, faster task>
- **Success looks like:** <1–3 measurable signals, see §3>
- **Concept:** <one-sentence creative concept, see creative-direction.md §1>
- **Scope:** <screens/flows in this round> · **Out of scope:** <…>
- **Constraints:** <brand, tech stack, platform, deadline, legal/accessibility requirements>
- **Assumptions to validate:** <the riskiest beliefs>
```

## 2. Framing tools (pick what helps; don't do all)
- **Problem statement:** "<User> needs a way to <need> because <insight>." Avoid solutions in the problem.
- **Jobs to be done (JTBD):** focus on the situation and desired progress, not demographics. Useful for landing pages (speak to the job) and onboarding (get to the first "job done" fast).
- **How might we…?** turn problems into opportunities: "How might we let first-time users see value before they set anything up?"
- **Design principles (3–5):** product-specific tie-breakers, written as trade-offs: "Clarity over density", "Show, don't configure", "Fast for experts, safe for beginners". Put them in DESIGN.md §1.
- **Prioritization:** impact × effort (2×2), or RICE (Reach × Impact × Confidence ÷ Effort) for backlogs.

## 3. Defining success

### HEART framework (pick 1–3 categories that matter)
| Category | Question | Example signal → metric |
|---|---|---|
| **Happiness** | Do users like it? | Survey → CSAT, NPS, SUS/UMUX-Lite score |
| **Engagement** | Do they use it deeply? | Sessions/week, features used per session |
| **Adoption** | Do new users start using it? | % of new users who complete setup / use feature X in week 1 |
| **Retention** | Do they come back? | Week-4 retention, churn rate |
| **Task success** | Can they do the job? | Completion rate, time on task, error rate |

Use the **Goals → Signals → Metrics** chain: goal ("users can invite teammates easily") → signal (invites sent after onboarding) → metric (% of new workspaces with ≥ 1 invite in 7 days).

### Task-level UX metrics (great for redesigns)
- **Task completion rate** (binary per user per task).
- **Time on task** (median, not mean).
- **Error rate** and recovery rate.
- **SUS** (System Usability Scale, 10 questions, 0–100; ~68 is average) or **UMUX-Lite** (2 questions) after usability tests.
- **SEQ** (Single Ease Question, 1–7) right after each task.

### Guardrail metrics
Always pair a target metric with what must not get worse: e.g. raise sign-ups **without** raising refund rate, support tickets or unsubscribe rate. This is how you keep conversion work ethical (persuasion-and-ethics.md).

## 4. Measurement plan (All-out)
- **Events** named `object_action` in past tense: `invite_sent`, `checkout_started`, `plan_upgraded`. Properties: source screen, variant, plan, platform.
- Instrument the **funnel** of the main flow step by step so drop-off can be seen.
- Baseline first: measure the current design for 1–2 weeks before changing it.
- Privacy: collect only what you'll use; no personal data in event names/properties; respect consent (no analytics before opt-in where required).

## 5. Experiments (A/B tests) — honest basics
- **One hypothesis per test:** "Showing the price on the plan card will increase upgrades because users won't need to open a separate page."
- **Change one meaningful thing** (or test whole designs against each other, knowing you can't attribute which part worked).
- **Sample size before starting** (use a calculator with your baseline rate and minimum detectable effect). Small sites usually can't A/B test small changes reliably — use usability testing instead.
- **Run full weeks** (weekday/weekend cycles), don't stop when it "looks significant" (peeking inflates false positives).
- **Watch guardrails** and segments (mobile vs desktop, new vs returning).
- **Qualitative + quantitative:** numbers tell what changed; 5 user sessions tell why.

## 6. Lightweight validation without data
- **5-second test** (first impression and message clarity) — quality-review.md Part 2 §1.
- **First-click test:** "Where would you click to…?" — first click correct → ~87% task success in classic studies.
- **Hallway/remote usability test:** 5 users find most major issues in a flow (research-and-information-architecture.md §5).
- **Preference test** only for aesthetics — never to decide usability questions.
- **Fake-door test** for demand: a real button that explains "coming soon — want to be notified?" (be honest; don't take payment).

## 7. Reporting design impact
Before → after with the metric, timeframe and sample: "Checkout completion 61% → 68% (+7 pts, 4 weeks, 12k sessions, mobile drove most of the gain). Guardrails: refunds flat." Pair with one user quote. Note what's uncertain.

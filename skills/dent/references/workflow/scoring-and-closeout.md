# Scoring, Attribution and Close-out

Every substantial deliverable ends with an honest scorecard, an attribution summary and a short close-out. The user can then ask `/dent:improve` to raise the score. Used by SKILL.md §8, `/dent:score`, `/dent:improve`.

---

## 1. Build the scorecard from the request (not a generic rubric)

1. **List what was asked.** Every explicit requirement becomes a line (R-01, R-02…). These lines come first and weigh most.
2. **Add the quality lines that matter for this deliverable** (pick the relevant ones):

| Line | 10 looks like |
|---|---|
| Clarity | Purpose and next step obvious in 5 s |
| Hierarchy & composition | One focal point per section, deliberate scale contrast, rhythm with intentional variation |
| Typography | Characterful pairing, strong scale, craft (tracking, wraps, numerals), hero type that carries the page |
| Color & surfaces | Intentional palette with roles, AA everywhere, depth used with purpose |
| Consistency | Every component matches its spec on every screen |
| States & feedback | All states designed and working |
| Accessibility | All gates G3–G4, G10–G11 pass; keyboard path verified |
| Web platform | Native, modern implementation per the retrieved Modern Web Guidance guides; fallbacks match the support policy; G13 passes |
| Responsiveness | Designed (not shrunk) at phone, tablet, desktop; zero overflow |
| Function | Every control does what it claims; journeys complete |
| Distinctiveness | Unmistakably *this* product; category cliché avoided; signature element |
| Content honesty & copy | Specific, true, no invented proof, no typos |
| Motion | Purposeful, on-system, smooth, reduced-motion alternative |
| Motion graphics | Strong concept, storyboarded, timing and composition of a professional reel |
| Sound | Cohesive palette, useful, never intrusive, fully optional |
| Voice/narration | Clear script, natural pacing, correct pronunciation, captions |
| Video | Message lands in the first seconds, pacing, sync, captions, platform specs |
| Performance | Measured and within budget |

3. **Score each line 0–10 with evidence.** Evidence = something observed: a screenshot, a check result, a measurement, a quote of the copy.

## 2. Scoring rules (keep yourself honest)
- **No evidence, no high score.** A line you could not verify is capped at **6** and marked "unverified".
- **A failed gate caps its line at 4** until fixed.
- **Requirements first:** if any Must requirement is not implemented, overall cannot exceed 6.
- Use the full scale. 7 = solid professional work; 8 = would ship proudly; 9 = portfolio-grade; 10 = best-in-class, rarely given.
- Overall = average of all lines, but requirement lines count double.
- You are scoring your own work, so you are biased upward. Before finalising, find the weakest visible thing in each screenshot and score with it in mind.
- Self-scores are not benchmark results. Independent review (a person or another model) is needed for published comparisons.
- **Blockers stay visible.** Any open Blocker (§6 severity) is listed above the overall score, and the overall cannot exceed **6** while one is open, however good the other lines are. A blocker is never averaged away.

## 3. Target and the improve loop
- **Target:** overall ≥ 8 and no line < 6 (the user may set another target, e.g. "9+ on distinctiveness").
- **Below target:** list the **3 highest-impact improvements**: each with the line it raises, what to change, and expected new score. Ask: "Want me to apply these (`/dent:improve`)?"
- **`/dent:improve`:** apply the listed fixes in order, re-verify the affected gates, re-score only with new evidence, show before → after per line. Stop when the target is met or when the remaining gap needs a user decision (e.g. real testimonials, brand assets, budget for a paid voice).
- Two improve rounds without movement → say so and propose a direction change instead of polishing further.

## 3b. Independent evaluation (three evaluators) [Rule at Polished+ and All-out]
The builder is biased toward its own work. Before the final score at Polished and All-out (and whenever the user asks for a review), run **three separate evaluators**. Where the agent can start subagents, give each one a fresh context with only: the original request, DESIGN.md/PLAN.md, the screenshots and verification output, and the files; never the builder's reasoning or self-score. Without subagents, run them yourself one after another, each from its checklist only, and say they were not independent.

| Evaluator | Looks at | Checklist |
|---|---|---|
| **Visual** | Rendered screenshots at 320/390/768/1440, both themes | Composition and hierarchy, typography craft, color and contrast, consistency, brand fit, responsive rendering, distinctiveness (`../creative/anti-slop.md`), polish |
| **UX** | The running page/app and the journeys | Task completion end to end, navigation and discoverability, interaction clarity, content and IA, empty/loading/success/error states, keyboard and screen-reader use |
| **Engineering** | The code and the check output | Correctness and regression risk, architecture fit, types and error handling, performance (measured), security (unsafe HTML, secrets, validation), dependencies justified (`../catalog/component-selection.md` §4b), tests, MWG compliance (G13) |

Each evaluator returns: a verdict (**Accept** / **Accept with fixes** / **Reject**), findings with severity (§6), evidence, and the lines it would score differently. **A Reject blocks delivery**: fix the cause or present the work with the rejection and its reasons stated plainly. Merge the three reports into `REVIEW.md` (`templates/REVIEW.md`) and use them when scoring; where the builder's score and an evaluator's differ by 2+ points, use the evaluator's unless you can show new evidence.

## 4. Attribution (what came from where)
Summarise the Decision Log's Source column in 3–6 lines:
- **From DENT:** e.g. "Swiss base style and its overrides (`styles/swiss.md`), landing-page section order (`recipes/landing-page.md` §3), motion tokens (`modern-layer.md` §7.2)."
- **From Modern Web Guidance:** the guides that shaped the web code (e.g. "native `<dialog>` mobile menu (`navigation-drawer`), per-rule reduced motion (`motion`)").
- **From you (the user):** effort level, brand color, chosen direction…
- **Agent judgment:** choices DENT left open (e.g. the exact hero crop, the second font).
- **Overrides:** any place you deliberately departed from a DENT default, and why it is better.

## 5. Close-out message (keep it short)
1. What was built (one or two lines + where the files are).
2. Requirements: met / partly met / not met.
3. Checks: the verification table (Passed / Failed / Not run / Blocked / N/A).
4. Scorecard summary: overall and the two weakest lines.
5. Attribution summary.
6. Known issues and anything that needs the user (real content, licences, accounts).
7. One-line next step (e.g. "Score is 7.6, below your 8 target: want me to run /dent:improve?").
8. If MWG was consulted, end with the `### Modern Web Guidance` section in MWG's own format: one first-person bullet per guide that shaped the code, with a short verbatim quote of the specific rule (`../modern-web-guidance.md` §2 step 5). Never cite a guide or quote you didn't retrieve in this session.

## 6. Severity levels (used by evaluators, audits and the scorecard)
- **Blocker:** prevents core use, breaks the app, or creates a serious security, privacy or accessibility barrier ([Rule] failure on a primary path). Must be fixed or explicitly disclosed before delivery.
- **High:** breaks an important workflow or causes a major visual/responsive defect.
- **Medium:** noticeably harms usability, consistency or maintainability.
- **Low:** polish or a non-essential refinement.

Write `SCORECARD.md` into the project (from `templates/SCORECARD.md`) at Standard effort and above, and for every showcase or benchmark run. A score that only exists in chat is lost.

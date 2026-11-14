# Planning and Plan Audit

How much to plan, how to write the plan, how to attack it, and when to ask for approval. Used by SKILL.md §1.0 and §1.3, and by `/dent:plan`, `/dent:create`, `/dent:redesign`, `/dent:implement`.

---

## 1. Choose the depth

Score each dimension, then take the **highest** level any dimension points to.

| Dimension | Quick | Standard | Advanced | Critical |
|---|---|---|---|---|
| Scope | One element | One component/screen/short piece | Several screens, a full page, a video, a sound identity | Whole product or architecture |
| Risk | Visual only | Functional, contained | Shared components, many users | Payments, auth, personal data, deletion, security |
| Ambiguity | One reading | Small gaps | Several plausible readings | Direction itself is unclear |
| Reversibility | Trivial undo | Easy undo | Needs migration | Hard to reverse |
| Verification need | Look once | Screens + states | Multi-viewport, journeys, regression | Expanded tests + staged rollout |

Effort level (Essential → All-out) is a separate dial: it changes craft depth, never the safety checks. A "quick" change to checkout is still Critical.

## 2. Gather facts first (all depths above Quick)

Write three short lists before planning:
- **Confirmed:** from the request, repository, DESIGN.md, or something you looked at.
- **Assumed:** reasonable working assumptions you will disclose.
- **Unknown:** things that would change correctness, risk or direction if answered differently. Ask about these only; decide the rest.

In a codebase also record: framework, router, styling system, token source, component library, icon set, fonts, test tools, build/lint commands, and screens that share components with the target.

## 3. Write the plan

**Standard depth:** an inline plan of 5–10 lines:
```
Goal: …   Deliverable: …   Direction: concept + base style (+accent)
Sections/screens: …   Components/libraries: …   States: …
Motion/sound: …   Verification: G1–G12 that apply + tools   Done when: …
```

**Advanced/Critical:** fill `templates/PLAN.md`. Rules:
- Every explicit requirement gets an ID (`R-01`), priority (Must/Should/Could) and an **observable acceptance criterion** ("At 390 px the page has no horizontal scroll", not "responsive").
- Never add requirements the user didn't ask for as Musts; suggestions go under Could or Next.
- Every requirement maps to a verification method in §11 of the plan.
- Phases are ordered by dependency, each with completion criteria.
- The definition of done is a checklist you can tick, not a feeling.

## 4. Audit the plan (a separate step, not a re-read)

Read the plan as a skeptical senior reviewer. Answer every question in writing (one line each is fine):

**Coverage:** Does every requirement have an implementation and an acceptance criterion? Any contradiction or ambiguity? Any user flow missing (first visit, error, empty, returning user)?

**Product and UX:** Does it solve the user's actual problem? Is there one obvious primary action per view? Any step or decision that could be removed? Are failure and recovery paths designed?

**Design:** Concept stated? Category cliché named and diverged from? One base style + ≤1 accent? Signature element chosen? Does it reuse the existing design language where one exists? Are motion and sound purposeful (or deliberately absent)?

**Honesty:** Does any planned section need numbers, testimonials, logos or reviews the user didn't provide? Replace them with verifiable content or bracketed placeholders now.

**Technical:** Fits the existing architecture? Reuses existing components/tokens? Every new dependency justified (one per job, licence known)? Performance, privacy and security implications? Simpler option available?

**Accessibility:** Semantics, keyboard, focus management, labels, contrast in every theme, reduced motion, sound alternatives, target sizes, zoom/reflow.

**Verification:** Can the planned checks actually prove each requirement? Which tools exist here? Which checks can't run, and what is the fallback?

**Scope and risk:** Only necessary files touched? Destructive or irreversible steps flagged for approval? High-risk work staged?

Classify each finding:
- **Blocker:** must be fixed before building.
- **Major:** fix it, or get the user to accept it explicitly.
- **Minor:** improve if cheap.
- **Observation:** note only.

**Revise the plan** for every Blocker and Major, then re-check those items. Listing problems and building the flawed plan anyway is a failure.

## 5. Approval policy

Proceed **without** a checkpoint when the task is small, clear and reversible, the user asked you to just do it, or the plan follows directly from the request.

**Ask for approval** (show a short summary: goal, direction, scope, risks, open questions) when the work changes product direction or major flows, several materially different approaches exist, it spans many screens or layers, it is risky/destructive/costly, important requirements are uncertain, or the user asked to see the plan first.

Never ask approval for routine details you can decide responsibly.

## 6. Requirements traceability

Keep a matrix in PLAN.md (not a separate file):

| ID | Requirement | Implementation | Verification | Status |
|---|---|---|---|---|
| R-01 | Responsive navigation | `Header` with disclosure menu < 768 px | No overflow at 320–1440; menu operable by keyboard | Verified |

Status is one of: Implemented · Verified · Partially verified · Blocked · Not implemented. "Code exists" is not "Verified".

## 7. Decisions and uncertainty

For consequential decisions record: decision, context, alternatives considered, why this one, trade-offs, and whether user approval was needed or obtained. Use the Decision Log's Source column (User / DENT file § / Agent judgment / Override). Ask the user only when an unknown materially affects correctness, risk or direction; otherwise make a reversible assumption and disclose it.

## 8. Re-plan when facts change

If the repository or user feedback invalidates an assumption mid-build: stop, update the plan (mark what changed and why), re-audit the affected part, and continue. Consequential scope growth needs approval.

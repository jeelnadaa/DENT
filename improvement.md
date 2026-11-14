# DENT 2.0 --- Comprehensive Improvement Specification

**Document type:** Product and engineering improvement specification\
**Target:** The DENT skill repository\
**Purpose:** Give an AI coding agent a complete, actionable
specification for auditing, upgrading, testing, and documenting DENT
without losing existing capabilities.

------------------------------------------------------------------------

## 1. Executive summary

DENT should evolve from a capable interface-design skill into a
**reliable product-design and implementation workflow**.

The objective is not to make the skill larger for its own sake. The
objective is to make an AI agent consistently:

1.  Understand the request and the existing product before making
    changes.
2.  Inspect the repository, architecture, design system, assets,
    constraints, and existing behavior.
3.  Plan substantial work before implementation.
4.  Audit and improve that plan against DENT's own principles.
5.  Obtain approval when the task warrants it.
6.  Implement in controlled, traceable phases.
7.  Verify the real product---not merely the source code or a
    screenshot.
8.  Detect regressions and protect unrelated functionality.
9.  Document decisions, deviations, and remaining risks.
10. Stop when the agreed definition of done has been met.
11. Select and integrate UI libraries based on verified fit rather than popularity.
12. Engineer purposeful motion graphics and sound as first-class experience disciplines.
13. Present DENT through a distinctive, truthful, media-rich README showcase.
14. Validate the repository, its documentation, its demos, and its Git state before declaring completion.

DENT must remain adaptable. A small visual correction should not trigger
an elaborate planning ceremony. A high-risk checkout redesign or
multi-screen application change should receive deeper analysis and
verification.

### Guiding principle

> DENT should not merely tell an agent what good design looks like. It
> should guide the agent through how to plan, justify, implement,
> verify, and maintain good design.

------------------------------------------------------------------------

## 2. Non-goals and guardrails

The upgrade must not:

-   Replace useful existing DENT capabilities merely to impose a new
    architecture.
-   Turn every request into a lengthy questionnaire or approval process.
-   Require a `PLAN.md` for trivial changes.
-   Treat every design guideline as an absolute rule.
-   Force the same visual style, layout, or component pattern on every
    product.
-   Introduce dependencies, frameworks, tools, or services without a
    reason.
-   Rewrite unrelated parts of a codebase while implementing a scoped
    request.
-   Claim that tests, browser checks, accessibility audits, or
    screenshots were performed when they were not.
-   Treat a screenshot as proof that an interactive product works.
-   Automatically reject intentional visual differences as regressions.
-   Generate excessive documentation that becomes stale or burdensome.
-   Break the existing `/dent` entry point, existing modes, references,
    templates, or `DESIGN.md` compatibility.
- Treat a catalogue of libraries as a popularity list; every recommendation must be contextual, sourced, and evaluated.
- Add motion or sound merely for decoration, or make essential functionality depend on either.
- Assume a package, plugin, asset, font, or sound file is commercially usable because it is free to download.
- Claim that a README supports interactive HTML, JavaScript, CSS, or autoplay media when GitHub does not reliably support it.

Preserve the existing modes, effort levels, design references, industry
playbooks, quality guidance, and benchmark/evaluation material wherever
possible. Extend and reorganize them incrementally.

------------------------------------------------------------------------

# Part I --- Workflow intelligence

## 3. Introduce a Plan → Audit → Approve → Execute → Verify workflow

This is the highest-priority change.

For substantial tasks, DENT should use a deliberate workflow before
making implementation changes.

### 3.1 Stage 1: Understand

Before planning, inspect the available context.

The agent should:

-   Parse the user's goal and explicit requirements.
-   Identify the expected deliverable and what success means.
-   Determine whether this is a new product, redesign, extension, bug
    fix, audit, or design-system task.
-   Inspect the repository structure and relevant source files.
-   Identify the framework, build system, routing, state management,
    styling approach, and test setup where applicable.
-   Inspect existing design tokens, components, typography, icon
    libraries, and conventions.
-   Identify existing functionality that must remain unchanged.
-   Inspect available assets and licenses where relevant.
-   Identify technical, product, platform, and time constraints.
-   Separate confirmed facts from assumptions and unknowns.

Do not infer that a feature exists simply because it is common in
similar products. Do not invent requirements.

### 3.2 Stage 2: Plan

Create a structured implementation plan for substantial work.

The plan should explain:

1.  **Objective:** What is being built or changed, and why?
2.  **Scope:** What is included and explicitly excluded?
3.  **Existing-system findings:** Architecture, components, tokens,
    behavior, constraints, and reusable assets.
4.  **User experience:** Screens, routes, user flows, information
    architecture, and interactions.
5.  **Design direction:** Visual concept, hierarchy, typography, color,
    spacing, density, imagery, and motion.
6.  **Technical strategy:** Components, state, data flow, dependencies,
    integration points, and architecture.
7.  **States and edge cases:** Loading, empty, error, success, offline,
    permissions, validation, and unavailable data as relevant.
8.  **Accessibility:** Keyboard, focus, semantics, screen readers,
    contrast, reduced motion, and responsive behavior.
9.  **Implementation phases:** Ordered tasks with dependencies and
    completion criteria.
10. **Verification strategy:** How each important requirement will be
    tested.
11. **Risks and trade-offs:** Known uncertainties, likely failure
    points, and alternatives.
12. **Definition of done:** Observable conditions that establish
    completion.

The plan should be concrete enough that another capable agent could
implement it without having to rediscover the entire task.

### 3.3 Suggested `PLAN.md` template

Use this template for substantial tasks. Adapt or omit sections that are
genuinely irrelevant.

``` markdown
# Implementation Plan

## 1. Objective
- Goal:
- User problem:
- Expected outcome:

## 2. Scope
### Included
- ...

### Excluded
- ...

## 3. Existing System Audit
- Framework and architecture:
- Relevant routes/screens:
- Existing components:
- Design tokens and conventions:
- Existing behavior to preserve:
- Available assets:
- Constraints:

## 4. Requirements
| ID | Requirement | Priority | Acceptance criteria |
|---|---|---|---|
| R-01 | ... | Must | ... |

## 5. Proposed Experience
- Information architecture:
- Screens:
- Primary user flows:
- Navigation:
- Key interactions:

## 6. Design Direction
- Concept:
- Visual hierarchy:
- Typography:
- Color and surfaces:
- Spacing and density:
- Imagery and assets:
- Motion:

## 7. Technical Strategy
- Components:
- State and data flow:
- Routing:
- Dependencies:
- Integration points:
- Persistence:
- Error handling:

## 8. States and Edge Cases
- Loading:
- Empty:
- Error:
- Success:
- Offline:
- Permissions:
- Validation:
- Other:

## 9. Accessibility and Responsive Behavior
- Keyboard:
- Focus:
- Semantics:
- Screen readers:
- Contrast:
- Reduced motion:
- Breakpoints and touch behavior:

## 10. Execution Phases
| Phase | Tasks | Dependencies | Completion criteria |
|---|---|---|---|
| 1 | ... | ... | ... |

## 11. Verification Strategy
| Requirement ID | Verification method | Expected result |
|---|---|---|
| R-01 | ... | ... |

## 12. Risks and Trade-offs
- Risk:
- Likelihood/impact:
- Mitigation:

## 13. Assumptions and Open Questions
- Confirmed:
- Assumed:
- Unknown:

## 14. Definition of Done
- [ ] ...
```

### 3.4 Stage 3: Audit the plan

The plan must be challenged before implementation. This is a separate
reasoning step, not a superficial re-reading.

The audit should evaluate:

**Requirement coverage** - Does every explicit requirement have a
proposed implementation? - Does each requirement have an acceptance
criterion? - Are any requirements ambiguous or contradictory? - Are
important user flows missing?

**Product and UX quality** - Does the proposed flow solve the actual
user problem? - Is the information architecture understandable? - Are
there unnecessary steps or decisions? - Are primary and secondary
actions clear? - Have failure and recovery paths been considered?

**Design quality** - Is the visual direction appropriate to the product
and audience? - Does it avoid generic or unjustified patterns? - Is the
hierarchy clear? - Does it reuse the existing design language
appropriately? - Are responsive and interaction states accounted for?

**Technical feasibility** - Does the plan fit the current
architecture? - Can existing components or utilities be reused? - Are
proposed dependencies justified? - Are data, state, routing, and
persistence handled coherently? - Is the proposed implementation
unnecessarily complicated? - Are there security, privacy, or performance
implications?

**Accessibility** - Are semantic structure, keyboard behavior, focus,
contrast, and reduced motion considered? - Are accessible names and
error announcements needed? - Are touch targets and responsive behavior
addressed?

**Verification** - Can the proposed tests actually prove the
requirements? - Are critical user journeys covered? - Is visual review
planned at relevant viewports? - Are limitations in available tools
identified honestly?

**Scope and risk** - Does the plan modify only what is necessary? - Are
destructive or irreversible operations avoided or explicitly approved? -
Are high-risk changes staged? - Are assumptions visible?

The agent should classify findings as: - **Blocker:** Must be resolved
before implementation. - **Major:** Should be resolved or explicitly
accepted. - **Minor:** Improvement that does not block progress. -
**Observation:** Informational note.

The agent must revise the plan after identifying blockers and major
issues. It should not merely list problems and then proceed with the
flawed plan.

### 3.5 Stage 4: Approval policy

Approval should be proportional to task complexity and risk.

**Proceed without a checkpoint** when: - The task is small and
unambiguous. - The changes are reversible and low-risk. - The user has
explicitly asked for direct implementation. - The plan can be safely
inferred from the request and repository.

**Present the plan for approval** when: - The work changes product
direction or major user flows. - Multiple materially different
approaches exist. - The work spans many screens or architectural
layers. - The change is high-risk, destructive, costly, or difficult to
reverse. - Important requirements remain uncertain. - The user
explicitly requests planning or approval first.

Do not ask the user to approve routine implementation details that DENT
can responsibly decide.

When presenting a plan, summarize the important decisions, scope, risks,
and open questions. Do not dump an unnecessarily long internal analysis.

### 3.6 Stage 5: Execute in phases

Implementation should follow the approved or internally audited plan.

-   Work in logical, testable increments.
-   Respect existing architecture and conventions.
-   Reuse healthy components and tokens.
-   Avoid unrelated refactoring.
-   Keep changes scoped.
-   Verify important functionality as it is implemented.
-   Update the plan if new repository facts invalidate it.
-   Record significant deviations and why they were necessary.
-   Do not claim a phase is complete until its completion criteria are
    met.

For large tasks, use checkpoints between phases. For small tasks, avoid
artificial phase overhead.

### 3.7 Stage 6: Verify

Verification must evaluate the actual implementation.

At minimum, choose relevant checks from: - Build and type checking. -
Unit and integration tests. - Route and navigation checks. - Browser
interaction tests. - Form and validation tests. - Keyboard-only
interaction. - Accessibility checks. - Responsive viewport checks. -
Screenshot inspection. - Visual regression comparison. - Performance
checks. - Error-state and recovery checks.

If a tool or environment is unavailable, state that limitation and
provide the strongest feasible alternative. Never fabricate
verification.

### 3.8 Stage 7: Close out

At completion, report:

-   What was implemented.
-   Which requirements were satisfied.
-   What was tested and the result.
-   Important design or technical decisions.
-   Any deviations from the plan.
-   Known issues and unverified areas.
-   Documentation updated.
-   Any recommended next steps.

Do not claim that every requirement passed if some were not verified.

------------------------------------------------------------------------

## 4. Complexity- and risk-based planning

DENT must not apply the same workflow to every task.

Introduce a lightweight task assessment before selecting workflow depth.

### 4.1 Suggested task dimensions

Assess:

-   Scope: one element, one screen, multiple screens, or whole product.
-   Complexity: straightforward, interconnected, or architecturally
    complex.
-   Risk: visual-only, functional, data-related, security-sensitive, or
    destructive.
-   Ambiguity: clear request versus multiple plausible interpretations.
-   Reversibility: easy to undo versus difficult to reverse.
-   Verification needs: visual inspection versus multi-layer testing.

Use the result to select a workflow depth.

  -----------------------------------------------------------------------
  Level                   Typical task            Workflow
  ----------------------- ----------------------- -----------------------
  Quick                   Text, color, spacing,   Understand → change →
                          isolated bug            verify

  Standard                Component, screen, or   Inspect → lightweight
                          contained feature       plan → implement →
                                                  verify

  Advanced                Multiple screens or     Full plan → plan audit
                          interconnected          → phased execution →
                          workflows               verification

  Critical                High-risk, destructive, Full plan → explicit
                          security-sensitive, or  approval where
                          major architecture      appropriate → staged
                          changes                 execution → expanded
                                                  verification
  -----------------------------------------------------------------------

These levels are workflow guidance, not a rigid scoring formula. A small
payment-related change may deserve Critical treatment because of its
risk.

### 4.2 Effort levels

Preserve DENT's existing effort levels: Essential, Standard, Polished,
and All-out.

Clarify that effort level controls the depth of exploration, polish, and
optional refinement---not whether basic safeguards apply.

For example: - Essential: satisfy requirements with clean, accessible
implementation. - Standard: thoughtful UX, responsive behavior, and
relevant verification. - Polished: deeper visual refinement, interaction
details, and broader testing. - All-out: extensive creative exploration,
multi-route review, regression coverage, and thorough verification.

Never use an effort level as an excuse to omit a necessary safety or
correctness check.

------------------------------------------------------------------------

# Part II --- Command architecture

## 5. Expand the slash-command interface

Keep `/dent` as the primary intelligent entry point. Add focused
commands as shortcuts into the same shared system.

### 5.1 Proposed commands

  -----------------------------------------------------------------------
  Command                             Purpose
  ----------------------------------- -----------------------------------
  `/dent`                             Automatically identify the task and
                                      select the right workflow

  `/dent:plan`                        Inspect context and produce a plan
                                      without implementation

  `/dent:audit`                       Audit an existing interface,
                                      codebase, screenshot, or
                                      implementation

  `/dent:create`                      Create a new product or interface

  `/dent:redesign`                    Redesign an existing product while
                                      preserving required behavior

  `/dent:implement`                   Implement an approved plan or
                                      existing `PLAN.md`

  `/dent:review`                      Deep visual, UX, accessibility, and
                                      consistency review

  `/dent:system`                      Inspect, create, or extend a design
                                      system

  `/dent:extend`                      Add a feature or screen while
                                      respecting the existing product

  `/dent:fix`                         Diagnose and fix a specific UI/UX
                                      problem

  `/dent:polish`                      Refine an already functional
                                      interface without unnecessary
                                      redesign

  `/dent:responsive`                  Focus on responsive layout and
                                      interaction behavior

  `/dent:accessibility`               Perform a focused accessibility
                                      audit and remediation

  `/dent:motion`                      Design or refine motion and
                                      micro-interactions
  -----------------------------------------------------------------------

### 5.2 Command behavior

Commands should be thin entry points, not independent implementations of
DENT.

Each command should: 1. Identify its specific intent. 2. Load the
central DENT instructions. 3. Load only the relevant references. 4.
Apply the shared principles and quality requirements. 5. Select the
appropriate workflow depth. 6. Preserve existing project conventions.

Do not duplicate the entire skill in every command file.

### 5.3 Command-specific expectations

**`/dent`** - Automatically classify the request. - Select the existing
DENT mode. - Determine workflow depth. - Route to the appropriate shared
references. - Ask only essential clarification questions.

**`/dent:plan`** - Inspect the relevant repository. - Produce or update
`PLAN.md`. - Audit the plan. - Identify assumptions, risks, and open
questions. - Do not implement unless explicitly requested.

**`/dent:audit`** - Establish audit scope. - Inspect the relevant
implementation. - Report evidence, severity, and impact. - Separate
findings from recommendations. - Do not silently redesign or fix
everything unless requested.

**`/dent:create`** - Understand the product and users. - Explore
creative directions when appropriate. - Plan substantial products. -
Build and verify the result.

**`/dent:redesign`** - Audit the existing product. - Identify
functionality and design decisions to preserve. - Establish the redesign
scope. - Prevent accidental feature removal. - Compare before/after
behavior and appearance where possible.

**`/dent:implement`** - Read the approved plan. - Verify that the
repository still matches its assumptions. - Identify changed or stale
assumptions. - Implement in phases. - Update the plan when justified.

**`/dent:review`** - Review the actual result. - Cover visual quality,
UX, accessibility, responsiveness, functionality, consistency, and
performance where relevant. - Prioritize issues by severity. -
Distinguish verified defects from subjective recommendations.

**`/dent:system`** - Inventory existing tokens and components. -
Identify healthy patterns, inconsistencies, missing capabilities, and
conflicts. - Propose a coherent system. - Avoid creating a parallel
system unnecessarily.

**`/dent:extend`** - Understand existing behavior. - Identify
integration points. - Preserve current conventions. - Avoid unrelated
redesign.

**`/dent:fix`** - Reproduce or understand the problem. - Identify the
root cause. - Make the smallest appropriate fix. - Verify the affected
behavior and nearby regressions.

**`/dent:polish`** - Preserve the established product direction. -
Refine hierarchy, spacing, typography, details, and interactions. -
Avoid changing the information architecture without justification.

**`/dent:responsive`** - Inspect relevant breakpoints and actual
content. - Check layout, overflow, touch interactions, navigation, and
typography. - Avoid merely shrinking the desktop design.

**`/dent:accessibility`** - Audit semantic structure, keyboard behavior,
focus, names, labels, contrast, errors, motion, and relevant WCAG
criteria. - Prioritize barriers that prevent task completion. - Verify
fixes.

**`/dent:motion`** - Define motion purpose and interaction triggers. -
Specify duration, easing, sequencing, and interruption behavior. -
Respect reduced-motion preferences. - Avoid animation that harms
performance or usability.

### 5.4 Command compatibility

Before implementing the command system: - Inspect how the target agent
platform discovers commands and skills. - Follow its actual file and
metadata conventions. - Do not assume that colon-separated command names
are supported by every platform. - If the platform requires a different
directory or naming convention, adapt the proposed names while
preserving their intent. - Test that every command is discoverable and
invokes the correct shared instructions.

------------------------------------------------------------------------

# Part III --- Requirements and design-system intelligence

## 6. Requirements traceability

Introduce a Requirements → Implementation → Verification matrix.

Every meaningful requirement should be traceable from the user's request
through implementation to verification.

### 6.1 Example

  -----------------------------------------------------------------------
  ID                Requirement       Implementation    Verification
  ----------------- ----------------- ----------------- -----------------
  R-01              Responsive        Responsive navbar Test narrow and
                    navigation                          wide viewports

  R-02              Dark mode         Semantic theme    Inspect both
                                      tokens            themes

  R-03              Keyboard access   Focus management  Keyboard-only
                                      and semantics     walkthrough

  R-04              Form validation   Validation and    Invalid and valid
                                      error states      submissions
  -----------------------------------------------------------------------

### 6.2 Rules

-   Assign stable IDs to requirements in substantial tasks.
-   Preserve the user's original intent.
-   Write observable acceptance criteria.
-   Link requirements to components, screens, or relevant implementation
    areas when practical.
-   Link requirements to tests or manual verification.
-   Mark each as implemented, verified, partially verified, blocked, or
    not implemented.
-   Explain any requirement that was changed or excluded.
-   Do not mark implementation as verified merely because code exists.

The matrix may live in `PLAN.md` for a task. Do not introduce a separate
tracking file for every tiny change.

------------------------------------------------------------------------

## 7. Design-system intelligence

DENT should perform a structured design-system inventory before creating
or significantly changing an existing product.

### 7.1 Inventory

Inspect:

**Foundations** - Color palette and semantic roles. - Typography
families, weights, and scales. - Spacing scale. - Border and radius
conventions. - Shadows and elevation. - Grid and layout rules. -
Breakpoints. - Motion and easing conventions.

**Components** - Buttons and variants. - Inputs and form controls. -
Navigation. - Cards and surfaces. - Dialogs and overlays. - Tables and
data displays. - Feedback and notification components. - Loading and
empty states. - Icons and icon conventions.

**Behavior** - Hover, focus, active, disabled, and selected states. -
Keyboard interaction. - Responsive variants. - Validation and
feedback. - Theme behavior.

**Implementation** - Token source. - Component library. - Styling
conventions. - Naming conventions. - Existing utilities. - Storybook or
component documentation, if present.

### 7.2 Classify findings

Classify each relevant finding as:

1.  **Healthy:** Preserve and reuse.
2.  **Inconsistent:** Consolidate where appropriate.
3.  **Missing:** Introduce only when required.
4.  **Outdated:** Recommend replacing with justification.
5.  **Conflicting:** Resolve before extending the system.
6.  **Intentional exception:** Preserve because the context justifies
    it.

Do not assume every deviation is accidental inconsistency.

### 7.3 Extension rules

-   Reuse healthy existing components and tokens.
-   Extend existing variants when that is the simplest coherent
    approach.
-   Avoid duplicate tokens and components.
-   Do not force unrelated screens into identical layouts.
-   Preserve intentional product-specific exceptions.
-   Document significant new tokens, components, and exceptions.
-   Avoid introducing a large design-system framework for a small
    project without a clear benefit.

------------------------------------------------------------------------

## 8. Uncertainty and decision protocol

DENT should make uncertainty visible.

Classify important information as:

-   **Confirmed:** Directly supported by the request, repository, or
    reliable evidence.
-   **Assumed:** A reasonable working assumption.
-   **Unknown:** Information not yet established.
-   **Decision:** A choice made by the agent, with rationale where
    consequential.

For consequential decisions, record: - Decision. - Context. -
Alternatives considered. - Reason for selection. - Trade-offs. - Whether
user approval was needed or obtained.

Ask the user only when an unknown materially affects correctness, risk,
or product direction. Otherwise make a reasonable, reversible assumption
and disclose it.

------------------------------------------------------------------------

## 9. Scope protection and change discipline

DENT must minimize unrelated changes.

Before editing: - Identify the files and components relevant to the
task. - Identify behavior that must remain unchanged. - Note any shared
components that could affect other routes.

During editing: - Avoid opportunistic refactoring. - Avoid replacing the
framework or styling architecture without justification. - Avoid
changing content, navigation, or features outside scope. - Avoid
deleting existing behavior because it is not visible in the requested
screenshot. - Keep changes logically grouped.

After editing: - Inspect the diff. - Look for unrelated modifications. -
Check shared components for unintended side effects. - Explain justified
scope changes.

If new findings require scope expansion, update the plan and obtain
approval when the expansion is consequential.

------------------------------------------------------------------------

# Part IV --- Quality and verification intelligence

## 10. Functional verification

Visual inspection alone is insufficient.

DENT should verify actual behavior using the tools available in the
environment.

### 10.1 Verification areas

  Area             Checks
  ---------------- ----------------------------------------------------------
  Navigation       Routes, links, back/forward behavior, active states
  Buttons          Correct action, disabled behavior, loading feedback
  Forms            Labels, validation, submission, error and success states
  Dialogs          Open, close, Escape, focus entry and restoration
  Menus            Keyboard operation, dismissal, selection
  Data             Loading, populated, empty, stale, and failed states
  Persistence      Refresh behavior where persistence is expected
  Authentication   Relevant authenticated and unauthenticated states
  Permissions      Denied, granted, and unavailable states
  Network          Failure, retry, timeout, and recovery where relevant
  Touch            Mobile interaction and target usability

Only test features relevant to the product and scope.

### 10.2 Test strategy

Prefer the existing test infrastructure. If the project uses Playwright,
Cypress, Vitest, Jest, or another framework, respect it.

Use: - Unit tests for isolated logic. - Component tests for component
behavior. - Integration tests for connected systems. - End-to-end tests
for critical user journeys. - Manual browser inspection where automated
tests cannot establish quality.

Do not add a new test framework automatically.

### 10.3 Honest reporting

For each important check, report one of: - Passed. - Failed. - Not
run. - Blocked. - Not applicable.

Explain blocked or unrun checks.

------------------------------------------------------------------------

## 11. Visual verification and regression

Preserve and extend DENT's existing screenshot-based review workflow.

### 11.1 Visual review

Inspect: - Hierarchy and composition. - Typography and readability. -
Spacing and alignment. - Color and contrast. - Consistency. - Image
quality and cropping. - Responsive layout. - Interaction states. -
Loading and error states. - Motion where relevant.

Capture screenshots at representative viewports, including narrow and
wide layouts. Add intermediate sizes when the layout has meaningful
breakpoint changes.

### 11.2 Baseline and regression system

For ongoing products, support: - Approved baseline screenshots. -
Route-level screenshot coverage. - Component-level visual comparison
where practical. - Design-token drift checks. - Responsive regression
checks. - Intentional-change annotations.

A screenshot difference is evidence to investigate, not automatically a
defect.

### 11.3 Regression policy

When a change is made: 1. Identify directly affected screens and
components. 2. Identify shared components that may affect other screens.
3. Capture or run relevant checks. 4. Compare with the approved baseline
if one exists. 5. Classify differences as intentional, acceptable, or
unintended. 6. Fix unintended regressions. 7. Document accepted visual
changes where meaningful.

Do not require full-product screenshot coverage for every trivial
change.

------------------------------------------------------------------------

## 12. Accessibility intelligence

Preserve DENT's WCAG 2.2 AA baseline and strengthen the practical
verification process.

Check relevant criteria including:

-   Semantic HTML and landmarks.
-   Heading hierarchy.
-   Accessible names and labels.
-   Keyboard navigation.
-   Focus visibility and order.
-   Focus management in dialogs and overlays.
-   Error identification and announcements.
-   Color contrast.
-   Non-color indicators.
-   Touch target size and spacing.
-   Zoom and reflow.
-   Reduced motion.
-   Screen-reader interpretation.
-   Form instructions and validation.
-   Accessible status messages.

### 12.1 Rules

-   Use native semantic elements where appropriate.
-   Do not use ARIA to compensate for avoidable semantic mistakes.
-   Do not remove focus indicators without a valid replacement.
-   Do not communicate essential information through color alone.
-   Respect `prefers-reduced-motion`.
-   Verify keyboard behavior rather than assuming semantic markup is
    sufficient.
-   Use automated accessibility tools as assistance, not as proof of
    complete accessibility.

Report the criteria and limitations of the checks actually performed. Do
not claim complete WCAG compliance based solely on an automated scan.

------------------------------------------------------------------------

## 13. Performance and technical quality

DENT should consider implementation quality as part of product quality.

### 13.1 Web applications

Where relevant, inspect: - Core Web Vitals. - Bundle size and
unnecessary dependencies. - Image dimensions, formats, and loading. -
Font-loading strategy. - Layout shift. - Excessive client-side
JavaScript. - Unnecessary re-renders. - Large lists and rendering
costs. - SSR and hydration issues. - Browser compatibility. - Network
and error handling. - Caching and loading strategy.

### 13.2 Native and other platforms

Use platform-specific performance and lifecycle practices. Do not apply
web-specific checks mechanically to native applications.

### 13.3 Performance policy

-   Measure before making performance claims.
-   Optimize real bottlenecks rather than guessing.
-   Avoid sacrificing accessibility or usability for insignificant
    performance gains.
-   Do not add performance libraries without a justified need.
-   Report measurements, environment, and limitations.

------------------------------------------------------------------------

## 14. User-journey simulation

For substantial workflows, DENT should inspect the product as a user
moving through it, not as a collection of isolated screens.

### 14.1 Example: e-commerce

1.  First-time visitor arrives.
2.  Visitor discovers a category.
3.  Visitor searches or filters.
4.  Visitor opens a product.
5.  Visitor selects a variant.
6.  Visitor adds it to cart.
7.  Visitor edits quantity.
8.  Visitor starts checkout.
9.  Validation fails.
10. Visitor recovers.
11. Payment fails.
12. Visitor retries.
13. Purchase completes.
14. Confirmation is presented.

At each stage, inspect: - Is the next action understandable? - Is the
user's progress visible? - Is feedback timely? - Can the user recover
from errors? - Is important information missing? - Are unnecessary
decisions being introduced? - Does navigation preserve context? - Can
the user abandon or reverse an action when appropriate?

### 14.2 Other product journeys

Adapt the journey to the product: - SaaS onboarding and workspace
setup. - Developer-tool project creation and debugging. - Fintech
account and transaction workflows. - Media discovery and playback. -
Healthcare information and appointment workflows.

Do not invent functionality that the product does not claim to support.

------------------------------------------------------------------------

# Part V --- Creative and product intelligence

## 15. Creative-direction exploration

For substantial new products or major redesigns, introduce a deliberate
divergence stage before committing to a visual concept.

### 15.1 Explore materially different directions

Possible directions include: - Editorial and typography-led. - Technical
and information-dense. - Warm and minimal. - Experimental and
expressive. - Premium and restrained. - Playful and approachable.

These are examples, not a fixed menu or mandatory set of templates.

### 15.2 Compare directions

For each serious candidate, explain: - Core concept. - Visual
language. - Suitability for the product and audience. - Strengths. -
Weaknesses. - Risks. - Accessibility implications. - Implementation
complexity.

Choose a direction based on the product's needs, not novelty alone.

For minor tasks, skip this stage.

### 15.3 Avoid template convergence

Do not make every product look like the same SaaS landing page. Preserve
product identity and use patterns because they solve a problem, not
because they are familiar.

------------------------------------------------------------------------

## 16. Context-aware design intelligence

DENT should adapt design reasoning to product type, audience, platform,
and usage context.

Examples:

  -----------------------------------------------------------------------
  Product type                        Important design considerations
  ----------------------------------- -----------------------------------
  Fintech                             Trust, precision, data clarity,
                                      transaction feedback

  E-commerce                          Discovery, comparison, product
                                      details, checkout recovery

  Developer tools                     Information density, keyboard
                                      shortcuts, code readability

  Healthcare                          Clarity, accessibility, trust,
                                      careful language

  SaaS                                Workflows, onboarding, permissions,
                                      collaboration

  Media                               Discovery, playback, immersion,
                                      content hierarchy

  AI applications                     Streaming, uncertainty, tool
                                      states, citations, retries

  Education                           Learning progression, feedback,
                                      comprehension

  Productivity                        Speed, focus, shortcuts, state
                                      persistence
  -----------------------------------------------------------------------

These are starting considerations, not stereotypes.

The agent should also consider: - User expertise. - Frequency of use. -
Device and input method. - Environmental constraints. - Consequences of
errors. - Data sensitivity. - Localization and content length. - Network
reliability where relevant.

Use existing DENT industry playbooks. Improve their selection and
application rather than duplicating their contents.

------------------------------------------------------------------------

## 17. Asset and imagery intelligence

Asset quality is part of design quality.

DENT should reason about: - Whether imagery is necessary. - Photography
versus illustration versus iconography versus CSS/SVG. - Visual
consistency across assets. - Aspect ratios and cropping. - Resolution
and responsive variants. - Loading and fallback behavior. - Lazy loading
where appropriate. - Font and asset licensing. - Attribution and license
documentation. - Avoiding meaningless decorative imagery.

### 17.1 Asset rules

-   Prefer existing approved project assets when suitable.
-   Do not fabricate product screenshots, logos, or testimonials.
-   Do not use arbitrary stock imagery merely to fill empty space.
-   Preserve aspect ratio and intentional cropping.
-   Provide meaningful alternative text for informative images.
-   Use empty alternative text for purely decorative images when
    appropriate.
-   Document licenses and attribution requirements.
-   Use mock or placeholder assets only when clearly identified as such.

------------------------------------------------------------------------

## 18. Anti-pattern and generic-design detection

Strengthen the existing anti-generic design philosophy with a
reason-based review.

Potential warning signs: - Repeated three-card layouts without an
information-architecture reason. - Unnecessary gradients. - Excessive
pill-shaped elements. - Generic hero compositions. - Arbitrary floating
decorations. - Excessive glassmorphism. - Repetitive animation on every
section. - Empty space without compositional purpose. - Inconsistent
icon styles. - Repeated page compositions. - Decorative elements that
compete with content. - Generic marketing copy unrelated to the product.

### 18.1 Important distinction

DENT must detect unjustified patterns, not ban patterns themselves.

A three-column card layout, gradient, rounded button, or glass surface
can be appropriate. The question is whether it serves the product,
hierarchy, usability, and visual identity.

For each suspected anti-pattern: 1. Identify the pattern. 2. Explain why
it may be harmful in this context. 3. Explain the user or product
impact. 4. Recommend an alternative only when justified.

Avoid turning anti-slop guidance into another rigid design template.

------------------------------------------------------------------------

## 19. Motion and interaction quality

Preserve DENT's existing motion guidance and strengthen it with
purpose-driven behavior.

For significant motion, define: - Trigger. - Purpose. - Duration. -
Easing. - Sequence. - Interruption behavior. - Reduced-motion
alternative. - Performance implications.

Motion should: - Communicate state or spatial relationships. - Provide
meaningful feedback. - Support orientation and continuity. - Avoid
delaying essential actions. - Avoid excessive repetition. - Remain
usable with reduced motion enabled.

Do not add animation merely to make an interface appear sophisticated.

------------------------------------------------------------------------

# Part VI --- Documentation and maintenance

## 20. Documentation architecture

Keep the central skill concise and use references for deeper material.

Suggested organization:

``` text
skills/dent/
│
├── SKILL.md
│
├── commands/
│   ├── dent.md
│   ├── plan.md
│   ├── audit.md
│   ├── create.md
│   ├── redesign.md
│   ├── implement.md
│   ├── review.md
│   ├── system.md
│   ├── extend.md
│   ├── fix.md
│   ├── polish.md
│   ├── responsive.md
│   ├── accessibility.md
│   └── motion.md
│
├── references/
│   ├── workflow/
│   │   ├── planning.md
│   │   ├── plan-audit.md
│   │   ├── execution.md
│   │   ├── approval-policy.md
│   │   └── handoff.md
│   │
│   ├── intelligence/
│   │   ├── codebase-analysis.md
│   │   ├── design-system-detection.md
│   │   ├── requirements-traceability.md
│   │   ├── user-journey-analysis.md
│   │   ├── product-context.md
│   │   └── uncertainty-and-decisions.md
│   │
│   ├── quality/
│   │   ├── visual-review.md
│   │   ├── functional-review.md
│   │   ├── accessibility.md
│   │   ├── performance.md
│   │   ├── regression.md
│   │   └── anti-patterns.md
│   │
│   ├── creative/
│   │   ├── creative-direction.md
│   │   ├── asset-intelligence.md
│   │   ├── styles/
│   │   └── inspiration.md
│   │
│   └── patterns/
│       ├── components.md
│       ├── applications.md
│       ├── platforms.md
│       └── industry-playbooks.md
│
├── templates/
│   ├── PLAN.md
│   ├── DESIGN.md
│   ├── AUDIT.md
│   └── REVIEW.md
│
└── evals/
    ├── ...
```

This is a target architecture, not an instruction to split every
existing file. Inspect the current repository first. Preserve useful
existing files, avoid duplicate references, and migrate only when the
resulting structure improves discoverability and maintenance.

### 20.1 Responsibilities

**`SKILL.md`** - Identity and purpose. - Core non-negotiable
principles. - Task classification. - Workflow selection. -
Reference-loading guidance. - Shared quality expectations. - Links to
commands and references.

**Command files** - Focused entry-point behavior. - Relevant references
to load. - Command-specific constraints. - Expected output.

**References** - Detailed workflows and domain guidance. - Reusable
rules shared by multiple commands. - Technical and quality criteria.

**Templates** - Reusable output structures. - Optional templates for
substantial tasks.

### 20.2 Progressive disclosure

Do not load every reference for every task.

Examples: - A small color fix should not load industry playbooks and
full performance guidance. - A responsive audit should load responsive
and visual verification references. - A new multi-screen product should
load planning, product context, creative direction, design-system,
accessibility, and verification guidance as relevant.

Commands must use the same shared rules rather than developing
contradictory versions.

------------------------------------------------------------------------

## 21. Documentation maintenance and stopping conditions

### 21.1 Incremental documentation

Maintain: - Current design specification in `DESIGN.md`. - Important
decisions and rationale. - Meaningful change history. - Known
exceptions. - Relevant constraints.

Update only the affected sections where practical. Avoid regenerating
large documents for tiny changes.

### 21.2 Definition of done

A task is complete when: - Requirements within scope are implemented. -
Critical acceptance criteria are satisfied. - Required verification has
been performed or limitations disclosed. - No known critical defects
remain. - Unrelated functionality has not been damaged. - Relevant
documentation is updated. - Remaining issues are reported.

### 21.3 Prevent endless polishing

Once the agreed quality bar is met: - Stop adding optional visual
effects. - Stop introducing unrequested features. - Stop repeatedly
refactoring acceptable code. - Report worthwhile future improvements
separately.

Quality means satisfying the goal well, not maximizing the number of
changes.

------------------------------------------------------------------------

# Part VII --- Evaluation and benchmarking

## 22. Expand the evaluation system

DENT should be evaluated empirically rather than judged only by how
comprehensive its instructions appear.

Preserve the existing benchmark and evaluation infrastructure. Inspect
it before adding new suites.

### 22.1 Evaluation categories

  -----------------------------------------------------------------------
  Category                            What to evaluate
  ----------------------------------- -----------------------------------
  Design quality                      Hierarchy, composition, typography,
                                      distinctiveness

  UX quality                          Task completion, clarity, friction,
                                      recovery

  Accessibility                       Semantic quality, keyboard
                                      usability, relevant WCAG criteria

  Functional quality                  Whether interactions and workflows
                                      work

  Consistency                         Design-system adherence across
                                      screens

  Performance                         Runtime performance and resource
                                      use

  Efficiency                          Time, tokens, tool calls, and
                                      unnecessary work

  Reliability                         Reproducibility, regressions, and
                                      honest reporting
  -----------------------------------------------------------------------

### 22.2 Benchmark scenarios

Add or adapt scenarios such as:

1.  Build a SaaS dashboard from scratch.
2.  Redesign an existing application without breaking functionality.
3.  Add a feature to a mature codebase with an existing design system.
4.  Build a multi-step checkout with validation and failure recovery.
5.  Audit and fix an inaccessible application.
6.  Build a responsive product with ten or more screens.
7.  Improve an already good-looking interface without unnecessary
    changes.
8.  Implement an approved design specification accurately.
9.  Fix a specific bug while protecting unrelated routes.
10. Extend a design system without creating duplicate tokens or
    components.
11. Build an AI application with streaming, uncertainty, retry, and tool
    states.
12. Diagnose and correct an unintended visual regression.

### 22.3 Compare three conditions

For relevant benchmark scenarios, compare:

**A. Baseline agent** - No DENT.

**B. Existing DENT** - Current skill and workflow.

**C. DENT with planning and plan auditing** - New workflow and shared
quality guidance.

This comparison helps isolate whether planning and plan auditing
actually improve results.

### 22.4 Measure more than screenshots

Compare: - Requirement coverage. - Functional test success. -
User-journey completion. - Accessibility findings. - Visual quality. -
Design-system consistency. - Regression count. - Performance. - Time and
token consumption. - Unnecessary file changes. - Accuracy of completion
reporting.

### 22.5 Evaluation discipline

-   Use consistent prompts and environments.
-   Keep a record of the model, tool availability, and relevant setup.
-   Use objective checks wherever possible.
-   Use human review for subjective design quality.
-   Avoid scoring only with the same model that generated the result.
-   Record failures and regressions, not just successful examples.
-   Do not optimize for a benchmark at the expense of general
    usefulness.

------------------------------------------------------------------------

# Part VIII --- Additional quality rules

## 23. Make rules proportional rather than rigid

DENT should distinguish three kinds of guidance:

### Non-negotiable requirements

Examples: - Do not claim unperformed verification. - Do not knowingly
break required functionality. - Respect relevant accessibility
requirements. - Do not fabricate product content or capabilities. -
Respect the user's explicit scope and constraints.

### Strong defaults

Examples: - Reuse healthy existing components. - Prefer semantic HTML. -
Keep interactions consistent. - Provide clear feedback. - Use responsive
layouts. - Avoid unnecessary dependencies.

### Context-dependent recommendations

Examples: - One dominant call to action. - Specific card counts. -
Particular animation styles. - Specific corner radii. - Particular
layout compositions.

The agent should understand the purpose behind a guideline and be able
to justify an exception.

## 24. Improve effort-level intelligence

Task complexity and effort preference are separate dimensions.

A user may request a quick fix on a high-risk feature. The work should
remain concise but still receive appropriate safety and verification.

A user may request an All-out landing page. That warrants creative
exploration and detailed visual refinement, but not necessarily an
elaborate backend test suite.

DENT should use: - User-selected effort level. - Task complexity. -
Risk. - Ambiguity. - Available tools.

Together, these determine the appropriate workflow.

## 25. Improve tool awareness

DENT should inspect what tools are available before planning
verification.

Possible tools include: - Browser automation. - Screenshot capture. -
Playwright or Cypress. - Accessibility scanners. - Build and test
commands. - Performance measurement tools. - Design-system or component
explorers.

Rules: - Prefer tools already installed in the project. - Do not assume
a tool exists. - Do not add a dependency just to satisfy a generic
checklist. - Provide manual alternatives where appropriate. - Clearly
disclose checks that could not be performed.

------------------------------------------------------------------------

# Part IX --- Implementation roadmap for upgrading DENT

## 26. Recommended implementation phases

Do not attempt to rewrite the entire repository in one pass.

### Phase 0 --- Repository audit and migration design

Before changing files:

1.  Read the complete current `SKILL.md`.
2.  Inspect every command, mode, reference, template, benchmark, and
    evaluation file.
3.  Map current capabilities to this specification.
4.  Identify duplicated instructions.
5.  Identify contradictory rules.
6.  Identify missing capabilities.
7.  Identify existing file conventions and platform-specific
    requirements.
8.  Build a migration map from existing files to the proposed
    architecture.
9.  Identify what should be preserved, modified, moved, merged, or
    added.

Deliverable: an audited migration plan.

Do not start implementation before understanding the current repository
structure.

### Phase 1 --- Planning and command architecture

Implement: - Complexity- and risk-based workflow selection. - Plan
template. - Plan audit. - Approval policy. - Phased execution. -
Verification and closeout. - Additional commands. - Shared command
behavior.

Test command discovery and backward compatibility.

### Phase 2 --- Requirements and system intelligence

Implement: - Requirements traceability. - Codebase inventory. -
Design-system inventory and classification. - Uncertainty protocol. -
Decision records. - Scope protection.

### Phase 3 --- Verification intelligence

Implement: - Functional verification. - Expanded visual review. -
Accessibility verification. - Responsive verification. - Regression
strategy. - Performance review. - Honest verification reporting.

### Phase 4 --- Creative and contextual intelligence

Implement: - Creative-direction exploration. - Product-context
selection. - User-journey simulation. - Asset and licensing guidance. -
Anti-pattern detection. - Motion and interaction refinement.

### Phase 5 --- Evaluation and refinement

Implement or improve: - Benchmark scenarios. - Evaluation criteria. -
Baseline comparisons. - Efficiency measurement. - Regression tests for
the skill itself. - Documentation and examples.

------------------------------------------------------------------------

# Part X --- Acceptance criteria for DENT 2.0

## 27. Workflow acceptance criteria

-   [ ] DENT can distinguish quick, standard, advanced, and critical
    tasks.
-   [ ] Trivial tasks do not trigger unnecessary planning.
-   [ ] Substantial tasks receive a structured plan.
-   [ ] Plans are audited against DENT principles before implementation.
-   [ ] Blockers and major plan issues are resolved before execution.
-   [ ] Approval is requested when risk or ambiguity warrants it.
-   [ ] Implementation follows logical phases.
-   [ ] Significant plan deviations are recorded.
-   [ ] A definition of done prevents endless polishing.

## 28. Command acceptance criteria

-   [ ] `/dent` remains the primary entry point.
-   [ ] Focused commands exist for the supported platform.
-   [ ] Every command is discoverable.
-   [ ] Commands reuse shared instructions.
-   [ ] Commands do not contradict the central skill.
-   [ ] Existing workflows remain accessible.
-   [ ] Command behavior is tested.

## 29. Intelligence acceptance criteria

-   [ ] Existing architecture is inspected before significant
    implementation.
-   [ ] Existing design systems are inventoried.
-   [ ] Healthy components and tokens are reused.
-   [ ] Requirements are traceable to implementation and verification.
-   [ ] Important assumptions and unknowns are visible.
-   [ ] Scope expansion is controlled.
-   [ ] Unrelated refactoring is avoided.

## 30. Quality acceptance criteria

-   [ ] Visual review remains supported.
-   [ ] Functional verification is included where relevant.
-   [ ] Accessibility checks are practical and honest.
-   [ ] Responsive behavior is verified.
-   [ ] Relevant failure and empty states are considered.
-   [ ] Regression risk is assessed.
-   [ ] Performance is measured when performance claims are made.
-   [ ] Verification limitations are disclosed.

## 31. Creative acceptance criteria

-   [ ] Major creative projects can explore distinct directions.
-   [ ] Design direction is grounded in product context.
-   [ ] Existing product identity is preserved where required.
-   [ ] Asset choices are intentional and licensing is considered.
-   [ ] Anti-pattern detection is reason-based, not a rigid ban list.
-   [ ] Motion serves a purpose and respects reduced motion.

## 32. Evaluation acceptance criteria

-   [ ] Existing benchmarks are preserved or migrated.
-   [ ] New scenarios cover creation, redesign, extension, audit, and
    repair.
-   [ ] Baseline and DENT results can be compared.
-   [ ] Planning improvements can be evaluated separately.
-   [ ] Functional, accessibility, consistency, and efficiency outcomes
    are measured.
-   [ ] Evaluation results are documented honestly.

------------------------------------------------------------------------

# Part XI --- Instructions to the AI agent implementing this specification

## 33. How to execute this upgrade

The AI agent receiving this document must treat it as a specification,
not as permission to blindly rewrite the repository.

### Step 1: Inspect before editing

Read the complete DENT repository. Do not rely on summaries, filenames,
or assumptions.

Inspect: - Main skill instructions. - All existing commands and modes. -
All references. - All templates. - Design and quality guidance. -
Existing benchmarks and evals. - Platform-specific metadata and
conventions.

### Step 2: Produce an implementation plan

Create a migration plan that: - Maps every relevant current capability
to its new location. - Identifies existing content to preserve. -
Identifies duplicate or contradictory content. - Lists new files and
modifications. - Identifies dependencies and compatibility risks. -
Defines tests for each phase.

### Step 3: Audit the implementation plan

Challenge the plan using the plan-audit criteria in this document.

Specifically verify: - No existing valuable capability is accidentally
lost. - No duplicate source of truth is introduced. - The command
architecture matches the actual target platform. - Shared rules remain
centralized. - References are loaded progressively. - The proposed
migration can be implemented incrementally. - The plan does not
overengineer small or optional features.

Revise the plan before editing.

### Step 4: Implement incrementally

Work phase by phase.

After each phase: - Inspect changed files. - Check links and
references. - Check for duplicated or contradictory instructions. -
Validate command discovery where possible. - Run relevant tests or
evaluations. - Update the migration plan.

Do not create every proposed file if an existing file already serves
that purpose well.

### Step 5: Validate the final repository

Check: - All internal references resolve. - All commands are
discoverable. - Existing `/dent` behavior remains compatible. - Existing
modes and effort levels remain available. - Templates are usable. -
Instructions are internally consistent. - No important existing content
was dropped. - Benchmarks and evals remain valid. - The central skill is
concise enough to be usable. - Progressive disclosure is working as
intended.

### Step 6: Report completion

Provide: 1. Summary of architectural changes. 2. New commands and their
behavior. 3. New and updated references. 4. Existing functionality
preserved. 5. Tests and evaluations performed. 6. Known limitations. 7.
Deferred improvements and rationale.

Do not claim full completion if a phase or acceptance criterion remains
unimplemented.

------------------------------------------------------------------------

## 34. Final product principle

DENT 2.0 should behave like a disciplined product-design and engineering
partner.

It should be: - Creative without being arbitrary. - Opinionated without
being rigid. - Thorough without being wasteful. - Technically aware
without overengineering. - Visually ambitious without sacrificing
usability. - Systematic without becoming bureaucratic. - Honest about
what it has and has not verified.

The measure of success is not the number of rules, references, commands,
or files in the repository.

**The measure of success is whether an agent using DENT consistently
produces better products, makes fewer avoidable mistakes, preserves
existing quality, and can demonstrate that its work meets the user's
requirements.**


------------------------------------------------------------------------

# Part XII --- UI component and library intelligence

## 35. Build a verified component-library intelligence system

DENT must be able to discover, compare, select, integrate, and verify UI
libraries. It must not blindly recommend a fashionable library or
replace a healthy existing component system.

### 35.1 Classify the ecosystem correctly

The catalogue must distinguish these categories because they solve
different problems:

1. **Accessible/headless primitives:** behavior, semantics, keyboard
   interaction, and accessibility foundations with limited or no visual
   styling.
2. **Complete component systems:** cohesive, pre-styled component
   families with themes, tokens, and conventions.
3. **Copy-and-customize collections:** components or patterns intended to
   be copied into an application and adapted.
4. **Specialized component libraries:** focused solutions for tables,
   charts, editors, calendars, notifications, maps, carousels, and other
   complex domains.
5. **Animation and interaction runtimes:** tools for motion and
   interactive behavior, not general-purpose component systems.
6. **Templates and commercial UI products:** complete layouts, starter
   kits, and paid resources, with distinct licensing and customization
   implications.

Never compare options from different categories as if they were direct
substitutes.

### 35.2 Initial ecosystem coverage

The catalogue should investigate, at minimum, relevant options from the
following groups. This is a discovery baseline, not a requirement to
install or recommend every item.

**Accessible and headless primitives**

- Radix UI.
- Base UI.
- React Aria and React Spectrum.
- Headless UI.
- Ark UI.
- Zag.js.

**Complete component systems**

- shadcn/ui.
- Mantine.
- MUI.
- Ant Design.
- Chakra UI.
- HeroUI (formerly NextUI; verify current naming and package status).
- PrimeReact.
- Fluent UI.
- Carbon Design System.
- Other actively maintained, stack-appropriate alternatives discovered
  during research.

**Visual component collections and patterns**

- Aceternity UI.
- Magic UI.
- Motion Primitives.
- Cult UI.
- Eldora UI.
- Origin UI.
- Kokonut UI.
- Tailwind UI.
- Tremor.

**Specialized component and interaction libraries**

- Sonner for toast notifications.
- Vaul for drawer patterns.
- cmdk for command menus.
- NumberFlow for animated number transitions.
- Embla Carousel and Swiper for carousels.
- TanStack Table and AG Grid for data grids.
- FullCalendar for calendar interfaces.
- Tiptap, Lexical, and Plate for rich-text editing.
- Recharts, Apache ECharts, and Visx for data visualization.
- React Flow for node-based editors and diagrams.
- dnd-kit for drag-and-drop interactions.
- Motion (formerly Framer Motion) and GSAP for animation.
- Lottie and Rive runtimes for authored animation and interactive assets.
- React Three Fiber and Three.js for 3D experiences.

The catalogue must also discover alternatives for navigation, sidebars,
menus, forms, inputs, selects, comboboxes, date/time pickers, tables,
charts, maps, editors, dialogs, notifications, file uploads, media
players, data displays, and other needs encountered in real projects.

### 35.3 Required metadata for each catalogue entry

Each maintained entry should include:

- Library/product name and category.
- Official website and official documentation URL.
- Date last checked.
- Supported frameworks, rendering environments, and relevant versions.
- Component or capability coverage.
- Styling model and customization depth.
- Accessibility model and documented limitations.
- TypeScript support and framework compatibility.
- Package names and verified installation/integration instructions.
- Peer dependencies and important transitive dependencies.
- License for the library itself, with a link to the license text.
- Commercial-use, attribution, redistribution, or seat restrictions where
  applicable.
- Maintenance signals: release activity, issue health, support policy,
  and compatibility status where verifiable.
- Performance and bundle considerations where measurable or documented.
- Strengths, weaknesses, lock-in, and migration costs.
- Ideal use cases and cases where it is a poor fit.
- Verification status and any unknown or unverified claims.

Do not invent version compatibility, accessibility guarantees, license
terms, or maintenance status. If official sources do not establish a
fact, mark it unknown and explain what must be checked.

### 35.4 Research and evidence policy

Prefer primary sources in this order:

1. Official documentation and API references.
2. Official repository and release notes.
3. Official license files and commercial terms.
4. Official accessibility statements or documented implementation
   guidance.
5. Reputable independent technical evaluations when primary sources do
   not answer a practical question.

Record source URLs and the date checked. Re-check time-sensitive facts
before making a consequential selection. Distinguish a package's
software license from the license of templates, icons, fonts, examples,
images, and other bundled assets.

### 35.5 Context-aware selection procedure

When a project needs a component or library, DENT should:

1. Detect the existing framework, version, styling system, routing,
   rendering model, TypeScript setup, and installed dependencies.
2. Identify the exact component behavior and UX requirements.
3. Inspect whether the project already has a suitable component or
   dependency.
4. Identify candidate libraries from the correct category.
5. Compare compatibility, accessibility, customization, visual fit,
   performance, licensing, maintenance, dependencies, and migration cost.
6. Recommend the smallest coherent solution and explain trade-offs.
7. Prefer reuse or extension when the existing implementation is
   healthy.
8. Avoid overlapping libraries that solve the same problem without a
   clear reason.
9. Confirm package names, install commands, APIs, and versions from
   current official sources before integration.
10. Implement using project conventions and verify behavior in the
    actual application.

A library recommendation is not permission to install it. Dependency
changes must be justified by the task and respect the user's constraints.

### 35.6 Integration and verification rules

- Inspect the installed package and its actual API; do not code against
  remembered or assumed APIs.
- Follow the project's package manager and lockfile.
- Check peer dependency and framework-version compatibility.
- Preserve existing theme tokens, typography, spacing, and interaction
  conventions.
- Avoid wrapping a library in unnecessary abstractions unless that
  abstraction provides real project value.
- Test keyboard behavior, focus, semantics, responsive behavior, and
  loading/error states for the integrated component.
- Verify bundle or runtime impact when it is material.
- Record why a library was selected and what alternatives were rejected
  for consequential decisions.

------------------------------------------------------------------------

# Part XIII --- Motion graphics and visual-experience engineering

## 36. Treat motion as an intentional design and engineering discipline

DENT must distinguish motion graphics from ordinary UI animation.
They overlap, but they have different creative goals, timing needs,
implementation techniques, and verification requirements.

### 36.1 Motion categories

Identify which category the task requires:

- **UI motion:** state transitions, hover/focus feedback, dialogs,
  navigation, loading, and micro-interactions.
- **Motion graphics:** kinetic typography, visual compositions,
  transitions, particles, masks, distortion, brand animation, and
  storytelling sequences.
- **Interactive graphics:** pointer-reactive visuals, generative
  graphics, interactive diagrams, and data-driven visual systems.
- **Scroll experiences:** scroll-linked storytelling, pinned scenes,
  parallax, progressive reveals, and timeline-controlled sections.
- **Product animation:** product tours, feature demonstrations, device
  mockups, and interface choreography.
- **2D/3D experiences:** illustrations, scenes, spatial composition,
  shaders, WebGL/WebGPU, and immersive interactions.
- **Data motion:** animated charts, maps, timelines, and changing
  information displays.

Do not solve every category with the same animation library.

### 36.2 Creative direction and pre-production

For substantial motion work, define:

- Creative objective and audience.
- The story or information the motion communicates.
- Visual concept, composition, hierarchy, and focal point.
- Storyboard or sequence of key states.
- Timing, rhythm, pacing, anticipation, and resolution.
- Kinetic typography and text treatment where relevant.
- Transitions between scenes and how users enter or leave them.
- Interaction triggers and interruption behavior.
- Responsive adaptations and reduced-motion alternatives.
- Asset requirements, provenance, and licensing.

For complex sequences, provide a concise storyboard or timing table
before implementation. Do not make every simple hover effect require a
storyboard.

### 36.3 Motion technology catalogue

Maintain a researched catalogue of relevant technologies, including:

**Browser and UI animation**

- CSS transitions, keyframes, and transforms.
- Web Animations API.
- Motion (formerly Framer Motion).
- GSAP and relevant official plugins.
- Anime.js.
- AutoAnimate.
- Native scroll-driven CSS animations and View Transitions where
  browser support fits the target.

**Timeline, authored, and interactive animation**

- GSAP timelines and ScrollTrigger.
- Theatre.js.
- Lottie and dotLottie.
- Rive and its runtime/state-machine capabilities.
- Lenis and Locomotive Scroll, with current maintenance and compatibility
  checked before use.

**SVG, canvas, and 2D graphics**

- SVG and SMIL where appropriate.
- Canvas 2D.
- PixiJS.
- p5.js.
- Paper.js.
- regl and shader-based approaches.
- Particle, physics, and text-splitting tools when justified.

**3D and GPU experiences**

- Three.js.
- React Three Fiber and Drei.
- Babylon.js.
- WebGL and WebGPU.
- OGL.
- Spline embeds/runtime, with current terms and platform support
  checked.
- Custom shaders and post-processing where necessary.

**Scroll and synchronization**

- ScrollTrigger and other GSAP capabilities.
- Lenis or other smooth-scroll tools only when the UX justifies them.
- Native scroll timelines and intersection-based triggers.
- View Transitions API.
- Animation-frame and timeline synchronization techniques.

For each technology, record official documentation, supported
platforms/frameworks, capability category, TypeScript support,
compatibility, performance characteristics, accessibility implications,
license, trade-offs, dependencies, maintenance signals, integration
steps, and date checked. Separate core libraries from paid plugins and
commercial services. Do not imply that a plugin is free because the core
library is free.

### 36.4 Technology selection

Choose technology based on the effect and project constraints:

- Prefer CSS for simple, declarative transitions and keyframes.
- Prefer the Web Animations API when native browser animation control is
  sufficient.
- Consider Motion for React-oriented UI and layout transitions.
- Consider GSAP for complex timelines, sequencing, scroll choreography,
  and detailed control.
- Consider Lottie/dotLottie for authored vector animation playback.
- Consider Rive for interactive, state-driven vector experiences.
- Consider Canvas/PixiJS for high-volume 2D rendering or particle scenes.
- Consider Three.js/React Three Fiber/Babylon.js for real 3D scenes.
- Consider shaders or lower-level GPU tools only when the effect
  warrants their complexity.
- Avoid adding smooth-scroll libraries if native scrolling meets the
  requirement.

These are starting heuristics, not fixed mandates. Verify current APIs
and browser support before implementation.

### 36.5 Define a coherent motion system

When motion is used across a product, define reusable conventions for:

- Duration tiers (micro, short, standard, long, and staged sequences).
- Easing curves and spring behavior.
- Stagger rules and sequencing.
- Enter/exit and shared-element transitions.
- Hover, focus, press, selection, and loading feedback.
- Scroll-trigger behavior and trigger boundaries.
- Interruption, reversal, cancellation, and repeated activation.
- Reduced-motion alternatives.
- Performance budgets and fallbacks.

Use motion to communicate hierarchy, cause and effect, continuity,
feedback, or narrative. Avoid arbitrary movement and perpetual motion
that distracts from the task.

### 36.6 Advanced motion capabilities

Where the product genuinely benefits, DENT may design and implement:

- Complex multi-stage timelines.
- Scroll-linked storytelling and pinned sequences.
- Kinetic typography and text reveals.
- SVG path drawing and morphing.
- Parallax and layered depth.
- Pointer-reactive and cursor-following effects.
- Particle systems and generative compositions.
- 2D/3D product scenes and camera movement.
- Animated charts, timelines, maps, and diagrams.
- Reusable looping animations.
- Data-driven and state-driven animation.
- Page and route transitions.
- Animation synchronized with sound or audio-reactive visuals.

Advanced effects are optional tools, not a quality checklist. Do not
introduce them without a product or storytelling reason.

### 36.7 Motion performance and lifecycle

Review:

- CPU and GPU cost.
- Frame rate and dropped frames.
- Layout and paint thrashing.
- Use of transform/opacity versus expensive layout properties.
- Canvas and WebGL resource usage.
- Large textures, video, and animation assets.
- Bundle size and lazy loading.
- Mobile and lower-powered device behavior.
- Resize, route-change, and component-unmount cleanup.
- Event listener and animation-frame cleanup.
- Fallbacks when a runtime or GPU feature is unavailable.

Measure meaningful effects on representative devices when possible.
Do not claim smooth 60 FPS without measurement.

### 36.8 Motion accessibility

- Respect `prefers-reduced-motion` and provide a considered alternative.
- Avoid flashing or rapidly repeating effects that may cause harm.
- Do not hide essential information behind animation.
- Keep controls usable by keyboard, touch, and assistive technology.
- Avoid motion that prevents reading or completing a task.
- Provide pause, stop, or hide controls when required by the nature and
  duration of moving content.
- Ensure that reduced-motion mode preserves the information and task
  outcome, not merely removes animation without replacement.

### 36.9 Motion verification

Verify the experience, not just compilation:

- Confirm that the intended animation actually plays.
- Check timeline order, duration, easing, and synchronization.
- Test scroll triggers at different speeds and viewport sizes.
- Test pointer, touch, keyboard, and focus behavior as relevant.
- Change viewport size during or between animations.
- Test reduced-motion preferences.
- Inspect visual glitches, clipping, layout shifts, and z-index issues.
- Check performance on desktop and mobile-class hardware where
  available.
- Confirm cleanup after navigation, unmount, and repeated activation.
- Verify fallback behavior when assets or runtimes fail.

Deliverables for substantial motion work should include creative
rationale, storyboard/timing, technology rationale, reusable
implementation, reduced-motion behavior, performance considerations,
and verification results.

------------------------------------------------------------------------

# Part XIV --- Sound design and audio engineering

## 37. Treat sound as an intentional product discipline

DENT must distinguish UI sound effects from product sound identity,
motion-graphics soundtracks, ambient audio, interactive audio, and
procedural or generative audio.

### 37.1 Audio categories

Identify the intended role:

- **UI sound:** subtle confirmation, selection, error, notification, or
  interaction feedback.
- **Product sound identity:** a consistent sonic language associated
  with a brand or product.
- **Motion-graphics sound:** sound effects and music synchronized to
  visual sequences.
- **Ambient sound:** optional environmental or atmospheric layers.
- **Interactive audio:** sound that responds to user input or application
  state.
- **Audio-reactive visuals:** graphics driven by audio amplitude,
  frequency, beats, or other features.
- **Generative/procedural audio:** sound generated or transformed at
  runtime.
- **Spatial audio:** positional or immersive sound in 3D or XR contexts.

Silence is a valid and sometimes preferable design choice.

### 37.2 Sound direction and design system

For meaningful audio work, define:

- Purpose and emotional tone.
- Sound palette, timbre, pitch, duration, and dynamics.
- Mapping between user actions and sound responses.
- Loudness and perceived-volume conventions.
- Timing, rhythm, and synchronization with motion.
- Attack, decay, sustain, and release where synthesis is involved.
- Layering, mixing, and frequency overlap.
- File formats, sample rates, bit depth, and compression where relevant.
- Loading, caching, and asset budgets.
- Volume, mute, and sound-preference behavior.
- Silent alternatives and failure behavior.

Sounds must be meaningful, consistent, restrained, and useful. Do not
add random clicks, arbitrary musical notes, or repetitive effects merely
to make an interface feel more elaborate.

### 37.3 Audio technology catalogue

Maintain a researched catalogue covering:

**Playback and synthesis**

- Native HTML audio and media elements.
- Web Audio API.
- Tone.js.
- Howler.js and relevant plugins.
- Pizzicato.js.
- Soundfont-based approaches.

**Procedural and interactive audio**

- Web Audio node graphs.
- AudioWorklet.
- Elementary Audio.
- Tuna.js.
- Web MIDI API and MIDI integration where relevant.

**Analysis and visualization**

- AnalyserNode.
- Meyda.
- WaveSurfer.js.
- Peaks.js.
- Audio buffer and waveform analysis approaches.

**Spatial audio and 3D integration**

- Web Audio PannerNode.
- Three.js audio integration.
- WebXR audio approaches.
- Spatial audio and positional sound techniques.

**Motion/audio integration**

- GSAP timeline synchronization.
- Rive events and state changes.
- Lottie synchronization where supported by the runtime.
- Audio-clock and animation-frame synchronization.

**Asset sources and production tools**

Investigate reputable asset sources such as Freesound, Pixabay sound
effects, Mixkit, and OpenGameArt audio, and production tools such as
Audacity, REAPER, Ardour, and LMMS. Check current terms and availability
before use; the examples are not blanket endorsements or guarantees of
license suitability.

Each technology entry must document official documentation, platforms
and frameworks, capability type, compatibility, TypeScript support,
performance and latency considerations, accessibility implications,
license, trade-offs, ideal use cases, installation/integration,
dependencies, maintenance signals, and date checked.

### 37.4 License and asset provenance rules

Software license and audio-asset license are separate concerns.

For every sound asset intended for inclusion, record:

- Asset title and creator where available.
- Original source URL.
- Exact license and a link to its terms.
- Whether commercial use is allowed.
- Attribution requirements.
- Modification and redistribution restrictions.
- Whether the asset is bundled, streamed, or user-provided.
- Date and evidence of the license check.

A free download does not automatically grant unrestricted commercial
use. Do not use an asset when its provenance or permitted use is unclear.
Prefer original, properly licensed, or user-supplied audio. Do not
repackage copyrighted music or sound effects without permission.

### 37.5 Audio technology selection

Choose the simplest suitable technology:

- Native audio elements for straightforward file playback and controls.
- Howler.js when cross-browser playback behavior, sprite support, or
  grouped sound management is needed and its dependency is justified.
- Tone.js for musical timing, synthesis, sequencing, and richer
  procedural audio.
- Web Audio API for custom routing, effects, mixing, analysis, and
  precise control.
- AudioWorklet for processing that must run off the main thread, when
  supported by the target environment.
- AnalyserNode or Meyda for frequency/time-domain analysis and
  audio-reactive experiences.
- WaveSurfer.js or Peaks.js for waveform and audio-region interfaces.

Account for autoplay restrictions, user activation, mobile browser
behavior, latency, supported formats, asset size, license, and user
preferences. Avoid overlapping audio libraries without a clear reason.

### 37.6 Audio implementation and lifecycle

Handle explicitly:

- Autoplay restrictions and user-gesture requirements.
- AudioContext creation, suspension, resume, and closure.
- Volume and mute state.
- Repeated triggers and overlapping sounds.
- Voice stealing or concurrency limits where synthesis is used.
- Asset loading, decoding, caching, and failure.
- Cleanup on route changes and component unmount.
- Latency and synchronization with animation.
- Mobile and desktop differences.
- Background behavior and user control.

Never autoplay unexpected sound. Background or ambient audio must be
opt-in. A blocked or failed audio context must not break the rest of the
application.

### 37.7 Audio accessibility and sensory considerations

- Provide visible sound controls when audio is part of the experience.
- Provide mute and volume controls where appropriate.
- Preserve a complete silent operating mode.
- Do not communicate essential information through sound alone.
- Avoid sudden loud, repetitive, or startling sounds.
- Consider hearing, sensory, and cognitive needs.
- Provide captions or transcripts for speech and meaningful audio
  content where appropriate.
- Respect user preferences and avoid repeatedly prompting after a
  preference is set.

### 37.8 Audio verification

Verify:

- Playback and synthesis actually work.
- Playback starts only after appropriate user activation.
- Autoplay restrictions are handled gracefully.
- Motion and audio synchronization is correct.
- Volume and mute controls work and persist as expected.
- Preferences are respected across relevant routes or sessions.
- Repeated interactions do not create uncontrolled overlapping audio.
- Audio contexts and event handlers are cleaned up.
- Mobile and desktop behavior is acceptable.
- Loading and decoding failures have graceful fallbacks.
- The product remains fully usable with sound disabled.

Use browser automation, audio capture, waveform inspection, or other
objective checks when available. Installing an audio library is not
proof that the intended sound experience works.

Deliverables for substantial audio work should include sound direction,
sound palette, interaction mapping, source/license records, reusable
audio utilities, motion synchronization where needed, controls, silent
alternatives, performance considerations, and verification results.

------------------------------------------------------------------------

# Part XV --- README as public landing page and portfolio

## 38. Redesign the README to showcase DENT

The README is DENT's public landing page and portfolio. It must explain
why DENT matters and demonstrate its capabilities, not merely list
installation instructions.

### 38.1 Audit and narrative planning

Before editing:

- Read the complete existing README.
- Identify accurate content, stale claims, broken links, and useful
  instructions to preserve.
- Establish DENT's identity, audience, differentiators, and central
  promise.
- Define a clear narrative from first impression to technical detail.
- Inventory real screenshots, demos, recordings, and examples available
  in the repository.
- Identify missing demo assets and decide whether they can be produced
  honestly during the upgrade.
- Respect GitHub Markdown and media-rendering limitations.

Do not invent capabilities, users, benchmarks, testimonials, or demo
results.

### 38.2 Visual identity and editorial direction

Create a distinctive, coherent README presentation through:

- A memorable hero and clear headline composition.
- Strong typography and deliberate spacing.
- A restrained, recognizable color language.
- Purposeful layout and visual hierarchy.
- Carefully selected screenshots, diagrams, and media.
- Consistent image framing, captions, and alt text.
- An editorial narrative rather than repetitive feature cards.

Avoid generic AI gradients, excessive glow, repetitive cards, decorative
noise, and visual effects that do not support DENT's identity.

### 38.3 Motion showcase

Show real motion capabilities where genuine demonstrations exist:

- Kinetic typography.
- Visual compositions and transitions.
- Timelines and scroll storytelling.
- Interactive visuals and UI demos.
- 2D/3D scenes.
- Particles or generative visuals.
- Animated data visualization.

Use formats GitHub actually supports in the target README context, such
as optimized GIFs and supported video embeds/links where appropriate.
For unsupported interactive experiences, use a static poster linking
to a real hosted demo or video. Do not assume arbitrary JavaScript,
CSS, or interactive HTML embeds execute in GitHub Markdown.

### 38.4 Sound showcase

Show real audio capabilities through suitable demonstrations:

- UI sound identity.
- Motion and sound synchronization.
- Interactive audio.
- Audio-reactive visuals.
- Procedural audio.
- Waveform or spectrum visualization.

GitHub README rendering cannot be assumed to support a custom
interactive player, arbitrary JavaScript, or autoplay. Use user-initiated
external demos, sample links, waveform/spectrogram images, or video with
sound where the platform supports it. Never autoplay audio.

### 38.5 Suggested README narrative

Use and adapt this sequence based on what the project can genuinely show:

1. Hero: identity, concise promise, and primary links.
2. Introduction: what DENT is and who it helps.
3. Capability overview: design, product engineering, and verification.
4. Motion showcase: real motion examples and demonstrations.
5. Sound/audio showcase: real audio examples and controls.
6. Workflow: discovery, requirements, planning, audit, implementation,
   and verification.
7. Component intelligence: how libraries are evaluated and selected.
8. Creative engineering: visual direction, interaction, motion, and
   sound.
9. Commands: concise command reference.
10. Architecture: how the skill is organized and extended.
11. Installation and usage: accurate, tested instructions.
12. Evaluation and verification: what is tested and how claims are
    measured.
13. Roadmap and contributing: honest status and contribution guidance.

Reorder, combine, or omit sections when a better story is justified.

### 38.6 README asset and publishing quality

- Use real repository-relative paths for committed assets.
- Optimize GIF, video, and image size without making demonstrations
  illegible.
- Add useful alt text and captions.
- Check links, anchors, badges, and media paths.
- Avoid badges that imply unsupported status or metrics.
- Preview the README using GitHub-compatible rendering or the closest
  available equivalent.
- Inspect narrow and wide rendering where possible.
- Ensure the README remains understandable without media, motion, or
  sound.
- Keep installation and usage instructions easy to find.

------------------------------------------------------------------------

# Part XVI --- Expanded evaluation and acceptance coverage

## 39. Expand benchmark scenarios and measurable evaluation

Retain existing benchmark scenarios and add cases that exercise the new
capabilities. Evaluate DENT's instructions and resulting implementation,
not merely the presence of documentation.

### 39.1 Required benchmark scenarios

Include representative tasks for:

- SaaS dashboard with real workflows and data states.
- Data-heavy application with tables, charts, filters, and responsive
  behavior.
- Responsive marketing site with a distinctive visual identity.
- Onboarding form with validation, errors, and recovery.
- Existing design system that must be extended without duplication.
- Unfamiliar framework or stack with compatibility constraints.
- Highly interactive application using drawers, command palette,
  tables, charts, and animations.
- Strict accessibility and performance requirements.
- Motion-heavy marketing experience with scroll storytelling.
- 3D product showcase with fallbacks and mobile constraints.
- Animated data visualization or timeline.
- Interactive audiovisual experience with user-controlled sound,
  synchronization, and a complete silent mode.
- Component-library choice where multiple categories and licenses must
  be compared.
- README/portfolio redesign with actual demos and GitHub media limits.

### 39.2 Compare against the previous version

Where feasible, compare DENT 2.0 against the prior version using the
same task briefs, environments, and evaluation rubric. Score observable
outcomes for:

- Requirement understanding and traceability.
- Plan quality and plan-audit effectiveness.
- Design distinctiveness and product fit.
- Component reuse and library-selection quality.
- Functional completeness and user journeys.
- Accessibility and responsive behavior.
- Motion quality, purpose, and verification.
- Audio quality, licensing, accessibility, and verification.
- Performance and runtime stability.
- Maintainability and scope discipline.
- Accuracy of claims and verification reporting.
- README clarity and authenticity.

Define scoring anchors and evidence for each score. Avoid unsupported
claims such as percentage improvements without repeatable measurement.

### 39.3 Evaluation artifacts

Provide reusable task fixtures, expected behaviors, scoring rubrics,
regression tests, and a results report. Keep fixtures independent of
private credentials and external services wherever possible. When a
scenario cannot be tested automatically, define a repeatable manual
procedure and mark it as manual.

------------------------------------------------------------------------

# Part XVII --- Repository architecture and migration discipline

## 40. Organize DENT for modularity and progressive disclosure

The upgraded repository should be easier to understand, maintain, and
extend without turning the central skill into an enormous instruction
file.

### 40.1 Recommended separation of responsibilities

Organize content according to the actual target platform and existing
repository conventions. The architecture should provide clear homes for:

- Central skill identity, entry point, and shared principles.
- Workflow and planning rules.
- Design and product principles.
- Component/library catalogue and selection methodology.
- Motion graphics and animation guidance/catalogue.
- Sound/audio guidance and catalogue.
- Platform/framework-specific implementation references.
- Commands and command-specific workflows.
- Reusable planning, audit, and verification templates.
- Scripts for link, metadata, and structural validation.
- Benchmark fixtures, evaluation rubrics, and results.
- README showcase assets and demo documentation.

These are responsibility boundaries, not a mandate to create one file
for every bullet. Reuse suitable existing files and avoid unnecessary
fragmentation.

### 40.2 Progressive disclosure

- Keep the central entry point concise and actionable.
- Load detailed catalogues only when the task needs them.
- Keep motion and audio references separate from general UI rules.
- Load framework-specific details only for the detected stack.
- Keep commands thin and route them to shared instructions.
- Avoid duplicating the same rule in multiple documents.
- Provide clear cross-references and a single source of truth for each
  policy.

### 40.3 Validation and backward compatibility

Validate:

- Every internal link and reference path.
- Every command's discoverability and routing.
- Every template's usability.
- Every script's invocation and failure behavior.
- Catalogue metadata consistency and source links.
- No duplicated or contradictory rules.
- Existing `/dent` entry point, modes, effort levels, references,
  templates, and `DESIGN.md` compatibility.
- No essential existing capability removed without explicit rationale.

Use scripts for repeatable checks where practical. A link checker must
handle expected external-link/network failures transparently and must
not silently report an incomplete check as a pass.

------------------------------------------------------------------------

# Part XVIII --- Final repository audit, Git hygiene, and delivery

## 41. Mandatory final audit

Before declaring DENT 2.0 complete, perform a requirement-by-requirement
final audit covering:

- Every original requirement in this specification.
- Every new requirement introduced by the latest upgrade scope.
- Every command, workflow, reference, template, and script.
- UI library entries, official sources, licenses, compatibility, and
  selection methodology.
- Motion technology entries, accessibility, performance, and actual
  verification guidance.
- Audio technology entries, sound-asset licensing, accessibility,
  browser behavior, synchronization, and verification.
- README claims, assets, links, media behavior, and GitHub rendering
  limitations.
- Evaluation fixtures, benchmark scenarios, and scoring methodology.
- Existing behavior and backward compatibility.
- Documentation consistency, duplicated material, and stale content.

For each item, record one of: complete and verified, implemented but
not verified, partial, blocked, deferred with rationale, or not
applicable. Do not mark an item complete based on a heading or planned
file alone.

### 41.1 Final validation sequence

1. Re-read the original user requirements and this specification.
2. Compare each requirement against actual repository changes.
3. Run all relevant existing tests and newly added tests.
4. Run scripts for internal links, command discovery, references, and
   catalogue metadata where available.
5. Run build/type/lint checks where relevant to the repository.
6. Inspect the final diff for regressions, duplication, stale content,
   secrets, generated junk, and accidental dependency changes.
7. Review README rendering and all referenced assets.
8. Verify demos and media behavior to the extent the environment allows.
9. Re-check the Git working tree and commit only intended files.
10. Produce an honest verification report with limitations.

## 42. Git and commit requirements

A local commit is part of the requested delivery when repository access
and Git are available. It is not permission to push to a remote.

Before editing or staging:

- Inspect `git status` and the current branch.
- Inspect recent history and repository conventions where useful.
- Identify pre-existing user changes and untracked files.
- Preserve unrelated work; never overwrite or discard it.

Before committing:

- Review the complete diff.
- Stage only files intentionally changed for DENT 2.0.
- Exclude secrets, credentials, local configuration, caches, temporary
  files, generated junk, and accidental build output.
- Review dependency and lockfile changes.
- Run final relevant validation against the exact staged state.

Use a clear commit message, for example:

```text
feat: transform DENT into DENT 2.0
```

After committing:

- Verify the commit hash.
- Verify the commit contains only intended changes.
- Verify the working tree status.
- Report the commit hash and whether the tree is clean.
- Do not push unless the user explicitly authorizes pushing.

If Git or repository access is unavailable, state the exact limitation
and provide the uncommitted changes or instructions honestly. Never claim
a commit was created when it was not.

## 43. Required delivery artifacts

The completed DENT 2.0 upgrade should deliver, as applicable to the
existing repository architecture:

1. Working upgraded DENT skill and compatible entry point.
2. Changelog or migration notes.
3. Architecture overview and command reference.
4. Component/library catalogue and selection methodology.
5. Motion technology catalogue, design guidance, and verification
   methodology.
6. Sound/audio catalogue, design guidance, asset-license policy, and
   verification methodology.
7. Redesigned README that acts as a genuine public showcase.
8. Real demo assets and demonstrations, not fabricated screenshots or
   benchmarks.
9. Updated templates, checklists, scripts, and references.
10. Automated tests and evaluation fixtures.
11. Benchmark/evaluation results with methodology and limitations.
12. Final verification report and known limitations.
13. Local Git commit when repository access and Git are available.

Not every item must become a separate file. Integrate deliverables into
existing architecture when that is clearer and more maintainable.

------------------------------------------------------------------------

# Part XIX --- Expanded DENT 2.0 acceptance criteria

## 44. Component intelligence acceptance criteria

- [ ] The catalogue distinguishes primitives, complete systems,
      copy/customize collections, specialized components, animation
      runtimes, and commercial templates.
- [ ] Required ecosystem examples are investigated or explicitly marked
      as not relevant/unverified.
- [ ] Entries include official URLs, date checked, framework and
      TypeScript compatibility, styling, accessibility, licensing,
      maintenance, dependencies, trade-offs, and use cases.
- [ ] Selection detects the project's actual stack and existing
      components.
- [ ] Recommendations compare alternatives and explain trade-offs.
- [ ] Installation and APIs are verified against current official
      documentation.
- [ ] Integration preserves existing conventions and avoids duplicate
      systems.
- [ ] Integrated components receive functional, responsive, and
      accessibility verification.

## 45. Motion acceptance criteria

- [ ] DENT distinguishes UI motion, motion graphics, interactive
      graphics, scroll experiences, product animation, 2D/3D, and data
      motion.
- [ ] Substantial motion work defines purpose, creative direction,
      sequence/storyboard, and timing.
- [ ] The motion catalogue covers relevant CSS/native, timeline,
      authored, canvas, SVG, 2D, 3D, scroll, and GPU approaches.
- [ ] Technology choice is justified by effect, stack, compatibility,
      performance, accessibility, and licensing.
- [ ] A coherent motion system is defined where motion is used broadly.
- [ ] Reduced-motion behavior and alternatives are implemented.
- [ ] Performance, responsive behavior, cleanup, and fallbacks are
      considered.
- [ ] Actual playback, timing, scroll, input, and lifecycle are
      verified; compilation alone is insufficient.

## 46. Audio acceptance criteria

- [ ] DENT distinguishes UI sound, sound identity, motion sound,
      ambient, interactive, reactive, procedural, and spatial audio.
- [ ] The audio catalogue covers playback, synthesis, processing,
      analysis, visualization, spatial audio, and motion integration.
- [ ] Software licenses and sound-asset licenses are treated separately.
- [ ] Asset provenance, commercial-use terms, and attribution are
      recorded before use.
- [ ] Autoplay restrictions, user activation, context lifecycle,
      concurrency, volume, mute, and cleanup are handled.
- [ ] Audio is opt-in where appropriate and never unexpectedly
      autoplayed.
- [ ] Silent operation remains complete and usable.
- [ ] Playback, synchronization, controls, failures, and mobile/desktop
      behavior are verified.

## 47. README and repository acceptance criteria

- [ ] The README has been audited and redesigned as DENT's public
      landing page and portfolio.
- [ ] Its identity and narrative are distinctive and consistent.
- [ ] It showcases only real, verifiable capabilities and demos.
- [ ] Motion and audio demonstrations respect GitHub Markdown/media
      limitations and user activation.
- [ ] Assets are optimized, have useful alt text, and use valid paths.
- [ ] README links, badges, commands, and installation instructions are
      checked.
- [ ] Repository architecture is modular, progressively disclosed,
      and avoids duplicated sources of truth.
- [ ] Existing functionality and compatibility are preserved.
- [ ] Automated tests, evaluation fixtures, and final audit are present
      and their actual results are reported.
- [ ] Git changes are reviewed, intended files alone are committed, the
      commit hash is verified, and no remote push occurs without
      authorization.

------------------------------------------------------------------------

# Part XX --- Updated implementation instructions

## 48. Execution protocol for the AI agent

The implementing agent must follow the protocol below. These
instructions supplement Sections 33 and 34; they do not replace the
original audit-first requirement.

### Step 1: Establish repository state

- Confirm the repository and target branch.
- Inspect `git status` before changing files.
- Identify existing user modifications and untracked files.
- Inventory all files, commands, references, scripts, templates,
  workflows, tests, configuration, and documentation.
- Read the current README completely.
- Read this entire `improvement.md` specification.
- Preserve existing capabilities and note compatibility constraints.

### Step 2: Create a complete requirement checklist

Convert every applicable requirement in this specification into a
traceable checklist. Group requirements by workflow, commands,
component intelligence, motion, audio, README, architecture,
verification, evaluation, delivery, and Git. Give each requirement an
acceptance criterion and a planned verification method.

### Step 3: Audit and plan before edits

- Map current repository structure and behavior.
- Identify duplicated, stale, broken, or conflicting instructions.
- Identify missing capabilities and existing functionality to preserve.
- Propose a phased migration with dependencies, target files,
  deliverables, risks, and validation.
- Include a README creative direction and real-demo asset plan.
- Include component, motion, and audio research/verification plans.
- Review the proposed architecture for modularity and progressive
  disclosure.
- Challenge the plan against every requirement and revise it.

Do not edit implementation files before this audit and plan are
complete. If the user explicitly requests an audit/plan checkpoint,
present it and wait for approval. Otherwise, once the plan has been
internally audited, proceed without unnecessary approval questions.

### Step 4: Research external technologies responsibly

For component, motion, and audio technologies:

- Use official documentation, repositories, release notes, and license
  files as primary evidence.
- Verify current package names, APIs, versions, compatibility, and
  terms.
- Record dates and uncertainty.
- Avoid adding dependencies simply to populate a catalogue.
- Distinguish open-source software, paid plugins, commercial services,
  templates, and media-asset licensing.

### Step 5: Implement incrementally

- Implement in logical phases with reviewable diffs.
- Keep the central skill focused and load detailed material
  progressively.
- Reuse existing architecture where healthy.
- Add commands only using the target platform's verified conventions.
- Add catalogue entries with evidence and consistent metadata.
- Build genuine demos only when they can be implemented and verified.
- Preserve all useful existing behavior.
- Update the plan when repository facts require a justified change.

### Step 6: Test and evaluate continuously

After each phase:

- Inspect changed files and the diff.
- Validate links, references, command discovery, and templates.
- Run relevant scripts, tests, builds, and evaluations.
- Test component integrations in the actual project context.
- Verify motion playback, accessibility, and performance where
  implemented.
- Verify audio behavior, licensing, synchronization, and silent mode
  where implemented.
- Review README assets and rendering.
- Fix regressions before proceeding.

Do not treat package installation, code compilation, or documentation
presence as proof that a capability works.

### Step 7: Perform final audit and commit

Follow Sections 41 and 42 exactly. Compare every requirement with the
actual repository. Inspect the final staged diff, run final checks, make
a local commit if possible, verify its hash and working tree, and do not
push without explicit authorization.

### Step 8: Report honestly

The final report must include:

1. Architecture and workflow changes.
2. New or updated commands and references.
3. Component intelligence added and evidence status.
4. Motion capabilities and verification status.
5. Audio capabilities, licensing, and verification status.
6. README redesign and real showcase assets.
7. Tests, benchmarks, and evaluation results.
8. Existing functionality preserved.
9. Known limitations, unknowns, and deferred work.
10. Git commit hash and working-tree status, or the exact reason no
    commit could be created.

Do not claim DENT 2.0 is complete while blockers remain or when major
requirements are only documented but not implemented.

------------------------------------------------------------------------

## 49. Final operating principle

DENT 2.0 must combine product judgment, design craft, engineering
reliability, and creative execution. It should be capable of selecting
the right component system, creating purposeful motion, designing
thoughtful sound, and demonstrating its work without sacrificing
accessibility, performance, maintainability, or trust.

The goal is not maximum complexity. It is the best coherent experience
for the actual product and its users.

------------------------------------------------------------------------

# Part XXI --- Scope added in the DENT 2.0 audit (2026-11-14)

The audit of this specification against the repository and the first
benchmark (Brewlog, Antigravity + Gemini 3.8 Flash High, scored 37
without DENT vs 35 with DENT) found gaps that Parts I--XX do not cover: video production, narration
and music, dimensionality (1D--3D), enforced gates, self-scoring,
attribution, the override clause, hero typography and the test
protocol. This part adds them; where it touches Parts XII--XIV it
extends them rather than replacing them.

## 50. Lessons from the first benchmark (enforce, don't advise)

The DENT run still shipped:

1.  Horizontal overflow on phones (page 444 px wide on a 390 px screen).
2.  Invented social proof (user counts, ratings, percentages) and a real
    person's name as a placeholder.
3.  Unlabeled inputs in an interactive demo.
4.  Three combined styles where one base + one accent is allowed.
5.  The category cliché (coffee → espresso brown, orange, serif), the
    same as the run without DENT.
6.  A copy typo ("Target Target").

Each becomes a **gate**: a named step in a procedure that the agent must
pass and report, plus an automated check where possible
(`scripts/verify_page.py`). Prose rules alone failed.

## 51. Guidance for weak models, freedom for strong ones

-   Assume the executing model is capable but literal. No design decision
    is left unguided: every deliverable type gets a recipe (ordered
    steps, decisions, minimum bars, gates, examples).
-   Recipes are defaults, not ceilings. A strong model may override a
    Convention, recipe default, pairing or composition when it has a
    better idea, and logs it as `Override` with the reason. Rules
    (accessibility, honesty, legal) are never overridden.
-   Closeout includes an **attribution report**: which decisions came
    from DENT (file and section), which from the user, and which from
    the agent's own judgment.

## 52. Self-scoring and the improve loop

-   After building, the agent scores its own work with a scorecard derived
    from the request: requirements coverage first, then design, usability,
    accessibility, function, distinctiveness, and motion, sound or video
    quality when in scope. 0--10 per line, with evidence for every score.
-   Missing evidence caps a score (unverified → max 6).
-   Below target (default: overall ≥ 8, no line < 6) the agent lists the
    three highest-impact improvements; `/dent:improve` executes them and
    re-scores.
-   Self-scores are not benchmark results; benchmarks still need human or
    independent review (§22.5).

## 53. Creative direction depth

-   A large, opinionated **directions library**: named concepts that each
    define type, color, layout, imagery, motion and sound, the products
    they fit and the clichés they avoid.
-   A **category-cliché check**: name the predictable look for the
    product's category and diverge on at least two axes unless the user
    asks for the expected look.
-   A **hero typography system**: headline composition techniques (scale,
    cropping, stacking, mixed faces, variable axes, masks, outlines,
    kinetic reveals) with code recipes and accessibility rules.
-   Reason-based anti-slop detection (§18) extended to motion, sound and
    video ("whoosh on every cut", "stock corporate ukulele", "random
    particles").

## 54. Component and library intelligence (extends Part XII)

A sourced catalogue that separates accessible primitives, complete styled
systems, copy-and-customize collections, specialized components,
animation runtimes, and templates or paid products. Each entry: name,
URL, frameworks, role, styling, accessibility, licence (and paid tiers),
strengths, weaknesses, use when, avoid when, and status (checked date or
"verify"). Plus a selection method: detect stack → list needs →
shortlist → compare (compatibility, a11y, customization, performance,
licence, maintenance, design fit) → recommend with trade-offs → one
library per job → verify it works.

## 55. Motion graphics and visual experience (extends Part XIII)

-   Distinguish interface motion, motion graphics, interactive graphics,
    3D experiences, product animation, data animation and generative art.
-   Dimensions: 1D (text, lines, timelines, tickers, waveforms), 2D
    (vector, raster, canvas), 2.5D (layers, parallax, isometric, depth
    cards), 3D (real-time WebGL/WebGPU, pre-rendered), XR.
-   Craft: concept → storyboard → animatic → timing → build → polish;
    animation principles; kinetic typography; transitions; loops; scroll
    storytelling; particles; shaders; data animation.
-   Technology catalogue with selection rules (CSS → WAAPI → Motion → GSAP
    → Lottie/Rive → Canvas/PixiJS → Three/R3F → shaders), licences, costs.
-   Motion system (durations, easings, springs, staggers, choreography),
    reduced-motion alternatives, performance budgets, verification
    (play-through, sync, cleanup, frame rate, reduced motion).

## 56. Audio: every kind of sound (extends Part XIV)

-   UI sound, sonic identity/logo, motion-graphics SFX, ambience,
    interactive/procedural audio, music (scored, licensed, generated),
    **narration and voice-over** (scripting, casting, recording, TTS and
    AI voice, pronunciation, pacing, captions and transcripts), audio
    description, podcasts, spatial audio, audio visualization, haptic
    pairing.
-   Technology and asset catalogue (Web Audio, Tone.js, Howler, analysis,
    waveform, spatial, TTS engines, music and SFX sources, DAWs) with
    software licences kept separate from asset licences.
-   Rules: never autoplay; opt-in, mutable, never required; visual
    equivalents; loudness targets; verification of autoplay handling,
    mute, sync, cleanup and failure.

## 57. Video production

-   Types and sub-types: launch (teaser, reveal, feature tour,
    manifesto), trailer, explainer (animated 2D, kinetic type,
    whiteboard, screencast, UI-led, 3D, hybrid), product demo, tutorial,
    social short, app-store preview, title sequence, data story, case
    study, event sizzle, brand film, lyric/music video, ads (6 s, 15 s,
    30 s).
-   Pipeline: brief → message → script → storyboard → animatic → voice →
    build → sound → captions → render → QA → deliver.
-   Tool selection: if the user has generative-video access (Veo, Sora,
    Runway, Kling, Luma…) ask whether to use it for footage; otherwise
    code-based video (HyperFrames, Remotion, Motion Canvas, Revideo,
    Manim), editors (DaVinci Resolve, Kdenlive, Shotcut, Blender) and
    FFmpeg. Check licences (e.g. Remotion's company licence above three
    people).
-   Platform specs (aspect ratios, durations, safe areas, captions,
    loudness) and verification (frame checks, sync, captions, export).

## 58. Commands added beyond §5

`/dent:components`, `/dent:directions`, `/dent:type`,
`/dent:motion-graphics`, `/dent:3d`, `/dent:sound`, `/dent:voice`,
`/dent:video`, `/dent:launch-video`, `/dent:brand`, `/dent:assets`,
`/dent:copy`, `/dent:verify`, `/dent:score`, `/dent:improve`,
`/dent:handoff`.

## 59. Testing protocol

Every capability is tested by running DENT on a real prompt and
recording: agent, model, settings, the exact prompt, **every question the
agent asked and the answer chosen**, the output, verification results,
the agent's self-score, an independent score, and failures. Showcase
pieces (DENT's own landing page, a motion-graphics piece about DENT, an
explainer video with narration) are produced this way and published on
the README.

# DENT Intelligence Upgrade Specification

## Turning DENT into a smarter, more reliable product-design and frontend-engineering agent

**Document type:** Implementation specification\
**Audience:** The AI coding agent responsible for upgrading the DENT
repository\
**Primary objective:** Improve DENT's reasoning, decision-making,
execution, verification, and learning---not merely increase the number
of design rules, styles, libraries, or reference files.

------------------------------------------------------------------------

## 1. Mission

Upgrade DENT into a context-aware, production-minded design and
frontend-engineering system that can understand a product, make
defensible design decisions, implement them cleanly, and verify the
result through real evidence.

DENT must behave less like a collection of prompts and more like a
coordinated engineering workflow. It should:

1.  Understand the user's actual goal and the existing project before
    making changes.
2.  Select an appropriate workflow and effort level based on context,
    complexity, risk, and uncertainty.
3.  Make deliberate product, UX, visual-design, architecture, and
    implementation decisions.
4.  Use existing project conventions and suitable libraries instead of
    introducing unnecessary dependencies.
5.  Implement the requested outcome without damaging unrelated
    functionality.
6.  Run the application and inspect the rendered result whenever the
    environment permits.
7.  Test functionality, responsiveness, accessibility, and engineering
    quality independently.
8.  Identify defects, fix the highest-impact ones, and verify the fixes.
9.  Preserve important project decisions and design-system consistency
    across sessions.
10. Report what was actually verified, what was not verified, and any
    remaining risks honestly.

**Core principle:** DENT should know not only *what* tools, styles,
libraries, and techniques exist, but *when, why, and how* to use them.

------------------------------------------------------------------------

## 2. Mandatory repository-first approach

Before changing anything, inspect the complete repository and understand
its current architecture.

### 2.1 Audit scope

Inspect, where present:

-   Main skill entrypoint and `SKILL.md`.
-   Every slash command and command-specific instruction.
-   All reference documents and their cross-references.
-   Templates, examples, scripts, configuration, and supporting assets.
-   Existing design-system and project-memory mechanisms.
-   Existing planning, audit, implementation, and verification
    workflows.
-   Evaluation rubrics, benchmarks, test cases, and sample outputs.
-   Any integration with browser, screenshot, testing, or development
    tools.

Do not assume that a capability described in documentation is
implemented or usable. Trace each important capability to its actual
instructions, scripts, tools, or demonstrated workflow.

### 2.2 Audit deliverables

Create an audit that records:

  -----------------------------------------------------------------------
  Field                               Required content
  ----------------------------------- -----------------------------------
  Capability                          What DENT claims or is expected to
                                      do

  Current implementation              Where and how it is implemented

  Evidence                            Relevant file, command, script, or
                                      test

  Defect                              Missing, contradictory, redundant,
                                      vague, or unreliable behaviour

  Impact                              Critical, high, medium, or low

  Recommendation                      Specific change required

  Acceptance test                     How the change will be verified
  -----------------------------------------------------------------------

Identify duplicate rules, conflicting instructions, oversized
references, dead documentation, missing links, unclear ownership, and
workflows that cannot be executed with available tools.

Do not rewrite the repository before completing this audit and proposing
an implementation plan.

------------------------------------------------------------------------

## 3. Intelligence architecture

Organise DENT around six cooperating disciplines. These may be
implemented as separate commands, reference modules, or clearly defined
workflow stages; do not create unnecessary abstractions or force a
complex software architecture into a prompt-based skill.

### 3.1 Context and decision engine

Responsible for understanding the task and choosing the right process.

It must establish:

-   User intent and expected deliverable.
-   Whether the task is new creation, redesign, audit, extension,
    implementation, or design-system adoption.
-   Existing application stack, architecture, conventions, and
    dependencies.
-   Existing functionality that must be preserved.
-   Product category, target users, key user tasks, and relevant
    constraints.
-   Complexity, implementation risk, uncertainty, and verification
    requirements.
-   Whether clarification is genuinely necessary.

The engine should distinguish between: - **Known facts:** directly
observed in the repository or explicitly provided by the user. -
**Assumptions:** reasonable but unverified interpretations. -
**Unknowns:** information that could materially change the
implementation. - **Constraints:** requirements that must not be
violated.

Never present assumptions as facts. Ask concise clarification questions
only when proceeding would create a meaningful risk of implementing the
wrong thing. Otherwise, state the assumption and continue.

#### Workflow selection

Retain DENT's existing modes and effort levels where they are useful.
Improve their selection logic rather than replacing them automatically.

Select the workflow dynamically based on: - Task type. - Number of
affected screens or components. - Architectural impact. - Visual
complexity. - Data and interaction complexity. - Accessibility and
security implications. - Risk of regression. - Available tools and
verification capability.

Effort levels must change the depth of investigation, planning,
implementation, and verification---not merely the length of the
response.

A small, isolated fix should not trigger an unnecessarily heavy process.
A high-impact product redesign must not be treated as a quick styling
task.

### 3.2 Product and UX intelligence

DENT must understand the product and the user's tasks before designing
its interface.

Evaluate, when relevant:

-   Product purpose and value proposition.
-   Primary user groups and their goals.
-   Information architecture and navigation.
-   Core user journeys and task completion.
-   Content hierarchy and information density.
-   Discoverability and cognitive load.
-   First-use, returning-user, empty, loading, success, and error
    states.
-   Permissions and role-specific experiences.
-   Validation, recovery, and destructive actions.
-   Responsive and touch interaction needs.

For data-heavy interfaces, identify the decisions users need to make
from the data before choosing charts, cards, filters, or layout.

For forms, consider field grouping, labels, validation timing, error
recovery, keyboard flow, and submission feedback.

For dashboards, prioritise meaningful information and workflows over
decorative metrics and arbitrary card grids.

Do not invent product requirements. Infer cautiously from the repository
and user request, and document important assumptions.

### 3.3 Design intelligence

Move beyond selecting a named aesthetic preset.

DENT should reason about the interaction of:

-   Visual hierarchy.
-   Composition and layout.
-   Typography, pairing, scale, and readability.
-   Color relationships and contrast.
-   Spacing, rhythm, and density.
-   Shape language, borders, surfaces, and elevation.
-   Imagery, iconography, and illustration.
-   Brand personality and product context.
-   Motion and interaction feedback.
-   Platform and audience expectations.

Use existing style references as a source of vocabulary and inspiration,
not as rigid templates.

#### Creative direction process

For substantial design work:

1.  Understand the product, audience, and content.
2.  Identify the desired brand personality and experience.
3.  Establish a small number of coherent visual directions internally or
    present alternatives when the user would benefit from choosing.
4.  Evaluate each direction against product fit, usability,
    distinctiveness, feasibility, accessibility, and consistency.
5.  Select and document a direction.
6.  Translate it into reusable design tokens and component rules.
7.  Apply the system consistently across the experience.

Avoid generic AI-generated visual patterns, including unnecessary
gradients, excessive glassmorphism, arbitrary glowing effects,
repetitive rounded cards, decorative charts, and oversized hero
typography when they do not serve the product.

A design must be distinctive because of its considered composition and
details, not because it uses more effects.

### 3.4 Frontend engineering intelligence

Treat implementation quality as a first-class requirement.

DENT should reason about:

  -----------------------------------------------------------------------
  Area                                Expected behaviour
  ----------------------------------- -----------------------------------
  Architecture                        Respect existing structure,
                                      component boundaries, and
                                      separation of concerns

  Components                          Prefer composable, reusable
                                      components where reuse is real

  State                               Choose appropriate local, shared,
                                      server, URL, and persistent state

  Data                                Handle loading, errors, empty
                                      states, validation, and stale data

  Type safety                         Preserve and improve the project's
                                      type guarantees

  Performance                         Avoid unnecessary renders,
                                      dependencies, large assets, and
                                      blocking work

  Responsive behaviour                Build content-driven layouts that
                                      adapt to real viewport constraints

  Accessibility                       Use semantic elements, keyboard
                                      support, focus management, and
                                      accessible names

  Security                            Avoid unsafe rendering, exposed
                                      secrets, weak validation, and
                                      insecure defaults

  Maintainability                     Prefer clear, idiomatic code over
                                      clever or excessively abstract
                                      solutions

  Testing                             Add or update tests proportionate
                                      to the changed behaviour
  -----------------------------------------------------------------------

Support the project's actual stack. Do not assume React or Next.js if
the repository uses something else.

Before introducing a dependency: 1. Check whether the project already
has an appropriate solution. 2. Check compatibility with the installed
framework and versions. 3. Consider bundle size, maintenance,
accessibility, licensing, and customisation. 4. Explain why the
dependency is justified. 5. Avoid adding a library for a trivial feature
that can be implemented safely with existing primitives.

Do not rewrite unrelated architecture simply because another approach is
preferred.

### 3.5 Visual and functional verification intelligence

Verification must be evidence-based and separate from implementation
claims.

When browser or runtime tools are available, DENT should:

1.  Start the application using the project's existing scripts.
2.  Confirm that it actually runs.
3.  Open the relevant route or workflow.
4.  Inspect the rendered interface.
5.  Capture screenshots at representative viewport sizes.
6.  Exercise important interactions.
7.  Inspect browser and runtime errors where available.
8.  Fix defects and repeat the relevant checks.

At minimum, consider: - Small mobile viewport. - Typical mobile
viewport. - Tablet or intermediate viewport. - Desktop viewport. - Wide
desktop where layout complexity warrants it.

Do not claim browser verification, screenshot inspection, or interaction
testing unless it actually happened.

If browser tooling is unavailable, perform the strongest available
static and automated checks, explicitly state the limitation, and do not
fabricate visual-verification results.

#### Visual inspection checklist

Inspect for: - Broken or inconsistent hierarchy. - Typography scale and
line-length problems. - Spacing and alignment inconsistencies. -
Clipping, overflow, and unexpected wrapping. - Inconsistent component
dimensions. - Weak contrast or unreadable content. - Poor responsive
behaviour. - Missing assets or incorrect image crops. - Inconsistent
states and interaction feedback. - Accidental changes outside the
intended scope.

Visual review should assess the actual rendered page, not only source
code.

### 3.6 Independent quality evaluation

Separate the implementation process from final evaluation.

Use three distinct review perspectives:

**Visual evaluator** - Composition and hierarchy. - Typography and
spacing. - Color and contrast. - Consistency and brand fit. - Responsive
rendering. - Distinctiveness and polish.

**UX evaluator** - Task completion. - Navigation and discoverability. -
Interaction clarity. - Content quality and information architecture. -
Empty, loading, success, and error states. - Keyboard and
assistive-technology usability.

**Engineering evaluator** - Correctness and regression risk. -
Architecture and maintainability. - Type safety and error handling. -
Performance. - Security. - Test quality.

Where the available agent/tool environment permits, evaluators should
inspect the implementation independently. At minimum, evaluate against
the original requirements and actual test/render evidence rather than
accepting the implementation agent's self-assessment.

A reviewer must be allowed to reject the work and explain why.

------------------------------------------------------------------------

## 4. Component and platform intelligence

Maintain a curated, task-oriented catalogue of relevant component
systems, primitives, and motion technologies.

Examples may include:

-   Radix UI, Base UI, React Aria, shadcn/ui.
-   Mantine, MUI, Ant Design, Chakra UI, Ark UI.
-   Aceternity UI, Magic UI, Motion Primitives.
-   Motion, GSAP, Lottie, Rive.
-   Three.js and React Three Fiber.

This list is not a requirement to install or use every library.

For each candidate, assess: - Framework and version compatibility. -
Accessibility and keyboard behaviour. - Styling and theming model. -
Customisation and composition. - Bundle and runtime cost. - Maintenance
and documentation quality. - Licensing and usage restrictions. - Fit
with the existing design system.

Prefer existing project dependencies and native platform capabilities
when they are sufficient.

Do not copy components blindly. Inspect their dependencies,
implementation, accessibility, and licensing before adopting them.

Use current official documentation when available and relevant. Treat
external examples as references, not unquestionable authority.

------------------------------------------------------------------------

## 5. Motion and interaction design

Motion should communicate state, causality, hierarchy, and
feedback---not exist solely for decoration.

DENT should define a coherent motion system for substantial interfaces:

-   Duration and easing conventions.
-   Enter and exit transitions.
-   Hover, focus, pressed, and disabled feedback.
-   Page and route transitions where appropriate.
-   Scroll-triggered motion only when it improves comprehension.
-   Staggering and sequencing.
-   Loading and progress states.
-   Reduced-motion alternatives.

Prefer transform and opacity animations when appropriate. Avoid
expensive layout or paint animations without a clear reason.

Respect `prefers-reduced-motion`. Do not make essential information or
functionality depend on animation.

Choose CSS, the project's existing motion library, GSAP, Lottie, Rive,
or 3D technologies according to actual requirements. Do not introduce
heavy motion tooling for simple transitions.

------------------------------------------------------------------------

## 6. Persistent project intelligence

Strengthen the existing project memory and design-decision mechanisms
rather than creating competing sources of truth.

Where DENT uses `DESIGN.md` or an equivalent file, make it the canonical
place for durable project-level design context.

Record only decisions that are useful across tasks:

-   Product and audience context.
-   Brand and visual direction.
-   Design tokens and typography.
-   Component conventions.
-   Navigation and interaction patterns.
-   Accessibility requirements.
-   Important technical constraints.
-   Accepted design decisions and their rationale.
-   Known exceptions and unresolved issues.

Each significant decision should include: - Decision. - Context and
reason. - Alternatives considered, where useful. - Consequences. - Date
or version when supported by the workflow.

Do not store every implementation detail or temporary thought. Update
existing records instead of creating duplicate documentation.

Before a new task, read the relevant project context. After a meaningful
change, update it and identify what changed.

------------------------------------------------------------------------

## 7. End-to-end execution workflow

Use the following workflow as the default for substantial tasks.
Simplify it for low-risk tasks.

### Phase 1 --- Understand

-   Read the request carefully.
-   Inspect the repository and relevant application routes.
-   Identify the existing stack and conventions.
-   Establish scope, constraints, and acceptance criteria.
-   Record important assumptions and unknowns.

### Phase 2 --- Decide

-   Select the task mode and effort level.
-   Identify the product and UX requirements.
-   Choose a design direction.
-   Choose implementation and verification strategies.
-   Identify dependencies, risks, and likely regressions.

### Phase 3 --- Plan

-   Break work into ordered, verifiable tasks.
-   Identify files and components likely to change.
-   Define what must remain unchanged.
-   Define acceptance criteria and tests.
-   Avoid speculative work outside scope.

### Phase 4 --- Implement

-   Follow the existing architecture unless a justified change is
    necessary.
-   Build reusable components where appropriate.
-   Implement all relevant states and interactions.
-   Preserve existing functionality.
-   Keep code and design decisions consistent.

### Phase 5 --- Verify

-   Run relevant tests, type checks, linting, and build checks.
-   Run the application where possible.
-   Inspect actual rendered output.
-   Exercise important interactions.
-   Check responsive behaviour and accessibility.
-   Review for unintended regressions.

### Phase 6 --- Improve

-   Rank defects by severity and impact.
-   Fix the highest-priority issues.
-   Avoid unnecessary redesign of already-correct areas.
-   Re-run affected checks after changes.

### Phase 7 --- Report

Provide a concise, evidence-based summary: - What changed. - Important
design and engineering decisions. - Files or areas affected. - Checks
actually run and their results. - Screenshots or routes inspected, if
available. - Known limitations and unverified areas. - Remaining risks
or follow-up work.

Never report a test as passing if it was not run. Distinguish between
passed, failed, blocked, and not run.

------------------------------------------------------------------------

## 8. Quality gates and acceptance criteria

A substantial task is not complete merely because code was generated.

Use these gates:

  -----------------------------------------------------------------------
  Gate                                Completion requirement
  ----------------------------------- -----------------------------------
  Requirement fit                     The implementation satisfies the
                                      user's actual request

  Product and UX                      Core user tasks and relevant states
                                      are considered

  Design coherence                    Visual decisions form a consistent,
                                      intentional system

  Functional correctness              Important interactions work as
                                      intended

  Responsive quality                  Relevant viewport sizes are checked

  Accessibility                       Semantic structure, keyboard use,
                                      focus, and contrast are considered
                                      and tested where possible

  Engineering quality                 Architecture, types, errors, and
                                      dependencies are appropriate

  Performance                         No obvious avoidable performance
                                      regressions

  Regression safety                   Existing relevant behaviour remains
                                      intact

  Evidence                            Claims are backed by checks or
                                      explicitly marked unverified
  -----------------------------------------------------------------------

Use severity levels:

-   **Blocker:** Prevents core use, creates serious
    security/accessibility risk, or breaks the application.
-   **High:** Breaks an important workflow or causes a major
    visual/responsive defect.
-   **Medium:** Noticeably harms usability, consistency, or
    maintainability.
-   **Low:** Minor polish or nonessential refinement.

Do not hide blockers behind a high aggregate score. A critical failure
must remain visible even if other dimensions score well.

### Definition of done

A task may be marked complete only when: 1. The agreed scope is
implemented. 2. Relevant existing functionality is preserved or
intentionally changed. 3. Applicable automated checks have been run. 4.
Relevant visual and interaction checks have been performed when tools
permit. 5. High-severity defects are resolved or explicitly disclosed.
6. Unverified areas and limitations are reported honestly.

------------------------------------------------------------------------

## 9. Benchmarking and measurable improvement

Create or improve a reproducible benchmark suite that evaluates DENT on
representative tasks.

Include task categories such as: - New landing page creation. - Existing
landing page redesign. - Complex dashboard design. - Multi-step form. -
Responsive navigation. - Design-system adoption. - Existing component
extension. - Accessibility remediation. - Visual bug fixing. - Frontend
refactoring without visual regression. - Product workflow
implementation.

For every benchmark, preserve: - Original prompt and constraints. -
Starting repository or fixture. - Expected behaviours and acceptance
criteria. - Test commands and environment. - Screenshots at defined
viewports where applicable. - Evaluation rubric. - Results and known
limitations.

Measure at least:

  Dimension               What to measure
  ----------------------- ------------------------------------------------
  Requirement adherence   Required features and constraints satisfied
  Visual quality          Independent review of rendered output
  UX quality              Task success and interaction clarity
  Accessibility           Automated findings plus manual checks
  Engineering quality     Tests, types, maintainability, and correctness
  Responsiveness          Layout and behaviour across viewports
  Performance             Relevant build/runtime measurements
  Regression              Existing behaviour preserved
  Efficiency              Time, tool calls, and unnecessary changes

Where feasible, compare: - DENT with its previous version. - DENT with
the upgraded version. - A baseline agent or workflow without DENT.

Keep the task, starting state, environment, and evaluation criteria
consistent. Do not claim improvement based on a different or easier
benchmark.

Use independent human review or a separate evaluator where possible.
Automated scores are useful signals, not proof of design quality.

Do not publish benchmark claims until the results are reproducible and
the methodology is documented.

------------------------------------------------------------------------

## 10. Reference and instruction architecture

Keep the skill usable and efficient.

-   Keep the main skill file focused on routing, core principles, and
    workflow orchestration.
-   Move detailed specialist guidance into focused reference files.
-   Load only the references needed for the current task.
-   Avoid duplicating the same rule across multiple files.
-   Establish one canonical location for each policy.
-   Ensure every referenced file exists and is discoverable.
-   Resolve contradictory instructions explicitly.
-   Prefer concise, executable guidance over long collections of generic
    advice.
-   Include examples only when they clarify decisions or expected
    behaviour.

Do not create a new reference file for every idea. Group related
guidance into a maintainable structure.

If a new capability is added, update the relevant command, routing
instructions, reference, and benchmark together.

------------------------------------------------------------------------

## 11. Safety, scope, and reliability rules

DENT must:

-   Never overwrite or delete user work without a clear reason and
    appropriate permission.
-   Inspect the impact of destructive or broad changes before executing
    them.
-   Avoid exposing secrets, credentials, or private data.
-   Avoid introducing untrusted scripts or dependencies without
    inspection.
-   Respect software, asset, font, icon, and component licences.
-   Never invent API capabilities, test results, browser observations,
    or benchmark outcomes.
-   Preserve user-requested constraints even when another approach
    appears aesthetically preferable.
-   Prefer minimal, targeted changes when they satisfy the task.
-   Explain meaningful trade-offs instead of silently making risky
    assumptions.

------------------------------------------------------------------------

## 12. Implementation requirements for the coding agent

The agent implementing this specification must follow these
instructions.

### 12.1 Do not blindly rewrite DENT

First audit the current repository. Preserve strong existing
capabilities, commands, references, conventions, and working
integrations.

This document is an upgrade specification, not permission to discard the
current architecture.

### 12.2 Resolve conflicts deliberately

If this specification conflicts with existing DENT instructions: 1.
Identify the exact conflict. 2. Determine whether the existing rule is
stronger, more specific, or required by the runtime. 3. Prefer the rule
that best satisfies the mission while respecting hard constraints. 4.
Update all affected documentation so only one clear instruction remains.
5. Record important architectural decisions.

Do not silently retain contradictory rules.

### 12.3 Implement working capabilities

Do not satisfy this specification by adding headings or aspirational
claims to `SKILL.md`.

For each proposed capability: - Identify its execution path. - Implement
or update the required command, reference, script, or workflow. -
Connect it to the main skill's routing. - Add a practical test or
benchmark. - Document tool limitations and fallback behaviour.

If a capability depends on a tool that is unavailable, describe the
fallback and mark the capability as unavailable in that environment. Do
not pretend it works.

### 12.4 Maintain compatibility

-   Preserve existing command names unless a change is justified.
-   Update all references when paths or names change.
-   Avoid unnecessary dependencies.
-   Follow the repository's existing conventions.
-   Keep the skill modular and progressively disclosed.
-   Ensure the main entrypoint remains concise enough to route tasks
    effectively.

### 12.5 Work in controlled stages

Use this implementation sequence:

**Stage A --- Audit** - Inspect the full repository. - Build the
capability and conflict matrix. - Identify what already works. -
Identify gaps and redundant material.

**Stage B --- Architecture and plan** - Design the updated workflow. -
Define ownership of each instruction and reference. - Map each
requirement to concrete files and tests. - Prioritise changes by impact
and dependency.

**Stage C --- Core intelligence** - Improve context understanding and
workflow selection. - Improve product/UX and design reasoning. - Improve
frontend engineering guidance. - Strengthen persistent project context.

**Stage D --- Execution and verification** - Improve browser/render
inspection workflows where supported. - Add independent evaluation
perspectives. - Improve quality gates and honest reporting. - Add
practical fallbacks for unavailable tools.

**Stage E --- Benchmarks and cleanup** - Add or update benchmark
fixtures and rubrics. - Test commands and reference loading. - Resolve
contradictions and broken links. - Remove redundant or obsolete
instructions. - Validate the complete workflow from the main entrypoint.

Do not start a later stage while critical blockers from an earlier stage
remain unresolved. If the environment prevents a stage, document the
blocker and continue only where safe.

------------------------------------------------------------------------

## 13. Required final deliverables

When the upgrade is complete, provide:

1.  **Repository audit:** What existed, what worked, and what was
    missing.
2.  **Architecture summary:** The updated intelligence and execution
    model.
3.  **Change inventory:** Files added, modified, renamed, or removed,
    with reasons.
4.  **Capability traceability matrix:** Each requirement mapped to its
    implementation and verification.
5.  **Benchmark report:** Reproducible results, methodology, and
    limitations.
6.  **Verification report:** Commands run, outcomes, and anything not
    tested.
7.  **Known limitations:** Tool dependencies, unsupported scenarios, and
    remaining risks.
8.  **Usage guide:** How to invoke the improved workflows and commands.

### Required traceability matrix

  -----------------------------------------------------------------------
  Requirement       Implementation    Verification      Status
                    location                            
  ----------------- ----------------- ----------------- -----------------
  Context-aware     Exact             Test or benchmark Pending
  decisions         file/command                        

  Product and UX    Exact             Test or benchmark Pending
  reasoning         file/command                        

  Design            Exact             Test or benchmark Pending
  intelligence      file/command                        

  Frontend          Exact             Test or benchmark Pending
  engineering       file/command                        

  Visual            Exact             Test or benchmark Pending
  verification      file/command                        

  Independent       Exact             Test or benchmark Pending
  evaluation        file/command                        

  Project memory    Exact             Test or benchmark Pending
                    file/command                        

  Benchmark suite   Exact             Reproducible run  Pending
                    file/command                        
  -----------------------------------------------------------------------

Replace every placeholder with actual repository paths and evidence. Do
not mark a requirement complete merely because documentation mentions
it.

------------------------------------------------------------------------

## 14. Final instruction

Take ownership of making DENT materially smarter and more reliable.

Do not optimise for the number of files, rules, commands, styles,
libraries, or features added. Optimise for better decisions, stronger
execution, fewer regressions, distinctive and usable interfaces,
maintainable code, and verifiable results.

**The desired outcome is a DENT that understands the product, chooses
the right approach, designs with intent, engineers with discipline,
evaluates independently, and improves through evidence.**

Start with the repository audit. Present the findings and implementation
plan before making broad architectural changes. Then implement the
approved plan completely, test it, and report the evidence.

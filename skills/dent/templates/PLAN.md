# Implementation Plan: <project / task>

> DENT plan (Advanced/Critical depth). Delete sections that genuinely don't apply; write "N/A" rather than leaving blanks.
> Depth: <Advanced | Critical> · Effort: <Essential | Standard | Polished | All-out> · Date: <yyyy-mm-dd>

## 1. Objective
- Goal:
- User problem:
- Expected outcome:

## 2. Scope
### Included
-
### Excluded
-

## 3. Existing system (facts)
- Framework / router / build:
- Styling and token source:
- Component library / icons / fonts:
- Screens and shared components touched:
- Behaviour that must not change:
- Available assets (and licences):
- Constraints (platform, performance, legal, time):

**Confirmed:** … · **Assumed:** … · **Unknown:** …

## 4. Requirements
| ID | Requirement | Priority (Must/Should/Could) | Acceptance criterion (observable) |
|---|---|---|---|
| R-01 | | Must | |

## 5. Experience
- Information architecture / sections:
- Screens and primary flows:
- Navigation:
- Key interactions:

## 6. Creative direction
- Concept sentence:
- Mood words / anti-words:
- Category cliché (named) and how we diverge (≥ 2 axes):
- Base style + accent (max one):
- Signature element(s):
- Typography (display / text / mono) and hero type move:
- Color roles and modes:
- Layout, density, grid:
- Imagery / illustration / 3D:
- Motion (interface + any motion graphics):
- Sound (on/off; palette; narration):

## 7. Technical strategy
- Components (reuse / extend / new):
- Web platform (Modern Web Guidance): browser-support policy; MWG guides per capability; native elements chosen (see references/modern-web-guidance.md):
- Libraries (one per job, licence, why, why not native — see catalog/component-selection.md):
- State and data flow:
- Persistence, error handling:
- Media pipeline (motion, audio, video tools):

## 8. States and edge cases
Loading · Empty · Error · Success · Offline · Permissions · Validation · Long content · 0/1/many · No JS / no motion / muted

## 9. Accessibility and responsive behaviour
Keyboard · Focus management · Semantics · Screen reader · Contrast (all themes) · Reduced motion · Sound alternatives · Breakpoints and touch

## 10. Phases
| Phase | Tasks | Depends on | Completion criteria |
|---|---|---|---|
| 1 | | | |

## 11. Verification
| Requirement / gate | Method (tool) | Expected result |
|---|---|---|
| R-01 | | |
| G2 Layout | verify_page.py at 320–1440 | No overflow |
| G13 Modern Web Guidance | MWG guides cross-checked + verify_page.py | MANDATORY rules and fallbacks met |

## 12. Risks and trade-offs
| Risk | Likelihood / impact | Mitigation |
|---|---|---|

## 13. Plan audit
| # | Finding | Severity (Blocker/Major/Minor/Obs.) | Resolution |
|---|---|---|---|

## 14. Definition of done
- [ ] All Must requirements implemented and verified
- [ ] Applicable gates G1–G13 Passed (or reported)
- [ ] `### Modern Web Guidance` disclosure written for web code
- [ ] Scorecard ≥ target, or gaps reported with next steps
- [ ] DESIGN.md / licences updated

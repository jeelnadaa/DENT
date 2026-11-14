# Deviations from ANSWERS.md

Batch run on 2026-11-14 (Claude Code desktop app, Claude Opus 5.5). Each run was a fresh session started from a coordinating session, with its working folder set to `<test>/without` or `<test>/with`, and the PROMPT.md text pasted word for word.

This file lists every place where a run did not get the brief that ANSWERS.md specifies, so the without/with comparison can be read fairly. Sources: each run's `QA.md` and, where noted, the session transcript.

## Setup notes that apply to several tests

- **The DENT plugin stayed installed for the without runs.** The plugin could not be turned off per session, so the only thing keeping DENT out was the prompt's own line ("Do not use the DENT skill/plugin…").
- **01 and 02 were started with a note to the agent:** "This is a benchmark run. The task above is the complete instruction set…".
  - The 02 with-DENT run read this as a non-interactive run and skipped all of DENT's questions. In its words: "This is a non-interactive benchmark run, so I'll use DENT's documented defaults and skip the questions."
  - From 03 on, the note was changed to say that the user is present and will answer questions.
  - The 01 prompt itself says "don't ask me any questions", so 01 is not affected.
- **The 02 with-DENT run's `/dent` command did not show the skill's text.** The agent found and read SKILL.md itself. This may be worth checking in the plugin.
- **03 with-DENT hit one API network error** (ENOTFOUND) partway through. It was retried with "Try again" and then finished.
- **Without-run QA.md files are blank.** Their question tables were never filled in. The 04 without transcript was checked and shows no questions asked; the others were not checked.

## Per test

| Test | Run | What ANSWERS.md says | What was given | Effect |
|---|---|---|---|---|
| 01-brewlog | both | Prompt says no questions | No questions asked | None |
| 02-saas-dashboard | with | Effort Standard; light and dark with a toggle; density Comfortable | No questions asked, so DENT used its defaults (Standard effort) | Questions skipped because of the coordinator's wording; effort matches |
| 03-checkout-flow | with | **Effort: Standard** | **All out** | Much larger scope and a higher score target |
| 03-checkout-flow | with | Anything else: the option marked Recommended | Market: **India** (not marked Recommended); sound: **opt-in subtle sounds** (not marked Recommended); direction: **C · Quiet showroom** (the log doesn't show which option was marked Recommended) | Content and features differ from the without run |
| 04-project-app | with | **Effort: Polished** | **Standard (Recommended)** | Lower effort than intended |
| 04-project-app | with | — | DESIGN.md was only written after delivery, in answer to a follow-up question (Q3). There is no SCORECARD.md | Missing artefact |
| 05-scroll-story-launch | with | **Sound: No** | **Optional ocean sound, off** | A feature the without run doesn't have |
| 05-scroll-story-launch | with | Never give design feedback | Q2: "A · Tide Almanac, **and use Satoshi font for body text**", which led to an extra font-loading question (Q3) | Design feedback given |
| 05-scroll-story-launch | with | Anything else: the option marked Recommended | Pricing: **bracketed placeholder plans**; currency: **Indian rupees** (neither marked Recommended) | Content differs |
| 06-meditation-sound | with | **Effort: Polished** | **All-out** | Much larger scope and a higher score target |
| 06-meditation-sound | with | Anything else: the option marked Recommended | Breathing patterns: **Presets + custom**; extras: **all four** (remember settings, session log, vibration, keep awake). Neither was marked Recommended | Extra features |
| 06-meditation-sound | with | — | No SCORECARD.md was written | Missing artefact |
| 07-3d-product-viewer | with | **Effort: Polished** | **All-out** | Much larger scope; scored about 8.6 against the All-out target of 9 |
| 07-3d-product-viewer | with | Never give design feedback; style: the option marked Recommended | Q9: "**A + B** … lamp little realistic … joints realistic … one font Satoshi, one grotesque". Q10 then chose Cabinet Grotesk | Design feedback given; a combined direction instead of the Recommended one |
| 07-3d-product-viewer | with | Anything else: the option marked Recommended | Price, specs and buy button: **plausible sample values**; sound: **opt-in switch click**. Neither was marked Recommended | Extra features |
| 08-launch-video | with | **Narration: No (music + on-screen captions)** | **Music + synthetic voice-over** (a Piper neural voice was downloaded; narrator "Cori", UK female) | Different audio from the without run |
| 08-launch-video | with | **Aspect ratios: 16:9 and 1:1** | **16:9 + 9:16** | Different deliverables (the without run made 16:9 + 1:1) |
| 08-launch-video | with | Effort not listed, so the option marked Recommended | **All-out** | Much larger scope; scored 8.4 against the All-out target of 9 |
| 08-launch-video | with | Never give design feedback | Q8: "A with the default normal font should be Satoshi"; Q3: "use demo links, not placeholders"; Q2: "choose features that you think can be the best" | Design feedback given |
| 08-launch-video | without | Music: free, with a commercial-use licence, source and licence written in a file | The without run's music source and licence file was not checked | Verify before scoring |

## Summary

- **Effort level differs from ANSWERS.md in 5 with runs:** 03, 06, 07 and 08 were set to All-out, and 04 to Standard. In 02, effort was left to DENT's default because its questions were skipped; it happens to match.
- **Design feedback was given in 3 with runs:** 05, 07 and 08 (a Satoshi font request each time).
- **Feature or format differences that make the outputs not directly comparable:** 03 (India market, sound), 05 (sound), 07 (sound, pricing), 08 (narration, 9:16 instead of 1:1).
- **Runs closest to the intended protocol:** 01 (both), 02 without, and all the without runs. Their QA.md tables are blank; only 04 without was confirmed to have no questions.
- **Missing DENT artefacts:** 04 has no SCORECARD.md and wrote DESIGN.md only after being asked; 06 has no SCORECARD.md.

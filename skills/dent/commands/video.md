# /dent:video

Produce any video: explainer, trailer, product demo, tutorial, social short, title sequence, data story.

**Usage:** `/dent:video <what video>` (also `/dent video …` or `dent video …`)
**Default depth:** Advanced. Effort level and the gates in SKILL.md §3 always apply.
**Web code:** if this command writes, changes or reviews HTML, CSS or client-side JS, Google's Modern Web Guidance is the primary authority for how it is built: run `references/modern-web-guidance.md` §2 (search → retrieve → apply → verify → disclose) before coding; MWG wins any implementation conflict with DENT.

## Load
- `references/video/video-types-and-craft.md`
- `references/video/video-tools-and-pipeline.md`
- `references/audio/voice-and-narration.md`
- `templates/VIDEO.md`

## Steps
1. Ask (one at a time, if unknown): type and platform, length, sound/narration, and **whether the user has generative video/image/voice access** (Veo, Sora, Runway, Kling, ElevenLabs…).
2. Brief → one message → script (read it aloud with a timer) → storyboard → animatic. Get the script approved.
3. Pick tools: generative if available and wanted; otherwise code-based (HyperFrames, Remotion, Motion Canvas, Revideo, Manim) or an editor; check licences.
4. Build, add voice/music/SFX, captions; render per platform spec.
5. QA with the VIDEO.md checklist (ffprobe, loudness, sync, captions, safe areas).

## Output
VIDEO.md, the rendered video(s), captions, licence table, QA results.

## Never
- Invent footage of the product doing things it can't.
- Use music without a licence.

Close with the scorecard summary, attribution (DENT / MWG / user / agent judgment / overrides), the `### Modern Web Guidance` disclosure if guides shaped the code, and a one-line next step (SKILL.md §8).

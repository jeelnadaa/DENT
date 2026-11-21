# /dent:launch-video

Make a product launch video end to end (teaser, reveal, feature tour or manifesto).

**Usage:** `/dent:launch-video <product>` (also `/dent launch-video …` or `dent launch-video …`)
**Default depth:** Advanced. Effort level and the gates in SKILL.md §3 always apply.
**Web code:** if this command writes, changes or reviews HTML, CSS or client-side JS, Google's Modern Web Guidance is the primary authority for how it is built: run `references/modern-web-guidance.md` §2 (search → retrieve → apply → verify → disclose) before coding; MWG wins any implementation conflict with DENT.

## Load
- `references/video/video-types-and-craft.md` §2 (launch)
- `references/video/video-tools-and-pipeline.md`
- `references/motion/motion-graphics.md`
- `references/audio/sound-design.md`
- `templates/VIDEO.md`

## Steps
1. Run `python scripts/doctor.py`. Ask the launch sub-type: teaser (10–20 s), reveal (30–45 s), feature tour (60–90 s) or manifesto (45–90 s); platforms; and where footage, voice and music come from (references/media-sourcing.md §2).
2. One message + hook in the first 2 seconds + proof (real product UI) + CTA.
3. Script, storyboard (shot list with durations), animatic; sonic logo or music bed.
4. Build with the chosen tool; real UI captures or faithful recreations only.
5. Narration (if any) through the voice command: blind A/B, `tts.py say` → `tts.py post`; sync to narration.timing.json.
6. Export 16:9 + 9:16 (+1:1) cuts, captions, thumbnail; QA.

## Output
Launch video files per platform, thumbnail, captions, VIDEO.md.

## Never
- Show features that don't exist.
- Bury the product name until the end.

Close with the scorecard summary, attribution (DENT / MWG / user / agent judgment / overrides), the `### Modern Web Guidance` disclosure if guides shaped the code, and a one-line next step (SKILL.md §8).

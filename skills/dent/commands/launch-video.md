# /dent:launch-video

Make a product launch video end to end (teaser, reveal, feature tour or manifesto) with an original direction.

**Usage:** `/dent:launch-video <product>` (also `/dent launch-video …` or `dent launch-video …`)
**Default depth:** Advanced. Effort level and the gates in SKILL.md §3 always apply.
**Web code:** if this command writes, changes or reviews HTML, CSS or client-side JS, Google's Modern Web Guidance is the primary authority for how it is built: run `references/modern-web-guidance.md` §2 (search → retrieve → apply → verify → disclose) before coding; MWG wins any implementation conflict with DENT.

## Load
- `references/video/video-creative-direction.md`
- `references/video/video-types-and-craft.md` §2–2b (launch, product truth)
- `references/video/video-tools-and-pipeline.md`
- `templates/video-kit/README.md`
- `references/audio/sound-design.md`
- `templates/VIDEO.md`

## Steps
1. Run `python scripts/doctor.py`. Ask the launch sub-type: teaser (10–20 s), reveal (30–45 s), feature tour (60–90 s) or manifesto (45–90 s); platforms; and where footage, voice and music come from (references/media-sourcing.md §2).
2. Ask the video creative menu (video-creative-direction.md §2) for what the user wants in typography, motion language, graphics, sound and what they never want.
3. Write the three answers (what is it, what does it do for me, how do I get it) and plan ≥ 60 % of screen time on the real product or its real output (video-types-and-craft.md §2b).
4. Invent 2–3 directions as film bibles with style frames; user picks; originality guard; 2–3 escalation moves; aim for the launch sub-type's bar (§5).
5. Script, storyboard, animatic; hook in the first 2 seconds with sound off; name by ~9 s; CTA held ≥ 2 s.
6. Build from templates/video-kit/ (engine + invariants; replace every placeholder with the bible); real UI captures or faithful reenactments only.
7. Narration (if any) through the voice command: blind A/B, `tts.py say` → `tts.py post`; sync to narration.timing.json; score and SFX on the timing grid.
8. Stills contact sheet → full render → export 16:9 + 9:16 (+1:1), captions, thumbnail → `python scripts/video_qa.py` passes → look at its sheet → score honestly.

## Output
Launch video files per platform, thumbnail, captions, VIDEO.md with the chosen bible and guard result, video_qa results.

## Never
- Show features that don't exist.
- Bury the product name until the end.
- Copy DENT's own launch film (dot, letterpress strike, wall of templates, split-flap, numbered 'It asks' chapters).

Close with the scorecard summary, attribution (DENT / MWG / user / agent judgment / overrides), the `### Modern Web Guidance` disclosure if guides shaped the code, and a one-line next step (SKILL.md §8).

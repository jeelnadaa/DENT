# /dent:video

Produce any video (explainer, trailer, product demo, tutorial, social short, title sequence, data story) with an original direction and measured craft.

**Usage:** `/dent:video <what video>` (also `/dent video …` or `dent video …`)
**Default depth:** Advanced. Effort level and the gates in SKILL.md §3 always apply.
**Web code:** if this command writes, changes or reviews HTML, CSS or client-side JS, Google's Modern Web Guidance is the primary authority for how it is built: run `references/modern-web-guidance.md` §2 (search → retrieve → apply → verify → disclose) before coding; MWG wins any implementation conflict with DENT.

## Load
- `references/video/video-creative-direction.md` (menu, film bibles, originality guard, genre bar, escalation)
- `references/video/video-types-and-craft.md`
- `references/video/video-tools-and-pipeline.md`
- `templates/video-kit/README.md` (engine + quality invariants)
- `references/audio/voice-and-narration.md`
- `templates/VIDEO.md`

## Steps
1. Run `python scripts/doctor.py`. Ask (one at a time, if unknown): type and platform, length, and where each kind of media comes from (references/media-sourcing.md §2), saying where real or generated assets would lift the video.
2. Ask the video creative menu (video-creative-direction.md §2): gate question first, then only the groups the user wants (feel, typography incl. custom lettering, motion language, graphics and imagery, sound, never).
3. Brief: one message, the three answers for products (video-types-and-craft.md §2b), and the bar for this genre (video-creative-direction.md §5).
4. Invent directions as film bibles (§3: 2 at Polished, 3 at All-out, 1 + an alternative at Standard), each with one rendered style frame and differing on at least four axes; the user picks or combines. Run the originality guard (§4): no DENT launch-film devices, no genre clichés, differ from earlier films. Choose 2–3 escalation moves (§6).
5. Script (read aloud with a timer) → storyboard → animatic. Get the script approved.
6. Decide how it is made (video-tools-and-pipeline.md §1: render / capture / generate / hybrid). For code-built films copy templates/video-kit/, keep its engine and quality invariants, replace every placeholder with the bible (§7 maps each choice to a technique); render through a browser engine, never OS raster text with system fonts.
7. Build, add voice (`tts.py say` → `tts.py post`, synced to narration.timing.json), score and SFX on the timing grid, captions; render per platform spec.
8. Review a contact sheet of stills before the full render; then `python scripts/video_qa.py <film> --captions <srt> --sheet <jpg>` must pass (colour range, sync, loudness, frozen time, longest hold) and you look at the sheet. Score against the genre bar; self-review is never called independent; sound not heard by a person scores <= 6.

## Output
VIDEO.md (brief, chosen bible, guard result), the rendered video(s), captions, licence table, video_qa results.

## Never
- Reuse DENT's launch-film devices or the kit's placeholder scenes as the film's look.
- Invent footage of the product doing things it can't.
- Use music without a licence.
- Present a film that video_qa.py fails without saying so.

Close with the scorecard summary, attribution (DENT / MWG / user / agent judgment / overrides), the `### Modern Web Guidance` disclosure if guides shaped the code, and a one-line next step (SKILL.md §8).

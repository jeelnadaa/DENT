# Voice, Narration and Voice-over

Narration makes explainers, launch videos, tutorials and product tours land. A great script with a clear, well-paced voice beats any visual effect. Used by `/dent:voice`, `/dent:video`, `/dent:launch-video`.

---

## 1. Ask first (one at a time, only if unknown)
1. Voice type: human (user records or hires) or synthetic (TTS)? Which service do they have (ElevenLabs, OpenAI TTS, Google, Azure, Amazon Polly, Apple/Android system voices) or should DENT use a free engine?
2. Language, accent, gender presentation (or "neutral"), age range, energy.
3. Tone (calm expert, warm friend, energetic launch, documentary).
4. Where it plays (video with music, product walkthrough, accessibility read-aloud).

## 2. Write for the ear
- Pace: **140–160 words per minute** for explainers (≈ 2.5 words/s); 120–140 for complex topics; 160–180 for energetic launches.
- Length: count words → time. 60 s ≈ 150 words. Read it aloud with a timer before producing anything.
- Short sentences (≤ 15 words), one idea each. Active voice. Contractions. Concrete nouns.
- Front-load the point: the first sentence says what the viewer gets.
- Write numbers how they're spoken ("forty-one styles", "version two point oh"), and spell out symbols.
- Signpost structure ("Three things happen. First…").
- Leave room for visuals: pauses `[pause 0.5s]` where the picture needs to speak.
- Script format: two columns (VO | visual) or the table in `templates/VIDEO.md` §3.

**Explainer script skeleton (60–90 s):** hook (problem in one line) → stakes (why it matters) → introduce the product (one sentence) → how it works (3 steps) → proof (real, specific) → call to action.

## 3. Pronunciation and delivery marks
- A pronunciation guide: product names, acronyms (spell "D-E-N-T" or say "dent"?), technical terms, people's names (ask them).
- TTS: use the engine's SSML or phoneme features (`<phoneme>`, `<say-as>`, `<break time="400ms"/>`, `<emphasis>`), or respell phonetically ("Kokoro" → "koh-KOH-roh").
- Mark emphasis on the one word per sentence that carries meaning; mark breaths at commas and line ends.

## 4. Recording (human voice)
- Quiet, soft-furnished room (closet with clothes works); mic 15–20 cm, slightly off-axis; pop filter.
- Record 48 kHz / 24-bit WAV; peaks around −12 dBFS; 10 s of room tone at the start.
- Multiple takes per paragraph; slate each take.
- Edit: remove mouth clicks and long breaths (keep natural ones), consistent pacing.
- Process (light): high-pass ~80 Hz → gentle de-ess → compression 2–3:1 → limiter; noise reduction sparingly.
- Free tools: Audacity, Ardour, Reaper (affordable licence), DaVinci Resolve Fairlight.

## 5. Synthetic voice (TTS and AI voice)
| Option | Quality | Licence/terms | Notes |
|---|---|---|---|
| ElevenLabs, OpenAI TTS, Google Cloud TTS, Azure Neural TTS, Amazon Polly | High | Provider terms per plan (commercial use, disclosure) | Only with the user's account; record the plan's terms |
| Kokoro (82M) | Good, natural for size | Model Apache-2.0 (✓ 2026-11-14) | Runs locally; check each voice pack |
| Piper | Fast, decent | Active repo GPL-3.0 (✓ 2026-11-14); output audio is yours, GPL affects distributing modified code | Many voices with their own licences, so check each voice |
| Coqui XTTS-v2 | Good, voice cloning | Model under CPML (non-commercial) — verify | Not for commercial use without a licence |
| Web Speech API (`speechSynthesis`) | System voices, varies by OS | Browser/OS | Great for in-product read-aloud, not for produced videos |

Rules:
- **Never clone or imitate a real person's voice without their documented consent.** Don't imitate celebrities.
- Disclose synthetic voices where the platform or law requires it.
- Fix pronunciations, add pauses, and re-generate weak lines; listen to everything end to end.
- Pick one voice per product/series for consistency.

## 6. Mixing narration
- Voice is the priority: music ducked −8 to −12 dB under speech (sidechain or keyframes); SFX never mask words.
- Loudness targets (integrated): **−14 LUFS** for most social/streaming video platforms, **−16 LUFS** for web/podcast-style audio, broadcast −23/−24 LUFS (EBU R128 / ATSC A/85); true peak ≤ −1 dBTP. Check the destination's current spec.
- Measure with FFmpeg: `ffmpeg -i in.wav -af loudnorm=I=-14:TP=-1:LRA=11:print_format=summary -f null -`

## 7. Captions and transcripts
- Captions for every narrated video (burned-in for social where sound is often off, plus sidecar `.srt`/`.vtt` for players).
- ≤ 42 characters per line, ≤ 2 lines, 1–6 s on screen, break at phrase boundaries, sync to speech within ~100 ms.
- Transcript published next to the video (accessibility + SEO).
- Generate drafts with speech-to-text (e.g. Whisper, open-source MIT), then correct by hand.

## 8. Audio description
If the video conveys essential information only visually (on-screen text without narration, actions), provide an audio-described version or an extended text description.

## 9. Verify
Listen fully on headphones and a phone speaker; check pronunciation guide items; loudness measured; captions synced and spell-checked; transcript matches final audio; licences/consent recorded.

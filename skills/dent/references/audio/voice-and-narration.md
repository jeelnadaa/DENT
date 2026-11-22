# Voice, Narration and Voice-over

Narration makes explainers, launch videos, tutorials and product tours land. A great script with a clear, well-paced voice beats any visual effect. Used by `/dent:voice`, `/dent:video`, `/dent:launch-video`.

---

## 1. Ask first (one at a time, only if unknown)
1. **Where the voice comes from** (`../media-sourcing.md` §2): a local model (free, private; DENT installs it after asking), a free cloud tier, a paid provider or connector they use (any provider, listed or not: DENT looks it up), or a human recording. Run `python scripts/tts.py engines` first so the options match what is installed and what the machine can run.
2. **Commercial use?** It decides which models qualify (Voxtral open weights and Coqui XTTS are non-commercial; Kitten TTS 2 has revenue and funding thresholds).
3. Language, accent, gender presentation (or "neutral"), age range, energy.
4. Tone (calm expert, warm friend, energetic launch, documentary).
5. Where it plays (video with music, product walkthrough, accessibility read-aloud).

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

Default order when the user says "you decide" and the use is commercial: **Qwen3-TTS** (GPU) → **Chatterbox** (GPU, slowed with `post --tempo 0.85`) → **Kokoro** (CPU) → **Kitten TTS 2** (CPU; check its licence thresholds) → Piper or system voices only for drafts and timing. This order comes from DENT's measured comparison and a blind listening test (§5.5). Before producing a whole script, offer a **blind A/B** of 2–3 engines on one real line (`tts.py compare`): taste in voices is personal and samples are cheap.

### 5.1 Engines DENT can drive (`scripts/tts.py`)
| Engine | Tier | Sounds like | Licence / commercial | Status |
|---|---|---|---|---|
| [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) (1.7B / 0.6B) | Local, GPU | The most natural local option in DENT's test; steerable by instruction; voice design from a description | Apache-2.0 / yes | ✓ 2026-11-21 (rendered on an 8 GB laptop GPU) |
| [Kitten TTS 2](https://github.com/KittenML/KittenTTS) | Local, CPU or GPU | Expressive presets, 20 languages; handles numbers and acronyms well, but the lowest signal quality in DENT's test (audible artefacts) | Stellon Labs Community Licence: commercial only under USD 1M revenue and 1M funding, after registering, with a "Powered by Stellon Labs" credit | ✓ 2026-11-21 |
| [Chatterbox](https://github.com/resemble-ai/chatterbox) | Local, GPU | Most expressive pitch and best word accuracy in DENT's test, but rushes (~220 wpm): slow it with `post --tempo 0.85`; English-first | MIT / yes (Perth watermark in output) | K |
| [Voxtral TTS](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603) | Local (large GPU, served by vLLM, `http` engine) or Mistral API | Very natural; open weights have fixed reference voices only | Weights CC BY-NC 4.0 (no commercial use); commercial through Mistral's paid API | ✓ 2026-11-21 |
| [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) | Local, CPU | Clean and intelligible but the flattest delivery in DENT's test; runs on CPU | Apache-2.0 / yes | ✓ 2026-11-14 |
| [Piper](https://github.com/OHF-Voice/piper1-gpl) | Local, CPU | Synthetic; drafts and offline read-aloud | GPL-3.0 engine; per-voice licences | ✓ 2026-11-14 |
| System voices (SAPI, `say`, espeak-ng) | Built-in | Robotic | OS terms | — |
| [OpenAI text-to-speech](https://platform.openai.com/docs/guides/text-to-speech) | Paid API | Instruction-steerable delivery | Provider terms; disclose AI voice | K |
| [ElevenLabs](https://elevenlabs.io) | Free plan (non-commercial) / paid | Top-tier expressiveness, voice design | Paid plans for commercial use | K |
| [Coqui XTTS-v2](https://github.com/coqui-ai/TTS) | Local | Good cloning | CPML: non-commercial | K |

Google Cloud TTS, Azure AI Speech, Amazon Polly, Cartesia, Hume, Fish Audio, Mistral's API and any other provider: free tiers or paid plans, provider terms; research them with §5.6 before use.

### 5.2 Using `tts.py` (agent guidelines)
1. **Check:** `python scripts/tts.py engines` lists installed engines, the GPU, licences and which API keys are set.
2. **Install only after a yes:** `python scripts/tts.py install <engine>` prints the commands, download size and licence and exits without installing. After the user agrees, run it again with `--yes`. Each engine gets its own virtual environment under `DENT_TTS_HOME` (default `~/.dent/tts`); model weights download on first use. If installation fails, say so and offer the next option.
3. **Write the script** one line per caption-sized thought; put pauses inline as `[pause 0.4]`. Respell hard names as `{shown|spoken}`: `{passkey|pass-key}` puts "passkey" in the captions and speaks "pass-key", so respellings never leak into captions.
4. **Sample first:** `python scripts/tts.py compare --engines qwen3,chatterbox,kokoro --text "<the hook line>" --out vo/ab` makes anonymised `sample_A.wav`… and a `KEY.json`; let the user listen before revealing the key.
5. **Render:** `python scripts/tts.py say --engine <engine> --script vo.txt --out vo/lines [engine options]` writes `line_001.wav`, its `.txt`, and `engine.json` (settings for reproducibility; keep `--seed` fixed).
6. **Master and caption:** `python scripts/tts.py post --in vo/lines --out vo/narration.wav --lufs -16 --srt vo/narration.srt --vtt vo/narration.vtt` trims silences, places lines with a fixed gap, high-passes, normalises loudness in two passes (−16 LUFS web, −14 social video, −23 broadcast; true peak ≤ −1.5 dBTP) and writes balanced captions (≤ 42 characters × 2 lines) plus `narration.timing.json` for syncing visuals. It prints PASS or FAIL against the loudness target.
7. **Check what was said:** `python scripts/tts.py check --in vo/lines` transcribes every line with faster-whisper (CPU by default; `DENT_STT_DEVICE=cuda` for the GPU) and reports the word error rate plus **inserted, dropped and replaced words** per line, writing `check.json`. It fails a line at WER > 0.15 or two or more inserted or dropped words. Read the replaced words: that is where names go wrong. Install with `tts.py install whisper` (after a yes).
8. **Listen to every line** on headphones and a phone speaker. Regenerate only weak lines with `say --line N` (same script, new `--seed`), then re-run `post`.
9. **Sync to picture:** `python scripts/tts.py words vo/narration.wav --out vo/words.json` gives word timestamps to put picture events on; `post --at 0.4,3.1,7.8` places each line at a chosen time instead of a fixed gap (or list lines in the timeline's `"vo"` block and let the video kit's `templates/video-kit/score.py` place them).

### 5.3 Per-engine tips
- **Qwen3-TTS.** Three modes. `--voice <preset>` (CustomVoice; presets aiden, dylan, eric, ono_anna, ryan, serena, sohee, uncle_fu, vivian) with `--instruct "warm, unhurried, smiling"` for delivery. `--design "<describe the voice>"` without `--voice` (VoiceDesign: invent a voice from words, e.g. "a calm female voice in her 40s, low pitch, slight rasp, documentary pacing"). `--ref clip.wav --ref-text "<transcript>"` (Base: cloning, only with documented consent). `--model 0.6B` for 4 GB GPUs; `--lang English` avoids accent drift on short lines. Lines of 8–25 words sound best; very short lines can rush, so join them or add `[pause]`.
- **Kitten TTS 2.** `--voice <preset>`: 115 character presets (the list prints on every run). For narration start with `AudiobookNarratorFemale` (the default), `NewsAnchorFemale`, `FrenchDocumentary`-style documentary reads, or named voices such as `Julian`, `Eleanor`, `Marcus`; avoid novelty presets (`AirportAnnouncer`, `BoredTeenager`) unless the concept calls for them; punctuation and fillers ("—", "…", "?!", "umm") shape delivery; `--ref` for cloning (5–30 s, one speaker, consent). CPU works but is slower than real time on laptops.
- **Chatterbox.** `--exaggeration 0.3–0.5` for narration, 0.7+ for energetic launches; `--ref` sets the voice. It speaks fast (about 3.6 words/s ≈ 220 wpm in DENT's test) and lowering `--cfg` to 0.3 barely changed that (3.5 words/s), so master with `tts.py post --tempo 0.85` (≈ 2.9 words/s) or split long lines with `[pause]`. English is strongest.
- **Kokoro.** `--voice af_heart` or another voice ID; its first letter sets the language (`a` US English, `b` UK English…); `--speed 0.95` for calmer reads.
- **Voxtral.** Commercial: Mistral's paid API, through your own adapter (§5.6) or the `http` engine where the endpoint is OpenAI-compatible. Non-commercial local: serve it with vLLM on a large GPU and call `--engine http --base-url http://localhost:8000/v1 --key-env <VAR>`.
- **OpenAI, ElevenLabs, http.** The user sets `OPENAI_API_KEY`, `ELEVENLABS_API_KEY` or the variable named by `--key-env` themselves. Estimate the cost from the character count and confirm before running.

### 5.4 Pronunciation traps every engine shares
Acronyms and invented names are the main failure in DENT's test: "WCAG" came out as "Quag" (Qwen3-TTS) and "WAG" (Chatterbox); "Tidewater" as "Tide water" or "Tied water" (Kokoro). Respell them in the script before rendering ("W-C-A-G", "Tide-water"), keep a pronunciation list (§3), and check every name with `tts.py check` before mastering.

### 5.5 How DENT ranked the local engines (2026-11-21)
Four contrasting lines (calm explainer, energetic launch, numbers and acronyms, a question) rendered by each engine with its default narrator voice on an RTX 3070 Ti Laptop GPU, then measured. Pace target for narration: 2.3–2.7 words/s (140–160 wpm).

| Engine | Signal quality (SQUIM PESQ / SI-SDR) | Pitch variation (semitones SD) | Pace (words/s) | Word error rate (Whisper small.en) | Blind listening rank (maintainer) | DENT rank |
|---|---|---|---|---|---|---|
| Qwen3-TTS 1.7B, voice `ryan` + instruction | **3.97 / 28.3 dB** (cleanest) | 4.3 | **2.6** (on target), natural pauses | 6.1 % (homophones; "WCAG") | 1 | **1** |
| Chatterbox | 3.95 / 24.0 dB | **4.9** (most expressive) | 3.6 (too fast; 2.9 with `--tempo 0.85`) | **3.4 %** | 2 | **2** |
| Kokoro-82M, `af_heart` | 3.75 / 24.3 dB | 2.7 (flattest) | 2.9 | 6.7 % ("Tied water") | 3 | **3** |
| Kitten TTS 2, `AudiobookNarratorFemale` | 3.34 / 24.4 dB (artefacts) | 3.4 | 2.3 | 4.9 % | 4 | **4** |

SQUIM's predicted MOS (4.3–4.4 for all four) was too saturated to separate the engines and is not used. The word error rates are mostly homophones (write/right, too/two), so intelligibility is effectively equal; the ranking rests on signal quality, delivery and the blind listening test, which agreed. Re-run the comparison when engines update: `tts.py compare` for the listening test, and measure before changing this order.

### 5.6 Any other provider
Follow `../media-sourcing.md` §4: read the official API docs; confirm pricing, licence and voice-consent terms; write a short adapter that saves `line_001.wav`, `line_001.txt`… (one per script line) into a folder; test one line; then run `tts.py post` on the folder. Record provider, model, voice and settings.

Rules:
- **Never clone or imitate a real person's voice without their documented consent.** Don't imitate celebrities.
- Disclose synthetic voices where the platform or law requires it.
- Fix pronunciations, add pauses and regenerate weak lines; listen to everything end to end.
- One voice per product or series; record engine, model, voice, seed and settings so new lines match later.

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
Listen fully on headphones and a phone speaker (never report a voice as good without listening; say which lines you heard); check pronunciation guide items; loudness measured (`tts.py post` prints it); captions synced and spell-checked; transcript matches final audio; licences/consent recorded.

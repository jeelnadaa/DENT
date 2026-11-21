# Media Sourcing: local, free cloud, paid cloud, any provider, or your own assets

Every time DENT needs media it did not draw in code (voice, music, sound effects, images, illustration, video footage, 3D models, fonts, upscaling, captions), **where it comes from is the user's decision**, not a silent default. This file is the one protocol for that decision. Used by `/dent:voice`, `/dent:sound`, `/dent:video`, `/dent:launch-video`, `/dent:assets`, `/dent:brand`, `/dent:3d`, `/dent:motion-graphics`, `/dent:create` (imagery at Polished+), `/dent:doctor`, and the All-out capability list (`workflow/all-out.md` §0).

Status: ✓ checked on the date shown · K from knowledge, verify before relying on it · ⚠ caveat. Prices, free tiers and licences change monthly: **re-check the official page before recommending a provider for commercial use.**

---

## 1. The rule [Rule]
1. **Ask once per media type per project, before producing it.** Batch related media into one question when you can ("voice and music"). Record the answer in the Decision Log (Source `User`) and in DESIGN.md so later commands don't ask again.
2. **Every option the user can pick has three tiers plus two escapes:** a local model (free, private), a free cloud tier, a paid cloud provider, **any provider not listed** (the user names it; DENT researches it, §4), and **their own assets** (recordings, photos, footage, brand files). "You decide" is always allowed: then use the best option that needs no account and no money (normally local, else code-generated), and say so.
3. **Never** spend money, create accounts, accept terms, or handle API keys or passwords on the user's behalf. The user creates the account and sets the key as an environment variable (or connects the provider as a connector/MCP server) themselves; DENT reads it from the environment. Never ask the user to paste a secret into chat, never print it, never write it into a committed file.
4. **Licence before use:** confirm the model's or provider's terms allow the intended use (commercial? attribution? voice consent? output ownership?) and record it in the licence table (gate G12). A model whose weights are non-commercial (CC BY-NC, Coqui CPML, Stellon Community above its thresholds) is offered only with that warning.
5. **Show the cost before spending.** For a paid provider estimate the cost of the job (characters, seconds, images, credits) and get a yes before the first paid call.
6. **Verify the output like any other work:** listen/look at every result; generated media gets the same QA as hand-made media (loudness, sync, artefacts, hands/text in images, licence).

## 2. The question (one per media type, 4 options + free answer)
Use the question tool. Adapt the labels to the media type and what `/dent:doctor` found (a GPU, installed engines, connected tools).

> **Where should the <voice-over / music / images / footage / 3D models> come from?**
> 1. **Local model, free (Recommended when the machine can run it)**: runs on this computer, private, no account. I'll install it if it isn't installed (I'll show the download size first).
> 2. **Free cloud tier**: better or faster for some media, needs a free account and has limits.
> 3. **Paid provider or connector you use**: ElevenLabs, OpenAI, Google, Runway… *or any other service, even one I don't list*: tell me which, and I'll look up how it works.
> 4. **Your own assets**: you record, shoot or upload; I'll edit, clean and integrate them.
> (Free answer: "you decide", a specific model, or a mix like "local voice, my own photos".)

Follow-ups only if needed: which engine/voice (offer 2–3 from §5 with one-line trade-offs), commercial use (yes/no: it changes which models qualify), and, for local, whether to install now.

**When real or generated assets would lift the result** (a launch video with real product footage, a landing page that needs photography, a 3D hero), say so in one line *before* the question: "Real product footage would make this much stronger than an animated mock-up; do you have some, or should I generate or build it?" Do this wherever it changes quality, not only when asked.

**Non-interactive / "don't ask":** local if it runs on the machine and its licence fits the use, otherwise code-generated (synthesis, SVG, canvas, HTML-to-video) or verified free libraries (§5). List the choice in the close-out.

## 3. Fonts follow the same pattern
Fonts are media too: *Free and open fonts (Recommended)* · *I own fonts / Adobe Fonts* · *Suggest paid fonts worth buying* · *You decide*. Method and sources: `typography.md` §0, §9.

## 4. A provider DENT doesn't list (or "find me a free one")
When the user names an unlisted service, or says "I don't know any free model, find one":
1. **Search the official sources** (provider docs, pricing page, terms, model card, GitHub/Hugging Face repo). Prefer primary sources over listicles.
2. **Extract and show** in 4–6 lines: what it produces and its quality evidence (official samples, independent comparisons if any), API or local install, auth method, price or free quota, licence/commercial terms and content policy, output format, limits (rate, length, languages), hardware needs if local.
3. **For "find a free one":** shortlist 2–3 candidates that (a) allow the intended use under their licence, (b) run on the detected hardware (`/dent:doctor`) or have a genuine free tier, (c) are maintained (release in the last ~12 months). Recommend one with the trade-offs. Don't invent quality claims; cite where they come from or say they are unverified.
4. **Integrate:** for a local model, ask before installing (§6). For an API, the user sets the key as an environment variable; write a small adapter that calls the official SDK or REST API and writes standard files (WAV/MP3, PNG/WebP, MP4, GLB) into the project's work folder. For narration, render one WAV per line, then let `scripts/tts.py post` do loudness, timing and captions (`audio/voice-and-narration.md` §5).
5. **Test with one small sample** (one line, one image, one 3-second clip) and show it before the batch.
6. **Record** provider, model/version, settings, cost, licence and date in the Decision Log, DESIGN.md and the licence table.

## 5. Options by media type
Each table lists a few strong options per tier; it is a starting point, not a whitelist. Commercial use: **Yes**, **No** (non-commercial), or **Check** (depends on plan or thresholds).

### 5.1 Voice and narration (details and per-engine guidance: `audio/voice-and-narration.md` §5)
| Option | Tier | Notes | Commercial | Status |
|---|---|---|---|---|
| [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | Local (GPU ≥ 6–8 GB for 1.7B; 0.6B smaller) | DENT's top-ranked local voice (`audio/voice-and-narration.md` §5.5); voices from a text description, 9 preset voices with instruction control, 3-second cloning (with consent); 10 languages | Yes (Apache-2.0) | ✓ 2026-11-21 |
| [Chatterbox](https://github.com/resemble-ai/chatterbox) | Local (GPU recommended) | Emotion-exaggeration control, zero-shot cloning, watermarked output | Yes (MIT) | K |
| [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) | Local (CPU fine) | Small, fast, clean; less expressive | Yes (Apache-2.0) | ✓ 2026-11-14 |
| [Kitten TTS 2](https://github.com/KittenML/KittenTTS) | Local (CPU ~6 GB RAM, or GPU) | 1.7B ternary model, expressive presets, cloning from 5–30 s, 20 languages; Mini/Nano/Pico for tiny devices | Check: Stellon Labs Community Licence (free commercial grant only under USD 1M revenue and 1M funding, registration, "Powered by Stellon Labs" credit, revocable) | ✓ 2026-11-21 |
| [Voxtral TTS 4B](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603) | Local (large GPU) or Mistral API | Very natural; open weights limited to fixed reference voices | No for the open weights (CC BY-NC 4.0); commercial through Mistral's paid API | ✓ 2026-11-21 |
| [Piper](https://github.com/OHF-Voice/piper1-gpl) | Local (CPU, very fast) | Robotic next to the above; fallback and offline read-aloud | Yes for output; engine GPL-3.0; each voice has its own licence | ✓ 2026-11-14 |
| [Google Cloud Text-to-Speech](https://cloud.google.com/text-to-speech) | Free monthly quota, then paid | Many languages and voices | Yes (provider terms) | K |
| [Azure AI Speech](https://azure.microsoft.com/products/ai-services/text-to-speech) | Free tier (F0), then paid | Neural voices, SSML | Yes (provider terms) | K |
| [ElevenLabs](https://elevenlabs.io) | Free plan (non-commercial, attribution) / paid | Top-tier expressiveness, voice design, dubbing | Check: paid plans for commercial use | K |
| [OpenAI text-to-speech](https://platform.openai.com/docs/guides/text-to-speech) | Paid API | Steerable delivery by instruction | Yes (disclose AI voice per policy) | K |
| [Cartesia](https://cartesia.ai), [Hume](https://www.hume.ai), [Fish Audio](https://fish.audio) | Paid API (free trials) | Low latency (Cartesia), emotional control (Hume), cloning (Fish) | Check plan | K |
| Human voice | Own asset | The user or a hired voice actor records (`audio/voice-and-narration.md` §4) | Yes with a written release | — |

### 5.2 Music
| Option | Tier | Notes | Commercial | Status |
|---|---|---|---|---|
| [ACE-Step](https://github.com/ace-step/ACE-Step) | Local (GPU) | Full songs and instrumentals from text | Check the repo licence | K |
| [Stable Audio Open](https://huggingface.co/stabilityai/stable-audio-open-1.0) | Local (GPU) | Short loops, textures, beds (≤ ~47 s) | Check: Stability AI Community Licence (revenue threshold) | K |
| [MusicGen / AudioCraft](https://github.com/facebookresearch/audiocraft) | Local (GPU) | Instrumental beds | No (weights CC BY-NC) | K |
| Code synthesis (Tone.js, Web Audio, SuperCollider) | Built-in | Generative or composed beds that match the motion exactly | Yes (your output) | — |
| [Pixabay Music](https://pixabay.com/music/), [Free Music Archive](https://freemusicarchive.org), [YouTube Audio Library](https://studio.youtube.com) | Free libraries | Per-track licence; check attribution | Check per track | K |
| [Suno](https://suno.com), [Udio](https://www.udio.com), [ElevenLabs Music](https://elevenlabs.io/music), [Stable Audio](https://stableaudio.com) | Free tier / paid | Full songs; free tiers are usually non-commercial | Check plan | K |

### 5.3 Sound effects
| Option | Tier | Notes | Commercial | Status |
|---|---|---|---|---|
| Synthesis (Web Audio, Tone.js, jsfxr-style) | Built-in | UI sounds that match the brand exactly; tiny files | Yes | — |
| [Stable Audio Open](https://huggingface.co/stabilityai/stable-audio-open-1.0) | Local (GPU) | Foley and textures from text | Check (Community Licence) | K |
| [Freesound](https://freesound.org), [Kenney](https://kenney.nl/assets), [Sonniss GameAudioGDC](https://sonniss.com/gameaudiogdc) | Free libraries | Per-sound CC licences (Freesound); CC0 (Kenney); royalty-free bundle (Sonniss) | Check per sound | K |
| [ElevenLabs Sound Effects](https://elevenlabs.io/sound-effects) | Free tier / paid | Text-to-SFX | Check plan | K |

### 5.4 Images, illustration and textures
| Option | Tier | Notes | Commercial | Status |
|---|---|---|---|---|
| Code (SVG, CSS, canvas, generative) | Built-in | Diagrams, patterns, abstract art, product mock-ups from real UI | Yes | — |
| [FLUX.1 [schnell]](https://huggingface.co/black-forest-labs/FLUX.1-schnell) via ComfyUI/diffusers | Local (GPU ≥ 12 GB, quantised less) | Fast, good prompt following | Yes (Apache-2.0) | K |
| [Qwen-Image](https://github.com/QwenLM/Qwen-Image) | Local (large GPU) | Strong text rendering in images | Check the repo licence | K |
| [Stable Diffusion 3.5 / SDXL](https://huggingface.co/stabilityai) | Local (GPU) | Large ecosystem of styles | Check (Community Licence / OpenRAIL++) | K |
| [Google AI Studio (Gemini image models)](https://aistudio.google.com) | Free tier / paid API | Editing and consistent characters | Check terms | K |
| [OpenAI image generation](https://platform.openai.com/docs/guides/image-generation), [Ideogram](https://ideogram.ai), [Recraft](https://www.recraft.ai) (vectors), [Adobe Firefly](https://firefly.adobe.com), [Midjourney](https://www.midjourney.com) | Paid (some free credits) | Recraft for SVG/icons; Firefly trained on licensed data | Check plan | K |
| [Unsplash](https://unsplash.com), [Pexels](https://www.pexels.com), [Openverse](https://openverse.org) | Free stock | Real photos; check each licence; no trademarks/people misuse | Yes (per licence) | K |
| User's photos, brand files, screenshots | Own asset | Always best for product truth | Yes | — |

### 5.5 Video footage and generative video
| Option | Tier | Notes | Commercial | Status |
|---|---|---|---|---|
| Code-based video (HTML/CSS/JS → frames → FFmpeg, Remotion, Motion Canvas, Revideo, Manim) | Built-in | Precise, on-brand, real UI; DENT's default (`video/video-tools-and-pipeline.md`) | Yes (check Remotion's company licence) | K |
| [Wan 2.x](https://github.com/Wan-Video) | Local (GPU ≥ 8 GB for small models) | Text/image-to-video, short clips | Yes (Apache-2.0) | K |
| [LTX-Video](https://github.com/Lightricks/LTX-Video), [HunyuanVideo](https://github.com/Tencent/HunyuanVideo) | Local (GPU) | Fast drafts (LTX); high quality (Hunyuan) | Check each licence | K |
| [Veo](https://deepmind.google/models/veo/), [Sora](https://openai.com/sora), [Runway](https://runwayml.com), [Kling](https://klingai.com), [Luma](https://lumalabs.ai), [Pika](https://pika.art), [Hailuo](https://hailuoai.video) | Free credits / paid | Cinematic b-roll, product-in-context shots; never fake product behaviour | Check plan | K |
| [Pexels Videos](https://www.pexels.com/videos/), [Pixabay Videos](https://pixabay.com/videos/), [Mixkit](https://mixkit.co) | Free stock | Real b-roll; check licence | Yes (per licence) | K |
| Screen recordings of the real product | Own asset | The most convincing footage there is | Yes | — |

### 5.6 3D models and scenes
| Option | Tier | Notes | Commercial | Status |
|---|---|---|---|---|
| Code (Three.js primitives, procedural geometry), [Blender](https://www.blender.org) | Built-in / local | Exact control; Blender output is yours | Yes | K |
| [TRELLIS](https://github.com/microsoft/TRELLIS), [Hunyuan3D-2](https://github.com/Tencent/Hunyuan3D-2) | Local (GPU) | Image/text-to-3D | Check each licence (Hunyuan has regional terms) | K |
| [Meshy](https://www.meshy.ai), [Tripo](https://www.tripo3d.ai), [Rodin](https://hyper3d.ai) | Free credits / paid | Fast textured meshes | Check plan | K |
| [Poly Haven](https://polyhaven.com), [Kenney](https://kenney.nl/assets), [Sketchfab](https://sketchfab.com) | Free libraries | CC0 (Poly Haven, Kenney); per-model licence (Sketchfab) | Check per asset | K |

### 5.7 Clean-up, upscaling, captions
| Option | Tier | Notes | Commercial | Status |
|---|---|---|---|---|
| [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN), [rembg](https://github.com/danielgatis/rembg) | Local | Upscaling; background removal | Yes (BSD-3 / MIT) | K |
| [Whisper](https://github.com/openai/whisper) / [faster-whisper](https://github.com/SYSTRAN/faster-whisper) | Local | Speech-to-text for captions and timing | Yes (MIT) | K |
| [Demucs](https://github.com/facebookresearch/demucs) | Local | Separate voice from music in user recordings | Yes (MIT) | K |

## 6. Installing a local model (ask first) [Rule]
1. `python scripts/doctor.py` (or `tts.py engines` for voice) shows what is installed and what the machine can run.
2. If the chosen engine is missing, ask: "**<Engine>** isn't installed. Install it now? About <size> download (Python packages + model weights), into its own virtual environment at `<path>`, licence <licence>." Options: *Install it (Recommended)* · *Pick a different option* · *I'll install it myself (show me the commands)*.
3. Install into a separate virtual environment per engine (their PyTorch and Transformers pins conflict); `tts.py install <engine>` prints and, after the user's yes, runs the exact commands. Model weights download on first use into the Hugging Face cache.
4. Test one sample, then continue. If the install fails, report the error plainly and offer the next option; never claim the engine works until a sample played.

## 7. Recording the choice
Decision Log row: `| Voice source | Qwen3-TTS 1.7B (local), voice "Vivian" | User chose local; commercial OK (Apache-2.0) | User |`. Licence table row in DESIGN.md: asset, source/model + version, licence, commercial OK, attribution text, consent (voices), date.

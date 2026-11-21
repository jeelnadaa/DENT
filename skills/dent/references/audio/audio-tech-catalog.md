# Audio Technology and Tools Catalogue

Choose the simplest audio technology that does the job; one library per job. Software licences are listed here; **asset licences** (sounds, music, voices) are in `../catalog/asset-sources.md` §7–9. Status: ✓ checked 2026-11-14 · K from knowledge, verify · ⚠ caveat.

---

## 1. Selection guide
| Need | Use |
|---|---|
| Play a file on demand (video, podcast, sample) | Native `<audio>`/`<video>` with controls |
| UI sound effects (several short sounds, overlap, volume, sprites, fallbacks) | **Howler.js**, or a 30-line Web Audio helper |
| Synthesised UI sounds / musical interactions / sequencing | **Tone.js** (or raw Web Audio oscillators for 2–3 sounds) |
| Precise low-level graphs, custom DSP, effects chains | **Web Audio API** (+ **AudioWorklet** for off-main-thread processing) |
| Audio features for visuals (RMS, centroid, MFCC) | **AnalyserNode** (simple FFT) or **Meyda** |
| Music information retrieval (tempo, key, beats) | Essentia.js (⚠ AGPL) |
| Waveform display + scrubbing | **WaveSurfer.js** (or Peaks.js, ⚠ LGPL) |
| Positional 3D audio | Web Audio **PannerNode** / Three.js `PositionalAudio` / Resonance-style libraries |
| Narration | TTS engines (§4) or recorded voice |
| Video soundtracks | Editors/DAWs (§6) + FFmpeg |

## 2. Browser audio, playback and synthesis

| Tech | Role | Platforms | Strengths | Limitations | Licence | Status |
|---|---|---|---|---|---|---|
| [Web Audio API](https://developer.mozilla.org/docs/Web/API/Web_Audio_API) | Low-level audio graph: sources, gain, filters, panners, analysers, convolution | All modern browsers | Sample-accurate scheduling (`audioContext.currentTime`), full control | Verbose; autoplay policy needs user gesture to `resume()` | Web standard | ✓ |
| [AudioWorklet](https://developer.mozilla.org/docs/Web/API/AudioWorklet) | Custom DSP on the audio thread | Modern browsers | Glitch-free custom processing | Requires module + secure context | Web standard | ✓ |
| HTML `<audio>` | Simple playback | All | Controls, accessibility, streaming | Weak overlap/timing control | Standard | ✓ |
| [Howler.js](https://howlerjs.com) | Cross-browser playback + sprites + spatial basics | Browsers | Format fallback, sprites, pooling, simple API | No synthesis; maintenance slower | MIT | K |
| [Tone.js](https://tonejs.github.io) | Synthesis, effects, sequencing, transport | Browsers | Musical timing, instruments, effects | Larger; learning curve | MIT | K |
| [Pizzicato.js](https://alemangui.github.io/pizzicato/) | Simple sound + effects | Browsers | Easy effects | Little maintenance (K: verify) | MIT | K |
| [Tuna.js](https://github.com/Theodeus/tuna) | Web Audio effects (chorus, delay, phaser…) | Browsers | Drop-in effect nodes | Old but stable | MIT | K |
| [Elementary Audio](https://www.elementary.audio) | Functional, declarative audio DSP (web, native, plugins) | Web (WASM), Node, plugins | Expressive DSP graphs | Smaller community | MIT (verify current terms) | K |
| [WebAudioFont](https://github.com/surikov/webaudiofont) / SoundFont players | Sample-based instruments | Browsers | Realistic instruments | Large sample payloads | Varies (library GPL-3.0? verify) | K |
| [Web MIDI API](https://developer.mozilla.org/docs/Web/API/Web_MIDI_API) | MIDI devices | Chromium (permission) | Hardware control | Limited support | Standard | K |

## 3. Analysis and visualisation

| Tech | Role | Licence | Status |
|---|---|---|---|
| [AnalyserNode](https://developer.mozilla.org/docs/Web/API/AnalyserNode) | FFT/time-domain data | Standard | ✓ |
| [Meyda](https://meyda.js.org) | Feature extraction (RMS, spectral centroid, MFCC, chroma) | MIT | K |
| [Essentia.js](https://mtg.github.io/essentia.js/) | Music analysis (beats, key, tempo, descriptors) | **AGPL-3.0**; pre-trained models **CC BY-NC-ND** (non-commercial) | ✓ 2026-11-14 |
| [WaveSurfer.js](https://wavesurfer.xyz) | Waveforms, regions, timelines, spectrogram plugins | BSD-3-Clause | K |
| [Peaks.js](https://github.com/bbc/peaks.js) (BBC) | Waveform UI for long audio | **LGPL-3.0** | ✓ 2026-11-14 (secondary sources) |
| [audiowaveform](https://github.com/bbc/audiowaveform) | Precompute waveform data (CLI) | GPL-3.0 (tool) | K |

## 4. Voice and text-to-speech

| Tech | Role | Licence / terms | Status |
|---|---|---|---|
| Web Speech API `speechSynthesis` | In-browser read-aloud with system voices | Standard (voices are OS-provided) | ✓ |
| [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | Most natural local TTS in DENT's tests; voice design, presets, cloning (`scripts/tts.py --engine qwen3`) | Apache-2.0 code and weights | ✓ 2026-11-21 |
| [Kitten TTS 2](https://github.com/KittenML/KittenTTS) | Expressive local TTS on CPU or GPU, 20 languages (`--engine kitten2`) | Code Apache-2.0; weights Stellon Labs Community Licence (commercial only under USD 1M revenue and funding, registration, credit) | ✓ 2026-11-21 |
| [Chatterbox](https://github.com/resemble-ai/chatterbox) | Emotion-controllable local TTS and cloning (`--engine chatterbox`) | MIT; watermarked output | K |
| [Voxtral TTS](https://huggingface.co/mistralai/Voxtral-4B-TTS-2603) | Very natural 4B TTS; local via vLLM or Mistral API (`--engine http`) | Weights CC BY-NC 4.0 (non-commercial); commercial via Mistral's API | ✓ 2026-11-21 |
| [Kokoro TTS](https://huggingface.co/hexgrad/Kokoro-82M) | Small, clean open TTS model, CPU-friendly (`--engine kokoro`) | Apache-2.0 model weights | ✓ 2026-11-14 |
| [Piper](https://github.com/OHF-Voice/piper1-gpl) | Fast local TTS | Active repo GPL-3.0; original MIT repo archived Oct 2025; each voice has its own licence | ✓ 2026-11-14 |
| [Coqui TTS / XTTS](https://github.com/coqui-ai/TTS) | Open TTS + cloning | Code MPL-2.0; XTTS model CPML non-commercial (verify) | K |
| ElevenLabs, OpenAI TTS, Google Cloud TTS, Azure Speech, Amazon Polly, Cartesia, Hume, Fish Audio | Hosted TTS/voice; free tiers and paid plans (`--engine openai`, `elevenlabs`, `http`, or an adapter per `../media-sourcing.md` §4) | Commercial terms per plan | K |
| [Whisper](https://github.com/openai/whisper) / whisper.cpp | Speech-to-text for captions | MIT | K |

## 5. Spatial and 3D audio
| Tech | Notes | Licence | Status |
|---|---|---|---|
| Web Audio PannerNode (HRTF) + AudioListener | Position sources in 3D; distance models | Standard | ✓ |
| Three.js `PositionalAudio` / `Audio` | Attach sounds to 3D objects | MIT | K |
| WebXR + Web Audio | Spatial audio in XR sessions | Standard | K |
| Resonance Audio (Google) | Ambisonic spatialisation | Apache-2.0 (archived; verify) | K |

## 6. Production tools (making and editing audio)
| Tool | Use | Licence | Status |
|---|---|---|---|
| [Audacity](https://www.audacityteam.org) | Record, edit, clean, export | GPL-2.0+ | K |
| [Reaper](https://www.reaper.fm) | Full DAW, scripting | Paid licence (generous evaluation) | K |
| [Ardour](https://ardour.org) | Open-source DAW | GPL-2.0 (binaries paid/donation) | K |
| [LMMS](https://lmms.io) | Music production | GPL-2.0 | K |
| [DaVinci Resolve (Fairlight)](https://www.blackmagicdesign.com/products/davinciresolve) | Video + audio post | Free edition + paid Studio | K |
| [FFmpeg](https://ffmpeg.org) | Convert, trim, loudness normalise, mux | LGPL/GPL (build dependent) | K |
| [SoX](https://sox.sourceforge.net) | CLI audio processing | GPL/LGPL | K |
| [sfxr / jsfxr / ChipTone](https://sfxr.me) | Generate retro SFX | MIT/varies | K |

## 7. Integration with motion
- GSAP timelines: trigger sounds with `.call()` at labels; for tight sync schedule on the audio clock (`audioCtx.currentTime + offset`) rather than `setTimeout`.
- Rive: listen for state-machine events and play mapped sounds.
- Lottie: use frame events (`enterFrame`) or markers to trigger sounds; keep sound files separate.
- Video (HyperFrames/Remotion/Motion Canvas): place audio tracks in the composition timeline; render with audio; check sync in the final file.

## 8. Formats
- Web: **Opus in WebM/Ogg** (small, high quality) with **AAC/MP3** fallback for Safari where needed; WAV only for very short, latency-critical sounds or source masters.
- UI sounds: mono, 44.1/48 kHz, 64–96 kbps Opus, < 20 KB each; consider one sprite file.
- Music/ambience: stereo 128–160 kbps; stream long files, don't preload.

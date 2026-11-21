# Video Tools and Production Pipeline

From brief to delivered files, with the right tools for what the user has. Status: ✓ checked 2026-11-14 · K from knowledge, verify (tool terms change often, especially generative services).

---

## 1. First questions: where each kind of media comes from
Run `python scripts/doctor.py` (tools, GPU, installed engines, API keys present), then ask the sourcing question from `../media-sourcing.md` §2 **per media type the video needs**, batching where you can (one question for footage and images, one for voice and music):
- **Footage / imagery:** code-built scenes with real product captures (Recommended: brand-exact, free) · a local generative model · a free cloud tier · a paid provider or connector they use (Veo, Sora, Runway, Kling, Luma, Pika, Hailuo, Midjourney, Firefly… or any other: DENT looks it up) · their own footage, screenshots and photos.
- **Voice:** `../audio/voice-and-narration.md` §1 (local Qwen3-TTS / Kitten TTS 2 / Chatterbox / Kokoro, free tiers, paid providers, any provider, or a human recording).
- **Music and SFX:** `../media-sourcing.md` §5.2–5.3.

Before asking, say in one line where real or generated assets would lift this video ("A 3-second shot of the real app on a phone would make the hook land; do you have one, or should I generate or recreate it?"). If the user will record or edit themselves, give them the script, storyboard, assets and an edit plan.

Then pick the stack (§3). Record every choice, cost and licence in `templates/VIDEO.md` §2.

## 2. Pipeline
1. **Brief** (type, sub-type, audience, platform, one message, CTA, length, aspect ratios) — `video-types-and-craft.md`.
2. **Script** (VO + on-screen text + visuals, timed at ~150 wpm) → user approval.
3. **Storyboard** (shot list with durations) → **animatic** (timing locked with scratch VO).
4. **Assets:** real UI captures (Playwright screen recordings at 2× scale, or OBS), HTML recreations of UI, illustrations, 3D renders, generated footage (if allowed), fonts, music, SFX — all licensed.
5. **Voice:** record or synthesise (`../audio/voice-and-narration.md` §5: `scripts/tts.py say` → `tts.py post`), then sync scenes to `narration.timing.json`.
6. **Build scenes** in the chosen tool using DESIGN.md tokens (type, color, motion personality).
7. **Sound:** music bed (ducked), SFX on key frames, sonic logo; mix to target loudness.
8. **Captions:** burned-in for social, sidecar `.srt/.vtt`.
9. **Render** each version (16:9, 9:16, 1:1) with platform specs (§5).
10. **QA** (§6), then deliver files + thumbnail + captions + licence table.

## 3. Tools

### 3.1 Code-based video (best for agents: deterministic, editable, brand-exact)
| Tool | How it works | Best for | Licence | Status |
|---|---|---|---|---|
| [HyperFrames](https://github.com/heygen-com/hyperframes) (HeyGen) | Write HTML/CSS/JS compositions; headless Chrome seeks each frame, FFmpeg encodes MP4; designed for AI agents | Launch videos, kinetic type, UI-led explainers using web tech you already have | Apache-2.0, free at any scale, self-hosted | ✓ 2026-11-14 |
| [Remotion](https://www.remotion.dev) | React components → video; Player for web previews; Lambda rendering | React teams, data-driven/templated videos | **Free for individuals, non-profits, for-profits with ≤ 3 people; company licence beyond** | ✓ 2026-11-14 |
| [Motion Canvas](https://motioncanvas.io) | TypeScript generators + timeline editor, audio sync | Explainers, diagrams, code animations | MIT | K |
| [Revideo](https://re.video) | Motion Canvas fork for programmatic rendering/APIs | Automated video generation | MIT | K |
| [Manim Community](https://www.manim.community) | Python math/diagram animation | Technical/math explainers | MIT | K |
| [Theatre.js](https://www.theatrejs.com) + capture | Keyframe web/3D scenes, record output | 3D web scenes to video | Core Apache-2.0, Studio AGPL (dev only) | ✓ 2026-11-14 |
| Playwright video capture | Record a real web animation/product run as WebM | Real UI demos, capturing your own motion pieces | Apache-2.0 | K |
| [FFmpeg](https://ffmpeg.org) | Encode, trim, concat, overlay, captions, loudness | Every pipeline | LGPL/GPL by build | K |

### 3.2 Editors and motion tools (when a human edits, or for finishing)
| Tool | Use | Licence | Status |
|---|---|---|---|
| [DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve) | Edit, color, Fairlight audio, Fusion VFX | Free edition; Studio paid | K |
| [Kdenlive](https://kdenlive.org) | Open-source editor | GPL | K |
| [Shotcut](https://shotcut.org) | Open-source editor | GPL | K |
| [Blender](https://www.blender.org) | 3D, Grease Pencil 2D animation, compositing, video sequencer | GPL (output yours) | K |
| [OBS Studio](https://obsproject.com) | Screen recording | GPL | K |
| [Natron](https://natrongithub.github.io) | Node compositing | GPL | K |
| [Synfig](https://www.synfig.org) / [OpenToonz](https://opentoonz.github.io) | 2D animation | GPL / BSD | K |
| [Rive](https://rive.app) / [Lottie](https://lottiefiles.com) | Vector animations exported into videos or embedded | Runtimes MIT; editors with plans | K |
| After Effects, Premiere, Final Cut, CapCut | Commercial/proprietary editors | Paid / provider terms | K |

### 3.3 Generative video, image and voice (only with the user's access)
| Category | Examples | Use for | Cautions |
|---|---|---|---|
| Text/image-to-video | Google Veo, OpenAI Sora, Runway, Kling, Luma Dream Machine, Pika, Hailuo/MiniMax | Atmosphere shots, abstract b-roll, concept visuals | Never to fake product UI or features; check plan's commercial terms; consistency across shots is hard (use reference frames); label AI content where required |
| Image generation | Midjourney, Imagen, GPT-image, Flux, Stable Diffusion | Storyboard frames, backgrounds, textures, key art | Licence by plan/model; avoid living artists' styles by name |
| Voice | ElevenLabs, OpenAI TTS, Azure/Google TTS | Narration | Consent for any cloned voice; plan terms |
| Music | Suno, Udio, Stable Audio | Beds and stings | Commercial rights depend on plan; avoid imitating named artists |
| Lip-sync/avatars | HeyGen, Synthesia | Presenter videos | Never impersonate real people without consent; disclose |

## 4. Build recipes (code-based)

**HyperFrames-style approach (any HTML-to-video renderer):** build each scene as an HTML composition at the exact output size (1920×1080 / 1080×1920), drive all animation from a single time variable (GSAP timeline `seek(t)` or CSS animations with negative delays) so every frame is deterministic, put audio on the timeline, render, then check with ffprobe. Follow the tool's current docs for its composition format and CLI.

**Remotion:** `npx create-video@latest` → compositions in React using `useCurrentFrame()` + `interpolate()`/`spring()`; `<Audio>` and `<OffthreadVideo>` for media; `npx remotion render <Comp> out.mp4`. Remember the licence threshold.

**Motion Canvas:** scenes as generator functions (`yield* all(...)`), audio track in the editor for sync; render to image sequence/video.

**Capture a web animation:** Playwright `record_video_dir`, viewport = output size, `deviceScaleFactor: 2` for crisp UI; trim and encode with FFmpeg.

**Useful FFmpeg commands:**
```bash
# H.264 MP4 for web/social, high quality, fast start
ffmpeg -i in.mov -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart out.mp4
# Vertical 9:16 crop from 16:9 (center)
ffmpeg -i in.mp4 -vf "crop=ih*9/16:ih,scale=1080:1920" -c:a copy vertical.mp4
# Burn captions
ffmpeg -i in.mp4 -vf subtitles=captions.srt -c:a copy captioned.mp4
# Loudness normalise to -14 LUFS (two-pass recommended)
ffmpeg -i in.mp4 -af loudnorm=I=-14:TP=-1:LRA=11 -c:v copy out.mp4
# Poster frame at 3s
ffmpeg -ss 3 -i in.mp4 -frames:v 1 poster.jpg
# Inspect
ffprobe -v error -show_entries format=duration:stream=codec_name,width,height,r_frame_rate -of compact in.mp4
```

## 5. Platform specs (verify current specs before delivery)
| Destination | Aspect | Resolution | Length guide | Notes |
|---|---|---|---|---|
| Website hero loop | 16:9 or custom | 1920×1080 (+ 1280 variant) | 6–15 s loop | Muted, `playsinline`, poster, < 3–5 MB, pause control |
| YouTube | 16:9 | 1920×1080 or 3840×2160 | Any | −14 LUFS typical; chapters; captions file |
| YouTube Shorts / TikTok / Reels | 9:16 | 1080×1920 | 15–60 s (longer allowed) | Burned captions; safe zones; hook in 1–2 s |
| LinkedIn / X / feeds | 1:1 or 4:5 or 16:9 | 1080×1080 / 1080×1350 | 15–90 s | Most watch muted: captions |
| Product Hunt / launch pages | 16:9 | 1920×1080 | 30–90 s | Often YouTube-hosted |
| App Store preview | Device-specific portrait/landscape | Per Apple spec | 15–30 s | Captured on-device UI; strict rules |
| Google Play promo | 16:9 YouTube link | — | 30 s–2 min | — |
| GitHub README | Inline MP4 via GitHub upload, or GIF/animated SVG | ≤ 10 MB for uploads (check) | Short | No autoplay with sound; poster image fallback |

Frame rates: 24 (cinematic), 30 (UI/screen), 60 (fast UI motion/games). Keep one rate per project.

## 6. Video QA (report each)
| Check | How |
|---|---|
| File plays, correct duration/resolution/fps/codec | `ffprobe` output |
| A/V sync | Scrub key moments (clap/impact frames) |
| Loudness and peaks | `ffmpeg -af ebur128` / loudnorm summary on target; true peak ≤ −1 dBTP |
| Captions | Present, synced, spelled correctly, readable on phone |
| Message with sound off | Watch muted: still understood? |
| First 2 s hook | Watch the first 2 s only |
| Text legibility | On a phone screen, every card readable |
| Truth | Every claim, feature and number true; UI real; no unlicensed assets |
| Safe areas | Overlay platform UI guides for vertical cuts |
| Flashing | No > 3 flashes/s (check fast cuts/strobes) |
| Versions | 16:9, 9:16, 1:1 rendered as planned; thumbnail exported |
| Licences | Every asset in the licence table |

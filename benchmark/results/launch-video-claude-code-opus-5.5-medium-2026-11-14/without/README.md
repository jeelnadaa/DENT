# Quill launch video

A 45-second launch film for Quill, made for X and LinkedIn.

## Deliverables

| File | What it is |
|---|---|
| `quill-launch-16x9.mp4` | 1920×1080, 30 fps, H.264 + AAC, 45 s. Use on X and as a LinkedIn landscape post. |
| `quill-launch-1x1.mp4` | 1080×1080, same edit laid out for the square feed. This one takes up more of the screen in the LinkedIn and X mobile feeds. |
| `quill-launch.srt` | Captions. Upload this alongside the video: LinkedIn asks for SRT, and X accepts SRT. |
| `quill-launch.vtt` | The same captions as WebVTT, for web players. |

All on-screen copy is readable with the sound off, so the video works when the feed autoplays it muted. Audio is normalised to about −16 LUFS with true peak at or below −1.5 dBTP.

## Edit (scene cuts land on bar lines at 120 BPM)

| Time | Scene | On screen |
|---|---|---|
| 0–4 s | Cold open | "Every idea starts somewhere." typed on paper |
| 4–8 s | Problem | Sticky notes, stray files, 47 tabs: "Then it ends up everywhere." |
| 8–12 s | Reveal | An ink stroke gathers the scraps into the Quill logo with the line "Where your thinking lives." |
| 12–20 s | Capture | Ctrl + Shift + Space opens quick capture; the note is typed and saved into the list |
| 20–28 s | Link | Typing `[[` links to "Reader survey", then the graph view maps the connections |
| 28–36 s | Find | Searching "pricing" highlights matches across four notes and opens one |
| 36–40 s | Sync | The phone saves while offline, then syncs to the laptop |
| 40–45 s | End card | Logo, the line again, and "Available today" |

## Project files

- `src/timeline.js`: the single source of timing and copy, shared by picture and sound.
- `src/quill.html`: the canvas renderer. Open it in a browser to preview it with sound. Space plays and pauses, and the slider scrubs. Add `?w=1080&h=1080` to see the square cut.
- `src/music.js`: synthesises the score and UI sounds into `build/music.wav`. No samples or stock music are used, so there is nothing to license.
- `render.py`: drives headless Chromium frame by frame and pipes the frames to ffmpeg. `python render.py 16x9 --stills 10 22.8` writes review PNGs.
- `build.sh`: rebuilds everything.

To change the copy or the timing, edit `src/timeline.js` and run `build.sh`.

## Before posting

- The app UI, the feature set ("Ctrl + Shift + Space", `[[links]]`, graph view, offline sync) and the line "Where your thinking lives." are placeholders written for this video. Check them against the real product, then change them in `timeline.js` / `quill.html`.
- The end card says "Available today" and gives no URL. Put the link in the post text, or add one to `T.copy.cta`.
- Fonts are Georgia, Segoe UI and Segoe Print as installed with Windows. Rendering on another OS will fall back to similar fonts.

### Suggested post copy

**X:** Your ideas are scattered across sticky notes, 47 tabs and emails to yourself. Quill gives them one quiet home: capture in a keystroke, link as you write, find anything instantly. Available today. [link]

**LinkedIn:** Every idea starts somewhere, and then it ends up everywhere. Today we're launching Quill, a note-taking app built around three things: capturing a thought in a single keystroke, linking ideas as you write, and finding any note instantly. It works offline and syncs across your laptop, phone and browser. Try it today: [link]

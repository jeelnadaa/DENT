# Audio Implementation and Verification

How to ship sound that works in real browsers and never annoys or blocks anyone, and how to prove it works.

---

## 1. Architecture (web)
- **One audio manager** module: owns the `AudioContext` (created lazily), master gain, mute state, volume, loading cache, and a `play(name, opts)` API. Components never create their own contexts.
- **Unlock on gesture:** create/resume the context inside the first explicit user action that opts into sound (the sound toggle). Browsers block audio before a gesture; handle `context.state === "suspended"`.
- **Preferences:** `soundEnabled` defaults to `false` on websites; persist in `localStorage` (try/catch); expose a visible toggle with `aria-pressed` and a label ("Sound: off").
- **Respect signals:** `navigator.connection?.saveData` → don't preload; tab hidden (`visibilitychange`) → suspend ambience; reduced-motion users often also prefer fewer sensory effects: default to off and never auto-enable.
- **Loading:** fetch + `decodeAudioData` once, cache buffers; lazy-load after the toggle is turned on; sprites for many tiny UI sounds.
- **Overlap:** limit voices per sound (e.g. max 2 concurrent), debounce rapid triggers (≥ 60–100 ms), skip if the same sound played < 50 ms ago.
- **Failure:** if decoding/loading fails, log once and continue silently; the UI never depends on audio.
- **Cleanup:** stop sources, disconnect nodes on unmount/route change; `context.close()` when the app tears down audio entirely.

```js
// minimal audio manager (Web Audio, no dependency)
const sounds = { confirm: "/sfx/confirm.webm", error: "/sfx/error.webm" };
let ctx, master, buffers = {}, enabled = false, last = {};
export async function enableSound(on) {
  enabled = on; try { localStorage.setItem("sound", on ? "1" : "0"); } catch {}
  if (!on) { await ctx?.suspend(); return; }
  ctx ??= new AudioContext(); master ??= ctx.createGain(); master.gain.value = 0.6; master.connect(ctx.destination);
  await ctx.resume();
  await Promise.all(Object.entries(sounds).map(async ([k, url]) => {
    if (buffers[k]) return;
    try { buffers[k] = await ctx.decodeAudioData(await (await fetch(url)).arrayBuffer()); } catch { /* stay silent */ }
  }));
}
export function play(name, { volume = 1, detune = 0 } = {}) {
  if (!enabled || !ctx || !buffers[name]) return;
  const now = ctx.currentTime; if (now - (last[name] ?? -1) < 0.06) return; last[name] = now;
  const src = ctx.createBufferSource(), g = ctx.createGain();
  src.buffer = buffers[name]; src.detune.value = detune + (Math.random() * 40 - 20); g.gain.value = volume;
  src.connect(g).connect(master); src.start();
}
```

**Synthesised UI tone (no asset, no licence):**
```js
export function tone(freq = 660, dur = 0.09) {
  if (!enabled || !ctx) return;
  const o = ctx.createOscillator(), g = ctx.createGain(), t = ctx.currentTime;
  o.type = "triangle"; o.frequency.setValueAtTime(freq, t);
  g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(0.2, t + 0.005); g.gain.exponentialRampToValueAtTime(0.0001, t + dur);
  o.connect(g).connect(master); o.start(t); o.stop(t + dur + 0.02);
}
```

## 2. Native platforms
- iOS: respect the silent switch for UI sounds (use the ambient audio session category); system sounds and haptics via UIFeedbackGenerator; never interrupt the user's music for UI sounds.
- Android: use `SoundPool` for short effects, respect media/notification volume streams and Do Not Disturb.
- Pair sounds with haptics deliberately (`../platforms-and-devices.md` §6).

## 3. Sync with motion and video
- Schedule on the audio clock: `src.start(ctx.currentTime + offset)` and start the animation from the same reference; for GSAP, use labels and `.call(() => play("hit"))` at the impact frame.
- Long sequences: drive the animation from the audio's `currentTime` (audio as master clock) to avoid drift.
- Video: mux audio and check sync in the rendered file (§4).

## 4. Verification (do not claim audio works because a library is installed)

| Check | How | Pass when |
|---|---|---|
| No autoplay | Load page fresh; `verify_page.py` flags autoplaying media and AudioContexts running before any gesture | Nothing audible or running before the user opts in |
| Opt-in works | Click the sound toggle, trigger events | Sounds play; toggle state and label update |
| Mute/volume | Toggle off mid-playback; change volume | Silence immediately; volume applies to all sounds |
| Persistence | Reload | Preference restored (and never auto-on for first visit) |
| Overlap | Trigger rapidly 20× | No distortion, stacking capped |
| Failure | Block audio requests (DevTools) / rename a file | UI still works, no errors shown to users |
| Muted equivalence | Turn sound off and complete every task | Every sound had a visual equivalent |
| Sync | Record screen + audio, step frames | Sound within ~1 frame of the visual key frame |
| Loudness | `ffmpeg -i file -af ebur128 -f null -` or loudnorm summary | On target; true peak ≤ −1 dBTP; UI sounds quieter than voice |
| Mobile | iOS Safari + Android Chrome (or emulation + note limits) | Unlocks on tap; silent switch respected on native |
| Cleanup | Navigate away/back several times | No duplicate sounds, no growing node count, context not duplicated |
| Accessibility | Captions/transcripts present for speech; no sudden loud sounds | Pass |

Can't test real devices? Say so; test in desktop browsers with emulation and list it as a limitation.

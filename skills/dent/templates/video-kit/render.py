#!/usr/bin/env python3
"""DENT video kit renderer: HTML composition -> frames (headless Chromium) -> MP4 (FFmpeg).

  python render.py stills --ratio 16x9 --times 0.5 3.4 7.2      # review frames -> out/stills/ (+ labelled contact sheet)
  python render.py stills --every 1                             # one still per second of the whole film (cheap, catches most bugs)
  python render.py video  --ratio 16x9 --draft                  # fast check: 30 fps, half size, no motion blur -> out/draft-16x9.mp4
  python render.py video  --ratio 16x9 --from 8 --to 14         # re-render one stretch only -> out/range-16x9-8-14.mp4
  python render.py video  --ratio 16x9                          # final: out/film-16x9.mp4 (+ out/score.wav if present)
  python render.py stills --page styleframes --times 0 1 2      # any page that defines window.render(t) and window.READY

Page contract: a page renders with this script when it sets `window.render = (t) => {...}` (deterministic in t) and
`window.READY = true` once fonts and assets are loaded. composition.html, techniques.html and styleframes.html follow it.

- Motion blur: inside timeline.json "blur" windows each frame averages SUB sub-frames across a 180° shutter.
- Colour: frames are full-range screenshots; the encode converts to TV-range yuv420p BT.709 (video_qa.py checks it).
- Layout check (stills and every 0.5 s of a video): text too small for a phone, two text runs colliding, cut off by
  the frame or by a clipping parent, or inside the 9:16 zones platform UI covers (top 12 %, bottom 20 %, right action rail). Deliberate exceptions:
  data-crop (intended crop; may be toggled per frame), data-overlap-ok (deliberately layered type), data-small (deliberately small text), data-mask or
  .line on reveal masks (they clip on purpose).
- Time: a screenshot per frame (6 per frame in blur windows): budget ~1-2 min per second of 60 fps film on a laptop.
  Iterate with stills and --draft; render the final once.
Copyright 2026 Jeel Nada (solarquack). Licensed under the Apache License 2.0.
"""
from __future__ import annotations

import argparse
import functools
import http.server
import json
import subprocess
import sys
import threading
import time
from pathlib import Path

from playwright.sync_api import Error as PWError, sync_playwright

HERE = Path(__file__).resolve().parent
RATIOS = {"16x9": (1920, 1080), "9x16": (1080, 1920), "1x1": (1080, 1080)}
SUB = 6
# 9:16 safe zones (one source of truth; references/video/video-types-and-craft.md §4 uses the same numbers)
SAFE = {"top": .12, "bottom": .20, "rail_x": .86, "rail_top": .45, "rail_bottom": .85}
LAYOUT_JS = """([ratio, SAFE]) => {
  const W = innerWidth, H = innerHeight, S = Math.min(W, H), MIN = S * .016, out = [];
  const vis = (el) => { let o = 1; for (let e = el; e && e !== document.body; e = e.parentElement) {
      const cs = getComputedStyle(e); if (cs.display === 'none' || cs.visibility === 'hidden') return 0; o *= +cs.opacity; } return o; };
  // the visible part of a rect after every ancestor that clips (overflow / clip-path boxes)
  const clipped = (el, r) => { let x0 = r.left, y0 = r.top, x1 = r.right, y1 = r.bottom;
    for (let e = el.parentElement; e && e !== document.body; e = e.parentElement) {
      if (e.matches('.line, [data-mask]')) continue;                         // reveal masks clip on purpose
      const cs = getComputedStyle(e);
      if (cs.overflow !== 'visible' || cs.overflowX !== 'visible' || cs.overflowY !== 'visible') {
        const b = e.getBoundingClientRect(); x0 = Math.max(x0, b.left); y0 = Math.max(y0, b.top); x1 = Math.min(x1, b.right); y1 = Math.min(y1, b.bottom); } }
    return { left: x0, top: y0, right: x1, bottom: y1, w: x1 - x0, h: y1 - y0 }; };
  const boxes = [];
  for (const el of document.querySelectorAll('body *')) {
    const own = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
    if (!own || vis(el) < .25) continue;
    const rg = document.createRange(); rg.selectNodeContents(el);              // the glyphs, not the box
    const r = rg.getBoundingClientRect(); if (r.width < 2 || r.height < 2) continue;
    if (r.right < 0 || r.left > W || r.bottom < 0 || r.top > H) continue;    // fully off-screen: not shown
    const c = clipped(el, r); if (c.w < 2 || c.h < 2) continue;                // fully hidden by a parent: not shown
    const crop = el.closest('[data-crop]'), txt = el.textContent.trim().slice(0, 40);
    if (!el.closest('[data-overlap-ok]')) boxes.push({ el, txt, r: c });
    // rendered size = CSS size x every ancestor transform (scaled phones, zooming cameras)
    const fs = parseFloat(getComputedStyle(el).fontSize) * (el.offsetHeight ? Math.min(4, Math.max(.1, el.getBoundingClientRect().height / el.offsetHeight)) : 1);
    if (fs < MIN - .5 && !el.closest('[data-small]')) out.push({ kind: 'small', txt, px: +fs.toFixed(1), min: +MIN.toFixed(1) });
    if (!crop && (c.w < r.width - 2 || c.h < r.height - 2)) out.push({ kind: 'clipped', txt });
    if (!crop && (r.left < -2 || r.right > W + 2 || r.top < -2 || r.bottom > H + 2)) out.push({ kind: 'cut', txt });
    if (ratio === '9x16' && !crop) {
      if (r.top < H * SAFE.top || r.bottom > H * (1 - SAFE.bottom)) out.push({ kind: 'unsafe', txt, top: Math.round(r.top), bottom: Math.round(r.bottom) });
      else if (r.right > W * SAFE.rail_x && r.bottom > H * SAFE.rail_top && r.top < H * SAFE.rail_bottom) out.push({ kind: 'rail', txt, right: Math.round(r.right) });
    }
  }
  // two separate text runs drawn on top of each other (a collision; mark deliberately layered type data-overlap-ok)
  for (let i = 0; i < boxes.length; i++) for (let j = i + 1; j < boxes.length; j++) {
    const A = boxes[i], B = boxes[j];
    if (A.el.contains(B.el) || B.el.contains(A.el)) continue;
    const ix = Math.min(A.r.right, B.r.right) - Math.max(A.r.left, B.r.left), iy = Math.min(A.r.bottom, B.r.bottom) - Math.max(A.r.top, B.r.top);
    if (ix <= 0 || iy <= 0) continue;
    const small = Math.min(A.r.w * A.r.h, B.r.w * B.r.h);
    if (ix * iy > .12 * small) out.push({ kind: 'overlap', txt: A.txt + '  x  ' + B.txt });
  }
  return out;
}"""


def serve() -> int:
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a):
            pass
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(HERE)))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv.server_address[1]


def render_at(page, t: float) -> None:
    try:
        page.evaluate(f"render({t})")
    except PWError as e:
        msg = str(e).splitlines()[0]
        sys.exit(f"render({t:.3f}) threw in the page: {msg}\n  -> fix the composition at t = {t:.3f} s (stills at that time reproduce it)")


def _label_font() -> str:
    """drawtext needs a font file on builds without fontconfig defaults (common on Windows)."""
    for f in ("C:/Windows/Fonts/arial.ttf", "/System/Library/Fonts/Supplemental/Arial.ttf", "/Library/Fonts/Arial.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "/usr/share/fonts/TTF/DejaVuSans.ttf"):
        if Path(f).is_file():
            return "fontfile='" + f.replace(":", chr(92) + ":") + "':"
    return ""


def sheet(files: list[Path], dst: Path, ratio: str) -> None:
    """Contact sheet with each tile labelled by its time, so a transition frame isn't mistaken for a bug."""
    tmp = dst.parent / "_labelled"
    tmp.mkdir(exist_ok=True)
    sw = 270 if ratio == "9x16" else 480
    font = _label_font()
    labelled = []
    for i, f in enumerate(files):
        try:
            t = f"{float(f.stem.rsplit('-', 1)[-1]):.2f}"
        except ValueError:
            t = f.stem
        o = tmp / f"{i:04d}.jpg"
        vf = f"scale={sw}:-2" + (f",drawtext={font}text='{t} s':x=6:y=6:fontsize=16:fontcolor=white:box=1:boxcolor=black@0.6" if font else "")
        subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(f), "-vf", vf, str(o)])
        labelled.append(o if o.is_file() else f)
    lst = tmp / "list.txt"
    lst.write_text("".join(f"file '{s.resolve().as_posix()}'\n" for s in labelled), encoding="utf-8")
    cols = 5 if ratio == "9x16" else 4
    rows = (len(labelled) + cols - 1) // cols
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst),
                    "-vf", f"scale={sw}:-2,tile={cols}x{rows}:padding=4:color=white", "-frames:v", "1", str(dst)])
    for f in tmp.iterdir():
        f.unlink()
    tmp.rmdir()


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["stills", "video"])
    ap.add_argument("--ratio", choices=sorted(RATIOS), default="16x9")
    ap.add_argument("--times", nargs="*", type=float, default=[])
    ap.add_argument("--every", type=float, help="stills: one frame every N seconds of the whole film")
    ap.add_argument("--page", default="composition", help="any page following the page contract (composition, techniques, styleframes…)")
    ap.add_argument("--draft", action="store_true", help="video: 30 fps, half size, no motion blur (fast check)")
    ap.add_argument("--from", dest="t_from", type=float, help="video: render from this time (s)")
    ap.add_argument("--to", dest="t_to", type=float, help="video: render up to this time (s)")
    a = ap.parse_args()
    tl = json.loads((HERE / "timeline.json").read_text(encoding="utf-8"))
    w, h = RATIOS[a.ratio]
    out = HERE / "out"
    out.mkdir(exist_ok=True)
    port = serve()
    tag = a.page if a.page != "composition" else a.ratio
    with sync_playwright() as p:
        b = p.chromium.launch()
        page = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
        errors: list[str] = []
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.goto(f"http://127.0.0.1:{port}/{a.page}.html?w={w}&h={h}", wait_until="networkidle")
        try:
            page.wait_for_function("window.READY === true", timeout=60000)
        except PWError:
            sys.exit(f"{a.page}.html never set window.READY (page errors: {errors or 'none'}). See the page contract in this file's docstring.")
        if a.mode == "stills":
            times = list(a.times)
            if a.every:
                times += [round(i * a.every, 3) for i in range(int(tl["duration"] / a.every) + 1)]
            (out / "stills").mkdir(exist_ok=True)
            shots = []
            for t in times:
                render_at(page, t)
                for it in page.evaluate(LAYOUT_JS, [a.ratio, SAFE]):
                    extra = {k: v for k, v in it.items() if k not in ("kind", "txt")}
                    print(f"  layout {t:6.2f}s  {it['kind']:<7} {it['txt']!r} {extra or ''}")
                f = out / "stills" / f"{tag}-{t:06.2f}.jpg"
                page.screenshot(path=str(f), type="jpeg", quality=88)
                shots.append(f)
            if shots:
                sheet(shots, out / "stills" / f"_sheet-{tag}.jpg", a.ratio)
            print(f"{len(shots)} stills + contact sheet in out/stills; page errors: {errors or 'none'}")
        else:
            fps = 30 if a.draft else tl["fps"]
            sub = 1 if a.draft else SUB
            t0s, t1s = a.t_from or 0.0, min(a.t_to or tl["duration"], tl["duration"])
            first, last = int(round(t0s * fps)), int(round(t1s * fps))
            blur = [] if a.draft else [tuple(x) for x in tl.get("blur", [])]
            name = "draft" if a.draft else ("range" if (a.t_from or a.t_to) else "film")
            dst = out / (f"{name}-{a.ratio}.mp4" if name != "range" else f"range-{a.ratio}-{t0s:g}-{t1s:g}.mp4")
            if a.draft:
                page.set_viewport_size({"width": w, "height": h})   # same layout; scaled down in the encode
            audio = out / "score.wav"
            cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "image2pipe", "-framerate", str(fps * sub), "-c:v", "mjpeg", "-i", "-"]
            if audio.is_file():
                cmd += ["-ss", f"{t0s:.3f}", "-i", str(audio)]
            vf = (f"tmix=frames={sub},select='eq(mod(n\\,{sub})\\,{sub - 1})',setpts=N/({fps}*TB)," if sub > 1 else "") \
                + ("scale=iw/2:ih/2," if a.draft else "") + "scale=in_range=full:out_range=tv,format=yuv420p"
            cmd += ["-vf", vf, "-color_range", "tv", "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709",
                    "-c:v", "libx264", "-preset", "veryfast" if a.draft else "slow", "-crf", "23" if a.draft else "16",
                    "-r", str(fps), "-movflags", "+faststart"]
            if audio.is_file():
                cmd += ["-c:a", "aac", "-b:a", "256k", "-shortest"]
            ff = subprocess.Popen(cmd + [str(dst)], stdin=subprocess.PIPE)
            layout: list = []
            started = time.time()
            for i in range(first, last):
                t0 = i / fps
                fast = any(s <= t0 < e for s, e in blur)
                for k in range(sub):                       # sub frames per output frame; tmix averages them
                    t = t0 + (k / sub) * (0.5 / fps) if fast else t0   # 180° shutter in fast windows, else identical
                    if k == 0 or fast:
                        render_at(page, t)
                        jpg = page.screenshot(type="jpeg", quality=88 if a.draft else 94)
                    ff.stdin.write(jpg)
                if (i - first) % max(1, fps // 2) == 0 and a.page == "composition":
                    for it in page.evaluate(LAYOUT_JS, [a.ratio, SAFE]):
                        layout.append({"t": round(t0, 2), **it})
                if (i - first) % (fps * 2) == 0 and i > first:
                    done = (i - first) / max(1, last - first)
                    eta = (time.time() - started) / done * (1 - done)
                    print(f"  {i - first}/{last - first} frames, ~{eta / 60:.1f} min left", flush=True)
            ff.stdin.close()
            ff.wait()
            (out / f"layout-{a.ratio}.json").write_text(json.dumps(layout, indent=1), encoding="utf-8")
            kinds = {k: sum(1 for x in layout if x["kind"] == k) for k in ("small", "overlap", "clipped", "cut", "unsafe", "rail")}
            print("layout check (every 0.5 s): " + ", ".join(f"{v} {k}" for k, v in kinds.items())
                  + (f" -> see out/layout-{a.ratio}.json and fix before delivery" if layout else " -> clean"))
            print(f"wrote {dst} in {(time.time() - started) / 60:.1f} min; page errors: {errors or 'none'}."
                  + ("" if name != "film" else f" Next: python <skill>/scripts/video_qa.py {dst} --sheet out/qa-sheet.jpg"))
        b.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

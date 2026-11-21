#!/usr/bin/env python3
"""DENT video kit renderer: HTML composition -> frames (headless Chromium) -> MP4 (FFmpeg).

  python render.py stills --ratio 16x9 --times 0.5 3.4 7.2      # review frames -> out/stills/ (+ contact sheet)
  python render.py video  --ratio 16x9                          # out/film-16x9.mp4 (uses out/score.wav if present)
  python render.py video  --ratio 9x16                          # vertical cut (layout adapts in composition.html)

- Deterministic: every frame calls window.render(t).
- Motion blur: inside timeline.json "blur" windows each frame averages SUB sub-frames across a 180° shutter.
- Colour: frames are full-range screenshots; the encode converts to TV-range yuv420p BT.709 (video_qa.py checks it).
Copyright 2026 Jeel Nada (solarquack). Licensed under the Apache License 2.0.
"""
from __future__ import annotations

import argparse
import functools
import http.server
import json
import subprocess
import threading
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
RATIOS = {"16x9": (1920, 1080), "9x16": (1080, 1920), "1x1": (1080, 1080)}
SUB = 6


def serve() -> int:
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a):
            pass
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(HERE)))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv.server_address[1]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["stills", "video"])
    ap.add_argument("--ratio", choices=sorted(RATIOS), default="16x9")
    ap.add_argument("--times", nargs="*", type=float, default=[])
    a = ap.parse_args()
    tl = json.loads((HERE / "timeline.json").read_text(encoding="utf-8"))
    w, h = RATIOS[a.ratio]
    out = HERE / "out"
    out.mkdir(exist_ok=True)
    port = serve()
    with sync_playwright() as p:
        b = p.chromium.launch()
        page = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
        errors: list[str] = []
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.goto(f"http://127.0.0.1:{port}/composition.html?w={w}&h={h}", wait_until="networkidle")
        page.wait_for_function("window.READY === true", timeout=60000)
        if a.mode == "stills":
            (out / "stills").mkdir(exist_ok=True)
            shots = []
            for t in a.times:
                page.evaluate(f"render({t})")
                f = out / "stills" / f"{a.ratio}-{t:06.2f}.jpg"
                page.screenshot(path=str(f), type="jpeg", quality=88)
                shots.append(f)
            if shots:
                lst = out / "stills" / "list.txt"
                lst.write_text("".join(f"file '{s.name}'\n" for s in shots), encoding="utf-8")
                cols = 4 if a.ratio != "9x16" else 5
                rows = (len(shots) + cols - 1) // cols
                sw = 480 if a.ratio != "9x16" else 270
                subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst),
                                "-vf", f"scale={sw}:-2,tile={cols}x{rows}:padding=4:color=white", "-frames:v", "1",
                                str(out / "stills" / f"_sheet-{a.ratio}.jpg")])
            print(f"{len(shots)} stills + contact sheet in out/stills; page errors: {errors or 'none'}")
        else:
            fps, n = tl["fps"], int(tl["duration"] * tl["fps"])
            blur = [tuple(x) for x in tl.get("blur", [])]
            dst = out / f"film-{a.ratio}.mp4"
            audio = out / "score.wav"
            cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "image2pipe", "-framerate", str(fps * SUB), "-c:v", "mjpeg", "-i", "-"]
            if audio.is_file():
                cmd += ["-i", str(audio)]
            cmd += ["-vf", f"tmix=frames={SUB},select='eq(mod(n\\,{SUB})\\,{SUB - 1})',setpts=N/({fps}*TB),"
                           "scale=in_range=full:out_range=tv,format=yuv420p",
                    "-color_range", "tv", "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709",
                    "-c:v", "libx264", "-preset", "slow", "-crf", "16", "-r", str(fps), "-movflags", "+faststart"]
            if audio.is_file():
                cmd += ["-c:a", "aac", "-b:a", "256k", "-shortest"]
            ff = subprocess.Popen(cmd + [str(dst)], stdin=subprocess.PIPE)
            for i in range(n):
                t0 = i / fps
                fast = any(s <= t0 < e for s, e in blur)
                for k in range(SUB):                      # SUB frames per output frame; tmix averages them
                    t = t0 + (k / SUB) * (0.5 / fps) if fast else t0   # 180° shutter in fast windows, else identical
                    if k == 0 or fast:
                        page.evaluate(f"render({t})")
                        jpg = page.screenshot(type="jpeg", quality=94)
                    ff.stdin.write(jpg)
                if i % (fps * 2) == 0:
                    print(f"  {i}/{n}", flush=True)
            ff.stdin.close()
            ff.wait()
            print(f"wrote {dst}; page errors: {errors or 'none'}. Next: python ../../scripts/video_qa.py {dst.name} (from the skill)")
        b.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

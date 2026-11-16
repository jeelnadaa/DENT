"""Render the DENT launch film: headless Chromium seeks every frame of composition.html, FFmpeg encodes.

Usage:
  python render.py stills 0.5 4.5 9.6 ...      # PNG stills into out/stills/ for review
  python render.py video [--fps 60] [--workers 4] [--start 0] [--end 48]
  python render.py mux                          # mux out/video.mp4 + out/score.wav -> final MP4
  python render.py video --scale 2 --name dent-launch-16x9_60fps   # native 3840x2160 (2x pixel density)
  python render.py mux --name dent-launch-16x9_60fps

Deterministic: the page exposes render(t); nothing animates on its own clock.
"""
import argparse, json, os, re, subprocess, sys, time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "out"
SUB = 8  # motion-blur sub-frames inside BLUR windows
COMP = (HERE / "composition.html").as_uri()
TL = json.loads(re.search(r"window\.TL\s*=\s*(\{.*\})", (HERE / "timeline.js").read_text(), re.S).group(1))


# windows with fast motion get real motion blur: the strike, the scatter, the hop, every dot-wipe, the burst entrances
BLUR = [(TL["dotFall"], TL["dotLand"] + .25)] + [(TL[w] - .36, TL[w] + .32) for w in ("wipe1", "wipe2", "wipe3", "wipe4", "wipe5")]      + [(s - .16, s + .06) for s in TL["stamps"] + TL["endStamps"]] + [(b, b + .3) for b in TL["burst"]] + [(TL["logoTok"] - .3, TL["logoTok"] + .1)]


GPU_ARGS = ["--use-angle=d3d11", "--enable-gpu", "--ignore-gpu-blocklist", "--enable-gpu-rasterization", "--force_high_performance_gpu"]
USE_GPU = os.environ.get("DENT_RENDER_GPU") == "1"   # opt-in: discrete GPU via ANGLE D3D11 (pixels differ slightly from the approved CPU render)


def open_page(p, scale=1):
    from playwright.sync_api import sync_playwright  # noqa
    b = p.chromium.launch(args=["--disable-lcd-text", "--font-render-hinting=none", "--force-color-profile=srgb"] + (GPU_ARGS if USE_GPU else []))
    pg = b.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=scale)
    pg.goto(COMP)
    pg.wait_for_function("window.READY === true", timeout=60000)
    return b, pg


def stills(times):
    from playwright.sync_api import sync_playwright
    d = OUT / "stills"; d.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b, pg = open_page(p)
        errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        for t in times:
            pg.evaluate("t => render(t)", float(t))
            f = d / f"t{float(t):06.2f}.png"
            pg.screenshot(path=str(f))
            print(f)
        b.close()
        if errs: print("PAGE ERRORS:", errs)


def worker(args):
    idx, f0, f1, fps, scale, name = args
    from playwright.sync_api import sync_playwright
    seg = OUT / f"{name}_seg{idx:02d}.mp4"
    crf = "14" if scale == 1 else "12"
    ff = subprocess.Popen([
        "ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(fps * SUB), "-c:v", "png", "-i", "-",
        "-vf", f"tmix=frames={SUB},select='eq(mod(n\,{SUB})\,{SUB - 1})',setpts=N/({fps}*TB)",
        "-c:v", "libx264", "-preset", "slow", "-crf", crf, "-tune", "animation", "-pix_fmt", "yuv420p",
        "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709", "-r", str(fps), str(seg)],
        stdin=subprocess.PIPE)
    t_start = time.time()
    with sync_playwright() as p:
        b, pg = open_page(p, scale)
        cdp = pg.context.new_cdp_session(pg)
        import base64
        SHOT = {"format": "png", "optimizeForSpeed": True, "clip": {"x": 0, "y": 0, "width": 1920, "height": 1080, "scale": scale}}  # clip.scale renders at native density
        for fr in range(f0, f1):
            t = fr / fps
            if any(a <= t < b for a, b in BLUR):   # 180-degree shutter: SUB samples across half the frame interval
                for k in range(SUB):
                    pg.evaluate("t => render(t)", t + k * .5 / (fps * SUB))
                    ff.stdin.write(base64.b64decode(cdp.send("Page.captureScreenshot", SHOT)["data"]))
            else:
                pg.evaluate("t => render(t)", t)
                img = base64.b64decode(cdp.send("Page.captureScreenshot", SHOT)["data"])
                for _ in range(SUB): ff.stdin.write(img)
            if (fr - f0) % 300 == 0:
                print(f"[w{idx}] frame {fr} ({fr - f0}/{f1 - f0}) {time.time() - t_start:.0f}s", flush=True)
        b.close()
    ff.stdin.close(); ff.wait()
    return str(seg)


def video(fps, workers, start, end, scale=1, name="video"):
    OUT.mkdir(exist_ok=True)
    f0, f1 = round(start * fps), round(end * fps)
    n = f1 - f0
    chunks = [(i, f0 + n * i // workers, f0 + n * (i + 1) // workers, fps, scale, name) for i in range(workers)]
    t = time.time()
    with ProcessPoolExecutor(workers) as ex:
        segs = list(ex.map(worker, chunks))
    lst = OUT / f"{name}_segments.txt"
    lst.write_text("".join(f"file '{Path(s).name}'\n" for s in segs))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(OUT / f"{name}_video.mp4")], check=True)
    for s_ in segs: Path(s_).unlink()
    print(f"{name}_video.mp4: {n} frames in {time.time() - t:.0f}s")


def mux(name="video"):
    src, aud = OUT / f"{name}_video.mp4", OUT / "score.wav"
    final = OUT / ("dent-launch-16x9.mp4" if name == "video" else f"{name}.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src), "-i", str(aud), "-map", "0:v", "-map", "1:a",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-shortest", "-movflags", "+faststart",
                    "-metadata", "title=DENT: Make a dent with your product's design", str(final)], check=True)
    print(final)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["stills", "video", "mux"])
    ap.add_argument("times", nargs="*", type=float)
    ap.add_argument("--fps", type=int, default=TL["fps"])
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--start", type=float, default=0.0)
    ap.add_argument("--end", type=float, default=TL["duration"])
    ap.add_argument("--scale", type=int, default=1, help="device pixel ratio: 2 = 3840x2160")
    ap.add_argument("--name", default="video", help="output basename, so earlier renders are never overwritten")
    a = ap.parse_args()
    if a.cmd == "stills": stills(a.times)
    elif a.cmd == "video": video(a.fps, a.workers, a.start, a.end, a.scale, a.name)
    else: mux(a.name)

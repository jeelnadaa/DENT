"""QA for the rendered film (VIDEO.md §9): metadata, loudness, flashes, A/V sync, contact sheet.

  python qa.py out/dent-launch-16x9.mp4
"""
import json, re, subprocess, sys
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
T = json.loads(re.search(r"window\.TL\s*=\s*(\{.*\})", (HERE / "timeline.js").read_text(), re.S).group(1))
f = Path(sys.argv[1] if len(sys.argv) > 1 else HERE / "out" / "dent-launch-16x9.mp4")
rep = {}

# 1. metadata
p = json.loads(subprocess.run(["ffprobe", "-v", "error", "-show_entries",
    "format=duration,size,bit_rate:stream=codec_name,profile,width,height,r_frame_rate,pix_fmt,sample_rate,channels,color_primaries",
    "-of", "json", str(f)], capture_output=True, text=True).stdout)
rep["ffprobe"] = p

# 2. loudness (EBU R128)
r = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(f), "-map", "0:a", "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
s = r[r.rfind("Summary:"):]
rep["loudness"] = {"I_LUFS": float(re.search(r"I:\s+(-?[\d.]+)", s).group(1)), "LRA": float(re.search(r"LRA:\s+(-?[\d.]+)", s).group(1)),
                   "true_peak_dBFS": float(re.search(r"Peak:\s+(-?[\d.]+)", s).group(1))}

# 3. flashes: per-frame mean luma; a flash = a pair of opposing swings >= 10% of full range within 1 s windows (WCAG 2.3.1, general-flash proxy on the whole frame)
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(f), "-vf", "scale=96:54,format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
fr = np.frombuffer(raw, np.uint8).reshape(-1, 54, 96).astype(float)
Y = fr.mean(axis=(1, 2)) / 255
fps = eval(p["streams"][0]["r_frame_rate"])
d = np.diff(Y)
sw = []  # significant swings (direction, frame)
acc, start = 0.0, 0
for i, v in enumerate(d):
    if acc == 0 or np.sign(v) == np.sign(acc): acc += v
    else:
        if abs(acc) >= .10: sw.append((np.sign(acc), i))
        acc = v
if abs(acc) >= .10: sw.append((np.sign(acc), len(d)))
flashes = [(sw[k][1], sw[k + 1][1]) for k in range(len(sw) - 1) if sw[k][0] != sw[k + 1][0]]
per_sec = max((sum(1 for a, b in flashes if t * fps <= a < (t + 1) * fps) for t in range(int(len(Y) / fps) + 1)), default=0)
rep["flashes"] = {"large_luma_swings": [(round(i / fps, 2), int(s_)) for s_, i in sw], "max_flash_pairs_per_second": per_sec, "limit": 3}

# 4. A/V sync: nearest audio onset to each hard visual hit
a = subprocess.run(["ffmpeg", "-v", "error", "-i", str(f), "-map", "0:a", "-ac", "1", "-ar", "48000", "-f", "f32le", "-"], capture_output=True).stdout
x = np.frombuffer(a, np.float32)
hop = 240  # 5 ms
env = np.sqrt(np.convolve(x ** 2, np.ones(hop) / hop, "same")[::hop])
on = np.maximum(0, np.diff(np.log(env + 1e-5)))
cues = {"impact": T["impact"], **{f"stamp{i+1}": s for i, s in enumerate(T["stamps"])}, "dotPress": T["dotPress"],
        "passed": T["passed"], "burst1": T["burst"][0], "logoTok": T["logoTok"]}
sync = {}
for k, c in cues.items():
    i0, i1 = int((c - .08) * 200), int((c + .08) * 200)
    j = i0 + int(np.argmax(on[i0:i1]))
    sync[k] = round((j * hop / 48000 - c) * 1000, 1)
rep["av_sync_ms"] = sync

# 5. contact sheet of one frame per scene
times = [1.6, 4.6, 6.5, 8.12, 12.5, 16.0, 20.5, 27.9, 33.0, 36.5, 39.7, 46.0]
out = HERE / "out"
args = sum((["-ss", str(t), "-i", str(f)] for t in times), [])
filt = "".join(f"[{i}:v]scale=480:270[v{i}];" for i in range(len(times)))
layout = "|".join(f"{(i % 4) * 480}_{(i // 4) * 270}" for i in range(len(times)))
filt += "".join(f"[v{i}]" for i in range(len(times))) + f"xstack=inputs={len(times)}:layout={layout}[o]"
subprocess.run(["ffmpeg", "-y", "-v", "error", *args, "-filter_complex", filt, "-map", "[o]", "-frames:v", "1", str(out / "qa-sheet.png")], check=True)
rep["contact_sheet"] = str(out / "qa-sheet.png")

print(json.dumps(rep, indent=1, default=str))
(out / "qa.json").write_text(json.dumps(rep, indent=1, default=str))

#!/usr/bin/env python3
"""DENT video QA: measure a finished video instead of trusting it. Exit 1 when a check fails.

  python video_qa.py film.mp4 [--captions film.srt] [--lufs -14] [--kind trailer|explainer|tutorial|loop]
                              [--end-hold 4] [--sheet out/sheet.jpg]

Checks (references/video/video-tools-and-pipeline.md §6):
  streams   H.264/HEVC/VP9/AV1 video, yuv420p, TV (limited) colour range, constant frame rate, AAC/Opus audio
  sync      video and audio durations agree (≤ 0.1 s)
  loudness  integrated LUFS within ±1 of the target, true peak ≤ −1 dBTP
  motion    share of the film that is frozen (no visible change) and the longest frozen hold, excluding the
            final end-card hold. Trailers and launch films: frozen ≤ 20 %, no hold > 2.5 s; explainers ≤ 35 % / 4 s;
            tutorials ≤ 50 % / 6 s. A deliberate still must be a decision, not the default.
  rhythm    shot changes per minute and the longest shot (information only)
  black     black frames outside the first/last 0.5 s
  captions  SRT/VTT: ≤ 42 characters × 2 lines, ≥ 1 s per cue, cues inside the film
  sheet     optional contact sheet (one frame every N s) for a human look; this script cannot judge taste.

Needs FFmpeg/ffprobe. Copyright 2026 Jeel Nada (solarquack). Licensed under the Apache License 2.0.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

LIMITS = {"trailer": (0.20, 2.5), "explainer": (0.35, 4.0), "tutorial": (0.50, 6.0), "loop": (0.20, 2.5)}
fails: list[str] = []
report: dict = {}


def check(ok: bool, msg: str, key: str | None = None) -> None:
    print(("  ok    " if ok else "  FAIL  ") + msg)
    if not ok:
        fails.append(msg)


def run(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(list(args), capture_output=True, text=True)


def probe(p: Path) -> dict:
    return json.loads(run("ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(p)).stdout)


def frozen(p: Path, dur: float, end_hold: float) -> tuple[float, float, list]:
    r = run("ffmpeg", "-hide_banner", "-nostats", "-i", str(p), "-vf", "freezedetect=n=0.002:d=0.5", "-map", "0:v", "-f", "null", "-")
    starts = [float(x) for x in re.findall(r"freeze_start: ([0-9.]+)", r.stderr)]
    ends = [float(x) for x in re.findall(r"freeze_end: ([0-9.]+)", r.stderr)]
    if len(ends) < len(starts):
        ends.append(dur)
    segs = []
    for s, e in zip(starts, ends):
        e = min(e, dur - end_hold) if e > dur - end_hold else e   # the closing end card may hold
        if e - s > 0.01:
            segs.append((round(s, 2), round(e, 2)))
    total = sum(e - s for s, e in segs)
    longest = max((e - s for s, e in segs), default=0.0)
    return total, longest, segs


def shots(p: Path) -> list[float]:
    r = run("ffmpeg", "-hide_banner", "-nostats", "-i", str(p), "-vf", "select='gt(scene,0.30)',showinfo", "-map", "0:v", "-f", "null", "-")
    return [float(x) for x in re.findall(r"pts_time:([0-9.]+)", r.stderr)]


def loud(p: Path, target: float) -> tuple[float, float]:
    r = run("ffmpeg", "-hide_banner", "-nostats", "-i", str(p), "-af", f"loudnorm=I={target}:TP=-1:print_format=json", "-f", "null", "-")
    j = json.loads(r.stderr[r.stderr.rfind("{"): r.stderr.rfind("}") + 1])
    return float(j["input_i"]), float(j["input_tp"])


def black(p: Path, dur: float) -> list:
    r = run("ffmpeg", "-hide_banner", "-nostats", "-i", str(p), "-vf", "blackdetect=d=0.2:pix_th=0.06", "-map", "0:v", "-f", "null", "-")
    segs = [(float(a), float(b)) for a, b in re.findall(r"black_start:([0-9.]+) black_end:([0-9.]+)", r.stderr)]
    return [(a, b) for a, b in segs if a > 0.5 and b < dur - 0.5]


def captions(path: Path, dur: float) -> None:
    text = path.read_text(encoding="utf-8")
    ts = r"(\d\d:\d\d:\d\d[,.]\d\d\d) --> (\d\d:\d\d:\d\d[,.]\d\d\d)"
    blocks = re.split(r"\n\s*\n", text.strip())
    cues = []
    for b in blocks:
        m = re.search(ts, b)
        if m:
            body = b[m.end():].strip().splitlines()
            cues.append((m.group(1), m.group(2), body))
    sec = lambda s: int(s[:2]) * 3600 + int(s[3:5]) * 60 + float(s[6:].replace(",", "."))  # noqa: E731
    check(bool(cues), f"captions: {len(cues)} cues in {path.name}")
    check(all(len(ln) <= 42 for _, _, body in cues for ln in body), "captions: every line ≤ 42 characters")
    check(all(len(body) <= 2 for _, _, body in cues), "captions: ≤ 2 lines per cue")
    check(all(sec(e) - sec(s) >= 1.0 for s, e, _ in cues), "captions: every cue ≥ 1 s")
    check(all(sec(e) <= dur + 0.5 for _, e, _ in cues), "captions: every cue inside the film")


def sheet(p: Path, out: Path, dur: float) -> None:
    every = max(1.0, dur / 16)
    out.parent.mkdir(parents=True, exist_ok=True)
    run("ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(p), "-vf",
        f"fps=1/{every:.3f},scale=480:-2,tile=4x4:padding=4:color=white", "-frames:v", "1", str(out))
    print(f"  info  contact sheet (one frame every {every:.1f} s): {out}  ← look at it")


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        pass
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("video")
    ap.add_argument("--captions")
    ap.add_argument("--lufs", type=float, default=-14.0)
    ap.add_argument("--kind", choices=sorted(LIMITS), default="trailer")
    ap.add_argument("--end-hold", type=float, default=4.0, help="seconds of closing end card allowed to hold still")
    ap.add_argument("--sheet")
    ap.add_argument("--json", help="write the report here")
    a = ap.parse_args()
    p = Path(a.video)
    print(f"DENT video QA: {p.name}")
    j = probe(p)
    v = next((s for s in j.get("streams", []) if s["codec_type"] == "video"), None)
    au = next((s for s in j.get("streams", []) if s["codec_type"] == "audio"), None)
    if not v:
        check(False, "has a video stream")
        return 1
    dur = float(j["format"]["duration"])
    check(v["codec_name"] in ("h264", "hevc", "vp9", "av1"), f"video codec {v['codec_name']}")
    check(v.get("pix_fmt") == "yuv420p", f"pixel format {v.get('pix_fmt')} (yuv420p; yuvj420p means full-range JPEG frames were piped in)")
    check(v.get("color_range", "tv") in ("tv", "unknown"), f"colour range {v.get('color_range', 'unset')} (TV/limited)")
    check(v.get("r_frame_rate") == v.get("avg_frame_rate"), f"constant frame rate ({v.get('r_frame_rate')})")
    if au:
        check(au["codec_name"] in ("aac", "opus"), f"audio codec {au['codec_name']}")
        ad = float(au.get("duration", dur))
        check(abs(float(v.get("duration", dur)) - ad) <= 0.1, f"A/V durations {float(v.get('duration', dur)):.2f} s / {ad:.2f} s")
        i, tp = loud(p, a.lufs)
        report["loudness"] = {"lufs": i, "true_peak": tp}
        check(abs(i - a.lufs) <= 1.0, f"loudness {i:.1f} LUFS (target {a.lufs} ± 1)")
        check(tp <= -1.0, f"true peak {tp:.1f} dBTP (≤ −1)")
    else:
        print("  info  no audio stream")
    share_max, hold_max = LIMITS[a.kind]
    total, longest, segs = frozen(p, dur, a.end_hold)
    body = max(0.1, dur - a.end_hold)
    report["motion"] = {"frozen_s": round(total, 2), "frozen_share": round(total / body, 3), "longest_hold_s": round(longest, 2), "segments": segs}
    check(total / body <= share_max, f"motion: {total:.1f} s of {body:.1f} s frozen ({100 * total / body:.0f} %, limit {100 * share_max:.0f} % for a {a.kind})")
    check(longest <= hold_max, f"motion: longest frozen hold {longest:.1f} s (limit {hold_max} s; closing {a.end_hold} s end card excluded)")
    cuts = shots(p)
    report["shots"] = {"cuts": len(cuts), "per_minute": round(len(cuts) / dur * 60, 1)}
    gaps = [b - a_ for a_, b in zip([0.0] + cuts, cuts + [dur])]
    print(f"  info  rhythm: {len(cuts)} shot changes ({len(cuts) / dur * 60:.0f}/min), longest shot {max(gaps):.1f} s")
    bl = black(p, dur)
    check(not bl, f"no unintended black frames ({len(bl)} found)")
    if a.captions:
        captions(Path(a.captions), dur)
    if a.sheet:
        sheet(p, Path(a.sheet), dur)
    if a.json:
        Path(a.json).write_text(json.dumps(report, indent=2), encoding="utf-8")
    print("  note  taste, message and product truth are not measured here: look at the sheet and watch it with sound off and on")
    print(f"\n{len(fails)} failure(s)" if fails else "\nAll measured checks passed")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())

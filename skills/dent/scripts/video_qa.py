#!/usr/bin/env python3
"""DENT video QA: measure a finished video instead of trusting it. Exit 1 when a check fails.

  python video_qa.py film.mp4 [--captions film.srt] [--lufs -14] [--kind trailer|short|explainer|tutorial|loop] [--audio out/score.wav] [--loop]
                              [--end-hold 4] [--sheet out/sheet.jpg]

Checks (references/video/video-tools-and-pipeline.md §6):
  streams   H.264/HEVC/VP9/AV1 video, yuv420p, TV (limited) colour range, constant frame rate, AAC/Opus audio
  sync      stream durations agree; with --audio <mix.wav>, the film's audio is within 20 ms of the mix it was built from
            (picture and mix share timeline.json, so this is where real-world drift shows up: muxing, trims, -ss)
  loudness  integrated LUFS within ±1 of the target, true peak ≤ −1 dBTP
  motion    share of the film that is frozen (no visible change) and the longest frozen hold, excluding the
            final end-card hold. Trailers and launch films: frozen ≤ 20 %, no hold > 2.5 s; explainers ≤ 35 % / 4 s;
            tutorials ≤ 50 % / 6 s. A deliberate still must be a decision, not the default.
  variety   longest stretch where the picture stays visually the same (trailer ≤ 6 s, explainer ≤ 10 s, tutorial ≤ 20 s)
  energy    mean picture change per second (trailers and loops ≥ 15/255; calibrated on DENT's launch film = 35)
  rhythm    shot changes per minute and the longest shot (information only)
  black     black frames outside the first/last 0.5 s
  captions  SRT/VTT: ≤ 42 characters × 2 lines, ≥ 1 s per cue, cues inside the film
  loop      with --loop (or --kind loop): the last frame flows back into the first
  sheet     optional contact sheet (time-labelled, one frame every N s) for a human look; this script cannot judge taste.

Needs FFmpeg/ffprobe. Copyright 2026 Jeel Nada (solarquack). Licensed under the Apache License 2.0.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

LIMITS = {"trailer": (0.20, 2.5), "short": (0.20, 2.5), "explainer": (0.35, 4.0), "tutorial": (0.50, 6.0), "loop": (0.20, 2.5)}
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


SAME_LIMIT = {"trailer": 6.0, "short": 4.0, "explainer": 10.0, "tutorial": 20.0, "loop": 6.0}
# Calibrated on four measured films: DENT launch film 35.1, a good GPT film 18.6, two flat films 11.3 and 4.2.
ENERGY_MIN = {"trailer": 15.0, "short": 18.0, "loop": 15.0}


def sameness(p: Path, dur: float, end_hold: float) -> tuple[float, float, float, bytes, bytes]:
    """Longest stretch where the picture stays visually the same (tiny grey thumbnails at 4 fps stay within a small
    mean difference of the stretch's first frame). Catches 'technically moving but nothing new' (slow drifts, a
    shimmering hold) that freeze detection misses. Pure standard library."""
    w, h, fps = 48, 27, 4
    r = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(p), "-vf", f"fps={fps},scale={w}:{h},format=gray",
                        "-f", "rawvideo", "-"], capture_output=True)
    raw, n = r.stdout, w * h
    frames = [raw[i:i + n] for i in range(0, len(raw) - n + 1, n)]
    limit_frames = int(max(0.0, dur - end_hold) * fps)
    frames = frames[:limit_frames]
    best, best_at, start = 0, 0, 0
    for i in range(1, len(frames) + 1):
        if i == len(frames) or sum(abs(a - b) for a, b in zip(frames[start], frames[i])) / n > 10:
            if i - start > best:
                best, best_at = i - start, start
            start = i
    allf = [raw[i:i + n] for i in range(0, len(raw) - n + 1, n)]
    diffs = [sum(abs(a - b) for a, b in zip(frames[i - fps], frames[i])) / n for i in range(fps, len(frames))]
    change = sum(diffs) / len(diffs) if diffs else 0.0
    return best / fps, change, best_at / fps, (allf[0] if allf else b""), (allf[-1] if allf else b"")


def _envelope(path: Path, seconds: float = 30.0) -> list[float]:
    """100 Hz loudness envelope of the first `seconds` (8 kHz mono PCM via FFmpeg, pure standard library)."""
    import array
    r = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(path), "-vn", "-af", "aresample=async=1:first_pts=0", "-ac", "1", "-ar", "8000",
                        "-t", str(seconds), "-f", "s16le", "-"], capture_output=True)
    pcm = array.array("h", r.stdout)
    return [sum(abs(x) for x in pcm[i:i + 80]) / 80 for i in range(0, len(pcm) - 80, 80)]


def sync(p: Path, source: Path) -> None:
    """A/V sync = is the film's audio exactly where the mix was built (picture and mix share timeline.json by
    construction)? Cross-correlate the encoded audio with the source mix and report the offset."""
    a, b = _envelope(p), _envelope(source)
    if len(a) < 100 or len(b) < 100:
        print("  info  sync: not enough audio to compare")
        return
    n = min(len(a), len(b))
    ma, mb = sum(a[:n]) / n, sum(b[:n]) / n
    a2, b2 = [x - ma for x in a[:n]], [x - mb for x in b[:n]]
    best, lag = -1e18, 0
    for k in range(-50, 51):   # ±500 ms in 10 ms steps
        c = sum(a2[i] * b2[i - k] for i in range(max(0, k), min(n, n + k)))
        if c > best:
            best, lag = c, k
    report["sync"] = {"offset_ms": lag * 10, "source": str(source)}
    check(abs(lag) * 10 <= 20, f"sync: film audio is {lag * 10:+d} ms from the source mix {source.name} (|offset| ≤ 20 ms)")


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


def _label_font() -> str:
    for f in ("C:/Windows/Fonts/arial.ttf", "/System/Library/Fonts/Supplemental/Arial.ttf", "/Library/Fonts/Arial.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "/usr/share/fonts/TTF/DejaVuSans.ttf"):
        if Path(f).is_file():
            return "fontfile='" + f.replace(":", chr(92) + ":") + "':"
    return ""


def sheet(p: Path, out: Path, dur: float) -> None:
    every = max(1.0, dur / 16)
    out.parent.mkdir(parents=True, exist_ok=True)
    font = _label_font()
    label = (f",drawtext={font}text='%{{pts\\:hms}}':x=6:y=6:fontsize=18:fontcolor=white:box=1:boxcolor=black@0.6" if font else "")
    run("ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(p), "-vf",
        f"fps=1/{every:.3f},scale=480:-2{label},tile=4x4:padding=4:color=white", "-frames:v", "1", str(out))
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
    ap.add_argument("--audio", help="the source mix (e.g. out/score.wav): measures the film's A/V offset against it")
    ap.add_argument("--loop", action="store_true", help="the film loops: check the last frame flows into the first")
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
        check(abs(float(v.get("duration", dur)) - ad) <= 0.1, f"A/V stream durations match ({float(v.get('duration', dur)):.2f} s / {ad:.2f} s)")
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
    same_s, change, same_at, first, last = sameness(p, dur, 0.0 if (a.loop or a.kind == "loop") else a.end_hold)
    report["variety"] = {"longest_same_s": same_s, "starts_at_s": same_at, "mean_change_per_s": round(change, 2)}
    check(same_s <= SAME_LIMIT[a.kind], f"variety: longest visually-unchanged stretch {same_s:.1f} s from {same_at:.1f} s (limit {SAME_LIMIT[a.kind]} s for a {a.kind})")
    if a.loop or a.kind == "loop":
        seam = sum(abs(x - y) for x, y in zip(first, last)) / max(1, len(first))
        report["loop_seam"] = round(seam, 1)
        check(seam <= 12, f"loop seam: last frame vs first frame differ by {seam:.1f}/255 (≤ 12 reads as one continuous loop)")
    if a.kind in ENERGY_MIN:
        check(change >= ENERGY_MIN[a.kind], f"energy: mean picture change {change:.1f}/255 per second (floor {ENERGY_MIN[a.kind]} for a {a.kind}; DENT's launch film: 35)")
    else:
        print(f"  info  energy: mean picture change {change:.1f}/255 per second (DENT's launch film: 35)")
    cuts = shots(p)
    report["shots"] = {"cuts": len(cuts), "per_minute": round(len(cuts) / dur * 60, 1)}
    gaps = [b - a_ for a_, b in zip([0.0] + cuts, cuts + [dur])]
    print(f"  info  rhythm: {len(cuts)} shot changes ({len(cuts) / dur * 60:.0f}/min), longest shot {max(gaps):.1f} s")
    bl = black(p, dur)
    check(not bl, f"no unintended black frames ({len(bl)} found)")
    if a.captions:
        captions(Path(a.captions), dur)
    if a.audio and au:
        sync(p, Path(a.audio))
    elif au:
        print("  info  sync: pass --audio out/score.wav to measure the film's A/V offset against its mix")
    if a.sheet:
        sheet(p, Path(a.sheet), dur)
    if a.json:
        Path(a.json).write_text(json.dumps(report, indent=2), encoding="utf-8")
    print("  note  taste, message and product truth are not measured here: look at the sheet and watch it with sound off and on")
    print(f"\n{len(fails)} failure(s)" if fails else "\nAll measured checks passed")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())

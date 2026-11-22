#!/usr/bin/env python3
"""DENT doctor: what can this machine and session actually do? Run it before promising media or verification.

  python doctor.py            # human-readable report
  python doctor.py --json     # machine-readable

Checks: Python, Node, FFmpeg/ffprobe, Playwright + Chromium (verify_page.py), GPU and VRAM, free disk,
TTS engines (via tts.py), Blender, ImageMagick, Whisper, which provider API keys are *set* (names only, never values),
and the age of the Google Fonts snapshot. Prints what DENT can promise and what needs a decision.
Copyright 2026 Jeel Nada (solarquack). Licensed under the Apache License 2.0.
"""
from __future__ import annotations

import datetime as dt
import importlib.util
import json
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
KEYS = ["OPENAI_API_KEY", "ELEVENLABS_API_KEY", "GEMINI_API_KEY", "GOOGLE_API_KEY", "MISTRAL_API_KEY", "REPLICATE_API_TOKEN",
        "FAL_KEY", "STABILITY_API_KEY", "RUNWAYML_API_SECRET", "LUMAAI_API_KEY", "CARTESIA_API_KEY", "HUME_API_KEY",
        "AZURE_SPEECH_KEY", "AWS_ACCESS_KEY_ID", "ANTHROPIC_API_KEY", "HF_TOKEN"]


def run(cmd: list[str], timeout: int = 20) -> str:
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return (r.stdout or r.stderr).strip().splitlines()[0] if (r.stdout or r.stderr).strip() else ""
    except Exception:  # noqa: BLE001
        return ""


def gpu() -> dict:
    out = run(["nvidia-smi", "--query-gpu=name,memory.total", "--format=csv,noheader,nounits"])
    if out and "," in out:
        name, mem = out.split(",", 1)
        return {"vendor": "nvidia", "name": name.strip(), "vram_gb": round(int(mem.strip()) / 1024, 1)}
    if platform.system() == "Darwin" and platform.machine() == "arm64":
        return {"vendor": "apple", "name": "Apple silicon (unified memory)", "vram_gb": None}
    return {"vendor": None, "name": "none detected", "vram_gb": None}


def playwright() -> str:
    if importlib.util.find_spec("playwright") is None:
        return "not installed (pip install playwright && python -m playwright install chromium)"
    probe = ("from playwright.sync_api import sync_playwright\n"
             "with sync_playwright() as p:\n b=p.chromium.launch(); print(b.version); b.close()")
    v = run([sys.executable, "-c", probe], timeout=60)
    return f"ok (Chromium {v})" if v and v[0].isdigit() else "installed, Chromium missing (python -m playwright install chromium)"


def tts_engines() -> list[str]:
    try:
        r = subprocess.run([sys.executable, str(HERE / "tts.py"), "engines"], capture_output=True, text=True, timeout=180)
        return [ln[2:].split(" licence")[0].strip() for ln in r.stdout.splitlines() if ln.startswith("- ")]
    except Exception:  # noqa: BLE001
        return ["tts.py could not run"]


def fonts_snapshot() -> str:
    p = HERE / "data" / "google-fonts.json"
    if not p.is_file():
        return "missing (python fonts.py refresh)"
    fetched = json.loads(p.read_text(encoding="utf-8")).get("fetched", "")
    try:
        age = (dt.date.today() - dt.date.fromisoformat(fetched)).days
    except ValueError:
        age = -1
    return f"{fetched} ({age} days old{'; run python fonts.py refresh' if age > 90 else ''})"


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        pass
    g = gpu()
    disk = shutil.disk_usage(Path.cwd())
    rep = {
        "os": f"{platform.system()} {platform.release()} {platform.machine()}",
        "python": platform.python_version(),
        "node": run(["node", "--version"]) or "not found",
        "ffmpeg": (run(["ffmpeg", "-version"]).split(" Copyright")[0] or "not found"),
        "ffprobe": "ok" if shutil.which("ffprobe") else "not found",
        "playwright": playwright(),
        "gpu": g,
        "disk_free_gb": round(disk.free / 1e9, 1),
        "blender": run(["blender", "--version"]) or "not found",
        "imagemagick": run(["magick", "-version"]) or "not found",
        "tts": tts_engines(),
        "api_keys_set": [k for k in KEYS if os.environ.get(k)],
        "fonts_snapshot": fonts_snapshot(),
    }
    # speech-to-text (tts.py check / words): this interpreter, a whisper CLI, or faster-whisper in the registered TTS home
    stt_home = any(t.lstrip("- ").startswith("whisper") and "installed" in t and "not installed" not in t for t in rep["tts"])
    rep["whisper"] = ("ok" if (importlib.util.find_spec("whisper") or importlib.util.find_spec("faster_whisper") or shutil.which("whisper"))
                      else "ok (faster-whisper in the TTS home)" if stt_home else "not found")
    can, ask = [], []
    can.append("render and inspect pages (verify_page.py)" if rep["playwright"].startswith("ok") else "static checks only: no browser verification until Playwright + Chromium are installed")
    if "not found" in rep["ffmpeg"]:
        ask.append("FFmpeg is missing: video export, loudness and captions need it")
    else:
        can.append("video render/export, loudness measurement, captions (FFmpeg)")
    vram = g.get("vram_gb") or 0
    if g["vendor"] == "nvidia" and vram >= 6:
        can.append(f"local GPU models on {g['name']} ({vram} GB): Qwen3-TTS 1.7B, Chatterbox, small image/video models")
    elif g["vendor"] == "nvidia":
        can.append(f"small local GPU models only ({vram} GB): Qwen3-TTS 0.6B, Kokoro")
    else:
        can.append("CPU-only local models: Kokoro, Kitten TTS 2 (slower), Piper; generative image/video needs a cloud option")
    installed = [t for t in rep["tts"] if "not installed" not in t and "needs " not in t]
    if not any(t.split()[0] in ("qwen3", "kitten2", "chatterbox", "kokoro") for t in installed):
        ask.append("no natural-sounding local TTS installed: ask before installing one (tts.py install <engine>)")
    if rep["api_keys_set"]:
        can.append("provider keys present (names only): " + ", ".join(rep["api_keys_set"]))
    if "--json" in sys.argv:
        print(json.dumps({**rep, "can": can, "ask": ask}, indent=2))
        return 0
    print("DENT doctor")
    for k, v in rep.items():
        if k == "tts":
            print("tts engines:")
            for t in v:
                print(f"  - {t}")
        elif k == "gpu":
            print(f"gpu: {v['name']}" + (f" ({v['vram_gb']} GB)" if v.get("vram_gb") else ""))
        else:
            print(f"{k}: {v if v else 'none'}")
    print("\nCan do now:")
    for c in can:
        print(f"  + {c}")
    print("Needs a decision or install:" if ask else "Nothing blocking.")
    for c in ask:
        print(f"  ? {c}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

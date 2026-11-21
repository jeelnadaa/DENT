#!/usr/bin/env python3
"""Regression tests for DENT's runnable tools.

- contrast.py: known ratios
- palette.py: cliché detection, generated palettes and every color.md library palette pass contrast in both themes
- fonts.py: overuse flags, suggestions, every pairing face exists on Google Fonts and is not overused
- tts.py: engine listing, install needs --yes, post (loudness, captions, timing) on synthetic tones
- doctor.py: JSON capability report
- verify_page.py (run with --surfaces match): evals/fixtures/bad.html must fail G2, G3, G4, G8_surfaces, G10, G11,
  G13 (each MWG rule and default surface it has);
  good.html must pass all (including a slowed progress spinner under reduced motion)
  (skipped with a clear message if Playwright/Chromium isn't installed)

Run: python scripts/test_tools.py   (exit 1 on failure)
Copyright 2026 Jeel Nada (solarquack). Licensed under the Apache License 2.0.
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "skills" / "dent" / "scripts"
FIX = ROOT / "evals" / "fixtures"
failures: list[str] = []


def check(cond: bool, msg: str) -> None:
    print(("  ok    " if cond else "  FAIL  ") + msg)
    if not cond:
        failures.append(msg)


def test_contrast() -> None:
    print("contrast.py")
    sys.path.insert(0, str(SCRIPTS))
    import contrast  # noqa: E402
    check(abs(contrast.ratio("#000000", "#FFFFFF") - 21.0) < 0.01, "black on white = 21:1")
    check(abs(contrast.ratio("#777777", "#FFFFFF") - 4.48) < 0.02, "#777 on white ≈ 4.48:1 (fails AA)")
    r = subprocess.run([sys.executable, str(SCRIPTS / "contrast.py"), "#767676:#FFFFFF"], capture_output=True, text=True)
    check(r.returncode == 0, "#767676 on white passes AA (exit 0)")


def run_verify(page: Path) -> dict | None:
    with tempfile.TemporaryDirectory() as out:
        r = subprocess.run([sys.executable, str(SCRIPTS / "verify_page.py"), str(page), "--out", out,
                            "--no-screenshots", "--widths", "390", "1024", "--surfaces", "match"], capture_output=True, text=True)
        if r.returncode == 2:
            print("  skip  verify_page.py could not run: " + (r.stdout.strip().splitlines() or ["?"])[-1])
            return None
        return json.loads((Path(out) / "report.json").read_text(encoding="utf-8"))


def test_verify() -> None:
    print("verify_page.py")
    bad = run_verify(FIX / "bad.html")
    if bad is None:
        return
    g = bad["gates"]
    for gate in ("G2_layout", "G3_contrast_sample", "G4_operability_auto", "G10_reduced_motion", "G11_no_autoplay_audio",
                 "G13_modern_web_auto", "G8_surfaces"):
        check(g.get(gate) == "Failed", f"bad.html fails {gate}")
    missing = set(bad.get("surfaces", {}).get("missing", []))
    for s in ("title tooltips", "range slider", "checkbox"):
        check(s in missing, f"bad.html: G8_surfaces flags {s}")
    rules = {f["rule"] for f in bad.get("mwg", {}).get("fails", [])}
    for rule in ("mwg:motion", "mwg:optimize-image-priority", "mwg:dialog", "mwg:sms-otp-form"):
        check(rule in rules, f"bad.html: G13 flags {rule}")
    good = run_verify(FIX / "good.html")
    for gate, verdict in good["gates"].items():
        check(verdict == "Passed", f"good.html passes {gate}")
    check(good.get("motion", {}).get("running_reduced", 0) >= 1, "good.html keeps its slowed progress spinner under reduced motion (allowed)")
    check(not good.get("mwg", {}).get("warns"), "good.html: no Modern Web Guidance warnings")
    with tempfile.TemporaryDirectory() as out:
        subprocess.run([sys.executable, str(SCRIPTS / "verify_page.py"), str(FIX / "scroll-driven.html"), "--out", out, "--widths", "390"],
                       capture_output=True, text=True)
        rep = json.loads((Path(out) / "report.json").read_text(encoding="utf-8")) if (Path(out) / "report.json").is_file() else {}
        check(rep.get("screenshot_mode", "").startswith("reduced-motion") and (Path(out) / "page-390.jpg").is_file(),
              "scroll-driven page: screenshots taken with reduced motion so below-the-fold content is visible")
    inv = good.get("motion_inventory", {})
    check(inv.get("keyframes", 0) >= 1 and inv.get("reducedMotionQueries", 0) >= 1 and inv.get("transitionRules", -1) >= 0,
          "motion inventory reports keyframes and reduced-motion queries")


REFS = ROOT / "skills" / "dent" / "references"


def test_palette() -> None:
    print("palette.py")
    sys.path.insert(0, str(SCRIPTS))
    import palette as P  # noqa: E402
    check(P.cliche_hits({"accent": "#6366F1"}) != [], "flags Tailwind indigo-500 as a cliché")
    check(any("combination" in h for h in P.cliche_hits({"bg": "#F7F5F0", "accent": "#C2410C"})), "flags cream + terracotta combination")
    check(any("zinc" in h for h in P.cliche_hits({"bg": "#09090B"})), "flags zinc-950 dark background")
    check(P.cliche_hits({"bg": "#FFFFFF", "accent": "#1F6F5C"}) == [], "white + kelp green is not a cliché")
    for seed in ("#F2C230", "#1F6F5C", "#E3582B", "#8FCF73"):
        p = P.build(seed, None, None, "tinted", None)
        ok = all(all(r[3] for r in P.report({k: v for k, v in t.items() if not k.startswith("_")})) for t in p["themes"].values())
        check(ok, f"make --accent {seed}: every role pair passes in light and dark")
    # every palette in the color.md library passes and has no cliché
    text = (REFS / "color.md").read_text(encoding="utf-8")
    rows = re.findall(r"^\| (light|dark) \| (.+) \|$", text, re.M)
    keys = ("brand", "bg", "surface", "text", "muted", "accent", "on-accent", "accent-text", "second")
    bad = 0
    for mode, cells in rows:
        vals = [c.strip().strip("`") for c in cells.split("|")]
        t = dict(zip(keys, vals))
        fails = [x for x in P.report(t) if not x[3]]
        hits = P.cliche_hits({k: v for k, v in t.items() if k in ("bg", "surface", "accent", "second")})
        bad += bool(fails or hits)
    check(len(rows) >= 40 and bad == 0, f"color.md library: {len(rows)} theme rows, {bad} with a contrast failure or cliché")
    r = subprocess.run([sys.executable, str(SCRIPTS / "palette.py"), "check", "bg=#FFFFFF", "text=#BBBBBB"], capture_output=True, text=True)
    check(r.returncode == 1, "check exits 1 on a contrast failure")


def test_fonts() -> None:
    print("fonts.py")
    sys.path.insert(0, str(SCRIPTS))
    import fonts as F  # noqa: E402
    data = {f["f"]: f for f in F.load()["families"]}
    check(len(data) > 1500, f"Google Fonts snapshot has {len(data)} families")
    r = subprocess.run([sys.executable, str(SCRIPTS / "fonts.py"), "check", "Satoshi"], capture_output=True, text=True)
    check(r.returncode == 1 and "OVERUSED" in r.stdout, "check flags Satoshi as overused (exit 1)")
    r = subprocess.run([sys.executable, str(SCRIPTS / "fonts.py"), "suggest", "--role", "display", "--axes", "wdth", "--limit", "5"],
                       capture_output=True, text=True)
    check(r.returncode == 0 and "candidates" in r.stdout and not any(n in r.stdout for n in F.OVERUSED), "suggest excludes overused fonts")
    # every free face named in the typography pairing table exists on Google Fonts and is not overused
    typo = (REFS / "typography.md").read_text(encoding="utf-8")
    table = typo.split("## 3. Pairing library", 1)[1].split("\n## 4.", 1)[0]
    names = set(re.findall(r"\*\*([A-Z][A-Za-z0-9 ]+?)\*\*", table))
    missing = sorted(n for n in names if n not in data)
    overused = sorted(n for n in names if n in F.OVERUSED)
    check(not missing, f"pairing faces on Google Fonts ({len(names)} checked){': missing ' + ', '.join(missing) if missing else ''}")
    check(not overused, f"no overused face in the pairing library{': ' + ', '.join(overused) if overused else ''}")


def _tone(path: Path, seconds: float, freq: float, sr: int = 24000, amp: float = 0.3) -> None:
    import math
    import struct
    import wave
    n = int(seconds * sr)
    frames = b"".join(struct.pack("<h", int(amp * 32767 * math.sin(2 * math.pi * freq * i / sr))) for i in range(n))
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(b"\x00\x00" * int(0.3 * sr) + frames + b"\x00\x00" * int(0.3 * sr))


def test_tts() -> None:
    print("tts.py")
    r = subprocess.run([sys.executable, str(SCRIPTS / "tts.py"), "engines"], capture_output=True, text=True, timeout=300)
    check(r.returncode == 0 and "qwen3" in r.stdout and "kitten2" in r.stdout, "engines lists the local engines")
    r = subprocess.run([sys.executable, str(SCRIPTS / "tts.py"), "install", "kokoro"], capture_output=True, text=True)
    check(r.returncode == 2 and "Ask the user first" in r.stdout, "install without --yes only prints commands (exit 2)")
    if not shutil.which("ffmpeg"):
        print("  skip  post: ffmpeg not installed")
        return
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        lines = d / "lines"
        lines.mkdir()
        texts = ["Meet Quill, the notebook that thinks in outlines and keeps every idea you capture in one calm place.", "Write first."]
        for i, (t, f) in enumerate(zip(texts, (220, 330)), 1):
            _tone(lines / f"line_{i:03d}.wav", 2.0 + i, f)
            (lines / f"line_{i:03d}.txt").write_text(t, encoding="utf-8")
        out = d / "narration.wav"
        r = subprocess.run([sys.executable, str(SCRIPTS / "tts.py"), "post", "--in", str(lines), "--out", str(out), "--lufs", "-16",
                            "--srt", str(d / "n.srt"), "--vtt", str(d / "n.vtt")], capture_output=True, text=True, timeout=300)
        check(r.returncode == 0 and "PASS" in r.stdout, "post masters to -16 LUFS within 1 LU and true peak <= -1.5 dBTP")
        srt = (d / "n.srt").read_text(encoding="utf-8") if (d / "n.srt").is_file() else ""
        cue_lines = [ln for ln in srt.splitlines() if ln and not ln[0].isdigit()]
        check(srt.count("-->") >= 2 and all(len(ln) <= 42 for ln in cue_lines), "captions: cues written, every line <= 42 characters")
        timing = json.loads(out.with_suffix(".timing.json").read_text(encoding="utf-8")) if out.with_suffix(".timing.json").is_file() else []
        check(len(timing) == 2 and timing[1]["start"] > timing[0]["end"], "timing JSON has ordered, gapped lines")
        check((d / "n.vtt").read_text(encoding="utf-8").startswith("WEBVTT"), "VTT has a WEBVTT header")
        slow = d / "slow.wav"
        r = subprocess.run([sys.executable, str(SCRIPTS / "tts.py"), "post", "--in", str(lines), "--out", str(slow), "--tempo", "0.8"],
                           capture_output=True, text=True, timeout=300)
        t2 = json.loads(slow.with_suffix(".timing.json").read_text(encoding="utf-8")) if slow.with_suffix(".timing.json").is_file() else []
        span = lambda tm: tm[0]["end"] - tm[0]["start"] if tm else 0  # noqa: E731
        check(r.returncode == 0 and span(t2) > span(timing) * 1.15, "post --tempo 0.8 slows lines (pitch-preserving) and still passes loudness")


def test_doctor() -> None:
    print("doctor.py")
    r = subprocess.run([sys.executable, str(SCRIPTS / "doctor.py"), "--json"], capture_output=True, text=True, timeout=600)
    try:
        rep = json.loads(r.stdout)
    except Exception:  # noqa: BLE001
        rep = {}
    check(r.returncode == 0 and "can" in rep and "gpu" in rep and "api_keys_set" in rep, "doctor --json reports capabilities")
    check(all(not isinstance(v, str) or "sk-" not in v for v in rep.values()), "doctor never prints key values")


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        pass
    test_contrast()
    test_palette()
    test_fonts()
    test_tts()
    test_doctor()
    test_verify()
    print(f"\n{len(failures)} failure(s)" if failures else "\nAll tool tests passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())

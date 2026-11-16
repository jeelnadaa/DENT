#!/usr/bin/env python3
"""Regression tests for DENT's runnable tools.

- contrast.py: known ratios
- verify_page.py (run with --surfaces match): evals/fixtures/bad.html must fail G2, G3, G4, G8_surfaces, G10, G11,
  G13 (each MWG rule and default surface it has);
  good.html must pass all (including a slowed progress spinner under reduced motion)
  (skipped with a clear message if Playwright/Chromium isn't installed)

Run: python scripts/test_tools.py   (exit 1 on failure)
Copyright 2026 Jeel Nada (solarquack). Licensed under the Apache License 2.0.
"""
from __future__ import annotations

import json
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
    inv = good.get("motion_inventory", {})
    check(inv.get("keyframes", 0) >= 1 and inv.get("reducedMotionQueries", 0) >= 1 and inv.get("transitionRules", -1) >= 0,
          "motion inventory reports keyframes and reduced-motion queries")


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        pass
    test_contrast()
    test_verify()
    print(f"\n{len(failures)} failure(s)" if failures else "\nAll tool tests passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())

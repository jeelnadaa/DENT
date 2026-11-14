#!/usr/bin/env python3
"""DENT contrast: WCAG 2.x contrast ratios for color pairs or CSS custom properties.

Usage:
  python contrast.py "#1A1A1A:#FFFFFF" "#6B7280:#F9FAFB"
  python contrast.py --css tokens.css "--text:--bg" "--muted:--bg" "--on-accent:--accent"
  python contrast.py --css styles.css --auto        # every --*text*/--*fg* var against every --*bg*/--*surface* var

Prints ratio and AA/AAA verdicts (normal text 4.5, large text 3, UI 3). Exit 1 if any pair fails AA normal
(use --large or --ui to judge pairs against 3:1 instead). No dependencies.
Copyright 2026 Jeel Nada (solarquack). Licensed under the Apache License 2.0.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def parse_color(c: str) -> tuple[float, float, float]:
    c = c.strip().lower()
    if c.startswith("#"):
        h = c[1:]
        if len(h) in (3, 4):
            h = "".join(ch * 2 for ch in h[:3])
        return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))  # type: ignore[return-value]
    m = re.match(r"rgba?\(([^)]+)\)", c)
    if m:
        parts = [float(x) for x in re.split(r"[ ,/]+", m.group(1).strip()) if x][:3]
        return tuple(v / 255 for v in parts)  # type: ignore[return-value]
    raise ValueError(f"Unsupported color: {c} (use #hex or rgb())")


def luminance(rgb) -> float:
    def f(v):
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (f(v) for v in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(a: str, b: str) -> float:
    l1, l2 = sorted((luminance(parse_color(a)), luminance(parse_color(b))), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


def css_vars(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    out = {}
    for name, value in re.findall(r"(--[\w-]+)\s*:\s*([^;}{]+)", text):
        v = value.strip()
        if re.match(r"^(#[0-9a-fA-F]{3,8}|rgba?\()", v):
            out.setdefault(name, v)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pairs", nargs="*", help="fg:bg pairs (#hex or --var names with --css)")
    ap.add_argument("--css", type=Path, help="CSS file with custom properties")
    ap.add_argument("--auto", action="store_true", help="check text-like vars against background-like vars")
    ap.add_argument("--large", action="store_true", help="judge against 3:1 (large text)")
    ap.add_argument("--ui", action="store_true", help="judge against 3:1 (UI components, focus rings)")
    args = ap.parse_args()

    vars_ = css_vars(args.css) if args.css else {}
    pairs = []
    for p in args.pairs:
        fg, bg = p.split(":", 1) if not p.startswith("--") else re.match(r"(--[\w-]+):(--[\w-]+)", p).groups()
        pairs.append((fg, bg))
    if args.auto and vars_:
        fgs = [k for k in vars_ if re.search(r"text|fg|ink|foreground|on-", k)]
        bgs = [k for k in vars_ if re.search(r"bg|background|surface|paper|canvas", k)]
        pairs += [(f, b) for f in fgs for b in bgs]
    if not pairs:
        ap.print_help()
        return 2

    need = 3.0 if (args.large or args.ui) else 4.5
    failed = 0
    print(f"{'pair':<40} {'ratio':>7}  AA({need})  AAA-normal(7)")
    for fg, bg in pairs:
        cf, cb = vars_.get(fg, fg), vars_.get(bg, bg)
        try:
            r = ratio(cf, cb)
        except ValueError as e:
            print(f"{fg}:{bg:<30} skipped ({e})")
            continue
        ok = r >= need
        failed += not ok
        print(f"{(fg + ' on ' + bg)[:40]:<40} {r:>6.2f}:1  {'pass' if ok else 'FAIL':<8} {'pass' if r >= 7 else '-'}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

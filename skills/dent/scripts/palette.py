#!/usr/bin/env python3
"""DENT palette builder: concept-led palettes in OKLCH with contrast checks and a cliché detector.

  python palette.py make --accent "#1F6F5C" --second "#E2A33B" --neutral warm --name "Kelp & Brass"
  python palette.py make --hue 25 --chroma 0.17 --neutral cool --css          # CSS custom properties, both themes
  python palette.py check bg=#F7F5F0 text=#1F2A37 accent=#C2410C             # contrast + cliché report

What `make` does (color.md §5 and Part 2 explain the design side):
  1. Accent scale 50-950 from the seed in OKLCH (perceptually even steps, gamut-mapped by lowering chroma).
  2. Neutrals tinted toward the accent (or warm / cool / pure), never flat zinc or slate.
  3. Role tokens for light AND dark: bg, surface, raised, border, text, muted, accent (fill), on-accent,
     accent-text (links, small accent text), second (optional), focus.
  4. Every text pair is checked against WCAG 2.2 (text 4.5:1, UI and focus 3:1); a failing role is moved
     along its scale until it passes, and the report says so.
  5. Each color is compared with the 2026 cliché registry (Tailwind indigo/violet, zinc backgrounds,
     cream + terracotta, acid lime on black...). A hit is not banned; it must be a logged decision.

Exit code 1 when `check` finds a contrast failure. Pure standard library.
Copyright 2026 Jeel Nada (solarquack). Licensed under the Apache License 2.0.
"""
from __future__ import annotations

import argparse
import math
import sys

# ---------- colour maths (sRGB <-> OKLab/OKLCH, WCAG luminance) ----------

def _lin(c: float) -> float:
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def _gam(c: float) -> float:
    return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055


def hex_to_rgb(h: str) -> tuple[float, float, float]:
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(ch * 2 for ch in h)
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))  # type: ignore[return-value]


def rgb_to_hex(rgb) -> str:
    return "#" + "".join(f"{round(min(1, max(0, c)) * 255):02X}" for c in rgb)


def rgb_to_oklab(rgb):
    r, g, b = (_lin(c) for c in rgb)
    l_ = (0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b) ** (1 / 3)
    m_ = (0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b) ** (1 / 3)
    s_ = (0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b) ** (1 / 3)
    return (0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_,
            1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_,
            0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_)


def oklab_to_rgb_linear(lab):
    L, a, b = lab
    l_ = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m_ = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s_ = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    return (4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_,
            -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_,
            -0.0041960863 * l_ - 0.7034186147 * m_ + 1.7076147010 * s_)


def oklch_to_hex(L: float, C: float, H: float) -> str:
    """Gamut-map by reducing chroma until the colour fits sRGB."""
    for _ in range(40):
        a, b = C * math.cos(math.radians(H)), C * math.sin(math.radians(H))
        lin = oklab_to_rgb_linear((L, a, b))
        if all(-1e-4 <= c <= 1 + 1e-4 for c in lin):
            return rgb_to_hex(tuple(_gam(min(1, max(0, c))) for c in lin))
        C *= 0.93
    return rgb_to_hex(tuple(_gam(min(1, max(0, c))) for c in oklab_to_rgb_linear((L, 0, 0))))


def hex_to_oklch(h: str):
    L, a, b = rgb_to_oklab(hex_to_rgb(h))
    return L, math.hypot(a, b), math.degrees(math.atan2(b, a)) % 360


def luminance(h: str) -> float:
    r, g, b = (_lin(c) for c in hex_to_rgb(h))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a: str, b: str) -> float:
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def delta(a: str, b: str) -> float:
    """OKLab distance with the chroma axes weighted x3, so a tint (cream vs mint) counts as different."""
    la, lb = rgb_to_oklab(hex_to_rgb(a)), rgb_to_oklab(hex_to_rgb(b))
    return math.sqrt((la[0] - lb[0]) ** 2 + (3 * (la[1] - lb[1])) ** 2 + (3 * (la[2] - lb[2])) ** 2)

# ---------- cliché registry (2026) ----------

CLICHES = [
    ("#6366F1", "Tailwind indigo-500: the loudest AI-template tell"), ("#4F46E5", "Tailwind indigo-600"),
    ("#8B5CF6", "Tailwind violet-500"), ("#7C3AED", "Tailwind violet-600"), ("#A78BFA", "Tailwind violet-400"),
    ("#9333EA", "Tailwind purple-600"), ("#2563EB", "Tailwind blue-600 'bright blue CTA'"), ("#3B82F6", "Tailwind blue-500"),
    ("#2DD4BF", "Tailwind teal-400"), ("#10B981", "Tailwind emerald-500 'fintech green'"), ("#22D3EE", "Tailwind cyan-400 glow"),
    ("#C2410C", "burnt orange / terracotta accent"), ("#B46F4D", "terracotta accent"),
    ("#C85A32", "terracotta accent"), ("#D97757", "clay orange accent"), ("#C8F169", "acid lime on black"), ("#D1FF48", "acid lime on black"),
    ("#FF5C00", "safety orange on navy (the 'bold' default)"),
]
CLICHE_DISTANCE = 0.04  # OKLab distance treated as "the same colour"


def _is_cream(v: str) -> bool:
    L, C, H = hex_to_oklch(v)
    return L > 0.92 and 0.006 < C < 0.04 and 55 < H < 105


def _is_zinc(v: str) -> bool:
    L, C, H = hex_to_oklch(v)
    return L < 0.25 and 0.003 < C < 0.03 and 250 < H < 295


def cliche_hits(colors: dict[str, str]) -> list[str]:
    """colors: role -> hex, only the identity roles (bg, surface, accent, second)."""
    hits = []
    for role, c in colors.items():
        if role in ("bg", "surface"):
            if _is_cream(c):
                hits.append(f"{role} {c}: cream/sand paper background (the 'warm editorial' default)")
            if _is_zinc(c):
                hits.append(f"{role} {c}: zinc/slate blue-grey dark background (the dark-SaaS default)")
            continue
        for ref, why in CLICHES:
            if delta(c, ref) < CLICHE_DISTANCE:
                hits.append(f"{role} {c} ~ {ref}: {why}")
    vals = list(colors.values())
    terra = any(0.5 < hex_to_oklch(v)[0] < 0.72 and hex_to_oklch(v)[1] > 0.1 and 28 < hex_to_oklch(v)[2] < 62 for v in vals)
    if terra and any(_is_cream(v) for v in vals):
        hits.append("combination: cream background + terracotta/orange accent (the 2025-26 'tasteful AI' look)")
    return hits


# ---------- palette generation ----------

STEPS = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950]
LIGHT = [0.975, 0.945, 0.885, 0.805, 0.715, 0.635, 0.555, 0.48, 0.405, 0.335, 0.26]
CHROMA_CURVE = [0.18, 0.3, 0.55, 0.8, 0.95, 1.0, 1.0, 0.92, 0.8, 0.66, 0.5]


def scale(L0: float, C0: float, H: float) -> dict[int, str]:
    return {s: oklch_to_hex(l, C0 * k, H) for s, l, k in zip(STEPS, LIGHT, CHROMA_CURVE)}


def neutral_scale(H: float, C: float) -> dict[int, str]:
    lights = [0.982, 0.958, 0.915, 0.855, 0.72, 0.58, 0.47, 0.38, 0.30, 0.235, 0.195]
    tint = [0.45, 0.55, 0.7, 0.85, 1, 1, 1, 1, 0.95, 0.9, 0.85]  # quieter tint at the very light end
    return {s: oklch_to_hex(l, C * k, H) for s, l, k in zip(STEPS, lights, tint)}


def pick(scale_: dict[int, str], against: str, ratio: float, order: list[int]) -> tuple[int, str]:
    for s in order:
        if contrast(scale_[s], against) >= ratio:
            return s, scale_[s]
    s = order[-1]
    return s, scale_[s]


def build(accent: str | None, hue: float | None, chroma: float | None, neutral: str, second: str | None) -> dict:
    if accent:
        L0, C0, H0 = hex_to_oklch(accent)
    else:
        L0, C0, H0 = 0.6, chroma if chroma is not None else 0.15, hue if hue is not None else 250
    acc = scale(L0, C0, H0)
    nh, nc = {"tinted": (H0, 0.012), "warm": (70, 0.014), "cool": (240, 0.012), "pure": (H0, 0.0)}[neutral]
    neu = neutral_scale(nh, nc)
    sec = scale(*hex_to_oklch(second)) if second else None
    # the accent step closest to the seed is the brand fill
    seed_step = min(STEPS, key=lambda s: abs(LIGHT[STEPS.index(s)] - L0)) if accent else 600
    themes = {}
    for mode in ("light", "dark"):
        if mode == "light":
            bg, surface, raised, border = neu[50], "#FFFFFF" if neutral == "pure" else oklch_to_hex(0.995, nc / 2, nh), neu[100], neu[200]
            text = neu[950]
            _, muted = pick(neu, bg, 4.5, [600, 700, 800, 900])
            fill_order = [seed_step] + [s for s in (600, 700, 500, 800) if s != seed_step]
            _, accent_text = pick(acc, bg, 4.5, [600, 700, 800, 900])
        else:
            bg, surface, raised, border = neu[950], neu[900], neu[800], oklch_to_hex(0.33, nc, nh)
            text = neu[50]
            _, muted = pick(neu, bg, 4.5, [400, 300, 200])
            fill_order = [s for s in (400, 300, 500, seed_step) if True]
            _, accent_text = pick(acc, bg, 4.5, [400, 300, 200, 100])
        light_on, dark_on = surface if mode == "light" else neu[50], neu[950]

        def label(f: str) -> str:
            return light_on if contrast(light_on, f) >= contrast(dark_on, f) else dark_on

        note = ""
        pool = dict(acc)
        if accent:
            pool["seed"] = accent.upper() if accent.startswith("#") else "#" + accent.upper()
        candidates = (["seed"] if accent else []) + fill_order + [s for s in STEPS if s not in fill_order]
        fill, on = pool[candidates[0]], label(pool[candidates[0]])
        for s in candidates:  # first candidate that passes label 4.5:1 AND shape 3:1 against the background
            f2 = pool[s]
            if contrast(label(f2), f2) >= 4.5 and contrast(f2, bg) >= 3.0:
                if s != candidates[0]:
                    note = f"accent fill moved to step {s} (seed step fails 4.5:1 label or 3:1 against the background); use `brand` for large decorative areas"
                fill, on = f2, label(f2)
                break
        if accent and contrast(pool["seed"], bg) >= 4.5:
            accent_text = pool["seed"]
        t = {"brand": pool["seed"] if accent else fill, "bg": bg, "surface": surface, "raised": raised, "border": border, "text": text, "muted": muted,
             "accent": fill, "on-accent": on, "accent-text": accent_text, "focus": accent_text}
        if sec:
            _, t["second"] = pick(sec, bg, 3.0, [500, 600, 700] if mode == "light" else [400, 300, 200])
        t["_note"] = note
        themes[mode] = t
    return {"accent_scale": acc, "neutral_scale": neu, "second_scale": sec, "themes": themes}


PAIRS = [("text", "bg", 4.5), ("text", "surface", 4.5), ("muted", "bg", 4.5), ("muted", "surface", 4.5),
         ("on-accent", "accent", 4.5), ("accent-text", "bg", 4.5), ("focus", "bg", 3.0), ("accent", "bg", 3.0),
         ("second", "bg", 3.0)]


def report(tokens: dict[str, str]) -> list[tuple[str, float, float, bool]]:
    rows = []
    for a, b, need in PAIRS:
        if a in tokens and b in tokens:
            r = contrast(tokens[a], tokens[b])
            rows.append((f"{a} on {b}", r, need, r >= need))
    return rows


def cmd_make(a) -> int:
    p = build(a.accent, a.hue, a.chroma, a.neutral, a.second)
    name = a.name or "palette"
    fails = 0
    print(f"## {name}")
    print("accent " + " ".join(f"{s}:{h}" for s, h in p["accent_scale"].items()))
    print("neutral " + " ".join(f"{s}:{h}" for s, h in p["neutral_scale"].items()))
    for mode, t in p["themes"].items():
        tokens = {k: v for k, v in t.items() if not k.startswith("_")}
        print(f"\n### {mode}")
        print(" ".join(f"{k}={v}" for k, v in tokens.items()))
        if t["_note"]:
            print(f"note: {t['_note']}")
        for label, r, need, ok in report(tokens):
            fails += not ok
            print(f"  {'ok  ' if ok else 'FAIL'} {label}: {r:.2f}:1 (needs {need})")
        hits = cliche_hits({k: v for k, v in tokens.items() if k in ('bg', 'accent', 'second', 'surface')})
        for h in hits:
            print(f"  cliche: {h}")
        if not hits:
            print("  cliché check: none")
        if a.css:
            sel = ":root" if mode == "light" else "@media (prefers-color-scheme: dark) { :root"
            body = "\n".join(f"  --color-{k}: {v};" for k, v in tokens.items())
            print(f"{sel} {{\n{body}\n}}" + (" }" if mode == "dark" else ""))
    return 1 if fails else 0


def cmd_check(a) -> int:
    tokens = dict(x.split("=", 1) for x in a.pairs)
    fails = 0
    for label, r, need, ok in report(tokens):
        fails += not ok
        print(f"{'ok  ' if ok else 'FAIL'} {label}: {r:.2f}:1 (needs {need})")
    for k in tokens:
        L, C, H = hex_to_oklch(tokens[k])
        print(f"  {k} {tokens[k]} = oklch({L * 100:.1f}% {C:.3f} {H:.0f})")
    hits = cliche_hits({k: v for k, v in tokens.items() if k in ("bg", "surface", "accent", "second")})
    for h in hits:
        print(f"cliche: {h}")
    if not hits:
        print("cliché check: none")
    return 1 if fails else 0


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        pass
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    m = sub.add_parser("make")
    m.add_argument("--accent", help="seed accent colour (hex)")
    m.add_argument("--hue", type=float, help="seed hue 0-360 when no accent is given")
    m.add_argument("--chroma", type=float, help="seed chroma (0.04 muted ... 0.25 vivid)")
    m.add_argument("--second", help="optional second colour (hex) for illustration/data")
    m.add_argument("--neutral", choices=["tinted", "warm", "cool", "pure"], default="tinted")
    m.add_argument("--name")
    m.add_argument("--css", action="store_true")
    c = sub.add_parser("check")
    c.add_argument("pairs", nargs="+", help="role=#hex (roles: bg surface text muted accent on-accent accent-text focus second)")
    a = ap.parse_args()
    return cmd_make(a) if a.cmd == "make" else cmd_check(a)


if __name__ == "__main__":
    sys.exit(main())

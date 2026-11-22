#!/usr/bin/env python3
"""DENT font finder: check fonts for overuse, licence and script support, and suggest fresh candidates.

Uses Google Fonts' own metadata (popularity rank, date added, variable axes, scripts, weights).
A bundled snapshot (scripts/data/google-fonts.json) works offline; `refresh` updates it from
https://fonts.google.com/metadata/fonts.

  python fonts.py check "Hedvig Letters Serif" "Satoshi" "Inter"
  python fonts.py suggest --role display --axes wdth --script latin-ext --limit 12
  python fonts.py suggest --role body --fresh            # added in the last ~2 years
  python fonts.py refresh                                # update the snapshot (needs network)

Every family on Google Fonts is open source (OFL, Apache-2.0 or UFL); the licence directory is
confirmed per family by `check --verify` against github.com/google/fonts. Fonts that are not on
Google Fonts (Fontshare, Velvetyne, paid foundries) are reported as "not on Google Fonts: check
the foundry licence".

Copyright 2026 Jeel Nada (solarquack). Licensed under the Apache License 2.0.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
import urllib.request
from pathlib import Path

DATA = Path(__file__).resolve().parent / "data" / "google-fonts.json"
META_URL = "https://fonts.google.com/metadata/fonts"

# Fonts that read as "default" or "AI-generated" in 2026 when picked without a reason.
# First-order: the template defaults. Second-order: the fonts every "avoid the AI look" guide recommends,
# which made them the new default. Any of these is allowed only as a logged decision (typography.md §0).
OVERUSED = {
    # first order
    "Inter": "the default of defaults", "Roboto": "Android/system default", "Open Sans": "2010s default",
    "Lato": "2010s default", "Montserrat": "template default", "Poppins": "template default",
    "Arial": "system default", "Helvetica": "system default", "Nunito Sans": "template default",
    "Source Sans 3": "template default", "Raleway": "template default", "Playfair Display": "default 'luxury' serif",
    "Bebas Neue": "default condensed display", "Anton": "default condensed display", "Oswald": "default condensed display",
    # operating-system fonts reached for because they are installed (rendered with GDI/PIL in DENT's weakest test films)
    "Impact": "system default display", "Georgia": "system default serif", "Times New Roman": "system default serif",
    "Consolas": "system default mono", "Courier New": "system default mono", "Verdana": "system default",
    "Tahoma": "system default", "Segoe UI": "system UI default", "Calibri": "Office default", "Cambria": "Office default",
    "Trebuchet MS": "system default", "Comic Sans MS": "system default", "Arial Black": "system default display",
    # second order (the "anti-slop" picks that became the slop)
    "Satoshi": "the default 'not Inter' grotesk", "General Sans": "Fontshare default", "Switzer": "Fontshare default",
    "Cabinet Grotesk": "default 'bold startup' display", "Clash Display": "default 'bold startup' display",
    "Clash Grotesk": "default 'bold startup' display", "DM Sans": "default 'friendly SaaS' sans",
    "Manrope": "default 'friendly SaaS' sans", "Plus Jakarta Sans": "default 'friendly SaaS' sans",
    "Space Grotesk": "default 'tech' grotesk", "Space Mono": "default 'tech' mono", "Geist": "default dev-tool sans",
    "Instrument Serif": "default 'elegant AI product' serif (italic word in the headline)",
    "Fraunces": "default 'warm editorial' serif", "Bricolage Grotesque": "default 'indie' grotesk",
    "Outfit": "default geometric", "Sora": "default geometric", "Urbanist": "default geometric", "Figtree": "default friendly sans",
}
COMMON_RANK = 40  # Google Fonts popularity rank at or above which a family is everywhere


def load() -> dict:
    if not DATA.is_file():
        sys.exit(f"missing {DATA}; run: python fonts.py refresh")
    return json.loads(DATA.read_text(encoding="utf-8"))


def refresh() -> int:
    req = urllib.request.Request(META_URL, headers={"User-Agent": "dent-fonts/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        text = r.read().decode("utf-8")
    d = json.loads(text[text.index("{"):])
    keep = {"latin", "latin-ext", "cyrillic", "greek", "vietnamese", "arabic", "hebrew", "devanagari", "bengali", "tamil",
            "telugu", "gujarati", "gurmukhi", "kannada", "malayalam", "thai", "japanese", "korean", "chinese-simplified",
            "chinese-traditional"}
    fams = [{"f": f["family"], "c": f["category"], "p": f["popularity"], "d": f.get("dateAdded", ""),
             "a": [a["tag"] for a in f.get("axes", [])], "s": sorted(set(f.get("subsets", [])) & keep),
             "w": sorted({int(k.rstrip("i")) for k in f.get("fonts", {}) if k.rstrip("i").isdigit()})}
            for f in d["familyMetadataList"]]
    DATA.parent.mkdir(parents=True, exist_ok=True)
    DATA.write_text(json.dumps({"source": META_URL, "fetched": dt.date.today().isoformat(), "families": fams},
                               separators=(",", ":"), ensure_ascii=False), encoding="utf-8")
    print(f"snapshot updated: {len(fams)} families")
    return 0


def verify_licence(family: str) -> str:
    d = family.replace(" ", "").lower()
    for lic in ("ofl", "apache", "ufl"):
        url = f"https://raw.githubusercontent.com/google/fonts/main/{lic}/{d}/METADATA.pb"
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "dent-fonts/1.0"}), timeout=20) as r:
                if r.status == 200:
                    return {"ofl": "OFL-1.1", "apache": "Apache-2.0", "ufl": "Ubuntu Font Licence"}[lic] + " (verified)"
        except Exception:  # noqa: BLE001
            continue
    return "not found in google/fonts (check manually)"


def verdict(f: dict | None, name: str) -> str:
    if name in OVERUSED:
        return f"OVERUSED: {OVERUSED[name]}; use only as a logged decision"
    if f and f["p"] <= COMMON_RANK:
        return f"COMMON: popularity rank {f['p']} on Google Fonts; fine for body text, weak as an identity face"
    return "fresh enough"


def check(names: list[str], do_verify: bool) -> int:
    fams = {f["f"].lower(): f for f in load()["families"]}
    bad = 0
    for n in names:
        f = fams.get(n.lower())
        name = f["f"] if f else n
        v = verdict(f, name)
        bad += v.startswith("OVERUSED")
        if f:
            lic = verify_licence(name) if do_verify else "open source (Google Fonts; --verify to confirm the directory)"
            print(f"{name}: {v}\n  category {f['c']}, rank {f['p']}, added {f['d']}, axes {','.join(f['a']) or 'static'}, "
                  f"weights {f['w'][0] if f['w'] else '?'}-{f['w'][-1] if f['w'] else '?'}, scripts {','.join(f['s'])}\n  licence: {lic}")
        else:
            print(f"{name}: {v}\n  not on Google Fonts: check the foundry licence (Fontshare = ITF Free Font Licence; paid foundries = desktop/web licence)")
    return 1 if bad else 0


ROLE_CATS = {"body": {"Sans Serif", "Serif"}, "display": {"Sans Serif", "Serif", "Display"},
             "serif": {"Serif"}, "sans": {"Sans Serif"}, "mono": {"Monospace"}, "hand": {"Handwriting"}}


def suggest(role: str, axes: list[str], scripts: list[str], fresh: bool, limit: int, min_rank: int, max_rank: int) -> int:
    data = load()
    today = dt.date.today()
    out = []
    for f in data["families"]:
        if f["c"] not in ROLE_CATS[role] or f["f"] in OVERUSED or f["f"].startswith("Noto "):
            continue
        if not (min_rank <= f["p"] <= max_rank):
            continue
        if any(a not in f["a"] for a in axes) or any(s not in f["s"] for s in scripts):
            continue
        if role == "body" and len(f["w"]) < 3 and "wght" not in f["a"]:
            continue  # body text needs a real weight range
        if fresh and f["d"] and (today - dt.date.fromisoformat(f["d"])).days > 730:
            continue
        out.append(f)
    out.sort(key=lambda f: (f["p"], f["f"]))
    print(f"{len(out)} candidates (snapshot {data['fetched']}; rank band {min_rank}-{max_rank}; overused list excluded)")
    for f in out[:limit]:
        print(f"  {f['f']:<28} {f['c']:<11} rank {f['p']:<5} added {f['d']}  axes {','.join(f['a']) or 'static':<14} scripts {','.join(s for s in f['s'] if s != 'latin')}")
    print("Render the top 3 with real copy in a style tile and choose by eye (typography.md §1).")
    return 0


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        pass
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check")
    c.add_argument("names", nargs="+")
    c.add_argument("--verify", action="store_true", help="confirm the licence directory on github.com/google/fonts")
    s = sub.add_parser("suggest")
    s.add_argument("--role", choices=sorted(ROLE_CATS), default="body")
    s.add_argument("--axes", default="", help="comma list of required variable axes, e.g. wdth,opsz")
    s.add_argument("--script", default="", help="comma list of required subsets, e.g. latin-ext,devanagari")
    s.add_argument("--fresh", action="store_true", help="only families added in the last two years")
    s.add_argument("--limit", type=int, default=15)
    s.add_argument("--min-rank", type=int, default=COMMON_RANK + 1, help="skip families more popular than this rank")
    s.add_argument("--max-rank", type=int, default=1600, help="skip very obscure families (thin support)")
    sub.add_parser("refresh")
    a = ap.parse_args()
    if a.cmd == "refresh":
        return refresh()
    if a.cmd == "check":
        return check(a.names, a.verify)
    split = lambda v: [x.strip() for x in v.split(",") if x.strip()]  # noqa: E731
    return suggest(a.role, split(a.axes), split(a.script), a.fresh, a.limit, a.min_rank, a.max_rank)


if __name__ == "__main__":
    sys.exit(main())

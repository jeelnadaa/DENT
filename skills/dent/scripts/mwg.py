#!/usr/bin/env python3
"""Offline lookup for Google's Modern Web Guidance (MWG) guides.

The official way to use MWG is its CLI (`npx -y modern-web-guidance@latest search|retrieve`),
which always serves the newest guides. Use this script only when that CLI can't run
(no network, no Node, sandbox without approval, or a shell bug). It searches the vendored
copy of the MWG skill that ships with DENT and prints the same shapes as the CLI:

  python scripts/mwg.py search "light dismiss dialog"     -> [{"id", "description"}, ...]
  python scripts/mwg.py retrieve dialog,motion             -> full guide text
  python scripts/mwg.py list                               -> every guide id + description
  python scripts/mwg.py info                               -> which copy and version is used

Guides refer to each other as `npx -y modern-web-guidance@latest retrieve "<id>"`; offline,
fetch those with `python scripts/mwg.py retrieve <id>`.

The MWG folder is found in this order: --dir, $MWG_DIR, `../modern-web-guidance` next to
this skill (plugin and installer layout), `vendor/modern-web-guidance` inside this skill
(zip and rules-file layout), then common agent skill folders.
Exit code: 0 ok, 1 unknown id / no results, 2 MWG copy not found.

Copyright 2026 Jeel Nada (solarquack). Licensed under the Apache License 2.0.
MWG content: the Google Chrome team and contributors (github.com/GoogleChrome/modern-web-guidance), Apache License 2.0.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
HOME = Path.home()
CANDIDATES = [
    SKILL.parent / "modern-web-guidance",
    SKILL / "vendor" / "modern-web-guidance",
    *(HOME / d / "skills" / "modern-web-guidance" for d in (".claude", ".agents", ".codex", ".cursor", ".gemini", ".copilot")),
]

# Words people use for a UI pattern -> the words MWG guides use.
SYNONYMS = {
    "modal": "dialog", "popup": "dialog popover", "lightbox": "dialog", "sheet": "drawer dialog",
    "dropdown": "select menu", "combobox": "select", "picker": "select", "toggle": "switch",
    "collapse": "accordion details", "expand": "accordion details", "disclosure": "details accordion",
    "faq": "accordion", "tooltip": "tooltip hint popover interest", "toast": "toast notification",
    "snackbar": "toast notification", "theme": "dark-mode color-scheme", "night": "dark-mode",
    "reveal": "scroll entry view", "parallax": "parallax scroll", "lazy": "lazy loading",
    "hero": "lcp image priority", "lcp": "lcp image priority", "font": "font fallbacks typography",
    "sidebar": "drawer navigation", "hamburger": "drawer navigation", "nav": "navbar navigation",
    "otp": "sms otp one-time-code", "login": "sign-in autofill passkey", "signup": "sign-up autofill",
    "checkout": "payment autofill", "xss": "sanitize html", "spinner": "spinner progress loading",
    "loader": "spinner progress", "stagger": "sibling-index", "fluid": "clamp fluid scaling",
    "breakpoint": "container queries responsive", "transition": "transition view-transition",
    "page": "cross-document view-transition", "route": "view-transition spa",
}


def find_mwg(explicit: str | None) -> Path | None:
    order = [Path(explicit)] if explicit else []
    if os.environ.get("MWG_DIR"):
        order.append(Path(os.environ["MWG_DIR"]))
    order += CANDIDATES
    order += sorted(HOME.glob(".claude/plugins/cache/*/*/*/skills/modern-web-guidance"), reverse=True)
    for c in order:
        if (c / "guides").is_dir() and (c / "SKILL.md").is_file():
            return c
    return None


def stem(word: str) -> str:
    for suf in ("ing", "es", "ed", "s"):
        if len(word) > 4 and word.endswith(suf):
            return word[: -len(suf)]
    return word


def tokens(text: str) -> list[str]:
    return [stem(t) for t in re.findall(r"[a-z0-9]+", text.lower()) if len(t) > 1]


def load(mwg: Path) -> list[dict]:
    guides = []
    for p in sorted((mwg / "guides").rglob("*.md")):
        text = p.read_text(encoding="utf-8")
        lines = text.splitlines()
        title = next((ln[2:].strip() for ln in lines if ln.startswith("# ")), p.stem)
        paras = [b.strip() for b in re.split(r"\n\s*\n", text) if b.strip() and not b.lstrip().startswith(("#", "```", "-", "|", "<", "*"))]
        desc = re.sub(r"\s+", " ", re.sub(r"\(via `npx[^)]*\)", "", paras[0] if paras else title))
        desc = re.sub(r"[`*]", "", desc)
        if len(desc) > 260:
            desc = desc[:257].rsplit(" ", 1)[0] + "..."
        heads = " ".join(ln.lstrip("#").strip() for ln in lines if ln.startswith("#"))
        guides.append({"id": p.stem, "category": p.parent.name, "title": title, "description": desc,
                       "path": p, "fields": {"id": tokens(p.stem.replace("-", " ")), "title": tokens(title),
                                             "head": tokens(heads), "desc": tokens(desc), "body": tokens(text)}})
    return guides


def search(guides: list[dict], query: str, limit: int) -> list[dict]:
    words = tokens(query)
    expanded = set(words)
    for w in re.findall(r"[a-z0-9]+", query.lower()):
        expanded |= set(tokens(SYNONYMS.get(w, "")))
    weights = {"id": 6.0, "title": 4.0, "head": 1.5, "desc": 2.5}
    scored = []
    for g in guides:
        f = g["fields"]
        score = 0.0
        for w in expanded:
            primary = 1.0 if w in words else 0.6
            for field, wt in weights.items():
                if w in f[field]:
                    score += wt * primary
            score += min(f["body"].count(w), 8) * 0.15 * primary
        hits = sum(1 for w in words if any(w in f[k] for k in ("id", "title", "head", "desc")))
        score *= 1 + hits / max(len(words), 1)
        if score > 0:
            scored.append((score, g))
    scored.sort(key=lambda x: -x[0])
    best = scored[0][0] if scored else 0
    return [{"id": g["id"], "description": g["description"]} for s, g in scored[:limit] if s >= best * 0.25]


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        pass
    ap = argparse.ArgumentParser(description="Offline Modern Web Guidance lookup (fallback for the npx CLI).")
    ap.add_argument("command", choices=["search", "retrieve", "list", "info"])
    ap.add_argument("arg", nargs="?", default="", help="search query, or comma-separated guide ids for retrieve")
    ap.add_argument("--dir", help="path to a modern-web-guidance skill folder")
    ap.add_argument("--limit", type=int, default=10)
    args = ap.parse_args()

    mwg = find_mwg(args.dir)
    if not mwg:
        print("error: no Modern Web Guidance copy found. Use the CLI (npx -y modern-web-guidance@latest ...), "
              "set MWG_DIR, or install DENT with its modern-web-guidance folder.", file=sys.stderr)
        return 2
    guides = load(mwg)
    by_id = {g["id"]: g for g in guides}

    if args.command == "info":
        upstream = mwg / "UPSTREAM.json"
        meta = json.loads(upstream.read_text(encoding="utf-8")) if upstream.is_file() else {"note": "no UPSTREAM.json (not a DENT-vendored copy)"}
        print(json.dumps({"path": str(mwg), "guides": len(guides), **meta}, indent=2))
        return 0
    if args.command == "list":
        print("[" + ",\n".join(json.dumps({"id": g["id"], "description": g["description"]}) for g in guides) + "]")
        return 0
    if args.command == "search":
        if not args.arg.strip():
            ap.error("search needs a query")
        found = search(guides, args.arg, args.limit)
        print("[" + ",\n".join(json.dumps(r) for r in found) + "]")
        return 0 if found else 1
    ids = [i.strip().strip('"') for i in args.arg.split(",") if i.strip()]
    if not ids:
        ap.error("retrieve needs one or more guide ids")
    missing = [i for i in ids if i not in by_id]
    for i in ids:
        if i in by_id:
            print(f"--- Guide for {i} ---")
            print(by_id[i]["path"].read_text(encoding="utf-8").rstrip() + "\n")
    if missing:
        print(f"error: unknown guide id(s): {', '.join(missing)}. Run `search` or `list`.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

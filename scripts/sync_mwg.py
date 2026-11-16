#!/usr/bin/env python3
"""Vendor Google's Modern Web Guidance (MWG) skill into this repository.

MWG (https://github.com/GoogleChrome/modern-web-guidance, Apache-2.0) is DENT's primary
authority for how web code is built. This script copies its skill folder verbatim into
`skills/modern-web-guidance/`, adds the upstream LICENSE, and records provenance in
`skills/modern-web-guidance/UPSTREAM.json` (commit, commit date, --skill-version, guide count).

Never hand-edit the vendored files: re-run this script instead.

Usage:
  python scripts/sync_mwg.py                      # shallow-clone the upstream default branch
  python scripts/sync_mwg.py --ref <branch|tag>   # a specific upstream branch or tag
  python scripts/sync_mwg.py --from <checkout>    # use an existing local checkout (no network)

Only files are copied; nothing from the upstream checkout is executed.
Afterwards: python scripts/validate.py, then add a CHANGELOG.md entry.
Copyright 2026 Jeel Nada (solarquack). Licensed under the Apache License 2.0.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / "skills" / "modern-web-guidance"
REPO = "https://github.com/GoogleChrome/modern-web-guidance"


def git(*args: str, cwd: Path | None = None) -> str:
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


def sync(checkout: Path) -> dict:
    src = checkout / "skills" / "modern-web-guidance"
    if not (src / "SKILL.md").is_file() or not (src / "guides").is_dir():
        raise SystemExit(f"error: {src} does not look like the MWG skill (SKILL.md + guides/ expected)")
    skill_text = (src / "SKILL.md").read_text(encoding="utf-8")
    m = re.search(r"--skill-version\s+(\S+)", skill_text)
    if not m:
        raise SystemExit("error: upstream SKILL.md has no --skill-version; the upstream format changed, review it by hand")
    try:
        commit = git("rev-parse", "HEAD", cwd=checkout)
        committed = git("log", "-1", "--format=%cI", cwd=checkout)
    except (subprocess.CalledProcessError, FileNotFoundError):
        commit, committed = "unknown", "unknown"

    if DEST.exists():
        shutil.rmtree(DEST)
    shutil.copytree(src, DEST, ignore=shutil.ignore_patterns(".*", "node_modules", "__pycache__"))
    shutil.copy2(checkout / "LICENSE", DEST / "LICENSE")
    guides = sorted(p.stem for p in (DEST / "guides").rglob("*.md"))
    info = {
        "name": "modern-web-guidance",
        "repository": REPO,
        "commit": commit,
        "committed": committed,
        "skill_version": m.group(1),
        "license": "Apache-2.0",
        "guides": len(guides),
        "synced": dt.date.today().isoformat(),
        "note": "Vendored verbatim by scripts/sync_mwg.py. Do not edit files in this folder; re-run the script.",
    }
    (DEST / "UPSTREAM.json").write_text(json.dumps(info, indent=2) + "\n", encoding="utf-8", newline="\n")
    return info


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--from", dest="src", help="existing local checkout of the upstream repository")
    ap.add_argument("--ref", help="upstream branch or tag to clone (default: default branch)")
    args = ap.parse_args()
    if args.src:
        info = sync(Path(args.src).resolve())
    else:
        with tempfile.TemporaryDirectory() as tmp:
            checkout = Path(tmp) / "mwg"
            cmd = ["clone", "--depth", "1", *(["--branch", args.ref] if args.ref else []), REPO, str(checkout)]
            try:
                git(*cmd)
            except (subprocess.CalledProcessError, FileNotFoundError) as e:
                raise SystemExit(f"error: could not clone {REPO} ({e}); use --from <checkout>")
            info = sync(checkout)
    print(f"Vendored MWG {info['skill_version']} (commit {info['commit'][:12]}, {info['guides']} guides) "
          f"into {DEST.relative_to(ROOT)}")
    print("Next: python scripts/validate.py, then add a CHANGELOG.md entry.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

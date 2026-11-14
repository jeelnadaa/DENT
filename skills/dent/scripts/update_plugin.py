#!/usr/bin/env python3
"""DENT updater for Claude Code: refresh the local DENT marketplace so the normal plugin update works.

Why: Claude Code updates a plugin when the marketplace lists a newer version, but it keeps a local git copy
of each third-party marketplace and doesn't always refresh it (auto-update is off by default for third-party
marketplaces). Removing and re-adding the plugin then reinstalls the same old version.

What this does (safe, no Claude settings are edited):
  1. Finds the DENT marketplace in ~/.claude/plugins/known_marketplaces.json
  2. Fetches the latest version from GitHub into that local copy (git fetch + reset to origin's default branch)
  3. Reports installed version vs available version and tells you the one click/command left

Usage:
  python update_plugin.py            # refresh + report
  python update_plugin.py --check    # report only, change nothing

Copyright 2026 Jeel Nada (solarquack). Licensed under the Apache License 2.0.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

REPO_HINT = "jeelnadaa/dent"


def claude_dir() -> Path:
    env = os.environ.get("CLAUDE_CONFIG_DIR")
    return Path(env) if env else Path.home() / ".claude"


def read_json(p: Path):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return None


def version_of(folder: Path) -> str | None:
    data = read_json(folder / ".claude-plugin" / "plugin.json")
    return data.get("version") if data else None


def git(cwd: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="report only; don't fetch")
    args = ap.parse_args()

    plugins = claude_dir() / "plugins"
    known = read_json(plugins / "known_marketplaces.json") or {}
    name, entry = next(((k, v) for k, v in known.items()
                        if REPO_HINT in json.dumps(v.get("source", {})).lower()), (None, None))
    if not entry:
        print("DENT isn't installed as a Claude Code plugin marketplace on this machine.")
        print("Install: /plugin marketplace add jeelnadaa/DENT  then  /plugin install dent@dent")
        return 1
    mp = Path(entry.get("installLocation", plugins / "marketplaces" / name))

    installed = None
    inst = read_json(plugins / "installed_plugins.json") or {}
    for key, rows in (inst.get("plugins") or {}).items():
        if key.startswith("dent@") and rows:
            installed = rows[0].get("version")

    before = version_of(mp)
    if not args.check:
        if not (mp / ".git").is_dir():
            print(f"Marketplace copy at {mp} isn't a git checkout; use Claude's 'Update marketplace' instead.")
            return 1
        r = git(mp, "fetch", "--quiet", "origin")
        if r.returncode != 0:
            print("Couldn't reach GitHub:", (r.stderr or r.stdout).strip()[:300])
            return 1
        head = git(mp, "symbolic-ref", "--short", "refs/remotes/origin/HEAD").stdout.strip() or "origin/main"
        r = git(mp, "reset", "--quiet", "--hard", head)
        if r.returncode != 0:
            print("Couldn't update the marketplace copy:", (r.stderr or r.stdout).strip()[:300])
            return 1
    after = version_of(mp)
    sha = git(mp, "rev-parse", "--short", "HEAD").stdout.strip()

    print(f"DENT marketplace '{name}': {before} -> {after} (commit {sha})" if before != after
          else f"DENT marketplace '{name}': {after} (commit {sha}, already current)" if not args.check
          else f"DENT marketplace '{name}': {after} (commit {sha}, not refreshed: --check)")
    print(f"Installed plugin version: {installed or 'not installed'}")
    if installed and after and installed != after:
        print("\nOne step left, pick whichever your Claude app allows:")
        print("  • App: Settings → Plugins (Customize) → DENT → Update   (or remove + add it again: it now gets the new version)")
        print("  • Claude Code chat:  /plugin update dent@dent   then   /reload-plugins")
        print("  • Terminal:          claude plugin update dent@dent")
        print("Then start a new chat so the new skill files load.")
    elif installed == after:
        print("You're on the latest version.")
    print("\nTip: turn on auto-update for the DENT marketplace (Plugins → Marketplaces → dent → Enable auto-update) "
          "so future versions arrive without this step. If updates still lag, run /dent:update again.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

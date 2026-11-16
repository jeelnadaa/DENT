#!/usr/bin/env python3
"""Build upload archives for Claude.ai / Claude Desktop or the Skills API.

dist/dent.zip                  one top-level folder `dent/` with SKILL.md, references/… and, under
                               `vendor/modern-web-guidance/`, Google's Modern Web Guidance skill (DENT's
                               authority for web code; its offline fallback when the CLI can't run).
dist/modern-web-guidance.zip   the same Modern Web Guidance skill on its own, for platforms where you
                               upload each skill separately (it then triggers on any web task by itself).

Copyright 2026 Jeel Nada (solarquack). Licensed under the Apache License 2.0.
"""
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "skills" / "dent"
MWG = ROOT / "skills" / "modern-web-guidance"
DIST = ROOT / "dist"


def add_tree(zf: zipfile.ZipFile, src: Path, prefix: Path) -> int:
    count = 0
    for path in sorted(src.rglob("*")):
        if path.is_file() and not path.name.startswith(".") and "__pycache__" not in path.parts:
            zf.write(path, prefix / path.relative_to(src))
            count += 1
    return count


def main() -> None:
    for skill in (SRC, MWG):
        if not (skill / "SKILL.md").is_file():
            raise SystemExit(f"error: {skill / 'SKILL.md'} not found")
    DIST.mkdir(exist_ok=True)

    out = DIST / "dent.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        count = add_tree(zf, SRC, Path("dent"))
        vendored = add_tree(zf, MWG, Path("dent") / "vendor" / "modern-web-guidance")
        # ship license + notice inside the skill bundle too
        for extra in ("LICENSE", "NOTICE"):
            zf.write(ROOT / extra, Path("dent") / extra)
    print(f"Wrote {out.relative_to(ROOT)} ({count} skill files + {vendored} Modern Web Guidance files, "
          f"{out.stat().st_size // 1024} KB)")

    out = DIST / "modern-web-guidance.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        count = add_tree(zf, MWG, Path("modern-web-guidance"))
    print(f"Wrote {out.relative_to(ROOT)} ({count} files, {out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Build dist/dent.zip for upload to Claude.ai / Claude Desktop or the Skills API.

The archive contains a single top-level folder `dent/` with SKILL.md and references/.
Copyright 2026 Jeel Nada (solarquack). Licensed under the Apache License 2.0.
"""
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "skills" / "dent"
OUT = ROOT / "dist" / "dent.zip"


def main() -> None:
    if not (SRC / "SKILL.md").is_file():
        raise SystemExit(f"error: {SRC / 'SKILL.md'} not found")
    OUT.parent.mkdir(exist_ok=True)
    count = 0
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(SRC.rglob("*")):
            if path.is_file() and not path.name.startswith("."):
                zf.write(path, Path("dent") / path.relative_to(SRC))
                count += 1
        # ship license + notice inside the skill bundle too
        for extra in ("LICENSE", "NOTICE"):
            zf.write(ROOT / extra, Path("dent") / extra)
    print(f"Wrote {OUT.relative_to(ROOT)} ({count} skill files, {OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()

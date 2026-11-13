#!/usr/bin/env python3
"""Validate the DENT skill: frontmatter, cross-file references and the styles index.

Run: python scripts/validate.py   (exit code 1 on errors)
Copyright 2026 Jeel Nada (solarquack). Licensed under the Apache License 2.0.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "dent"
REFS = SKILL / "references"
STYLES = REFS / "styles"
errors: list[str] = []
warnings: list[str] = []


def frontmatter(text: str) -> dict[str, str]:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append("SKILL.md: missing YAML frontmatter")
        return {}
    data = {}
    for line in m.group(1).splitlines():
        if re.match(r"^[a-z_]+:", line):
            key, _, value = line.partition(":")
            data[key.strip()] = value.strip()
    return data


def check_frontmatter() -> None:
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    fm = frontmatter(text)
    name = fm.get("name", "")
    if name != SKILL.name:
        errors.append(f"SKILL.md: name '{name}' must match folder '{SKILL.name}'")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name or "x") or len(name) > 64:
        errors.append("SKILL.md: name must be lowercase letters, digits and hyphens, max 64 chars")
    desc = fm.get("description", "")
    if not desc:
        errors.append("SKILL.md: description is required")
    elif len(desc) > 1024:
        errors.append(f"SKILL.md: description is {len(desc)} chars (max 1024)")
    lines = text.count("\n")
    if lines > 1000:
        warnings.append(f"SKILL.md is {lines} lines; consider moving detail into references/")


def check_links() -> None:
    files = [SKILL / "SKILL.md", *REFS.glob("*.md"), *STYLES.glob("*.md")]
    pattern = re.compile(r"`((?:references/|\.\./)?[a-z0-9_./-]+\.md)`")
    for f in files:
        for ref in pattern.findall(f.read_text(encoding="utf-8")):
            if ref in ("SKILL.md", "DESIGN.md", "README.md", "CONVENTIONS.md", "AGENTS.md", "GEMINI.md") \
                    or "<" in ref:
                continue
            candidates = [
                (f.parent / ref),
                (SKILL / ref),
                (REFS / ref),
                (STYLES / ref),
            ]
            if not any(c.resolve().is_file() for c in candidates):
                errors.append(f"{f.relative_to(ROOT)}: broken reference `{ref}`")


def check_styles() -> None:
    index = (STYLES / "_styles-index.md").read_text(encoding="utf-8")
    listed = set(re.findall(r"\| `([a-z0-9-]+\.md)` \|", index))
    actual = {p.name for p in STYLES.glob("*.md") if not p.name.startswith("_")}
    for missing in sorted(actual - listed):
        errors.append(f"styles/{missing} is not listed in _styles-index.md")
    for ghost in sorted(listed - actual):
        errors.append(f"_styles-index.md lists {ghost}, which does not exist")
    required = ["## Overrides", "## Signature moves", "## Accessibility watch-outs", "## Starter tokens"]
    for p in sorted(STYLES.glob("*.md")):
        if p.name.startswith("_"):
            continue
        body = p.read_text(encoding="utf-8")
        for section in required:
            if section not in body:
                errors.append(f"styles/{p.name}: missing section '{section}'")
    skill_text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    m = re.search(r"(\d+) aesthetic styles", skill_text) or re.search(r"\((\d+) styles\)", skill_text)
    if m and int(m.group(1)) != len(actual):
        errors.append(f"SKILL.md says {m.group(1)} styles but {len(actual)} style files exist")


def main() -> int:
    check_frontmatter()
    check_links()
    check_styles()
    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    if errors:
        print(f"\n{len(errors)} error(s)")
        return 1
    styles = len([p for p in STYLES.glob('*.md') if not p.name.startswith('_')])
    refs = len(list(REFS.glob('*.md')))
    print(f"OK: SKILL.md + {refs} reference files + {styles} styles")
    return 0


if __name__ == "__main__":
    sys.exit(main())

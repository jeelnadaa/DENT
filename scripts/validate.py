#!/usr/bin/env python3
"""Validate the DENT skill repository.

Checks:
  1. SKILL.md frontmatter (name = folder, description <= 1024 chars) and size budget
  2. Every backticked .md/.py path in the skill resolves to a real file
  3. Styles index <-> style files, required sections in every style
  4. Commands: skills/dent/commands/X.md <-> commands/X.md (plugin wrapper) <-> SKILL.md §4 table
  5. Catalogue rows (entries starting with a link) carry a status marker (✓ date or K)
  6. Templates and scripts referenced by SKILL.md exist; plugin JSON parses; versions agree

Run: python scripts/validate.py   (exit 1 on errors)
Copyright 2026 Jeel Nada (solarquack). Licensed under the Apache License 2.0.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "dent"
REFS = SKILL / "references"
STYLES = REFS / "styles"
errors: list[str] = []
warnings: list[str] = []

# Bare file names that legitimately refer to user-project files, not skill files.
PROJECT_FILES = {"DESIGN.md", "PLAN.md", "README.md", "AGENTS.md", "GEMINI.md", "CONVENTIONS.md", "SKILL.md",
                 "SCORECARD.md", "AUDIT.md", "REVIEW.md", "MOTION.md", "SOUND.md", "VIDEO.md", "CHANGELOG.md",
                 "RESULT.md", "index.md"}


def rel(p: Path) -> str:
    return str(p.relative_to(ROOT)).replace("\\", "/")


def frontmatter(text: str) -> dict[str, str]:
    m = re.match(r"^---\n(.*?)\n---\n", text.replace("\r\n", "\n"), re.S)
    if not m:
        errors.append("SKILL.md: missing YAML frontmatter")
        return {}
    data = {}
    for line in m.group(1).splitlines():
        if re.match(r"^[a-z_]+:", line):
            key, _, value = line.partition(":")
            data[key.strip()] = value.strip()
        mv = re.match(r'^\s+version:\s*"?([\d.]+)"?', line)
        if mv:
            data["version"] = mv.group(1)
    return data


def check_skill_md() -> dict[str, str]:
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
    if lines > 450:
        warnings.append(f"SKILL.md is {lines} lines (budget 450): move detail into references/")
    return fm


def resolve(ref: str, base: Path) -> bool:
    candidates = [base / ref, SKILL / ref, REFS / ref, STYLES / ref, ROOT / ref, SKILL / "scripts" / ref]
    return any(c.resolve().is_file() for c in candidates)


def check_links() -> int:
    pattern = re.compile(r"`((?:\.\./)*[A-Za-z0-9_][A-Za-z0-9_./-]*\.(?:md|py))(?:[^`\n]*)`")
    files = [p for p in SKILL.rglob("*.md")]
    count = 0
    for f in files:
        for ref in pattern.findall(f.read_text(encoding="utf-8")):
            if "<" in ref or ref in PROJECT_FILES or ref.startswith(("http", "docs/")):
                continue
            if "/" not in ref and ref.count(".") > 1:
                continue  # code identifiers like DS.Spacing.md
            count += 1
            if not resolve(ref, f.parent):
                errors.append(f"{rel(f)}: broken reference `{ref}`")
    return count


def check_styles() -> int:
    index = (STYLES / "_styles-index.md").read_text(encoding="utf-8")
    listed = set(re.findall(r"\| `([a-z0-9-]+\.md)` \|", index))
    actual = {p.name for p in STYLES.glob("*.md") if not p.name.startswith("_")}
    for missing in sorted(actual - listed):
        errors.append(f"styles/{missing} is not listed in _styles-index.md")
    for ghost in sorted(listed - actual):
        errors.append(f"_styles-index.md lists {ghost}, which does not exist")
    for p in sorted(STYLES.glob("*.md")):
        if p.name.startswith("_"):
            continue
        body = p.read_text(encoding="utf-8")
        for section in ("## Overrides", "## Signature moves", "## Accessibility watch-outs", "## Starter tokens"):
            if section not in body:
                errors.append(f"styles/{p.name}: missing section '{section}'")
    skill_text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    for m in re.finditer(r"(\d+) (?:aesthetic )?styles", skill_text):
        if int(m.group(1)) != len(actual):
            errors.append(f"SKILL.md says {m.group(1)} styles but {len(actual)} style files exist")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    m = re.search(r"aesthetic%20styles-(\d+)", readme)
    if m and int(m.group(1)) != len(actual):
        errors.append(f"README badge says {m.group(1)} styles but {len(actual)} exist")
    return len(actual)


def check_commands() -> int:
    skill_cmds = {p.stem for p in (SKILL / "commands").glob("*.md")}
    plugin_cmds = {p.stem for p in (ROOT / "commands").glob("*.md")}
    table = set(re.findall(r"`commands/([a-z0-9-]+)\.md`", (SKILL / "SKILL.md").read_text(encoding="utf-8")))
    for name in sorted(skill_cmds - plugin_cmds):
        errors.append(f"command '{name}' has no plugin wrapper commands/{name}.md (run scripts/build_commands.py)")
    for name in sorted(plugin_cmds - skill_cmds):
        errors.append(f"plugin wrapper commands/{name}.md has no skills/dent/commands/{name}.md")
    for name in sorted(skill_cmds - table):
        errors.append(f"command '{name}' is missing from the SKILL.md §4 table")
    for name in sorted(table - skill_cmds):
        errors.append(f"SKILL.md §4 lists commands/{name}.md, which does not exist")
    orch = (REFS / "workflow" / "orchestration.md").read_text(encoding="utf-8")
    for name in sorted(skill_cmds - {"dent"}):
        if f"`{name}`" not in orch:
            warnings.append(f"orchestration.md never routes to `{name}`")
    for p in (ROOT / "commands").glob("*.md"):
        t = p.read_text(encoding="utf-8")
        if not t.startswith("---\ndescription:"):
            errors.append(f"{rel(p)}: wrapper must start with frontmatter 'description:'")
    return len(skill_cmds)


def check_catalogues() -> int:
    files = [*(REFS / "catalog").glob("*.md"), REFS / "motion" / "motion-tech-catalog.md", REFS / "audio" / "audio-tech-catalog.md",
             REFS / "video" / "video-tools-and-pipeline.md"]
    rows = 0
    for f in files:
        if f.name in ("README.md", "component-selection.md"):
            continue
        for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if not line.startswith("| ["):
                continue
            rows += 1
            if "✓" not in line and not re.search(r"\|\s*K\s*\|\s*$", line):
                errors.append(f"{rel(f)}:{i}: catalogue row without status (✓ <date> or K)")
            if not re.search(r"\]\(https?://", line):
                errors.append(f"{rel(f)}:{i}: catalogue row without an official URL")
    return rows


def check_repo(fm: dict[str, str]) -> None:
    version = fm.get("version")
    for name in ("plugin.json", "marketplace.json"):
        p = ROOT / ".claude-plugin" / name
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except Exception as e:  # noqa: BLE001
            errors.append(f".claude-plugin/{name}: invalid JSON ({e})")
            continue
        found = {data.get("version"), (data.get("metadata") or {}).get("version")}
        found |= {pl.get("version") for pl in data.get("plugins", [])}
        found.discard(None)
        if version and found and found != {version}:
            errors.append(f".claude-plugin/{name}: version {sorted(found)} != SKILL.md {version}")
    for t in ("PLAN", "AUDIT", "REVIEW", "SCORECARD", "MOTION", "SOUND", "VIDEO"):
        if not (SKILL / "templates" / f"{t}.md").is_file():
            errors.append(f"missing template templates/{t}.md")
    for s in ("verify_page.py", "contrast.py"):
        if not (SKILL / "scripts" / s).is_file():
            errors.append(f"missing script skills/dent/scripts/{s}")


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        pass
    fm = check_skill_md()
    links = check_links()
    styles = check_styles()
    cmds = check_commands()
    rows = check_catalogues()
    check_repo(fm)
    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    if errors:
        print(f"\n{len(errors)} error(s)")
        return 1
    refs = len(list(REFS.rglob("*.md"))) - len(list(STYLES.glob("*.md")))
    print(f"OK: SKILL.md v{fm.get('version')} + {refs} reference files + {styles} styles + {cmds} commands + "
          f"{rows} catalogue entries; {links} internal references resolved")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Validate the DENT skill repository.

Checks:
  1. SKILL.md frontmatter (name = folder, description <= 1024 chars) and size budget
  2. Every backticked .md/.py path in the skill resolves to a real file
  3. Styles index <-> style files, required sections in every style
  4. Commands: skills/dent/commands/X.md <-> commands/X.md (plugin wrapper) <-> SKILL.md §4 table
  5. Catalogue rows (entries starting with a link) carry a status marker (✓ date or K)
  6. Templates and scripts referenced by SKILL.md exist; plugin JSON parses; versions agree
  7. Vendored Modern Web Guidance (skills/modern-web-guidance): intact, provenance recorded, and every
     `mwg:<id>` mentioned anywhere in DENT names a real guide

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
MWG = ROOT / "skills" / "modern-web-guidance"
errors: list[str] = []
warnings: list[str] = []

# Bare file names that legitimately refer to user-project files, not skill files.
PROJECT_FILES = {"DESIGN.md", "PLAN.md", "README.md", "AGENTS.md", "GEMINI.md", "CONVENTIONS.md", "SKILL.md",
                 "SCORECARD.md", "AUDIT.md", "REVIEW.md", "MOTION.md", "SOUND.md", "VIDEO.md", "CHANGELOG.md",
                 "RESULT.md", "index.md", "CLAUDE.md"}


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
    m = re.search(r"badge/commands-(\d+)-", (ROOT / "README.md").read_text(encoding="utf-8"))
    if m and int(m.group(1)) != len(skill_cmds):
        errors.append(f"README badge says {m.group(1)} commands but {len(skill_cmds)} exist")
    for p in (ROOT / "commands").glob("*.md"):
        t = p.read_text(encoding="utf-8")
        if not t.startswith("---\ndescription:"):
            errors.append(f"{rel(p)}: wrapper must start with frontmatter 'description:'")
    return len(skill_cmds)


def check_catalogues() -> int:
    files = [*(REFS / "catalog").glob("*.md"), REFS / "motion" / "motion-tech-catalog.md", REFS / "audio" / "audio-tech-catalog.md",
             REFS / "video" / "video-tools-and-pipeline.md", REFS / "media-sourcing.md", REFS / "audio" / "voice-and-narration.md"]
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
    for s in ("verify_page.py", "contrast.py", "palette.py", "fonts.py", "tts.py", "doctor.py", "video_qa.py", "data/google-fonts.json"):
        if not (SKILL / "scripts" / s).is_file():
            errors.append(f"missing script skills/dent/scripts/{s}")


def check_capabilities() -> int:
    """Guard against capabilities that are promised but never triggered (the 'go all out skips motion' class of bug)."""
    n = 0
    cmds = {p.stem: p.read_text(encoding="utf-8") for p in (SKILL / "commands").glob("*.md")}
    allout = (REFS / "workflow" / "all-out.md").read_text(encoding="utf-8")
    sec0 = allout.split("## 0.", 1)[1].split(chr(10) + "## 1.", 1)[0] if "## 0." in allout else ""
    if not sec0:
        errors.append("all-out.md has no §0 capability list")
    for name in re.findall(r"\|\s*`([a-z0-9-]+)`(?:\s*/\s*`([a-z0-9-]+)`)?(?:\s*\+[^|]*)?\s*\|", sec0):
        for c in filter(None, name):
            n += 1
            if c not in cmds:
                errors.append(f"all-out.md §0 lists `{c}`, which is not a command")
    for must in ("motion", "surfaces", "type", "copy", "assets", "directions", "review", "sound", "voice", "video", "3d", "brand"):
        if f"`{must}`" not in sec0:
            errors.append(f"all-out.md §0 capability list is missing `{must}`")
    # commands that build visual UI must actually run motion and surfaces, not just mention them
    for c in ("create", "redesign"):
        t = cmds.get(c, "")
        for need in ("commands/motion.md", "commands/surfaces.md"):
            if need not in t:
                errors.append(f"commands/{c}.md never runs {need} (motion/surfaces would be skipped)")
    orch = (REFS / "workflow" / "orchestration.md").read_text(encoding="utf-8")
    for line in orch.splitlines():
        if "go all out" in line.lower() and "landing page" in line.lower() and "motion (" not in line:
            errors.append("orchestration.md: the All-out landing-page example must include the motion command")
    if "all-out.md` §0" not in orch:
        errors.append("orchestration.md must expand pipelines with the All-out capability list (all-out.md §0)")
    # every media command asks where media comes from
    for c in ("voice", "video", "launch-video", "sound", "assets", "3d", "motion-graphics", "brand"):
        if "media-sourcing.md" not in cmds.get(c, ""):
            errors.append(f"commands/{c}.md doesn't ask where media comes from (references/media-sourcing.md)")
    # video: the creative process, the kit and the measured QA must be wired into every video command
    for c in ("video", "launch-video"):
        t = cmds.get(c, "")
        for need in ("video-creative-direction.md", "video_qa.py", "video-kit"):
            if need not in t:
                errors.append(f"commands/{c}.md doesn't use {need}")
    if "PLACEHOLDERS ONLY" not in (SKILL / "templates" / "video-kit" / "composition.html").read_text(encoding="utf-8"):
        errors.append("templates/video-kit/composition.html must mark its scenes as placeholders (originality guard)")
    # effort tables must not undercut the motion floor (motion-menu.md §2 is the motion authority)
    lp = (REFS / "recipes" / "landing-page.md").read_text(encoding="utf-8")
    ess = next((ln for ln in lp.splitlines() if ln.startswith("| Essential |")), "")
    if ess and "motion-menu.md" not in ess:
        errors.append("recipes/landing-page.md: the Essential row must point to the motion floor (motion/motion-menu.md §2)")
    wq = (REFS / "workflow-questions-and-effort.md").read_text(encoding="utf-8")
    if "| Motion" in wq and "motion-menu.md" not in next((ln for ln in wq.splitlines() if ln.startswith("| Motion")), ""):
        errors.append("workflow-questions-and-effort.md: the Motion row of the effort table must defer to motion/motion-menu.md §2")
    # starter fonts in style files: warn when a style's first face is on the overused registry
    try:
        sys.path.insert(0, str(SKILL / "scripts"))
        from fonts import OVERUSED  # type: ignore
    except Exception:  # noqa: BLE001
        OVERUSED = {}
    try:
        import palette as _P  # type: ignore
        for f in STYLES.glob("*.md"):
            for h in set(re.findall(r"#[0-9A-Fa-f]{6}", f.read_text(encoding="utf-8"))):
                for ref, why in _P.CLICHES:
                    if _P.delta(h, ref) < 0.02:
                        warnings.append(f"{rel(f)}: {h} is the template colour {ref} ({why}); use a concept colour or log why")
    except Exception:  # noqa: BLE001
        pass
    # styles whose identity IS the default face (typography.md §0.1 "a style depends on it")
    allowed = {"material.md": {"Roboto"}, "brutalism.md": {"Arial", "Times New Roman", "Courier New"},
               "anti-design.md": {"Times New Roman"}, "retro-os.md": {"Tahoma", "Verdana", "Segoe UI"}}
    for f in STYLES.glob("*.md"):
        for fam in re.findall(r"--font-[a-z0-9-]+:\s*\"([^\"]+)\"", f.read_text(encoding="utf-8")):
            if fam in OVERUSED and fam not in allowed.get(f.name, set()):
                warnings.append(f"{rel(f)}: starter font '{fam}' is on the overused registry (typography.md §0.1)")
    return n


def check_mwg() -> int:
    skill = MWG / "SKILL.md"
    if not skill.is_file():
        errors.append("skills/modern-web-guidance/SKILL.md missing (run scripts/sync_mwg.py)")
        return 0
    text = skill.read_text(encoding="utf-8")
    if not re.search(r"^name:\s*modern-web-guidance\s*$", text, re.M):
        errors.append("skills/modern-web-guidance/SKILL.md: name must be 'modern-web-guidance'")
    for f in ("LICENSE", "UPSTREAM.json"):
        if not (MWG / f).is_file():
            errors.append(f"skills/modern-web-guidance/{f} missing (run scripts/sync_mwg.py)")
    try:
        up = json.loads((MWG / "UPSTREAM.json").read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        up = {}
    sv = up.get("skill_version", "")
    if not sv or f"--skill-version {sv}" not in text:
        errors.append("skills/modern-web-guidance/UPSTREAM.json skill_version doesn't match SKILL.md (re-run scripts/sync_mwg.py)")
    ids: dict[str, Path] = {}
    for g in (MWG / "guides").rglob("*.md"):
        if g.stem in ids:
            errors.append(f"MWG guide id '{g.stem}' is duplicated ({rel(ids[g.stem])}, {rel(g)})")
        ids[g.stem] = g
    if up.get("guides") not in (None, len(ids)):
        errors.append(f"UPSTREAM.json says {up.get('guides')} guides but {len(ids)} exist (vendored copy edited by hand?)")
    if len(ids) < 100:
        errors.append(f"only {len(ids)} MWG guides vendored; expected the full corpus")
    adapter = REFS / "modern-web-guidance.md"
    if not adapter.is_file():
        errors.append("references/modern-web-guidance.md (DENT's MWG adapter) is missing")
    used = 0
    for f in [*SKILL.rglob("*.md"), ROOT / "README.md", *(ROOT / "docs").glob("*.md")]:
        for gid in re.findall(r"mwg:([a-z0-9][a-z0-9-]*)", f.read_text(encoding="utf-8")):
            used += 1
            if gid not in ids:
                errors.append(f"{rel(f)}: `mwg:{gid}` is not an MWG guide id")
    return used


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
    mwg_refs = check_mwg()
    check_capabilities()
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
          f"{rows} catalogue entries; {links} internal references resolved; {mwg_refs} MWG guide references resolved")
    return 0


if __name__ == "__main__":
    sys.exit(main())

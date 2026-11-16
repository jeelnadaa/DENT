#!/usr/bin/env sh
# DENT installer — copies skills/dent (and the bundled Modern Web Guidance skill) into an agent's skills folder.
# Usage: ./scripts/install.sh <agent> [--project] [--path DIR]
#        ./scripts/install.sh --list
# Copyright 2026 Jeel Nada (solarquack). Licensed under the Apache License 2.0.
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
SRC="$SCRIPT_DIR/../skills/dent"
MWG="$SCRIPT_DIR/../skills/modern-web-guidance"
AGENT=""
PROJECT=0
CUSTOM=""

usage() {
  cat <<'EOF'
DENT installer

  ./scripts/install.sh <agent> [--project]   install for an agent
  ./scripts/install.sh --path <dir>          install into <dir>/dent
  ./scripts/install.sh rules --path <dir>    copy to <dir> and print a rules snippet
  ./scripts/install.sh --list                show targets

Agents (personal path  |  --project path):
  claude    ~/.claude/skills    | .claude/skills
  codex     ~/.codex/skills     | .agents/skills
  copilot   ~/.copilot/skills   | .github/skills
  cursor    ~/.cursor/skills    | .cursor/skills
  gemini    ~/.gemini/skills    | .gemini/skills
  agents    (project only)      | .agents/skills
EOF
}

while [ $# -gt 0 ]; do
  case "$1" in
    --list|-h|--help) usage; exit 0 ;;
    --project) PROJECT=1 ;;
    --path) shift; CUSTOM="${1:-}" ;;
    *) AGENT="$1" ;;
  esac
  shift
done

[ -f "$SRC/SKILL.md" ] || { echo "error: cannot find $SRC/SKILL.md (run from a DENT clone)" >&2; exit 1; }

if [ "$AGENT" = "rules" ]; then
  DEST="${CUSTOM:-.dent}"
  rm -rf "$DEST"; mkdir -p "$(dirname "$DEST")"; cp -R "$SRC" "$DEST"
  if [ -f "$MWG/SKILL.md" ]; then mkdir -p "$DEST/vendor"; cp -R "$MWG" "$DEST/vendor/modern-web-guidance"; fi
  echo "DENT copied to $DEST (Modern Web Guidance in $DEST/vendor/modern-web-guidance)"
  echo
  echo "Add this to your agent's rules file (AGENTS.md, .windsurf/rules/dent.md, .clinerules/dent.md, CONVENTIONS.md…):"
  echo
  echo "## Design work (DENT)"
  echo "For any UI, UX, visual design, design-system or front-end styling task, first read \`$DEST/SKILL.md\`"
  echo "and follow its workflow. Open files in \`$DEST/references/\` only when SKILL.md points to them."
  echo "For any HTML, CSS or client-side JS, follow Google's Modern Web Guidance first:"
  echo "\`$DEST/vendor/modern-web-guidance/SKILL.md\` (DENT's summary: \`$DEST/references/modern-web-guidance.md\`)."
  exit 0
fi

if [ -n "$CUSTOM" ]; then
  BASE="$CUSTOM"
else
  case "$AGENT:$PROJECT" in
    claude:0)  BASE="$HOME/.claude/skills" ;;   claude:1)  BASE=".claude/skills" ;;
    codex:0)   BASE="$HOME/.codex/skills" ;;    codex:1)   BASE=".agents/skills" ;;
    copilot:0) BASE="$HOME/.copilot/skills" ;;  copilot:1) BASE=".github/skills" ;;
    cursor:0)  BASE="$HOME/.cursor/skills" ;;   cursor:1)  BASE=".cursor/skills" ;;
    gemini:0)  BASE="$HOME/.gemini/skills" ;;   gemini:1)  BASE=".gemini/skills" ;;
    agents:*)  BASE=".agents/skills" ;;
    *) usage; exit 1 ;;
  esac
fi

DEST="$BASE/dent"
mkdir -p "$BASE"
rm -rf "$DEST"
cp -R "$SRC" "$DEST"
echo "DENT installed to $DEST"
# Modern Web Guidance ships next to DENT. Refresh our copy; never overwrite a separate install of the official skill.
MDEST="$BASE/modern-web-guidance"
if [ -f "$MWG/SKILL.md" ]; then
  if [ -d "$MDEST" ] && [ ! -f "$MDEST/UPSTREAM.json" ]; then
    echo "Modern Web Guidance already installed at $MDEST (not by DENT): kept as is"
  else
    rm -rf "$MDEST"; cp -R "$MWG" "$MDEST"
    echo "Modern Web Guidance installed to $MDEST"
  fi
fi
echo "Start a new agent session, then ask for design work (e.g. \"Design a sign-up screen for a recipe app\")."

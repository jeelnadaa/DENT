<#
.SYNOPSIS
  DENT installer for Windows - copies skills\dent into an agent's skills folder.
.EXAMPLE
  .\scripts\install.ps1 -Agent claude
  .\scripts\install.ps1 -Agent cursor -Project
  .\scripts\install.ps1 -Path C:\my\skills
  .\scripts\install.ps1 -Agent rules -Path .dent
.NOTES
  Copyright 2026 Jeel Nada (solarquack). Licensed under the Apache License 2.0.
#>
param(
  [ValidateSet('claude','codex','copilot','cursor','gemini','agents','rules','list')]
  [string]$Agent = 'list',
  [switch]$Project,
  [string]$Path
)

$ErrorActionPreference = 'Stop'
$Src = Join-Path $PSScriptRoot '..\skills\dent'
if (-not (Test-Path (Join-Path $Src 'SKILL.md'))) { throw "Cannot find $Src\SKILL.md (run from a DENT clone)." }

function Show-Usage {
@"
DENT installer

  .\scripts\install.ps1 -Agent <agent> [-Project]   install for an agent
  .\scripts\install.ps1 -Path <dir>                 install into <dir>\dent
  .\scripts\install.ps1 -Agent rules -Path <dir>    copy to <dir> and print a rules snippet

Agents (personal path  |  -Project path):
  claude    ~\.claude\skills    | .claude\skills
  codex     ~\.codex\skills     | .agents\skills
  copilot   ~\.copilot\skills   | .github\skills
  cursor    ~\.cursor\skills    | .cursor\skills
  gemini    ~\.gemini\skills    | .gemini\skills
  agents    (project only)      | .agents\skills
"@
}

if ($Agent -eq 'rules') {
  $Dest = if ($Path) { $Path } else { '.dent' }
  if (Test-Path $Dest) { Remove-Item -Recurse -Force $Dest }
  Copy-Item -Recurse $Src $Dest
  Write-Output "DENT copied to $Dest`n"
  Write-Output "Add this to your agent's rules file (AGENTS.md, .windsurf\rules\dent.md, .clinerules\dent.md, CONVENTIONS.md...):`n"
  Write-Output "## Design work (DENT)"
  Write-Output "For any UI, UX, visual design, design-system or front-end styling task, first read ``$Dest/SKILL.md``"
  Write-Output "and follow its workflow. Open files in ``$Dest/references/`` only when SKILL.md points to them."
  return
}

if ($Path) {
  $Base = $Path
} else {
  $h = $HOME
  $map = @{
    'claude'  = @("$h\.claude\skills",  '.claude\skills')
    'codex'   = @("$h\.codex\skills",   '.agents\skills')
    'copilot' = @("$h\.copilot\skills", '.github\skills')
    'cursor'  = @("$h\.cursor\skills",  '.cursor\skills')
    'gemini'  = @("$h\.gemini\skills",  '.gemini\skills')
    'agents'  = @('.agents\skills',     '.agents\skills')
  }
  if (-not $map.ContainsKey($Agent)) { Show-Usage; return }
  $Base = if ($Project) { $map[$Agent][1] } else { $map[$Agent][0] }
}

$Dest = Join-Path $Base 'dent'
New-Item -ItemType Directory -Force -Path $Base | Out-Null
if (Test-Path $Dest) { Remove-Item -Recurse -Force $Dest }
Copy-Item -Recurse $Src $Dest
Write-Output "DENT installed to $Dest"
Write-Output 'Start a new agent session, then ask for design work (e.g. "Design a sign-up screen for a recipe app").'

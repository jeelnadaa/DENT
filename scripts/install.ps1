<#
.SYNOPSIS
  DENT installer for Windows - copies skills\dent (and the bundled Modern Web Guidance skill) into an agent's skills folder.
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
$Mwg = Join-Path $PSScriptRoot '..\skills\modern-web-guidance'
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
  if (Test-Path (Join-Path $Mwg 'SKILL.md')) {
    New-Item -ItemType Directory -Force -Path (Join-Path $Dest 'vendor') | Out-Null
    Copy-Item -Recurse $Mwg (Join-Path $Dest 'vendor\modern-web-guidance')
  }
  Write-Output "DENT copied to $Dest (Modern Web Guidance in $Dest/vendor/modern-web-guidance)`n"
  Write-Output "Add this to your agent's rules file (AGENTS.md, .windsurf\rules\dent.md, .clinerules\dent.md, CONVENTIONS.md...):`n"
  Write-Output "## Design work (DENT)"
  Write-Output "For any UI, UX, visual design, design-system or front-end styling task, first read ``$Dest/SKILL.md``"
  Write-Output "and follow its workflow. Open files in ``$Dest/references/`` only when SKILL.md points to them."
  Write-Output "For any HTML, CSS or client-side JS, follow Google's Modern Web Guidance first:"
  Write-Output "``$Dest/vendor/modern-web-guidance/SKILL.md`` (DENT's summary: ``$Dest/references/modern-web-guidance.md``)."
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
# Modern Web Guidance ships next to DENT. Refresh our copy; never overwrite a separate install of the official skill.
$MDest = Join-Path $Base 'modern-web-guidance'
if (Test-Path (Join-Path $Mwg 'SKILL.md')) {
  if ((Test-Path $MDest) -and -not (Test-Path (Join-Path $MDest 'UPSTREAM.json'))) {
    Write-Output "Modern Web Guidance already installed at $MDest (not by DENT): kept as is"
  } else {
    if (Test-Path $MDest) { Remove-Item -Recurse -Force $MDest }
    Copy-Item -Recurse $Mwg $MDest
    Write-Output "Modern Web Guidance installed to $MDest"
  }
}
Write-Output 'Start a new agent session, then ask for design work (e.g. "Design a sign-up screen for a recipe app").'

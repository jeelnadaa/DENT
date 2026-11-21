# /dent:doctor

Check what this machine and session can actually do (browser checks, FFmpeg, GPU, installed TTS engines, provider keys) and set up missing media tools with the user's permission.

**Usage:** `/dent:doctor [what you want to make, e.g. narrated video]` (also `/dent doctor …` or `dent doctor …`)
**Default depth:** Quick. Effort level and the gates in SKILL.md §3 always apply.

## Load
- `scripts/doctor.py`
- `scripts/tts.py`
- `references/media-sourcing.md` (§2 question, §6 installing)

## Steps
1. Run `python scripts/doctor.py` and read the report (tools, GPU/VRAM, disk, TTS engines, provider keys set: names only).
2. Say in plain words what DENT can do now and what it can't (and what that means for the user's goal).
3. For each missing capability the goal needs, offer the options from media-sourcing.md §2 (local install, free cloud tier, paid provider or connector, own assets).
4. Install only what the user approves: show size and licence first (`tts.py install <engine>`, then `--yes`); verify with one sample.

## Output
Capability report, decisions made, anything installed and verified with a sample.

## Never
- Install anything without a yes.
- Ask the user to paste API keys into chat.
- Promise a capability the report doesn't show.

Close with what DENT can do now, what was installed or decided, and a one-line next step.

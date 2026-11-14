# /dent:update

Update the DENT plugin to the latest version without reinstalling (refreshes the local marketplace copy so Claude's normal update works).

**Usage:** `/dent:update [--check]` (also `/dent update …` or `dent update …`)
**Default depth:** Quick. Effort level and the gates in SKILL.md §3 always apply.

## Load
- `scripts/update_plugin.py`

## Steps
1. Tell the user what you'll do in one line: refresh DENT's local marketplace copy from GitHub (no Claude settings are edited).
2. Run `python scripts/update_plugin.py` from this skill's folder (add `--check` to only report). If Python or git isn't available, explain the manual path: Settings → Plugins → Marketplaces → dent → Update, then update the plugin.
3. Report the installed version and the available version from the script output.
4. If a newer version is available, give the one remaining step: Settings → Plugins → DENT → Update (or remove + add it again, which now gets the new version), or `/plugin update dent@dent` then `/reload-plugins`, or `claude plugin update dent@dent` in a terminal. Then a new chat.
5. Suggest enabling auto-update for the DENT marketplace so future versions arrive automatically.

## Output
Installed vs available version, what was refreshed, and the one step left (if any).

## Never
- Edit Claude's settings or install records by hand.
- Delete the user's plugin folders.

Close with the scorecard summary, attribution (DENT / user / agent judgment / overrides) and a one-line next step (SKILL.md §8).

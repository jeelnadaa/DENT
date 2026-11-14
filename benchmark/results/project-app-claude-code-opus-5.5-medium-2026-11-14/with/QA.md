# Questions and answers

Write down every question the agent asked you, in order, and the answer you chose.
If it asked nothing, write "No questions".

| # | Agent's question | My answer |
|---|---|---|
| 1 | How far should I take the project management screen (kanban, command palette, drawer, burndown, animations)? Options: Skip — you decide all · Standard (Recommended) · Polished · All-out | Standard (Recommended) |
| 2 | Which visual direction should the project board take? Options: Drafting table (Recommended) · Night console · Clean neutral · You decide | Drafting table (Recommended) |
| 3 | Want me to write DESIGN.md so this direction is locked in? (asked after delivery) Options: Write DESIGN.md · Not now | Write DESIGN.md |

## Run details
- Agent (e.g. Claude Code, Antigravity, Codex, Cursor): Claude Code (desktop app, Code tab) with the DENT 2.0 plugin
- Model + effort/reasoning setting: Claude Opus 5.5 (claude-opus-5-5); effort setting: [fill in — not visible to the agent]
- Date: 2026-11-14
- Roughly how long it took: [fill in]
- Times I had to type "continue": 0
- Anything that went wrong:
  - One shell edit (a Python heredoc) was blocked by Claude Code's safety check; the same change was then applied with the Edit tool.
  - The in-app browser pane froze CSS/JS animations at their first frame, so its screenshots were unreliable. Interaction tests and screenshots were redone in headless Chromium (Playwright).
  - Bugs found during testing and fixed before delivery:
    - Drops below a short column were missed.
    - The drawer title rendered with zero height.
    - Focus was lost after palette commands.
    - The empty state showed a misleading chart.
  - Known remaining gap: the touch drag grip is 40 px rather than 44 px.

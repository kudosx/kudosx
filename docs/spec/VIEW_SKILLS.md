# Skill Visualization

## Overview

Full-screen TUI (k9s-style) để browse và manage Claude Code skills.

## Requirements

### UI Components

- **Banner**: ASCII art logo với version info, có margin
- **Skills Table**: DataTable hiển thị danh sách skills, full-height
- **Footer**: Hiển thị keyboard shortcuts

### Table Columns

| Column | Width | Description |
|--------|-------|-------------|
| NAME | 30 | Tên skill |
| STATUS | 12 | installed/available |
| GLOBAL | 10 | Version cài ở ~/.claude/skills |
| LOCAL | 10 | Version cài ở ./.claude/skills |
| (spacer) | auto | Fill remaining width |

### Keyboard Shortcuts

- `q` - Quit
- `r` - Refresh danh sách skills
- `?` - Hiển thị help
- `Enter` - Install/Update skill (TODO)
- `d` - Delete skill (TODO)

### Styling

- Dark theme (#1e1e1e background)
- Orange accent color (#d77757)
- Row highlight full-width khi select
- Border style: solid với title "Skills"

## Implementation

- File: `kudosx/commands/explore.py`
- Command: `kudosx explore`
- Tests: `tests/test_explore.py` (20 tests)

## Status

- [x] Basic TUI layout
- [x] Skills table với status
- [x] Full-width row highlight
- [x] Keyboard shortcuts (quit, refresh, help)
- [x] Unit tests
- [ ] Install/Update action
- [ ] Delete action

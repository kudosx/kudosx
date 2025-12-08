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
| STATUS | 12 | installed/available/update |
| GLOBAL | 10 | Version cài ở ~/.claude/skills |
| LOCAL | 10 | Version cài ở ./.claude/skills |
| LATEST | 10 | Latest version từ GitHub |
| (spacer) | auto | Fill remaining width |

### Status Values

| Status | Color | Description |
|--------|-------|-------------|
| installed | green | Skill đã cài và up-to-date (semantic version comparison) |
| available | dim | Skill chưa cài |
| update | yellow | Có version mới từ remote (installed < latest) |

**Note:** Version comparison sử dụng semantic versioning (e.g., `v1.9.0 < v1.10.0`)

### Keyboard Shortcuts

- `q` - Quit
- `r` - Refresh danh sách skills (fetch latest versions)
- `?` - Hiển thị help
- `Enter` - Install/Update skill
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
- [x] LATEST column with remote version
- [x] Update status detection (installed/available/update)
- [x] Install/Update action (Enter key)
- [ ] Delete action

## Related Specs

- [VERSION_MANAGEMENT.md](VERSION_MANAGEMENT.md) - Version management and update functionality
- [CLI.md](CLI.md) - CLI command reference

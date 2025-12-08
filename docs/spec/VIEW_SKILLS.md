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
- `Enter` - Install/Update skill (shows location selection popup)
- `g` - Install/Update skill to global (~/.claude/skills) - quick action
- `l` - Install/Update skill to local (./.claude/skills) - quick action
- `d` - Delete skill (removes from global ~/.claude/skills)

### Install Location Selection

When pressing `Enter` on a skill, a popup appears to select installation location:

| Option | Path | Description |
|--------|------|-------------|
| Global | ~/.claude/skills | Available to all projects |
| Local | ./.claude/skills | Only for current project |

Quick install shortcuts (`g` and `l`) bypass the popup and install directly to the selected location.

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
- [x] Remote skills.yaml fetching (with local fallback)
- [x] Delete action (d key)
- [x] Install location selection (global/local popup)
- [x] Quick install shortcuts (g for global, l for local)

## Related Specs

- [VERSION_MANAGEMENT.md](VERSION_MANAGEMENT.md) - Version management, remote fetching, and owner sync command
- [CLI.md](CLI.md) - CLI command reference

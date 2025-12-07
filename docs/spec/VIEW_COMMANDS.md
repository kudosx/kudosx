# Commands View

## Overview

Hiển thị danh sách các Claude Code slash commands trong TUI explore.

## Requirements

### UI Components

- **Banner**: ASCII art logo với version info
- **Tab Indicator**: Hiển thị tab "Commands" đang active
- **Commands Table**: DataTable hiển thị danh sách commands
- **Footer**: Hiển thị keyboard shortcuts

### Table Columns

| Column | Width | Description |
|--------|-------|-------------|
| NAME | 30 | Tên command (không có `/`) |
| LOCATION | 10 | global hoặc local |
| PATH | 50 | Đường dẫn đầy đủ tới file .md |
| (spacer) | auto | Fill remaining width |

### Data Sources

Commands được scan từ 2 locations:

| Location | Path | Priority |
|----------|------|----------|
| Global | `~/.claude/commands/*.md` | Lower |
| Local | `./.claude/commands/*.md` | Higher |

### Keyboard Shortcuts

- `a` - Switch to Agents view
- `k` - Switch to Skills view
- `c` - Switch to Commands view
- `q` - Quit
- `r` - Refresh
- `?` - Help
- `Enter` - View command content (TODO)
- `d` - Delete command (TODO)

### Styling

- Dark theme (#1e1e1e background)
- Orange accent color (#d77757)
- Location column: cyan for global, green for local
- Path column: dim color

### Empty State

Khi không có commands:
```
[dim]No commands found[/dim]  [dim]-[/dim]  [dim]-[/dim]
```

## Implementation

- File: `kudosx/commands/explore.py`
- Method: `load_commands()`
- Command: `kudosx explore` then press `c`

### Scanning Logic

```python
global_commands = Path.home() / ".claude" / "commands"
local_commands = Path.cwd() / ".claude" / "commands"

# Scan global first
if global_commands.exists():
    for cmd_file in sorted(global_commands.glob("*.md")):
        # Add to table

# Then scan local
if local_commands.exists():
    for cmd_file in sorted(local_commands.glob("*.md")):
        # Add to table
```

## Status

- [x] Commands table với columns
- [x] Scan global commands
- [x] Scan local commands
- [x] Keyboard shortcut (c)
- [x] Tab indicator update
- [x] Empty state handling
- [x] Unit tests
- [ ] View command content (Enter)
- [ ] Delete command (d)
- [ ] Create new command

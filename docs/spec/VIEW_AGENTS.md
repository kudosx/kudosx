# Agents View

## Overview

Hiển thị danh sách các Claude Code built-in agents trong TUI explore.

## Requirements

### UI Components

- **Banner**: ASCII art logo với version info
- **Tab Indicator**: Hiển thị tab "Agents" đang active
- **Agents Table**: DataTable hiển thị danh sách agents
- **Footer**: Hiển thị keyboard shortcuts

### Table Columns

| Column | Width | Description |
|--------|-------|-------------|
| NAME | 30 | Tên agent |
| TYPE | 15 | Loại agent (research, explore, architect, docs, automation) |
| STATUS | 12 | enabled/disabled |
| (spacer) | auto | Fill remaining width |

### Available Agents

| Name | Type | Description |
|------|------|-------------|
| general-purpose | research | General-purpose agent for complex tasks |
| Explore | explore | Fast agent for exploring codebases |
| Plan | architect | Software architect for implementation plans |
| claude-code-guide | docs | Documentation and feature guide |
| skill-adder | automation | Add new skills to projects |

### Keyboard Shortcuts

- `a` - Switch to Agents view
- `k` - Switch to Skills view
- `c` - Switch to Commands view
- `q` - Quit
- `r` - Refresh
- `?` - Help

### Styling

- Dark theme (#1e1e1e background)
- Orange accent color (#d77757)
- Type column: cyan color
- Status column: green for enabled

## Data Source

```python
AGENTS = [
    {"name": "general-purpose", "type": "research", "description": "..."},
    {"name": "Explore", "type": "explore", "description": "..."},
    {"name": "Plan", "type": "architect", "description": "..."},
    {"name": "claude-code-guide", "type": "docs", "description": "..."},
    {"name": "skill-adder", "type": "automation", "description": "..."},
]
```

## Implementation

- File: `kudosx/commands/explore.py`
- Method: `load_agents()`
- Command: `kudosx explore` then press `a`

## Status

- [x] Agents table với columns
- [x] Keyboard shortcut (a)
- [x] Tab indicator update
- [x] Unit tests
- [ ] Agent details view (Enter)
- [ ] Enable/Disable toggle

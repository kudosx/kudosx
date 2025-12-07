# Explore Tabs Feature

## Overview

Thêm tính năng chuyển đổi giữa các view trong TUI explore bằng keyboard shortcuts.

## Requirements

### Keyboard Shortcuts

| Key | View | Description |
|-----|------|-------------|
| `a` | Agents | Hiển thị danh sách AI agents |
| `k` | Skills | Hiển thị danh sách skills (default) |
| `c` | Commands | Hiển thị danh sách commands |
| `u` | Usage | Hiển thị Claude API usage |

### UI Changes

- **Tab indicator**: Hiển thị tab đang active ở phía trên table
- **Table title**: Thay đổi theo view đang chọn ("Agents", "Skills", "Commands", "Usage")
- **Footer**: Thêm shortcuts `a/k/c/u` vào danh sách

### Tab Indicator Style

```
  [dim]a:Agents[/]  [bold #d77757]k:Skills[/]  [dim]c:Commands[/]  [dim]u:Usage[/]
```

- Tab active: bold, màu accent (#d77757)
- Tab inactive: dim

### Table Columns

#### Agents View
| Column | Width | Description |
|--------|-------|-------------|
| NAME | 30 | Tên agent |
| TYPE | 15 | Loại agent (explore, plan, etc.) |
| STATUS | 12 | enabled/disabled |
| (spacer) | auto | Fill remaining width |

#### Skills View (existing)
| Column | Width | Description |
|--------|-------|-------------|
| NAME | 30 | Tên skill |
| STATUS | 12 | installed/available |
| GLOBAL | 10 | Version ở ~/.claude/skills |
| LOCAL | 10 | Version ở ./.claude/skills |
| (spacer) | auto | Fill remaining width |

#### Commands View
| Column | Width | Description |
|--------|-------|-------------|
| NAME | 30 | Tên command |
| LOCATION | 10 | global/local |
| PATH | 50 | Đường dẫn file .md |
| (spacer) | auto | Fill remaining width |

#### Usage View
| Column | Width | Description |
|--------|-------|-------------|
| METRIC | 30 | Tên metric |
| VALUE | 40 | Giá trị |
| (spacer) | auto | Fill remaining width |

## Implementation

### Files to modify
- `kudosx/commands/explore.py` - Thêm logic chuyển tab

### New bindings
```python
BINDINGS = [
    Binding("a", "show_agents", "Agents"),
    Binding("k", "show_skills", "Skills"),
    Binding("c", "show_commands", "Commands"),
    Binding("u", "show_usage", "Usage"),
    # ... existing bindings
]
```

### State management
```python
class ExploreTUI(App):
    current_view: str = "skills"  # "agents" | "skills" | "commands" | "usage"
```

### Actions
```python
def action_show_agents(self) -> None:
    self.current_view = "agents"
    self.load_agents()

def action_show_skills(self) -> None:
    self.current_view = "skills"
    self.load_skills()

def action_show_commands(self) -> None:
    self.current_view = "commands"
    self.load_commands()

def action_show_usage(self) -> None:
    self.current_view = "usage"
    self.load_usage()
```

## Data Sources

### Agents
- Hardcoded list từ Claude Code agent types
- Types: general-purpose, Explore, Plan, claude-code-guide, etc.

### Skills
- Existing: `kudosx.commands.add.SKILLS`

### Commands
- Scan: `~/.claude/commands/*.md` (global)
- Scan: `./.claude/commands/*.md` (local)

### Usage
- Source: `claude usage` command output
- Fallback: "Usage data unavailable" if command fails

## Status

- [x] Tab indicator widget
- [x] Agents view
- [x] Commands view
- [x] Usage view
- [x] Keyboard shortcuts (a/k/c/u)
- [x] Update tests

# Footer Bar Feature

## Overview

Footer bar hiển thị keyboard shortcuts cho TUI explore. Textual Footer widget tự động hiển thị các bindings với `show=True`.

## Requirements

### UI Layout

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  ╭─────────────────────────────── Skills ────────────────────────────────╮   │
│  │ NAME                 STATUS      GLOBAL     LOCAL                     │   │
│  │ browser-use          installed   0.1.0      -                         │   │
│  │ ...                                                                   │   │
│  ╰───────────────────────────────────────────────────────────────────────╯   │
├──────────────────────────────────────────────────────────────────────────────┤
│  a Agents  k Skills  c Commands  u Usage  │  q Quit  r Refresh  ? Help      │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Keyboard Shortcuts

#### Tab Navigation (always visible)

| Key | Action | Description |
|-----|--------|-------------|
| `a` | show_agents | Chuyển sang Agents view |
| `k` | show_skills | Chuyển sang Skills view |
| `c` | show_commands | Chuyển sang Commands view |
| `u` | show_usage | Chuyển sang Usage view |

#### General Actions (always visible)

| Key | Action | Description |
|-----|--------|-------------|
| `q` | quit | Thoát ứng dụng |
| `r` | refresh | Refresh data hiện tại |
| `?` | help | Hiển thị help dialog |

#### Skills View Actions (context-specific)

| Key | Action | Description | Visible |
|-----|--------|-------------|---------|
| `enter` | install_update | Install hoặc update skill đang chọn | No |
| `g` | install_global | Install skill vào global (~/.claude/skills) | No |
| `l` | install_local | Install skill vào local (./.claude/skills) | No |
| `d` | delete_item | Xóa skill đã install | No |

#### Usage View Actions (context-specific)

| Key | Action | Description | Visible |
|-----|--------|-------------|---------|
| `d` | usage_daily | Hiển thị usage theo ngày | No |
| `w` | usage_weekly | Hiển thị usage theo tuần | No |
| `m` | usage_monthly | Hiển thị usage theo tháng | No |

### Binding Priority

Một số key được tái sử dụng theo context:
- `d`: Delete skill (Skills view) / Daily usage (Usage view)

### Footer Styling

```css
Footer {
    background: #1e1e1e;
    color: #cccccc;
    dock: bottom;
    height: 1;
}

Footer > .footer--key {
    background: #3d3d3d;
    color: #d77757;
    text-style: bold;
}

Footer > .footer--description {
    color: #cccccc;
}
```

## Implementation

### Files modified
- `kudosx/commands/explore.py`

### Bindings Definition

```python
class ExploreTUI(App):
    BINDINGS = [
        # Tab navigation (visible in footer)
        Binding("a", "show_agents", "Agents"),
        Binding("k", "show_skills", "Skills"),
        Binding("c", "show_commands", "Commands"),
        Binding("u", "show_usage", "Usage"),

        # Usage period shortcuts (hidden)
        Binding("d", "usage_daily", "Daily", show=False),
        Binding("w", "usage_weekly", "Weekly", show=False),
        Binding("m", "usage_monthly", "Monthly", show=False),

        # General actions (visible)
        Binding("q", "quit", "Quit"),
        Binding("r", "refresh", "Refresh"),
        Binding("?", "help", "Help"),

        # Skills actions (hidden)
        Binding("enter", "install_update", "Install/Update", show=False),
        Binding("g", "install_global", "Install Global", show=False),
        Binding("l", "install_local", "Install Local", show=False),
    ]
```

### ExploreTable Bindings

```python
class ExploreTable(DataTable):
    BINDINGS = [
        Binding("enter", "select_item", "Select"),
        Binding("d", "delete_item", "Delete"),
    ]
```

### InstallLocationDialog Bindings

```python
class InstallLocationDialog(ModalScreen):
    BINDINGS = [
        Binding("escape", "cancel", "Cancel"),
        Binding("g", "select_global", "Global", show=False),
        Binding("l", "select_local", "Local", show=False),
    ]
```

### Compose Footer

```python
def compose(self) -> ComposeResult:
    with Horizontal(id="header"):
        yield SystemInfo(id="system-info")
        yield ExplorerTabs(id="explorer-tabs")
        yield Static(self._render_banner(), id="banner")
    yield ExploreTable(id="data-table")
    yield Footer()  # Auto-displays bindings with show=True
```

## Notes

- Sử dụng Textual's built-in `Footer` widget
- Bindings với `show=False` không hiển thị trong footer nhưng vẫn hoạt động
- Footer tự động cập nhật khi focus thay đổi giữa các widgets

## Status

- [x] Tab navigation shortcuts (a/k/c/u)
- [x] General actions (q/r/?)
- [x] Skills view actions (enter/g/l/d)
- [x] Usage view actions (d/w/m)
- [x] Footer widget integration

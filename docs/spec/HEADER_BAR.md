# Header Bar Feature

## Overview

Layout với 3 phần theo chiều ngang: System Info, Explorer Tabs (vertical), và KudosX Banner.

## Requirements

### UI Layout

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  ┌───────────────┐  ┌────────────┐  ┌─────────────────────────────────────┐  │
│  │ SYSTEM INFO   │  │ a  agents  │  │  ██╗  ██╗██╗   ██╗██████╗  ...      │  │
│  │ OS: Darwin    │  │ k  skills← │  │  ██║ ██╔╝██║   ██║██╔══██╗ ...      │  │
│  │ Python: 3.14  │  │ c  commands│  │  █████╔╝ ██║   ██║██║  ██║ ...      │  │
│  │ Claude: 2.0   │  │ u  usage   │  │  ...                                │  │
│  │ Kudosx: 0.3   │  │            │  │                                     │  │
│  └───────────────┘  └────────────┘  └─────────────────────────────────────┘  │
│                                                                              │
├──────────────────────────────────────────────────────────────────────────────┤
│  ╭─────────────────────────────── Skills ────────────────────────────────╮   │
│  │ NAME                 STATUS      GLOBAL     LOCAL                     │   │
│  │ browser-use          installed   0.1.0      -                         │   │
│  │ ...                                                                   │   │
│  ╰───────────────────────────────────────────────────────────────────────╯   │
├──────────────────────────────────────────────────────────────────────────────┤
│  q Quit  r Refresh  ? Help                                                   │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Header Components (3 columns)

| Component | Position | Width | Description |
|-----------|----------|-------|-------------|
| System Info | Left | 20 | OS, Python, Claude version |
| Explorer Tabs | Center | 16 | Vertical tab list |
| KudosX Banner | Right | 1fr | ASCII art logo |

### System Info Content

```
OS     : Darwin
Python : 3.14
Claude : 2.0.60
Kudosx : 0.2.5
```

- **OS**: Từ `platform.system()`
- **Python**: Từ `sys.version_info`
- **Claude**: Từ `claude --version` command (extract x.y.z)
- **Kudosx**: Từ `kudosx.__version__`

### Label Styling

Labels sử dụng màu accent (#d77757), aligned với 6 chars:
```python
f"[#d77757]OS     :[/] {os_name}"
f"[#d77757]Python :[/] {py_ver}"
f"[#d77757]Claude :[/] {claude_ver}"
f"[#d77757]Kudosx :[/] {kudosx_ver}"
```

### Explorer Tabs (Vertical)

```
a  agents      ← 'a' underlined
k  skills      ← active (highlighted), 'k' underlined
c  commands    ← 'c' underlined
u  usage       ← 'u' underlined
```

- Active tab: bold, orange (#d77757)
- Inactive tabs: dim
- Shortcut letter underlined within label (lowercase)

### KudosX Banner

ASCII art logo với version info, right-aligned trong container.

### Styling

```css
#header {
    height: 8;
    layout: horizontal;
    background: #1e1e1e;
    margin: 1 1 0 1;
}

#system-info {
    width: 20;
    padding: 1;
    border: solid #3d3d3d;
    background: #1e1e1e;
}

#explorer-tabs {
    width: 16;
    padding: 1;
    border: solid #3d3d3d;
    background: #1e1e1e;
}

#banner {
    width: 1fr;
    background: #1e1e1e;
    padding: 0 1;
    overflow: hidden;
    content-align: right middle;
}
```

## Implementation

### Files modified
- `kudosx/commands/explore.py`

### Helper function

```python
def get_claude_version() -> str:
    """Get Claude Code version by running claude --version."""
    try:
        result = subprocess.run(
            ["claude", "--version"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        if result.returncode == 0:
            # Extract x.y.z version pattern
            match = re.search(r"(\d+\.\d+\.\d+)", result.stdout)
            if match:
                return match.group(1)
    except (subprocess.TimeoutExpired, FileNotFoundError, Exception):
        pass
    return "N/A"
```

### Widgets

```python
from kudosx import __version__

class SystemInfo(Static):
    """System information panel."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._claude_version = get_claude_version()

    def render(self) -> str:
        os_name = platform.system()
        py_ver = f"{sys.version_info.major}.{sys.version_info.minor}"

        return (
            f"[#d77757]OS:[/] {os_name}\n"
            f"[#d77757]Python:[/] {py_ver}\n"
            f"[#d77757]Claude:[/] {self._claude_version}\n"
            f"[#d77757]Kudosx:[/] {__version__}"
        )


class ExplorerTabs(Static):
    """Vertical explorer tabs."""

    current_tab: reactive[str] = reactive("skills")

    def render(self) -> str:
        # (key, before_underline, underline_char, after_underline, tab_name)
        tabs = [
            ("a", "", "a", "gents", "agents"),       # a  _a_gents
            ("k", "s", "k", "ills", "skills"),       # k  s_k_ills
            ("c", "", "c", "ommands", "commands"),   # c  _c_ommands
            ("u", "", "u", "sage", "usage"),         # u  _u_sage
        ]
        lines = []
        for key, before, char, after, tab_name in tabs:
            if tab_name == self.current_tab:
                lines.append(f"[bold #d77757]{key}  {before}[underline]{char}[/underline]{after}[/]")
            else:
                lines.append(f"[dim]{key}  {before}[underline]{char}[/underline]{after}[/]")
        return "\n".join(lines)
```

### Compose

```python
def compose(self) -> ComposeResult:
    with Horizontal(id="header"):
        yield SystemInfo(id="system-info")
        yield ExplorerTabs(id="explorer-tabs")
        yield Static(self._render_banner(), id="banner")
    yield ExploreTable(id="data-table")
    yield Footer()
```

## Status

- [x] Create SystemInfo widget with Claude version detection
- [x] Create ExplorerTabs widget (vertical)
- [x] Update header layout (horizontal 3-column)
- [x] Update CSS
- [x] Update tests

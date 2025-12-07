# Usage View

## Overview

Hiển thị thông tin usage của Claude Code API trong TUI explore với các report theo Daily, Weekly, Monthly.

## Requirements

### UI Components

- **Banner**: Title box hiển thị "Claude Code Token Usage Report - {Period}"
- **Period Tabs**: Sub-tabs để chọn Daily (d), Weekly (w), Monthly (m)
- **Usage Table**: Bảng thống kê chi tiết token usage
- **Footer**: Hiển thị keyboard shortcuts

### Period Options

| Key | Period | Description |
|-----|--------|-------------|
| `d` | Daily | Thống kê theo ngày |
| `w` | Weekly | Thống kê theo tuần |
| `m` | Monthly | Thống kê theo tháng |

### Table Columns

| Column | Width | Description |
|--------|-------|-------------|
| Date | 10 | Ngày/Tuần/Tháng (format: YYYY-MM-DD) |
| Models | 25 | Danh sách TẤT CẢ models sử dụng (bullet list, multi-line) |
| Input | 10 | Input tokens |
| Output | 10 | Output tokens |
| Cache Create | 11 | Cache creation tokens |
| Cache Read | 11 | Cache read tokens |
| Total Tokens | 11 | Tổng tokens |
| Cost (USD) | 10 | Chi phí USD |

### Models Display

Cột Models hiển thị **TẤT CẢ** các models được sử dụng trong period đó:
- Mỗi model một dòng với format `- model-name`
- Không giới hạn số lượng models
- Models được normalize: `opus-4-5`, `sonnet-4-5`, `haiku-4-5`
- Skip synthetic models (`<synthetic>`)

Ví dụ với 3 models:
```
- haiku-4-5
- opus-4-5
- sonnet-4-5
```

### Table Format Example

```
╭──────────────────────────────────────────╮
│                                          │
│  Claude Code Token Usage Report - Daily  │
│                                          │
╰──────────────────────────────────────────╯

┌──────────┬───────────────────────────┬──────────┬──────────┬───────────┬───────────┬───────────┬──────────┐
│ Date     │ Models                    │    Input │   Output │     Cache │     Cache │     Total │     Cost │
│          │                           │          │          │    Create │      Read │    Tokens │    (USD) │
├──────────┼───────────────────────────┼──────────┼──────────┼───────────┼───────────┼───────────┼──────────┤
│ 2025     │ - haiku-4-5               │  652,923 │   92,594 │ 2,519,938 │ 53,041,9… │ 56,307,3… │   $46.00 │
│ 12-07    │ - opus-4-5                │          │          │           │           │           │          │
│          │ - sonnet-4-5              │          │          │           │           │           │          │
├──────────┼───────────────────────────┼──────────┼──────────┼───────────┼───────────┼───────────┼──────────┤
│ Total    │                           │ 4,228,4… │ 1,337,2… │ 48,790,6… │ 821,943,… │ 876,299,… │  $656.34 │
└──────────┴───────────────────────────┴──────────┴──────────┴───────────┴───────────┴───────────┴──────────┘
```

### Data Formatting

- **Numbers**: Dùng thousand separator (,) - ví dụ: 1,234,567
- **Truncation**: Số dài hơn column width sẽ truncate với "…" - ví dụ: 53,041,9…
- **Cost**: Format "$X.XX" - tính theo per-model pricing từ LiteLLM
- **Models**: Hiển thị TẤT CẢ models dạng bullet list "- model-name" (multi-line)
- **Date**: Split thành 2 dòng nếu cần (YYYY trên, MM-DD dưới)
- **Model names**: Normalize thành short form (opus-4-5, sonnet-4-5, haiku-4-5)

### Keyboard Shortcuts

**Main Navigation:**
- `u` - Switch to Usage view
- `a` - Switch to Agents view
- `k` - Switch to Skills view
- `c` - Switch to Commands view
- `q` - Quit
- `r` - Refresh
- `?` - Help

**Usage Period Tabs (khi đang ở Usage view):**
- `d` - Daily report
- `w` - Weekly report
- `m` - Monthly report

**Note:** Delete shortcut không hiển thị trong Usage view vì không thể xóa usage data.

### Styling

- Dark theme (#1e1e1e background)
- Orange accent color (#d77757)
- Numbers: cyan color
- Total row: bold
- Box border: rounded corners (╭╮╰╯)
- Table border: standard box drawing (┌┐└┘├┤┬┴┼─│)

## Data Source

### Session Files

Data được parse từ Claude Code session files tại `~/.claude/projects/`:

```python
from kudosx.utils.claude_usage import get_claude_usage, aggregate_usage

usage = get_claude_usage()  # Parse all session files
daily = aggregate_usage(usage, "daily")  # Aggregate by period
```

### Data Processing (matching ccusage behavior)

1. **Deduplication**: Skip duplicate entries using `message.id:requestId` hash
2. **Timezone**: Sử dụng local timezone để nhóm ngày (không dùng UTC)
3. **Schema Validation**: Require cả `input_tokens` và `output_tokens`
4. **Skip Synthetic**: Bỏ qua model `<synthetic>`
5. **Per-model Cost**: Tính cost chính xác cho từng model

### Model Pricing (from LiteLLM)

```python
MODEL_PRICING = {
    "opus-4-5":   {"input": 5.0, "output": 25.0, "cache_create": 6.25, "cache_read": 0.50},
    "sonnet-4-5": {"input": 3.0, "output": 15.0, "cache_create": 3.75, "cache_read": 0.30},
    "haiku-4-5":  {"input": 1.0, "output": 5.0,  "cache_create": 1.25, "cache_read": 0.10},
}
```

### Data Structures

```python
from dataclasses import dataclass
from datetime import date
from typing import Literal

@dataclass
class DailyUsage:
    """Usage data for a single day."""
    date: date
    models: list[str]  # ["haiku-4-5", "opus-4-5", "sonnet-4-5"]
    input_tokens: int
    output_tokens: int
    cache_create_tokens: int
    cache_read_tokens: int

    @property
    def total_tokens(self) -> int:
        return (self.input_tokens + self.output_tokens +
                self.cache_create_tokens + self.cache_read_tokens)

    @property
    def cost_usd(self) -> float:
        # Cost calculation based on model pricing
        pass

UsagePeriod = Literal["daily", "weekly", "monthly"]
```

### Aggregation Logic

```python
def aggregate_usage(
    daily_data: list[DailyUsage],
    period: UsagePeriod
) -> list[dict]:
    """Aggregate daily usage data by period."""
    if period == "daily":
        return daily_data
    elif period == "weekly":
        # Group by ISO week (Monday-Sunday)
        pass
    elif period == "monthly":
        # Group by month
        pass
```

## Implementation

- File: `kudosx/commands/explore.py`
- Method: `load_usage(period: UsagePeriod)`
- Command: `kudosx explore` then press `u`

### State Variables

```python
class ExplorerApp(App):
    # ... existing code ...
    usage_period: reactive[str] = reactive("daily")  # daily, weekly, monthly
```

### ExplorerTabs Update

```python
class ExplorerTabs(Static):
    """Vertical explorer tabs."""

    current_tab: reactive[str] = reactive("skills")

    def render(self) -> str:
        """Render vertical tabs."""
        tabs = [
            ("a", "Agents"),
            ("k", "Skills"),
            ("c", "Commands"),
            ("u", "Usage"),
        ]
        lines = []
        for key, label in tabs:
            if label.lower() == self.current_tab:
                lines.append(f"[bold #d77757]{key} {label}[/]")
            else:
                lines.append(f"[dim]{key} {label}[/]")
        return "\n".join(lines)
```

### UsagePeriodTabs Widget

```python
class UsagePeriodTabs(Static):
    """Horizontal period tabs for Usage view."""

    current_period: reactive[str] = reactive("daily")

    def render(self) -> str:
        """Render horizontal period tabs."""
        tabs = [
            ("d", "Daily"),
            ("w", "Weekly"),
            ("m", "Monthly"),
        ]
        parts = []
        for key, label in tabs:
            if label.lower() == self.current_period:
                parts.append(f"[bold #d77757][{key}] {label}[/]")
            else:
                parts.append(f"[dim][{key}] {label}[/dim]")
        return "  ".join(parts)
```

### load_usage Method

```python
def load_usage(self, period: str = "daily") -> None:
    """Load usage data into the table."""
    self.current_view = "usage"
    self.usage_period = period

    table = self.query_one("#data-table", DataTable)
    table.clear(columns=True)
    table.border_title = f"Claude Code Token Usage Report - {period.title()}"

    # Add columns
    table.add_column("Date", width=10)
    table.add_column("Models", width=25)
    table.add_column("Input", width=10)
    table.add_column("Output", width=10)
    table.add_column("Cache Create", width=11)
    table.add_column("Cache Read", width=11)
    table.add_column("Total Tokens", width=11)
    table.add_column("Cost (USD)", width=10)

    self.usage_data = []
    raw_usage = get_claude_usage()
    parsed_data = parse_usage_data(raw_usage)
    aggregated_data = aggregate_usage(parsed_data, period)

    for row in aggregated_data:
        models_str = "\n".join(f"- {m}" for m in row["models"])
        table.add_row(
            row["date_display"],
            models_str,
            format_number(row["input_tokens"]),
            format_number(row["output_tokens"]),
            format_number(row["cache_create"]),
            format_number(row["cache_read"]),
            format_number(row["total_tokens"]),
            f"${row['cost']:.2f}",
        )

    # Add total row
    totals = calculate_totals(aggregated_data)
    table.add_row(
        "[bold]Total[/bold]",
        "",
        f"[bold]{format_number(totals['input'])}[/bold]",
        f"[bold]{format_number(totals['output'])}[/bold]",
        f"[bold]{format_number(totals['cache_create'])}[/bold]",
        f"[bold]{format_number(totals['cache_read'])}[/bold]",
        f"[bold]{format_number(totals['total'])}[/bold]",
        f"[bold]${totals['cost']:.2f}[/bold]",
    )

    table.cursor_type = "row"
```

### Key Bindings

```python
def action_usage_daily(self) -> None:
    """Switch to daily usage view."""
    if self.current_view == "usage":
        self.load_usage("daily")

def action_usage_weekly(self) -> None:
    """Switch to weekly usage view."""
    if self.current_view == "usage":
        self.load_usage("weekly")

def action_usage_monthly(self) -> None:
    """Switch to monthly usage view."""
    if self.current_view == "usage":
        self.load_usage("monthly")
```

### Helper Functions

```python
def format_number(n: int, max_width: int = 10) -> str:
    """Format number with thousand separator, truncate if needed."""
    formatted = f"{n:,}"
    if len(formatted) > max_width:
        return formatted[:max_width-1] + "…"
    return formatted

def parse_usage_data(raw: str) -> list[DailyUsage]:
    """Parse raw claude usage output into structured data."""
    # Implementation depends on actual claude usage output format
    pass

def calculate_totals(data: list[dict]) -> dict:
    """Calculate sum totals for all columns."""
    return {
        "input": sum(d["input_tokens"] for d in data),
        "output": sum(d["output_tokens"] for d in data),
        "cache_create": sum(d["cache_create"] for d in data),
        "cache_read": sum(d["cache_read"] for d in data),
        "total": sum(d["total_tokens"] for d in data),
        "cost": sum(d["cost"] for d in data),
    }
```

## Status

- [x] Usage table với columns (cũ)
- [x] Keyboard shortcut (u)
- [x] Tab indicator update
- [x] get_claude_usage helper function
- [x] Daily/Weekly/Monthly period tabs
- [x] New table format với 8 columns
- [x] Number formatting (thousand separator)
- [x] Truncation với "…"
- [x] Total row calculation
- [x] Period aggregation logic
- [x] Unit tests update (45 tests passing)

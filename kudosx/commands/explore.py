"""Explore command for Kudosx CLI - Browse available skills."""

import platform
import re
import subprocess
import sys
from pathlib import Path

import click
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical, Center
from textual.reactive import reactive
from textual.screen import ModalScreen
from textual.widgets import Button, DataTable, Footer, Static
from textual.worker import Worker

from kudosx.commands.add import SKILLS, get_latest_version, download_and_extract_skill
from kudosx import __version__, __package_name__
from kudosx.utils.claude_usage import (
    get_claude_usage as get_usage_from_sessions,
    format_number,
    aggregate_usage,
    calculate_totals,
)
from kudosx.utils.version import is_update_available, format_version

# Claude Code built-in agents
AGENTS = [
    {"name": "general-purpose", "type": "research", "description": "General-purpose agent for complex tasks"},
    {"name": "Explore", "type": "explore", "description": "Fast agent for exploring codebases"},
    {"name": "Plan", "type": "architect", "description": "Software architect for implementation plans"},
    {"name": "claude-code-guide", "type": "docs", "description": "Documentation and feature guide"},
    {"name": "skill-adder", "type": "automation", "description": "Add new skills to projects"},
]

BANNER_ART = [
    "  ██╗  ██╗██╗   ██╗██████╗  ██████╗ ███████╗██╗   ██╗  ",
    "  ██║ ██╔╝██║   ██║██╔══██╗██╔═══██╗██╔════╝╚██╗ ██╔╝  ",
    "  █████╔╝ ██║   ██║██║  ██║██║   ██║███████╗ ╚████╔╝   ",
    "  ██╔═██╗ ██║   ██║██║  ██║██║   ██║╚════██║ ██╔═██╗   ",
    "  ██║  ██╗╚██████╔╝██████╔╝╚██████╔╝███████║██╔╝  ██╗  ",
    "  ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝   ╚═╝  ",
]


def get_installed_version(skill_path: Path) -> str | None:
    """Get installed version from VERSION file."""
    version_file = skill_path / "VERSION"
    if version_file.exists():
        return version_file.read_text().strip()
    return None


class ExploreTable(DataTable):
    """Data table for explore views."""

    BINDINGS = [
        Binding("enter", "select_item", "Select"),
        Binding("d", "delete_item", "Delete"),
    ]


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


def get_claude_usage() -> dict:
    """Get Claude Code usage from local session files."""
    try:
        return get_usage_from_sessions()
    except Exception:
        return {}


class SystemInfo(Static):
    """System information panel."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._claude_version = get_claude_version()

    def render(self) -> str:
        """Render system information."""
        os_name = platform.system()
        py_ver = f"{sys.version_info.major}.{sys.version_info.minor}"

        return (
            f"[#d77757]OS     :[/] {os_name}\n"
            f"[#d77757]Python :[/] {py_ver}\n"
            f"[#d77757]Claude :[/] {self._claude_version}\n"
            f"[#d77757]Kudosx :[/] {__version__}"
        )


class ExplorerTabs(Static):
    """Vertical explorer tabs."""

    current_tab: reactive[str] = reactive("skills")

    def render(self) -> str:
        """Render vertical tabs.

        Format: key  label with shortcut letter underlined (lowercase).
        Example: a  agents, k  skills, c  commands, u  usage
        """
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
                # Active tab: bold accent color with underlined letter in label
                lines.append(f"[bold #d77757]{key}  {before}[underline]{char}[/underline]{after}[/]")
            else:
                # Inactive tab: dim with underlined letter in label
                lines.append(f"[dim]{key}  {before}[underline]{char}[/underline]{after}[/]")
        return "\n".join(lines)


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


class InstallLocationScreen(ModalScreen):
    """Modal screen for selecting install location (global/local)."""

    CSS = """
    InstallLocationScreen {
        align: center middle;
    }

    #install-dialog {
        width: 50;
        height: auto;
        padding: 1 2;
        background: #2d2d2d;
        border: solid #d77757;
    }

    #install-dialog-title {
        text-align: center;
        text-style: bold;
        color: #d77757;
        margin-bottom: 1;
    }

    #install-dialog-subtitle {
        text-align: center;
        color: #888888;
        margin-bottom: 1;
    }

    .install-button {
        width: 100%;
        margin: 1 0;
    }

    .install-button:focus {
        background: #d77757;
    }

    #btn-global {
        background: #3d6d3d;
    }

    #btn-local {
        background: #3d5d6d;
    }

    #btn-cancel {
        background: #4d4d4d;
    }
    """

    BINDINGS = [
        Binding("escape", "cancel", "Cancel"),
        Binding("g", "select_global", "Global", show=False),
        Binding("l", "select_local", "Local", show=False),
    ]

    def __init__(self, skill_name: str):
        super().__init__()
        self.skill_name = skill_name

    def compose(self) -> ComposeResult:
        with Vertical(id="install-dialog"):
            yield Static(f"Install {self.skill_name}", id="install-dialog-title")
            yield Static("Select installation location", id="install-dialog-subtitle")
            yield Button("[g] Global (~/.claude/skills)", id="btn-global", classes="install-button")
            yield Button("[l] Local (./.claude/skills)", id="btn-local", classes="install-button")
            yield Button("Cancel", id="btn-cancel", classes="install-button")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        if event.button.id == "btn-global":
            self.dismiss("global")
        elif event.button.id == "btn-local":
            self.dismiss("local")
        else:
            self.dismiss(None)

    def action_cancel(self) -> None:
        """Cancel installation."""
        self.dismiss(None)

    def action_select_global(self) -> None:
        """Select global installation."""
        self.dismiss("global")

    def action_select_local(self) -> None:
        """Select local installation."""
        self.dismiss("local")


def colorize_banner(text: str) -> str:
    """Apply Rich markup colors to ASCII art."""
    result = ""
    for char in text:
        if char == "█":
            result += f"[#d77757]{char}[/]"
        elif char in "╗╔╝╚║═":
            result += f"[#eb9f7f]{char}[/]"
        else:
            result += char
    return result


class ExploreTUI(App):
    """Full-screen TUI for exploring KudosX skills."""

    CSS = """
    Screen {
        background: #1e1e1e;
        layout: vertical;
    }

    Footer {
        background: #2d2d2d;
    }

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

    #usage-period-tabs {
        height: 1;
        margin: 0 2;
        padding: 0 1;
        display: none;
    }

    #usage-period-tabs.visible {
        display: block;
    }

    #data-table {
        background: #1e1e1e;
        margin: 1 1 0 1;
        height: 1fr;
        width: 100%;
        border: solid #d77757;
        border-title-color: #d77757;
        border-title-style: bold;
        border-title-align: center;
    }

    DataTable > .datatable--header {
        background: #2d2d2d;
        color: #d77757;
        text-style: bold;
    }

    DataTable > .datatable--cursor {
        background: #d77757;
        color: #1e1e1e;
        width: 100%;
    }

    DataTable > .datatable--hover {
        background: #3d3d3d;
        width: 100%;
    }

    DataTable {
        scrollbar-size: 0 0;
    }
    """

    BINDINGS = [
        Binding("a", "show_agents", "Agents"),
        Binding("k", "show_skills", "Skills"),
        Binding("c", "show_commands", "Commands"),
        Binding("u", "show_usage", "Usage"),
        Binding("d", "usage_daily", "Daily", show=False),
        Binding("w", "usage_weekly", "Weekly", show=False),
        Binding("m", "usage_monthly", "Monthly", show=False),
        Binding("q", "quit", "Quit"),
        Binding("r", "refresh", "Refresh"),
        Binding("?", "help", "Help"),
        Binding("enter", "install_update", "Install/Update", show=False),
        Binding("g", "install_global", "Install Global", show=False),
        Binding("l", "install_local", "Install Local", show=False),
    ]

    current_view: reactive[str] = reactive("skills")
    usage_period: reactive[str] = reactive("daily")

    def __init__(self):
        super().__init__()
        self.skills_data = []
        self.agents_data = []
        self.commands_data = []
        self.usage_data = []
        self._cached_usage: dict | None = None
        self._latest_versions: dict | None = None

    def compose(self) -> ComposeResult:
        with Horizontal(id="header"):
            yield SystemInfo(id="system-info")
            yield ExplorerTabs(id="explorer-tabs")
            yield Static(self._render_banner(), id="banner")
        yield UsagePeriodTabs(id="usage-period-tabs")
        yield ExploreTable(id="data-table")
        yield Footer()

    def _render_banner(self) -> str:
        """Render the ASCII art banner with version."""
        lines = []
        for art_line in BANNER_ART:
            colored = colorize_banner(art_line)
            lines.append(colored)
        return "\n".join(lines)

    def on_mount(self) -> None:
        """Initialize the app."""
        self.title = f"{__package_name__} v{__version__}"
        self.sub_title = "Explorer"
        table = self.query_one("#data-table", DataTable)
        table.fixed_columns = 0
        self.load_skills()

    def watch_current_view(self, view: str) -> None:
        """React to current_view changes."""
        explorer_tabs = self.query_one("#explorer-tabs", ExplorerTabs)
        explorer_tabs.current_tab = view

    def load_skills(self) -> None:
        """Load skills data into the table."""
        self.current_view = "skills"
        table = self.query_one("#data-table", DataTable)
        table.clear(columns=True)
        table.border_title = "Skills"

        # Add columns (spacer column with large width fills remaining space)
        table.add_column("NAME", width=30)
        table.add_column("STATUS", width=12)
        table.add_column("GLOBAL", width=10)
        table.add_column("LOCAL", width=10)
        table.add_column("LATEST", width=10)
        table.add_column(" ", width=500)  # Spacer fills remaining width

        global_base = Path.home() / ".claude" / "skills"
        local_base = Path.cwd() / ".claude" / "skills"

        self.skills_data = []

        for skill_name, config in sorted(SKILLS.items()):
            target_dir = config["target_dir"]
            global_path = global_base / target_dir
            local_path = local_base / target_dir

            global_installed = global_path.exists()
            local_installed = local_path.exists()

            global_ver = get_installed_version(global_path) if global_installed else None
            local_ver = get_installed_version(local_path) if local_installed else None
            latest_ver = self._latest_versions.get(skill_name) if self._latest_versions else None

            # Determine status based on installed vs latest
            status = self._get_skill_status(global_ver, local_ver, latest_ver)

            self.skills_data.append({
                "name": skill_name,
                "config": config,
                "global_path": global_path,
                "local_path": local_path,
                "global_ver": global_ver,
                "local_ver": local_ver,
                "latest_ver": latest_ver,
            })

            table.add_row(
                skill_name,
                status,
                f"[green]{global_ver}[/green]" if global_ver else "[dim]-[/dim]",
                f"[cyan]{local_ver}[/cyan]" if local_ver else "[dim]-[/dim]",
                f"[#d77757]{latest_ver}[/]" if latest_ver else "[dim]...[/dim]",
                " ",  # Spacer
            )

        table.cursor_type = "row"

        # Fetch latest versions in background if not cached
        if not self._latest_versions:
            self.run_worker(self._fetch_latest_versions, thread=True, name="_fetch_latest_versions")

    def _get_skill_status(self, global_ver: str | None, local_ver: str | None, latest_ver: str | None) -> str:
        """Determine skill status based on versions using semantic version comparison."""
        installed_ver = global_ver or local_ver
        if not installed_ver:
            return "[dim]available[/dim]"
        if not latest_ver:
            return "[green]installed[/green]"  # Can't check, assume OK
        if is_update_available(installed_ver, latest_ver):
            return "[yellow]update[/yellow]"
        return "[green]installed[/green]"

    def _fetch_latest_versions(self) -> dict:
        """Fetch latest versions from GitHub in background."""
        versions = {}
        for skill_name, config in SKILLS.items():
            versions[skill_name] = get_latest_version(config["repo"])
        return versions

    def load_agents(self) -> None:
        """Load agents data into the table."""
        self.current_view = "agents"
        table = self.query_one("#data-table", DataTable)
        table.clear(columns=True)
        table.border_title = "Agents"

        table.add_column("NAME", width=30)
        table.add_column("TYPE", width=15)
        table.add_column("STATUS", width=12)
        table.add_column(" ", width=500)

        self.agents_data = []

        for agent in AGENTS:
            self.agents_data.append(agent)
            table.add_row(
                agent["name"],
                f"[cyan]{agent['type']}[/cyan]",
                "[green]enabled[/green]",
                " ",
            )

        table.cursor_type = "row"

    def load_commands(self) -> None:
        """Load commands data into the table."""
        self.current_view = "commands"
        table = self.query_one("#data-table", DataTable)
        table.clear(columns=True)
        table.border_title = "Commands"

        table.add_column("NAME", width=30)
        table.add_column("LOCATION", width=10)
        table.add_column("PATH", width=50)
        table.add_column(" ", width=500)

        global_commands = Path.home() / ".claude" / "commands"
        local_commands = Path.cwd() / ".claude" / "commands"

        self.commands_data = []

        # Scan global commands
        if global_commands.exists():
            for cmd_file in sorted(global_commands.glob("*.md")):
                cmd_name = cmd_file.stem
                self.commands_data.append({
                    "name": cmd_name,
                    "location": "global",
                    "path": cmd_file,
                })
                table.add_row(
                    cmd_name,
                    "[cyan]global[/cyan]",
                    f"[dim]{cmd_file}[/dim]",
                    " ",
                )

        # Scan local commands
        if local_commands.exists():
            for cmd_file in sorted(local_commands.glob("*.md")):
                cmd_name = cmd_file.stem
                self.commands_data.append({
                    "name": cmd_name,
                    "location": "local",
                    "path": cmd_file,
                })
                table.add_row(
                    cmd_name,
                    "[green]local[/green]",
                    f"[dim]{cmd_file}[/dim]",
                    " ",
                )

        if not self.commands_data:
            table.add_row(
                "[dim]No commands found[/dim]",
                "[dim]-[/dim]",
                "[dim]-[/dim]",
                " ",
            )

        table.cursor_type = "row"

    def load_usage(self, period: str = None) -> None:
        """Load usage data into the table."""
        if period:
            self.usage_period = period

        self.current_view = "usage"

        # Show/hide period tabs
        period_tabs = self.query_one("#usage-period-tabs", UsagePeriodTabs)
        period_tabs.add_class("visible")
        period_tabs.current_period = self.usage_period

        table = self.query_one("#data-table", DataTable)
        table.clear(columns=True)
        table.border_title = f"Claude Code Token Usage Report - {self.usage_period.title()}"

        # Add columns for new format
        table.add_column("Date", width=10)
        table.add_column("Models", width=25)
        table.add_column("Input", width=10)
        table.add_column("Output", width=10)
        table.add_column("Cache Create", width=12)
        table.add_column("Cache Read", width=12)
        table.add_column("Total Tokens", width=12)
        table.add_column("Cost (USD)", width=10)

        self.usage_data = []
        # Show loading state
        table.add_row("[dim]Loading...[/dim]", "", "", "", "", "", "", "")
        table.cursor_type = "row"

        # Fetch usage data in background if not cached
        if self._cached_usage:
            self._update_usage_table(self._cached_usage)
        else:
            self.run_worker(self._fetch_usage, thread=True, name="_fetch_usage")

    def _fetch_usage(self) -> dict:
        """Fetch usage data in background thread."""
        return get_claude_usage()

    def on_worker_state_changed(self, event: Worker.StateChanged) -> None:
        """Handle worker completion."""
        if event.state.name == "SUCCESS":
            if event.worker.name == "_fetch_usage":
                self._cached_usage = event.worker.result
                self._update_usage_table(event.worker.result)
            elif event.worker.name == "_fetch_latest_versions":
                self._latest_versions = event.worker.result
                # Refresh skills table with latest versions
                if self.current_view == "skills":
                    self.load_skills()
            elif event.worker.name.startswith("install_"):
                success, result = event.worker.result
                skill_name = event.worker.name.replace("install_", "")
                if success:
                    self.notify(f"Installed {skill_name} to {result}", severity="information")
                    self.load_skills()  # Refresh to show new version
                else:
                    self.notify(f"Failed to install {skill_name}: {result}", severity="error")
            elif event.worker.name.startswith("delete_"):
                success, result = event.worker.result
                skill_name = event.worker.name.replace("delete_", "")
                if success:
                    self.notify(f"Deleted {skill_name}", severity="information")
                    self.load_skills()  # Refresh to show updated status
                else:
                    self.notify(f"Failed to delete {skill_name}: {result}", severity="error")

    def _update_usage_table(self, usage_data: dict) -> None:
        """Update usage table with fetched data."""
        if self.current_view != "usage":
            return

        table = self.query_one("#data-table", DataTable)
        table.clear()

        if usage_data and usage_data.get("by_date"):
            # Aggregate data by selected period
            aggregated = aggregate_usage(usage_data, self.usage_period)

            for row in aggregated:
                models_str = "\n".join(f"- {m}" for m in row["models"]) if row["models"] else "-"
                is_current = row.get("is_current", False)

                # Highlight current date/week/month with orange
                if is_current:
                    table.add_row(
                        f"[bold #d77757]{row['date_display']}[/]",
                        f"[#d77757]{models_str}[/]",
                        f"[bold #d77757]{format_number(row['input_tokens'])}[/]",
                        f"[bold #d77757]{format_number(row['output_tokens'])}[/]",
                        f"[bold #d77757]{format_number(row['cache_create'])}[/]",
                        f"[bold #d77757]{format_number(row['cache_read'])}[/]",
                        f"[bold #d77757]{format_number(row['total_tokens'])}[/]",
                        f"[bold #d77757]${row['cost']:.2f}[/]",
                    )
                else:
                    table.add_row(
                        row["date_display"],
                        models_str,
                        f"[cyan]{format_number(row['input_tokens'])}[/cyan]",
                        f"[cyan]{format_number(row['output_tokens'])}[/cyan]",
                        f"[cyan]{format_number(row['cache_create'])}[/cyan]",
                        f"[cyan]{format_number(row['cache_read'])}[/cyan]",
                        f"[cyan]{format_number(row['total_tokens'])}[/cyan]",
                        f"[green]${row['cost']:.2f}[/green]",
                    )

            # Add total row
            if aggregated:
                totals = calculate_totals(aggregated)
                table.add_row(
                    "[bold]Total[/bold]",
                    "",
                    f"[bold cyan]{format_number(totals['input'])}[/bold cyan]",
                    f"[bold cyan]{format_number(totals['output'])}[/bold cyan]",
                    f"[bold cyan]{format_number(totals['cache_create'])}[/bold cyan]",
                    f"[bold cyan]{format_number(totals['cache_read'])}[/bold cyan]",
                    f"[bold cyan]{format_number(totals['total'])}[/bold cyan]",
                    f"[bold green]${totals['cost']:.2f}[/bold green]",
                )

            self.usage_data = aggregated
        else:
            table.add_row(
                "[dim]No usage data[/dim]",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
            )

    def _hide_period_tabs(self) -> None:
        """Hide the usage period tabs."""
        period_tabs = self.query_one("#usage-period-tabs", UsagePeriodTabs)
        period_tabs.remove_class("visible")

    def action_show_agents(self) -> None:
        """Switch to agents view."""
        self._hide_period_tabs()
        self.load_agents()

    def action_show_skills(self) -> None:
        """Switch to skills view."""
        self._hide_period_tabs()
        self.load_skills()

    def action_show_commands(self) -> None:
        """Switch to commands view."""
        self._hide_period_tabs()
        self.load_commands()

    def action_show_usage(self) -> None:
        """Switch to usage view."""
        self.load_usage()

    def action_usage_daily(self) -> None:
        """Switch to daily usage view or delete skill."""
        if self.current_view == "usage":
            self.load_usage("daily")
        elif self.current_view == "skills":
            self.action_delete_skill()

    def action_usage_weekly(self) -> None:
        """Switch to weekly usage view."""
        if self.current_view == "usage":
            self.load_usage("weekly")

    def action_usage_monthly(self) -> None:
        """Switch to monthly usage view."""
        if self.current_view == "usage":
            self.load_usage("monthly")

    def action_refresh(self) -> None:
        """Refresh the current view."""
        if self.current_view == "usage":
            self._cached_usage = None  # Clear cache on refresh
        elif self.current_view == "skills":
            self._latest_versions = None  # Clear cache to re-fetch latest versions
        if self.current_view == "agents":
            self.load_agents()
        elif self.current_view == "commands":
            self.load_commands()
        elif self.current_view == "usage":
            self.load_usage()
        else:
            self.load_skills()
        self.notify(f"{self.current_view.capitalize()} refreshed", severity="information")

    def action_help(self) -> None:
        """Show help."""
        if self.current_view == "usage":
            msg = "a/k/c/u: Switch view | d/w/m: Period | q: Quit | r: Refresh"
        elif self.current_view == "skills":
            msg = "Enter: Install | g: Global | l: Local | d: Delete | r: Refresh | q: Quit"
        else:
            msg = "a/k/c/u: Switch view | q: Quit | r: Refresh"
        self.notify(msg, title="Keyboard Shortcuts", severity="information")

    def action_install_update(self) -> None:
        """Install or update the selected skill - shows location selection popup."""
        if self.current_view != "skills":
            return

        table = self.query_one("#data-table", DataTable)
        if table.cursor_row is None or table.cursor_row >= len(self.skills_data):
            return

        skill = self.skills_data[table.cursor_row]
        skill_name = skill["name"]

        # Show location selection popup
        self.push_screen(InstallLocationScreen(skill_name), self._on_install_location_selected)

    def _on_install_location_selected(self, location: str | None) -> None:
        """Handle install location selection from popup."""
        if location is None:
            return  # Cancelled

        table = self.query_one("#data-table", DataTable)
        if table.cursor_row is None or table.cursor_row >= len(self.skills_data):
            return

        skill = self.skills_data[table.cursor_row]
        self._do_install_at_location(skill, location)

    def action_install_global(self) -> None:
        """Install the selected skill to global location (~/.claude/skills)."""
        if self.current_view != "skills":
            return

        table = self.query_one("#data-table", DataTable)
        if table.cursor_row is None or table.cursor_row >= len(self.skills_data):
            return

        skill = self.skills_data[table.cursor_row]
        self._do_install_at_location(skill, "global")

    def action_install_local(self) -> None:
        """Install the selected skill to local location (./.claude/skills)."""
        if self.current_view != "skills":
            return

        table = self.query_one("#data-table", DataTable)
        if table.cursor_row is None or table.cursor_row >= len(self.skills_data):
            return

        skill = self.skills_data[table.cursor_row]
        self._do_install_at_location(skill, "local")

    def _do_install_at_location(self, skill: dict, location: str) -> None:
        """Install a skill at the specified location (global or local)."""
        skill_name = skill["name"]
        config = skill["config"]
        latest_ver = skill.get("latest_ver")

        # Determine target path based on location
        if location == "local":
            target_path = skill["local_path"]
        else:
            target_path = skill["global_path"]

        self.notify(f"Installing {skill_name} ({location})...", severity="information")

        # Run installation in background
        self.run_worker(
            lambda: self._do_install_skill(config, target_path, latest_ver),
            thread=True,
            name=f"install_{skill_name}",
        )

    def _do_install_skill(self, config: dict, target_path: Path, version: str | None) -> tuple[bool, str]:
        """Perform skill installation in background thread."""
        try:
            download_and_extract_skill(
                repo=config["repo"],
                source_path=config["source_path"],
                target_path=target_path,
                version=version,
            )
            return True, str(target_path)
        except Exception as e:
            return False, str(e)

    def action_delete_skill(self) -> None:
        """Delete the selected skill."""
        if self.current_view != "skills":
            return

        table = self.query_one("#data-table", DataTable)
        if table.cursor_row is None or table.cursor_row >= len(self.skills_data):
            return

        skill = self.skills_data[table.cursor_row]
        skill_name = skill["name"]
        global_path = skill["global_path"]
        local_path = skill["local_path"]

        # Check if skill is installed
        global_installed = global_path.exists()
        local_installed = local_path.exists()

        if not global_installed and not local_installed:
            self.notify(f"{skill_name} is not installed", severity="warning")
            return

        # Prefer deleting global, then local
        if global_installed:
            target_path = global_path
            location = "global"
        else:
            target_path = local_path
            location = "local"

        self.notify(f"Deleting {skill_name} ({location})...", severity="information")

        # Run deletion in background
        self.run_worker(
            lambda: self._do_delete_skill(target_path),
            thread=True,
            name=f"delete_{skill_name}",
        )

    def _do_delete_skill(self, target_path: Path) -> tuple[bool, str]:
        """Perform skill deletion in background thread."""
        import shutil
        try:
            shutil.rmtree(target_path)
            return True, str(target_path)
        except Exception as e:
            return False, str(e)


def run_tui():
    """Run the explore TUI."""
    app = ExploreTUI()
    app.run()


@click.command("explore")
def explore():
    """Explore available skills in a full-screen TUI.

    Opens a k9s-style interactive interface to browse and manage
    skills. Use keyboard shortcuts to navigate and install skills.

    Shortcuts:
        q: Quit
        r: Refresh
        Enter: Install/Update
        d: Delete
        ?: Help

    Examples:

        kudosx explore
    """
    run_tui()


if __name__ == "__main__":
    run_tui()

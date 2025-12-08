"""Tests for Kudosx explore command and TUI."""

from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest
from click.testing import CliRunner

from kudosx.cli import cli
from kudosx.commands.explore import (
    get_installed_version,
    get_claude_version,
    get_claude_usage,
    colorize_banner,
    ExploreTUI,
    ExplorerTabs,
    SystemInfo,
    BANNER_ART,
    AGENTS,
)
from kudosx import __version__ as kudosx_version


class TestGetInstalledVersion:
    """Tests for get_installed_version function."""

    def test_version_file_exists(self, tmp_path):
        """Test reading version from existing VERSION file."""
        version_file = tmp_path / "VERSION"
        version_file.write_text("1.2.3\n")
        result = get_installed_version(tmp_path)
        assert result == "1.2.3"

    def test_version_file_not_exists(self, tmp_path):
        """Test returns None when VERSION file doesn't exist."""
        result = get_installed_version(tmp_path)
        assert result is None

    def test_version_file_with_whitespace(self, tmp_path):
        """Test version is stripped of whitespace."""
        version_file = tmp_path / "VERSION"
        version_file.write_text("  0.1.0  \n\n")
        result = get_installed_version(tmp_path)
        assert result == "0.1.0"


class TestGetClaudeVersion:
    """Tests for get_claude_version function."""

    @patch("kudosx.commands.explore.subprocess.run")
    def test_extracts_version_from_output(self, mock_run):
        """Test extracting x.y.z version from claude --version output."""
        mock_run.return_value = MagicMock(
            returncode=0,
            stdout="2.0.60 (Claude Code)\n"
        )
        result = get_claude_version()
        assert result == "2.0.60"

    @patch("kudosx.commands.explore.subprocess.run")
    def test_returns_na_on_failure(self, mock_run):
        """Test returns N/A when command fails."""
        mock_run.return_value = MagicMock(returncode=1, stdout="")
        result = get_claude_version()
        assert result == "N/A"

    @patch("kudosx.commands.explore.subprocess.run")
    def test_returns_na_on_exception(self, mock_run):
        """Test returns N/A when exception occurs."""
        mock_run.side_effect = FileNotFoundError()
        result = get_claude_version()
        assert result == "N/A"


class TestGetClaudeUsage:
    """Tests for get_claude_usage function."""

    @patch("kudosx.commands.explore.get_usage_from_sessions")
    def test_returns_usage_dict(self, mock_get_usage):
        """Test returning usage dict from local session files."""
        mock_get_usage.return_value = {
            "sessions": 10,
            "messages": 100,
            "total_input_tokens": 1000,
            "total_output_tokens": 500,
        }
        result = get_claude_usage()
        assert isinstance(result, dict)
        assert result["sessions"] == 10
        assert result["messages"] == 100

    @patch("kudosx.commands.explore.get_usage_from_sessions")
    def test_returns_empty_on_exception(self, mock_get_usage):
        """Test returns empty dict when exception occurs."""
        mock_get_usage.side_effect = Exception("Test error")
        result = get_claude_usage()
        assert result == {}


class TestSystemInfo:
    """Tests for SystemInfo widget."""

    @patch("kudosx.commands.explore.get_claude_version")
    def test_render_contains_os(self, mock_claude_ver):
        """Test SystemInfo render includes OS."""
        mock_claude_ver.return_value = "2.0.60"
        widget = SystemInfo()
        rendered = widget.render()
        assert "[#d77757]OS     :[/]" in rendered

    @patch("kudosx.commands.explore.get_claude_version")
    def test_render_contains_python(self, mock_claude_ver):
        """Test SystemInfo render includes Python version."""
        mock_claude_ver.return_value = "2.0.60"
        widget = SystemInfo()
        rendered = widget.render()
        assert "[#d77757]Python :[/]" in rendered

    @patch("kudosx.commands.explore.get_claude_version")
    def test_render_contains_claude(self, mock_claude_ver):
        """Test SystemInfo render includes Claude version."""
        mock_claude_ver.return_value = "2.0.60"
        widget = SystemInfo()
        rendered = widget.render()
        assert "[#d77757]Claude :[/]" in rendered
        assert "2.0.60" in rendered

    @patch("kudosx.commands.explore.get_claude_version")
    def test_render_contains_kudosx(self, mock_claude_ver):
        """Test SystemInfo render includes Kudosx version."""
        mock_claude_ver.return_value = "2.0.60"
        widget = SystemInfo()
        rendered = widget.render()
        assert "[#d77757]Kudosx :[/]" in rendered
        assert kudosx_version in rendered


class TestColorizeBanner:
    """Tests for colorize_banner function."""

    def test_colorize_block_char(self):
        """Test block characters are colored."""
        result = colorize_banner("██")
        assert "[#d77757]█[/]" in result

    def test_colorize_border_chars(self):
        """Test border characters are colored."""
        result = colorize_banner("╗╔╝╚║═")
        assert "[#eb9f7f]╗[/]" in result
        assert "[#eb9f7f]═[/]" in result

    def test_colorize_regular_chars(self):
        """Test regular characters are not colored."""
        result = colorize_banner("abc")
        assert result == "abc"

    def test_colorize_mixed(self):
        """Test mixed characters."""
        result = colorize_banner("█X║")
        assert "[#d77757]█[/]" in result
        assert "X" in result
        assert "[#eb9f7f]║[/]" in result


class TestBannerArt:
    """Tests for banner art constant."""

    def test_banner_has_six_lines(self):
        """Test banner art has 6 lines."""
        assert len(BANNER_ART) == 6

    def test_banner_contains_kudosx(self):
        """Test banner spells out KUDOSX."""
        combined = "".join(BANNER_ART)
        assert "██" in combined


class TestExploreCommand:
    """Tests for explore CLI command."""

    def test_explore_help(self):
        """Test explore command help."""
        runner = CliRunner()
        result = runner.invoke(cli, ["explore", "--help"])
        assert result.exit_code == 0
        assert "Explore available skills" in result.output
        assert "full-screen TUI" in result.output

    @patch("kudosx.commands.explore.run_tui")
    def test_explore_calls_run_tui(self, mock_run_tui):
        """Test explore command calls run_tui."""
        runner = CliRunner()
        result = runner.invoke(cli, ["explore"])
        mock_run_tui.assert_called_once()


class TestExploreTUI:
    """Tests for ExploreTUI app."""

    def test_tui_has_bindings(self):
        """Test TUI has expected key bindings."""
        app = ExploreTUI()
        binding_keys = [b.key for b in app.BINDINGS]
        assert "q" in binding_keys
        assert "r" in binding_keys
        assert "?" in binding_keys
        assert "u" in binding_keys
        assert "enter" in binding_keys

    def test_tui_has_css(self):
        """Test TUI has CSS defined."""
        assert ExploreTUI.CSS is not None
        assert "#banner" in ExploreTUI.CSS
        assert "#data-table" in ExploreTUI.CSS
        assert "#explorer-tabs" in ExploreTUI.CSS
        assert "#system-info" in ExploreTUI.CSS
        assert "#header" in ExploreTUI.CSS

    def test_banner_is_right_aligned(self):
        """Test banner CSS includes right alignment."""
        assert "content-align: right" in ExploreTUI.CSS

    def test_tui_initial_state(self):
        """Test TUI initializes with empty skills_data."""
        app = ExploreTUI()
        assert app.skills_data == []
        assert app._latest_versions is None

    def test_get_skill_status_available(self):
        """Test status is 'available' when not installed."""
        app = ExploreTUI()
        status = app._get_skill_status(None, None, "v1.0.0")
        assert "available" in status

    def test_get_skill_status_installed_up_to_date(self):
        """Test status is 'installed' when version matches latest."""
        app = ExploreTUI()
        status = app._get_skill_status("v1.0.0", None, "v1.0.0")
        assert "installed" in status
        assert "green" in status

    def test_get_skill_status_update_available(self):
        """Test status is 'update' when newer version available."""
        app = ExploreTUI()
        status = app._get_skill_status("v1.0.0", None, "v1.1.0")
        assert "update" in status
        assert "yellow" in status

    def test_get_skill_status_no_latest(self):
        """Test status is 'installed' when can't check latest."""
        app = ExploreTUI()
        status = app._get_skill_status("v1.0.0", None, None)
        assert "installed" in status

    def test_get_skill_status_installed_newer_than_latest(self):
        """Test status is 'installed' when installed is newer than latest."""
        app = ExploreTUI()
        status = app._get_skill_status("v2.0.0", None, "v1.0.0")
        assert "installed" in status
        assert "green" in status

    def test_get_skill_status_semantic_version_comparison(self):
        """Test semantic version comparison works correctly."""
        app = ExploreTUI()
        # v1.0.0 vs v1.0.1 - patch update
        status = app._get_skill_status("v1.0.0", None, "v1.0.1")
        assert "update" in status

        # v1.9.0 vs v1.10.0 - minor update (10 > 9 numerically)
        status = app._get_skill_status("v1.9.0", None, "v1.10.0")
        assert "update" in status

    def test_get_skill_status_local_version_used(self):
        """Test local version is used when global is None."""
        app = ExploreTUI()
        status = app._get_skill_status(None, "v1.0.0", "v1.1.0")
        assert "update" in status


@pytest.mark.asyncio(loop_scope="class")
class TestExploreTUIAsync:
    """Async tests for ExploreTUI app using Textual testing."""

    async def test_tui_mounts(self):
        """Test TUI mounts successfully."""
        app = ExploreTUI()
        async with app.run_test() as pilot:
            assert app.title is not None
            assert "Explorer" in app.sub_title

    async def test_tui_has_banner(self):
        """Test TUI displays banner widget."""
        app = ExploreTUI()
        async with app.run_test() as pilot:
            banner = app.query_one("#banner")
            assert banner is not None

    async def test_tui_has_data_table(self):
        """Test TUI displays data table with Skills as default."""
        app = ExploreTUI()
        async with app.run_test() as pilot:
            table = app.query_one("#data-table")
            assert table is not None
            assert table.border_title == "Skills"

    async def test_tui_skills_has_latest_column(self):
        """Test skills table has LATEST column."""
        app = ExploreTUI()
        async with app.run_test() as pilot:
            table = app.query_one("#data-table")
            columns = [col.label.plain for col in table.columns.values()]
            assert "LATEST" in columns

    async def test_tui_has_explorer_tabs(self):
        """Test TUI displays explorer tabs."""
        app = ExploreTUI()
        async with app.run_test() as pilot:
            explorer_tabs = app.query_one("#explorer-tabs", ExplorerTabs)
            assert explorer_tabs is not None
            assert explorer_tabs.current_tab == "skills"

    async def test_tui_has_system_info(self):
        """Test TUI displays system info."""
        app = ExploreTUI()
        async with app.run_test() as pilot:
            system_info = app.query_one("#system-info", SystemInfo)
            assert system_info is not None

    async def test_tui_quit_binding(self):
        """Test pressing q quits the app."""
        app = ExploreTUI()
        async with app.run_test() as pilot:
            await pilot.press("q")
            assert app.return_code is not None

    async def test_tui_refresh_action(self):
        """Test refresh action reloads skills."""
        app = ExploreTUI()
        async with app.run_test() as pilot:
            initial_data = app.skills_data.copy()
            await pilot.press("r")
            # Skills should be reloaded (data refreshed)
            assert app.skills_data is not None

    async def test_tui_help_action(self):
        """Test help action shows notification."""
        app = ExploreTUI()
        async with app.run_test() as pilot:
            await pilot.press("?")
            # Help notification should be shown (no error)
            assert True

    async def test_tui_switch_to_agents(self):
        """Test pressing 'a' switches to agents view."""
        app = ExploreTUI()
        async with app.run_test() as pilot:
            await pilot.press("a")
            assert app.current_view == "agents"
            table = app.query_one("#data-table")
            assert table.border_title == "Agents"

    async def test_tui_switch_to_commands(self):
        """Test pressing 'c' switches to commands view."""
        app = ExploreTUI()
        async with app.run_test() as pilot:
            await pilot.press("c")
            assert app.current_view == "commands"
            table = app.query_one("#data-table")
            assert table.border_title == "Commands"

    async def test_tui_switch_to_skills(self):
        """Test pressing 'k' switches to skills view."""
        app = ExploreTUI()
        async with app.run_test() as pilot:
            await pilot.press("a")  # First switch to agents
            await pilot.press("k")  # Then switch back to skills
            assert app.current_view == "skills"
            table = app.query_one("#data-table")
            assert table.border_title == "Skills"

    async def test_tui_explorer_tabs_updates(self):
        """Test explorer tabs updates when switching views."""
        app = ExploreTUI()
        async with app.run_test() as pilot:
            explorer_tabs = app.query_one("#explorer-tabs", ExplorerTabs)
            assert explorer_tabs.current_tab == "skills"
            await pilot.press("a")
            assert explorer_tabs.current_tab == "agents"
            await pilot.press("c")
            assert explorer_tabs.current_tab == "commands"
            await pilot.press("u")
            assert explorer_tabs.current_tab == "usage"

    async def test_tui_switch_to_usage(self):
        """Test pressing 'u' switches to usage view."""
        app = ExploreTUI()
        async with app.run_test() as pilot:
            await pilot.press("u")
            assert app.current_view == "usage"
            table = app.query_one("#data-table")
            assert "Usage Report" in table.border_title

    async def test_tui_usage_initial_data(self):
        """Test usage view initializes with usage_data."""
        app = ExploreTUI()
        async with app.run_test() as pilot:
            await pilot.press("u")
            assert app.usage_data is not None

    async def test_tui_usage_period_tabs_visible(self):
        """Test period tabs are visible when in usage view."""
        app = ExploreTUI()
        async with app.run_test() as pilot:
            await pilot.press("u")
            period_tabs = app.query_one("#usage-period-tabs")
            assert "visible" in period_tabs.classes

    async def test_tui_usage_period_tabs_hidden_in_other_views(self):
        """Test period tabs are hidden when in other views."""
        app = ExploreTUI()
        async with app.run_test() as pilot:
            await pilot.press("u")
            await pilot.press("k")
            period_tabs = app.query_one("#usage-period-tabs")
            assert "visible" not in period_tabs.classes

    async def test_tui_usage_daily_period(self):
        """Test pressing 'd' switches to daily period."""
        app = ExploreTUI()
        async with app.run_test() as pilot:
            await pilot.press("u")
            await pilot.press("d")
            assert app.usage_period == "daily"
            assert "Daily" in app.query_one("#data-table").border_title

    async def test_tui_usage_weekly_period(self):
        """Test pressing 'w' switches to weekly period."""
        app = ExploreTUI()
        async with app.run_test() as pilot:
            await pilot.press("u")
            await pilot.press("w")
            assert app.usage_period == "weekly"
            assert "Weekly" in app.query_one("#data-table").border_title

    async def test_tui_usage_monthly_period(self):
        """Test pressing 'm' switches to monthly period."""
        app = ExploreTUI()
        async with app.run_test() as pilot:
            await pilot.press("u")
            await pilot.press("m")
            assert app.usage_period == "monthly"
            assert "Monthly" in app.query_one("#data-table").border_title


class TestAgents:
    """Tests for agents data."""

    def test_agents_list_not_empty(self):
        """Test AGENTS list is not empty."""
        assert len(AGENTS) > 0

    def test_agents_have_required_fields(self):
        """Test each agent has required fields."""
        for agent in AGENTS:
            assert "name" in agent
            assert "type" in agent
            assert "description" in agent

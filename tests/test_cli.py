"""Tests for Kudosx CLI."""

from unittest.mock import MagicMock, patch

from click.testing import CliRunner

from kudosx.cli import cli
from kudosx import __version__


def test_cli_version():
    """Test CLI version command."""
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert "kudosx" in result.output
    assert __version__ in result.output


def test_cli_help():
    """Test CLI help command."""
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "Kudosx" in result.output


@patch("kudosx.commands.explore.ExploreTUI.run")
def test_cli_default_runs_explore(mock_run):
    """Test that running kudosx without subcommand launches explore."""
    runner = CliRunner()
    result = runner.invoke(cli, [])
    assert result.exit_code == 0
    mock_run.assert_called_once()


def test_search_help():
    """Test search command help."""
    runner = CliRunner()
    result = runner.invoke(cli, ["search", "--help"])
    assert result.exit_code == 0
    assert "Search for files or content" in result.output


def test_cloud_help():
    """Test cloud command help."""
    runner = CliRunner()
    result = runner.invoke(cli, ["cloud", "--help"])
    assert result.exit_code == 0
    assert "industry-standard cloud" in result.output


def test_software_help():
    """Test software command help."""
    runner = CliRunner()
    result = runner.invoke(cli, ["software", "--help"])
    assert result.exit_code == 0
    assert "industry-standard software" in result.output


class TestCloudCommand:
    """Tests for the cloud command."""

    @patch("kudosx.commands.cloud.subprocess.run")
    @patch("kudosx.commands.cloud.get_content_path")
    def test_cloud_success(self, mock_get_content_path, mock_run):
        """Test cloud command runs tree successfully."""
        mock_path = MagicMock()
        mock_path.__truediv__ = lambda self, x: MagicMock(exists=lambda: True)
        mock_get_content_path.return_value = mock_path
        mock_run.return_value = MagicMock(stdout="mock tree output\n", returncode=0)
        runner = CliRunner()
        result = runner.invoke(cli, ["cloud"])
        assert result.exit_code == 0
        assert "mock tree output" in result.output
        mock_run.assert_called_once()

    @patch("kudosx.commands.cloud.subprocess.run")
    @patch("kudosx.commands.cloud.get_content_path")
    def test_cloud_with_level_option(self, mock_get_content_path, mock_run):
        """Test cloud command with custom level option."""
        mock_path = MagicMock()
        mock_path.__truediv__ = lambda self, x: MagicMock(exists=lambda: True)
        mock_get_content_path.return_value = mock_path
        mock_run.return_value = MagicMock(stdout="mock tree output\n", returncode=0)
        runner = CliRunner()
        result = runner.invoke(cli, ["cloud", "-L", "5"])
        assert result.exit_code == 0
        call_args = mock_run.call_args[0][0]
        assert "-L" in call_args
        assert "5" in call_args

    @patch("kudosx.commands.cloud.subprocess.run")
    @patch("kudosx.commands.cloud.get_content_path")
    def test_cloud_tree_not_found(self, mock_get_content_path, mock_run):
        """Test cloud command when tree is not installed."""
        mock_path = MagicMock()
        mock_path.__truediv__ = lambda self, x: MagicMock(exists=lambda: True)
        mock_get_content_path.return_value = mock_path
        mock_run.side_effect = FileNotFoundError()
        runner = CliRunner()
        result = runner.invoke(cli, ["cloud"])
        assert result.exit_code == 1
        assert "tree" in result.output
        assert "not found" in result.output

    @patch("kudosx.commands.cloud.get_content_path")
    def test_cloud_template_not_found(self, mock_get_content_path):
        """Test cloud command when template directory doesn't exist."""
        mock_path = MagicMock()
        mock_path.__truediv__ = lambda self, x: MagicMock(exists=lambda: False)
        mock_get_content_path.return_value = mock_path
        runner = CliRunner()
        result = runner.invoke(cli, ["cloud"])
        assert result.exit_code == 1
        assert "Template not found" in result.output


class TestSoftwareCommand:
    """Tests for the software command."""

    @patch("kudosx.commands.software.subprocess.run")
    @patch("kudosx.commands.software.get_content_path")
    def test_software_success(self, mock_get_content_path, mock_run):
        """Test software command runs tree successfully."""
        mock_path = MagicMock()
        mock_path.__truediv__ = lambda self, x: MagicMock(exists=lambda: True)
        mock_get_content_path.return_value = mock_path
        mock_run.return_value = MagicMock(stdout="mock tree output\n", returncode=0)
        runner = CliRunner()
        result = runner.invoke(cli, ["software"])
        assert result.exit_code == 0
        assert "mock tree output" in result.output
        mock_run.assert_called_once()

    @patch("kudosx.commands.software.subprocess.run")
    @patch("kudosx.commands.software.get_content_path")
    def test_software_with_level_option(self, mock_get_content_path, mock_run):
        """Test software command with custom level option."""
        mock_path = MagicMock()
        mock_path.__truediv__ = lambda self, x: MagicMock(exists=lambda: True)
        mock_get_content_path.return_value = mock_path
        mock_run.return_value = MagicMock(stdout="mock tree output\n", returncode=0)
        runner = CliRunner()
        result = runner.invoke(cli, ["software", "-L", "2"])
        assert result.exit_code == 0
        call_args = mock_run.call_args[0][0]
        assert "-L" in call_args
        assert "2" in call_args

    @patch("kudosx.commands.software.subprocess.run")
    @patch("kudosx.commands.software.get_content_path")
    def test_software_tree_not_found(self, mock_get_content_path, mock_run):
        """Test software command when tree is not installed."""
        mock_path = MagicMock()
        mock_path.__truediv__ = lambda self, x: MagicMock(exists=lambda: True)
        mock_get_content_path.return_value = mock_path
        mock_run.side_effect = FileNotFoundError()
        runner = CliRunner()
        result = runner.invoke(cli, ["software"])
        assert result.exit_code == 1
        assert "tree" in result.output
        assert "not found" in result.output

    @patch("kudosx.commands.software.get_content_path")
    def test_software_template_not_found(self, mock_get_content_path):
        """Test software command when template directory doesn't exist."""
        mock_path = MagicMock()
        mock_path.__truediv__ = lambda self, x: MagicMock(exists=lambda: False)
        mock_get_content_path.return_value = mock_path
        runner = CliRunner()
        result = runner.invoke(cli, ["software"])
        assert result.exit_code == 1
        assert "Template not found" in result.output

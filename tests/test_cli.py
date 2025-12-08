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


class TestUpdateCommand:
    """Tests for the update command."""

    def test_update_help(self):
        """Test update command help."""
        runner = CliRunner()
        result = runner.invoke(cli, ["update", "--help"])
        assert result.exit_code == 0
        assert "Update installed skills" in result.output
        assert "--all" in result.output
        assert "--local" in result.output

    def test_update_requires_name_or_all(self):
        """Test update command requires name or --all flag."""
        runner = CliRunner()
        result = runner.invoke(cli, ["update"])
        assert result.exit_code == 1
        assert "Specify a skill name or use --all" in result.output

    def test_update_unknown_skill(self):
        """Test update command with unknown skill."""
        runner = CliRunner()
        result = runner.invoke(cli, ["update", "unknown-skill"])
        assert result.exit_code == 1
        assert "Unknown skill" in result.output

    @patch("kudosx.commands.update.get_installed_skills")
    def test_update_all_no_skills(self, mock_get_installed):
        """Test update --all when no skills installed."""
        mock_get_installed.return_value = []
        runner = CliRunner()
        result = runner.invoke(cli, ["update", "--all"])
        assert result.exit_code == 0
        assert "No skills installed" in result.output

    @patch("kudosx.commands.update.Path")
    def test_update_skill_not_installed(self, mock_path):
        """Test update specific skill when not installed."""
        mock_path.home.return_value = MagicMock()
        mock_path.home.return_value.__truediv__ = lambda self, x: MagicMock(
            __truediv__=lambda self, x: MagicMock(
                __truediv__=lambda self, x: MagicMock(exists=lambda: False)
            )
        )
        runner = CliRunner()
        result = runner.invoke(cli, ["update", "skill-browser-use"])
        assert result.exit_code == 1
        assert "not installed" in result.output

    @patch("kudosx.commands.update.get_latest_version")
    @patch("kudosx.commands.update.download_and_extract_skill")
    @patch("kudosx.commands.update.get_installed_version")
    @patch("kudosx.commands.update.Path")
    def test_update_skill_success(
        self, mock_path, mock_get_installed, mock_download, mock_get_latest
    ):
        """Test successful skill update."""
        # Mock path to exist
        mock_skill_path = MagicMock()
        mock_skill_path.exists.return_value = True
        mock_path.home.return_value.__truediv__.return_value.__truediv__.return_value.__truediv__.return_value = mock_skill_path

        mock_get_installed.return_value = "v1.0.0"
        mock_get_latest.return_value = "v1.1.0"

        runner = CliRunner()
        result = runner.invoke(cli, ["update", "skill-browser-use"])

        # Should attempt to download and extract
        assert mock_get_latest.called

    @patch("kudosx.commands.update.get_latest_version")
    @patch("kudosx.commands.update.get_installed_version")
    @patch("kudosx.commands.update.Path")
    def test_update_skill_already_up_to_date(
        self, mock_path, mock_get_installed, mock_get_latest
    ):
        """Test update when skill is already up-to-date."""
        mock_skill_path = MagicMock()
        mock_skill_path.exists.return_value = True
        mock_path.home.return_value.__truediv__.return_value.__truediv__.return_value.__truediv__.return_value = mock_skill_path

        mock_get_installed.return_value = "v1.0.0"
        mock_get_latest.return_value = "v1.0.0"

        runner = CliRunner()
        result = runner.invoke(cli, ["update", "skill-browser-use"])

        assert "up-to-date" in result.output

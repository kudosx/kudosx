"""Add command for Kudosx CLI - Install skills and extensions."""

import shutil
import tempfile
import zipfile
from pathlib import Path
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

import click


# Mapping of skill names to their GitHub repos and target directories
SKILLS = {
    "skill-browse-use": {
        "repo": "kudosx/claude-skill-browser-use",
        "source_path": ".claude/skills/browser-use",  # Path within repo to extract
        "target_dir": "browser-use",  # Target folder name in ~/.claude/skills/
    },
}


def download_and_extract_skill(repo: str, source_path: str, target_path: Path) -> None:
    """Download a GitHub repo and extract only the skill folder.

    Args:
        repo: GitHub repo in format "owner/repo"
        source_path: Path within the repo to the skill folder (e.g., ".claude/skills/browser-use")
        target_path: Path to extract the skill to
    """
    zip_url = f"https://github.com/{repo}/archive/refs/heads/main.zip"

    click.echo(f"Downloading from {zip_url}...")

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        zip_path = tmp_path / "repo.zip"

        # Download zip file
        try:
            with urlopen(zip_url) as response:
                with open(zip_path, "wb") as f:
                    f.write(response.read())
        except HTTPError as e:
            raise click.ClickException(f"Failed to download: HTTP {e.code} - {e.reason}")
        except URLError as e:
            raise click.ClickException(f"Failed to download: {e.reason}")

        click.echo("Extracting archive...")

        # Extract zip file
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(tmp_path)

        # Find extracted folder (usually repo-name-main)
        extracted_dirs = [d for d in tmp_path.iterdir() if d.is_dir()]
        if not extracted_dirs:
            raise click.ClickException("No directory found in extracted archive")

        extracted_dir = extracted_dirs[0]

        # Find the skill source folder within the extracted repo
        skill_source = extracted_dir / source_path
        if not skill_source.exists():
            raise click.ClickException(f"Skill folder not found at '{source_path}' in repository")

        # Create target parent directory if needed
        target_path.parent.mkdir(parents=True, exist_ok=True)

        # Remove existing target if exists
        if target_path.exists():
            shutil.rmtree(target_path)

        # Copy only the skill folder to target
        shutil.copytree(skill_source, target_path)


@click.command("add")
@click.argument("name")
@click.option(
    "--force",
    "-f",
    is_flag=True,
    help="Force reinstall even if already exists",
)
@click.option(
    "--local",
    "-l",
    is_flag=True,
    help="Install to project folder (./.claude/skills) instead of home (~/.claude/skills)",
)
def add(name: str, force: bool, local: bool):
    """Add a skill or extension to Claude Code.

    NAME is the skill/extension to install.

    Available skills:

        skill-browse-use    Browser automation skill

    Examples:

        kudosx add skill-browse-use

        kudosx add skill-browse-use --force

        kudosx add skill-browse-use --local
    """
    if name not in SKILLS:
        available = ", ".join(SKILLS.keys())
        click.secho(f"Error: Unknown skill '{name}'", fg="red")
        click.echo(f"Available skills: {available}")
        raise SystemExit(1)

    skill_config = SKILLS[name]
    repo = skill_config["repo"]
    source_path = skill_config["source_path"]
    target_dir = skill_config["target_dir"]

    # Target path: ./.claude/skills (local) or ~/.claude/skills (global)
    if local:
        skills_dir = Path.cwd() / ".claude" / "skills"
    else:
        skills_dir = Path.home() / ".claude" / "skills"
    target_path = skills_dir / target_dir

    if target_path.exists() and not force:
        click.secho(f"Skill already installed at {target_path}", fg="yellow")
        click.echo("Use --force to reinstall")
        raise SystemExit(1)

    location = "project" if local else "global"
    click.echo(f"Installing '{name}' from {repo} ({location})...")

    try:
        download_and_extract_skill(repo, source_path, target_path)
        click.secho(f"Successfully installed to {target_path}", fg="green")
    except click.ClickException:
        raise
    except Exception as e:
        click.secho(f"Error: {e}", fg="red")
        raise SystemExit(1)

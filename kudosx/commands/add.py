"""Add command for Kudosx CLI - Install skills and extensions."""

import re
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

import click
import yaml

# Path to skills registry
SKILLS_YAML = Path(__file__).parent.parent / "repo" / "skills.yaml"


def load_skills() -> dict:
    """Load skills from skills.yaml registry."""
    if not SKILLS_YAML.exists():
        return {}
    with open(SKILLS_YAML) as f:
        data = yaml.safe_load(f)
    return data.get("skills", {})


# Load skills from YAML registry
SKILLS = load_skills()


def parse_version(tag: str) -> tuple[int, ...]:
    """Parse a version tag into a tuple of integers for comparison.

    Args:
        tag: Version tag (e.g., "v0.1.0", "0.1.0", "v1.2.3-beta")

    Returns:
        Tuple of integers for comparison (e.g., (0, 1, 0))
    """
    # Remove 'v' prefix and any suffix like -beta, -rc1
    version_str = re.sub(r"^v", "", tag)
    version_str = re.sub(r"[-+].*$", "", version_str)

    # Extract numbers
    parts = re.findall(r"\d+", version_str)
    return tuple(int(p) for p in parts) if parts else (0,)


def get_latest_version(repo: str) -> str | None:
    """Get the latest version for a skill.

    First checks skills.yaml registry, then falls back to git ls-remote.

    Args:
        repo: GitHub repo in format "owner/repo"

    Returns:
        Version string (e.g., "0.1.0") or None if not found
    """
    # First, check skills.yaml for cached latest version
    for skill_config in SKILLS.values():
        if skill_config.get("repo") == repo:
            latest = skill_config.get("latest")
            if latest:
                return str(latest)
            break

    # Fallback to git ls-remote
    return fetch_latest_version_from_git(repo)


def fetch_latest_version_from_git(repo: str) -> str | None:
    """Fetch the latest version tag from GitHub using git ls-remote.

    Uses git ls-remote instead of GitHub API to avoid rate limiting.

    Args:
        repo: GitHub repo in format "owner/repo"

    Returns:
        Version string (e.g., "0.1.0") or None if not found
    """
    repo_url = f"https://github.com/{repo}.git"
    try:
        result = subprocess.run(
            ["git", "ls-remote", "--tags", repo_url],
            capture_output=True,
            text=True,
            timeout=10,
        )
        if result.returncode != 0:
            return None

        # Parse tags from output: "sha\trefs/tags/v0.1.0"
        tags = []
        for line in result.stdout.strip().split("\n"):
            if not line:
                continue
            parts = line.split("\t")
            if len(parts) == 2:
                ref = parts[1]
                # Skip ^{} dereferenced tags
                if ref.endswith("^{}"):
                    continue
                tag = ref.replace("refs/tags/", "")
                tags.append(tag)

        if not tags:
            return None

        # Sort by semantic version and return latest
        tags.sort(key=parse_version, reverse=True)
        latest = tags[0]
        # Strip 'v' prefix if present
        return latest[1:] if latest.startswith("v") else latest
    except (subprocess.TimeoutExpired, subprocess.SubprocessError, OSError):
        return None


def download_and_extract_skill(
    repo: str, source_path: str, target_path: Path, version: str | None = None
) -> None:
    """Download a GitHub repo and extract only the skill folder.

    Args:
        repo: GitHub repo in format "owner/repo"
        source_path: Path within the repo to the skill folder (e.g., ".claude/skills/browser-use")
        target_path: Path to extract the skill to
        version: Version string to save in VERSION file
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

        # Save version file if version is provided
        if version:
            version_file = target_path / "VERSION"
            version_file.write_text(version + "\n")


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

        skill-browser-use    Browser automation skill

        skill-cloud-aws      AWS cloud management skill

    Examples:

        kudosx add skill-browser-use

        kudosx add skill-browser-use --force

        kudosx add skill-browser-use --local
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

    # Fetch latest version from GitHub
    click.echo(f"Fetching latest version from {repo}...")
    version = get_latest_version(repo)
    if version:
        click.echo(f"Latest version: {version}")

    click.echo(f"Installing '{name}' from {repo} ({location})...")

    try:
        download_and_extract_skill(repo, source_path, target_path, version)
        if version:
            click.secho(f"Successfully installed {name} {version} to {target_path}", fg="green")
        else:
            click.secho(f"Successfully installed {name} to {target_path}", fg="green")
    except click.ClickException:
        raise
    except Exception as e:
        click.secho(f"Error: {e}", fg="red")
        raise SystemExit(1)

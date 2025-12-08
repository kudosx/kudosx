"""Update command for Kudosx CLI - Update installed skills."""

from pathlib import Path

import click

from kudosx.commands.add import (
    SKILLS,
    get_latest_version,
    download_and_extract_skill,
)
from kudosx.utils.version import is_update_available, format_version


def get_installed_version(skill_path: Path) -> str | None:
    """Get installed version from VERSION file."""
    version_file = skill_path / "VERSION"
    if version_file.exists():
        return version_file.read_text().strip()
    return None


def get_installed_skills(local: bool = False) -> list[dict]:
    """Get list of installed skills with their versions.

    Args:
        local: Check local directory instead of global

    Returns:
        List of dicts with skill info
    """
    if local:
        skills_dir = Path.cwd() / ".claude" / "skills"
    else:
        skills_dir = Path.home() / ".claude" / "skills"

    installed = []
    for skill_name, config in SKILLS.items():
        target_dir = config["target_dir"]
        skill_path = skills_dir / target_dir

        if skill_path.exists():
            installed_ver = get_installed_version(skill_path)
            installed.append({
                "name": skill_name,
                "config": config,
                "path": skill_path,
                "version": installed_ver,
            })

    return installed


def update_skill(
    skill_name: str,
    config: dict,
    skill_path: Path,
    installed_ver: str | None,
    force: bool = False,
) -> bool:
    """Update a single skill.

    Args:
        skill_name: Name of the skill
        config: Skill configuration dict
        skill_path: Path where skill is installed
        installed_ver: Currently installed version
        force: Force update even if up-to-date

    Returns:
        True if updated, False otherwise
    """
    repo = config["repo"]
    source_path = config["source_path"]

    # Fetch latest version
    click.echo(f"Checking {skill_name}...")
    latest_ver = get_latest_version(repo)

    if latest_ver is None:
        click.secho(f"  Could not fetch latest version from {repo}", fg="yellow")
        return False

    click.echo(f"  Installed: {format_version(installed_ver)}")
    click.echo(f"  Latest:    {format_version(latest_ver)}")

    # Check if update is needed
    if not force and not is_update_available(installed_ver, latest_ver):
        click.secho(f"  Already up-to-date", fg="green")
        return False

    # Perform update
    click.echo(f"  Updating to {latest_ver}...")
    try:
        download_and_extract_skill(repo, source_path, skill_path, latest_ver)
        click.secho(f"  Updated {skill_name} to {latest_ver}", fg="green")
        return True
    except Exception as e:
        click.secho(f"  Failed to update: {e}", fg="red")
        return False


@click.command("update")
@click.argument("name", required=False)
@click.option(
    "--all",
    "-a",
    "update_all",
    is_flag=True,
    help="Update all installed skills",
)
@click.option(
    "--local",
    "-l",
    is_flag=True,
    help="Update local skills (./.claude/skills) instead of global (~/.claude/skills)",
)
@click.option(
    "--force",
    "-f",
    is_flag=True,
    help="Force update even if already up-to-date",
)
def update(name: str | None, update_all: bool, local: bool, force: bool):
    """Update installed skills to latest version.

    Updates skills by fetching the latest release from GitHub and
    replacing the installed version.

    Examples:

        kudosx update skill-browser-use

        kudosx update --all

        kudosx update --all --local
    """
    if not name and not update_all:
        click.secho("Error: Specify a skill name or use --all", fg="red")
        click.echo("Usage: kudosx update <name> or kudosx update --all")
        raise SystemExit(1)

    location = "local" if local else "global"
    skills_dir = (
        Path.cwd() / ".claude" / "skills" if local
        else Path.home() / ".claude" / "skills"
    )

    if update_all:
        # Update all installed skills
        installed = get_installed_skills(local=local)

        if not installed:
            click.secho(f"No skills installed ({location})", fg="yellow")
            return

        click.echo(f"Checking {len(installed)} installed skill(s) ({location})...\n")

        updated_count = 0
        for skill in installed:
            if update_skill(
                skill["name"],
                skill["config"],
                skill["path"],
                skill["version"],
                force=force,
            ):
                updated_count += 1
            click.echo()

        if updated_count > 0:
            click.secho(f"Updated {updated_count} skill(s)", fg="green")
        else:
            click.secho("All skills are up-to-date", fg="green")

    else:
        # Update specific skill
        if name not in SKILLS:
            available = ", ".join(SKILLS.keys())
            click.secho(f"Error: Unknown skill '{name}'", fg="red")
            click.echo(f"Available skills: {available}")
            raise SystemExit(1)

        config = SKILLS[name]
        target_dir = config["target_dir"]
        skill_path = skills_dir / target_dir

        if not skill_path.exists():
            click.secho(f"Skill '{name}' is not installed ({location})", fg="yellow")
            click.echo(f"Use 'kudosx add {name}' to install it first")
            raise SystemExit(1)

        installed_ver = get_installed_version(skill_path)

        if not update_skill(name, config, skill_path, installed_ver, force=force):
            if not force:
                click.echo("Use --force to reinstall")

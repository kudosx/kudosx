"""Remove command for Kudosx CLI - Uninstall skills and extensions."""

import shutil
from pathlib import Path

import click

from kudosx.commands.add import SKILLS


@click.command("remove")
@click.argument("name")
@click.option(
    "--local",
    "-l",
    is_flag=True,
    help="Remove from project folder (./.claude/skills) instead of home (~/.claude/skills)",
)
def remove(name: str, local: bool):
    """Remove a skill or extension from Claude Code.

    NAME is the skill/extension to remove.

    Available skills:

        skill-browser-use    Browser automation skill

        skill-cloud-aws      AWS cloud management skill

    Examples:

        kudosx remove skill-browser-use

        kudosx remove skill-browser-use --local
    """
    if name not in SKILLS:
        available = ", ".join(SKILLS.keys())
        click.secho(f"Error: Unknown skill '{name}'", fg="red")
        click.echo(f"Available skills: {available}")
        raise SystemExit(1)

    skill_config = SKILLS[name]
    target_dir = skill_config["target_dir"]

    # Target path: ./.claude/skills (local) or ~/.claude/skills (global)
    if local:
        skills_dir = Path.cwd() / ".claude" / "skills"
    else:
        skills_dir = Path.home() / ".claude" / "skills"
    target_path = skills_dir / target_dir

    location = "project" if local else "global"

    if not target_path.exists():
        click.secho(f"Skill '{name}' is not installed ({location})", fg="yellow")
        raise SystemExit(1)

    click.echo(f"Removing '{name}' from {target_path}...")

    try:
        shutil.rmtree(target_path)
        click.secho(f"Successfully removed {name} ({location})", fg="green")
    except Exception as e:
        click.secho(f"Error: {e}", fg="red")
        raise SystemExit(1)

"""List command for Kudosx CLI - List installed commands and skills."""

from pathlib import Path

import click


def get_items(directory: Path, pattern: str = "*") -> list[dict]:
    """Get list of items in a directory.

    Args:
        directory: Path to the directory
        pattern: Glob pattern to match (default: "*")

    Returns:
        List of dicts with name and path
    """
    if not directory.exists():
        return []

    items = []
    for item in directory.glob(pattern):
        if not item.name.startswith("."):
            items.append({"name": item.name, "path": item})
    return sorted(items, key=lambda x: x["name"])


def print_section(title: str, items: list[dict], is_dir: bool = True) -> int:
    """Print a section of items.

    Args:
        title: Section title
        items: List of items to display
        is_dir: Whether items are directories (skills) or files (commands)

    Returns:
        Count of items displayed
    """
    click.secho(title, fg="cyan", bold=True)
    if items:
        for item in items:
            name = item["name"]
            if not is_dir and name.endswith(".md"):
                name = name[:-3]  # Remove .md extension for commands
            click.echo(f"  • {name}")
    else:
        click.echo("  (none)")
    return len(items)


@click.command("list")
@click.option(
    "--local",
    "-l",
    is_flag=True,
    help="List only project-local items (./.claude)",
)
@click.option(
    "--global",
    "-g",
    "global_only",
    is_flag=True,
    help="List only global items (~/.claude)",
)
@click.option(
    "--commands",
    "-c",
    is_flag=True,
    help="List only commands",
)
@click.option(
    "--skills",
    "-s",
    is_flag=True,
    help="List only skills",
)
def list_skills(local: bool, global_only: bool, commands: bool, skills: bool):
    """List installed commands and skills.

    By default, lists both global and local commands/skills.

    Examples:

        kudosx list

        kudosx list --local

        kudosx list --global

        kudosx list --commands

        kudosx list --skills
    """
    global_base = Path.home() / ".claude"
    local_base = Path.cwd() / ".claude"

    # Determine what to show
    if local:
        show_global = False
        show_local = True
    elif global_only:
        show_global = True
        show_local = False
    else:
        show_global = True
        show_local = True

    if commands:
        show_commands = True
        show_skills = False
    elif skills:
        show_commands = False
        show_skills = True
    else:
        show_commands = True
        show_skills = True

    total_commands = 0
    total_skills = 0

    # Global items
    if show_global:
        if show_commands:
            global_commands = get_items(global_base / "commands", "*.md")
            total_commands += print_section(
                "Global commands (~/.claude/commands):", global_commands, is_dir=False
            )
            click.echo()

        if show_skills:
            global_skills = [
                item for item in get_items(global_base / "skills")
                if (global_base / "skills" / item["name"]).is_dir()
            ]
            total_skills += print_section(
                "Global skills (~/.claude/skills):", global_skills, is_dir=True
            )
            click.echo()

    # Local items
    if show_local:
        if show_commands:
            local_commands = get_items(local_base / "commands", "*.md")
            total_commands += print_section(
                "Project commands (./.claude/commands):", local_commands, is_dir=False
            )
            click.echo()

        if show_skills:
            local_skills = [
                item for item in get_items(local_base / "skills")
                if (local_base / "skills" / item["name"]).is_dir()
            ]
            total_skills += print_section(
                "Project skills (./.claude/skills):", local_skills, is_dir=True
            )
            click.echo()

    # Summary
    summary_parts = []
    if show_commands:
        summary_parts.append(f"{total_commands} command(s)")
    if show_skills:
        summary_parts.append(f"{total_skills} skill(s)")
    click.echo(f"Total: {', '.join(summary_parts)}")

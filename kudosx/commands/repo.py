"""Repo command for Kudosx CLI - Repository management for maintainers."""

import click
import yaml

from kudosx.commands.add import (
    SKILLS_YAML,
    fetch_latest_version_from_git,
    load_skills_from_local,
)


@click.group("repo")
def repo():
    """Repository management commands for maintainers."""
    pass


@repo.command("sync")
def sync():
    """Sync skill versions from GitHub tags to skills.yaml.

    Fetches the latest version tag from each skill's GitHub repository
    and updates the local skills.yaml registry.

    Example:
        kudosx repo sync
    """
    click.echo("Syncing skill versions...")

    # Load current skills from local file
    skills = load_skills_from_local()
    if not skills:
        click.secho("No skills found in skills.yaml", fg="yellow")
        return

    # Track changes
    changes = []
    updated_skills = {}

    for skill_name, config in skills.items():
        repo = config.get("repo")
        if not repo:
            click.secho(f"  {skill_name}: no repo configured", fg="yellow")
            updated_skills[skill_name] = config
            continue

        current_version = config.get("latest", "")
        click.echo(f"  Fetching {skill_name}...", nl=False)

        # Fetch latest version from git tags
        new_version = fetch_latest_version_from_git(repo)

        if new_version is None:
            click.secho(" failed to fetch", fg="red")
            updated_skills[skill_name] = config
            continue

        if new_version != current_version:
            if current_version:
                click.secho(f" {current_version} → {new_version}", fg="green")
            else:
                click.secho(f" {new_version} (new)", fg="green")
            changes.append((skill_name, current_version, new_version))
        else:
            click.echo(f" {new_version} (unchanged)")

        # Update config with new version
        updated_config = dict(config)
        updated_config["latest"] = new_version
        updated_skills[skill_name] = updated_config

    # Write updated skills.yaml
    if changes:
        data = {"skills": updated_skills}
        with open(SKILLS_YAML, "w") as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
        click.secho(f"\nUpdated {SKILLS_YAML}", fg="green")
        click.echo("Don't forget to commit and push the changes!")
    else:
        click.echo("\nNo changes to sync.")

"""Init command for Kudosx CLI."""

import shutil
from pathlib import Path

import click


@click.command("init")
@click.argument("name", default="my-project")
@click.option(
    "--template",
    "-t",
    default="default",
    help="Project template to use (default: default)",
)
@click.option(
    "--dir",
    "-d",
    default=".",
    help="Directory to initialize the project in (default: current directory)",
)
@click.option(
    "--force",
    "-f",
    is_flag=True,
    help="Delete existing directory and reinitialize",
)
def init_project(name, template, dir, force):
    """Initialize a new Kudosx project.

    NAME is the project directory name (default: my-project).

    Examples:

        kudosx init

        kudosx init my-project

        kudosx init my-project --template python

        kudosx init my-project --dir samples
    """
    target_dir = Path(dir) / name

    click.echo(f"Initializing project '{name}' in '{target_dir}' with template '{template}'...")

    # Create directory if it doesn't exist
    if target_dir.exists():
        if force:
            shutil.rmtree(target_dir)
            click.secho(f"Deleted existing directory '{target_dir}'.", fg="yellow")
        else:
            click.secho(f"Error: Directory '{target_dir}' already exists. Use -f to force.", fg="red")
            raise SystemExit(1)
    target_dir.mkdir(parents=True, exist_ok=True)

    # Copy template folder
    template_dir = Path(__file__).parent.parent / "templates" / "v1"
    if not template_dir.exists():
        click.secho(f"Error: Template directory '{template_dir}' not found.", fg="red")
        raise SystemExit(1)

    shutil.copytree(template_dir, target_dir, dirs_exist_ok=True)
    click.echo(f"Copied template from {template_dir}")

    click.secho("Project initialized successfully!", fg="green")

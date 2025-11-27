"""Cloud command for Jasmine CLI."""

import subprocess
from pathlib import Path

import click


def get_content_path() -> Path:
    """Get the path to content directory."""
    return Path(__file__).parent.parent / "content"


@click.command()
@click.option(
    "--level", "-L",
    default=3,
    help="Depth of tree to display (default: 3)",
)
def cloud(level):
    """Show industry-standard cloud project structure.

    Displays the folder structure of content/industry-standard-cloud.

    Examples:

        jasmine cloud

        jasmine cloud -L 2
    """
    content_path = get_content_path()
    template_path = content_path / "industry-standard-cloud"

    if not template_path.exists():
        click.secho(f"Template not found at {template_path}", fg="red")
        raise SystemExit(1)

    try:
        result = subprocess.run(
            ["tree", "-L", str(level), str(template_path)],
            capture_output=True,
            text=True,
            check=True,
        )
        click.echo(result.stdout)
    except FileNotFoundError:
        click.secho("'tree' command not found. Please install tree.", fg="red")
        raise SystemExit(1)
    except subprocess.CalledProcessError as e:
        click.secho(f"Error running tree: {e.stderr}", fg="red")
        raise SystemExit(1)

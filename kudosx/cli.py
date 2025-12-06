"""Main CLI entry point for Kudosx."""

import click

from kudosx import __version__
from kudosx.commands.add import add
from kudosx.commands.cloud import cloud
from kudosx.commands.init import init_project
from kudosx.commands.list import list_skills
from kudosx.commands.search import search
from kudosx.commands.software import software


@click.group()
@click.version_option(version=__version__, prog_name="kudosx")
def cli():
    """Kudosx - An Agentic Coding CLI tool."""
    pass


cli.add_command(add)
cli.add_command(cloud)
cli.add_command(init_project)
cli.add_command(list_skills)
cli.add_command(search)
cli.add_command(software)


def main():
    """Entry point for the CLI."""
    cli()


if __name__ == "__main__":
    main()

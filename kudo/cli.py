"""Main CLI entry point for Kudo."""

import click

from kudo import __version__
from kudo.commands.cloud import cloud
from kudo.commands.search import search
from kudo.commands.software import software


@click.group()
@click.version_option(version=__version__, prog_name="kudo")
def cli():
    """Kudo - An Agentic Coding CLI tool."""
    pass


cli.add_command(cloud)
cli.add_command(search)
cli.add_command(software)


def main():
    """Entry point for the CLI."""
    cli()


if __name__ == "__main__":
    main()

"""Main CLI entry point for Jasmine."""

import click

from jasmine import __version__
from jasmine.commands.cloud import cloud
from jasmine.commands.search import search


@click.group()
@click.version_option(version=__version__, prog_name="jasmine")
def cli():
    """Jasmine - An Agentic Coding CLI tool."""
    pass


cli.add_command(cloud)
cli.add_command(search)


def main():
    """Entry point for the CLI."""
    cli()


if __name__ == "__main__":
    main()

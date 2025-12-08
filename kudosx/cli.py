"""Main CLI entry point for Kudosx."""

import click

from kudosx import __version__
from kudosx.commands.add import add
from kudosx.commands.cloud import cloud
from kudosx.commands.explore import explore
from kudosx.commands.init import init_project
from kudosx.commands.list import list_skills
from kudosx.commands.remove import remove
from kudosx.commands.search import search
from kudosx.commands.software import software
from kudosx.commands.update import update


@click.group(invoke_without_command=True)
@click.version_option(version=__version__, prog_name="kudosx")
@click.pass_context
def cli(ctx):
    """Kudosx - An AI software team that builds products with industry standard practices."""
    if ctx.invoked_subcommand is None:
        # Default to explore when no subcommand is given
        ctx.invoke(explore)


cli.add_command(add)
cli.add_command(cloud)
cli.add_command(explore)
cli.add_command(init_project)
cli.add_command(list_skills)
cli.add_command(remove)
cli.add_command(search)
cli.add_command(software)
cli.add_command(update)


def main():
    """Entry point for the CLI."""
    cli()


if __name__ == "__main__":
    main()

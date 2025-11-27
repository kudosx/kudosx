"""Search command for Jasmine CLI."""

import os
import re
from pathlib import Path

import click


@click.command()
@click.argument("query")
@click.option(
    "-p", "--path",
    default=".",
    help="Directory to search in (default: current directory)",
    type=click.Path(exists=True),
)
@click.option(
    "-t", "--type",
    "search_type",
    type=click.Choice(["file", "content", "all"]),
    default="all",
    help="Search type: file (filename), content (file content), or all",
)
@click.option(
    "-e", "--extension",
    multiple=True,
    help="Filter by file extension (e.g., -e py -e js)",
)
@click.option(
    "-i", "--ignore-case",
    is_flag=True,
    default=False,
    help="Case insensitive search",
)
@click.option(
    "-m", "--max-results",
    default=50,
    help="Maximum number of results to show (default: 50)",
)
@click.option(
    "--hidden",
    is_flag=True,
    default=False,
    help="Include hidden files and directories",
)
def search(query, path, search_type, extension, ignore_case, max_results, hidden):
    """Search for files or content in the codebase.

    QUERY is the search term (supports regex patterns).

    Examples:

        jasmine search "def main"

        jasmine search "TODO" -t content -e py

        jasmine search "test_*.py" -t file
    """
    search_path = Path(path).resolve()
    results = []
    flags = re.IGNORECASE if ignore_case else 0

    try:
        pattern = re.compile(query, flags)
    except re.error as e:
        click.secho(f"Invalid regex pattern: {e}", fg="red", err=True)
        raise SystemExit(1)

    extensions = set(ext.lstrip(".") for ext in extension) if extension else None

    click.echo(f"Searching for '{query}' in {search_path}...")
    click.echo()

    for root, dirs, files in os.walk(search_path):
        if not hidden:
            dirs[:] = [d for d in dirs if not d.startswith(".")]
            files = [f for f in files if not f.startswith(".")]

        for filename in files:
            if len(results) >= max_results:
                break

            file_path = Path(root) / filename
            rel_path = file_path.relative_to(search_path)

            if extensions and file_path.suffix.lstrip(".") not in extensions:
                continue

            if search_type in ("file", "all"):
                if pattern.search(filename):
                    results.append({
                        "type": "file",
                        "path": str(rel_path),
                        "match": filename,
                    })
                    if len(results) >= max_results:
                        break

            if search_type in ("content", "all"):
                try:
                    content = file_path.read_text(encoding="utf-8", errors="ignore")
                    for line_num, line in enumerate(content.splitlines(), 1):
                        if pattern.search(line):
                            results.append({
                                "type": "content",
                                "path": str(rel_path),
                                "line": line_num,
                                "match": line.strip()[:100],
                            })
                            if len(results) >= max_results:
                                break
                except (OSError, IOError):
                    continue

        if len(results) >= max_results:
            break

    _display_results(results, max_results)


def _display_results(results, max_results):
    """Display search results."""
    if not results:
        click.secho("No results found.", fg="yellow")
        return

    file_results = [r for r in results if r["type"] == "file"]
    content_results = [r for r in results if r["type"] == "content"]

    if file_results:
        click.secho("Files:", fg="green", bold=True)
        for r in file_results:
            click.echo(f"  {r['path']}")
        click.echo()

    if content_results:
        click.secho("Content matches:", fg="blue", bold=True)
        for r in content_results:
            click.echo(f"  {r['path']}:{r['line']}: {r['match']}")
        click.echo()

    total = len(results)
    click.echo(f"Found {total} result(s)", nl=False)
    if total >= max_results:
        click.secho(f" (limited to {max_results})", fg="yellow")
    else:
        click.echo()

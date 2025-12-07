# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Kudosx is an AI software team that builds products with industry standard practices. This repository is in early development.

## Custom Commands

- `/commit-code` - Commits all staged and unstaged changes with a properly formatted message and pushes to remote. Uses conventional commit style (Fix, Add, Update, Remove, Refactor, Docs, Test, Chore) without Claude Code footers.
- `/commit-code <version>` - Creates a release with the specified version (e.g., `/commit-code 0.3.0`).

## Version Management

When releasing a new version, update these files:
- `pyproject.toml` - `version = "X.X.X"`
- `kudosx/__init__.py` - `__version__ = "X.X.X"`
- `VERSION` - `X.X.X`
- `CHANGELOG.md` - Add new version section
- `uv.lock` - Run `uv lock` to update lockfile

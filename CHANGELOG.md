# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 0.3.2 - 2025-12-08

### Added

- Remote skills.yaml fetching from GitHub (with local fallback)
- `kudosx repo sync` command for maintainers to sync versions from GitHub tags
- In-memory cache for skills registry to avoid repeated fetches

### Changed

- Version fetching now uses `git ls-remote --tags` instead of GitHub API (no rate limiting)
- Skills registry loaded from remote URL first, falls back to local bundled file

## 0.3.1 - 2025-12-08

### Fixed

- Correct model pricing using LiteLLM rates (opus-4-5: $5/$25, haiku-4-5: $1/$5)
- Deduplication of usage entries using message.id + requestId hash
- Local timezone conversion for accurate date grouping

### Changed

- Per-model cost calculation for accurate usage costs
- Display all models in usage view (multi-line bullet list)
- Skip synthetic models in usage tracking

## 0.3.0 - 2025-12-07

### Added

- `explore` command - k9s-style TUI for browsing skills, agents, commands, and usage
- Usage view with Daily/Weekly/Monthly period tabs (`d`/`w`/`m`)
- Token usage tracking from local Claude Code session files
- Cost calculation with model-specific pricing
- Current date/week/month highlighting in usage table
- Spec documentation for all TUI views

## 0.2.5 - 2025-12-06

### Fixed

- Sync `__version__` in `kudosx/__init__.py` with `pyproject.toml`

### Changed

- Add version management documentation to CLAUDE.md

## 0.2.4 - 2025-12-06

### Added

- `remove` command - Uninstall skills from Claude Code (supports `--local` flag)
- `skill-cloud-aws` - AWS cloud management skill
- `skill-adder` agent for adding new skills to the project

## 0.2.3 - 2025-12-06

### Changed

- Update project description to "An AI software team that builds products with industry standard practices."

## 0.2.2 - 2025-12-06

### Added

- Version display for skills in `list` command - shows version from GitHub releases
- Version fetching from GitHub releases API in `add` command
- VERSION file saved to installed skills for tracking installed version
- Release workflow option in `/commit-code` command

## 0.2.1 - 2025-12-06

### Fixed

- Fix typo in skill name: `skill-browse-use` → `skill-browser-use`

## 0.2.0 - 2025-12-06

### Added

- `add` command - Install skills and extensions to Claude Code from GitHub repositories
- `list` command - List installed commands and skills (global and project-local)
- `assets/` directory for project media files

### Changed

- Moved video files from root to `assets/` folder for better project organization

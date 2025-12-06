# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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

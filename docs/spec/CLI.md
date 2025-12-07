# CLI

## Overview

Kudosx CLI is the command-line interface for managing skills, commands, and exploring the Kudosx ecosystem.

## Installation

```bash
pip install kudosx
# or
uv add kudosx
```

## Default Behavior

When running `kudosx` without any subcommand, it launches the TUI explorer (`kudosx explore`).

```bash
kudosx  # Same as kudosx explore
```

## Commands

| Command | Description |
|---------|-------------|
| `kudosx add` | Install a skill to Claude Code |
| `kudosx remove` | Uninstall a skill from Claude Code |
| `kudosx list` | List installed commands and skills |
| `kudosx search` | Search for files or content in codebase |
| `kudosx init` | Initialize a new Kudosx project |
| `kudosx explore` | TUI for browsing agents, skills, commands, and usage |
| `kudosx software` | Show industry-standard software project structure |
| `kudosx cloud` | Show industry-standard cloud project structure |

## Command Reference

### kudosx add

Install a skill or extension to Claude Code.

```bash
kudosx add <name> [--force] [--local]
```

**Arguments:**
- `name` - Skill name to install

**Options:**
- `-f, --force` - Force reinstall even if already exists
- `-l, --local` - Install to project folder (./.claude/skills) instead of global (~/.claude/skills)

**Available Skills:**
- `skill-browser-use` - Browser automation skill
- `skill-cloud-aws` - AWS cloud management skill

**Examples:**
```bash
kudosx add skill-browser-use
kudosx add skill-browser-use --force
kudosx add skill-browser-use --local
```

### kudosx remove

Remove a skill or extension from Claude Code.

```bash
kudosx remove <name> [--local]
```

**Arguments:**
- `name` - Skill name to remove

**Options:**
- `-l, --local` - Remove from project folder (./.claude/skills) instead of global (~/.claude/skills)

**Examples:**
```bash
kudosx remove skill-browser-use
kudosx remove skill-browser-use --local
```

### kudosx list

List installed commands and skills.

```bash
kudosx list [--local] [--global] [--commands] [--skills]
```

**Options:**
- `-l, --local` - List only project-local items (./.claude)
- `-g, --global` - List only global items (~/.claude)
- `-c, --commands` - List only commands
- `-s, --skills` - List only skills

**Examples:**
```bash
kudosx list
kudosx list --local
kudosx list --global
kudosx list --commands
kudosx list --skills
```

### kudosx search

Search for files or content in the codebase.

```bash
kudosx search <query> [options]
```

**Arguments:**
- `query` - Search term (supports regex patterns)

**Options:**
- `-p, --path` - Directory to search in (default: current directory)
- `-t, --type` - Search type: `file`, `content`, or `all` (default: all)
- `-e, --extension` - Filter by file extension (can be used multiple times)
- `-i, --ignore-case` - Case insensitive search
- `-m, --max-results` - Maximum number of results (default: 50)
- `--hidden` - Include hidden files and directories

**Examples:**
```bash
kudosx search "def main"
kudosx search "TODO" -t content -e py
kudosx search "test_*.py" -t file
```

### kudosx init

Initialize a new Kudosx project.

```bash
kudosx init [name] [--template] [--dir] [--force]
```

**Arguments:**
- `name` - Project directory name (default: my-project)

**Options:**
- `-t, --template` - Project template to use (default: default)
- `-d, --dir` - Directory to initialize the project in (default: current directory)
- `-f, --force` - Delete existing directory and reinitialize

**Examples:**
```bash
kudosx init
kudosx init my-project
kudosx init my-project --template python
kudosx init my-project --dir samples
```

### kudosx explore

Launch the TUI (Text User Interface) for exploring Kudosx.

```bash
kudosx explore
```

**Tabs:**
- `a` - Agents view
- `k` - Skills view
- `c` - Commands view
- `u` - Usage view

See separate specs for each view:
- [VIEW_AGENTS.md](VIEW_AGENTS.md)
- [VIEW_SKILLS.md](VIEW_SKILLS.md)
- [VIEW_COMMANDS.md](VIEW_COMMANDS.md)
- [VIEW_USAGE.md](VIEW_USAGE.md)

### kudosx software

Show industry-standard software project structure.

```bash
kudosx software [--level]
```

**Options:**
- `-L, --level` - Depth of tree to display (default: 3)

**Examples:**
```bash
kudosx software
kudosx software -L 2
```

### kudosx cloud

Show industry-standard cloud project structure.

```bash
kudosx cloud [--level]
```

**Options:**
- `-L, --level` - Depth of tree to display (default: 3)

**Examples:**
```bash
kudosx cloud
kudosx cloud -L 2
```

## Global Options

```bash
kudosx --version  # Show version
kudosx --help     # Show help
```

## Implementation

- Entry point: `kudosx/cli.py`
- Commands directory: `kudosx/commands/`
- Uses Click framework for CLI parsing

## Status

- [x] add command
- [x] remove command
- [x] list command
- [x] search command
- [x] init command
- [x] explore command (TUI)
- [x] software command
- [x] cloud command

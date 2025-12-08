# Version Management

## Overview

Version management for Skills, Commands, and Agents trong Kudosx ecosystem. Cho phép quản lý packages, cập nhật từ remote repos, và hiển thị version info.

## Features

### 1. Package Version Tracking

- **VERSION file**: Mỗi skill có file `VERSION` chứa version string (e.g., `v0.1.0`)
- **Local storage**:
  - Global: `~/.claude/skills/<skill>/VERSION`
  - Local: `./.claude/skills/<skill>/VERSION`

### 2. Remote Version Fetching

- Fetch latest release từ GitHub API: `GET /repos/{owner}/{repo}/releases/latest`
- Response: `tag_name` field chứa version (e.g., `v0.1.0`)
- Timeout: 10 seconds
- Error handling: Return `None` if fetch fails

### 3. Version Comparison

| Scenario | Status | Action Available |
|----------|--------|------------------|
| Not installed | `available` | Install |
| Installed == Latest | `installed` | Reinstall (--force) |
| Installed < Latest | `update` | Update |
| Latest unknown | `installed` | Reinstall (--force) |

### 4. Update Command

```bash
kudosx update [name] [--all] [--local]
```

**Arguments:**
- `name` - Skill name to update (optional if --all)

**Options:**
- `-a, --all` - Update all installed skills
- `-l, --local` - Update local skills (./.claude/skills) instead of global

**Examples:**
```bash
kudosx update skill-browser-use      # Update specific skill
kudosx update --all                   # Update all global skills
kudosx update --all --local           # Update all local skills
```

## Implementation

### Files

| File | Purpose |
|------|---------|
| `kudosx/commands/add.py` | `get_latest_version()` function |
| `kudosx/commands/update.py` | Update command implementation |
| `kudosx/commands/explore.py` | TUI version display |
| `kudosx/utils/version.py` | Version comparison utilities |

### Data Flow

```
1. User runs: kudosx update <skill-name>
2. Check if skill is installed (global or local)
3. Fetch latest version from GitHub API
4. Compare versions
5. If update available:
   a. Download latest release
   b. Extract and replace skill folder
   c. Update VERSION file
6. Display result
```

### Version Format

- Semantic versioning: `vX.Y.Z` or `X.Y.Z`
- VERSION file contains single line with version string
- Trailing newline is stripped when reading

### API Integration

```python
def get_latest_version(repo: str) -> str | None:
    """Fetch latest version from GitHub releases."""
    api_url = f"https://api.github.com/repos/{repo}/releases/latest"
    # Returns tag_name or None
```

## TUI Integration

### Skills View Columns

| Column | Description |
|--------|-------------|
| NAME | Skill name |
| STATUS | installed/available/update |
| GLOBAL | Version in ~/.claude/skills |
| LOCAL | Version in ./.claude/skills |
| LATEST | Latest version from GitHub |

### Keyboard Shortcuts

- `Enter` - Install/Update selected skill
- `r` - Refresh (re-fetch latest versions)

## CLI Commands

| Command | Description |
|---------|-------------|
| `kudosx add <name>` | Install skill (saves version) |
| `kudosx update <name>` | Update skill to latest |
| `kudosx update --all` | Update all installed skills |
| `kudosx list --skills` | List skills with versions |

## Related Specs

- [VIEW_SKILLS.md](VIEW_SKILLS.md) - Skills TUI view
- [CLI.md](CLI.md) - CLI command reference

## Status

- [x] VERSION file storage
- [x] GitHub API version fetching
- [x] TUI version display (GLOBAL, LOCAL, LATEST columns)
- [x] Status detection (installed/available/update)
- [x] Install with version tracking
- [x] Update command
- [x] Update all functionality
- [x] Version comparison utilities

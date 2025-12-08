# Version Management

## Overview

Version management for Skills, Commands, and Agents trong Kudosx ecosystem. Cho phép quản lý packages, cập nhật từ remote repos, và hiển thị version info.

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        Remote (GitHub)                          │
│  https://raw.githubusercontent.com/kudosx/kudosx/main/          │
│                kudosx/repo/skills.yaml                          │
│                                                                 │
│  skills:                                                        │
│    skill-browser-use:                                           │
│      repo: kudosx/claude-skill-browser-use                      │
│      latest: 0.1.1                                              │
│      ...                                                        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ fetch (HTTP GET)
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      User Machine                               │
│                                                                 │
│  kudosx add/update/explore                                      │
│       │                                                         │
│       ▼                                                         │
│  load_skills_from_remote() ──► Parse YAML ──► Get latest ver    │
│       │                                                         │
│       │ fallback (if remote fails)                              │
│       ▼                                                         │
│  kudosx/repo/skills.yaml (local bundled)                        │
└─────────────────────────────────────────────────────────────────┘
```

## Features

### 1. Remote Skills Registry

- **Primary source**: `https://raw.githubusercontent.com/kudosx/kudosx/main/kudosx/repo/skills.yaml`
- **Fallback**: Local bundled `kudosx/repo/skills.yaml`
- **Cache**: In-memory during session
- **Timeout**: 5 seconds for remote fetch

### 2. Skills Registry Format (skills.yaml)

```yaml
skills:
  skill-browser-use:
    repo: kudosx/claude-skill-browser-use
    source_path: .claude/skills/browser-use
    target_dir: browser-use
    latest: 0.1.1
    description: Browser automation skill

  skill-cloud-aws:
    repo: kudosx/claude-skill-cloud-aws
    source_path: .claude/skills/cloud-aws
    target_dir: cloud-aws
    latest: 0.0.3
    description: AWS cloud management skill
```

### 3. Package Version Tracking

- **VERSION file**: Mỗi skill có file `VERSION` chứa version string (e.g., `0.1.0`)
- **Local storage**:
  - Global: `~/.claude/skills/<skill>/VERSION`
  - Local: `./.claude/skills/<skill>/VERSION`

### 4. Version Comparison

| Scenario | Status | Action Available |
|----------|--------|------------------|
| Not installed | `available` | Install |
| Installed == Latest | `installed` | Reinstall (--force) |
| Installed < Latest | `update` | Update |
| Latest unknown | `installed` | Reinstall (--force) |

### 5. Owner Command: Sync Versions

Cho phép repo owner sync latest versions từ GitHub tags vào skills.yaml:

```bash
kudosx repo sync
```

**Actions:**
1. Fetch latest tag từ mỗi skill repo via `git ls-remote --tags`
2. Update `latest` field trong `kudosx/repo/skills.yaml`
3. Display changes

**Example output:**
```
Syncing skill versions...
  skill-browser-use: 0.1.0 → 0.1.1
  skill-cloud-aws: 0.0.3 (unchanged)
Updated kudosx/repo/skills.yaml
```

### 6. Update Command

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
| `kudosx/repo/skills.yaml` | Skills registry (bundled with package) |
| `kudosx/commands/add.py` | `load_skills()`, `get_latest_version()` |
| `kudosx/commands/update.py` | Update command implementation |
| `kudosx/commands/repo.py` | Owner commands (sync) |
| `kudosx/commands/explore.py` | TUI version display |
| `kudosx/utils/version.py` | Version comparison utilities |

### Data Flow: User Fetching Versions

```
1. User runs: kudosx add/update/explore
2. load_skills() called:
   a. Try fetch from remote URL (5s timeout)
   b. If success: parse YAML, return skills dict
   c. If fail: load from local bundled skills.yaml
3. get_latest_version(repo):
   a. Look up `latest` field from loaded skills
   b. Return version string
4. Proceed with install/update/display
```

### Data Flow: Owner Syncing Versions

```
1. Owner runs: kudosx repo sync
2. For each skill in skills.yaml:
   a. Run: git ls-remote --tags <repo-url>
   b. Parse tags, sort by semver
   c. Get latest tag (strip 'v' prefix)
3. Update skills.yaml with new versions
4. Owner commits and pushes changes
5. Users get new versions on next fetch
```

### Remote URL

```
REMOTE_SKILLS_URL = "https://raw.githubusercontent.com/kudosx/kudosx/refs/heads/main/kudosx/repo/skills.yaml"
```

### Version Format

- Semantic versioning: `X.Y.Z` (no 'v' prefix in registry)
- VERSION file contains single line with version string
- Trailing newline is stripped when reading

## TUI Integration

### Skills View Columns

| Column | Description |
|--------|-------------|
| NAME | Skill name |
| STATUS | installed/available/update |
| GLOBAL | Version in ~/.claude/skills |
| LOCAL | Version in ./.claude/skills |
| LATEST | Latest version from remote registry |

### Keyboard Shortcuts

- `Enter` - Install/Update selected skill
- `r` - Refresh (re-fetch from remote)

## CLI Commands

| Command | Description |
|---------|-------------|
| `kudosx add <name>` | Install skill (saves version) |
| `kudosx update <name>` | Update skill to latest |
| `kudosx update --all` | Update all installed skills |
| `kudosx repo sync` | Sync versions from GitHub tags (owner) |

## Related Specs

- [VIEW_SKILLS.md](VIEW_SKILLS.md) - Skills TUI view
- [CLI.md](CLI.md) - CLI command reference

## Status

- [x] VERSION file storage
- [x] Local skills.yaml registry
- [x] TUI version display (GLOBAL, LOCAL, LATEST columns)
- [x] Status detection (installed/available/update)
- [x] Install with version tracking
- [x] Update command
- [x] Update all functionality
- [x] Version comparison utilities
- [x] Remote skills.yaml fetching
- [x] Owner sync command

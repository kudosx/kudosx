# DEP04-BP01: Semantic Versioning

Đánh version theo Semantic Versioning (SemVer).

## Format

```
MAJOR.MINOR.PATCH

v1.2.3
│ │ │
│ │ └── Patch: Bug fixes (backwards compatible)
│ └──── Minor: New features (backwards compatible)
└────── Major: Breaking changes
```

## When to Bump

| Change Type | Example | Bump |
|-------------|---------|------|
| Breaking API change | Remove endpoint, change response format | MAJOR |
| New feature | Add new endpoint, new option | MINOR |
| Bug fix | Fix calculation error | PATCH |
| Performance improvement | Optimize query | PATCH |
| Documentation | Update README | No bump |

## Examples

```
1.0.0 → 1.0.1  # Bug fix
1.0.1 → 1.1.0  # New feature added
1.1.0 → 2.0.0  # Breaking change
```

## Pre-release Versions

```
1.0.0-alpha.1    # Alpha release
1.0.0-beta.1     # Beta release
1.0.0-rc.1       # Release candidate
```

## Changelog

```markdown
# Changelog

## [2.1.0] - 2024-01-15
### Added
- New user profile API endpoint
- Support for dark mode

### Changed
- Improved performance of search

### Fixed
- Fixed login timeout issue

## [2.0.0] - 2024-01-01
### Breaking Changes
- Changed authentication from API key to JWT
- Removed deprecated /v1/users endpoint

### Added
- New authentication system
```

## Automated Versioning

```yaml
# Using semantic-release
# .releaserc.json
{
  "branches": ["main"],
  "plugins": [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    "@semantic-release/changelog",
    "@semantic-release/npm",
    "@semantic-release/github"
  ]
}
```

Commit messages trigger version bumps:
```
fix: handle null pointer → PATCH (1.0.0 → 1.0.1)
feat: add user search   → MINOR (1.0.1 → 1.1.0)
feat!: change API       → MAJOR (1.1.0 → 2.0.0)
```

## Git Tags

```bash
# Create tag
git tag -a v1.2.3 -m "Release version 1.2.3"

# Push tag
git push origin v1.2.3

# List tags
git tag -l "v1.*"
```

## Checklist

- [ ] Follow SemVer strictly
- [ ] Document breaking changes
- [ ] Maintain CHANGELOG
- [ ] Tag releases in git
- [ ] Use automated versioning

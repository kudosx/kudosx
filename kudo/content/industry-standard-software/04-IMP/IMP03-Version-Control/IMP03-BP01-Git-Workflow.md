# IMP03-BP01: Git Workflow

Branching strategies phổ biến và cách áp dụng.

## Git Flow

```
main        ─────●─────────────────●─────────────────●────
                 │                 │                 │
release     ─────┼─────────●───────┤                 │
                 │         │       │                 │
develop     ─────●─────●───┼───────●─────●───────────●────
                 │     │   │             │
feature          └──●──┘   │             └──●──●──●──┘
                           │
hotfix                     └──●──┘
```

### Branches

| Branch | Purpose | From | Merge to |
|--------|---------|------|----------|
| `main` | Production code | - | - |
| `develop` | Development | main | main |
| `feature/*` | New features | develop | develop |
| `release/*` | Release prep | develop | main, develop |
| `hotfix/*` | Production fixes | main | main, develop |

## Trunk-Based Development

```
main      ─────●─────●─────●─────●─────●─────●─────●────
               │     │     │     │     │     │     │
feature        └──●──┘     └──●──┘     └──●──┘     └──●──┘
               (short-lived feature branches)
```

**Best for**: CI/CD, small teams, frequent releases

## GitHub Flow

```
main      ─────●─────────────────●─────────────────●────
               │                 │                 │
feature        └──●──●──●──PR────┘                 │
                                                   │
feature                          └──●──●──PR───────┘
```

**Process**:
1. Create branch from `main`
2. Make commits
3. Open Pull Request
4. Review & discuss
5. Merge to `main`
6. Deploy

## Branch Naming

```bash
# Format: type/ticket-description
feature/JIRA-123-user-authentication
bugfix/JIRA-456-fix-login-error
hotfix/JIRA-789-security-patch
refactor/JIRA-101-cleanup-user-service

# Short version
feat/add-login
fix/null-pointer
```

## Common Commands

```bash
# Start new feature
git checkout develop
git pull origin develop
git checkout -b feature/JIRA-123-new-feature

# Keep feature branch updated
git fetch origin
git rebase origin/develop

# Finish feature
git checkout develop
git merge --no-ff feature/JIRA-123-new-feature
git push origin develop
git branch -d feature/JIRA-123-new-feature
```

## Merge Strategies

| Strategy | Command | Use When |
|----------|---------|----------|
| Merge commit | `git merge` | Preserve history |
| Squash | `git merge --squash` | Clean history |
| Rebase | `git rebase` | Linear history |

## Checklist

- [ ] Branch naming convention nhất quán
- [ ] Feature branches short-lived (< 1 week)
- [ ] Regular sync với base branch
- [ ] PR trước khi merge
- [ ] Delete merged branches

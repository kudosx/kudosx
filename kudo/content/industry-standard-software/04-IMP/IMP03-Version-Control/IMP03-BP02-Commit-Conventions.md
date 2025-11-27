# IMP03-BP02: Commit Conventions

Quy ước viết commit message theo Conventional Commits.

## Format

```
<type>(<scope>): <subject>

[optional body]

[optional footer]
```

## Types

| Type | Mô tả | Example |
|------|-------|---------|
| `feat` | New feature | `feat(auth): add login with Google` |
| `fix` | Bug fix | `fix(api): handle null response` |
| `docs` | Documentation | `docs(readme): update installation guide` |
| `style` | Formatting | `style: fix indentation` |
| `refactor` | Code change (no fix/feature) | `refactor(user): simplify validation` |
| `test` | Add/update tests | `test(api): add user endpoint tests` |
| `chore` | Maintenance | `chore: update dependencies` |
| `perf` | Performance | `perf(query): optimize user lookup` |
| `ci` | CI/CD changes | `ci: add GitHub Actions workflow` |

## Scope

Optional, indicates affected area:
- `auth`, `api`, `ui`, `db`, `config`

```
feat(auth): add JWT refresh token
fix(api): handle timeout error
docs(readme): add deployment guide
```

## Subject

- Viết imperative mood: "add" không phải "added"
- Không viết hoa chữ đầu
- Không có dấu chấm cuối
- Max 50 characters

```
✅ feat: add user authentication
✅ fix: handle null pointer exception

❌ feat: Added user authentication
❌ fix: Handle null pointer exception.
```

## Body

Optional, giải thích "what" và "why":

```
feat(auth): add two-factor authentication

Implement TOTP-based 2FA using Google Authenticator.
This provides an additional security layer for user accounts.

- Add QR code generation for setup
- Store encrypted TOTP secrets
- Validate 6-digit codes on login
```

## Footer

For breaking changes and issue references:

```
feat(api)!: change response format

BREAKING CHANGE: API response now wraps data in { data: ... }
instead of returning raw objects.

Closes #123
Refs #456
```

## Breaking Changes

Use `!` after type/scope:

```
feat(api)!: remove deprecated endpoints
fix(auth)!: change token expiry to 1 hour
```

## Examples

```bash
# Simple feature
git commit -m "feat(cart): add quantity selector"

# Bug fix with scope
git commit -m "fix(checkout): calculate correct tax"

# With body
git commit -m "refactor(user): extract validation logic

Move validation from controller to service layer.
This improves testability and reusability."

# Breaking change
git commit -m "feat(api)!: change authentication header

BREAKING CHANGE: Use 'Authorization: Bearer <token>'
instead of 'X-Auth-Token: <token>'"
```

## Tools

| Tool | Purpose |
|------|---------|
| **commitlint** | Lint commit messages |
| **husky** | Git hooks |
| **commitizen** | Interactive commit |
| **semantic-release** | Auto versioning |

## Checklist

- [ ] Type phù hợp với thay đổi
- [ ] Subject imperative mood
- [ ] Subject ≤ 50 characters
- [ ] Body explains why (if needed)
- [ ] Breaking changes documented
- [ ] Issue references included

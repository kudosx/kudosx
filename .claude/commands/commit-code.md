# Commit Code Command

Commit all staged and unstaged changes to git and push to the remote repository.

## Arguments

- `$ARGUMENTS` - Optional: If set to a version like `0.3.0`, triggers a release workflow

## Standard Commit Instructions

1. Run `git status` to see all modified, deleted, and untracked files
2. Run `git diff --stat` to understand the scope of changes
3. Run `git log --oneline -3` to see recent commit message style
4. Analyze the changes and draft a concise commit message that:
   - Starts with a verb (Fix, Add, Update, Remove, Refactor, etc.)
   - Summarizes the main change in the first line (50 chars max)
   - Includes bullet points for multiple changes in the body
   - Does NOT include "Generated with Claude Code" or "Co-Authored-By" footers
5. Stage all changes with `git add -A`
6. Commit with the drafted message using a HEREDOC format
7. Push to remote (use `--set-upstream origin <branch>` if needed)
8. Report the commit hash and confirmation of push

## Release Instructions (when $ARGUMENTS is a version like `0.3.0`)

If `$ARGUMENTS` contains a version number (e.g., `0.3.0`), perform a release:

1. **Update version in pyproject.toml**:
   - Change `version = "X.X.X"` to the new version

2. **Update CHANGELOG.md**:
   - Add a new section at the top (after the header) with format:
   ```
   ## X.X.X - YYYY-MM-DD

   ### Added
   - New features...

   ### Changed
   - Changes...

   ### Fixed
   - Bug fixes...
   ```
   - Summarize changes since the last version by checking git log
   - Use appropriate sections (Added, Changed, Fixed, Removed, etc.)

3. **Commit the release**:
   - Stage all changes with `git add -A`
   - Commit with message: `Release: vX.X.X`

4. **Create and push git tag**:
   - Create tag: `git tag vX.X.X`
   - Push commits: `git push`
   - Push tag: `git push origin vX.X.X`

5. **Create GitHub release**:
   - Use `gh release create vX.X.X --title "vX.X.X" --notes "See CHANGELOG.md for details"`

6. Report the release URL when complete

## Commit Message Format

```
<type>: <short summary>

- Detail 1
- Detail 2
```

Types: Fix, Add, Update, Remove, Refactor, Docs, Test, Chore
# Claude Code Tips and Tricks
 
## Flag `--dangerously-skip-permissions`

The `--dangerously-skip-permissions` flag enables "YOLO mode" in Claude Code, bypassing all permission prompts and allowing Claude to work uninterrupted until task completion. This is useful for fixing lint errors across projects, multi-file refactors, and generating boilerplate code. However, it carries risks including unintended file deletion, scope creep, and configuration overwrites.

For safety, always run in a Docker container or VM, provide explicit task scoping, and avoid directories containing secrets or production configs. A safer alternative is using `allowedTools` in `~/.claude/settings.json` to pre-approve specific commands like `Bash(git:*)` without disabling all safety checks.

### References

- [Claude Code dangerously-skip-permissions: Safe Usage Guide](https://www.ksred.com/claude-code-dangerously-skip-permissions-when-to-use-it-and-when-you-absolutely-shouldnt/)
- [Dangerous Skip Permissions | ClaudeLog](https://claudelog.com/mechanics/dangerous-skip-permissions/)
- [Claude Code: Best practices for agentic coding](https://www.anthropic.com/engineering/claude-code-best-practices)

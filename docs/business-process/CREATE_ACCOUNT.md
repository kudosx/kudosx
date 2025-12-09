# Create Account

## Steps

### 1. Create Routing Email in Cloudflare

1. **Open Cloudflare Dashboard**
   ```bash
   cd ~/.claude/skills/browser-use/scripts
   uv run browser.py open https://dash.cloudflare.com --account cloudflare --wait 180
   ```

2. **Navigate to Email Routing**
   - Select your domain
   - Go to **Email** > **Email Routing**
   - Click **Create address**

3. **Create a routing email**
   - Enter custom address (e.g., `newaccount@yourdomain.com`)
   - Set destination email (your main email)
   - Click **Save**

### Browser Skill Reference

```bash
# List saved accounts
cd ~/.claude/skills/browser-use/scripts
uv run browser.py accounts

# Create login session (first time)
uv run browser.py create-login https://dash.cloudflare.com --account cloudflare --wait 120
```

### Notes
- Sessions are stored in `~/.auth/` directory
- Use `--wait` to specify timeout in seconds (default: 120)


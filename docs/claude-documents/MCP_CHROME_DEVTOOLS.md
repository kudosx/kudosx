# Chrome DevTools MCP

Chrome DevTools MCP is a Model Context Protocol server that gives AI coding assistants the ability to control and inspect a live Chrome browser. Released in public preview by Google in September 2025, it bridges the gap between AI code generation and real browser behavior.

## The Problem It Solves

Coding agents face a fundamental limitation: they cannot see what their generated code actually does when it runs in a browser. They're essentially programming blindfolded. Chrome DevTools MCP changes this by giving AI assistants direct access to Chrome's debugging capabilities.

## Key Features

**Performance Analysis**
- Record and analyze performance traces
- Extract actionable performance insights (LCP, FCP, etc.)
- Identify bottlenecks and optimization opportunities

**Browser Debugging**
- Analyze network requests and identify CORS issues
- Take screenshots of rendered pages
- Read and monitor console output
- Inspect DOM and CSS in real-time

**Reliable Automation**
- Automate user actions via Puppeteer
- Handle form filling, clicks, navigation
- Wait for action results automatically
- Simulate user flows for testing

## Setup Chrome with Remote Debugging

### Step 1: Create Chrome Profile

1. Open Chrome
2. Click avatar icon (top right)
3. Select "Add" to create new profile
4. Name your profile (e.g., `dev-profile`, `test-profile`)

### Step 2: Launch Chrome with Remote Debugging Port

```bash
# macOS - Single profile on port 9222
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --remote-debugging-port=9222 \
  --user-data-dir="$HOME/Library/Application Support/Google/Chrome/Profile dev-profile"

# Multiple profiles on different ports
# Profile 1 - Port 9222
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --remote-debugging-port=9222 \
  --user-data-dir="$HOME/Library/Application Support/Google/Chrome/Profile profile1"

# Profile 2 - Port 9223
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --remote-debugging-port=9223 \
  --user-data-dir="$HOME/Library/Application Support/Google/Chrome/Profile profile2"
```

### Step 3: Verify Chrome is Ready

Open browser and visit:
```
http://localhost:9222/json
```
If you see JSON response, Chrome is ready for MCP.

## Installation

### Project Configuration (.mcp.json)

Create `.mcp.json` in your project folder:

```json
{
  "mcpServers": {
    "chrome-mcp-1": {
      "type": "stdio",
      "command": "npx",
      "args": [
        "chrome-devtools-mcp@latest",
        "--browser-url=http://127.0.0.1:9223"
      ],
      "env": {}
    },
    "chrome-mcp-2": {
      "type": "stdio",
      "command": "npx",
      "args": [
        "chrome-devtools-mcp@latest",
        "--browser-url=http://127.0.0.1:9222"
      ],
      "env": {}
    }
  }
}
```

### Claude Code CLI

```bash
# Default (port 9222)
claude mcp add chrome-devtools -- npx chrome-devtools-mcp@latest

# Verify installation
claude mcp list
```

## Available Tools (26 Total)

| Category | Tools |
|----------|-------|
| **Input** | `click`, `drag`, `fill`, `fill_form`, `handle_dialog`, `hover`, `press_key`, `upload_file` |
| **Navigation** | `close_page`, `list_pages`, `navigate_page`, `new_page`, `select_page`, `wait_for` |
| **Emulation** | `emulate`, `resize_page` |
| **Performance** | `performance_start_trace`, `performance_stop_trace`, `performance_analyze_insight` |
| **Network** | `get_network_request`, `list_network_requests` |
| **Debugging** | `evaluate_script`, `get_console_message`, `list_console_messages`, `take_screenshot`, `take_snapshot` |

## Configuration Options

| Option | Description |
|--------|-------------|
| `--autoConnect` | Connect to already-running Chrome (M144+) |
| `--browser-url` | Connect to a debuggable Chrome instance |
| `--headless` | Run Chrome without UI |
| `--isolated` | Use temporary profile with auto-cleanup |
| `--channel` | Chrome channel: stable, canary, beta, dev |
| `--viewport` | Initial viewport size (e.g., 1280x720) |
| `--proxy-server` | Proxy server configuration |

## Use Cases

1. **Real-time Verification** - Validate that AI-generated fixes actually work
2. **Error Diagnosis** - Automatically detect CORS errors, console errors, network failures
3. **User Flow Testing** - Reproduce bugs through automated form interactions
4. **Layout Debugging** - Inspect live styling and DOM structure
5. **Performance Auditing** - Run traces and analyze Core Web Vitals

## Usage Examples

```python
# 1. List all open tabs
list_pages()

# 2. Open new page
new_page(url="https://example.com")

# 3. Take snapshot to get element uids
take_snapshot()

# 4. Click element by uid
click(uid="abc123")

# 5. Fill login form
fill_form(elements=[
    {"uid": "email-input-uid", "value": "user@example.com"},
    {"uid": "password-input-uid", "value": "password123"}
])

# 6. Wait for page content
wait_for(text="Dashboard")

# 7. Take screenshot
take_screenshot()

# 8. Check console logs
list_console_messages()

# 9. View network requests
list_network_requests()
```

## Troubleshooting

### Cannot connect to Chrome
```
Error: Failed to connect to Chrome
```
**Solution:**
- Verify Chrome started with `--remote-debugging-port`
- Check correct port (9222, 9223...)
- Visit `http://localhost:9222/json` to confirm

### Element not found
```
Error: Element with uid "xxx" not found
```
**Solution:**
- Take fresh snapshot: `take_snapshot()`
- UIDs change after page reload/navigate
- Wait for page to fully load first

### Timeout waiting
```
Error: Timed out after waiting 5000ms
```
**Solution:**
- Increase timeout: `wait_for(text="...", timeout=10000)`
- Verify text actually appears on page
- Take snapshot to check current state

### Click not working
**Solution:**
- Element may be covered by popup/modal
- Try hover before click
- Check element is clickable (button, link, etc.)

## Best Practices

1. **Always snapshot before interacting** - Get current page structure
2. **UIDs are dynamic** - Refresh after any page change
3. **Wait for page load** - Use `wait_for()` before actions
4. **One tab at a time** - Select correct page before actions
5. **Profile persistence** - Chrome profiles keep cookies/login state

## Quick Test

After installation, try this prompt with your AI assistant:

> "Check the performance of https://web.dev"

This validates that browser automation and performance tracing are working correctly.

## Resources

- [GitHub Repository](https://github.com/ChromeDevTools/chrome-devtools-mcp)
- [Official Chrome Blog](https://developer.chrome.com/blog/chrome-devtools-mcp)
- [Addy Osmani's Guide](https://addyosmani.com/blog/devtools-mcp/)
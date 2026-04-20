#!/bin/bash
# Install Claude Buddy to auto-start on login

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PLIST_NAME="com.allen.claudebuddy.plist"
LAUNCH_AGENTS_DIR="$HOME/Library/LaunchAgents"

echo "Installing Claude Buddy..."

# Create venv and install dependencies
if [ ! -d "$SCRIPT_DIR/venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$SCRIPT_DIR/venv"
    source "$SCRIPT_DIR/venv/bin/activate"
    pip install -r "$SCRIPT_DIR/requirements.txt"
else
    echo "Virtual environment already exists."
fi

# Create LaunchAgents directory if needed
mkdir -p "$LAUNCH_AGENTS_DIR"

# Create the plist file
cat > "$LAUNCH_AGENTS_DIR/$PLIST_NAME" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.allen.claudebuddy</string>
    <key>ProgramArguments</key>
    <array>
        <string>$SCRIPT_DIR/venv/bin/python</string>
        <string>$SCRIPT_DIR/buddy.py</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <false/>
    <key>StandardOutPath</key>
    <string>/tmp/claudebuddy.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/claudebuddy.err</string>
</dict>
</plist>
EOF

echo "LaunchAgent created at: $LAUNCH_AGENTS_DIR/$PLIST_NAME"

# Load the agent (starts it now and on future logins)
launchctl unload "$LAUNCH_AGENTS_DIR/$PLIST_NAME" 2>/dev/null || true
launchctl load "$LAUNCH_AGENTS_DIR/$PLIST_NAME"

echo ""
echo "✅ Claude Buddy installed!"
echo "   - Running now"
echo "   - Will auto-start on login"
echo ""
echo "To uninstall: ./uninstall.sh"

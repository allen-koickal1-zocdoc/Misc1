#!/bin/bash
# Uninstall Claude Buddy

PLIST_NAME="com.allen.claudebuddy.plist"
LAUNCH_AGENTS_DIR="$HOME/Library/LaunchAgents"

echo "Uninstalling Claude Buddy..."

# Stop and unload the agent
if [ -f "$LAUNCH_AGENTS_DIR/$PLIST_NAME" ]; then
    launchctl unload "$LAUNCH_AGENTS_DIR/$PLIST_NAME" 2>/dev/null || true
    rm "$LAUNCH_AGENTS_DIR/$PLIST_NAME"
    echo "LaunchAgent removed."
else
    echo "LaunchAgent not found (already uninstalled?)."
fi

# Kill any running instance
pkill -f "buddy.py" 2>/dev/null || true

echo ""
echo "✅ Claude Buddy uninstalled."
echo "   (Source files in claude-buddy/ kept - delete manually if needed)"

#!/bin/bash
set -e

INSTALL_DIR="$HOME/.local/share/claude-sandbox"
CONFIG_DIR="$HOME/.config/claude-sandbox"

echo "🗑️  Uninstalling Claude Sandbox..."

# Kill any running instances
pkill -f "claude_sandbox.py" 2>/dev/null || true

# Remove install directory
if [ -d "$INSTALL_DIR" ]; then
    rm -rf "$INSTALL_DIR"
    echo "✓ Removed $INSTALL_DIR"
fi

# Ask about config
if [ -d "$CONFIG_DIR" ]; then
    read -p "Remove config and recent directories? [y/N] " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -rf "$CONFIG_DIR"
        echo "✓ Removed $CONFIG_DIR"
    else
        echo "✓ Kept $CONFIG_DIR"
    fi
fi

echo ""
echo "✅ Claude Sandbox uninstalled!"

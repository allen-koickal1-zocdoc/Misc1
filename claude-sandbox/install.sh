#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INSTALL_DIR="$HOME/.local/share/claude-sandbox"

echo "🚀 Installing Claude Sandbox..."

# Create install directory
mkdir -p "$INSTALL_DIR"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv "$INSTALL_DIR/venv"
source "$INSTALL_DIR/venv/bin/activate"

# Install dependencies
echo "📥 Installing dependencies..."
pip install --upgrade pip
pip install -r "$SCRIPT_DIR/requirements.txt"

# Copy files
echo "📂 Copying files..."
cp "$SCRIPT_DIR/claude_sandbox.py" "$INSTALL_DIR/"
cp "$SCRIPT_DIR/icon.png" "$INSTALL_DIR/" 2>/dev/null || true

# Create launcher script
cat > "$INSTALL_DIR/run.sh" << 'EOF'
#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/venv/bin/activate"
python3 "$SCRIPT_DIR/claude_sandbox.py"
EOF
chmod +x "$INSTALL_DIR/run.sh"

echo ""
echo "✅ Claude Sandbox installed successfully!"
echo ""
echo "📍 Installed to: $INSTALL_DIR"
echo ""
echo "To start:       $INSTALL_DIR/run.sh"
echo "To uninstall:   $SCRIPT_DIR/uninstall.sh"
echo ""
echo "⚠️  For global hotkey (⌘⇧C), grant Accessibility permissions:"
echo "   System Settings > Privacy & Security > Accessibility"
echo "   Add: $INSTALL_DIR/venv/bin/python3"

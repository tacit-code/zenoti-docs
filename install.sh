#!/bin/bash
# install.sh - Install zenoti-docs for Claude Code

set -e

REPO_URL="https://github.com/tacit-code/zenoti-docs"
INSTALL_DIR="$HOME/.zenoti-docs"

echo "Installing Zenoti API Documentation..."

# Clone or update repository
if [ -d "$INSTALL_DIR" ]; then
    echo "Updating existing installation..."
    cd "$INSTALL_DIR"
    git pull
else
    echo "Cloning repository..."
    git clone "$REPO_URL" "$INSTALL_DIR"
fi

# Create symlink in common locations
if [ -d "$HOME/.claude" ]; then
    ln -sf "$INSTALL_DIR/docs" "$HOME/.claude/zenoti-docs"
fi

echo ""
echo "Installation complete!"
echo ""
echo "Usage with Claude Code:"
echo "  Add to your CLAUDE.md:"
echo "    Reference Zenoti API docs at: ~/.zenoti-docs/docs/"
echo ""
echo "  Or use the /zenoti command if configured."

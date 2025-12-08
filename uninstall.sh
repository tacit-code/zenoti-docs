#!/bin/bash
# uninstall.sh - Uninstall zenoti-docs

set -e

INSTALL_DIR="$HOME/.zenoti-docs"

echo "Uninstalling Zenoti API Documentation..."

# Remove symlink if it exists
if [ -L "$HOME/.claude/zenoti-docs" ]; then
    echo "Removing symlink..."
    rm "$HOME/.claude/zenoti-docs"
fi

# Remove installation directory
if [ -d "$INSTALL_DIR" ]; then
    echo "Removing installation directory..."
    rm -rf "$INSTALL_DIR"
fi

echo ""
echo "Uninstallation complete!"

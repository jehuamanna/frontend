#!/bin/bash
# Install diagram generation tools

echo "Installing Graphviz and Python bindings..."

# Check if running with sudo
if [ "$EUID" -ne 0 ]; then
    echo "This script needs sudo privileges to install system packages."
    echo "Run with: sudo bash install-diagram-tools.sh"
    exit 1
fi

# Update package list
apt-get update

# Install graphviz and Python bindings
apt-get install -y graphviz python3-graphviz

# Verify installation
if which dot > /dev/null 2>&1 && python3 -c "import graphviz" 2>/dev/null; then
    echo ""
    echo "Success! Diagram tools installed."
    echo ""
    echo "Test with:"
    echo "  python3 generate_diagrams.py"
    echo ""
    echo "Generate PDF with diagrams:"
    echo "  bash generate-pdf.sh"
else
    echo ""
    echo "Installation failed. Please check the error messages above."
    exit 1
fi


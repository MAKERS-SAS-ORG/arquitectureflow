#!/bin/bash
# Setup script for Diagrams Python
# Usage: bash drawflow/tools/diagrams-python/setup.sh

set -e

TOOL_DIR="/Users/didierrestrepo/MK/arquitectureflow-main/drawflow/tools/diagrams-python"

echo "🔧 Setting up Diagrams Python environment..."

# Check graphviz
if ! command -v dot &> /dev/null; then
    echo "📦 Installing Graphviz..."
    brew install graphviz
else
    echo "✅ Graphviz already installed: $(dot -V 2>&1)"
fi

# Create/update venv
if [ ! -d "$TOOL_DIR/.venv" ]; then
    echo "📦 Creating Python virtual environment..."
    python3 -m venv "$TOOL_DIR/.venv"
fi

echo "📦 Installing diagrams..."
source "$TOOL_DIR/.venv/bin/activate"
pip install --quiet diagrams

echo ""
echo "✅ Setup completado."
echo ""
echo "Para activar el entorno:"
echo "  source $TOOL_DIR/.venv/bin/activate"
echo ""
echo "Para generar un diagrama:"
echo "  python3 templates/c4_context.py"

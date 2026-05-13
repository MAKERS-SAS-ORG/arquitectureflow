#!/bin/bash
# Setup script for Excalidraw Local MCP Server
# Usage: bash drawflow/tools/excalidraw-local/setup.sh

set -e

REPO_DIR="/Users/didierrestrepo/MK/arquitectureflow-main/drawflow/tools/excalidraw-local/server"

echo "🔧 Building Excalidraw MCP Server..."
cd "$REPO_DIR"
npm ci
npm run build

echo ""
echo "✅ Build completado exitosamente."
echo ""
echo "Para iniciar el canvas server:"
echo "  cd $REPO_DIR"
echo "  PORT=3000 npm run canvas"
echo ""
echo "Luego abre http://127.0.0.1:3000 en tu navegador."
echo ""
echo "Para verificar:"
echo "  curl -s http://127.0.0.1:3000/health"

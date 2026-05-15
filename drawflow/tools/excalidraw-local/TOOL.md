# Herramienta: Excalidraw Local (yctimlin/mcp_excalidraw)
# Tipo: MCP Server (stdio) + Canvas Server (HTTP)

---

## Resumen

Canvas Excalidraw controlado por IA con 26 herramientas MCP. El agente crea
elementos uno a uno o en batch, verifica visualmente con screenshots, y
refina iterativamente. Ideal para diagramas C4 y arquitectura formal.

## Setup

### Build (una sola vez)
```bash
cd /Users/didierrestrepo/MK/arquitectureflow-main/drawflow/tools/excalidraw-local/server
npm ci && npm run build
```

### Iniciar Canvas Server
```bash
cd /Users/didierrestrepo/MK/arquitectureflow-main/drawflow/tools/excalidraw-local/server
PORT=3000 npm run canvas
# Abrir http://127.0.0.1:3000 en navegador
```

### Verificar
```bash
curl -s http://127.0.0.1:3000/health
```

### MCP Config para Antigravity (~/.gemini/antigravity/mcp_config.json)
```json
{
  "excalidraw-local": {
    "command": "node",
    "args": ["/Users/didierrestrepo/MK/arquitectureflow-main/drawflow/tools/excalidraw-local/server/dist/index.js"],
    "env": {
      "EXPRESS_SERVER_URL": "http://127.0.0.1:3000",
      "ENABLE_CANVAS_SYNC": "true"
    }
  }
}
```

---

## Herramientas MCP (28 total)

### Librerías .excalidrawlib (USAR PRIMERO para C4 / BPMN / hexagonal)
| Tool | Descripción |
|---|---|
| `list_library_items` | Lista items de las librerías (C4, BPMN, hexagonal, lib general). **Primera llamada al diagramar C4** — descubre Person, Web App, Database, System, etc. |
| `insert_library_item` | Inserta un item pre-estilado en `(x,y)` con `label`/`description` opcionales. Mucho mas barato en tokens que `batch_create_elements` desde cero. |

### CRUD de Elementos
| Tool | Descripción |
|---|---|
| `create_element` | Crear un elemento individual |
| `batch_create_elements` | Crear múltiples elementos en un batch |
| `get_element` | Obtener un elemento por ID |
| `query_elements` | Listar todos los elementos |
| `update_element` | Actualizar un elemento |
| `delete_element` | Eliminar un elemento |
| `duplicate_elements` | Duplicar elementos con offset |

### Layout y Organización
| Tool | Descripción |
|---|---|
| `align_elements` | Alinear elementos (left/center/right/top/middle/bottom) |
| `distribute_elements` | Distribuir uniformemente |
| `group_elements` | Agrupar elementos |
| `ungroup_elements` | Desagrupar |
| `lock_elements` | Bloquear posición |
| `unlock_elements` | Desbloquear |

### Inspección y Verificación
| Tool | Descripción |
|---|---|
| `describe_scene` | Texto estructurado del estado del canvas |
| `get_canvas_screenshot` | **PNG del canvas** — el agente VE su trabajo |
| `set_viewport` | Control de zoom y scroll (scrollToContent) |

### Exportación
| Tool | Descripción |
|---|---|
| `export_scene` | Exportar a .excalidraw JSON |
| `import_scene` | Importar desde .excalidraw JSON |
| `export_to_image` | Exportar a PNG/SVG |
| `export_to_excalidraw_url` | URL compartible en excalidraw.com |

### Conversión y Estado
| Tool | Descripción |
|---|---|
| `create_from_mermaid` | Convertir diagrama Mermaid a Excalidraw |
| `clear_canvas` | Limpiar todo el canvas |
| `snapshot_scene` | Guardar estado con nombre |
| `restore_snapshot` | Restaurar estado guardado |
| `read_diagram_guide` | Mejores prácticas de diseño |
| `read_me` | Información del servidor |

---

## Referencia detallada

Para guía completa de workflows, anti-patrones, coordenadas, y colores C4:
- `drawflow/tools/excalidraw-local/TOOL.md`
- `drawflow/tools/excalidraw-local/references/cheatsheet.md`

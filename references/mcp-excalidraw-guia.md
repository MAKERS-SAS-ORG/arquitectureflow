# Guia de Uso: Excalidraw MCP Server para Arquitectura

> Server: yctimlin/mcp_excalidraw — https://github.com/yctimlin/mcp_excalidraw
> Ubicacion local: `/Users/didierrestrepo/MK/arquitectureflow-main/drawflow/tools/excalidraw-local/server/`

---

## Regla #1: NUNCA generar JSON raw de Excalidraw

El MCP server tiene 26 herramientas que crean elementos uno a uno o en batch.
Generar arrays JSON completos de Excalidraw desperdicia tokens y no permite iteracion.

**SIEMPRE:** Usar MCP tools (batch_create_elements) o REST API (POST /api/elements/batch)
**NUNCA:** Generar JSON de Excalidraw manualmente ni usar create_view del MCP built-in de Claude

---

## Setup

### 1. Iniciar canvas server
```bash
cd /Users/themakers/mcp_excalidraw
PORT=3000 npm run canvas
# Abrir http://localhost:3000 en navegador
```

### 2. Registrar MCP en Claude Code (una sola vez)
```bash
claude mcp add excalidraw -s user \
  -e EXPRESS_SERVER_URL=http://localhost:3000 \
  -- node /Users/didierrestrepo/MK/arquitectureflow-main/drawflow/tools/excalidraw-local/server/dist/index.js
```

### 3. Verificar
```bash
curl -s http://localhost:3000/health
# Debe retornar: {"status":"healthy",...}
```

---

## Librerias C4 Disponibles

Ubicacion: `drawflow/tools/excalidraw-local/libs/`

### c4-architecture.excalidrawlib (10 items)
| Item | Elementos | Uso |
|---|---|---|
| C4 elements | 41 | Coleccion completa C4 |
| Person | 5 | Actor/usuario (ellipse + rect + labels) |
| Web App | 8 | Contenedor tipo web app |
| Mobile App | 6 | Contenedor tipo mobile |
| Component | 4 | Componente interno |
| System | 4 | Sistema principal (azul) |
| Existing System | 4 | Sistema externo (gris) |
| Database | 5 | Contenedor tipo base de datos |
| Group | 2 | Boundary/agrupacion |
| Relation | 2 | Flecha con label |

### Colores de la libreria C4
| Elemento | Background | Uso |
|---|---|---|
| Person | `#0c37a2` | Actores/usuarios |
| System/Container | `#228be6` | Sistema principal y contenedores |
| Existing System | `#868e96` | Sistemas externos |
| Queue/Middleware | `#7048e8` | Colas, buses, middleware |
| Boundary | `#ced4da` opacity 15 | Grupos/boundaries |

---

## Referencia Rapida de Herramientas

### MCP Tools (26) — cuando estan registradas

| Categoria | Tool | Descripcion |
|---|---|---|
| **CRUD** | `batch_create_elements` | Crear multiples elementos en un batch |
| | `create_element` | Crear un elemento |
| | `update_element` | Modificar elemento por ID |
| | `delete_element` | Eliminar elemento |
| | `query_elements` | Buscar elementos |
| **Layout** | `align_elements` | Alinear (left/center/right/top/middle/bottom) |
| | `distribute_elements` | Distribuir uniformemente |
| | `group_elements` / `ungroup_elements` | Agrupar/desagrupar |
| **Verificacion** | `describe_scene` | Descripcion textual de la escena |
| | `get_canvas_screenshot` | Screenshot PNG para verificar |
| **Estado** | `clear_canvas` | Limpiar todo |
| | `snapshot_scene` | Guardar snapshot con nombre |
| | `restore_snapshot` | Restaurar snapshot |
| **Exportar** | `export_scene` | Exportar a .excalidraw |
| | `export_to_image` | Exportar PNG/SVG |
| | `export_to_excalidraw_url` | URL compartible |
| **Conversion** | `create_from_mermaid` | Mermaid → Excalidraw |
| **Viewport** | `set_viewport` | Controlar camara/zoom |
| **Guia** | `read_diagram_guide` | Mejores practicas |

### REST API — fallback cuando MCP no esta registrado

| Operacion | Endpoint |
|---|---|
| Limpiar canvas | `DELETE /api/elements/clear` |
| Crear batch | `POST /api/elements/batch` con `{"elements": [...]}` |
| Obtener elementos | `GET /api/elements` |
| Actualizar | `PUT /api/elements/:id` |
| Eliminar | `DELETE /api/elements/:id` |
| Snapshot guardar | `POST /api/snapshots` con `{"name": "..."}` |
| Snapshot restaurar | `GET /api/snapshots/:name` |
| Health check | `GET /health` |

### CRITICO: Diferencias de formato MCP vs REST

| Campo | MCP | REST |
|---|---|---|
| Labels | `"text": "Label"` | `"label": {"text": "Label"}` |
| Arrow start | `startElementId: "id"` | `"start": {"id": "id"}` |
| Arrow end | `endElementId: "id"` | `"end": {"id": "id"}` |

---

## Workflow para Arquitecto

### Para generar un diagrama C4 nuevo:

1. Verificar que el canvas server esta corriendo
2. Abrir http://localhost:3000 en el navegador para ver el canvas en vivo
3. Pedir a la IA que genere el diagrama siguiendo `skills/diagramas/SKILL.md`
4. Revisar en el navegador — pedir ajustes si es necesario
5. Guardar snapshot para iterar despues
6. Exportar .excalidraw al directorio del proyecto

### Para iterar un diagrama existente:

1. Restaurar snapshot: `restore_snapshot("nombre")`
2. Pedir a la IA los cambios especificos (agregar sistema, mover contenedor, etc.)
3. La IA usa update_element/delete_element/create_element individualmente
4. Verificar con screenshot
5. Guardar nuevo snapshot

### Scripts utiles (en drawflow/tools/excalidraw-local/scripts/)

```bash
node scripts/healthcheck.cjs              # Verificar server
node scripts/clear-canvas.cjs             # Limpiar canvas
node scripts/export-elements.cjs --out diagram.json  # Exportar
node scripts/import-elements.cjs --in diagram.json   # Importar
```

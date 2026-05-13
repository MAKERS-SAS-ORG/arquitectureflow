# Herramienta: Excalidraw Remote (excalidraw/excalidraw-mcp — Oficial)
# Tipo: MCP App (Streamable HTTP)

---

## Resumen

MCP App oficial de Excalidraw. Genera diagramas hand-drawn desde prompts
de texto natural. Zero setup — funciona desde URL remota.

Ideal para: bocetos rápidos, prototipos, ideación.
NO ideal para: diagramas C4 formales, iteración detallada.

## MCP Config para Antigravity (~/.gemini/antigravity/mcp_config.json)

```json
{
  "excalidraw-remote": {
    "url": "https://mcp.excalidraw.com",
    "headers": {
      "Authorization": "Bearer sk-DTnbHT6f1UVG30mcYP6wLQgzSb5wVAPpKu-oZtM98kaACc3ifGc4BPd1VPM_Ub4C"
    }
  }
}
```

### URL alternativa (si la anterior falla)
```json
{
  "excalidraw-remote": {
    "url": "https://api.excalidraw.com/api/v1/mcp",
    "headers": {
      "Authorization": "Bearer sk-DTnbHT6f1UVG30mcYP6wLQgzSb5wVAPpKu-oZtM98kaACc3ifGc4BPd1VPM_Ub4C"
    }
  }
}
```

## Herramienta MCP

| Tool | Descripción |
|---|---|
| `create_excalidraw` | Genera un diagrama Excalidraw completo desde un prompt |

## Uso

Prompt de ejemplo:
- "Dibuja un diagrama de arquitectura con un usuario conectándose a un API server que habla con una base de datos"
- "Sketch de microservicios con API Gateway, 3 servicios y una cola de mensajes"

## Cuándo Preferir Excalidraw Remote

| Situación | Excalidraw Remote | Excalidraw Local |
|---|---|---|
| Boceto rápido de idea | ✅ | ⚠️ Overkill |
| Diagrama C4 formal | ❌ | ✅ |
| Iteración y refinamiento | ❌ | ✅ |
| Sin setup local | ✅ | ❌ |
| Control preciso | ❌ | ✅ |

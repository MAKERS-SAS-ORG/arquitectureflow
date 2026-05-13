# Skill: Drawflow — Hub Unificado de Diagramación
# Version: 2026.5
# Tipo: Skill de soporte (invocado por orquestador o directamente)

> Referencia: Brown, S. *C4 Model.* c4model.com
> Referencia: ISO/IEC/IEEE 42010:2022 — Architecture Views
> Herramientas: Excalidraw MCP (local+remoto) + Diagrams (Python)

---

## Propósito

Hub centralizado de herramientas de diagramación para arquitectura de soluciones.
Consolida 3 herramientas complementarias bajo un solo punto de entrada para el
orquestador y otros skills.

### Activación

Este skill se activa cuando:
- `/orquestador drawflow` — Selección interactiva de herramienta
- `/orquestador excalidraw-local` — Directo a Excalidraw MCP local (C4, iterativo)
- `/orquestador excalidraw-remote` — Directo a Excalidraw remoto (bocetos rápidos)
- `/orquestador diagrams-python` — Directo a Diagrams (infra con iconos cloud)
- `skills/diagramas/SKILL.md` solicita una herramienta de diagramación

---

## Herramientas Disponibles

| Herramienta | ID | Tipo | Cuándo Usar |
|---|---|---|---|
| **Excalidraw Local** | `excalidraw-local` | MCP (26 tools, stdio) | C4 L1/L2, deployment, arquitectura formal — iterativo con feedback visual |
| **Excalidraw Remote** | `excalidraw-remote` | MCP (streamable HTTP) | Bocetos rápidos, prototipos, ideación desde prompt |
| **Diagrams Python** | `diagrams-python` | Script Python + Graphviz | Infraestructura con iconos oficiales AWS/GCP/Azure/K8s, Diagram as Code |

---

## Tabla de Decisión: ¿Qué Herramienta Usar?

| Tipo de Diagrama | Herramienta Recomendada | Alternativa |
|---|---|---|
| C4 Context (L1) | `excalidraw-local` | `diagrams-python` (si incluye cloud icons) |
| C4 Container (L2) | `excalidraw-local` | Mermaid C4 (text-based) |
| C4 Deployment | `excalidraw-local` | `diagrams-python` (topología infra) |
| Arquitectura AWS/GCP/Azure | `diagrams-python` ⭐ | `excalidraw-local` |
| Kubernetes Deployment | `diagrams-python` ⭐ | `excalidraw-local` |
| Microservicios + Event-driven | `diagrams-python` | `excalidraw-local` |
| Boceto rápido / ideación | `excalidraw-remote` | `excalidraw-local` |
| Secuencia (sequence diagram) | Mermaid | `excalidraw-local` |
| Flujo / flowchart | Mermaid | `excalidraw-local` |
| Context Map (DDD) | `excalidraw-local` | Mermaid |
| Stakeholder Map | `excalidraw-local` | — |

---

## Herramienta 1: Excalidraw Local (yctimlin/mcp_excalidraw)

### Descripción
Canvas Excalidraw en vivo con 26 herramientas MCP. El agente crea, edita, y verifica
diagramas element-by-element con feedback visual (screenshot + describe_scene).

### Ventajas
- ✅ 26 herramientas MCP (CRUD, align, distribute, group, snapshot, viewport)
- ✅ Feedback loop cerrado: `get_canvas_screenshot` → ve lo que dibujó → corrige
- ✅ Control preciso de coordenadas, colores, tamaños
- ✅ Conversión Mermaid → Excalidraw: `create_from_mermaid`
- ✅ Export: .excalidraw JSON, PNG, SVG, URL compartible
- ✅ Snapshots: guardar/restaurar estados del canvas
- ✅ Librerías C4: colores y shapes preconfigurados

### Pre-requisitos
```bash
# 1. Build (una sola vez)
cd /Users/didierrestrepo/MK/arquitectureflow-main/drawflow/tools/excalidraw-local/server
npm ci && npm run build

# 2. Iniciar canvas server (en terminal separada)
PORT=3000 npm run canvas

# 3. Verificar
curl -s http://127.0.0.1:3000/health
```

### MCP Config (Antigravity)
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

### Workflow Completo
Ver `drawflow/tools/excalidraw-local/TOOL.md` o `drawflow/tools/excalidraw-local/TOOL.md`

---

## Herramienta 2: Excalidraw Remote (excalidraw/excalidraw-mcp — Oficial)

### Descripción
MCP App oficial que genera diagramas Excalidraw desde un prompt. Rendering inline
en chat con viewport interactivo. No requiere setup local.

### Ventajas
- ✅ Zero setup — funciona con URL remota
- ✅ Generación rápida desde prompt natural
- ✅ Rendering visual en chat
- ✅ Soporte MCP Apps (streamable HTTP)

### Limitaciones
- ❌ Solo 1 herramienta (create_excalidraw)
- ❌ Sin feedback loop (no puede ver lo que dibujó)
- ❌ Sin control de coordenadas
- ❌ Sin conversión Mermaid
- ❌ Sin export a archivo

### MCP Config (Antigravity)
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

---

## Herramienta 3: Diagrams Python (diagrams.mingrammer.com)

### Descripción
Librería Python para diagramar infraestructura cloud como código. Genera PNG con
iconos oficiales de proveedores cloud (AWS, GCP, Azure, K8s, OnPrem, etc.)

### Ventajas
- ✅ **Iconos oficiales** de AWS, GCP, Azure, K8s, Firebase, etc.
- ✅ **Diagram as Code** — versionable en Git
- ✅ Clusters (agrupación visual)
- ✅ Edges con colores y labels
- ✅ Soporte C4 nativo (`diagrams.c4`)
- ✅ Nodos custom con imágenes propias
- ✅ Output: PNG, SVG, PDF, DOT

### Limitaciones
- ❌ No interactivo (genera imagen estática)
- ❌ Layout automático por Graphviz (menos control manual)
- ❌ Requiere Python + Graphviz

### Pre-requisitos
```bash
# Activar venv
source /Users/didierrestrepo/MK/arquitectureflow-main/drawflow/tools/diagrams-python/.venv/bin/activate

# Verificar
python3 -c "from diagrams import Diagram; print('OK')"
```

### Proveedores Soportados
- **AWS**: EC2, ECS, EKS, Lambda, RDS, DynamoDB, S3, SQS, SNS, ELB, CloudFront, Route53, etc.
- **GCP**: GCE, GKE, Cloud Run, BigQuery, PubSub, Cloud Functions, Cloud SQL, etc.
- **Azure**: VM, AKS, Functions, SQL DB, CosmosDB, Event Grid, etc.
- **Kubernetes**: Pod, Deployment, Service, Ingress, StatefulSet, HPA, etc.
- **OnPrem**: Nginx, PostgreSQL, Redis, Kafka, Prometheus, Grafana, etc.
- **C4**: Person, System, Container, Component, Relationship
- **Custom**: Cualquier icono PNG/SVG propio

### Workflow
1. Activar venv: `source drawflow/tools/diagrams-python/.venv/bin/activate`
2. Crear script Python (o usar template de `drawflow/tools/diagrams-python/templates/`)
3. Ejecutar: `python3 script.py`
4. Output: PNG en directorio actual (o en `drawflow/tools/diagrams-python/output/`)

Ver `drawflow/tools/diagrams-python/TOOL.md` para detalles y templates.

---

## Integración con Orquestador

Cuando `skills/diagramas/SKILL.md` necesita generar un diagrama, carga este skill
y selecciona la herramienta según la tabla de decisión.

### Flujo
```
/orquestador diagrama
  → skills/diagramas/SKILL.md
    → drawflow/SKILL.md (selección de herramienta)
      → drawflow/tools/[herramienta]/TOOL.md
```

### Comandos directos
```
/orquestador drawflow               → Menú interactivo
/orquestador excalidraw-local        → Excalidraw MCP local directo
/orquestador excalidraw-remote       → Excalidraw remoto directo
/orquestador diagrams-python         → Diagrams Python directo
```

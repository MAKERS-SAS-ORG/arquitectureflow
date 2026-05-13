# Drawflow — Hub de Herramientas de Diagramación

**Version:** 2026.5  
**Framework:** ArquitectureFlow

## Descripción

Drawflow es el hub unificado de herramientas de diagramación para el framework
ArquitectureFlow. Consolida 3 herramientas complementarias para cubrir todo el
espectro de diagramación en arquitectura de soluciones.

## Herramientas

### 1. Excalidraw Local (⭐ Principal para C4)
- **Repo:** [yctimlin/mcp_excalidraw](https://github.com/yctimlin/mcp_excalidraw)
- **Tipo:** MCP Server (26 herramientas) + Canvas Server local
- **Ideal para:** C4 L1/L2, deployment, arquitectura formal con iteración
- **Puerto:** 3000

### 2. Excalidraw Remote (Bocetos rápidos)
- **Repo:** [excalidraw/excalidraw-mcp](https://github.com/excalidraw/excalidraw-mcp)
- **Tipo:** MCP App (streamable HTTP remoto)
- **Ideal para:** Bocetos rápidos, prototipos, ideación

### 3. Diagrams Python (Infraestructura Cloud)
- **Repo:** [mingrammer/diagrams](https://github.com/mingrammer/diagrams)
- **Tipo:** Python + Graphviz (Diagram as Code)
- **Ideal para:** Arquitectura AWS/GCP/Azure/K8s con iconos oficiales

## Estructura
```
drawflow/
├── SKILL.md              # Skill principal
├── README.md             # Este archivo
├── tools/
│   ├── excalidraw-local/
│   │   ├── TOOL.md       # Documentación (26 MCP tools)
│   │   └── setup.sh      # Script de build
│   ├── excalidraw-remote/
│   │   └── TOOL.md       # Config remota
│   └── diagrams-python/
│       ├── TOOL.md        # Documentación completa
│       ├── setup.sh       # Instalación (venv + pip)
│       ├── .venv/         # Virtual environment
│       ├── templates/     # Templates listos para usar
│       │   ├── c4_context.py
│       │   ├── c4_container.py
│       │   ├── aws_architecture.py
│       │   ├── k8s_deployment.py
│       │   └── microservices.py
│       └── output/        # Diagramas generados (.png)
```

## Invocación desde Orquestador

```
/orquestador drawflow            # Menú interactivo
/orquestador excalidraw-local    # Excalidraw iterativo
/orquestador excalidraw-remote   # Boceto rápido
/orquestador diagrams-python     # Infra con iconos cloud
```

## Comparación Rápida

| Criterio | Excalidraw Local | Excalidraw Remote | Diagrams Python |
|---|---|---|---|
| Setup | npm ci + build | Zero | pip + graphviz |
| Iteración | ✅ Feedback visual | ❌ One-shot | ❌ Estático |
| Control layout | ✅ Preciso (x,y) | ❌ Automático | ⚠️ Graphviz |
| Iconos cloud | ❌ | ❌ | ✅ Oficiales |
| C4 Model | ✅ Ideal | ⚠️ Básico | ✅ Bueno |
| Interactivo | ✅ Canvas vivo | ✅ En chat | ❌ PNG estático |
| Tools MCP | 26 | 1 | 0 (script) |
| Versionable | .excalidraw JSON | ❌ | ✅ Python code |

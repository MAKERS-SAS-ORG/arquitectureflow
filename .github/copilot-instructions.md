# ArquitectureFlow — Instrucciones para GitHub Copilot

Este repositorio contiene un framework de arquitectura de soluciones asistida por IA.
Lee estas instrucciones antes de responder cualquier pregunta sobre arquitectura.

## Punto de entrada

El flujo siempre inicia con el orquestador. Cuando el usuario mencione arquitectura,
disenar un sistema, o pida crear artefactos, lee `skills/orquestador/SKILL.md` y
sigue sus fases en orden.

## Skills disponibles

Cada skill vive en `skills/[nombre]/SKILL.md`. Cargalos cuando el orquestador
los necesite:

- `skills/rfc/SKILL.md` — Request for Comments
- `skills/adr/SKILL.md` — Architecture Decision Record
- `skills/prd/SKILL.md` — Product Requirements Document
- `skills/tech-spec/SKILL.md` — Technical Specification
- `skills/system-design/SKILL.md` — System Design
- `skills/runbook/SKILL.md` — Requisitos Operacionales
- `skills/post-mortem/SKILL.md` — Post-Mortem
- `skills/system-prompt-spec/SKILL.md` — Especificacion de Agente LLM
- `skills/diagramas/SKILL.md` — Diagramas C4 con Excalidraw MCP

## Templates

Todos los artefactos usan plantillas en `templates/`. Siempre usa la plantilla
del artefacto que estes generando.

## Idioma

Todo el contenido se escribe en Espanol.

## Como invocar el flujo en Copilot Chat

```
@workspace Lee skills/orquestador/SKILL.md y ejecuta la Fase 0.
Necesito disenar la arquitectura de [tu problema].
```

Para artefactos especificos:
```
@workspace Lee skills/rfc/SKILL.md y templates/rfc.md.
Genera el RFC basandote en [archivo CB-NNN.md].
```

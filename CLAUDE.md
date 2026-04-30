# ArquitectureFlow — Framework Modular de Arquitectura de Soluciones

**Version:** 2026.4
**Idioma:** Todo el contenido se escribe en Espanol.

## Que es ArquitectureFlow

Framework de skills modulares para la practica de arquitectura de soluciones asistida por IA.
Guia al arquitecto de soluciones en la creacion iterativa de artefactos arquitectonicos
con estandares de la industria, diagramas C4 via Excalidraw MCP, y metodologia specs-driven.

## Principio Anti-Vibecoding

> Si no puedes explicar en un parrafo que problema resuelve lo que estas a punto de construir,
> no estas listo para construir. Pensar antes de construir. Documentar antes de codear.
> Decidir antes de implementar.

Ver `references/manifiesto.md` para el manifiesto completo.

## Alcance: Arquitecto de Soluciones

Este framework opera en el scope del **Arquitecto de Soluciones** (SA):
- El QUE y el POR QUE: alineacion de negocio, seleccion tecnologica, estrategia de integracion, NFRs
- NO el COMO de implementacion: eso es responsabilidad del Arquitecto de Software y el equipo de ingenieria

Ver `references/scope-sa-vs-swa.md` para la delineacion completa.

## Punto de Entrada

El skill principal es el **orquestador**: `skills/orquestador/SKILL.md`
Registrado como slash command en `.claude/commands/orquestador.md`.

### Modos de invocacion

| Comando | Que hace |
|---|---|
| `/orquestador` | Auto-detecta: si hay artefactos muestra estado, si no inicia nuevo |
| `/orquestador nuevo` | Inicia arquitectura nueva (pregunta tipo de proyecto y carpeta) |
| `/orquestador continuar` | Lista arquitecturas existentes y pregunta cual retomar |
| `/orquestador estado` | Muestra estado de artefactos sin preguntar |
| `/micro-cdt` | Taller guiado con ejercicio de micro-inversion en CDTs |

El orquestador carga internamente el skill de artefacto apropiado:
- `skills/rfc/SKILL.md` — Request for Comments
- `skills/adr/SKILL.md` — Architecture Decision Record
- `skills/prd/SKILL.md` — Product Requirements Document
- `skills/tech-spec/SKILL.md` — Technical Specification
- `skills/system-design/SKILL.md` — System Design Document
- `skills/runbook/SKILL.md` — Runbook de Operaciones
- `skills/post-mortem/SKILL.md` — Post-Mortem de Incidentes
- `skills/system-prompt-spec/SKILL.md` — Especificacion de Agente LLM
- `skills/diagramas/SKILL.md` — Generacion de diagramas C4 con Excalidraw MCP

## Adherencia Arquitectonica

El **Tablero de Adherencia Arquitectonica (TAA)** es el artefacto que conecta la arquitectura
documentada con la implementacion. Rastrea estado de artefactos, trazabilidad de decisiones,
gates de revision por sprint y desviaciones justificadas.
Template: `templates/tablero-adherencia.md`. Se genera en la Fase 7 del orquestador.

## Taller Guiado

Ver `taller.md` para un taller paso a paso con prompts de ejemplo, flujo completo
y el Tablero de Adherencia como artefacto final.

## Metodologia Specs-Driven

La arquitectura se entrega **iterativamente**, no en cascada:
1. Cada artefacto tiene niveles de madurez: Draft -> Review -> Approved -> Superseded
2. El arquitecto entrega el artefacto de mayor valor primero
3. Los artefactos se refactorizan cuando la arquitectura evoluciona
4. La IA asiste pero el arquitecto aprueba — human-in-the-loop siempre

Ver `references/protocolo-iteracion.md` para la metodologia completa.

## Estandares de Referencia

Todos los artefactos estan alineados con estandares de la industria documentados en
`references/bibliografia.md`. Principales: TOGAF 10th Ed, ISO/IEC/IEEE 42010:2022,
C4 Model, Arc42, MADR 4.0, ISO/IEC 25010:2023, Google SRE Book.

## Diagramas

Los diagramas se generan via Excalidraw MCP (C4 Model como notacion principal).
Ver `references/diagramas-estrategia.md` para la estrategia y `skills/diagramas/SKILL.md` para el skill.

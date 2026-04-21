# ArquitectureFlow — Framework Modular de Arquitectura de Soluciones

**Version:** 2026.2
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
Usa `/orquestador` para iniciar un flujo de arquitectura.

El orquestador evalua el contexto y enruta al skill de artefacto apropiado:
- `/rfc` — Request for Comments
- `/adr` — Architecture Decision Record
- `/prd` — Product Requirements Document
- `/tech-spec` — Technical Specification
- `/system-design` — System Design Document
- `/runbook` — Runbook de Operaciones
- `/post-mortem` — Post-Mortem de Incidentes
- `/system-prompt-spec` — Especificacion de Agente LLM
- `/diagramas` — Generacion de diagramas C4 con Excalidraw MCP

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

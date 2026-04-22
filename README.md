# ArquitectureFlow

Framework modular de arquitectura de soluciones asistida por IA.
Guia al **Arquitecto de Soluciones** en la creacion iterativa de artefactos
arquitectonicos con estandares de la industria.

---

## Para quien es este framework

Para **Arquitectos de Soluciones** que trabajan en el QUE y el POR QUE:
- Alineacion de negocio y seleccion tecnologica
- Estrategia de integracion y NFRs cuantificados
- Comunicacion con stakeholders via diagramas C4
- Decisiones arquitectonicas documentadas y trazables

NO es para implementacion (eso lo resuelve el Software Architect y el equipo de ingenieria).

---

## Flujo de Trabajo

El framework sigue una metodologia **specs-driven iterativa**: no es necesario completar
todos los artefactos antes de entregar valor. Cada artefacto entregado es valor.

### Orden recomendado

```
  1. RFC                    "Que problema resolvemos y como?"
     |
  2. ADR                    "Que decisiones tomamos y por que?"
     |
  3. PRD                    "Que funcionalidades exactamente?"
     |
  4. Tech Spec + Diagramas  "Con que tecnologias y como se integran?"
     |                      (Diagrama C4 Level 2 via Excalidraw MCP)
     |
  5. System Design          "Como escala, como es seguro?"
     |
  6. Runbook (*)            "Que necesita Operations para operar?"
     |
  7. Post-Mortem (**)       "Que aprendimos cuando fallo?"

  (*) El SA define REQUISITOS operacionales; Operations redacta los procedimientos
  (**) Solo cuando ocurre un incidente
```

### Si el sistema incluye un agente LLM:
Agregar **System Prompt Spec** en paralelo con la Tech Spec.

### Excepciones validas al orden:
- Decision urgente que bloquea al equipo → empezar con **ADR**
- Incidente en produccion → empezar con **Post-Mortem**
- Spike tecnico → **RFC lite** (version reducida)
- Integracion con tercero → agregar **Context Map** en paralelo

---

## Como empezar

### 1. Abrir el orquestador
El punto de entrada es `skills/orquestador/SKILL.md`. El orquestador:
- Captura el contexto del proyecto (problema, stakeholders, restricciones)
- Selecciona que artefactos aplican segun `references/matriz-decision.md`
- Enruta al skill de artefacto apropiado

### 2. Crear artefactos iterativamente
Cada artefacto tiene:
- **Skill** (`skills/[nombre]/SKILL.md`) — workflow guiado paso a paso
- **Template** (`templates/[nombre].md`) — plantilla con YAML frontmatter estandarizado
- **Niveles de madurez** — Draft → Review → Approved → Superseded

### 3. Generar diagramas C4
Los diagramas se generan con el MCP server de Excalidraw (`skills/diagramas/SKILL.md`):
- Iniciar canvas server: `cd /path/to/mcp_excalidraw && PORT=3000 npm run canvas`
- Abrir http://localhost:3000 en el navegador
- La IA crea los diagramas element-by-element via MCP tools o REST API
- Librerias C4 incluidas en `mcp-excalidraw/libs/`

---

## Estructura del proyecto

```
arquitectureflow/
|
|-- CLAUDE.md                  # Punto de entrada para Claude (instrucciones del proyecto)
|-- README.md                  # Esta guia
|
|-- skills/                    # Skills modulares (workflow guiado)
|   |-- orquestador/           # Orquestador principal
|   |-- rfc/                   # Request for Comments
|   |-- adr/                   # Architecture Decision Record
|   |-- prd/                   # Product Requirements Document
|   |-- tech-spec/             # Technical Specification
|   |-- system-design/         # System Design Document
|   |-- runbook/               # Requisitos Operacionales (SA scope)
|   |-- post-mortem/           # Post-Mortem de Incidentes
|   |-- system-prompt-spec/    # Especificacion de Agente LLM
|   '-- diagramas/             # Generacion de diagramas C4
|
|-- templates/                 # Plantillas de artefactos
|   |-- _frontmatter.md        # Frontmatter YAML comun
|   |-- rfc.md
|   |-- adr-madr.md            # Formato MADR 4.0
|   |-- adr-nygard.md          # Formato Nygard lightweight
|   |-- prd.md
|   |-- tech-spec.md
|   |-- system-design.md
|   |-- runbook.md
|   |-- post-mortem.md
|   |-- system-prompt-spec.md
|   |-- context-map.md         # DDD Context Map
|   '-- fitness-functions.md   # Architecture Fitness Functions
|
|-- references/                # Material de referencia
|   |-- bibliografia.md        # 20+ estandares citados
|   |-- manifiesto.md          # Anti-vibecoding
|   |-- scope-sa-vs-swa.md     # SA vs Software Architect
|   |-- niveles-madurez.md     # Draft -> Approved -> Superseded
|   |-- matriz-decision.md     # Que artefactos por tipo de proyecto
|   |-- protocolo-iteracion.md # Metodologia specs-driven
|   |-- nfr-taxonomia.md       # ISO 25010 + Quality Attribute Scenarios
|   |-- patrones-integracion.md # Patrones a nivel de politica SA
|   |-- diagramas-estrategia.md # Excalidraw vs Mermaid por artefacto
|   |-- c4-guia.md             # C4 Model para SA (L1-L2)
|   '-- mcp-excalidraw-guia.md # Guia practica del MCP server
|
|-- mcp-excalidraw/            # Excalidraw MCP server (integrado)
|   |-- libs/                  # Librerias C4 + software architecture
|   '-- excalidraw-skill/      # Skill, scripts CLI y cheatsheet
|
'-- examples/                  # Ejemplos completos
    '-- inversion-pasiva/      # Plataforma de inversion en renta fija
        |-- RFC-001.md
        |-- ADR-001.md
        |-- TS-001.md
        '-- c4-container-diagram.excalidraw
```

---

## Artefactos: que aporta el SA en cada uno

| Artefacto | El SA define | NO define (scope de otros) |
|---|---|---|
| **RFC** | Problema, opciones, recomendacion, riesgos | Detalles de implementacion |
| **ADR** | Decision, justificacion, consecuencias | Configuracion especifica |
| **PRD** | NFRs cuantificados, restricciones, scope | Features detalladas (Product Owner) |
| **Tech Spec** | Stack, contratos de integracion, fitness functions | Patrones de codigo, estructura de clases |
| **System Design** | SLOs, STRIDE, escalabilidad, deployment logico | Infra fisica, CI/CD pipelines |
| **Runbook** | Requisitos operacionales, metricas criticas, SLAs | Procedimientos paso a paso (Operations) |
| **Post-Mortem** | Facilitacion, causa raiz sistemica, acciones | Fixes de codigo |
| **System Prompt Spec** | Allowlist, denylist, compliance, test cases | Fine-tuning, prompt engineering avanzado |

---

## Estandares de referencia

Todos los artefactos estan alineados con estandares documentados en `references/bibliografia.md`:

| Estandar | Aplicabilidad |
|---|---|
| **TOGAF 10th Ed** (The Open Group, 2022) | Gobernanza, ADM, Architecture Building Blocks |
| **ISO/IEC/IEEE 42010:2022** | Estructura de descripciones de arquitectura |
| **C4 Model** (Simon Brown) | Notacion de diagramas (L1 Context, L2 Container) |
| **Arc42 v8** (Starke & Hruschka) | Template de documentacion |
| **MADR 4.0** (Kopp et al., 2024) | Formato de ADR |
| **ISO/IEC 25010:2023** (SQuaRE) | Taxonomia de atributos de calidad |
| **Building Evolutionary Architectures** (Ford, Parsons, Kua, 2023) | Fitness functions, arquitectura incremental |
| **Domain-Driven Design** (Evans, Vernon, Khononov) | Bounded contexts, context mapping |
| **Google SRE Book** (Beyer et al., 2016) | Post-mortem blameless, SLIs/SLOs |
| **STRIDE** (Microsoft) | Modelo de amenazas de seguridad |
| **Team Topologies** (Skelton, Pais, 2019) | Alineacion equipo-arquitectura |

---

## Principio Anti-Vibecoding

> Si no puedes explicar en un parrafo que problema resuelve lo que estas
> a punto de construir, no estas listo para construir.

Este framework existe para: **Pensar antes de construir. Documentar antes de codear. Decidir antes de implementar.**

Ver `references/manifiesto.md` para el manifiesto completo.

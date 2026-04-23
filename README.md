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
  0. Context Brief           "Cual es el problema y el contexto?"
     |                       (OBLIGATORIO antes de cualquier artefacto)
     |
  1. RFC                     "Que opciones tenemos y cual recomendamos?"
     |
  2. ADR                     "Que decisiones tomamos y por que?"
     |
  3. PRD                     "Que funcionalidades exactamente?"
     |
  4. Tech Spec + Diagramas   "Con que tecnologias y como se integran?"
     |                       (Diagrama C4 Level 2 via Excalidraw MCP)
     |
  5. System Design           "Como escala, como es seguro?"
     |
  6. Req. Operacionales (*)  "Que necesita Operations para operar?"
     |
  7. Post-Mortem (**)        "Que aprendimos cuando fallo?"

  (*) El SA define REQUISITOS operacionales; Operations redacta los procedimientos
  (**) Solo cuando ocurre un incidente
```

### Regla de oro: iteracion sobre perfeccion

> Un RFC Draft entregado hoy tiene mas valor que un RFC perfecto que nunca se publica.

Los artefactos maduran de Draft a Approved conforme avanza la comunicacion con los equipos.
No esperar a tener toda la informacion para empezar a escribir.

### Si el sistema incluye un agente LLM:
Agregar **System Prompt Spec** en paralelo con la Tech Spec.

### Excepciones validas al orden:
- Decision urgente que bloquea al equipo → empezar con **ADR**
- Incidente en produccion → empezar con **Post-Mortem**
- Spike tecnico → **RFC lite** (version reducida)
- Integracion con tercero → agregar **Context Map** en paralelo

---

## Como usar este framework (guia para arquitectos)

Este framework funciona como un **asistente de IA** que te guia paso a paso.
Tu le das el contexto de negocio, y la IA genera borradores de artefactos
que tu revisas, corriges y apruebas. Tu sigues siendo el arquitecto — la IA
es tu asistente.

**El punto de entrada SIEMPRE es el orquestador (`/orquestador`).**
El orquestador te guia por todas las fases: captura de contexto, seleccion
de artefactos, creacion, critica y diagramas. No necesitas cargar skills
individuales manualmente — el orquestador lo hace por ti.

### Prerequisito: elegir tu herramienta de IA

| Herramienta | Donde se usa | Como se instala |
|---|---|---|
| **Claude Code** (recomendado) | Terminal o VS Code | `npm install -g @anthropic-ai/claude-code` |
| **GitHub Copilot** | VS Code, JetBrains | Extension de Copilot + Copilot Chat |
| **Cursor** | Editor Cursor | Ya incluido |

### Con Claude Code (recomendado)

Claude Code lee automaticamente `CLAUDE.md` y conoce todos los skills.

```bash
# 1. Clonar este repositorio
git clone https://github.com/MAKERS-SAS-ORG/arquitectureflow.git
cd arquitectureflow

# 2. Abrir Claude Code
claude

# 3. Iniciar el orquestador — SIEMPRE es el punto de entrada
```

**Que decirle a Claude:**

```
> /orquestador
  → Inicia el flujo completo. Claude te pedira el Context Brief (Fase 0),
    seleccionara artefactos (Fase 1), y te guiara por cada uno.

> "Necesito disenar la arquitectura de un nuevo sistema de inversiones"
  → Claude carga el orquestador automaticamente, empieza por el Context Brief

> /orquestador — ya tengo el CB-001 listo, quiero crear el RFC
  → Claude valida que CB-001 existe y carga el skill de RFC

> /orquestador — critica el RFC-001
  → Claude aplica la Fase 4 (critica automatica con 🔴🟡🟢)

> /orquestador — genera diagrama C4 para la Tech Spec
  → Claude carga el skill de diagramas y usa Excalidraw MCP
```

### Con GitHub Copilot

Copilot no tiene `/orquestador` nativo, pero puedes simular el flujo
referenciando el skill del orquestador en Copilot Chat:

```
# Paso 1: Iniciar con el orquestador
@workspace Lee skills/orquestador/SKILL.md y guiame desde la Fase 0.
Necesito disenar un sistema de pagos.

# Paso 2: El orquestador te pedira el Context Brief
@workspace Lee templates/context-brief.md y ayudame a llenarlo
con el contexto que te acabo de dar.

# Paso 3: El orquestador selecciona artefactos y carga cada skill
@workspace Segun el Context Brief CB-001 y references/matriz-decision.md,
que artefactos necesito? Empieza con el primero.

# Paso 4: Para cada artefacto siguiente
@workspace Sigue con el siguiente artefacto del flujo del orquestador.
```

### Con Cursor

Cursor lee `CLAUDE.md` automaticamente:

```
1. Abrir el proyecto en Cursor
2. En el chat: "/orquestador — necesito disenar un nuevo sistema"
3. Cursor seguira el flujo del orquestador
```

---

## Flujo guiado por el orquestador

Cuando escribes `/orquestador`, la IA ejecuta estas fases en orden:

### Fase 0: Context Brief (OBLIGATORIO)
La IA te hace preguntas de contexto y genera `CB-NNN.md`:
- Problema de negocio (max 2 oraciones)
- Stakeholders y gobernanza
- Restricciones tecnicas
- Scope IN/OUT

> Sin Context Brief aprobado, no se crea ningun otro artefacto.

### Fase 1: Seleccion de artefactos
La IA consulta `references/matriz-decision.md` y te dice:
- Que artefactos son obligatorios (MUST) para tu tipo de proyecto
- Que artefactos son recomendados (SHOULD)
- En que orden crearlos

### Fase 2: Creacion iterativa
Para cada artefacto, la IA:
1. Carga el skill correspondiente (`skills/[nombre]/SKILL.md`)
2. Carga la plantilla (`templates/[nombre].md`)
3. Genera un borrador basado en tu Context Brief
4. Marca con 🔴 TODO lo que necesita tu validacion

> No necesitas tenerlo perfecto — un Draft con TODOs tiene mas valor que nada.

### Fase 3: Critica automatica
Despues de cada artefacto, la IA actua como arquitecto esceptico:
- Encuentra minimo 3 problemas
- Clasifica: 🔴 Critico | 🟡 Importante | 🟢 Sugerencia

### Fase 4: Diagramas C4
Cuando un artefacto necesita diagrama (Tech Spec, System Design):
- La IA carga `skills/diagramas/SKILL.md`
- Genera el diagrama con Excalidraw MCP server (L1 o L2 segun el artefacto)
- Tu lo revisas en http://localhost:3000

### Fase 5: Siguiente artefacto
La IA verifica consistencia entre artefactos y te guia al siguiente.
El ciclo se repite hasta que el checklist de aprobacion esta completo.

### Para diagramas: iniciar el canvas Excalidraw
```bash
# Solo necesario cuando vas a generar diagramas (Fase 4)
cd /ruta/a/mcp_excalidraw && PORT=3000 npm run canvas
# Abrir http://localhost:3000 en el navegador para ver el canvas en vivo
```

---

## Skills con Tessl (opcional — evaluacion y distribucion)

[Tessl](https://tessl.io) es el package manager para skills de agentes IA.
Permite instalar, versionar y evaluar skills compatibles con Claude, Copilot y Cursor.

### Skills relevantes en el registro de Tessl

| Skill | Que hace | Score |
|---|---|---|
| [c4-architecture](https://tessl.io/registry/skills/github/softaworks/agent-toolkit/c4-architecture) | Genera diagramas C4 en Mermaid con workflow de 4 pasos | Quality: 86%, Impact: 95% |
| [architecture-patterns](https://tessl.io/registry/skills/github/secondsky/claude-skills/architecture-patterns) | Clean Architecture, Hexagonal, DDD patterns | Quality: 52% (en mejora) |

### Como usar Tessl para evaluar y distribuir skills

```bash
# Instalar Tessl
curl -fsSL https://get.tessl.io | sh
tessl login

# Inicializar en tu proyecto (detecta Claude Code y Copilot automaticamente)
cd arquitectureflow
tessl init

# Buscar skills de arquitectura
tessl search architecture
tessl search "C4 model"

# Instalar un skill del registro
tessl install softaworks/agent-toolkit --skill c4-architecture

# Listar skills instalados
tessl list
```

### Evaluar nuestros skills con Tessl

Tessl permite evaluar la calidad de skills propios contra metricas objetivas:
```bash
# Evaluar un skill local
tessl skill review --optimize ./skills/rfc/SKILL.md
tessl skill review --optimize ./skills/tech-spec/SKILL.md
```

### Publicar skills al registro (futuro)
Si quieres compartir los skills de ArquitectureFlow con otros arquitectos:
```bash
tessl publish ./skills/orquestador
```

Ver registro completo en: https://tessl.io/registry

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
|   |-- context-brief.md       # Context Brief (Fase 0 — OBLIGATORIO)
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
        |-- CB-001.md          # Context Brief (Fase 0)
        |-- RFC-001.md         # Request for Comments
        |-- ADR-001.md         # Decision: event-driven con SQS
        |-- PRD-001.md         # Product Requirements + QA scenarios
        |-- TS-001.md          # Tech Spec + contratos
        |-- SD-001.md          # System Design + STRIDE
        |-- RO-001.md          # Requisitos Operacionales
        |-- CM-001.md          # Context Map DDD
        |-- FF-001.md          # Fitness Functions
        '-- c4-container-diagram.excalidraw
```

---

## Artefactos: que aporta el SA en cada uno

| Artefacto | El SA define | NO define (scope de otros) |
|---|---|---|
| **Context Brief** | Problema, stakeholders, restricciones, scope IN/OUT | -- (es 100% SA) |
| **RFC** | Opciones, recomendacion, riesgos, plan de rollback | Detalles de implementacion |
| **ADR** | Decision, justificacion, consecuencias, validacion | Configuracion especifica |
| **PRD** | NFRs cuantificados, quality attribute scenarios, scope | Features detalladas (Product Owner) |
| **Tech Spec** | Stack, contratos de integracion, politicas de solucion | Patrones de codigo, estructura de clases |
| **System Design** | SLOs, STRIDE, escalabilidad, deployment logico | Infra fisica, CI/CD pipelines |
| **Fitness Functions** | Que medir, umbrales, que bloquea deploy | Implementacion de tests automatizados |
| **Req. Operacionales** | Metricas criticas, SLAs, criterios de rollback | Procedimientos paso a paso (Operations) |
| **Context Map** | Bounded contexts, patrones de integracion DDD | Implementacion de ACL, adapters |
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

# Ejemplo: Plataforma de Inversion en Renta Fija

Este ejemplo muestra el flujo completo de ArquitectureFlow aplicado a un caso real:
una plataforma fintech de inversion en CDTs para personas naturales en Colombia.

---

## Como se creo este ejemplo (paso a paso con el orquestador)

### 1. Inicio: `/orquestador`

Se inicio el flujo con el orquestador. Claude leyo `CLAUDE.md`, cargo
`skills/orquestador/SKILL.md` y empezo por la Fase 0.

```
Arquitecto: /orquestador
            Necesito disenar la arquitectura de una plataforma de inversion
            en renta fija para personas naturales en Colombia.

Claude:     Vamos a empezar con el Context Brief (Fase 0).
            Te voy a hacer algunas preguntas...
```

### 2. Fase 0 → CB-001.md (Context Brief)

El orquestador cargo `templates/context-brief.md` y guio al arquitecto
por los 5 bloques: negocio, stakeholders, tecnico, IA/compliance, scope.

```
Claude:     Cual es el problema principal? (max 2 oraciones)
Arquitecto: El 78% de los colombianos con capacidad de ahorro no invierte
            porque los CDTs requieren montos minimos altos...

Claude:     [genera CB-001.md como Draft]
            Revisa el Context Brief. Hay algo que corregir?

Arquitecto: Aprobado.
Claude:     CB-001 → estado: Approved.
            Segun la matriz de decision, para un sistema greenfield completo
            necesitas: RFC, ADR, PRD, Tech Spec, System Design,
            Req. Operacionales, Context Map, Fitness Functions.
            Empezamos con el RFC?
```

**Resultado:** `CB-001.md` — Context Brief Approved

### 3. Fase 2 → RFC-001.md (Request for Comments)

El orquestador cargo `skills/rfc/SKILL.md` + `templates/rfc.md` y genero
el RFC basado en el contexto de CB-001.

```
Claude:     Cargo el skill de RFC. Basado en CB-001, el problema es...
            Genero 3 opciones incluyendo "No hacer nada".
            [genera RFC-001.md como Draft]

            Fase 4 — Critica automatica:
            🔴 Falta cuantificar el costo de oportunidad con fuente
            🟡 El plan de rollback es generico, especificar mecanismo
            🟢 Agregar benchmark de competidores con datos publicos

Arquitecto: [corrige los puntos criticos]
            Aprobado.
```

**Resultado:** `RFC-001.md` — RFC Approved (opcion C: plataforma propia)

### 4. Fase 2 → ADR-001.md (Architecture Decision Record)

El orquestador identifico que la decision "event-driven vs sincrono"
necesita ADR. Cargo `skills/adr/SKILL.md` + `templates/adr-madr.md`.

```
Claude:     La decision mas critica del RFC es el patron de comunicacion.
            Los proveedores externos (Deceval, PSE) tienen latencias de
            1-30 segundos. Recomiendo ADR con formato MADR.
            [genera ADR-001.md]

Arquitecto: Aceptado. La justificacion tecnica es correcta.
```

**Resultado:** `ADR-001.md` — ADR Accepted (event-driven con SQS)

### 5. Fase 2 → PRD-001.md (Product Requirements)

```
Claude:     Cargo el skill de PRD. Basado en CB-001 y RFC-001...
            Genero 4 casos de uso, user stories en Gherkin,
            3 Quality Attribute Scenarios (ISO 25010), y reglas de negocio.
            [genera PRD-001.md como Draft]

            🔴 TODO: RN-007 monto maximo sin aprobacion — validar con Compliance
            🔴 TODO: RN-008 inversiones recurrentes — validar con Product Owner

Arquitecto: Bien. Queda en Review hasta resolver los TODOs.
```

**Resultado:** `PRD-001.md` — PRD en Review (con TODOs pendientes)

### 6. Fase 2 → TS-001.md (Tech Spec)

```
Claude:     Cargo el skill de Tech Spec. Stack basado en restricciones de
            CB-001 (equipo .NET, AWS, presupuesto $1.200M)...
            Contratos de integracion con Deceval, PSE, KYC.
            Politicas SA (JWT 15min, Secrets Manager, idempotencia).
            [genera TS-001.md como Draft]

            🔴 TODO: Falta ADR formal para eleccion de PostgreSQL
            🔴 TODO: SLA con Deceval pendiente de firma

            Fase 4 — Diagramas: este artefacto necesita C4 Level 2.
            Cargo skills/diagramas/SKILL.md...
```

**Resultado:** `TS-001.md` — Tech Spec en Review + `c4-container-diagram.excalidraw`

### 7. Fase 4 → Diagrama C4 Level 2 (Excalidraw MCP)

```
# Se inicio el canvas server
cd /Users/themakers/mcp_excalidraw && PORT=3000 npm run canvas

Claude:     Creo el diagrama via REST API del MCP server:
            - Batch 1: titulo + persona (Inversionista)
            - Batch 2: boundary + 6 containers internos
            - Batch 3: 3 sistemas externos (Deceval, PSE, SFC)
            - Batch 4: 10 flechas con protocolos
            Snapshot guardado como "c4-inversion-pasiva-v1"
            Exportado a c4-container-diagram.excalidraw (54 elementos)

Arquitecto: [revisa en http://localhost:3000] Aprobado.
```

**Resultado:** `c4-container-diagram.excalidraw` — 54 elementos, C4 Level 2

### 8. Fase 2 → SD-001.md, RO-001.md, CM-001.md, FF-001.md

```
Claude:     Siguientes artefactos segun la secuencia:

            SD-001 (System Design): STRIDE, SLAs, escalabilidad, SPOFs,
            observabilidad. Referencia a TS-001 y PRD-001 NFRs.
            → Draft (SPOFs pendientes de negociacion)

            RO-001 (Req. Operacionales): Metricas criticas, umbrales,
            criterios de rollback, SLAs de externos.
            → Draft

            CM-001 (Context Map DDD): 5 bounded contexts, patrones
            ACL/Conformist/Published Language, 7 domain events.
            → Draft

            FF-001 (Fitness Functions): 6 FFs como contrato verificable.
            Cada una traza a un NFR del PRD o restriccion del CB.
            → Draft (pendiente implementacion por ingenieria)
```

**Resultado:** 4 artefactos Draft completando el flujo

### 9. Fase 7 → TAA-001.md (Tablero de Adherencia Arquitectonica)

```
Claude:     Cargo templates/tablero-adherencia.md.
            Consolido el estado de todos los artefactos, genero el mapa
            de trazabilidad (decision → modulo → validacion), defino
            gates de revision por sprint y enlazo el dashboard de FF.
            [genera TAA-001.md como Draft]

Arquitecto: Reviso con el Tech Lead. Acordamos gates de revision
            en sprint planning y code review arquitectonico.
```

**Resultado:** `TAA-001.md` — Tablero de Adherencia (documento vivo)

---

## Mapa de artefactos y como se conectan

```
CB-001 (Approved)
  Contexto, restricciones, scope
  |
  ├── RFC-001 (Approved)
  |     Problema, opciones, recomendacion
  |     |
  |     ├── ADR-001 (Accepted)
  |     |     Decision: event-driven con SQS
  |     |
  |     └── PRD-001 (Review — tiene 🔴 TODOs)
  |           Casos de uso, NFRs, reglas de negocio
  |           |
  |           └── TS-001 (Review — tiene 🔴 TODOs)
  |                 Stack, contratos, politicas SA
  |                 |
  |                 ├── c4-container-diagram.excalidraw
  |                 |     Diagrama C4 L2 (54 elementos)
  |                 |
  |                 ├── SD-001 (Draft)
  |                 |     STRIDE, SLAs, escalabilidad, SPOFs
  |                 |
  |                 ├── RO-001 (Draft)
  |                 |     Metricas, rollback, SLAs externos
  |                 |
  |                 ├── CM-001 (Draft)
  |                 |     5 bounded contexts, 7 domain events
  |                 |
  |                 └── FF-001 (Draft)
  |                       6 fitness functions como contrato
  |
  └── TAA-001 (Draft — documento vivo)
        Estado de artefactos, trazabilidad, gates de revision,
        desviaciones, dashboard de FF
```

## Que demuestra este ejemplo

1. **Trazabilidad completa:** cada artefacto referencia a CB-001 en `artefactos-origen`
2. **Iteracion en practica:** PRD y TS tienen 🔴 TODOs reales, no estan "perfectos"
3. **Scope SA claro:** TS-001 tiene "SA define politica | SWA implementa"
4. **Fitness Functions como contrato:** FF-001 traza cada FF a un NFR del PRD
5. **Diagramas C4 solo L1/L2:** el SA no creo diagramas L3/L4
6. **Tablero de Adherencia:** TAA-001 conecta decisiones con modulos de implementacion
7. **Orquestador como guia:** todo el flujo fue dirigido por `/orquestador`

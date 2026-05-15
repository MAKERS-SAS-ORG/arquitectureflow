# Frontmatter Comun para Artefactos

Todos los artefactos de ArquitectureFlow MUST incluir este YAML frontmatter al inicio.
Copiar y adaptar para cada artefacto nuevo.

```yaml
---
titulo: "[Nombre descriptivo del artefacto]"
identificador: "[TIPO]-[NNN]"    # Ej: RFC-001, ADR-003, PRD-001
tipo: RFC | ADR | PRD | Tech-Spec | API-Design | System-Design | Runbook | Post-Mortem | System-Prompt-Spec | Context-Map | Fitness-Functions | Stakeholder-Map | Tablero-Adherencia
estado: Draft | Review | Approved | Superseded
version: "1.0.0"
autor: "[Nombre del autor]"
fecha-creacion: YYYY-MM-DD
fecha-ultima-revision: YYYY-MM-DD
revisores: []               # Lista de nombres de revisores
decision-esperada: YYYY-MM-DD  # Fecha limite para decision (solo RFC)
estimacion-esfuerzo: S | M | L | XL  # S(<1sem), M(1-2sem), L(2-4sem), XL(>4sem)
supersede: null             # Identificador del artefacto que este reemplaza
superseded-by: null         # Identificador del artefacto sucesor
artefactos-origen: []       # Ej: [RFC-001, ADR-002]
stakeholders: []
firmas-roles: []            # Evidencia auditable. Lista de {rol, persona, fecha, nota}.
                            # Obligatorio para artefactos en sectores regulados.
                            # Ej:
                            #   - rol: Acelerador
                            #     persona: "Juan Perez"
                            #     fecha: 2026-05-07
                            #     nota: "Aprueba ROI y deadline"
                            #   - rol: Especialista Tecnico
                            #     persona: "@tech-lead"
                            #     fecha: 2026-05-08
                            #     nota: "Valida viabilidad tecnica"
tags: []
---
```

## Campos por Tipo

| Campo | RFC | ADR | PRD | Tech Spec | System Design | Runbook | Post-Mortem | System Prompt Spec |
|---|---|---|---|---|---|---|---|---|
| decision-esperada | MUST | -- | -- | -- | -- | -- | -- | -- |
| estimacion-esfuerzo | MUST | -- | SHOULD | SHOULD | -- | -- | -- | -- |
| revisores | MUST | MUST | MUST | MUST | MUST | SHOULD | MUST | MUST |
| artefactos-origen | -- | MUST (RFC) | MUST (RFC) | MUST (PRD, ADRs) | MUST (Tech Spec) | MUST (System Design) | -- | MUST (PRD) |
| severidad | -- | -- | -- | -- | -- | -- | MUST | -- |
| nivel-riesgo | -- | -- | -- | -- | -- | -- | -- | MUST |
| firmas-roles | SHOULD | SHOULD | SHOULD | SHOULD | SHOULD | SHOULD | -- | **MUST** |

## Campo `firmas-roles` (evidencia auditable)

Captura quien firmo el artefacto desde cada rol colaborador (ver bloque
"Roles colaboradores" en cada template).

**Cuando es MUST:**
- Sistemas regulados (financiero, salud, gobierno, datos personales sensibles).
- Componentes con LLM (System Prompt Spec) — Compliance MUST firmar.
- Cualquier artefacto que avance a estado **Approved** en sectores con auditoria externa.

**Cuando es SHOULD:**
- Artefactos en estado Approved fuera de sectores regulados.
- En estados Draft/Review puede dejarse vacio (`[]`).

**Reglas de uso:**
- Cada firma es un objeto: `{rol, persona, fecha, nota}`.
- El SA NO debe declarar un artefacto **Approved** sin tener firma del rol principal
  indicado en el bloque "Roles colaboradores" del template.
- Las firmas son apend-only: NO se borran. Si una firma queda obsoleta, agregar
  una nueva con `nota: "Reemplaza firma del YYYY-MM-DD"` y dejar la anterior.

**Mapeo recomendado rol principal → artefacto:**

| Artefacto | Rol que MUST firmar para Approved |
|---|---|
| Context Brief | Acelerador (Sponsor / PO) |
| RFC | Acelerador + Especialista Tecnico |
| ADR | Especialista Tecnico |
| PRD | Acelerador + QA (+ Responsable de Seguridad si hay PII / datos sensibles) |
| Tech Spec | Especialista Tecnico |
| API Design REST (OpenAPI 3.1) | Especialista Tecnico + **Responsable de Seguridad** (auth, scopes, PII) |
| API Design GraphQL | Especialista Tecnico + **Responsable de Seguridad** + Front-end Tech Lead |
| System Design | DevOps + Especialista Tecnico + **Responsable de Seguridad (STRIDE) — bloqueante si hay datos sensibles o regulación** |
| Req. Operacionales | DevOps (+ Responsable de Seguridad para incident response / accesos privilegiados) |
| Tablero Adherencia | Tech Lead + DevOps + QA + Responsable de Seguridad (cada gate firma su seccion) |
| System Prompt Spec | **Compliance** (bloqueante) + Especialista Tecnico + QA + **Responsable de Seguridad** (adversarial / prompt injection) |
| Stakeholder Map | Acelerador / Sponsor |

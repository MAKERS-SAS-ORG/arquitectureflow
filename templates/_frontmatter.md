# Frontmatter Comun para Artefactos

Todos los artefactos de ArquitectureFlow MUST incluir este YAML frontmatter al inicio.
Copiar y adaptar para cada artefacto nuevo.

```yaml
---
titulo: "[Nombre descriptivo del artefacto]"
identificador: "[TIPO]-[NNN]"    # Ej: RFC-001, ADR-003, PRD-001
tipo: RFC | ADR | PRD | Tech-Spec | System-Design | Runbook | Post-Mortem | System-Prompt-Spec | Context-Map | Fitness-Functions
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

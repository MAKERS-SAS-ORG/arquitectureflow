# Niveles de Madurez de Artefactos

> Referencia: Ford, N.; Parsons, R.; Kua, P. *Building Evolutionary Architectures.* 2nd Ed. O'Reilly, 2023.
> Principio: La arquitectura evoluciona. Los artefactos son documentos vivos, no fosiles.

---

## Estados

| Estado | Significado | Quien transiciona |
|---|---|---|
| **Draft** | Trabajo en progreso. Puede cambiar radicalmente. | Autor |
| **Review** | Listo para feedback de stakeholders y revisores. | Autor -> Revisores |
| **Approved** | Aceptado como referencia para la arquitectura. | Revisores -> Arquitecto SA |
| **Superseded** | Reemplazado por una version nueva. MUST enlazar al sucesor. | Arquitecto SA |

## Transiciones Validas

```
Draft ──> Review ──> Approved ──> Superseded
  |                                    ^
  └──────────────────────────────────┘  (cancelado antes de aprobacion)

Approved ──> Draft  (reabierto para revision mayor)
```

## Frontmatter de Madurez

Cada artefacto MUST incluir en su YAML frontmatter:

```yaml
---
titulo: "[Nombre del Artefacto]"
tipo: RFC | ADR | PRD | Tech-Spec | System-Design | Runbook | Post-Mortem | System-Prompt-Spec
estado: Draft | Review | Approved | Superseded
version: "1.0.0"
autor: "[nombre]"
fecha-creacion: YYYY-MM-DD
fecha-ultima-revision: YYYY-MM-DD
supersede: null          # enlace al artefacto que este reemplaza
superseded-by: null      # enlace al artefacto sucesor
stakeholders: []
tags: []
---
```

## Reglas de Versionamiento

- **Patch (1.0.x):** Correcciones menores de redaccion, typos, clarificaciones
- **Minor (1.x.0):** Adiciones que no cambian decisiones existentes
- **Major (x.0.0):** Cambios que alteran decisiones o scope fundamentales

## Triggers de Refactoring

Un artefacto SHOULD revisarse cuando:

| Trigger | Ejemplo | Accion |
|---|---|---|
| Cambio en requisitos de negocio | Nuevo mercado, nuevo regulador | Revisar RFC, PRD, System Design |
| Nuevo ADR que contradice decision previa | ADR-005 supersede ADR-002 | Actualizar Tech Spec, System Design |
| Post-mortem revela fallos de diseno | SPOF no mitigado | Actualizar System Design, Runbook |
| Cambio de tecnologia o proveedor | Migracion de AWS a Azure | Revisar Tech Spec, ADRs, Runbook |
| Umbral de escala superado | 10x usuarios en 6 meses | Revisar System Design capacity planning |
| Cambio organizacional | Merger, nuevo equipo | Revisar scope boundaries, Context Map |

## Cadena de Supersesion

Los artefactos NUNCA se borran — se superseden:

1. Crear nuevo artefacto (ej: ADR-005)
2. En ADR-005 frontmatter: `supersede: ADR-002`
3. En ADR-002 frontmatter: `superseded-by: ADR-005`, `estado: Superseded`
4. La historia de decisiones es tan valiosa como las decisiones actuales

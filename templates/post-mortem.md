---
titulo: "Post-Mortem: [Titulo descriptivo del incidente]"
identificador: PM-[NNN]
tipo: Post-Mortem
estado: Draft
version: "1.0.0"
autor: "[Nombre]"
fecha-creacion: YYYY-MM-DD
fecha-ultima-revision: YYYY-MM-DD
revisores: []
severidad: P1 | P2 | P3
firmas-roles: []   # SHOULD firmas de Oncall + Tech Lead. Ver _frontmatter.md
tags: []
---

# Post-Mortem: [Titulo]

## Roles colaboradores

> El SA facilita la sesion blameless y firma la causa raiz sistemica.
> Los datos vienen de **DevOps** (timeline tecnico) y del **Equipo de Desarrollo**
> (acciones correctivas). Ver diagrama de roles en `README.md`.

| Rol | Que aporta al SA | Cuando consultarlo |
|---|---|---|
| **DevOps / SRE / Oncall** | Timeline exacto del incidente, alertas, primeras acciones de mitigacion, evidencia de monitoring | Seccion 2 (timeline) y header de severidad |
| **Equipo de Desarrollo** | Detalle tecnico del fallo, accion correctiva proxima (fix de codigo, parche), dueno de cada tarea | Secciones 5-6 (lo que no funciono, acciones correctivas) |
| **Especialista Tecnico** (SWA) | Validar que la causa raiz sistemica es real (no solo proxima) y proponer cambios estructurales | Seccion 3 (5 Por Ques) — el SA insiste, el SWA aterriza |
| **Acelerador / PO** | Si hubo impacto a clientes, comunicacion externa y compromiso de mejora | Seccion 7 (lecciones aprendidas) y comunicacion downstream |

| Campo | Valor |
|---|---|
| Fecha del incidente | YYYY-MM-DD HH:MM UTC-5 |
| Duracion | [X horas Y minutos] |
| Severidad | P1 (caido) / P2 (degradado) / P3 (parcial) |
| Sistemas afectados | [lista] |
| Usuarios afectados | [numero o porcentaje] |

## 1. Resumen Ejecutivo
> Maximo 5 oraciones: que paso, cuanto duro, cuanto impacto y causa raiz.

## 2. Timeline

| Hora | Evento |
|---|---|
| HH:MM | [evento] |

## 3. Root Cause Analysis (5 Por Ques)

1. **Por que [sintoma]?** Porque [causa 1]
2. **Por que [causa 1]?** Porque [causa 2]
3. **Por que [causa 2]?** Porque [causa 3]
4. **Por que [causa 3]?** Porque [causa 4]
5. **Por que [causa 4]?** Porque [causa raiz sistemica]

**Causa raiz sistemica:** [descripcion]

## 4. Lo Que Funciono Bien
- [aprendizaje positivo]

## 5. Lo Que No Funciono
- [aprendizaje de mejora]

## 6. Acciones Correctivas

| Accion | Dueno | Fecha limite | Ticket |
|---|---|---|---|
| [accion] | [persona] | YYYY-MM-DD | #XXXX |

## 7. Lecciones Aprendidas
> Resumen para compartir en la reunion de equipo.

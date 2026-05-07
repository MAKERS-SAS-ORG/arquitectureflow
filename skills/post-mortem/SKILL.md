# Skill: Post-Mortem — Aprendizaje de Incidentes
# Version: 2026.2

> Referencia: Google SRE Book, Capitulo 15 — Postmortem Culture — `references/bibliografia.md#sre`
> Principio Blameless: "Por que el sistema permitio que esto pasara?" no "Quien rompio esto?"

---

## Proposito

Documentar que paso, por que, y que se va a cambiar para que no vuelva a pasar.
Cada incidente es una oportunidad de aprendizaje del sistema, no de culpar personas.

## Principios

1. **Blameless:** Buscar causas sistemicas, no culpables
2. **Accionable:** Cada post-mortem MUST terminar con acciones concretas con dueno y fecha

## Prerequisitos

- Context Brief del sistema afectado (si existe)
- No requiere otros artefactos previos — el Post-Mortem se crea por un incidente

## Roles colaboradores en este artefacto

> Ver bloque "Roles colaboradores" en `templates/post-mortem.md` y diagrama en `README.md`.
> El SA facilita; los datos vienen de DevOps y Equipo de Desarrollo.

| Rol | Que pedirle al consultarlo | En que paso del workflow |
|---|---|---|
| **DevOps / SRE / Oncall** | **Principal.** Timeline exacto, alertas, primeras acciones de mitigacion, evidencia de monitoring | Paso 1 (timeline) y campos de severidad/duracion |
| **Equipo de Desarrollo** | Detalle tecnico del fallo, accion correctiva proxima (fix, parche), dueno de cada tarea | Paso 3 (lo que no funciono) y Paso 4 (acciones correctivas) |
| **Especialista Tecnico** (SWA) | Validar que la causa raiz es **sistemica** (no solo proxima) y proponer cambios estructurales | Paso 2 (5 Por Ques) — el SA insiste, el SWA aterriza |
| **Acelerador / PO** | Si hubo impacto a clientes: comunicacion externa, compromisos de mejora | Paso 5 (lecciones para compartir) |

> Principio blameless: la culpa nunca es de personas, es del sistema que permitio el fallo.
> El SA modera para mantenerlo asi.

## Cuando Escribir

- Incidentes de severidad alta (sistema caido o degradado > 15 min)
- Incidentes que afectaron datos de usuarios
- Incidentes que violaron un SLA
- SIEMPRE dentro de las 48 horas — la memoria se degrada

## Workflow de Creacion

### Paso 1: Timeline
Reconstruir cronologia exacta: primera alerta, diagnostico, acciones, resolucion.

### Paso 2: Root Cause Analysis (5 Por Ques)
Encadenar preguntas "por que?" hasta llegar a la causa sistemica, no la causa proxima.

### Paso 3: Lo Que Funciono y Lo Que No
Aprendizaje positivo + aprendizaje de mejora.

### Paso 4: Acciones Correctivas
Acciones concretas con dueno, fecha limite y ticket de seguimiento.

### Paso 5: Lecciones para Compartir
Resumir para presentar al equipo en la reunion mas proxima.

## Plantilla

Usar `templates/post-mortem.md` como base.

## Diagramas

- **Timeline del incidente:** Mermaid timeline — SHOULD.

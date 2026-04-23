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

# Skill: System Design — Diseno del Sistema
# Version: 2026.2

> Referencia: TOGAF Fase D — Technology Architecture — `references/bibliografia.md#togaf`
> Referencia: STRIDE Threat Modeling — `references/bibliografia.md#stride`
> Referencia: Google SRE — SLIs/SLOs/SLAs — `references/bibliografia.md#sre`
> Referencia: DDD Context Mapping — `references/bibliografia.md#ddd`

---

## Proposito

Define como el sistema escala, como es seguro y como se comporta bajo carga y bajo fallo.
Mientras la Tech Spec define la estructura, el System Design define el **comportamiento operacional**.

## Cuando es Obligatorio

- Cualquier sistema que atienda trafico de produccion real
- Cualquier sistema con requerimientos de disponibilidad > 99%
- Cualquier sistema que maneje datos sensibles o financieros
- Cualquier sistema que integre con agentes LLM

## Prerequisitos

- Tech Spec aprobada (o al menos en Review)

## Workflow de Creacion

### Paso 1: Drivers de Arquitectura
- Requisitos de rendimiento (latencia, throughput) con escenarios medibles
- Disponibilidad y tolerancia a fallos (SLOs, RPO, RTO)
- Proyecciones de escalabilidad (hoy, 1 ano, 3 anos)

### Paso 2: Modelo de Amenazas (STRIDE)
Analisis sistematico de amenazas de seguridad:
- Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation of Privilege
- Cada amenaza con nivel de riesgo y mitigacion

### Paso 3: Dependencias Externas y SLAs
Documentar cada sistema externo con SLA contratado, timeout y fallback.

### Paso 4: Observabilidad
Logs, metricas, trazas, alertas. Metricas criticas con umbrales de alarma.

### Paso 5: SPOFs y Capacity Planning
Puntos de fallo unicos identificados con mitigacion actual y pendiente.
Plan de capacidad: recursos actuales, proyeccion, accion si se supera.

### Paso 6: Context Map (si aplica)
Si hay multiples bounded contexts o servicios, crear DDD Context Map.
Usar template `templates/context-map.md`.

## Plantilla

Usar `templates/system-design.md` como base.

## Diagramas

- **C4 L2 Container + Deployment:** MUST — Excalidraw.
- **Context Map DDD:** Excalidraw — si hay multiples bounded contexts.
- **Flujo de datos:** Mermaid flowchart — SHOULD.
- **STRIDE threat flow:** Mermaid — condicional.

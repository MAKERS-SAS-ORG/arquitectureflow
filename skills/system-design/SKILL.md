# Skill: System Design — Diseno del Sistema
# Version: 2026.3

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

- Context Brief aprobado (`CB-NNN` — Fase 0 del orquestador)
- Tech Spec aprobada (o al menos en Review)

## Roles colaboradores en este artefacto

> Ver bloque "Roles colaboradores" en `templates/system-design.md` y diagrama en `README.md`.

| Rol | Que pedirle al consultarlo | En que paso del workflow |
|---|---|---|
| **Responsable de Seguridad** (CISO / Security Architect / AppSec Lead) | **PRINCIPAL para Paso 2 (STRIDE) — LIDERA el modelado de amenazas en la fase de diseño y arquitectura.** Identifica amenazas por componente, evalúa riesgo, define mitigaciones, valida controles existentes y requisitos de auditoría | Paso 2 (STRIDE) — **bloqueante para Approved**. Cruzar con Paso 3 (dependencias externas) y Paso 4 (observabilidad de eventos de seguridad) |
| **DevOps / SRE / Infra** | **Principal para infraestructura.** Capacidad real, costos de auto-scaling, plataforma de observabilidad, viabilidad de SLOs declarados | Paso 1 (drivers — disponibilidad, escalabilidad), Paso 4 (observabilidad), Paso 5 (capacity planning) |
| **Especialista Tecnico** (SWA) | Despliegue logico (que corre donde), patrones de tolerancia a fallos, contraparte técnica del STRIDE para validar viabilidad de mitigaciones | Paso 2 (STRIDE — como soporte técnico al SEC), Paso 5 (SPOFs), Paso 6 (Context Map si aplica) |
| **QA** | Disenar load tests y chaos engineering que validan los NFRs antes de produccion; tests de seguridad automatizables | Paso 1 (rendimiento) — define como se prueba; Paso 2 (validación de mitigaciones STRIDE) |

> Sin DevOps el System Design es un PowerPoint. Sin Responsable de Seguridad el
> STRIDE es teatro. Si alguno no esta disponible, marcar 🔴 TODO en sus secciones
> y dejar el SD en Draft. **No se promueve a Approved sin firma del SEC en sec. 3.**

## Workflow de Creacion

### Paso 1: Drivers de Arquitectura
- Requisitos de rendimiento (latencia, throughput) con escenarios medibles
- Disponibilidad y tolerancia a fallos (SLOs, RPO, RTO)
- Proyecciones de escalabilidad (hoy, 1 ano, 3 anos)

### Paso 2: Modelo de Amenazas (STRIDE) — Liderado por el Responsable de Seguridad
Analisis sistematico de amenazas de seguridad — **el SEC lidera, el SA facilita, el SWA aporta detalle técnico**:
- Listar activos protegidos (PII, datos financieros, credenciales, etc.) y regulación aplicable
- Aplicar STRIDE **por componente** (no una sola tabla global): Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation of Privilege
- Cada amenaza con vector concreto, likelihood × impact = riesgo y mitigación trazada a ADR/TS/API/FF
- Firma del SEC obligatoria en `firmas-roles` antes de Approved

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

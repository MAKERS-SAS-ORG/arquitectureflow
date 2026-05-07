# Skill: Runbook — Requisitos Operacionales
# Version: 2026.3

> Referencia: Google SRE Book, Capitulo 10 — `references/bibliografia.md#sre`

---

## Proposito

Definir los REQUISITOS OPERACIONALES que el equipo de Operations/SRE necesita
para crear el runbook detallado. El SA NO redacta procedimientos paso a paso
— define QUE se debe operar, monitorear y proteger.

## Scope del SA en el Runbook

**SA define (este artefacto):**
- Metricas criticas y umbrales de alarma
- SLAs con sistemas externos
- Requisitos de deployment (blue-green, canary, rolling)
- Criterios de rollback
- Contactos de escalada y niveles de severidad
- Requisitos de gestion de cambios

**Operations/SRE define (fuera de scope):**
- Procedimientos paso a paso de despliegue
- Scripts de diagnostico y remediacion
- Configuracion de alertas en plataformas especificas
- Runbooks detallados con comandos especificos

## Principio: "4AM Test"

El SA se pregunta: "Si falla a las 4AM, el equipo de guardia tiene
suficiente informacion arquitectonica para entender el sistema?"
Si la respuesta es no, los requisitos operacionales estan incompletos.

## Prerequisitos

- Context Brief aprobado (`CB-NNN` — Fase 0 del orquestador)
- System Design aprobado (o en Review)

## Roles colaboradores en este artefacto

> Ver bloque "Roles colaboradores" en `templates/runbook.md` y diagrama en `README.md`.
> Sin **DevOps / SRE** este artefacto queda en abstracto — son los duenos operativos.

| Rol | Que pedirle al consultarlo | En que paso del workflow |
|---|---|---|
| **DevOps / SRE / Infra** | **Principal.** Health check viable, ventana de deployment realista, criterios de rollback automatizables, severidades del oncall, integracion con plataforma de monitoreo | Pasos 2-4 (deployment, rollback, metricas) |
| **Especialista Tecnico** (SWA) | Comportamiento esperado bajo cada metrica; dependencias internas que pueden fallar | Paso 4 (metricas) y Paso 6 (cambios que requieren aprobacion arq.) |
| **Vendor / Proveedores externos** | SLAs reales contratados, ventanas de mantenimiento, contactos de soporte | Paso 5 (dependencias externas) |
| **Compliance** | Politicas de cambio en sistemas regulados (SOX, PCI), evidencia auditable | Paso 6 si aplica |

> El SA define QUE operar; DevOps define COMO. Si no se puede coordinar con DevOps,
> el Runbook queda en estado "Requisitos Operacionales" y NO avanza a runbook completo.

## Workflow de Creacion

### Paso 1: Informacion del Sistema
URLs, endpoints, cuentas, dashboards de referencia.

### Paso 2: Requisitos de Deployment
Estrategia de deployment, criterios de health check, tiempo maximo de deployment.

### Paso 3: Criterios de Rollback
Condiciones que disparan rollback y como volver al estado anterior.

### Paso 4: Metricas Criticas
Que medir, que umbrales disparan alarma, a quien escalar.

### Paso 5: Dependencias y SLAs
Cada sistema externo con SLA, timeout esperado y comportamiento si falla.

### Paso 6: Gestion de Cambios
Politica de aprobaciones para cambios en produccion.

## Plantilla

Usar `templates/runbook.md` como base.

## Diagramas

- **Decision tree de escalada:** Mermaid flowchart — SHOULD.

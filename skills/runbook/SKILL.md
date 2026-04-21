# Skill: Runbook — Gestion de Operaciones en Produccion
# Version: 2026.2

> Referencia: Google SRE Book, Capitulo 10 — `references/bibliografia.md#sre`
> Principio: "4AM Test" — Si falla a las 4AM, puede la persona de guardia resolverlo leyendo el Runbook?

---

## Proposito

Guia de operaciones para que cualquier persona del equipo pueda operar,
diagnosticar y resolver problemas sin depender de conocimiento tribal.

## Cuando se Redacta

ANTES del primer despliegue a produccion. No despues.

## Prerequisitos

- System Design aprobado (o en Review)

## Workflow de Creacion

### Paso 1: Informacion del Sistema
URLs, endpoints, cuentas, dashboards — todo lo necesario para acceder.

### Paso 2: Proceso de Despliegue
Paso a paso del despliegue normal + checklist de verificacion post-despliegue.

### Paso 3: Rollback
Como deshacer un despliegue problematico. MUST ser ejecutable sin conocimiento previo.

### Paso 4: Operaciones Comunes
Procedimientos para tareas frecuentes (restart, cache invalidation, DB access).

### Paso 5: Diagnostico de Problemas
Para cada problema comun: sintoma, causa probable, diagnostico paso a paso, resolucion.

### Paso 6: Escalada
Contactos, canales, cuando escalar.

## Plantilla

Usar `templates/runbook.md` como base.

## Diagramas

- **Decision tree operacional:** Mermaid flowchart — SHOULD.

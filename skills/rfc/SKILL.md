# Skill: RFC — Request for Comments
# Version: 2026.2

> Referencia: RFC 2119 (Bradner, 1997) — Keywords MUST/SHOULD/MAY
> Referencia: TOGAF Fase Preliminary + Fase A — Architecture Vision
> Referencia: Ver `references/bibliografia.md#rfc2119` y `references/bibliografia.md#togaf`

---

## Proposito

Abrir la discusion sobre que problema existe y como podria resolverse.
El RFC NO es una decision. Es una propuesta formal para que el equipo
y stakeholders comenten.

## Pregunta Central

Una sola oracion: **"Debemos [hacer X] para [resolver Y] porque [Z]?"**
Si no puedes formularla, el problema no esta suficientemente entendido.

## Cuando Crear un RFC

- Cambio que afecta mas de un modulo, servicio o equipo
- Nueva capacidad con impacto en usuarios o en produccion
- Cambio dificil o costoso de revertir
- Integracion con un sistema externo nuevo
- Cualquier trabajo estimado en mas de 2 semanas

## Prerequisitos

- Context Brief aprobado (`CB-NNN` — Fase 0 del orquestador, `templates/context-brief.md`)
- El RFC es el primer artefacto DESPUES del Context Brief

## Roles colaboradores en este artefacto

> Ver bloque "Roles colaboradores" en `templates/rfc.md` y diagrama en `README.md`.

| Rol | Que pedirle al consultarlo | En que paso del workflow |
|---|---|---|
| **Acelerador** (Negocio) | Confirmar el problema, validar el costo de cada opcion, alinear urgencia con el deadline del CB | Paso 1 (formulacion) y Paso 3 (matriz, criterios de negocio) |
| **Especialista Tecnico** (SWA / Tech Lead) | Generar opciones tecnicas viables, anticipar riesgos no obvios, evaluar plan de rollback realista | Paso 2 (opciones), Paso 4 (riesgos y rollback) |
| **Compliance / Legal** | Solo si una opcion impacta regulacion | Paso 4 (impacto regulatorio) |

> Si el SA no consigue input de Acelerador o Especialista Tecnico, marcar 🔴 TODO en la
> seccion afectada y NO declarar el RFC en Review hasta cerrarlo.

## Workflow de Creacion

### Paso 1: Formulacion del Problema
Guiar al arquitecto a articular:
1. El problema en terminos de negocio (no tecnicos)
2. El costo cuantificado de no resolver
3. Por que ahora (urgencia o ventana de oportunidad)
4. Metricas de exito medibles

### Paso 2: Generacion de Opciones
MUST generar minimo 3 opciones incluyendo **"No hacer nada"**:
- La opcion "no hacer nada" obliga a justificar la accion
- Cada opcion con pros, contras y estimacion
- Una opcion DEBE ser la recomendada con justificacion

### Paso 3: Matriz de Decision
Crear matriz ponderada con criterios explicitados:
- Criterios derivados de NFRs (ver `references/nfr-taxonomia.md`)
- Pesos asignados con input del arquitecto
- Scoring transparente

### Paso 4: Impacto y Riesgos
- Sistemas y modulos afectados
- Riesgos con plan de mitigacion
- Plan de rollback (como deshacer si falla)
- Impacto regulatorio (si aplica)

### Paso 5: Critica
Aplicar la critica del orquestador (🔴🟡🟢).

## Plantilla

Usar `templates/rfc.md` como base.

## Diagramas

- **C4 Level 1 (System Context):** SHOULD generarse para visualizar el problema
  y las integraciones propuestas. Ver `skills/diagramas/SKILL.md`.
- **Formato:** Excalidraw preferido para comunicacion con stakeholders no tecnicos.

## Reglas de Contenido

- MUST usar RFC 2119: MUST, SHOULD, MAY, MUST NOT, SHOULD NOT
- MUST incluir la opcion "No hacer nada"
- MUST documentar riesgos con plan de mitigacion
- SHOULD incluir estimacion cuantificada del impacto
- El RFC NO es el lugar para detalles de implementacion (eso va en Tech Spec)
- El RFC NO debe recomendar tecnologias especificas (eso va en ADR)

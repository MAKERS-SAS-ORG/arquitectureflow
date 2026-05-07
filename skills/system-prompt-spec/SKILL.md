# Skill: System Prompt Spec — Especificacion para Agentes LLM
# Version: 2026.2

---

## Proposito

Si el sistema integra un agente LLM, el System Prompt Spec documenta como se comporta,
que puede y no puede hacer, y como se prueba su comportamiento.
Sin esta especificacion, el comportamiento del agente es impredecible y no auditable.

## Cuando es Obligatorio

- Cualquier componente que use un LLM para tomar decisiones o generar texto visible al usuario
- Cualquier agente que acceda a datos del sistema o los modifique
- En sistemas financieros: SIEMPRE que un LLM este en el flujo de una decision

## Prerequisitos

- Context Brief aprobado (`CB-NNN` — debe indicar "Integra IA/LLM: Si")
- PRD aprobado (define que hace el agente para el usuario)
- ADRs de tecnologia (que modelo LLM, que proveedor)

## Roles colaboradores en este artefacto

> Ver bloque "Roles colaboradores" en `templates/system-prompt-spec.md` y diagrama en `README.md`.

| Rol | Que pedirle al consultarlo | En que paso del workflow |
|---|---|---|
| **Especialista Tecnico** (con experiencia en LLMs) | **Principal.** Estructura del system prompt, eleccion de modelo y parametros, integracion con el resto del sistema | Paso 4 (system prompt) y Paso 5 (datos de contexto) |
| **QA** | Casos adversariales: prompt injection, jailbreaks, fuera de scope, edge cases. Disenar el suite de regresion | Paso 5 (test cases) — bloqueante antes de produccion |
| **Compliance / Legal** | Disclosure obligatorio, regulacion local (UE AI Act, NIST AI RMF, regulacion financiera), datos prohibidos en contexto | Paso 6 (compliance) y revision de datos inyectados |
| **Acelerador** (Negocio) | Comportamiento esperado, tono, idioma, casos priorizados | Paso 1 (proposito) y Paso 2 (allowlist) |

> Si compliance no firma, el agente NO va a produccion — sin importar cuan bueno sea el prompt.

## Workflow de Creacion

### Paso 1: Proposito del Agente
Una sola oracion: que hace y para quien.

### Paso 2: Allowlist (capacidades permitidas)
Lista explicita de lo que el agente PUEDE hacer.

### Paso 3: Denylist (restricciones obligatorias)
Lista explicita de lo que el agente NO PUEDE hacer bajo ninguna circunstancia.

### Paso 4: System Prompt (version aprobada)
El prompt completo, marcado como inmutable sin aprobacion del arquitecto.

### Paso 5: Test Cases
Casos de prueba obligatorios antes de produccion: preguntas normales,
prompt injection, preguntas fuera de scope, promesas de resultado.

### Paso 6: Compliance
Consideraciones regulatorias del uso de IA en el dominio.

## Plantilla

Usar `templates/system-prompt-spec.md` como base.

## Diagramas

- **Flujo behavioral del agente:** Mermaid stateDiagram — SHOULD.

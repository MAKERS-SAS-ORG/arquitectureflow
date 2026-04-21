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

- PRD aprobado (define que hace el agente para el usuario)
- ADRs de tecnologia (que modelo LLM, que proveedor)

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

# Skill: PRD — Product Requirements Document
# Version: 2026.2

> Referencia: TOGAF Business Architecture — `references/bibliografia.md#togaf`
> Referencia: ISO/IEC 25010:2023 — Quality Model — `references/bibliografia.md#iso25010`
> Referencia: Bass, L. et al. Quality Attribute Scenarios — `references/bibliografia.md#complementarias`

---

## Proposito

Define QUE se construye exactamente: funcionalidades, criterios de aceptacion,
NFRs cuantificados, casos de uso y reglas de negocio.
Sin PRD, el equipo implementa su interpretacion del RFC.
Con PRD, todos construyen lo mismo.

## Diferencia con el RFC

- **RFC:** "Debemos construir X y como?" (problema y alternativas)
- **PRD:** "Exactamente que tiene X?" (funcionalidades y criterios)

## Scope del SA en el PRD

El Arquitecto de Soluciones contribuye al PRD con:
- Quality Attribute Scenarios (NFRs medibles)
- Restricciones tecnicas y regulatorias
- Dependencias de sistemas externos
- Scope explicito (IN y OUT)

El Product Owner contribuye con:
- User stories y criterios de aceptacion funcionales
- Priorizacion de negocio
- Metricas de exito del producto

## Prerequisitos

- RFC aprobado

## Workflow de Creacion

### Paso 1: Objetivo del Producto
Una oracion: que resultado de negocio logra esta funcionalidad.
No que hace el sistema — que logra el usuario o el negocio.

### Paso 2: Usuarios Objetivo
Identificar personas/roles con sus necesidades principales.

### Paso 3: Casos de Uso
Flujos principales y alternativos con precondiciones y postcondiciones.

### Paso 4: User Stories con Criterios de Aceptacion
Formato Gherkin (Given/When/Then) como contrato de pruebas.

### Paso 5: Quality Attribute Scenarios (aporte del SA)
Usar formato de `references/nfr-taxonomia.md`:
```
Fuente → Estimulo → Artefacto → Entorno → Respuesta → Medida
```

### Paso 6: Reglas de Negocio
Invariantes que no pueden violarse nunca.

### Paso 7: Scope Explicito
Funcionalidades que NO estan en este PRD y por que.

## Plantilla

Usar `templates/prd.md` como base.

## Diagramas

- **Stakeholder map:** Excalidraw (SHOULD)
- **Flujos de caso de uso:** Mermaid sequence diagram (si hay flujos complejos)

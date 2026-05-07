# validacionTaller-v2 — AsistIA: Asistente Conversacional para Reclamos de Seguros

> **Proposito de esta carpeta:** validar end-to-end que el flujo de ArquitectureFlow
> v2026.4 (con la nueva guia de **roles colaboradores** en templates/skills/taller)
> funciona automaticamente y deja clara la interaccion del SA con cada rol.

## El caso (distinto del ejemplo de inversion)

**Cliente:** SaludVita Seguros (Colombia, ficticio).

**Problema:** los asegurados tardan en promedio 18 minutos en radicar un reclamo
(formularios mal disenados, llamadas perdidas a call center). El 34% abandona el
proceso. Esto cuesta NPS y aumenta CAC. Quieren un asistente conversacional con
LLM que radique reclamos en menos de 5 minutos, con audit trail completo (regulacion
SuperSalud + Habeas Data Ley 1581/2012).

**Por que sirve para validar:**
- Tiene **componente IA** → ejercita System Prompt Spec (artefacto que solo aplica con LLM).
- Tiene **compliance pesado** → ejercita coordinacion con Compliance/Legal.
- Tiene **multiples integraciones** (core de polizas, sistema de pagos, ARL, RIPS) →
  ejercita Context Map.
- Tiene **NFRs reales** (latencia conversacional, audit trail inmutable, disponibilidad).
- Es un dominio **diferente al ejemplo** (inversion-pasiva) → fuerza al framework a
  aplicarse desde cero.

## Que se valido

Cada artefacto generado tiene su seccion "Roles colaboradores" explicita y marca
con :busts_in_silhouette: el rol que provee cada decision. Las decisiones que NO
fueron validadas con el rol indicado aparecen marcadas con :red_circle: TODO.

## Estructura

```
validacionTaller-v2/
|-- README.md                # Este archivo
|-- CB-001.md                # Context Brief (Approved)
|-- RFC-001.md               # Request for Comments (Approved)
|-- ADR-001.md               # Decision: proveedor LLM (Aceptado)
|-- ADR-002.md               # Decision: arquitectura conversacional (Aceptado)
|-- PRD-001.md               # Product Requirements (Review)
|-- TS-001.md                # Tech Spec + diagrama C4 L2 referenciado (Review)
|-- SD-001.md                # System Design (Draft)
|-- RO-001.md                # Requisitos Operacionales (Draft)
|-- CM-001.md                # Context Map DDD (Draft)
|-- FF-001.md                # Fitness Functions (Draft)
|-- SPS-001.md               # System Prompt Spec del agente (Draft - bloqueado por compliance)
|-- TAA-001.md               # Tablero de Adherencia (Draft - vivo)
'-- VALIDACION.md            # Reporte de mejoras detectadas en el flujo
```

## Como leer esta validacion

1. Empezar por `CB-001.md` y seguir el orden numerico.
2. En cada artefacto, mirar la seccion **"Roles colaboradores"** y los marcadores
   :busts_in_silhouette:[ROL] / :red_circle: TODO en el cuerpo.
3. Terminar en `VALIDACION.md` para ver que mejoras al framework se detectaron.

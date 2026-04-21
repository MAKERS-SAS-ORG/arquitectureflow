# Matriz de Decision: Artefactos por Tipo de Trabajo

> Referencia: TOGAF ADM — seleccion de deliverables por fase.
> Referencia: Arc42 — documentacion proporcional a la complejidad.

---

## Matriz Principal

| Tipo de trabajo | RFC | ADR | PRD | Tech Spec | System Design | Runbook | Post-Mortem | System Prompt Spec | Context Map | Fitness Functions |
|---|---|---|---|---|---|---|---|---|---|---|
| **Nuevo sistema completo** | MUST | MUST | MUST | MUST | MUST | MUST | Cuando aplique | Si hay LLM | MUST | SHOULD |
| **Nueva funcionalidad mayor** | MUST | Si aplica | MUST | MUST | Si afecta escala | -- | -- | Si hay LLM | SHOULD | SHOULD |
| **Integracion con sistema externo** | MUST | MUST | MUST | MUST | Si afecta escala | Actualizar | -- | -- | MUST | SHOULD |
| **Cambio de decision arquitectonica** | MUST | MUST | -- | Si aplica | Si aplica | Actualizar | -- | -- | Si aplica | -- |
| **Incidente de produccion** | -- | Si se aprende algo | -- | -- | -- | Actualizar | MUST | -- | -- | -- |
| **Spike / investigacion tecnica** | RFC lite | Si aplica | -- | -- | -- | -- | -- | -- | -- | -- |
| **Agente LLM o componente IA** | MUST | MUST | MUST | MUST | MUST | MUST | -- | MUST | SHOULD | SHOULD |
| **Migracion de plataforma** | MUST | MUST | -- | MUST | MUST | MUST | -- | Si hay LLM | MUST | MUST |

## Guia Rapida de Seleccion

### Pregunta 1: Es una propuesta nueva o una decision ya tomada?
- **Propuesta nueva** -> Empezar con RFC
- **Decision ya tomada que necesita documentarse** -> Empezar con ADR

### Pregunta 2: Tiene componente de producto (usuarios, funcionalidades)?
- **Si** -> PRD despues del RFC
- **No (infra, migracion, refactor)** -> Saltar PRD, ir directo a Tech Spec

### Pregunta 3: Va a produccion con trafico real?
- **Si** -> System Design + Runbook obligatorios
- **No (herramienta interna, PoC)** -> System Design lite, sin Runbook

### Pregunta 4: Incluye un LLM/agente de IA?
- **Si** -> System Prompt Spec obligatorio ANTES de integracion
- **No** -> No aplica

### Pregunta 5: Integra con sistemas externos?
- **Si** -> Context Map (DDD) obligatorio
- **No** -> Opcional

## RFC Lite (para spikes)

Un RFC lite es un RFC reducido que solo incluye:
- Resumen ejecutivo (1 parrafo)
- Contexto y motivacion (breve)
- Opciones consideradas (minimo 2 incluyendo "no hacer nada")
- Recomendacion
- Time-box del spike (maximo 1 semana)
- Criterios de exito del spike

No requiere matriz de decision ponderada ni plan de rollback.

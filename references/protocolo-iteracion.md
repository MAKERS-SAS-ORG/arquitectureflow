# Protocolo de Iteracion Specs-Driven

> Referencia: Ford, N.; Parsons, R.; Kua, P. *Building Evolutionary Architectures.* 2nd Ed. O'Reilly, 2023.
> Principio: "Last Responsible Moment" — diferir decisiones hasta tener informacion suficiente, pero no mas alla.

---

## Filosofia

La arquitectura de soluciones NO es un proceso waterfall donde el SA entrega
un "paquete completo" de artefactos antes de que ingenieria empiece.

La arquitectura se entrega **iterativamente**:
- Cada artefacto entregado es valor
- Los artefactos evolucionan con el proyecto
- El SA mantiene la vision pero acepta que los detalles emergen
- La IA acelera la creacion pero el SA valida cada entrega

### Regla de oro: iteracion sobre perfeccion

> Un RFC Draft entregado hoy tiene mas valor que un RFC perfecto que nunca se publica.

Los artefactos DEBEN madurar de Draft a Approved conforme avanza la comunicacion
con los equipos. El SA no espera a tener toda la informacion para empezar a escribir.
Los gaps se marcan con 🔴 TODO y se resuelven en iteraciones posteriores.

## Ciclo de Iteracion

```
1. EVALUAR ──> Contexto del proyecto (negocio, stakeholders, constraints)
     |
2. SELECCIONAR ──> Artefacto de mayor valor inmediato
     |
3. CREAR ──> Borrador (Draft) del artefacto con asistencia de IA
     |
4. REVISAR ──> Feedback de stakeholders (Review)
     |
5. DECIDIR ──> Aprobar o iterar
     |         |
     |         └── Volver a 3 con feedback incorporado
     |
6. EVALUAR ──> Siguiente artefacto necesario?
     |         |
     |         ├── SI -> Volver a 2
     |         └── NO -> Arquitectura suficiente para esta fase
     |
7. MONITOREAR ──> Trigger de refactoring?
               |
               ├── SI -> Volver a 2 con artefacto afectado
               └── NO -> Mantener vigilancia
```

## Reglas de Secuencia

### Secuencia recomendada (default)
RFC -> ADR -> PRD -> Tech Spec -> System Design -> Runbook

### Excepciones validas

| Situacion | Secuencia alternativa |
|---|---|
| Decision urgente que bloquea al equipo | ADR primero, RFC despues (documentar retroactivamente) |
| Incidente en produccion | Post-Mortem primero, luego ADR si hay cambio arquitectonico |
| PoC/spike tecnico | RFC lite, luego ADR con hallazgos |
| Nuevo componente IA | System Prompt Spec en paralelo con Tech Spec |
| Integracion con tercero | Context Map en paralelo con RFC |

### Regla de dependencia minima
Un artefacto SHOULD tener como prerequisito solo el artefacto inmediatamente anterior.
Pero PUEDE crearse en paralelo si el SA tiene suficiente contexto para ambos.

## Entrega Incremental dentro de un Artefacto

Un artefacto no necesita estar 100% completo para entregarse como Draft:

### RFC incremental
1. Primera entrega: Problema + Contexto + 1 opcion explorada
2. Segunda entrega: Todas las opciones + Matriz de decision
3. Tercera entrega: Recomendacion + Riesgos + Plan de rollback

### ADR incremental
1. Primera entrega: Contexto + Decision propuesta
2. Segunda entrega: Opciones consideradas + Justificacion
3. Tercera entrega: Consecuencias + Plan de validacion

### System Design incremental
1. Primera entrega: Diagrama C4 L1 + Drivers de arquitectura
2. Segunda entrega: Diagrama C4 L2 + NFRs cuantificados
3. Tercera entrega: STRIDE + Observabilidad + Capacity planning

## Criterios de "Arquitectura Suficiente"

La arquitectura es "suficiente" para que ingenieria empiece cuando:

- [ ] El problema y la justificacion estan claros (RFC aprobado)
- [ ] Las decisiones irreversibles estan documentadas (ADRs criticos aprobados)
- [ ] Los limites del sistema son visibles (Context Map o C4 L1 minimo)
- [ ] Los NFRs tienen objetivos medibles (no "debe ser rapido" sino "< 200ms p99")
- [ ] Los riesgos criticos tienen plan de mitigacion
- [ ] El equipo puede empezar sin bloqueos de informacion

NO se requiere:
- Todos los ADRs (las decisiones reversibles pueden tomarse durante implementacion)
- System Design completo (puede crecer con el proyecto)
- Runbook completo (se completa antes del primer despliegue, no antes de empezar a codear)

## Rol de la IA en cada fase

| Fase | La IA hace | El SA hace |
|---|---|---|
| EVALUAR | Sugiere preguntas de contexto, identifica gaps | Formula el problema, valida contexto |
| SELECCIONAR | Recomienda artefacto segun matriz | Decide prioridad basado en valor de negocio |
| CREAR | Genera borrador siguiendo template y estandares | Revisa, corrige, enriquece con conocimiento de dominio |
| REVISAR | Aplica critica contra el skill, identifica 🔴 TODOs | Valida con stakeholders reales |
| DECIDIR | Actualiza estado y version | Aprueba o rechaza |
| MONITOREAR | Detecta inconsistencias entre artefactos | Decide si refactorizar |

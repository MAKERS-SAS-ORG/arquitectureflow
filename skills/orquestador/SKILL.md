# Skill: Orquestador de Arquitectura de Soluciones
# Version: 2026.2
# Tipo: Orquestador principal

---

## Proposito

Orquestar el flujo completo de arquitectura de soluciones: desde la captura del contexto
de negocio hasta la entrega iterativa de artefactos arquitectonicos.

Este skill se activa cuando el usuario quiere:
- Iniciar un nuevo proyecto o solucion arquitectonica
- Crear cualquier artefacto de arquitectura (RFC, ADR, PRD, etc.)
- Seguir la metodologia de arquitectura de soluciones
- Evaluar que artefactos necesita un proyecto
- Revisar el estado de madurez de artefactos existentes

---

## Fase 1: Captura de Contexto

Antes de generar cualquier artefacto, MUST capturar el contexto del proyecto.

### Preguntas Obligatorias (hacer al arquitecto)

**Negocio:**
1. Cual es el problema de negocio que estamos resolviendo? (en 1-2 oraciones)
2. Quien es el usuario/beneficiario principal?
3. Cual es el costo de NO resolver este problema? (cuantificado si es posible)
4. Hay deadline de negocio o regulatorio?

**Stakeholders:**
5. Quienes son los stakeholders principales? (decision-makers, usuarios, equipos afectados)
6. Quien aprueba las decisiones arquitectonicas?

**Contexto Tecnico:**
7. Es greenfield (nuevo), evolucion (existente) o migracion?
8. Que sistemas existentes estan involucrados?
9. Hay restricciones tecnologicas (regulatorias, vendor, skills del equipo)?

**Escala:**
10. Cual es la escala esperada? (usuarios, transacciones, datos)

### Preguntas Opcionales (segun contexto)
- Hay componente de IA/LLM en la solucion?
- Que nivel de compliance se requiere? (GDPR, PCI-DSS, SOX, regulacion financiera local)
- Hay requisitos de multi-tenancy o internacionalizacion?

---

## Fase 2: Seleccion de Artefactos

Leer `references/matriz-decision.md` y determinar que artefactos aplican.

Presentar al arquitecto:
- Lista de artefactos MUST (obligatorios para este tipo de proyecto)
- Lista de artefactos SHOULD (recomendados)
- Lista de artefactos que NO aplican y por que
- Recomendacion de cual artefacto iniciar primero

---

## Fase 3: Entrega Iterativa

Leer `references/protocolo-iteracion.md` para la metodologia completa.

### Secuencia por Defecto
RFC -> ADR -> PRD -> Tech Spec -> System Design -> Requisitos Operacionales

### Adaptacion
El orquestador PUEDE recomendar una secuencia diferente segun el contexto:
- Decision urgente: ADR primero
- Incidente: Post-Mortem primero
- Spike: RFC lite
- Componente IA: System Prompt Spec en paralelo

---

## Fase 4: Hand-off a Skill Especifico

Cuando el arquitecto elige un artefacto, el orquestador:

1. Resume el contexto capturado en Fase 1
2. Indica los artefactos prerequisito y su estado
3. Carga el skill especifico:

```
Lee skills/[artefacto]/SKILL.md
Lee templates/[artefacto].md

Contexto del proyecto:
- Problema: [resumen]
- Stakeholders: [lista]
- Tipo: [greenfield/evolucion/migracion]
- Restricciones: [lista]
- Artefactos previos: [estado]

Genera el artefacto siguiendo el skill y la plantilla.
Marca con 🔴 TODO lo que necesita validacion del arquitecto.
```

---

## Fase 5: Critica y Revision

Despues de generar cualquier artefacto, aplicar critica automatica:

```
Actua como arquitecto esceptico. Lee el artefacto generado.
Encuentra minimo 3 problemas potenciales.
Clasifica:
  🔴 Critico — bloquea aprobacion
  🟡 Importante — debe resolverse antes de Approved
  🟢 Sugerencia — mejora opcional

Se directo y especifico. No halagues.
```

---

## Fase 6: Diagramas

Despues de aprobar un artefacto que requiere diagramas:

Leer `references/diagramas-estrategia.md` para determinar:
- Que tipo de diagrama necesita este artefacto
- Si usar Excalidraw MCP o Mermaid inline
- El nivel de C4 apropiado

Cargar `skills/diagramas/SKILL.md` para generar los diagramas.

---

## Fase 7: Evolucion y Consistencia

El orquestador SHOULD monitorear consistencia entre artefactos:

### Checks de Consistencia
- Un ADR contradice una decision en la Tech Spec?
- El System Design referencia tecnologias no mencionadas en ADRs?
- Los NFRs del PRD estan reflejados en el System Design?
- El Runbook cubre los componentes del System Design?

### Triggers de Re-evaluacion
Leer `references/niveles-madurez.md` seccion "Triggers de Refactoring".

---

## Checklist de Aprobacion Arquitectonica

Antes de que ingenieria empiece a implementar, el arquitecto firma:

### Artefactos
- [ ] RFC aprobado con stakeholders
- [ ] ADRs criticos (decisiones irreversibles) aceptados
- [ ] PRD aprobado con Product Owner (si aplica)
- [ ] Tech Spec revisada
- [ ] System Design revisado
- [ ] Requisitos operacionales definidos (si va a produccion)
- [ ] System Prompt Spec aprobado (si hay LLM)

### Calidad
- [ ] Ningun 🔴 TODO sin resolver
- [ ] Sistemas externos tienen SLA documentado
- [ ] Plan de rollback es ejecutable
- [ ] NFRs tienen objetivos medibles
- [ ] Criterios de aceptacion son verificables

### Equipo
- [ ] El equipo leyo los artefactos relevantes
- [ ] No hay preguntas sin responder sobre "que construir"
- [ ] Los limites de scope estan claros (que esta IN y que esta OUT)

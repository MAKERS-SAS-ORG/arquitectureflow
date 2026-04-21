# Estrategia de Diagramas por Artefacto

> Referencia: Brown, S. *C4 Model.* c4model.com
> Referencia: ISO/IEC/IEEE 42010:2022 — Architecture Views and Viewpoints

---

## Principio

Cada diagrama es una **vista** (view) de la arquitectura desde un **punto de vista** (viewpoint)
especifico para una audiencia especifica. No generar diagramas por generar.

## Cuando generar un diagrama

Un diagrama SHOULD generarse cuando:
- La estructura no es obvia solo con texto
- Hay multiples stakeholders con diferentes niveles tecnicos
- El artefacto describe integraciones entre sistemas
- El artefacto describe topologia de deployment
- Se necesita comunicar a audiencia no tecnica

Un diagrama NO es necesario cuando:
- La decision es puramente textual (ej: ADR sobre formato de fechas)
- El artefacto es procesal (ej: Runbook con pasos secuenciales simples)
- Solo hay un sistema sin integraciones

## Notacion Principal: C4 Model

El Arquitecto de Soluciones trabaja primariamente en **C4 Level 1 y Level 2**:

### Level 1: System Context
- **Que muestra:** El sistema como caja negra + usuarios + sistemas externos
- **Audiencia:** Todos, incluyendo stakeholders no tecnicos
- **Cuando:** SIEMPRE para cualquier sistema nuevo
- **Herramienta preferida:** Excalidraw (visual argument importa)

### Level 2: Container
- **Que muestra:** Contenedores dentro del sistema (apps, DBs, colas, caches)
- **Audiencia:** Equipo tecnico, arquitectos, DevOps
- **Cuando:** Cualquier sistema con mas de un componente deployable
- **Herramienta preferida:** Excalidraw (layout espacial importa)

### Level 3: Component (colaboracion con Software Architect)
- **Que muestra:** Componentes internos de un contenedor
- **Audiencia:** Desarrolladores del equipo
- **Cuando:** Selectivo, solo contenedores complejos
- **Nota:** Mas cercano al scope de Software Architect

### Diagramas Suplementarios
- **Deployment Diagram:** Mapeo a infraestructura (VPCs, AZs, clusters)
- **Dynamic Diagram:** Secuencias de interaccion en runtime
- **Context Map (DDD):** Relaciones entre bounded contexts

## Mapa Completo

| Artefacto | Diagrama | Formato | Obligatorio |
|---|---|---|---|
| RFC | C4 L1 System Context | Excalidraw | SHOULD |
| ADR | (ninguno tipicamente) | -- | -- |
| PRD | Stakeholder map | Excalidraw | SHOULD |
| PRD | Flujos de caso de uso | Mermaid sequence | Condicional |
| Tech Spec | C4 L2 Container | Excalidraw | MUST |
| Tech Spec | Secuencias de integracion | Mermaid sequence | SHOULD |
| System Design | C4 L2 Container + Deployment | Excalidraw | MUST |
| System Design | Flujo de datos | Mermaid flowchart | SHOULD |
| System Design | Context Map DDD | Excalidraw | Condicional |
| System Design | STRIDE threat flow | Mermaid flowchart | Condicional |
| Runbook | Decision tree operacional | Mermaid flowchart | SHOULD |
| Post-Mortem | Timeline del incidente | Mermaid timeline | SHOULD |
| System Prompt Spec | Flujo behavioral del agente | Mermaid stateDiagram | SHOULD |

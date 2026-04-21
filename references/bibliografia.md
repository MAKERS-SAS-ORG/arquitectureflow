# Bibliografia y Estandares de Referencia

Referencia central para todos los skills de ArquitectureFlow.
Cada entrada incluye: citacion completa, aplicabilidad y artefactos donde se usa.

---

## TOGAF {#togaf}

- **Citacion:** The Open Group. *TOGAF Standard, 10th Edition.* 2022.
- **URL:** https://www.opengroup.org/togaf
- **Aplicabilidad:** Gobernanza de artefactos, Architecture Development Method (ADM),
  Architecture Building Blocks (ABBs) vs Solution Building Blocks (SBBs),
  Capability-Based Planning, Business Scenarios.
- **Conceptos clave para SA:**
  - Fase Preliminary: principios de arquitectura
  - Fase A (Architecture Vision): stakeholder map, solution concept diagram
  - Fase B (Business Architecture): capability map, procesos BPMN
  - Fase C (Information Systems): application communication, data dissemination
  - Fase D (Technology Architecture): platform decomposition, deployment
- **Artefactos donde aplica:** RFC, PRD, Tech Spec, System Design
- **Certificaciones:** TOGAF Foundation (Level 1), TOGAF Certified (Level 2)

## ISO/IEC/IEEE 42010:2022 {#iso42010}

- **Citacion:** ISO/IEC/IEEE. *Systems and software engineering — Architecture description.* ISO/IEC/IEEE 42010:2022.
- **Aplicabilidad:** EL estandar internacional para documentacion de arquitecturas.
  Define como se deben describir las arquitecturas de sistemas y software.
- **Conceptos clave:**
  - Architecture Description (AD): producto de trabajo que expresa una arquitectura
  - Stakeholders y Concerns: toda AD debe identificar quien le importa y que le importa
  - Architecture Viewpoints: convenciones para construir e interpretar una vista
  - Architecture Views: representacion concreta desde un viewpoint particular
  - Architecture Rationale: registro de decisiones y trade-offs (enlaza con ADRs)
  - Correspondence Rules: relaciones y consistencia entre vistas
- **Artefactos donde aplica:** ADR, Tech Spec, System Design

## Modelo C4 {#c4}

- **Citacion:** Brown, Simon. *The C4 Model for Visualising Software Architecture.* c4model.com. Actualizado continuamente.
- **URL:** https://c4model.com
- **Aplicabilidad:** Notacion principal para diagramas de arquitectura en este framework.
  "Mapas de tu codigo a diferentes niveles de zoom."
- **Niveles:**
  - **L1 — System Context:** El sistema como caja, rodeado de usuarios y sistemas externos.
    SIEMPRE se crea. Audiencia: todos incluyendo stakeholders no tecnicos.
  - **L2 — Container:** Zoom al sistema mostrando contenedores (apps, DBs, colas, etc.)
    Nivel MAS UTIL para el Arquitecto de Soluciones.
  - **L3 — Component:** Zoom a un contenedor mostrando componentes internos.
    Selectivo, solo para contenedores complejos. Mas cercano al scope de Software Architect.
  - **L4 — Code:** Diagramas de clases UML. Scope de Software Architect. Rara vez se genera.
- **Diagramas suplementarios:** System Landscape (L0), Dynamic Diagram, Deployment Diagram.
- **Tooling:** Structurizr DSL (structurizr.com), Mermaid C4, Excalidraw.
- **Nota SA:** El Arquitecto de Soluciones trabaja primariamente en L1-L2. L3 es colaboracion con Software Architect. L4 esta fuera de scope.
- **Artefactos donde aplica:** RFC (L1), Tech Spec (L1-L2), System Design (L2, Deployment)

## Arc42 {#arc42}

- **Citacion:** Starke, Gernot; Hruschka, Peter. *Arc42: Template for Architecture Documentation.* v8.x, 2023-2024.
- **URL:** https://arc42.org
- **Licencia:** Creative Commons (uso libre)
- **Aplicabilidad:** Template de documentacion de arquitectura compatible con ISO 42010.
  12 secciones que cubren desde objetivos hasta riesgos.
- **Secciones relevantes para SA:**
  1. Introduction and Goals (requisitos, quality goals, stakeholders)
  2. Architecture Constraints (tecnicas, organizacionales, politicas)
  3. System Scope and Context (contexto de negocio y tecnico)
  4. Solution Strategy (decisiones fundamentales)
  5. Building Block View (descomposicion estatica — mapea a C4 L2-L3)
  6. Runtime View (escenarios clave de interaccion)
  7. Deployment View (infraestructura, topologia)
  8. Cross-cutting Concepts (domain model, patrones, seguridad)
  9. Architecture Decisions (ADRs)
  10. Quality Requirements (quality tree, quality scenarios)
  11. Risks and Technical Debt
  12. Glossary
- **Artefactos donde aplica:** Tech Spec, System Design

## MADR {#madr}

- **Citacion:** Kopp, Oliver et al. *Markdown Any Decision Records (MADR).* Version 4.0.0, 2024.
- **URL:** https://adr.github.io/madr/
- **Aplicabilidad:** Formato estructurado para ADRs con decision drivers,
  opciones consideradas, pros/contras, y justificacion explicita.
- **Artefactos donde aplica:** ADR

## Formato Nygard {#nygard}

- **Citacion:** Nygard, Michael. "Documenting Architecture Decisions." Cognitect Blog, Noviembre 2011.
- **URL:** https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- **Aplicabilidad:** Formato lightweight original para ADRs: Title, Status, Context, Decision, Consequences.
  Preferido para decisiones rapidas que no requieren comparacion exhaustiva de opciones.
- **Artefactos donde aplica:** ADR

## RFC 2119 {#rfc2119}

- **Citacion:** Bradner, S. *Key words for use in RFCs to Indicate Requirement Levels.* RFC 2119, Marzo 1997.
- **URL:** https://www.rfc-editor.org/rfc/rfc2119
- **Aplicabilidad:** Palabras clave MUST, SHOULD, MAY, MUST NOT, SHOULD NOT
  para especificar niveles de requerimiento en documentos tecnicos.
- **Artefactos donde aplica:** RFC, Tech Spec, System Design, Runbook

## Arquitecturas Evolutivas {#evolutionary}

- **Citacion:** Ford, Neal; Parsons, Rebecca; Kua, Patrick. *Building Evolutionary Architectures: Automated Software Governance.* 2nd Edition. O'Reilly, 2023.
- **Aplicabilidad:** Fundamento de la metodologia specs-driven de este framework.
  Arquitectura que soporta cambio incremental guiado por fitness functions.
- **Conceptos clave:**
  - Incremental change: cambios pequenos y reversibles vs big-bang redesign
  - Fitness functions: evaluacion objetiva y automatizada de caracteristicas de arquitectura
  - Last Responsible Moment: diferir decisiones hasta tener informacion suficiente
  - Sacrificial Architecture: planear para reemplazabilidad
- **Artefactos donde aplica:** Todos (metodologia transversal)

## Domain-Driven Design {#ddd}

- **Citaciones:**
  - Evans, Eric. *Domain-Driven Design: Tackling Complexity in the Heart of Software.* Addison-Wesley, 2003.
  - Vernon, Vaughn. *Implementing Domain-Driven Design.* Addison-Wesley, 2013.
  - Vernon, Vaughn. *Domain-Driven Design Distilled.* Addison-Wesley, 2016.
  - Khononov, Vlad. *Learning Domain-Driven Design.* O'Reilly, 2021.
- **Aplicabilidad:** Patrones estrategicos para definir limites de modulos y servicios.
- **Patrones estrategicos para SA:**
  - Bounded Context: limite explicito donde un modelo de dominio aplica
  - Context Mapping: relaciones entre bounded contexts (Shared Kernel, Customer-Supplier, ACL, Open Host Service, etc.)
  - Subdomains: Core (ventaja competitiva), Supporting (necesario), Generic (commodity)
  - Domain Events: base para arquitectura event-driven
- **Tecnicas complementarias:**
  - EventStorming (Alberto Brandolini, eventstorming.com)
  - Context Mapper DSL (contextmapper.org)
- **Artefactos donde aplica:** Tech Spec, System Design, Context Map

## Calidad de Software — ISO 25010 {#iso25010}

- **Citacion:** ISO/IEC. *ISO/IEC 25010:2023 — Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model.*
- **Aplicabilidad:** Taxonomia de atributos de calidad para especificar NFRs.
- **Caracteristicas de calidad:**
  - Functional Suitability (correctness, appropriateness, completeness)
  - Performance Efficiency (time behavior, resource utilization, capacity)
  - Compatibility (co-existence, interoperability)
  - Usability (appropriateness recognizability, learnability, operability, accessibility)
  - Reliability (maturity, availability, fault tolerance, recoverability)
  - Security (confidentiality, integrity, non-repudiation, accountability, authenticity)
  - Maintainability (modularity, reusability, analysability, modifiability, testability)
  - Portability (adaptability, installability, replaceability)
- **Artefactos donde aplica:** PRD, Tech Spec, System Design

## Google SRE {#sre}

- **Citacion:** Beyer, Betsy; Jones, Chris; Petoff, Jennifer; Murphy, Niall Richard. *Site Reliability Engineering: How Google Runs Production Systems.* O'Reilly, 2016.
- **URL:** https://sre.google/sre-book/table-of-contents/
- **Aplicabilidad:**
  - Capitulo 10: Practical Alerting — para Runbook
  - Capitulo 15: Postmortem Culture — para Post-Mortem (blameless)
  - SLIs, SLOs, SLAs — para System Design
- **Artefactos donde aplica:** Runbook, Post-Mortem, System Design

## STRIDE {#stride}

- **Citacion:** Microsoft. *STRIDE Threat Modeling.* Microsoft Security Development Lifecycle.
- **URL:** https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool
- **Aplicabilidad:** Modelo de amenazas: Spoofing, Tampering, Repudiation,
  Information Disclosure, Denial of Service, Elevation of Privilege.
- **Artefactos donde aplica:** System Design

## Team Topologies {#teamtopologies}

- **Citacion:** Skelton, Matthew; Pais, Manuel. *Team Topologies: Organizing Business and Technology Teams for Fast Flow.* IT Revolution, 2019.
- **Aplicabilidad:** Alineacion de limites de equipo con limites de arquitectura (Ley de Conway aplicada).
  Stream-aligned teams, platform teams, enabling teams, complicated-subsystem teams.
- **Artefactos donde aplica:** System Design, Tech Spec

## Enterprise Integration Patterns {#eip}

- **Citacion:** Hohpe, Gregor; Woolf, Bobby. *Enterprise Integration Patterns: Designing, Building, and Deploying Messaging Solutions.* Addison-Wesley, 2003.
- **Aplicabilidad:** Patrones de integracion entre sistemas: Message Channel, Message Router,
  Message Translator, Message Endpoint, Publish-Subscribe, etc.
- **Artefactos donde aplica:** Tech Spec, System Design

## Referencias Complementarias {#complementarias}

| Titulo | Autores | Ano | Relevancia |
|---|---|---|---|
| *Software Architecture in Practice* 4th Ed | Bass, Clements, Kazman | 2021 | Quality attribute scenarios, metodo ADD |
| *Fundamentals of Software Architecture* | Richards, Ford | 2020 | Survey moderno de estilos de arquitectura |
| *Software Architecture: The Hard Parts* | Ford, Richards, Sadalage, Dehghani | 2021 | Trade-offs en arquitecturas distribuidas |
| *The Software Architect Elevator* | Hohpe | 2020 | Conectar arquitectura con estrategia de negocio |
| *Continuous Architecture in Practice* | Erder, Pureur, Woods | 2021 | Entrega continua de arquitectura |
| *Designing Data-Intensive Applications* | Kleppmann | 2017 | Sistemas distribuidos, arquitectura de datos |
| *Release It!* 2nd Ed | Nygard | 2018 | Patrones de estabilidad, produccion |
| *Just Enough Software Architecture* | Fairbanks | 2010 | Arquitectura guiada por riesgo |
| *Technology Strategy Patterns* | Hewitt | 2018 | Comunicacion de arquitectura y estrategia |

## Articulos Clave {#articulos}

- Kruchten, P. "Architectural Blueprints — The 4+1 View Model of Software Architecture." IEEE Software, 12(6), Nov 1995.
- Conway, M. "How Do Committees Invent?" Datamation, Abril 1968 (Ley de Conway).
- ThoughtWorks Technology Radar: https://www.thoughtworks.com/radar

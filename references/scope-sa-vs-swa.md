# Alcance: Solution Architect vs Software Architect

> Referencia: Hohpe, G. *The Software Architect Elevator.* O'Reilly, 2020.
> Referencia: Skelton, M.; Pais, M. *Team Topologies.* IT Revolution, 2019.

---

## Solution Architect (scope de este framework)

### Alineacion con el Negocio
- Traduce requisitos y estrategia de negocio en disenos tecnicos de solucion
- Asegura que la solucion entrega el valor de negocio esperado y ROI
- Participa en desarrollo de business case (TCO, build vs buy)
- Mapea capacidades de negocio a capacidades tecnicas
- Alinea la solucion con el roadmap de arquitectura empresarial

### Seleccion Tecnologica
- Evalua y recomienda tecnologias, plataformas y productos
- Conduce evaluaciones de vendor y Proof of Technology (PoT)
- Define estandares y guardrails tecnologicos para la solucion
- Toma decisiones build vs buy vs open-source
- Evalua riesgo tecnologico (madurez, vendor lock-in, comunidad, licenciamiento)

### Estrategia de Integracion
- Define como la solucion se integra con sistemas enterprise existentes
- Disena estrategia de API (REST, gRPC, GraphQL, event-driven) a nivel inter-sistema
- Especifica flujos de datos entre sistemas (sincrono, asincrono, batch)
- Define patrones de integracion (API Gateway, ESB, event broker, point-to-point)
- Gestiona contratos de integracion con terceros

### Requisitos No Funcionales (NFRs)
- Elicita, cuantifica y prioriza NFRs con stakeholders
- Define objetivos medibles: disponibilidad, latencia (p50, p95, p99), throughput, RTO/RPO
- Asegura que el diseno cumple NFRs y define fitness functions para probarlo
- Especifica arquitectura de seguridad (autenticacion, autorizacion, cifrado, auditoria)
- Define requisitos de compliance y sus implicaciones arquitectonicas

### Comunicacion con Stakeholders
- Crea y presenta artefactos a audiencias diversas (C-level, producto, ingenieria, operaciones, seguridad)
- Produce diagramas C4 Nivel 1 y 2 como herramientas principales de comunicacion
- Autoria de Architecture Decision Records para decisiones significativas
- Facilita architecture review boards y sesiones de diseno
- Gestiona riesgos arquitectonicos

### Artefactos que Posee el SA
- RFC, ADR (cross-cutting), PRD (NFRs), Tech Spec (nivel solucion), System Design
- Diagramas C4 L1 (Context) y L2 (Container)
- Specification de NFRs con objetivos medibles
- Decisiones de stack y plataforma
- Tablero de Adherencia Arquitectonica (gobernanza de implementacion)

---

## Software Architect / Equipo de Ingenieria (fuera de scope)

### Patrones de Implementacion
- Seleccion y aplicacion de design patterns (GoF, CQRS, Event Sourcing, Repository)
- Arquitectura interna de servicios (Clean Architecture, Hexagonal, Vertical Slice)
- Diseno de domain model (aggregates, entities, value objects — DDD tactico)
- Implementacion de anti-corruption layers y adapters
- Patrones de acceso a datos (ORM, query builders, raw SQL)

### Estructura de Codigo
- Estructura de proyectos/modulos, convenciones de packaging y namespacing
- Estandares de codigo, linting rules, formatting
- Grafo de dependencias internas dentro de un servicio
- Inyeccion de dependencias e inversion de control

### Diseno Detallado
- Diagramas de componentes (C4 L3) para servicios complejos
- Modelos de datos detallados (table schemas, indices, query patterns)
- Modelos de concurrencia y threading internos
- Estrategias de caching dentro del servicio
- Patrones de error handling, retry y resiliencia a nivel de codigo

### Practicas de Ingenieria
- Diseno de CI/CD pipeline stages y quality gates
- Implementacion de fitness functions como tests automatizados
- Estrategia de testing (unit, integration, contract, e2e)
- Documentacion de desarrollador (API docs, getting-started)
- Gestion de deuda tecnica

### Artefactos que Posee Ingenieria
- Diagramas C4 L3 (Component) y L4 (Code)
- Modelos de datos detallados y schemas
- Especificaciones API (OpenAPI, AsyncAPI, protobuf) — implementacion de contratos
- ADRs a nivel de implementacion
- Estandares de codigo y reglas de arquitectura interna

---

## Zona de Colaboracion

La linea entre ambos roles es un **gradiente**, no un muro:

| Area | SA define (que/por que) | SWA/Ingenieria define (como) |
|---|---|---|
| Base de datos | "Usaremos PostgreSQL" (ADR) | Connection pooling, ORM, indices |
| Performance | "El servicio DEBE responder < 200ms p99" (NFR) | Read replicas, caching, query optimization |
| Integracion | "Estos contextos se comunican via eventos" | MassTransit, Kafka client config |
| Seguridad | "JWT con expiracion 15min, MFA obligatorio" | Middleware implementation, token refresh |
| API | "Contrato: POST /solicitudes, 202 Accepted" | Handlers, validators, serializers |
| Datos | "Entidades de dominio: Solicitud, Evaluacion" | Table schemas, migrations, repositories |

### Inverse Conway Maneuver
El SA SHOULD trabajar con liderazgo de ingenieria para asegurar que los limites
de equipo se alinean con los limites de arquitectura (Team Topologies).

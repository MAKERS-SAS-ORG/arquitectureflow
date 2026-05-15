# Skill: Tech Spec — Technical Specification
# Version: 2026.3

> Referencia: Arc42 Secciones 4-8 — `references/bibliografia.md#arc42`
> Referencia: C4 Model Level 2 — `references/bibliografia.md#c4`
> Referencia: ISO/IEC/IEEE 42010:2022 — Architecture Views — `references/bibliografia.md#iso42010`

---

## Proposito

Define la estrategia tecnica de la solucion a nivel de Arquitecto de Soluciones:
seleccion tecnologica, estructura de contenedores, contratos de integracion,
y quality attributes. NO contiene codigo ni patrones de implementacion.

## Diferencia con ADR y System Design

- **ADR:** "Decidimos usar PostgreSQL porque..." (la decision y por que)
- **Tech Spec:** "Asi se organiza la solucion y sus tecnologias" (estructura y contratos)
- **System Design:** "Asi escala y es segura bajo carga" (comportamiento operacional)

## Scope del SA en la Tech Spec

INCLUYE (scope SA):
- Seleccion de stack tecnologico con referencia a ADRs
- Estructura de contenedores (C4 L2) y sus responsabilidades
- Contratos de integracion entre contenedores y sistemas externos
- Quality attribute trade-offs
- Architecture fitness functions
- Convenciones a nivel de solucion

NO INCLUYE (scope Software Architect/Ingenieria):
- Patrones de codigo (CQRS handlers, Repository pattern)
- Configuracion de frameworks (Entity Framework, Polly, MediatR)
- Estructura interna de modulos/clases
- Estrategia detallada de testing (unit vs integration)

## Prerequisitos

- Context Brief aprobado (`CB-NNN` — Fase 0 del orquestador)
- RFC aprobado
- ADRs criticos aceptados
- PRD aprobado

## Roles colaboradores en este artefacto

> Ver bloque "Roles colaboradores" en `templates/tech-spec.md` y diagrama en `README.md`.
> Esta es la **bisagra**: aqui el SA traduce decisiones a contratos que el equipo implementa.

| Rol | Que pedirle al consultarlo | En que paso del workflow |
|---|---|---|
| **Especialista Tecnico** (SWA / Tech Lead) | **Principal.** Validar el stack, contratos realistas, capacidad del equipo, identificar que es politica (SA) vs implementacion (SWA) | Pasos 1-3 (stack, contenedores, contratos) y Paso 4 (politicas) |
| **Equipo de Desarrollo** | Recibe la Tech Spec. Devuelve preguntas, supuestos descubiertos al implementar | Despues de Approved — leen antes de cada sprint y reportan gaps |
| **DevOps / SRE** | Restricciones de infraestructura, plataformas disponibles, costos del stack | Paso 1 (stack) y contenedores tipo Worker/Queue/DB |
| **QA** | Que es testeable como contract testing; necesidades de entornos de prueba | Paso 3 (contratos) y Paso 5 (Fitness Functions) |

> El SA NO debe declarar la Tech Spec en Approved sin haber recorrido los contratos
> con el Especialista Tecnico — el costo de una integracion mal especificada es alto.

## Workflow de Creacion

### Paso 1: Stack Tecnologico
Tabla de tecnologias por capa con referencia al ADR que justifica cada eleccion.

### Paso 2: Estructura de Contenedores (C4 L2)
Diagrama C4 Level 2 mostrando todos los contenedores deployables.
Cada contenedor con: nombre, tecnologia, responsabilidad.

### Paso 3: Contratos de Integracion
Para cada relacion entre contenedores o con sistemas externos:
- Protocolo (REST, GraphQL, gRPC, async/queue, batch)
- Contrato (endpoint, schema de eventos, formato de datos)
- SLA esperado
- Estrategia de error (retry, circuit breaker, fallback — a nivel de politica, no de implementacion)

### Paso 3.1: Diseño detallado de APIs expuestas (sub-artefacto API-NNN)

Cuando el sistema **expone** una o más APIs, la Tech Spec NO contiene el diseño
detallado del contrato — referencia al sub-artefacto `API-NNN`:

| Tipo de API | Cuándo dispararlo | Template |
|---|---|---|
| **REST + OpenAPI 3.1** (default para APIs de dominio / B2B / publicas) | Recursos estables, semántica HTTP fuerte, partners externos. Requiere SemVer 2.0.0 + política de deprecación (RFC 8594 Sunset header) | `templates/api-design-rest.md` |
| **GraphQL** (default para APIs de **experiencia** web/mobile → backend) | Front-end compone datos de múltiples fuentes, varios clientes, iteración UX rápida | `templates/api-design-graphql.md` |
| **gRPC / async (events)** | Comunicación interna alta-throughput / desacoplada | Documentar inline en TS-NNN sec. 3 |

> Regla: para promover una API a estado **Approved** debe existir el sub-artefacto
> `API-NNN` correspondiente con su spec canónico versionado (`openapi/*.yaml` o
> `schema/*.graphql`). El handoff lo dispara este skill al detectar contenedores
> de tipo API en la sección 2.

### Paso 3.2: Trigger del sub-artefacto desde el orquestador

Cuando el SA llene la sección 3 del Tech Spec y aparezca al menos una API expuesta:

1. Detectar en sección 2 (Contenedores) los de tipo `API`.
2. Para cada uno, preguntar: "¿Es API de experiencia (front-end → backend) o de dominio (B2B / backend)?"
3. Cargar el template y skill apropiado y crear `API-NNN.md`.
4. Anotar en la tabla 3.1 del Tech Spec el `API-NNN`, tipo y versión.

### Paso 4: Quality Attribute Trade-offs
Documentar los trade-offs entre atributos de calidad:
- "Mayor consistencia vs menor latencia"
- "Mayor seguridad vs mayor complejidad operacional"

### Paso 5: Fitness Functions
Definir mecanismos automatizados para validar la arquitectura.
Usar template `templates/fitness-functions.md`.

## Plantilla

Usar `templates/tech-spec.md` como base.

## Diagramas

- **C4 Level 2 (Container):** MUST — Excalidraw. Es el diagrama central de la Tech Spec.
- **Secuencias de integracion:** SHOULD — Mermaid. Para flujos entre contenedores.

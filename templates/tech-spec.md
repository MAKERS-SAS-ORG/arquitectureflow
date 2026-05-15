---
titulo: "Tech Spec: [Nombre del Sistema/Modulo]"
identificador: TS-[NNN]
tipo: Tech-Spec
estado: Draft
version: "1.0.0"
autor: "[Nombre]"
fecha-creacion: YYYY-MM-DD
fecha-ultima-revision: YYYY-MM-DD
revisores: []
artefactos-origen: ["RFC-NNN", "ADR-001", "ADR-002", "PRD-NNN"]
stakeholders: []
firmas-roles: []   # MUST firma del Especialista Tecnico para Approved. Ver _frontmatter.md
tags: []
---

# Tech Spec: [Nombre del Sistema/Modulo]

## Roles colaboradores

> Aqui el SA detalla el QUE con el **Especialista Tecnico** y entrega contratos al
> **Equipo de Desarrollo**. Es el artefacto de bisagra entre el dominio del SA y el del SWA.
> Ver diagrama de roles en `README.md`.

| Rol | Que aporta al SA | Cuando consultarlo |
|---|---|---|
| **Especialista Tecnico** (SWA / Tech Lead) | Validacion del stack, contratos de integracion realistas, estimaciones, capacidad real del equipo, identificacion de patrones de implementacion (que NO van aqui pero deben quedar claros) | Secciones 1-3 (stack, contenedores, contratos) y seccion 6 (politicas de solucion) |
| **DevOps / SRE** | Restricciones de infraestructura, plataformas disponibles, costos operativos del stack propuesto | Seccion 1 (stack) y seccion 2 (contenedores con tipo Worker/DB/Queue) |
| **QA** | Que de los contratos es testeable como contract testing, dependencias para entornos de prueba | Seccion 3 (contratos) y seccion 5 (Fitness Functions) |
| **Equipo de Desarrollo** | **Recibe** los contratos y politicas para implementar. Devuelve preguntas, dudas, supuestos que descubre al implementar | Despues de Approved — el equipo lee la Tech Spec antes de cada sprint |

## 1. Stack Tecnologico

| Capa | Tecnologia | Version | Justificacion (-> ADR) |
|---|---|---|---|
| [Capa 1] | [Tecnologia] | [Version] | ADR-NNN |
| [Capa 2] | [Tecnologia] | [Version] | ADR-NNN |

## 2. Estructura de Contenedores (C4 Level 2)

> Diagrama C4 L2 generado con Excalidraw MCP. Ver `skills/diagramas/SKILL.md`.

[Insertar diagrama o referencia al archivo .excalidraw]

### Contenedores

| Contenedor | Tecnologia | Responsabilidad | Tipo |
|---|---|---|---|
| [Nombre] | [Tech] | [Que hace] | API / Worker / DB / Queue / Cache |

## 3. Contratos de Integracion

### Contrato: [Contenedor A] -> [Contenedor B]

| Campo | Valor |
|---|---|
| Protocolo | REST/HTTPS | gRPC | GraphQL | Async/Queue |
| Endpoint/Topic | [ruta o nombre del topic] |
| Formato | JSON | Protobuf | Avro |
| Autenticacion | JWT | API Key | mTLS |
| SLA esperado | [latencia, disponibilidad] |
| Idempotencia | Si/No — [mecanismo] |
| Estrategia de error | Retry con backoff / Circuit breaker / Fallback manual |
| Diseño detallado | -> API-NNN (`templates/api-design-rest.md` o `api-design-graphql.md`) |

### Contrato: [Sistema] -> [Sistema Externo]

| Campo | Valor |
|---|---|
| Proveedor | [nombre] |
| Protocolo | [protocolo] |
| SLA contratado | [SLA] |
| Timeout configurado | [timeout] |
| Fallback | [que pasa si no responde] |

### 3.1 Sub-artefactos de Diseño de API (cuando se expone una API)

Cuando el sistema **expone** una API (sea pública, B2B o entre contextos internos),
crear el sub-artefacto correspondiente y referenciarlo aqui:

| Tipo de API | Cuándo aplica | Sub-artefacto |
|---|---|---|
| **REST + OpenAPI 3.1** (default para APIs de dominio / backend-a-backend / B2B) | Recursos estables, semántica HTTP fuerte, integraciones backend, partners externos | `templates/api-design-rest.md` → `API-NNN` |
| **GraphQL** (default para APIs de **experiencia** web/mobile → backend) | Front-end compone datos de múltiples fuentes, varios clientes, iteración rápida de UI | `templates/api-design-graphql.md` → `API-NNN` |
| **gRPC / async (events)** | Comunicación interna alta-throughput o desacoplada | Documentar en este Tech Spec; sin sub-artefacto dedicado por ahora |

> Politica: para cualquier API en estado **Approved** debe existir el sub-artefacto API-NNN
> con su spec canónico versionado (OpenAPI YAML o GraphQL SDL). Ver `references/_frontmatter.md`
> y `skills/tech-spec/SKILL.md` para el handoff.

| API expuesta por este sistema | Tipo | Sub-artefacto | Versión actual | Estado |
|---|---|---|---|---|
| [ej: `pagos-api`] | REST/OpenAPI | API-001 | v1.0.0 | Draft |
| [ej: `experience-api`] | GraphQL | API-002 | 2026-05-15 | Draft |

## 4. Quality Attribute Trade-offs

| Trade-off | Decision | Justificacion |
|---|---|---|
| Consistencia vs Latencia | [cual priorizamos] | [por que] |
| Seguridad vs Complejidad | [cual priorizamos] | [por que] |

## 5. Fitness Functions

> Ver template completo en `templates/fitness-functions.md`

| Fitness Function | Tipo | Que valida | Automatizacion |
|---|---|---|---|
| [FF-001] | Atomic/Holistic | [atributo] | [como se ejecuta] |

## 6. Politicas a Nivel de Solucion (SA define politica, SWA implementa)

| Politica | Decision SA | SWA implementa |
|---|---|---|
| Errores API REST | "Todos los errores siguen RFC 9457 Problem Details" (ver API-NNN sec. 4) | Framework, middleware, formato exacto |
| Errores API GraphQL | "Errores de dominio en `payload.errors: [UserError!]!`; sistémicos en array `errors` standard" (ver API-NNN sec. 4) | Resolvers, error formatter |
| Versionamiento API REST | "SemVer 2.0.0 + URI (`/v1/`) — 2 MAJOR soportadas — ventana deprecación 12 meses" (ver API-NNN sec. 9) | Routing, backward compat, headers `Deprecation`/`Sunset` |
| Versionamiento API GraphQL | "Evolución continua aditiva, `@deprecated`, breaking detectado en CI con graphql-inspector" (ver API-NNN sec. 9) | Schema registry, CI checks |
| Autenticacion | "JWT con expiracion [X]min, MFA obligatorio" | Middleware, token refresh |
| Secretos | "Todos en vault, rotacion cada [X] dias" | Config de vault, integracion |
| Logging | "Centralizado en [plataforma], correlation-id obligatorio" | Formato JSON, structured fields |
| Idempotencia | "Todas las escrituras aceptan Idempotency-Key (REST) / `clientMutationId` (GraphQL)" | Storage de keys, deduplicacion |

## 7. Decisiones Pendientes

🔴 TODO: [decision que necesita validacion del arquitecto]

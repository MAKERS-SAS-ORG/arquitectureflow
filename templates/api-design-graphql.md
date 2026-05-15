---
titulo: "API Design (GraphQL): [Nombre del API de Experiencia]"
identificador: API-[NNN]
tipo: API-Design
subtipo: GraphQL
estado: Draft
version: "1.0.0"               # SemVer del documento del diseño
version-api: "2026-05-15"       # GraphQL no es SemVer — versionar por fecha o sin versión
autor: "[Nombre del SA]"
fecha-creacion: YYYY-MM-DD
fecha-ultima-revision: YYYY-MM-DD
revisores: []
artefactos-origen: ["TS-NNN", "PRD-NNN"]
stakeholders: []
firmas-roles: []   # MUST firma del Especialista Tecnico + Responsable de Seguridad + Front-end Tech Lead
tags: ["api", "graphql", "experience-api", "bff"]
estandares:
  - GraphQL Spec October 2021 (https://spec.graphql.org/October2021/)
  - GraphQL over HTTP (https://github.com/graphql/graphql-over-http)
  - Relay Cursor Connections Spec (https://relay.dev/graphql/connections.htm)
---

# API Design (GraphQL): [Nombre del API de Experiencia]

> Sub-artefacto de la Tech Spec. El SA define **el contrato de experiencia** que el
> front-end consume: tipos, queries, mutations, suscripciones, política de errores,
> evolución del esquema. El **COMO** (servidor, federación, resolvers, dataloaders)
> es responsabilidad del Especialista Técnico.

## Cuándo usar este template

GraphQL es el **default** para APIs de **experiencia** (web/mobile → backend):

- El front-end necesita **componer datos de múltiples fuentes** en una sola pantalla
- Hay **varios clientes** (web, mobile, partners) con necesidades distintas sobre el mismo dominio
- Se busca **reducir over-fetching / under-fetching** que tendría una API REST genérica
- El equipo de UX itera rápido en pantallas y el contrato debe acompañar sin breaking changes

> **NO** usar GraphQL para APIs de dominio backend-a-backend, integraciones B2B, o flujos
> con semántica HTTP fuerte (caching CDN agresivo, RFC-friendly). Para esos usar
> `templates/api-design-rest.md`.

## Roles colaboradores

| Rol | Que aporta al SA | Cuándo consultarlo |
|---|---|---|
| **Front-end Tech Lead** | **Principal** — necesidades reales de las pantallas, granularidad, modelos de paginación, optimismo UI | Secciones 2-4 (tipos, queries, mutations) |
| **Especialista Técnico** (SWA) | Origen de datos por campo, costo de cada resolver, riesgo de N+1, federación si aplica | Secciones 2-3 (tipos, fuentes), Sección 7 (rendimiento) |
| **Responsable de Seguridad** | Auth/AuthZ a nivel de campo, control de profundidad/complejidad, exposición de PII en errores | Sección 6 (seguridad) y cruce con STRIDE en SD-NNN |
| **DevOps / SRE** | Métricas por operation, persisted queries, throttling, observabilidad | Sección 7 (observabilidad/SLOs) |
| **UX / Producto** | Qué pantallas resuelve el contrato (NO listas de campos sueltos) | Sección 1 (casos de uso) |
| **QA** | Test de queries por escenario UX, contract testing | Sección 8 (testeabilidad) |

## 1. Identidad y casos de uso

| Campo | Valor |
|---|---|
| Nombre lógico | [ej: `experience-api`] |
| Endpoint | `https://api.[dominio]/graphql` (HTTPS, **único endpoint**) |
| Subscriptions endpoint | `wss://api.[dominio]/graphql` o GraphQL SSE |
| Esquema canónico | `schema/[nombre].graphql` (SDL) |
| Audiencia | Web SPA / Mobile / Partners |
| Servicios backend que agrega | [referencia containers en TS-NNN sec. 2] |
| Patrón | BFF (Backend for Frontend) / Federación / Monolítico |

### Casos de uso UX que el API resuelve

> El SA describe **pantallas**, no campos sueltos. Esto fuerza modelar por experiencia, no por tabla.

| Pantalla / flujo UX | Datos que necesita en una sola query | Operations involucradas |
|---|---|---|
| [ej: Detalle de Portafolio] | Saldo total + lista de inversiones + última actividad + alertas | `portfolio(userId)` |
| [ej: Wizard de compra] | Catálogo filtrable + tasas vigentes + perfil de riesgo | `availableProducts`, `userRiskProfile` |
| [ej: Notificaciones live] | Stream de eventos del usuario | `subscription notifications` |

## 2. Tipos del dominio expuestos

> El esquema GraphQL es **un modelo de la experiencia**, no del dominio de backend.
> El front consume tipos pensados para pantallas; los servicios backend exponen sus
> propios contratos (REST/gRPC) que el GraphQL agrega.

| Tipo | Representa | Fuente(s) de datos | Notas |
|---|---|---|---|
| `User` | El usuario autenticado | `kyc-api`, `auth-api` | Solo se devuelve a sí mismo (control por viewer) |
| `Portfolio` | Vista agregada de inversiones | `portfolio-api`, `pricing-api` | Computado on-demand |
| `Investment` | Una posición individual | `portfolio-api` | -- |
| `Money` | Monto + moneda | -- | Scalar custom o type con `amount: Float!` + `currency: String!` |
| `Connection<T>` | Paginación cursor-based | -- | Sigue Relay Connections Spec |

### Convenciones de tipos

| Convención | Decisión |
|---|---|
| Naming | `PascalCase` para tipos, `camelCase` para campos, `SCREAMING_SNAKE` para enums |
| Nullability | **Default = nullable**. Solo marcar `!` cuando es verdaderamente no-nulo. (Errores parciales > error total) |
| Identificadores | `ID!` (Relay Global Object Identification — base64 de `tipo:id`) |
| Fechas | Custom scalar `DateTime` (ISO 8601 UTC) |
| Dinero | Custom scalar `Money` o type `{ amount, currency }` — NO usar `Float` raw |
| Paginación | **Relay Connections** (`edges`, `node`, `cursor`, `pageInfo`) |
| Filtros | Argumentos tipados (`filter: InvestmentFilter`) — no strings ad-hoc |
| Deprecación | Directiva `@deprecated(reason: "...")` — ver sección 9 |

## 3. Operaciones (queries, mutations, subscriptions)

> Cada operación se diseña para resolver una **pantalla o un caso de uso de UX**, no
> como un getter de un campo aislado.

### 3.1 Queries

| Operation | Propósito UX | Autorización | Costo estimado | SLO p99 |
|---|---|---|---|---|
| `viewer` | Usuario autenticado actual | Requiere JWT | Bajo | < 200ms |
| `portfolio(userId)` | Vista de detalle del portafolio | `viewer.id == userId` o admin | Medio (agrega 3 servicios) | < 400ms |
| `availableProducts(filter)` | Catálogo filtrable | Pública | Bajo (cacheable) | < 200ms |

### 3.2 Mutations

| Operation | Propósito UX | Autorización | Idempotencia |
|---|---|---|---|
| `createInvestmentOrder(input)` | Submit del wizard de compra | `viewer + scope:invest` | `clientMutationId` único por intento |
| `updateProfile(input)` | Editar perfil | `viewer.id == input.userId` | No |

**Patrón obligatorio:** todas las mutations reciben un `input: XxxInput!` y devuelven un `payload: XxxPayload`. Incluir siempre:
- `clientMutationId: ID` para idempotencia (Relay Mutation pattern)
- `errors: [UserError!]!` en el payload para errores **esperables** del dominio (validaciones, reglas de negocio)
- Los errores **inesperados** (auth, sistema, red) usan el array `errors` estándar de GraphQL

### 3.3 Subscriptions

| Operation | Evento UX | Transporte | Persistencia tras desconexión |
|---|---|---|---|
| `notifications(userId)` | Push de notificaciones del usuario | WebSocket / SSE | Cliente reconecta con last-event-id |
| `portfolioUpdated(userId)` | Cambios en precios/saldo | WebSocket | -- |

## 4. Política de errores

GraphQL tiene **dos canales de error**:

| Tipo de error | Canal | Cuándo | Quién lo consume |
|---|---|---|---|
| **Errores de dominio esperables** | Campo `errors: [UserError!]!` dentro del payload de la mutation | Validaciones, reglas de negocio, "ya existe" | UI los muestra al usuario |
| **Errores técnicos / sistémicos** | Array `errors` estándar de GraphQL en la respuesta | Auth, autorización, timeout, error de resolver | UI muestra estado genérico, telemetría los captura |

```graphql
type UserError {
  code: String!          # ej: "INSUFFICIENT_FUNDS"
  message: String!       # mensaje legible (i18n del lado servidor)
  field: [String!]       # path al campo del input que falló
}

type CreateInvestmentOrderPayload {
  order: Investment
  errors: [UserError!]!
  clientMutationId: ID
}
```

> Esta separación viene de Shopify, Relay y otros equipos con APIs GraphQL en producción.
> Evita que un error de validación devuelva HTTP 200 con `data: null` y un error genérico.

## 5. Esquema (SDL canónico)

> El archivo `schema/[nombre].graphql` es el **contrato vinculante**.

Esqueleto mínimo de referencia:

```graphql
"""Identidad y autenticación de quien hace la query."""
type Query {
  viewer: User
  portfolio(userId: ID!): Portfolio
  availableProducts(filter: ProductFilter, first: Int = 20, after: String): ProductConnection!
}

type Mutation {
  createInvestmentOrder(input: CreateInvestmentOrderInput!): CreateInvestmentOrderPayload!
}

type Subscription {
  notifications(userId: ID!): Notification!
}

type User {
  id: ID!
  name: String!
  email: String!
  kycStatus: KycStatus!
}

enum KycStatus {
  NOT_STARTED
  IN_REVIEW
  APPROVED
  REJECTED
}

type Portfolio {
  totalBalance: Money!
  investments(first: Int = 10, after: String): InvestmentConnection!
  lastActivity: DateTime
}

scalar DateTime
scalar Money
```

## 6. Seguridad (Responsable de Seguridad firma)

> Esta sección la define el SA pero **MUST** ser firmada por el Responsable de Seguridad.
> Cruzar con STRIDE en `SD-NNN`.

| Aspecto | Decisión |
|---|---|
| Autenticación | JWT en `Authorization: Bearer ...` (mismo issuer que las APIs REST de dominio) |
| Autorización | Verificación a nivel de **viewer** (cada resolver valida que `viewer` puede ver el campo), no solo a nivel de operation |
| Control de profundidad | Limitar a `maxDepth: 10` para prevenir queries maliciosas |
| Control de complejidad | Calcular costo estático antes de ejecutar; rechazar si excede `maxComplexity: 1000` |
| Rate limiting | Por usuario + por IP, considerando complejidad de la query (no solo conteo) |
| Persisted queries / APQ | **Recomendado** en clientes propios: solo IDs de operaciones pre-aprobadas; bloquea queries arbitrarias |
| Introspección | **Deshabilitada en producción** para APIs propietarias; habilitada en staging |
| Errores | Nunca devolver stack traces, paths internos o nombres de servicios en errores al cliente |
| PII en campos | Campos sensibles solo se resuelven si `viewer` tiene permiso; documentar en `description` |
| Anti-batching abuse | Limitar tamaño de aliases y de batched queries |
| CORS | Allowlist explícito |

## 7. Rendimiento y observabilidad

| Aspecto | Decisión SA |
|---|---|
| N+1 | **MUST** usar DataLoader o equivalente en backend (lo implementa SWA) |
| Caching | Persisted queries + caching por operationName + variables; CDN para queries públicas idempotentes |
| Métricas obligatorias | Latencia por `operationName` (no global), error rate por operación, complejidad p99 |
| Tracing | Apollo Tracing / OTel — span por resolver |
| Logs | Estructurados con `operationName`, `clientName`, `clientVersion`, `traceId`, `userId` (hash) |

### SLOs por tipo de operación

| Grupo | Disponibilidad | Latencia p99 |
|---|---|---|
| Queries (read-only) | 99.9% | < 400ms |
| Mutations | 99.5% | < 1000ms |
| Subscriptions (entrega de evento) | 99.5% | < 2s |

## 8. Testeabilidad

| Tipo de test | Quién ejecuta | Herramienta sugerida (informativo) |
|---|---|---|
| Validación del schema | CI en cada PR | `graphql-cli`, `graphql-inspector` |
| Detección de breaking changes en schema | CI obligatorio en cualquier PR que modifique SDL | `graphql-inspector diff` |
| Contract testing front↔backend | Front + Backend | Snapshots de operaciones, mocks con MSW |
| Carga | DevOps | k6 con persisted queries |
| Fuzzing del schema | QA | `easygraphql-tester`, queries generadas |

## 9. Evolución y deprecación del schema

GraphQL **no usa versionamiento por URL**. La evolución es **continua y aditiva**.

### 9.1 Reglas anti-breaking

| Cambio | ¿Es breaking? | Acción requerida |
|---|---|---|
| Añadir tipo, campo, query, mutation | No | Adelante |
| Añadir argumento **opcional** (con default) | No | Adelante |
| Añadir valor a un enum | **Potencialmente sí** (clientes deben tolerar valores desconocidos) | Anunciar + verificar con `graphql-inspector` |
| Cambiar tipo de campo (`String → Int`, nullable → no-nullable) | **Sí** | Solo via campo nuevo + deprecar el viejo |
| Eliminar campo / tipo / operación | **Sí** | Deprecar primero, esperar ventana, luego eliminar |
| Añadir argumento **requerido** | **Sí** | Añadir como opcional con default; "requerido" solo en una versión nueva del campo |

### 9.2 Mecanismo de deprecación

GraphQL provee la directiva oficial:

```graphql
type Investment {
  amount: Money!
  amountCop: Float @deprecated(reason: "Usar 'amount' (type Money). Sunset: 2026-12-31.")
}
```

Política de deprecación:

| Audiencia | Ventana mínima desde anuncio hasta eliminación |
|---|---|
| Clientes propios (web, mobile internos) | **3 meses** + 2 versiones de app publicadas que dejen de usarlo |
| Partners externos | **12 meses** + notificación directa |

Tooling obligatorio:
- `graphql-inspector` corre en CI y bloquea breaking changes no anunciados
- Métrica de **uso de campos deprecados** por cliente — para saber a quién contactar
- Schema registry (Apollo, Hive, GraphQL Hive) con changelog histórico

### 9.3 Versionamiento del documento de diseño

Aunque el schema GraphQL no use SemVer, **este documento sí**. Usar SemVer del campo `version` para el doc, y `version-api` como fecha (YYYY-MM-DD) que representa el "snapshot del contrato a una fecha".

## 10. Decisiones pendientes

🔴 TODO: [decisión que necesita validación]

## 11. Referencias

- GraphQL Spec (October 2021): https://spec.graphql.org/October2021/
- GraphQL over HTTP: https://github.com/graphql/graphql-over-http
- Relay Cursor Connections: https://relay.dev/graphql/connections.htm
- Relay Mutations: https://relay.dev/docs/guides/graphql-server-specification/#mutations
- Shopify GraphQL Design Tutorial: https://github.com/Shopify/graphql-design-tutorial
- Principled GraphQL: https://principledgraphql.com/
- GraphQL Inspector (CI breaking-change detection): https://graphql-inspector.com/

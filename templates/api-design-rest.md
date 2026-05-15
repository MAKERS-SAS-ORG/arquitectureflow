---
titulo: "API Design (REST/OpenAPI): [Nombre del API]"
identificador: API-[NNN]
tipo: API-Design
subtipo: REST-OpenAPI
estado: Draft
version: "1.0.0"               # SemVer del documento del diseño (no de la API)
version-api: "v1.0.0"           # SemVer publica de la API (lo que ven los consumidores)
autor: "[Nombre del SA]"
fecha-creacion: YYYY-MM-DD
fecha-ultima-revision: YYYY-MM-DD
revisores: []
artefactos-origen: ["TS-NNN", "PRD-NNN"]
stakeholders: []
firmas-roles: []   # MUST firma del Especialista Tecnico + Responsable de Seguridad para Approved
tags: ["api", "rest", "openapi-3.1", "semver"]
estandares:
  - OpenAPI 3.1.0 (https://spec.openapis.org/oas/v3.1.0)
  - Semantic Versioning 2.0.0 (https://semver.org/)
  - RFC 9457 Problem Details for HTTP APIs
  - RFC 8594 Sunset HTTP Header
  - RFC 7234 Deprecation HTTP Header (draft-ietf-httpapi-deprecation-header)
---

# API Design (REST/OpenAPI): [Nombre del API]

> Sub-artefacto de la Tech Spec. El SA define el **QUE** del contrato:
> recursos, operaciones, formatos, política de versiones, ciclo de vida.
> El **COMO** (frameworks, ORMs, generadores) es responsabilidad del Especialista Técnico.

## Cuándo usar este template

- API de **dominio / sistema** (backend ↔ backend, integraciones B2B, APIs publicas)
- Necesidad de contrato máquina-legible (spec → SDKs, mocks, tests)
- Se requiere ciclo de vida formal con deprecación y sunset

> Si el API es **de experiencia** (web/mobile → backend agregando data de múltiples
> fuentes), usar `templates/api-design-graphql.md` en su lugar.

## Roles colaboradores

| Rol | Que aporta al SA | Cuándo consultarlo |
|---|---|---|
| **Especialista Técnico** (SWA / Tech Lead) | Validar recursos vs modelo de datos real, factibilidad de filtros/paginación, generación de stubs desde el spec | Secciones 2-5 (recursos, operaciones, contratos) |
| **Responsable de Seguridad** | Auth/AuthZ por endpoint, scopes/permisos, manejo de datos sensibles en payloads, rate limiting | Sección 6 (Seguridad) y revisión cruzada con STRIDE en System Design |
| **DevOps / SRE** | SLOs por endpoint, cuotas/throttling, observabilidad del contrato | Sección 7 (SLOs & cuotas) |
| **QA** | Contract testing (Pact, Schemathesis), generación de tests desde el spec | Sección 8 (testeabilidad) |
| **Equipo Consumidor** (interno o externo) | Casos de uso reales, granularidad esperada, modelo mental | Sección 2 (recursos) y Sección 9 (deprecación) |

## 1. Identidad del API

| Campo | Valor |
|---|---|
| Nombre lógico | [ej: `pagos-api`] |
| Base URL prod | `https://api.[dominio]/[ruta-base]` |
| Estrategia de versionado | URI (`/v1/`, `/v2/`) **o** Header (`API-Version: 2026-05-15`) — elegir uno y mantener |
| Esquema de versionamiento | **Semantic Versioning 2.0.0** (`MAJOR.MINOR.PATCH`) |
| Formato de spec | OpenAPI 3.1.0 (YAML o JSON — uno como canónico, el otro se genera) |
| Archivo canónico del spec | `openapi/[nombre].yaml` |
| Audiencia | Interna / Partner / Pública |
| Servicio que la expone | [referencia al container en TS-NNN sec. 2] |

### Política de SemVer aplicada a APIs

| Cambio | Bump | Ejemplo |
|---|---|---|
| **MAJOR** (breaking) | Romper compatibilidad: cambiar tipo de un campo, eliminar campo, eliminar endpoint, cambiar status code esperado, cambiar semántica de un parámetro | 1.4.2 → 2.0.0 |
| **MINOR** (additive) | Añadir endpoint, añadir campo opcional, añadir enum value (consumidores deben tolerar valores desconocidos) | 1.4.2 → 1.5.0 |
| **PATCH** (no-functional) | Corregir typos en docs, ejemplos, descripciones, mensajes de error no estructurados | 1.4.2 → 1.4.3 |

> Regla anti-vibecoding: **cualquier breaking change requiere ADR + nueva versión MAJOR**. No se hacen breaking changes "silenciosos" sobre una versión existente, ni siquiera en Draft expuesto a consumidores.

## 2. Recursos y modelo de dominio

Lista de recursos del API y su mapeo al dominio (no al modelo de DB).

| Recurso | URI base | Identificador | Bounded Context (→ CM-NNN) |
|---|---|---|---|
| [Recurso 1] | `/v1/[recursos]` | `id: UUID` | [contexto] |
| [Recurso 2] | `/v1/[recursos]/{id}/[sub]` | `id: UUID` | [contexto] |

### Diagrama del modelo (opcional)

> Mermaid o Excalidraw. **No** es el modelo de DB — es el modelo expuesto al consumidor.

## 3. Operaciones (endpoints)

Tabla resumen. El detalle exhaustivo vive en el spec OpenAPI (`openapi/*.yaml`).

| Método | Path | Operation ID | Auth | Idempotente | Rate limit | SLO p99 | Casos de uso |
|---|---|---|---|---|---|---|---|
| GET | `/v1/[recurso]` | `list[Recurso]s` | JWT scope `read:x` | Sí | 100 rps | < 300ms | Listar con paginación |
| GET | `/v1/[recurso]/{id}` | `get[Recurso]` | JWT scope `read:x` | Sí | 200 rps | < 300ms | Detalle |
| POST | `/v1/[recurso]` | `create[Recurso]` | JWT scope `write:x` + `Idempotency-Key` | Con clave | 50 rps | < 800ms | Crear |
| PATCH | `/v1/[recurso]/{id}` | `update[Recurso]` | JWT scope `write:x` | No | 50 rps | < 800ms | Actualización parcial (RFC 7396 Merge Patch) |
| DELETE | `/v1/[recurso]/{id}` | `delete[Recurso]` | JWT scope `delete:x` | Sí | 10 rps | < 500ms | Borrado lógico |

> El **Operation ID** es el contrato estable que usan los generadores de SDK. NO cambiar entre versiones MINOR/PATCH.

## 4. Convenciones (SA define, SWA implementa)

| Convención | Decisión SA | Justificación / referencia |
|---|---|---|
| Formato de datos | `application/json; charset=utf-8` | Mainstream, herramientas amplias |
| Casing de campos | `camelCase` o `snake_case` (elegir uno) | Consistencia entre todos los endpoints |
| Identificadores | `UUID v7` (time-ordered) | Sortable, sin colisiones, sin info sensible |
| Fechas | ISO 8601 UTC (`2026-05-15T14:32:00Z`) | RFC 3339 |
| Paginación | `cursor` + `limit` (max 100) — devuelve `next_cursor` en body | Estable bajo escrituras concurrentes |
| Filtros | Query params (`?status=active&createdAfter=...`) | Documentado en spec por endpoint |
| Errores | **RFC 9457 Problem Details** — `application/problem+json` con `type`, `title`, `status`, `detail`, `instance` | Estandar industria |
| Códigos HTTP | 2xx éxito, 4xx error del cliente, 5xx error del servidor (NO 200 con `success: false`) | Semantica HTTP |
| Idempotencia | `Idempotency-Key` header en POST/PATCH (UUID por intento), TTL 24h | RFC draft Idempotency-Key |
| HATEOAS | [Sí / No / Solo en recursos navegables] | [justificación] |
| Trazabilidad | `X-Request-Id` header echo + `traceparent` (W3C Trace Context) | Correlación end-to-end |

## 5. Esquemas (referencias al spec OpenAPI)

> El SA define **el qué se intercambia**, no las clases. Los esquemas viven en el spec
> (`openapi/[nombre].yaml#/components/schemas`). Acá listamos los principales.

| Esquema | Campos clave | PII / Datos sensibles | Notas |
|---|---|---|---|
| `[RecursoCreate]` | nombre, tipo, monto | `montoCop` (financiero) | Schema usado en POST |
| `[Recurso]` | id, nombre, estado, createdAt | -- | Schema de respuesta |
| `[Problem]` | type, title, status, detail, instance, traceId | -- | RFC 9457 |

> ⚠️ Para cada campo con PII / dato sensible, escalar al **Responsable de Seguridad** y reflejar en STRIDE (`SD-NNN` sección 3 — Information Disclosure).

## 6. Seguridad (Responsable de Seguridad firma)

> Esta sección la define el SA pero **MUST** ser firmada por el Responsable de Seguridad.
> Insumo cruzado de STRIDE en `SD-NNN`.

| Aspecto | Decisión |
|---|---|
| Autenticación | OAuth 2.1 + OIDC / JWT RS256 / mTLS (elegir y referenciar ADR) |
| Autorización | Scopes por endpoint (ver tabla sec. 3) + claims en JWT (`roles`, `tenantId`) |
| Transporte | TLS 1.3 mandatorio, HSTS, sin downgrade |
| Rate limiting | Por API key + por usuario (ver sec. 3) — 429 con `Retry-After` |
| Anti-abuso | Quotas diarias, captcha en flujos públicos, detección de scraping |
| PII en payloads | [Lista de campos] — todos con masking en logs, encriptados at-rest |
| Audit log | Todos los `write:*` + `delete:*` se persisten con actor + traceId (retención según compliance) |
| CORS | Allowlist explícito de orígenes (no `*` en endpoints autenticados) |
| Headers de seguridad | `Strict-Transport-Security`, `X-Content-Type-Options: nosniff`, sin `Server` exponiendo versión |

## 7. SLOs, cuotas y observabilidad

| Endpoint / grupo | SLO disponibilidad | SLO latencia | Cuota por consumidor | Métrica de éxito |
|---|---|---|---|---|
| Lecturas (`GET *`) | 99.9% | p99 < 300ms | 1000 rpm | `error_rate < 0.1%` |
| Escrituras | 99.5% | p99 < 800ms | 100 rpm | `error_rate < 0.5%` |

Estas métricas deben aparecer en `FF-NNN` (Fitness Functions) como contratos automatizados.

## 8. Testeabilidad

| Tipo de test | Quién lo ejecuta | Herramienta sugerida (informativo) |
|---|---|---|
| Validación del spec | CI (cualquier PR que toque `openapi/`) | Spectral, Redocly CLI |
| Contract testing consumidor↔proveedor | QA + Equipos | Pact, Schemathesis |
| Fuzz / property-based del spec | QA | Schemathesis, Dredd |
| Carga | DevOps | k6, Gatling |

> El SA exige que existan; el SWA elige las herramientas.

## 9. Ciclo de vida y política de deprecación

Esta es la **política contractual** con consumidores. NO opcional para APIs públicas o B2B.

### 9.1 Estados de una versión

```
   Preview (alpha/beta)  →  GA (Generally Available)  →  Deprecated  →  Sunset (retirada)
```

| Estado | Significado | Compromiso de estabilidad | Header `Deprecation` |
|---|---|---|---|
| **Preview** | Pruebas, contrato puede cambiar | Ninguno — uso bajo riesgo | No |
| **GA** | Producción, contrato congelado en SemVer MAJOR.MINOR | Sí — solo cambios MINOR/PATCH backward-compat | No |
| **Deprecated** | Aún funciona, pero hay sucesora | Sí — sigue respondiendo durante la ventana | Sí (`Deprecation: true` + `Sunset: <fecha>`) |
| **Sunset** | Retirada — devuelve `410 Gone` | Ninguno | -- |

### 9.2 Política de soporte simultáneo

| Tipo de API | Versiones MAJOR soportadas a la vez | Ventana mínima de deprecación |
|---|---|---|
| Pública / B2B | **2 versiones MAJOR** (N y N-1) | **12 meses** desde anuncio hasta sunset |
| Interna entre equipos | **2 versiones MAJOR** (N y N-1) | **6 meses** desde anuncio hasta sunset |
| Experimental / Preview | **1 versión** (la última) | **30 días** con aviso |

> Ajustar estos valores al contexto del proyecto y dejar **justificado** en este documento.
> Reflejar en `RO-NNN` (Requisitos Operacionales) los procedimientos.

### 9.3 Mecanismos técnicos de deprecación

Cuando una versión entra en **Deprecated**, el API debe:

1. **Responder los headers de aviso en cada respuesta:**
   ```
   Deprecation: true
   Sunset: Tue, 31 Dec 2026 23:59:59 GMT   ← RFC 8594
   Link: <https://api.[dominio]/v2/recursos>; rel="successor-version"
   Link: <https://docs.[dominio]/migracion-v1-v2>; rel="deprecation"
   ```

2. **Emitir métrica de uso por consumidor** para identificar a quién contactar.

3. **Después del Sunset:** responder `410 Gone` con `Problem Details` que apunte a la nueva versión:
   ```json
   {
     "type": "https://api.[dominio]/errors/version-sunset",
     "title": "API version retired",
     "status": 410,
     "detail": "v1 was retired on 2026-12-31. Use v2.",
     "instance": "/v1/recursos/abc"
   }
   ```

### 9.4 Plan de migración (cuando se anuncia una MAJOR nueva)

| Hito | Cuándo | Acción del proveedor | Acción del consumidor |
|---|---|---|---|
| T0 — Anuncio | Día 0 | Publicar changelog + guía de migración + headers `Deprecation` | Inventariar uso de v(N-1) |
| T0 + 30d | -- | Outreach directo a top consumidores | Empezar migración |
| T0 + 90d | -- | Reporte público de % migrado | -- |
| T0 + 180d | -- | Recordatorio formal + ticket de soporte | Completar migración |
| T0 + ventana | Sunset | Devolver `410 Gone` | -- |

### 9.5 Registro histórico de versiones

| Versión | Estado | GA desde | Deprecated desde | Sunset | ADR / Tech Spec |
|---|---|---|---|---|---|
| v1.x | [GA / Deprecated] | YYYY-MM-DD | YYYY-MM-DD | YYYY-MM-DD | ADR-NNN |
| v2.x | [Preview / GA] | YYYY-MM-DD | -- | -- | ADR-NNN |

## 10. Spec OpenAPI 3.1 (canonical)

> El archivo `openapi/[nombre].yaml` es el **contrato vinculante**. Este documento
> describe las decisiones de diseño; el spec describe el comportamiento exacto.

Esqueleto mínimo del spec (referencia rápida):

```yaml
openapi: 3.1.0
info:
  title: [Nombre del API]
  version: "1.0.0"          # SemVer público de la API
  description: |
    [Una línea sobre el QUE resuelve la API]
  contact:
    name: "[Equipo dueño]"
    email: "[contacto]"
  license:
    name: "[Interna / Propietaria / etc.]"
servers:
  - url: https://api.[dominio]/v1
    description: Producción
  - url: https://api-staging.[dominio]/v1
    description: Staging
tags:
  - name: [Recurso]
    description: [Qué representa]
paths:
  /[recurso]:
    get:
      operationId: list[Recurso]s
      summary: Lista [recursos] paginados
      tags: [[Recurso]]
      parameters:
        - $ref: "#/components/parameters/Cursor"
        - $ref: "#/components/parameters/Limit"
      responses:
        "200":
          description: OK
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/[Recurso]Page"
        "4XX":
          $ref: "#/components/responses/ProblemDetails"
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
  schemas:
    Problem:
      $ref: "https://opensource.zalando.com/problem/schema.yaml#/Problem"
  responses:
    ProblemDetails:
      description: Error siguiendo RFC 9457
      content:
        application/problem+json:
          schema: { $ref: "#/components/schemas/Problem" }
security:
  - bearerAuth: []
```

## 11. Decisiones pendientes

🔴 TODO: [decisión que necesita validación del SA o de un rol no consultado]

## 12. Referencias

- OpenAPI 3.1: https://spec.openapis.org/oas/v3.1.0
- Semantic Versioning 2.0.0: https://semver.org/
- RFC 9457 — Problem Details: https://www.rfc-editor.org/rfc/rfc9457
- RFC 8594 — Sunset HTTP Header: https://www.rfc-editor.org/rfc/rfc8594
- API Improvement Proposals (Google AIPs): https://google.aip.dev/
- Zalando RESTful API Guidelines: https://opensource.zalando.com/restful-api-guidelines/

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
tags: []
---

# Tech Spec: [Nombre del Sistema/Modulo]

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
| Protocolo | REST/HTTPS | gRPC | Async/Queue |
| Endpoint/Topic | [ruta o nombre del topic] |
| Formato | JSON | Protobuf | Avro |
| Autenticacion | JWT | API Key | mTLS |
| SLA esperado | [latencia, disponibilidad] |
| Idempotencia | Si/No — [mecanismo] |
| Estrategia de error | Retry con backoff / Circuit breaker / Fallback manual |

### Contrato: [Sistema] -> [Sistema Externo]

| Campo | Valor |
|---|---|
| Proveedor | [nombre] |
| Protocolo | [protocolo] |
| SLA contratado | [SLA] |
| Timeout configurado | [timeout] |
| Fallback | [que pasa si no responde] |

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
| Errores API | "Todos los errores siguen RFC 7807 Problem Details" | Framework, middleware, formato exacto |
| Versionamiento API | "URL-based: /v1/, /v2/" o "Header-based" | Routing, backward compat |
| Autenticacion | "JWT con expiracion [X]min, MFA obligatorio" | Middleware, token refresh |
| Secretos | "Todos en vault, rotacion cada [X] dias" | Config de vault, integracion |
| Logging | "Centralizado en [plataforma], correlation-id obligatorio" | Formato JSON, structured fields |
| Idempotencia | "Todas las escrituras aceptan Idempotency-Key" | Storage de keys, deduplicacion |

## 7. Decisiones Pendientes

🔴 TODO: [decision que necesita validacion del arquitecto]

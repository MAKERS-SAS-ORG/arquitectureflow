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

## 6. Convenciones a Nivel de Solucion

- Nomenclatura de APIs: [convencion]
- Formato de errores: [estructura estandar]
- Versionamiento de APIs: [estrategia]
- Logging: [formato y niveles]
- Secretos: [donde y como se gestionan]

## 7. Decisiones Pendientes

🔴 TODO: [decision que necesita validacion del arquitecto]

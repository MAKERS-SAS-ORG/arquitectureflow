---
titulo: "System Design: [Nombre del Sistema]"
identificador: SD-[NNN]
tipo: System-Design
estado: Draft
version: "1.0.0"
autor: "[Nombre]"
fecha-creacion: YYYY-MM-DD
fecha-ultima-revision: YYYY-MM-DD
revisores: []
artefactos-origen: ["TS-NNN"]
stakeholders: []
firmas-roles: []   # MUST firma de DevOps + Especialista Tecnico + Responsable de Seguridad (STRIDE) para Approved. Ver _frontmatter.md
tags: []
---

# System Design: [Nombre del Sistema]

## Roles colaboradores

> El SA define como escala y como es seguro. **Responsable de Seguridad** es el dueño
> del STRIDE. **Especialista Tecnico** aporta despliegue logico y consecuencias de diseño.
> **DevOps** aporta infraestructura, escalabilidad real y observabilidad.
> Ver diagrama de roles en `README.md`.

| Rol | Que aporta al SA | Cuando consultarlo |
|---|---|---|
| **Responsable de Seguridad** (CISO / Security Architect / AppSec Lead) | **PRINCIPAL — lidera STRIDE en fase de diseño.** Identifica amenazas por componente, evalúa riesgo, propone mitigaciones, valida controles existentes, requisitos de auditoría y compliance | **Sección 3 (STRIDE) — BLOQUEANTE**; revisa sec. 1 (deployment) y sec. 5 (observabilidad de eventos de seguridad). Firma `firmas-roles` para Approved |
| **Especialista Tecnico** (SWA / Tech Lead) | Despliegue logico (que corre donde), patrones de tolerancia a fallos, viabilidad de las mitigaciones propuestas por SEC | Seccion 1 (deployment logico), seccion 3 (STRIDE — como contraparte tecnica) y seccion 9 (decisiones de diseno) |
| **DevOps / SRE / Infra** | Capacidad real de la infraestructura, costos de auto-scaling, plataforma de observabilidad disponible, viabilidad de SLOs | Seccion 2 (rendimiento, disponibilidad, escalabilidad), seccion 5 (observabilidad) y seccion 7 (capacity planning) |
| **QA** | Escenarios de carga y pruebas de resiliencia (chaos / load test) que validan los NFRs; tests de seguridad automatizables (auth bypass, fuzzing) | Seccion 2 (rendimiento) y Sección 3 (validación de mitigaciones STRIDE) |

> ⚠️ **El System Design NO se declara Approved sin firma del Responsable de Seguridad
> en `firmas-roles`** cuando el sistema maneja datos personales, financieros, de salud,
> o cae en regulacion (ver `templates/_frontmatter.md`).

## 1. Diagrama de Arquitectura

> Diagrama C4 L2 Container + Deployment logico generado con Excalidraw MCP.
> SA crea: contenedores, relaciones, deployment logico (que corre donde).
> Operations crea: infra fisica (VPC, subnets, security groups, auto-scaling config).

[Insertar diagrama o referencia]

## 2. Drivers de Arquitectura

### 2.1 Requisitos de Rendimiento
| Escenario | Latencia objetivo | Throughput | Medicion |
|---|---|---|---|
| [Escenario 1] | < [X]ms P99 | [Y] req/seg | [como se mide] |

### 2.2 Disponibilidad y Tolerancia a Fallos
| Componente | Disponibilidad | Estrategia |
|---|---|---|
| [Componente] | [SLO] | [estrategia HA] |

**RPO:** [Recovery Point Objective]
**RTO:** [Recovery Time Objective]

### 2.3 Escalabilidad
| Horizonte | Metrica | Valor | Estrategia |
|---|---|---|---|
| Hoy | [metrica] | [valor] | -- |
| 1 ano | [metrica] | [valor] | [estrategia] |
| 3 anos | [metrica] | [valor] | [estrategia] |

## 3. Seguridad (STRIDE) — Dueño: Responsable de Seguridad

> Referencia: Microsoft STRIDE Threat Modeling — `references/bibliografia.md#stride`
>
> **STRIDE es responsabilidad del Responsable de Seguridad** ejecutada en la fase de
> diseño y arquitectura. El SA facilita la sesión, el SEC lidera la identificación
> de amenazas y el SWA aporta detalle técnico de los componentes. **MUST** firmar
> esta sección antes de promover el SD a Approved.

### 3.1 Activos protegidos

Lista de **activos** del sistema que el modelado de amenazas debe cubrir:

| Activo | Sensibilidad | Regulación aplicable |
|---|---|---|
| [ej: Datos personales del usuario] | Alta (PII) | GDPR / Habeas Data |
| [ej: Saldo y operaciones financieras] | Crítica | SFC / SOX |
| [ej: Tokens de sesión] | Crítica | -- |

### 3.2 Amenazas por componente (STRIDE)

> Hacer una tabla por **container** relevante de la sec. 1, no una sola tabla global.
> El nivel de riesgo se evalúa con el SEC (matriz Likelihood × Impact).

#### Componente: [Container A — ej: API Gateway]

| Amenaza STRIDE | Vector concreto | Likelihood | Impact | Riesgo | Mitigación (decisión SA + SEC) | Validación |
|---|---|---|---|---|---|---|
| **S**poofing — suplantación de identidad | Robo de JWT, replay de credenciales | Alta | Alto | 🔴 Critico | JWT corto (15min) + refresh rotativo + mTLS interno | FF-NNN |
| **T**ampering — alteración de datos en tránsito o reposo | MITM, modificación de payload | Media | Alto | 🟡 Importante | TLS 1.3, HSTS, integridad de payloads firmados | -- |
| **R**epudiation — negación de acciones | Usuario niega haber operado | Alta | Alto | 🔴 Critico | Audit trail inmutable + firma de operaciones críticas | FF-NNN |
| **I**nformation Disclosure — exposición de PII | Logs con datos sensibles, errores verbosos | Media | Alto | 🟡 Importante | Masking en logs, Problem Details genérico, encriptación at-rest | -- |
| **D**enial of Service | Flood al API, queries GraphQL costosas | Alta | Medio | 🟡 Importante | Rate limiting por IP + por user, complexity limit GraphQL, WAF | FF-NNN |
| **E**levation of Privilege | Escalada vertical/horizontal de permisos | Baja | Crítico | 🟡 Importante | Verificación de scope por endpoint, viewer-based authz en GraphQL | -- |

#### Componente: [Container B — repetir la tabla]

| Amenaza STRIDE | Vector | Likelihood | Impact | Riesgo | Mitigación | Validación |
|---|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... | ... |

### 3.3 Trazabilidad de mitigaciones

Cada mitigación crítica debe estar referenciada en:
- **ADR-NNN** si implica una decisión arquitectónica
- **TS-NNN** sec. 6 (Políticas) si es política transversal
- **API-NNN** sec. 6 (Seguridad) si afecta a un API expuesta
- **FF-NNN** si es validable automáticamente

### 3.4 Firmas

| Rol | Persona | Fecha | Decisión |
|---|---|---|---|
| Responsable de Seguridad | [nombre] | YYYY-MM-DD | Aprueba / Aprueba con condiciones / Rechaza |
| Especialista Técnico | [nombre] | YYYY-MM-DD | Acepta implementar |
| Arquitecto de Soluciones | [nombre] | YYYY-MM-DD | Integra al SD |

## 4. Dependencias Externas

| Sistema | SLA contratado | Timeout | Fallback |
|---|---|---|---|
| [Sistema externo] | [SLA] | [timeout] | [fallback] |

## 5. Observabilidad (SA define QUE medir y umbrales; SWA/Ops implementa)

**Plataforma elegida:** [CloudWatch / DataDog / New Relic / etc.] (ver ADR-NNN)

### Metricas criticas que SA define
| Metrica | Umbral de alarma | Por que importa |
|---|---|---|
| Disponibilidad | < [X]% en ventana de 30 dias | SLO comprometido |
| Latencia P99 | > [X]ms | Degradacion de experiencia |
| Tasa de error | > [X]% en ventana de 5 min | Posible incidente |
| Queue depth | > [X] mensajes por [Y] min | Backlog excesivo |

### Lo que SWA/Ops implementa (fuera de scope SA)
- Formato de logs (JSON fields, structured logging)
- Instrumentacion de trazas distribuidas
- Configuracion de dashboards y alertas en la plataforma
- Retencion y rotacion de logs

## 6. SPOFs (Single Points of Failure)

| SPOF | Impacto | Mitigacion actual | Mitigacion pendiente |
|---|---|---|---|
| [componente] | [impacto] | [actual] | [pendiente] |

## 7. Capacity Planning (SA define umbrales y estrategia; Ops ejecuta)

### SA define:
| Recurso | Actual | Proyeccion 6m | Trigger de escalado | Estrategia |
|---|---|---|---|---|
| [recurso] | [actual] | [proyeccion] | [condicion] | Horizontal / Vertical / Auto |

### Ops implementa:
- Configuracion de auto-scaling rules
- Monitoreo de metricas de capacidad
- Ejecucion de scaling manual cuando aplica

## 8. Context Map (DDD)

> Si aplica. Ver `templates/context-map.md` para formato completo.

[Insertar Context Map o referencia]

## 9. Decisiones de Diseno Clave
- ADR-001: [titulo]
- ADR-002: [titulo]

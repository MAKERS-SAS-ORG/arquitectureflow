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
tags: []
---

# System Design: [Nombre del Sistema]

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

## 3. Seguridad (STRIDE)

> Referencia: Microsoft STRIDE Threat Modeling

| Amenaza | Riesgo | Mitigacion |
|---|---|---|
| Spoofing | [nivel] | [mitigacion] |
| Tampering | [nivel] | [mitigacion] |
| Repudiation | [nivel] | [mitigacion] |
| Information Disclosure | [nivel] | [mitigacion] |
| Denial of Service | [nivel] | [mitigacion] |
| Elevation of Privilege | [nivel] | [mitigacion] |

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

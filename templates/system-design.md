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

> Diagrama C4 L2 + Deployment generado con Excalidraw MCP.

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

## 5. Observabilidad

- **Logs:** [plataforma, formato]
- **Metricas:** [plataforma, metricas custom]
- **Trazas:** [plataforma, trazabilidad E2E]
- **Alertas:** [plataforma, canales de notificacion]

### Metricas Criticas con Alarma
| Metrica | Umbral | Accion |
|---|---|---|
| [metrica] | > [valor] | [accion] |

## 6. SPOFs (Single Points of Failure)

| SPOF | Impacto | Mitigacion actual | Mitigacion pendiente |
|---|---|---|---|
| [componente] | [impacto] | [actual] | [pendiente] |

## 7. Capacity Planning

| Recurso | Actual | Proyeccion 6m | Accion si se supera |
|---|---|---|---|
| [recurso] | [actual] | [proyeccion] | [accion] |

## 8. Context Map (DDD)

> Si aplica. Ver `templates/context-map.md` para formato completo.

[Insertar Context Map o referencia]

## 9. Decisiones de Diseno Clave
- ADR-001: [titulo]
- ADR-002: [titulo]

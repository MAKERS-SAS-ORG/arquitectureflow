# Taxonomia de Requisitos No Funcionales (NFRs)

> Referencia: ISO/IEC 25010:2023 — Product Quality Model (SQuaRE)
> Referencia: Bass, L.; Clements, P.; Kazman, R. *Software Architecture in Practice.* 4th Ed. 2021.

---

## Formato de Quality Attribute Scenario (Bass/Kazman)

Cada NFR SHOULD documentarse como un Quality Attribute Scenario medible:

```
Fuente:        [Quien o que genera el estimulo]
Estimulo:      [Que ocurre]
Artefacto:     [Que parte del sistema se ve afectada]
Entorno:       [Bajo que condiciones]
Respuesta:     [Que hace el sistema]
Medida:        [Como se mide que la respuesta fue aceptable]
```

### Ejemplo
```
Fuente:        Usuario autenticado
Estimulo:      Solicita crear una inversion
Artefacto:     API de Inversiones
Entorno:       Operacion normal, hora pico (11:00-13:00)
Respuesta:     El sistema crea la inversion y confirma
Medida:        Latencia < 500ms p99, disponibilidad 99.9%
```

---

## Taxonomia ISO 25010:2023

### 1. Performance Efficiency
| Sub-atributo | Pregunta SA | Ejemplo de medida |
|---|---|---|
| Time behavior | Cual es la latencia aceptable? | < 200ms p99 para API, < 3s para UI |
| Resource utilization | Cuanto recurso es aceptable? | CPU < 70% en pico, memoria < 80% |
| Capacity | Cuantos usuarios/transacciones simultaneas? | 500 req/seg, 10K usuarios concurrentes |

### 2. Reliability
| Sub-atributo | Pregunta SA | Ejemplo de medida |
|---|---|---|
| Availability | Cuanto uptime se requiere? | 99.9% (8.7h downtime/ano), 99.99% (52min/ano) |
| Fault tolerance | Que pasa cuando falla un componente? | Failover automatico < 30s, degradacion graceful |
| Recoverability | Cuanto se puede perder y cuanto tarda recuperar? | RPO: 1 hora, RTO: 4 horas |

### 3. Security
| Sub-atributo | Pregunta SA | Ejemplo de medida |
|---|---|---|
| Confidentiality | Que datos son sensibles? | Cifrado en reposo AES-256, en transito TLS 1.3 |
| Integrity | Como se previene manipulacion? | Audit trail inmutable, checksums |
| Non-repudiation | Se puede negar una accion? | Log de auditoria con firma digital |
| Authenticity | Como se verifica identidad? | JWT + MFA, expiracion 15min |
| Accountability | Quien hizo que y cuando? | Audit log con retencion 7 anos |

### 4. Compatibility
| Sub-atributo | Pregunta SA | Ejemplo de medida |
|---|---|---|
| Interoperability | Con que sistemas debe integrarse? | REST API, eventos async, batch files |
| Co-existence | Puede coexistir con sistemas legacy? | Blue-green deployment, feature flags |

### 5. Maintainability
| Sub-atributo | Pregunta SA | Ejemplo de medida |
|---|---|---|
| Modularity | Cuales son los limites de modulos? | Bounded contexts independientes |
| Modifiability | Cuan facil es cambiar un modulo? | Cambio en modulo X no requiere deploy de Y |
| Testability | Se puede probar independientemente? | Contract tests entre servicios |

### 6. Portability
| Sub-atributo | Pregunta SA | Ejemplo de medida |
|---|---|---|
| Adaptability | Puede funcionar en otro entorno? | Multi-cloud, containerizado |
| Installability | Cuan facil es desplegar? | Despliegue automatizado < 15 min |

### 7. Usability (si aplica al SA)
| Sub-atributo | Pregunta SA | Ejemplo de medida |
|---|---|---|
| Accessibility | Cumple estandares de accesibilidad? | WCAG 2.1 AA |
| Learnability | Cuanto tarda un usuario nuevo? | Onboarding < 5 min para flujo principal |

---

## Priorizacion de NFRs

Usar la tecnica de **Quality Attribute Workshop (QAW)** simplificada:

1. Listar todos los NFRs como quality attribute scenarios
2. Asignar prioridad: Alta (compromete el negocio si falla), Media (degrada la experiencia), Baja (deseable)
3. Identificar trade-offs: "Mayor disponibilidad vs menor costo" — documentar como ADR
4. Incluir en PRD los NFRs de prioridad Alta y Media
5. Definir fitness functions para NFRs de prioridad Alta

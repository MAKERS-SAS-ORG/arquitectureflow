---
titulo: "Fitness Functions: [Nombre del Sistema]"
identificador: FF-[NNN]
tipo: Fitness-Functions
estado: Draft
version: "1.0.0"
autor: "[Nombre]"
fecha-creacion: YYYY-MM-DD
fecha-ultima-revision: YYYY-MM-DD
artefactos-origen: ["TS-NNN"]
tags: []
---

# Architecture Fitness Functions: [Nombre del Sistema]

> Referencia: Ford, N.; Parsons, R.; Kua, P. *Building Evolutionary Architectures.* 2nd Ed. O'Reilly, 2023.
> Definicion: Una fitness function es una evaluacion objetiva y automatizada de alguna
> caracteristica de la arquitectura.
>
> **Fitness Functions como contrato:** Las definiciones del SA (latencia < 200ms,
> retencion de audit trail 7 anos, zero vulnerabilidades criticas) se convierten en
> pruebas automatizadas que el equipo de ingenieria implementa. Asi, las decisiones
> del SA no se quedan en documentos — se vuelven verificaciones objetivas que corren
> en cada deploy y durante toda la vida del sistema.

## Catalogo de Fitness Functions

### FF-001: [Nombre]
| Campo | Valor |
|---|---|
| Atributo de calidad | Performance / Security / Reliability / Coupling / ... |
| Tipo | Atomic (una dimension) / Holistic (multiples dimensiones) |
| Trigger | CI Pipeline / Deployment / Continuo (monitoring) / Manual |
| Metrica | [que se mide] |
| Umbral | [valor aceptable] |
| Herramienta | [como se automatiza] |
| Accion si falla | Bloquear deploy / Alarma / Ticket automatico |

### FF-002: [Nombre]
| Campo | Valor |
|---|---|
| Atributo de calidad | |
| Tipo | |
| Trigger | |
| Metrica | |
| Umbral | |
| Herramienta | |
| Accion si falla | |

## Ejemplos por Atributo de Calidad

### Performance
- Latencia p99 < [X]ms en endpoints criticos (medido con load test en CI)
- Throughput minimo [Y] req/seg bajo carga simulada

### Reliability
- Disponibilidad > [X]% medida en ventana de 30 dias
- Tiempo de recuperacion < [Y] minutos tras fallo simulado

### Security
- Zero vulnerabilidades criticas en SAST/DAST scan
- Todas las APIs requieren autenticacion (test automatizado)
- Datos sensibles cifrados en reposo y transito (audit automatizado)

### Coupling
- Ningun modulo depende directamente de la implementacion interna de otro
- Contratos de API no tienen breaking changes sin versionamiento (contract testing)

### Compliance
- Audit trail completo para todas las operaciones financieras
- Retencion de datos cumple regulacion (verificacion automatizada)

## Dashboard de Fitness Functions

| FF | Estado | Ultima ejecucion | Resultado |
|---|---|---|---|
| FF-001 | Activo | YYYY-MM-DD | PASS / FAIL |
| FF-002 | Pendiente implementacion | -- | -- |

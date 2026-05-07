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
firmas-roles: []   # SHOULD firma de Especialista Tecnico + DevOps + QA. Ver _frontmatter.md
tags: []
---

# Architecture Fitness Functions: [Nombre del Sistema]

## Roles colaboradores

> Las FF son el contrato del SA hecho prueba automatica. El SA define **que medir y umbrales**;
> los demas roles las hacen ejecutables. Ver diagrama de roles en `README.md`.

| Rol | Que aporta al SA | Cuando consultarlo |
|---|---|---|
| **Especialista Tecnico** (SWA / Ingenieria) | Implementa las FF estaticas (NetArchTest, ArchUnit, dependency-cruiser) y dinamicas (k6, JMeter) en el pipeline CI | Definir herramienta en cada ficha FF y al integrar con el pipeline |
| **DevOps / SRE** | Provee las **metricas e informes continuos** (Datadog, CloudWatch, Grafana), configura alertas, dueno del dashboard | Modo "Dinamica" y dashboard de FF (seccion final) |
| **QA** | Valida que los criterios automatizados cubren los Quality Attribute Scenarios del PRD; complementa con casos edge | Mapear cada FF a un QA-Scenario del PRD |
| **Equipo de Desarrollo** | Acepta el bloqueo de deploy cuando una FF falla; reporta falsos positivos | "Accion si falla" (bloquear deploy / alarma) |

> Referencia: Ford, N.; Parsons, R.; Kua, P. *Building Evolutionary Architectures.* 2nd Ed. O'Reilly, 2023.
> Definicion: Una fitness function es una evaluacion objetiva y automatizada de alguna
> caracteristica de la arquitectura.
>
> **Fitness Functions como contrato:** Las definiciones del SA (latencia < 200ms,
> retencion de audit trail 7 anos, zero vulnerabilidades criticas) se convierten en
> pruebas automatizadas que el equipo de ingenieria implementa. Asi, las decisiones
> del SA no se quedan en documentos — se vuelven verificaciones objetivas que corren
> en cada deploy y durante toda la vida del sistema.

## Clasificacion por Modo de Ejecucion

Toda fitness function se clasifica ademas por **como se ejecuta**:

| Modo | Que valida | Cuando corre | Herramientas tipicas |
|---|---|---|---|
| **Estatica** | Reglas estructurales en el codigo (capas, dependencias, convenciones) | Build time / CI en cada PR | NetArchTest, ArchUnit, dependency-cruiser, eslint-plugin-boundaries |
| **Dinamica** | Comportamiento real bajo carga o en produccion (latencia, throughput, disponibilidad) | CI con load test / Monitoring continuo | k6, JMeter, Gatling, CloudWatch, Datadog |
| **Juicio** | Coherencia y vigencia de los artefactos arquitectonicos (.md) | Bajo demanda / Gate de sprint review | Agente IA que analiza artefactos y responde: "el sistema sigue siendo apto (fit)?" |

> **Juicio con Agente IA:** El agente lee los artefactos .md del proyecto (CB, RFC, ADR, Tech Spec,
> System Design, FF) y evalua: consistencia entre artefactos, TODOs criticos sin resolver,
> decisiones que ya no aplican, NFRs sin fitness function, y desviaciones no documentadas.
> No reemplaza las FF estaticas/dinamicas — las complementa con analisis semantico.
>
> **Loop FF-007 -> TAA seccion 4:** los hallazgos de la FF de Juicio MUST cerrarse
> agregandose al **Registro de Desviaciones del Tablero de Adherencia** como entradas
> D-NNN. Sin este loop la FF de Juicio se queda en reporte sin accion. Ver
> `references/protocolo-iteracion.md` seccion "Loop de Retroalimentacion".
> Comando rapido: `/orquestador critica-juicio`.

## Catalogo de Fitness Functions

### FF-001: [Nombre]
| Campo | Valor |
|---|---|
| Atributo de calidad | Performance / Security / Reliability / Coupling / ... |
| Tipo | Atomic (una dimension) / Holistic (multiples dimensiones) |
| Modo | Estatica / Dinamica / Juicio |
| Trigger | CI Pipeline / Deployment / Continuo (monitoring) / Sprint Review |
| Metrica | [que se mide] |
| Umbral | [valor aceptable] |
| Herramienta | [como se automatiza] |
| Accion si falla | Bloquear deploy / Alarma / Ticket automatico / Escalar a SA |

### FF-002: [Nombre]
| Campo | Valor |
|---|---|
| Atributo de calidad | |
| Tipo | |
| Modo | |
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

| FF | Modo | Estado | Ultima ejecucion | Resultado |
|---|---|---|---|---|
| FF-001 | Estatica | Activo | YYYY-MM-DD | PASS / FAIL |
| FF-002 | Dinamica | Pendiente implementacion | -- | -- |
| FF-003 | Juicio | Activo | YYYY-MM-DD | FIT / UNFIT |

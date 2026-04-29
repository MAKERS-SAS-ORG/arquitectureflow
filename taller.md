# Taller Guiado: Arquitectura de Soluciones con ArquitectureFlow

> **Duracion estimada:** 2-3 horas (puede hacerse en multiples sesiones)
> **Nivel:** Arquitecto de soluciones con experiencia basica en herramientas de IA
> **Resultado:** Una arquitectura completa, documentada y lista para entregar a desarrollo

---

## Que vas a lograr

Al terminar este taller tendras:

1. Un flujo completo de arquitectura con 8+ artefactos profesionales
2. Diagramas C4 Level 2 generados con Excalidraw MCP
3. Fitness Functions como contrato automatizable entre arquitectura e ingenieria
4. Un **Tablero de Adherencia Arquitectonica** que te permite rastrear avance e implementacion
5. Experiencia practica usando el orquestador como punto de entrada unico

El taller sigue el mismo problema del ejemplo incluido (`examples/inversion-pasiva/`),
asi puedes comparar tus resultados con los artefactos de referencia en cualquier momento.

---

## Prerequisitos

### Conocimiento previo

- Saber que es un arquitecto de soluciones (el QUE y el POR QUE, no la implementacion)
- Conceptos basicos de C4 Model (Context, Container — no necesitas L3/L4)
- Familiaridad basica con terminal/CLI o un IDE

### Herramientas necesarias

| Herramienta | Para que | Obligatoria |
|---|---|---|
| **Claude Code** o **GitHub Copilot** o **Cursor** | Ejecutar los skills del framework | Si (al menos una) |
| **Git** | Clonar el repo y versionar artefactos | Si |
| **Excalidraw MCP** | Generar diagramas C4 (Fase 5) | Recomendado |
| **Editor de texto** | Revisar y editar artefactos .md | Si |

---

## Paso 0: Instalacion y Setup

### Opcion A: Claude Code (recomendado)

Claude Code lee `CLAUDE.md` automaticamente y conoce todos los skills.
Los skills funcionan nativamente — no hay instalacion adicional.

```bash
# 1. Instalar Claude Code (si no lo tienes)
npm install -g @anthropic-ai/claude-code

# 2. Clonar el framework
git clone https://github.com/MAKERS-SAS-ORG/arquitectureflow.git
cd arquitectureflow

# 3. Crear carpeta para TU proyecto dentro del repo
mkdir -p mi-proyecto

# 4. Abrir Claude Code
claude

# 5. Verificar que los skills estan disponibles
#    Escribe /orquestador — si Claude responde con el flujo de fases, estas listo
```

**Como funcionan los skills en Claude Code:**
- Claude lee `CLAUDE.md` al iniciar y carga las instrucciones del framework
- Los skills viven en `skills/*/SKILL.md` — Claude los carga bajo demanda
- Tu solo escribes `/orquestador` y el framework se encarga del resto
- Los templates en `templates/` se usan automaticamente al crear cada artefacto

### Opcion B: GitHub Copilot

Copilot no tiene skills nativos, pero puedes simular el flujo referenciando los archivos:

```
# Paso 1: Clonar el repo e instalar skills manualmente
git clone https://github.com/MAKERS-SAS-ORG/arquitectureflow.git
cd arquitectureflow

# Paso 2: Configurar Copilot para que lea los skills
#   En VS Code: abrir el proyecto con el repo clonado
#   Copilot Chat leera los archivos cuando se los referencie con @workspace

# Paso 3: (Opcional) Instalar skills via Tessl
curl -fsSL https://get.tessl.io | sh
tessl login
tessl init
tessl install softaworks/agent-toolkit --skill c4-architecture
```

**Como invocar skills en Copilot Chat:**

En lugar de `/orquestador`, usa este patron:

```
@workspace Lee skills/orquestador/SKILL.md y ejecuta la Fase 0.
Necesito disenar un sistema de [tu problema].
```

Para cada artefacto:

```
@workspace Lee skills/rfc/SKILL.md y templates/rfc.md.
Usa el contexto del CB-001.md para generar el RFC.
```

### Opcion C: Cursor

Cursor lee `CLAUDE.md` automaticamente (similar a Claude Code):

```
# 1. Clonar el repo
git clone https://github.com/MAKERS-SAS-ORG/arquitectureflow.git

# 2. Abrir en Cursor
cursor arquitectureflow

# 3. En el chat de Cursor:
/orquestador
```

### Setup del Excalidraw MCP (para diagramas)

Solo necesario cuando llegues a la Fase 5 (diagramas). Puedes avanzar sin esto y agregar diagramas despues.

```bash
# Desde el directorio del framework
cd mcp-excalidraw
npm install

# Iniciar el canvas (cuando necesites generar diagramas)
PORT=3000 npm run canvas

# Abrir http://localhost:3000 en el navegador para ver el canvas en vivo
```

---

## El Problema: Plataforma de Inversion en Renta Fija

> Este taller usa el mismo escenario del ejemplo incluido.
> Puedes comparar tus resultados con `examples/inversion-pasiva/` en cualquier momento.

**Contexto de negocio:**
Eres el Arquitecto de Soluciones de una fintech colombiana. Te piden disenar
una plataforma que permita a personas naturales invertir en CDTs (renta fija)
desde montos tan bajos como $100.000 COP. El mercado es de 8 millones de personas
que hoy no invierten, con una ventana competitiva de 6-9 meses.

**Restricciones:** regulacion financiera SFC, equipo de 5 personas (.NET + AWS),
integraciones con Deceval (custodia), PSE (pagos) y core bancario (KYC).

---

## Paso 1: Iniciar el Orquestador

El orquestador es el unico punto de entrada. Evaluara tu contexto y te guiara
por las fases automaticamente.

### En Claude Code o Cursor

```
Tu:
> /orquestador

Claude:
> Voy a guiarte por el flujo de arquitectura. Empecemos con la Fase 0:
> Context Brief. Necesito entender el contexto de negocio.
> Cuentame: que problema de negocio quieres resolver?
```

### En GitHub Copilot

```
Tu:
> @workspace Lee skills/orquestador/SKILL.md y guiame desde la Fase 0.
> Necesito disenar la arquitectura de una plataforma de inversion en
> renta fija para personas naturales en Colombia.
```

---

## Paso 2: Context Brief (Fase 0 — OBLIGATORIO)

El orquestador te pedira informacion sobre 5 bloques. Dale el contexto de
forma natural — no necesitas llenar la plantilla tu mismo.

### Prompt de ejemplo

```
Tu:
> El problema es que el 78% de los colombianos con capacidad de ahorro no invierte
> porque los CDTs requieren montos minimos altos y procesos complejos.
>
> Queremos permitir micro-inversion en renta fija desde $100k COP.
> Tenemos sandbox aprobado por SFC en Q1 2026 y necesitamos MVP antes de Q4 2026.
>
> El equipo es de 5 ingenieros con experiencia en .NET y AWS.
> Necesitamos integrar con Deceval (custodia), PSE (pagos) y core bancario (KYC).
>
> Stakeholders: Director de Producto (PO), equipo de Compliance, Operaciones
> financieras, y el equipo de ingenieria.
>
> Compliance: Ley 964/2005, Ley 1581/2012, reportes SFC diarios,
> audit trail inmutable con retencion de 10 anos.
>
> Scope IN: onboarding KYC, compra de CDTs, consulta portafolio, redencion automatica.
> Scope OUT: renta variable, mercado secundario, app mobile nativa, robo-advisor, multi-moneda.
```

### Que genera la IA

La IA crea `CB-001.md` siguiendo la plantilla `templates/context-brief.md`.
Revisa especialmente:

- Que el "Costo de NO resolver" tenga numeros concretos (no "es importante")
- Que las restricciones innegociables esten listadas
- Que el scope OUT sea explicito (previene scope creep)

### Tu accion como arquitecto

```
Tu:
> El CB-001 se ve bien. Agrego una restriccion: presupuesto de $1.200M COP
> para desarrollo. Apruebo el Context Brief.

Claude:
> Actualizo CB-001 a estado: Approved. Pasamos a Fase 1: Seleccion de artefactos.
```

**Referencia:** compara tu resultado con `examples/inversion-pasiva/CB-001.md`

---

## Paso 3: Seleccion de Artefactos (Fase 1)

El orquestador consulta `references/matriz-decision.md` y te presenta los
artefactos que aplican.

### Que esperar

```
Claude:
> Segun la matriz de decision para "Nuevo sistema completo":
>
> MUST (obligatorios):
>   - RFC: que opciones tenemos y cual recomendamos
>   - ADR: decisiones criticas irreversibles
>   - PRD: que funcionalidades, con NFRs cuantificados
>   - Tech Spec: stack, contratos, politicas de solucion
>   - System Design: como escala, como es seguro, como se opera
>   - Req. Operacionales: que necesita Ops para operar
>
> SHOULD (recomendados):
>   - Context Map: bounded contexts DDD (hay 3+ integraciones externas)
>   - Fitness Functions: contratos automatizados de los NFRs
>
> No aplica:
>   - Post-Mortem: no hay incidente
>   - System Prompt Spec: no hay LLM en esta fase
>
> Recomiendo empezar con RFC-001. Procedemos?
```

### Tu accion

```
Tu:
> De acuerdo con la seleccion. Procedamos con el RFC.
```

---

## Paso 4: RFC — Request for Comments

El orquestador carga `skills/rfc/SKILL.md` y genera el borrador.

### Prompt de ejemplo

```
Tu:
> /orquestador — genera el RFC-001 para la plataforma de inversion.
> Las opciones que quiero evaluar son:
> A) No hacer nada (baseline)
> B) White-label de un tercero
> C) Construir plataforma propia con integraciones

Claude:
> [Genera RFC-001.md con las 3 opciones, matriz de decision ponderada,
>  analisis de riesgos, y recomendacion de Opcion C]
```

### Critica automatica (Fase 4)

Despues de generar el RFC, la IA aplica critica automaticamente:

```
Claude:
> Critica del RFC-001:
> 🟡 La matriz de decision no pondera "time-to-market" — agregar dado el deadline Q4 2026
> 🟡 Opcion B (white-label): falta analisis de vendor lock-in con regulacion SFC
> 🟢 Considerar un spike de 2 semanas con Deceval antes de comprometerse con Opcion C
```

### Tu accion

```
Tu:
> Buen punto sobre el time-to-market. Agreguemoslo como criterio con peso 20%.
> El vendor lock-in del white-label es un riesgo real — confirmo que Opcion C
> (plataforma propia) sigue siendo la recomendacion.
> Apruebo el RFC-001 con estos ajustes.

Claude:
> RFC-001 actualizado a estado: Approved. Siguiente: ADR-001.
```

**Referencia:** compara con `examples/inversion-pasiva/RFC-001.md`

---

## Paso 5: ADR — Architecture Decision Record

El ADR documenta las decisiones tecnicas irreversibles que emergen del RFC.

### Prompt de ejemplo

```
Tu:
> /orquestador — siguiente artefacto (ADR)
>
> La decision principal es: usamos comunicacion asincrona (event-driven) para
> las integraciones con Deceval y PSE, porque sus APIs tienen latencias
> variables de 1 a 30 segundos y no podemos bloquear al usuario.

Claude:
> [Genera ADR-001.md con formato MADR 4.0:
>  - Decision: Event-driven con SQS + REST API para endpoints sincronos
>  - Opciones: Event-driven vs REST sincrono vs Polling
>  - Justificacion: latencia variable de terceros, experiencia del equipo
>  - Consecuencias: necesidad de worker, idempotencia, reintentos]
```

### Tu accion

```
Tu:
> Correcto. Agrego la consecuencia de que necesitamos un patron de idempotencia
> robusto — cada mensaje debe procesarse exactamente una vez para operaciones
> financieras. Acepto el ADR-001.

Claude:
> ADR-001 estado: Accepted. Siguiente: PRD-001.
```

**Referencia:** compara con `examples/inversion-pasiva/ADR-001.md`

---

## Paso 6: PRD — Product Requirements Document

El PRD define QUE se construye. Como SA, tu enfoque son los NFRs cuantificados
y los Quality Attribute Scenarios (QAS).

### Prompt de ejemplo

```
Tu:
> /orquestador — siguiente artefacto (PRD)
>
> Casos de uso principales:
> 1. Onboarding con KYC (registro + verificacion de identidad)
> 2. Compra de CDT (desde $100k COP, seleccion de plazo y emisor)
> 3. Consulta de portafolio (inversiones activas y rendimientos)
> 4. Redencion automatica al vencimiento
>
> NFRs criticos:
> - Latencia: < 500ms p99 para consultas y operaciones
> - Disponibilidad: 99.5% mensual
> - Seguridad: zero accesos no autorizados, audit trail inmutable
```

### Que esperar de la IA

La IA genera QAS (Quality Attribute Scenarios) en formato ISO 25010:

```
QA-001: Performance
  Fuente: Usuario autenticado
  Estimulo: Solicita compra de CDT
  Artefacto: API de Inversiones
  Entorno: Carga normal (100 req/seg)
  Respuesta: Operacion registrada y confirmacion enviada
  Medida: Latencia < 500ms p99
```

### Tu accion

```
Tu:
> Los QAS estan bien. Agrego reglas de negocio faltantes:
> - Monto minimo de inversion: $100.000 COP
> - KYC obligatorio antes de primera inversion
> - Redencion solo al vencimiento (no anticipada en MVP)
> Paso el PRD a estado Review — necesito validacion del Product Owner.

Claude:
> PRD-001 estado: Review. Siguiente: Tech Spec (TS-001).
```

**Referencia:** compara con `examples/inversion-pasiva/PRD-001.md`

---

## Paso 7: Tech Spec + Diagrama C4

La Tech Spec define el stack, los contratos de integracion y las politicas
de solucion. Aqui es donde se genera el diagrama C4 Level 2.

### Prompt de ejemplo

```
Tu:
> /orquestador — siguiente artefacto (Tech Spec)
>
> Stack definido: .NET 8, AWS (ECS Fargate, SQS, RDS PostgreSQL, S3).
> El equipo tiene experiencia en .NET y AWS — no hay razon para cambiar.
>
> Containers principales que visualizo:
> - API Gateway (punto de entrada)
> - API de Inversiones (.NET)
> - Worker de Eventos (procesa integraciones asincronas)
> - Base de datos (PostgreSQL)
> - Integraciones: Deceval, PSE, Core Bancario, SFC
```

### Que genera la IA

1. **TS-001.md** con:
   - Diagrama C4 L2 (containers y relaciones)
   - Contratos de integracion por sistema externo
   - Politicas: autenticacion (JWT RS256), idempotencia, retry con backoff
   - Tabla "SA define | SWA implementa" para cada politica

2. **Diagrama C4 Level 2** (si tienes Excalidraw MCP):

```
Tu:
> /orquestador — genera el diagrama C4 L2 para la Tech Spec

Claude:
> Cargando skills/diagramas/SKILL.md...
> Generando diagrama con Excalidraw MCP en http://localhost:3000
> [Crea containers, relaciones y sistemas externos en el canvas]
> Diagrama guardado como c4-container-diagram.excalidraw
```

Si **no tienes Excalidraw MCP**, la IA genera un diagrama Mermaid inline:

```
Tu:
> No tengo Excalidraw MCP. Genera el diagrama en Mermaid.

Claude:
> [Genera bloque Mermaid con C4 L2 que puedes renderizar en cualquier visor]
```

### Tu accion

```
Tu:
> La Tech Spec cubre bien los contratos. Dos ajustes:
> 1. Agregar timeout de 30s para llamadas a Deceval (su SLA lo permite)
> 2. El Worker necesita DLQ (dead letter queue) para mensajes fallidos
> Paso a Review.

Claude:
> TS-001 actualizado. Estado: Review. Siguiente: System Design (SD-001).
```

**Referencia:** compara con `examples/inversion-pasiva/TS-001.md`

---

## Paso 8: System Design

El System Design cubre: como escala, como es seguro, como se observa y opera.

### Prompt de ejemplo

```
Tu:
> /orquestador — siguiente artefacto (System Design)
>
> Prioridades para este diseno:
> - STRIDE threat model (es sistema financiero, seguridad es critica)
> - SLO: 99.5% disponibilidad mensual
> - Observabilidad: que metricas necesita Ops desde dia 1
> - Capacity planning para 50k usuarios en el primer ano
```

### Que genera la IA

- Modelo de amenazas STRIDE por componente
- SLOs/SLAs con error budget
- Estrategia de observabilidad (metricas, logs, traces)
- Capacity planning con proyecciones
- SPOFs (puntos unicos de falla) y mitigaciones
- Estrategia de deployment (blue-green)

### Tu accion

```
Tu:
> El STRIDE esta completo. Agrego: el audit trail es un SPOF —
> si el servicio de auditoria falla, la operacion financiera NO debe proceder
> (fail-closed, no fail-open). Esto es requisito regulatorio.
> Paso a Draft — necesito mas iteracion con Ops.
```

**Referencia:** compara con `examples/inversion-pasiva/SD-001.md`

---

## Paso 9: Artefactos Complementarios

### Requisitos Operacionales (RO-001)

```
Tu:
> /orquestador — siguiente artefacto (Requisitos Operacionales)
>
> Necesito definir: metricas criticas, umbrales de alarma,
> estrategia de deployment y criterios de rollback.
> El equipo de Ops llenara los procedimientos — yo defino los requisitos.
```

### Context Map (CM-001)

```
Tu:
> /orquestador — genera el Context Map DDD
>
> Los bounded contexts que identifico:
> - Portafolio (inversiones, rendimientos)
> - KYC (identidad, verificacion)
> - Custodia (integracion con Deceval)
> - Pagos (integracion con PSE/ACH)
> - Compliance (auditoria, reportes SFC)
```

### Fitness Functions (FF-001)

```
Tu:
> /orquestador — genera las Fitness Functions
>
> Quiero contratos automatizados para:
> - Latencia < 500ms p99 (del QA-001 del PRD)
> - Zero vulnerabilidades criticas (seguridad)
> - Audit trail 100% completo (compliance)
> - Aislamiento de datos por usuario (STRIDE)
> - Disponibilidad > 99.5% (SLO del System Design)
> - Desacoplamiento entre bounded contexts (Context Map)
> - Coherencia de artefactos (que un agente IA valide los .md)
```

Las Fitness Functions se clasifican por **modo de ejecucion**:

| Modo | Que valida | Herramienta tipica |
|---|---|---|
| **Estatica** | Reglas estructurales en el codigo (capas, dependencias) | NetArchTest, ArchUnit |
| **Dinamica** | Comportamiento real bajo carga o en produccion | k6, JMeter, CloudWatch |
| **Juicio** | Coherencia y vigencia de los artefactos arquitectonicos (.md) | Agente IA |

La FF de **Juicio** es clave: un agente IA lee los artefactos del proyecto y responde
"el sistema sigue siendo apto (fit)?". Detecta TODOs sin resolver, ADRs que contradicen
la Tech Spec, NFRs sin FF automatizada, y desviaciones no documentadas.

**Referencia:** compara con los archivos en `examples/inversion-pasiva/`

---

## Paso 10: Tablero de Adherencia Arquitectonica

Este es el artefacto que responde: **como sabemos que la implementacion sigue
la arquitectura?** Es el "plano de avance" entre el SA y el equipo de desarrollo.

### Que es el Tablero de Adherencia (TAA)

El TAA es un documento vivo que contiene:

1. **Estado de artefactos** — que tenemos, en que estado, que falta
2. **Mapa de trazabilidad** — cada decision arquitectonica mapeada a modulos de codigo
3. **Gates de revision** — checkpoints por sprint para validar alineacion
4. **Registro de desviaciones** — cuando el equipo se desvia, se documenta y justifica
5. **Dashboard de Fitness Functions** — estado de automatizacion de cada FF

### Prompt de ejemplo

```
Tu:
> /orquestador — genera el Tablero de Adherencia Arquitectonica para
> la plataforma de inversion. Usa la plantilla templates/tablero-adherencia.md.
> Incluye todos los artefactos que hemos creado y las fitness functions.
```

### El TAA generado tendra este aspecto

#### Estado de Artefactos

| # | Artefacto | ID | Estado | Version |
|---|---|---|---|---|
| 0 | Context Brief | CB-001 | Approved | 1.0.0 |
| 1 | RFC | RFC-001 | Approved | 1.0.0 |
| 2 | ADR | ADR-001 | Accepted | 1.0.0 |
| 3 | PRD | PRD-001 | Review | 1.0.0 |
| 4 | Tech Spec | TS-001 | Review | 1.0.0 |
| 5 | System Design | SD-001 | Draft | 1.0.0 |
| 6 | Req. Operacionales | RO-001 | Draft | 1.0.0 |
| 7 | Context Map | CM-001 | Draft | 1.0.0 |
| 8 | Fitness Functions | FF-001 | Draft | 1.0.0 |
| 9 | Diagrama C4 L2 | c4-container | Generado | -- |

#### Criterio de Arquitectura Suficiente

- [x] Context Brief aprobado (CB-001)
- [x] RFC aprobado con stakeholders (RFC-001)
- [x] ADRs criticos aceptados (ADR-001)
- [ ] PRD aprobado con Product Owner (PRD-001 en Review)
- [ ] Tech Spec en Review con diagrama C4 L2 (TS-001 en Review)
- [x] Fitness Functions definidas (FF-001)
- [ ] Sin TODOs criticos pendientes

> **Estado: 4/7 criterios cumplidos.** Ingenieria puede comenzar trabajo
> exploratorio pero NO features criticos hasta que PRD y Tech Spec esten aprobados.

#### Mapa de Trazabilidad

| Decision | Que dice la arquitectura | Modulo(s) | Implementado | Validacion |
|---|---|---|---|---|
| ADR-001 | Event-driven con SQS para integraciones | Worker.Events | No | FF-006 |
| TS-001 sec. Auth | JWT RS256, expiracion 15 min | API.Auth | No | FF-002 |
| TS-001 sec. Idempotencia | IdempotencyKey en header, dedup en DB | API.Inversiones | No | Manual |
| PRD-001 QA-001 | Latencia < 500ms p99 | API completa | No | FF-001 |
| PRD-001 QA-003 | Zero accesos no autorizados | API completa | No | FF-004 |
| PRD-001 RN-003 | Audit trail inmutable | Worker.Audit | No | FF-003 |
| CM-001 | 5 bounded contexts separados | Todos los modulos | No | FF-006 |

#### Dashboard de Fitness Functions

| FF | Atributo | Implementacion | Automatizado | Resultado |
|---|---|---|---|---|
| FF-001 | Performance | Pendiente | Pipeline CI | -- |
| FF-002 | Security | Pendiente | Pipeline CI | -- |
| FF-003 | Compliance | Pendiente | Pipeline deploy | -- |
| FF-004 | Security | Pendiente | Pipeline CI | -- |
| FF-005 | Reliability | Pendiente | Monitoring | -- |
| FF-006 | Coupling | Pendiente | Pipeline CI | -- |

### Como se usa el TAA durante el desarrollo

**Sprint 1:** El equipo implementa API.Auth y Worker.Events

```
Tu (SA, en sprint review):
> Actualizo el TAA:
> - ADR-001 (event-driven): Implementado = Si
> - TS-001 Auth (JWT RS256): Implementado = Parcial (falta refresh token)
> - FF-002 (security scan): En CI, PASS
> - FF-006 (desacoplamiento): En CI, PASS
```

**Sprint 3:** Un desarrollador necesita desviarse de la arquitectura

```
Desarrollador:
> No podemos usar SQS para la notificacion de redencion — necesitamos
> respuesta sincrona porque Deceval confirma en < 2 segundos en este flujo.

Tu (SA):
> Registro desviacion D-001: comunicacion sincrona para redencion en lugar
> de event-driven. Justificacion: Deceval confirma en < 2s para este caso.
> Impacto: Bajo (solo un flujo, el patron general se mantiene).
> Resolucion: Aceptar deuda tecnica, evaluar en sprint 6.
```

---

## Resultado Final: Tu Arquitectura Completa

Al completar el taller, tu carpeta de proyecto tendra esta estructura:

```
mi-proyecto/
|-- CB-001.md                    # Context Brief (Approved)
|-- RFC-001.md                   # Request for Comments (Approved)
|-- ADR-001.md                   # Decision: event-driven (Accepted)
|-- PRD-001.md                   # Product Requirements (Review -> Approved)
|-- TS-001.md                    # Tech Spec (Review -> Approved)
|-- SD-001.md                    # System Design (Draft -> Review)
|-- RO-001.md                    # Requisitos Operacionales (Draft)
|-- CM-001.md                    # Context Map DDD (Draft)
|-- FF-001.md                    # Fitness Functions (Draft)
|-- TAA-001.md                   # Tablero de Adherencia (Draft — vivo)
|-- c4-container-diagram.excalidraw  # Diagrama C4 L2
```

### El flujo completo visualizado

```
    /orquestador
         |
    Fase 0: CB-001 (Approved)
         |
    Fase 1: Seleccion → RFC, ADR, PRD, TS, SD, RO, CM, FF
         |
    Fase 2-3: Creacion iterativa
         |
         |── RFC-001 (Approved)         ← Que opciones y recomendacion
         |── ADR-001 (Accepted)         ← Decision event-driven
         |── PRD-001 (Review→Approved)  ← NFRs cuantificados + QAS
         |── TS-001  (Review→Approved)  ← Stack, contratos, politicas
         |── SD-001  (Draft→Review)     ← STRIDE, SLOs, capacity
         |── RO-001  (Draft)            ← Metricas, alarmas, rollback
         |── CM-001  (Draft)            ← Bounded contexts DDD
         |── FF-001  (Draft)            ← Contratos automatizados
         |
    Fase 4: Critica automatica (en cada artefacto)
         |
    Fase 5: Diagramas C4 L2 (Excalidraw MCP)
         |
    Fase 6: Consistencia entre artefactos
         |
    TAA-001: Tablero de Adherencia ← PUENTE hacia desarrollo
         |
         |── Estado de artefactos    → "Que tenemos y que falta"
         |── Mapa de trazabilidad    → "Decision → Modulo → Validacion"
         |── Gates de revision       → "Checkpoints por sprint"
         |── Registro desviaciones   → "Donde nos desviamos y por que"
         |── Dashboard FF            → "Que esta automatizado"
         |
    DESARROLLO INICIA
         |
    (El TAA se actualiza cada sprint)
```

---

## Como saber que estamos listos

### Para iniciar desarrollo (arquitectura suficiente)

Revisar la seccion "Criterio de Arquitectura Suficiente" del TAA-001.
Minimo necesitas:

- [x] Context Brief aprobado
- [x] RFC aprobado
- [x] ADRs criticos aceptados
- [x] PRD aprobado (NFRs cuantificados)
- [x] Tech Spec con C4 L2
- [x] Fitness Functions definidas

### Para saber si la implementacion esta alineada

Revisar estas secciones del TAA-001 en cada sprint:

| Pregunta | Donde mirar en el TAA |
|---|---|
| Que artefactos estan listos? | Seccion 1: Estado de Artefactos |
| Que decisiones ya se implementaron? | Seccion 2: Mapa de Trazabilidad |
| Estamos revisando en cada sprint? | Seccion 3: Gates de Revision |
| Nos desviamos de la arquitectura? | Seccion 4: Registro de Desviaciones |
| Las fitness functions estan automatizadas? | Seccion 5: Dashboard de FF |
| Como le explico al sponsor? | Seccion 6: Resumen Ejecutivo |

### Ciclo de vida del TAA

```
Creacion (SA genera al terminar artefactos)
    |
    v
Sprint Planning (SA + Tech Lead revisan gates)
    |
    v
Durante Sprint (Tech Lead actualiza trazabilidad, devs registran desviaciones)
    |
    v
Sprint Review (SA actualiza estado, valida alineacion)
    |
    v
Mensual (SA revisa consistencia general, actualiza resumen ejecutivo)
```

---

## FAQ

### Puedo empezar por un artefacto que no sea el RFC?

Si. El orquestador soporta excepciones documentadas:
- Decision urgente → empezar con ADR
- Incidente → empezar con Post-Mortem
- Spike tecnico → RFC lite

Pero SIEMPRE necesitas el Context Brief primero.

### Que pasa si no tengo Excalidraw MCP?

Puedes generar diagramas en Mermaid como alternativa. La IA generara bloques
Mermaid inline que puedes renderizar en cualquier visor compatible.
El diagrama Excalidraw es preferido para presentaciones a stakeholders.

### Cuantas sesiones necesito para completar el taller?

Puedes hacerlo en una sesion de 2-3 horas, o dividirlo:
- Sesion 1: CB + RFC + ADR (~45 min)
- Sesion 2: PRD + Tech Spec + Diagrama (~60 min)
- Sesion 3: System Design + RO + CM + FF + TAA (~60 min)

### Puedo usar el framework para un proyecto diferente al ejemplo?

Si — ese es el objetivo. El taller usa el ejemplo de inversion para que puedas
comparar resultados, pero una vez que entiendas el flujo, usa `/orquestador`
con TU problema de negocio y el framework te guia igual.

### Que pasa si la arquitectura cambia despues de empezar desarrollo?

Es normal y esperado. El framework maneja esto con:
- **Registro de desviaciones** en el TAA (seccion 4)
- **Supersesion de artefactos** (ADR-002 supersede ADR-001)
- **Fitness Functions** que detectan violaciones automaticamente
- **Triggers de refactoring** documentados en `references/niveles-madurez.md`

### Cual es la diferencia entre Fitness Functions y el TAA?

Las **Fitness Functions** (FF-001) definen QUE medir y los umbrales — son el
contrato tecnico que se automatiza en CI/CD.

El **Tablero de Adherencia** (TAA-001) es la vista completa de gobernanza:
incluye las FF pero tambien el estado de artefactos, la trazabilidad de
decisiones, los gates de revision y las desviaciones. Es el artefacto que
el SA usa para comunicar con stakeholders y con el equipo de desarrollo.

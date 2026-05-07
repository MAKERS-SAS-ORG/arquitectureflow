---
titulo: "Tablero de Adherencia Arquitectonica: [Nombre del Sistema]"
identificador: TAA-[NNN]
tipo: Tablero-Adherencia
estado: Draft
version: "1.0.0"
autor: "[Nombre]"
fecha-creacion: YYYY-MM-DD
fecha-ultima-revision: YYYY-MM-DD
artefactos-origen: ["CB-NNN"]
tags: []
---

# Tablero de Adherencia Arquitectonica: [Nombre del Sistema]

> **Proposito:** Este artefacto es el puente entre la arquitectura documentada y la
> implementacion. Permite al SA y al equipo de desarrollo rastrear (1) el avance de
> la arquitectura, (2) la alineacion del codigo con las decisiones arquitectonicas,
> y (3) las desviaciones justificadas.
>
> Se actualiza en cada sprint/ciclo de desarrollo. Es un documento vivo.

---

## Roles colaboradores

> El TAA es donde **todos** los roles se reunen alrededor del SA. Cada gate tiene un dueno
> operativo distinto. Ver diagrama de roles en `README.md`.

| Rol | Que aporta al SA | Donde colabora en el TAA |
|---|---|---|
| **Especialista Tecnico** (SWA / Tech Lead) | Llena la columna "Modulo afectado" del mapa de trazabilidad; lidera **Gate 2: Code Review Arquitectonico** | Seccion 2 (trazabilidad) y seccion 3 — Gate 2 |
| **DevOps / SRE** | Lidera **Gate 3: Pre-Deploy** (FF en CI, alarmas, criterios de rollback) y **Gate 4: Post-Deploy / Review Mensual** (SLOs reales) | Seccion 3 — Gates 3 y 4; seccion 5 (dashboard FF) |
| **QA** | Aporta cobertura de tests por decision; firma criterios de aceptacion en **Gate 1: Sprint Planning** | Seccion 3 — Gate 1; seccion 5 (FF de QA) |
| **Equipo de Desarrollo** | **Registra desviaciones** en seccion 4 con justificacion; ejecuta acciones derivadas | Seccion 4 (registro de desviaciones) — entrada principal |
| **Acelerador / PO** | Lee la seccion 6 (resumen ejecutivo) y firma riesgo arquitectonico aceptable | Seccion 6 (resumen ejecutivo) |

> El SA modera. Los demas roles llenan. Sin ellos el TAA es teoria.

---

## 1. Estado de Artefactos Arquitectonicos

> Vista rapida: que tenemos, en que estado esta, y que falta.

| # | Artefacto | Identificador | Estado | Version | Revisor | Fecha |
|---|---|---|---|---|---|---|
| 0 | Context Brief | CB-NNN | Draft / Review / Approved | 1.0.0 | -- | -- |
| 1 | RFC | RFC-NNN | -- | -- | -- | -- |
| 2 | ADR(s) | ADR-NNN | -- | -- | -- | -- |
| 3 | PRD | PRD-NNN | -- | -- | -- | -- |
| 4 | Tech Spec | TS-NNN | -- | -- | -- | -- |
| 5 | System Design | SD-NNN | -- | -- | -- | -- |
| 6 | Req. Operacionales | RO-NNN | -- | -- | -- | -- |
| 7 | Context Map | CM-NNN | -- | -- | -- | -- |
| 8 | Fitness Functions | FF-NNN | -- | -- | -- | -- |
| 9 | Diagrama C4 L2 | -- | -- | -- | -- | -- |

### Leyenda de estados

| Estado | Significado | Icono |
|---|---|---|
| No iniciado | Artefacto identificado pero no creado | -- |
| Draft | Trabajo en progreso, puede cambiar | :pencil2: |
| Review | Listo para feedback de stakeholders | :mag: |
| Approved | Aceptado como referencia | :white_check_mark: |
| Superseded | Reemplazado por version nueva | :arrows_counterclockwise: |

### Criterio de "Arquitectura Suficiente"

Checklist minimo para que el equipo de desarrollo pueda iniciar implementacion:

- [ ] Context Brief aprobado (CB-NNN)
- [ ] RFC aprobado con stakeholders (RFC-NNN)
- [ ] ADRs criticos aceptados (decisiones irreversibles documentadas)
- [ ] PRD aprobado con Product Owner (NFRs cuantificados)
- [ ] Tech Spec en Review con diagrama C4 L2 (TS-NNN)
- [ ] Fitness Functions definidas para NFRs criticos (FF-NNN)
- [ ] Sin 🔴 TODOs criticos pendientes en artefactos Approved

> Cuando este checklist se cumple, el equipo puede empezar a codear.
> Los artefactos restantes (System Design, Runbook) pueden completarse en paralelo.

---

## 2. Mapa de Trazabilidad: Decision -> Implementacion

> Conecta cada decision arquitectonica con su impacto en el codigo.
> El SA llena la columna de decision; el tech lead llena modulo y estado.

| Decision (ADR/TS) | Que dice la arquitectura | Modulo(s) afectado(s) | Implementado | Validacion |
|---|---|---|---|---|
| ADR-NNN: [titulo] | [resumen de la decision] | [modulo.componente] | Si / No / Parcial | FF-NNN / Manual / N/A |
| TS-NNN sec. X | [politica o contrato] | [modulo.componente] | Si / No / Parcial | FF-NNN / Manual / N/A |
| PRD-NNN QA-NNN | [NFR cuantificado] | [endpoint/servicio] | Si / No / Parcial | FF-NNN |

### Ejemplo

| Decision | Que dice la arquitectura | Modulo(s) | Implementado | Validacion |
|---|---|---|---|---|
| ADR-001: Event-driven | Comunicacion asincrona entre servicios via SQS | Worker.Events | Si | FF-006 |
| TS-001 sec. 5.1 | JWT con RS256, token expira en 15 min | API.Auth | Parcial | FF-002 |
| PRD-001 QA-001 | Latencia < 500ms p99 | API.Inversiones | No | FF-001 |

---

## 3. Gates de Revision Arquitectonica

> Checkpoints donde el SA valida que la implementacion sigue alineada.
> Configurar estos gates en el flujo de desarrollo del equipo.

### Gate 1: Sprint Planning

**Cuando:** Al inicio de cada sprint/ciclo
**Quien:** SA + Tech Lead
**Que revisar:**

- [ ] Las historias del sprint estan alineadas con el scope del PRD
- [ ] Si hay decisiones tecnicas nuevas, existe ADR o se necesita uno
- [ ] Los bounded contexts del Context Map se respetan en la asignacion de trabajo
- [ ] No hay conflictos con restricciones documentadas en CB/TS

### Gate 2: Code Review Arquitectonico

**Cuando:** PRs que tocan limites de bounded context, integraciones, o seguridad
**Quien:** SA o delegado arquitectonico
**Que revisar:**

- [ ] El PR respeta los contratos de integracion definidos en la Tech Spec
- [ ] No hay dependencias directas entre bounded contexts (viola CM-NNN)
- [ ] Patrones de seguridad siguen STRIDE del System Design
- [ ] Si hay desviacion de la arquitectura, esta documentada en seccion 4

### Gate 3: Pre-Deploy

**Cuando:** Antes de cada deploy a staging/produccion
**Quien:** Automatizado (CI/CD) + SA en primer deploy
**Que revisar:**

- [ ] Fitness Functions del pipeline CI pasan (FF-NNN)
- [ ] Metricas de observabilidad configuradas segun Req. Operacionales
- [ ] Criterios de rollback definidos y probados
- [ ] Alarmas configuradas segun umbrales del System Design

### Gate 4: Post-Deploy / Review Mensual

**Cuando:** 1 semana despues de deploy significativo o mensualmente
**Quien:** SA + Tech Lead + Ops
**Que revisar:**

- [ ] SLOs del System Design se estan cumpliendo
- [ ] Fitness Functions continuas (monitoring) reportan dentro de umbrales
- [ ] No hay deuda arquitectonica no documentada
- [ ] Actualizar este tablero con el estado real

---

## 4. Registro de Desviaciones Arquitectonicas

> Cuando el equipo se desvia de la arquitectura documentada, registrar aqui.
> Desviar NO es malo — lo malo es desviar sin documentar y sin justificar.
> Una desviacion justificada puede convertirse en un nuevo ADR.

| # | Fecha | Artefacto afectado | Desviacion | Justificacion | Impacto | Resolucion |
|---|---|---|---|---|---|---|
| D-001 | YYYY-MM-DD | ADR-NNN / TS-NNN | [que cambio vs lo documentado] | [por que fue necesario] | Alto / Medio / Bajo | ADR nuevo / Actualizar TS / Aceptar deuda |

### Flujo de desviacion

```
Desarrollador detecta que no puede seguir la arquitectura
    |
    v
Documenta en este registro (D-NNN)
    |
    v
Tech Lead evalua impacto
    |
    ├── Impacto Bajo → Aceptar, documentar, continuar
    |
    ├── Impacto Medio → Discutir con SA, posible actualizacion de artefacto
    |
    └── Impacto Alto → SA evalua, genera nuevo ADR, actualiza artefactos afectados
```

---

## 5. Dashboard de Fitness Functions

> Enlace directo al catalogo de FF-NNN. Esta seccion es un espejo rapido.

| FF | Atributo | Estado Implementacion | Automatizado | Resultado |
|---|---|---|---|---|
| FF-001 | [atributo] | Pendiente / En CI / Activo | Pipeline CI / Monitoring / Manual | PASS / FAIL / -- |

### Estados de implementacion

| Estado | Significado |
|---|---|
| **Pendiente** | Definido por SA, no implementado por ingenieria |
| **En CI** | Implementado en pipeline, ejecutandose en cada merge/deploy |
| **Activo** | Funcionando en produccion (monitoring continuo) |
| **Deshabilitado** | Temporalmente desactivado (MUST tener justificacion en seccion 4) |

---

## 6. Resumen Ejecutivo para Stakeholders

> Seccion para compartir con stakeholders no tecnicos. Actualizar cada sprint.

**Fecha de ultimo reporte:** YYYY-MM-DD

| Dimension | Estado | Detalle |
|---|---|---|
| Arquitectura documentada | X/Y artefactos aprobados | [lista de artefactos pendientes] |
| Alineacion de implementacion | X% decisiones implementadas | [ver seccion 2] |
| Fitness Functions | X/Y automatizadas | [ver seccion 5] |
| Desviaciones abiertas | N desviaciones sin resolver | [ver seccion 4] |
| Riesgo arquitectonico | Alto / Medio / Bajo | [justificacion breve] |

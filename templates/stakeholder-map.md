---
titulo: "Stakeholder Map: [Nombre del Sistema/Iniciativa]"
identificador: SM-[NNN]
tipo: Stakeholder-Map
estado: Draft
version: "1.0.0"
autor: "[Nombre - Arquitecto SA]"
fecha-creacion: YYYY-MM-DD
fecha-ultima-revision: YYYY-MM-DD
artefactos-origen: ["CB-NNN"]
firmas-roles: []   # SHOULD firma del Acelerador / Sponsor. Ver _frontmatter.md
tags: ["stakeholder-management", "togaf"]
---

# Stakeholder Map: [Nombre del Sistema/Iniciativa]

> Referencia: TOGAF 10th Ed — Stakeholder Management.
> Referencia: ISO/IEC/IEEE 42010:2022 — Architecture Stakeholders & Concerns.
> Referencia: Mendelow's Power-Interest Grid (1981).

> **Proposito:** identificar a TODOS los stakeholders, sus intereses y su poder
> de influencia sobre la solucion, para que el SA sepa **a quien priorizar**,
> **con que cadencia comunicar** y **que tipo de artefacto entregar a cada uno**.

---

## Roles colaboradores

> :busts_in_silhouette: **Acelerador / Sponsor** principal — conoce el mapa politico real.
> :busts_in_silhouette: **Patrocinador** firma el mapa para evidenciar alineacion.

| Rol | Que aporta al SA | Cuando consultarlo |
|---|---|---|
| **Acelerador** (Sponsor / PO) | Mapa politico real, intereses ocultos, niveles de influencia, historial de cada stakeholder | Secciones 1-2 (lista + grid) |
| **Patrocinador / VP** | Validar y firmar | Seccion 4 (estrategia) |
| **Compliance / Legal** | Stakeholders regulatorios externos | Seccion 1 si hay regulador |
| **HR / People Ops** | Stakeholders internos no obvios (sindicatos, comites) | Solo si aplica |

---

## 1. Lista de Stakeholders

> Listar TODOS, internos y externos. Nadie queda fuera por ahora — el grid los prioriza despues.

| # | Stakeholder | Tipo | Rol en el sistema | Concerns / Intereses principales |
|---|---|---|---|---|
| 1 | [Nombre / Rol] | Interno / Externo / Regulador | Patrocinador / Usuario / Operador / Aprobador / Influenciador | [Que le importa de este sistema] |
| 2 | | | | |

### Tipos de stakeholders (referencia ISO/IEC/IEEE 42010:2022)

- **Acquirer:** quien financia o adquiere el sistema (Sponsor).
- **User:** quien lo opera o consume.
- **Developer:** quien lo construye (no SA).
- **Maintainer:** Operations / SRE.
- **Supplier:** vendors o proveedores externos.
- **Regulator:** autoridad regulatoria que puede vetar o multar.
- **Influencer:** sin autoridad formal pero con peso politico.

---

## 2. Power-Interest Grid (Mendelow)

> Clasificar cada stakeholder en uno de cuatro cuadrantes para definir estrategia
> de comunicacion. Eje X: Interes en el sistema. Eje Y: Poder de influencia.

```
        Alto poder
            |
            |   Manage Closely    |   Keep Satisfied
            |   (alta prioridad)  |   (mantener felices,
            |                     |    no abrumar)
   ---------|---------------------|--------------------- > Alto interes
            |   Keep Informed     |   Monitor
            |   (informar         |   (minimo esfuerzo,
            |    regularmente)    |    revisar periodicamente)
            |
        Bajo poder
```

| Stakeholder | Cuadrante | Estrategia |
|---|---|---|
| [Nombre] | Manage Closely / Keep Satisfied / Keep Informed / Monitor | [Frecuencia + canal + tipo de artefacto] |

---

## 3. Concerns y Artefactos por Stakeholder

> Mapear cada stakeholder a los artefactos arquitectonicos que le interesan.
> Un stakeholder NO necesita leer todos — el SA entrega lo que aplica.

| Stakeholder | Concerns | Artefactos relevantes | Nivel de detalle |
|---|---|---|---|
| Sponsor / VP | ROI, deadline, riesgo | CB, RFC, TAA seccion 6 | Resumen ejecutivo |
| Tech Lead | Stack, contratos, NFRs | TS, ADRs, FF | Tecnico completo |
| DevOps Lead | Infra, SLOs, rollback | SD, RO, FF | Tecnico operativo |
| QA Lead | Criterios verificables | PRD (QA-Scenarios), FF | Criterios + tests |
| Compliance | Regulacion, audit trail | CB seccion 4, SPS, FF-003 | Regulatorio |
| Regulador (externo) | Cumplimiento de norma X | TAA seccion 6, audit trail | Solo lo que la norma exige |
| Equipo Desarrollo | Como construir | TS, ADRs, contratos | Implementacion |
| Usuario final | Funcionalidades visibles | PRD (casos de uso) | Negocio |

---

## 4. Estrategia de Comunicacion

| Cuadrante | Frecuencia | Canal | Formato |
|---|---|---|---|
| Manage Closely | Semanal | Reunion + email | Resumen ejecutivo + decisiones pendientes |
| Keep Satisfied | Quincenal | Reporte | Resumen TAA seccion 6 |
| Keep Informed | Mensual | Email / wiki | Estado de artefactos + hitos |
| Monitor | Trimestral | Wiki | Solo cambios mayores |

---

## 5. Diagrama (opcional)

> Generar con Excalidraw MCP: stakeholders como circulos, lineas de influencia,
> agrupacion por cuadrante.

[Insertar diagrama o referencia]

---

## 6. Riesgos del Stakeholder Management

> Riesgos politicos / organizacionales que pueden bloquear la arquitectura.

| Riesgo | Probabilidad | Impacto | Mitigacion |
|---|---|---|---|
| [Stakeholder X bloquea por intereses contrapuestos] | Alta/Media/Baja | Alto/Medio/Bajo | [Plan] |

---

## Cuando se actualiza este mapa

- Al **inicio del proyecto** (Fase 0-1 del orquestador).
- Cuando entra o sale un stakeholder (cambio organizacional).
- En cada **Gate 4 (Post-Deploy / Review Mensual)** del TAA — revalidar cuadrantes.
- Si un stakeholder cambia de poder/interes (promocion, reorganizacion, regulacion).

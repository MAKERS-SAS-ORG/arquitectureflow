---
titulo: "Requisitos Operacionales: [Nombre del Sistema]"
identificador: RO-[NNN]
tipo: Runbook
estado: Draft
version: "1.0.0"
autor: "[Nombre - Arquitecto SA]"
fecha-creacion: YYYY-MM-DD
fecha-ultima-revision: YYYY-MM-DD
artefactos-origen: ["SD-NNN"]
firmas-roles: []   # MUST firma de DevOps para Approved. Ver _frontmatter.md
tags: []
---

# Requisitos Operacionales: [Nombre del Sistema]

> Este documento define los REQUISITOS que Operations/SRE necesita para
> crear el runbook detallado. El SA define QUE operar; Operations define COMO.

## Roles colaboradores

> Aqui el dialogo principal del SA es con **DevOps / SRE**. Sin ellos este documento
> queda en abstracto. Ver diagrama de roles en `README.md`.

| Rol | Que aporta al SA | Cuando consultarlo |
|---|---|---|
| **DevOps / SRE / Infra** | Health check viable, ventana de deployment realista, criterios de rollback automatizables, integracion con plataforma de monitoreo, severidades reales del oncall | Secciones 2-4 (deployment, rollback, metricas) — son los duenos operativos |
| **Especialista Tecnico** | Comportamiento esperado del sistema bajo cada metrica, dependencias internas que pueden fallar | Seccion 4 (metricas criticas) y seccion 6 (cambios que requieren aprobacion arq.) |
| **Vendor / Proveedores externos** | SLAs reales contratados, ventanas de mantenimiento, contactos de soporte | Seccion 5 (dependencias externas) |
| **Compliance** | Politicas de cambio en sistemas regulados (SOX, PCI), evidencia auditable | Seccion 6 (gestion de cambios) si aplica |

## 1. Informacion del Sistema

| Item | Valor |
|---|---|
| URL produccion | |
| URL staging | |
| Region/Zona | |
| Dashboard de monitoreo | [link] |
| Contacto de escalada | [Nombre — canal] |

## 2. Requisitos de Deployment

| Requisito | Valor |
|---|---|
| Estrategia | Blue-green / Canary / Rolling |
| Tiempo maximo de deployment | [minutos] |
| Health check endpoint | [ruta] |
| Health check criterio | [que debe retornar para considerar healthy] |

### Checklist de verificacion post-despliegue (SA define criterios)
- [ ] Health check retorna OK
- [ ] Tasa de error < [umbral]
- [ ] Flujo principal funciona (cual flujo: [describir])
- [ ] Metricas de negocio en rango normal

## 3. Criterios de Rollback

| Condicion | Accion |
|---|---|
| Tasa de error > [X]% por mas de [Y] minutos | Rollback automatico |
| Health check falla en [Z] segundos post-deploy | Rollback automatico |
| Degradacion de latencia > [W]x sobre baseline | Evaluacion manual, posible rollback |

**Ventana de rollback segura:** [tiempo despues del deploy en que rollback es viable]

## 4. Metricas Criticas y Umbrales

| Metrica | Umbral de alarma | Severidad | Escalar a |
|---|---|---|---|
| [metrica 1] | > [valor] por [tiempo] | P1 / P2 / P3 | [equipo/persona] |
| [metrica 2] | > [valor] por [tiempo] | P1 / P2 / P3 | [equipo/persona] |

### Niveles de severidad
| Nivel | Definicion | Tiempo de respuesta |
|---|---|---|
| P1 | Sistema caido o datos en riesgo | < 15 minutos |
| P2 | Funcionalidad degradada | < 1 hora |
| P3 | Issue menor, sin impacto critico | Proximo dia habil |

## 5. Dependencias Externas y SLAs

| Sistema externo | SLA contratado | Timeout esperado | Comportamiento si falla |
|---|---|---|---|
| [sistema] | [SLA] | [timeout] | [degradacion graceful / fallback / bloqueo] |

## 6. Politica de Gestion de Cambios

Todo cambio en produccion MUST:
- Tener ticket aprobado con descripcion del cambio
- Tener plan de rollback documentado
- Ejecutarse en ventana de bajo trafico: [definir horario]

Cambios que requieren aprobacion adicional del SA:
- Cambios en schema de base de datos
- Cambios en contratos de API
- Cambios en integraciones con sistemas externos
- Actualizaciones de dependencias mayores

> **NOTA PARA OPERATIONS:** Usar este documento como base para crear
> el runbook detallado con procedimientos paso a paso, comandos especificos
> y scripts de diagnostico.

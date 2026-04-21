---
titulo: "Runbook: [Nombre del Sistema]"
identificador: RB-[NNN]
tipo: Runbook
estado: Draft
version: "1.0.0"
autor: "[Nombre]"
fecha-creacion: YYYY-MM-DD
fecha-ultima-revision: YYYY-MM-DD
artefactos-origen: ["SD-NNN"]
tags: []
---

# Runbook: [Nombre del Sistema]

**Contactos de escalada:** [Nombre (rol) — canal]

## 1. Informacion del Sistema

| Item | Valor |
|---|---|
| URL produccion | |
| URL staging | |
| Region/Zona | |
| Dashboard de monitoreo | [link] |
| Pipeline CI/CD | [link] |

## 2. Despliegue

### Proceso normal
1. [paso 1]
2. [paso 2]

### Checklist post-despliegue
- [ ] Health check retorna 200
- [ ] Tasa de error < [umbral]
- [ ] Flujo principal funciona (test de humo)

### Rollback
1. [paso para revertir]
2. [verificacion]

## 3. Operaciones Comunes

### OP-001: [Nombre de la operacion]
- **Cuando:** [condicion]
- **Pasos:**
  1. [paso]
- **Verificacion:** [como confirmar que funciono]

## 4. Diagnostico de Problemas

### PROB-001: [Descripcion del sintoma]
- **Sintoma:** [que se observa]
- **Causa probable:** [causa mas comun]
- **Diagnostico:**
  1. [paso de investigacion]
- **Resolucion:** [como resolver]
- **Escalada:** [cuando escalar y a quien]

## 5. Gestion de Cambios
Todo cambio en produccion MUST:
1. Tener ticket con descripcion
2. Tener aprobacion del responsable
3. Tener plan de rollback documentado
4. Quedar registrado en log de cambios

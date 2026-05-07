---
titulo: "RFC-[NNN]: [Titulo descriptivo del problema]"
identificador: RFC-[NNN]
tipo: RFC
estado: Draft
version: "1.0.0"
autor: "[Nombre]"
fecha-creacion: YYYY-MM-DD
fecha-ultima-revision: YYYY-MM-DD
revisores: ["@persona1", "@persona2"]
decision-esperada: YYYY-MM-DD
estimacion-esfuerzo: S | M | L | XL
stakeholders: []
tags: []
---

# RFC-[NNN]: [Titulo]

## Roles colaboradores

> El SA lidera y aprueba el RFC. Es el primer artefacto donde aparecen **dos roles**:
> el Acelerador (sigue siendo necesario) y el Especialista Tecnico (entra al juego).
> Ver diagrama de roles en `README.md`.

| Rol | Que aporta al SA | Cuando consultarlo |
|---|---|---|
| **Acelerador** (Negocio/Financiero) | Confirmar el problema y el costo, validar ROI de cada opcion, alinear urgencia | Secciones 1-2 (resumen, motivacion) y al puntuar criterios de negocio en la matriz |
| **Especialista Tecnico** (SWA / Tech Lead) | Viabilidad tecnica de cada opcion, riesgos no evidentes, dependencias internas, plan de rollback realista | Seccion 3 (opciones), seccion 4 (matriz) y seccion 5 (riesgos + rollback) |
| **Compliance / Legal** | Solo si una opcion impacta regulacion | Seccion 5.4 (impacto regulatorio) |

> QA y DevOps todavia NO participan — entran en PRD/Tech Spec/System Design.

## 1. Resumen Ejecutivo
> Una sola oracion: que problema resuelve y como.

## 2. Contexto y Motivacion

### 2.1 El Problema Hoy
> Datos concretos, no percepciones. Metricas actuales si existen.

### 2.2 Costo de No Resolver
> Cuantificado: dinero, tiempo, riesgo, oportunidad perdida.

### 2.3 Por Que Ahora
> Urgencia, ventana de oportunidad, cambio regulatorio, deadline.

### 2.4 Metricas de Exito
> Numeros medibles. No "mejorar la experiencia" sino "reducir tiempo de X de 5min a 30seg".

| Metrica | Valor actual | Objetivo | Plazo |
|---|---|---|---|
| [Metrica 1] | [actual] | [objetivo] | [plazo] |

## 3. Opciones Consideradas

### Opcion A: No Hacer Nada
- **Descripcion:** Mantener el estado actual.
- **Pros:** Sin costo, sin riesgo de cambio.
- **Contras:** [costo de no resolver continua]
- **Estimacion:** $0
- **Por que se descarta:** [justificacion]

### Opcion B: [Nombre]
- **Descripcion:**
- **Pros:**
- **Contras:**
- **Estimacion:**
- **Por que se descarta:**

### Opcion C: [Nombre] — RECOMENDADA
- **Descripcion:**
- **Pros:**
- **Contras:**
- **Estimacion:**
- **Por que se recomienda:**

## 4. Matriz de Decision

| Criterio | Peso | A: No Hacer Nada | B: [Nombre] | C: [Nombre] |
|---|---|---|---|---|
| [Criterio 1] | [%] | [1-5] | [1-5] | [1-5] |
| [Criterio 2] | [%] | [1-5] | [1-5] | [1-5] |
| **Total ponderado** | | [total] | [total] | [total] |

## 5. Impacto y Riesgos

### 5.1 Sistemas y Modulos Afectados
- [Sistema/modulo 1]: [tipo de impacto]

### 5.2 Riesgos con Plan de Mitigacion
| Riesgo | Probabilidad | Impacto | Mitigacion |
|---|---|---|---|
| [Riesgo 1] | Alta/Media/Baja | Alto/Medio/Bajo | [Plan] |

### 5.3 Plan de Rollback
> Como deshacer si falla. MUST ser tecnica y operativamente ejecutable.

### 5.4 Impacto Regulatorio
> Si aplica: regulaciones afectadas, aprobaciones necesarias.

## 6. Preguntas Abiertas
- [ ] Pregunta 1?
- [ ] Pregunta 2?

## 7. Supuestos Explicitos
- SUPUESTO-01: [descripcion del supuesto]

## 8. Referencias
- [Documentos relacionados, links, artefactos previos]

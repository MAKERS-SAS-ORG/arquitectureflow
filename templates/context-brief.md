---
titulo: "Context Brief: [Nombre del Proyecto/Iniciativa]"
identificador: CB-[NNN]
tipo: Context-Brief
estado: Draft
version: "1.0.0"
autor: "[Nombre - Arquitecto SA]"
fecha-creacion: YYYY-MM-DD
fecha-ultima-revision: YYYY-MM-DD
stakeholders: []
tags: []
---

# Context Brief: [Nombre del Proyecto/Iniciativa]

> Principio Anti-Vibecoding: "Si no puedes explicar en un parrafo que problema resuelve
> lo que estas a punto de construir, no estas listo para construir."
>
> Este documento captura el contexto esencial ANTES de generar cualquier artefacto.
> Sin Context Brief aprobado, no se inicia ningun RFC, ADR ni Tech Spec.

---

## 1. Contexto de Negocio

**Problema principal** (maximo 2 oraciones):
> [Describir el problema en terminos de negocio, no tecnicos]

**Usuario o beneficiario principal:**
> [Quien sufre el problema o se beneficia de la solucion]

**Costo de NO resolver** (cuantificado en dinero, tiempo, riesgo u oportunidad):
> [No "es importante" — sino "$X/mes", "Y horas/semana", "riesgo de multa de $Z"]

**Deadline inamovible** (negocio o regulatorio):
> [Fecha y motivo, o "Sin deadline fijo — priorizado por valor de negocio"]

---

## 2. Stakeholders y Gobernanza

| Rol | Nombre | Responsabilidad |
|---|---|---|
| Patrocinador / Product Owner | [nombre] | Aprueba el exito del producto |
| Aprobador de arquitectura | [nombre] | Decision final tecnica |
| Equipos afectados | [lista] | Sistemas o dominios que se impactan |
| Compliance / Legal | [nombre o N/A] | Validacion regulatoria |

---

## 3. Contexto Tecnico y Restricciones

**Naturaleza del sistema:**
- [ ] Greenfield (nuevo)
- [ ] Evolucion (sistema existente)
- [ ] Migracion (cambio de plataforma)

**Sistemas existentes involucrados:**
> [Listar sistemas legados, de terceros o internos que se deben integrar]

**Escala esperada:**
| Dimension | Valor actual | Proyeccion 1 ano |
|---|---|---|
| Usuarios | [actual o 0] | [proyeccion] |
| Transacciones/dia | [actual o 0] | [proyeccion] |
| Datos almacenados | [actual o 0] | [proyeccion] |

**Restricciones innegociables:**
> [Regulaciones, vendor lock-in, skills del equipo, presupuesto, timeline]

---

## 4. IA y Compliance

**La solucion integra componentes de IA/LLM?**
- [ ] Si → requiere System Prompt Spec obligatorio
- [ ] No

**Requisitos de compliance especificos:**
> [GDPR, PCI-DSS, SOX, regulacion financiera local, Ley de datos personales, etc.]
> [Si no aplica: "Sin requisitos regulatorios especificos"]

---

## 5. Resumen de Scope Inicial

**IN scope (que SI aborda esta iniciativa):**
- [capacidad 1]
- [capacidad 2]

**OUT scope (que NO aborda — explicito para evitar scope creep):**
- [exclusion 1 — razon]
- [exclusion 2 — razon]

---

## Siguiente paso

Con este Context Brief aprobado, el orquestador determina:
- Que artefactos aplican (ver `references/matriz-decision.md`)
- En que orden se crean (ver `references/protocolo-iteracion.md`)
- El primer artefacto recomendado suele ser el **RFC**

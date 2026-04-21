---
titulo: "PRD: [Nombre del Producto/Funcionalidad]"
identificador: PRD-[NNN]
tipo: PRD
estado: Draft
version: "1.0.0"
autor: "[Nombre]"
fecha-creacion: YYYY-MM-DD
fecha-ultima-revision: YYYY-MM-DD
revisores: []
artefactos-origen: ["RFC-NNN"]
estimacion-esfuerzo: M
stakeholders: []
tags: []
---

# PRD: [Nombre del Producto/Funcionalidad]

## 1. Objetivo del Producto
> Una sola oracion: que resultado de negocio logra esta funcionalidad.

## 2. Usuarios Objetivo

| Persona | Descripcion | Necesidad Principal |
|---|---|---|
| [Rol 1] | [descripcion] | [necesidad] |

## 3. Funcionalidades (Casos de Uso)

### CU-001: [Nombre del caso de uso]
- **Actores:** [quien participa]
- **Precondicion:** [que debe ser verdad antes]
- **Flujo principal:**
  1. El usuario hace X
  2. El sistema responde con Y
- **Flujos alternativos:**
  - Alt-A: Si X falla -> [que pasa]
- **Postcondicion:** [que es verdad despues]
- **Prioridad:** Must Have | Should Have | Nice to Have

## 4. User Stories con Criterios de Aceptacion

### US-001: [Titulo]
**Como** [rol], **quiero** [accion], **para** [beneficio de negocio].

**Criterios de Aceptacion:**
```gherkin
Scenario: [Nombre del escenario]
  Given [contexto inicial]
  When  [accion del usuario]
  Then  [resultado esperado]

Scenario: [Escenario de error]
  Given [contexto]
  When  [accion que genera error]
  Then  [como se maneja el error]
```

## 5. Quality Attribute Scenarios (NFRs)

> Referencia: ISO/IEC 25010:2023, Bass et al. Quality Attribute Scenarios

### QA-001: [Nombre del atributo]
| Campo | Valor |
|---|---|
| Fuente | [quien genera el estimulo] |
| Estimulo | [que ocurre] |
| Artefacto | [que parte del sistema] |
| Entorno | [bajo que condiciones] |
| Respuesta | [que hace el sistema] |
| Medida | [como se mide] |

## 6. Reglas de Negocio
- RN-001: [regla invariante del dominio]

## 7. Fuera de Scope (explicito)
- [Funcionalidad A] — razon por la que no esta
- [Funcionalidad B] — pendiente para fase posterior

## 8. Dependencias y Restricciones
- Depende de: [sistemas, APIs, decisiones]
- Restricciones: [regulatorias, tecnicas, de tiempo]

## 9. Metricas de Exito

| Metrica | Linea base | Objetivo | Plazo |
|---|---|---|---|
| [Metrica 1] | [actual] | [objetivo] | [plazo] |

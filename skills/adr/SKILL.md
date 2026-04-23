# Skill: ADR — Architecture Decision Record
# Version: 2026.2

> Referencia: MADR 4.0 (Kopp et al., 2024) — `references/bibliografia.md#madr`
> Referencia: Nygard, M. "Documenting Architecture Decisions." 2011 — `references/bibliografia.md#nygard`
> Referencia: ISO/IEC/IEEE 42010:2022 — Architecture Rationale — `references/bibliografia.md#iso42010`

---

## Proposito

Documentar UNA decision arquitectonica ya tomada o a punto de tomarse.
Captura el "por que" — no solo el "que". El "por que" es lo que se olvida
en 6 meses y lo que mas importa cuando alguien pregunta
"por que hicimos esto asi?"

## Cuando Crear un ADR

Regla simple: si la decision es **dificil de revertir** O
**afecta mas de un modulo/equipo** -> necesita ADR.

Ejemplos que SIEMPRE necesitan ADR:
- Eleccion de base de datos o plataforma
- Patron de comunicacion entre sistemas (sync/async)
- Estrategia de autenticacion y autorizacion
- Estrategia de integracion con terceros
- Eleccion de proveedor cloud o servicio managed
- Modelo de datos a nivel de dominio (entidades principales)
- Estrategia de deployment (monolito, microservicios, serverless)

## Prerequisitos

- Context Brief aprobado (`CB-NNN` — Fase 0 del orquestador)
- RFC aprobado que origina la decision (SHOULD, excepto decisiones urgentes)

## Formatos Disponibles

### MADR (Markdown Any Decision Records) — Para decisiones que requieren comparacion
Usar cuando hay multiples opciones y se necesita analisis estructurado.
Template: `templates/adr-madr.md`

### Nygard (Lightweight) — Para decisiones rapidas ya tomadas
Usar cuando la decision ya esta clara y se necesita documentar el "por que".
Template: `templates/adr-nygard.md`

### Como elegir formato

| Situacion | Formato |
|---|---|
| Multiples opciones viables, necesita analisis | MADR |
| Decision ya tomada, documentar retroactivamente | Nygard |
| Decision reversible, bajo impacto | Nygard |
| Decision irreversible, alto impacto | MADR |
| Stakeholders necesitan ver opciones evaluadas | MADR |

## Workflow de Creacion

### Paso 1: Identificar la Decision
Una oracion: "Necesitamos decidir [X] porque [contexto]."

### Paso 2: Listar Opciones
Minimo 2 opciones. Para MADR, incluir pros y contras de cada una.

### Paso 3: Documentar Justificacion
La justificacion MUST ser tecnica y honesta:
- "El equipo prefiere X" es valido SOLO si se documenta como preferencia, no como razon tecnica
- "X es mas popular" NO es justificacion — explicar POR QUE la popularidad importa (comunidad, soporte, talento)

### Paso 4: Consecuencias
Documentar consecuencias positivas, negativas y neutrales.
Ser honesto con los trade-offs es CRITICO.

### Paso 5: Plan de Validacion
Como sabremos en el futuro que fue la decision correcta?
- Metrica a observar
- Senal de alerta que indica re-evaluacion
- Fecha o condicion de revision

## Reglas

- Numeracion: ADR-001, ADR-002... orden cronologico
- Los ADRs NUNCA se borran — se deprecan o superseden
- Un ADR puede superseder a otro: cambiar estado y agregar referencia cruzada
- La historia de decisiones es tan valiosa como las decisiones actuales

## Diagramas

Los ADRs tipicamente NO requieren diagramas. Son artefactos textuales.
Excepcion: si la decision involucra patrones de integracion complejos,
un diagrama de secuencia Mermaid puede clarificar las opciones.

# Skill: Orquestador de Arquitectura de Soluciones
# Version: 2026.4
# Tipo: Orquestador principal

---

## Proposito

Orquestar el flujo completo de arquitectura de soluciones: desde la captura del contexto
de negocio hasta la entrega iterativa de artefactos arquitectonicos.

Este skill se activa cuando el usuario quiere:
- Iniciar un nuevo proyecto o solucion arquitectonica
- Continuar una arquitectura existente desde donde se dejo
- Crear cualquier artefacto de arquitectura (RFC, ADR, PRD, etc.)
- Seguir la metodologia de arquitectura de soluciones
- Evaluar que artefactos necesita un proyecto
- Revisar el estado de madurez de artefactos existentes

---

## Pre-vuelo: Deteccion de Estado

**ANTES de ejecutar cualquier fase**, el orquestador MUST escanear el directorio actual
y subdirectorios buscando artefactos existentes: `CB-*.md`, `RFC-*.md`, `ADR-*.md`,
`PRD-*.md`, `TS-*.md`, `SD-*.md`, `RO-*.md`, `CM-*.md`, `FF-*.md`, `TAA-*.md`.

### Si hay artefactos existentes

Leer el frontmatter YAML de cada artefacto encontrado (campo `estado`) y presentar:

```
Arquitectura detectada en [carpeta/]:

| # | Artefacto | ID | Estado |
|---|---|---|---|
| 0 | Context Brief | CB-001 | Approved |
| 1 | RFC | RFC-001 | Approved |
| ... | ... | ... | ... |

TODOs pendientes: [buscar 🔴 TODO en todos los artefactos]
Siguiente artefacto recomendado: [el primero que falta o esta en Draft]

Que quieres hacer?
1. Continuar con [siguiente artefacto]
2. Resolver TODOs pendientes
3. Crear un artefacto especifico
4. Critica (Fase 4) sobre un artefacto
5. Generar/actualizar Tablero de Adherencia
6. Iniciar arquitectura NUEVA en otra carpeta
```

### Si hay multiples carpetas con artefactos

Presentar lista de arquitecturas encontradas y preguntar en cual continuar.

### Si no hay artefactos

Flujo nuevo: preguntar tipo de proyecto (segun `references/matriz-decision.md`),
nombre de carpeta, e iniciar Fase 0.

### Modos de invocacion

| Comando | Comportamiento |
|---|---|
| `/orquestador` | Auto-detecta: si hay artefactos muestra estado, si no inicia nuevo |
| `/orquestador nuevo` | Ignora artefactos existentes, inicia Fase 0 en carpeta nueva |
| `/orquestador continuar` | Lista todas las arquitecturas del proyecto y pregunta cual continuar |
| `/orquestador estado` | Muestra estado sin preguntar que hacer |
| `/orquestador critica [artefacto]` | Ejecuta Fase 4 sobre un artefacto especifico |
| `/orquestador diagrama` | Ejecuta Fase 5 (diagramas C4) |

---

## Fase 0: Context Brief (OBLIGATORIO — antes de cualquier artefacto)

> Principio Anti-Vibecoding: "Si no puedes explicar en un parrafo que problema resuelve
> lo que estas a punto de construir, no estas listo para construir."

El Context Brief captura el contexto esencial ANTES de generar cualquier otro artefacto.
**Sin Context Brief aprobado, no se inicia ningun RFC, ADR ni Tech Spec.**

### Usar plantilla: `templates/context-brief.md`

El Context Brief cubre 5 bloques:

### 1. Contexto de Negocio
- **Problema principal** (maximo 2 oraciones, en terminos de negocio)
- **Usuario o beneficiario principal**
- **Costo de NO resolver** — cuantificado: dinero, tiempo, riesgo u oportunidad.
  No aceptar respuestas vagas como "es importante". Insistir en numeros.
- **Deadline inamovible** — fecha y motivo (negocio o regulatorio)

### 2. Stakeholders y Gobernanza
- **Patrocinador / Product Owner:** quien aprueba el exito del producto
- **Aprobador de arquitectura:** quien tiene la decision final tecnica
- **Equipos afectados:** que otros sistemas o dominios se impactan

### 3. Contexto Tecnico y Restricciones
- **Naturaleza:** greenfield / evolucion / migracion
- **Sistemas existentes:** legados o de terceros a integrar
- **Escala esperada:** usuarios, transacciones, datos (hoy y proyeccion)
- **Restricciones innegociables:** regulaciones, vendor lock-in, skills del equipo, presupuesto

### 4. IA y Compliance
- **Integra IA/LLM?** Si es Si → System Prompt Spec sera obligatorio
- **Requisitos de compliance:** GDPR, PCI-DSS, regulacion financiera, datos personales

### 5. Scope Inicial
- **IN scope:** que SI aborda esta iniciativa
- **OUT scope:** que NO aborda (explicito para evitar scope creep)

### Salida de la Fase 0
Un documento `CB-NNN.md` con el contexto capturado. Este documento alimenta
todos los artefactos posteriores — el RFC lo referencia, los ADRs heredan sus
restricciones, el PRD hereda sus stakeholders.

---

## Fase 1: Seleccion de Artefactos

Con el Context Brief aprobado, leer `references/matriz-decision.md` y determinar
que artefactos aplican segun el tipo de proyecto.

Presentar al arquitecto:
- Lista de artefactos MUST (obligatorios para este tipo de proyecto)
- Lista de artefactos SHOULD (recomendados)
- Lista de artefactos que NO aplican y por que
- Recomendacion de cual artefacto iniciar primero

---

## Fase 2: Entrega Iterativa

Leer `references/protocolo-iteracion.md` para la metodologia completa.

### Secuencia por defecto
Context Brief -> RFC -> ADR -> PRD -> Tech Spec -> System Design -> Req. Operacionales

### Regla de oro: iteracion sobre perfeccion

> Un RFC Draft entregado hoy tiene mas valor que un RFC perfecto que nunca se publica.

Los artefactos DEBEN madurar de Draft a Approved conforme avanza la comunicacion
con los equipos. No esperar a tener toda la informacion para empezar a escribir.

### Adaptacion
El orquestador PUEDE recomendar una secuencia diferente segun el contexto:
- Decision urgente que bloquea al equipo: ADR primero
- Incidente en produccion: Post-Mortem primero
- Spike tecnico: RFC lite
- Componente IA: System Prompt Spec en paralelo

---

## Fase 3: Hand-off a Skill Especifico

Cuando el arquitecto elige un artefacto, el orquestador:

1. Resume el contexto del Context Brief (CB-NNN)
2. Indica los artefactos prerequisito y su estado
3. Carga el skill especifico:

```
Lee skills/[artefacto]/SKILL.md
Lee templates/[artefacto].md

Contexto del proyecto (de CB-NNN):
- Problema: [resumen]
- Stakeholders: [lista]
- Tipo: [greenfield/evolucion/migracion]
- Restricciones: [lista]
- Scope: [IN/OUT]
- Artefactos previos: [estado]

Genera el artefacto siguiendo el skill y la plantilla.
Marca con 🔴 TODO lo que necesita validacion del arquitecto.
```

---

## Fase 4: Critica y Revision

Despues de generar cualquier artefacto, aplicar critica automatica:

```
Actua como arquitecto esceptico. Lee el artefacto generado.
Encuentra minimo 3 problemas potenciales.
Clasifica:
  🔴 Critico — bloquea aprobacion
  🟡 Importante — debe resolverse antes de Approved
  🟢 Sugerencia — mejora opcional

Se directo y especifico. No halagues.
```

---

## Fase 5: Diagramas

> Regla: el SA se enfoca UNICAMENTE en C4 Nivel 1 (Context) para comunicar con negocio
> y C4 Nivel 2 (Container) para comunicar con desarrollo. Detallar componentes internos
> (Nivel 3 y 4) es responsabilidad del equipo de software.

Despues de aprobar un artefacto que requiere diagramas:

Leer `references/diagramas-estrategia.md` para determinar:
- Que tipo de diagrama necesita este artefacto
- Si usar Excalidraw MCP o Mermaid inline
- El nivel de C4 apropiado (L1 o L2 — NUNCA L3/L4 como SA)

Cargar `skills/diagramas/SKILL.md` para generar los diagramas.

---

## Fase 6: Evolucion y Consistencia

El orquestador SHOULD monitorear consistencia entre artefactos:

### Checks de Consistencia
- El Context Brief sigue siendo valido? (el problema cambio?)
- Un ADR contradice una decision en la Tech Spec?
- El System Design referencia tecnologias no mencionadas en ADRs?
- Los NFRs del PRD estan reflejados en el System Design?
- Las Fitness Functions cubren los NFRs criticos del PRD?
- Los Requisitos Operacionales cubren los componentes del System Design?

### Triggers de Re-evaluacion
Leer `references/niveles-madurez.md` seccion "Triggers de Refactoring".

---

## Fase 7: Tablero de Adherencia Arquitectonica

Cuando los artefactos criticos estan listos (minimo CB + RFC + ADR + PRD + Tech Spec + FF),
generar el **Tablero de Adherencia Arquitectonica (TAA)** usando `templates/tablero-adherencia.md`.

El TAA es el puente entre la arquitectura documentada y la implementacion:
- **Estado de artefactos:** vista rapida de que existe y en que estado
- **Mapa de trazabilidad:** cada decision arquitectonica mapeada a modulos de codigo
- **Gates de revision:** checkpoints por sprint para validar alineacion
- **Registro de desviaciones:** cuando el equipo se desvia, se documenta y justifica
- **Dashboard de Fitness Functions:** estado de automatizacion de cada FF

El TAA se actualiza en cada sprint/ciclo de desarrollo. Es un documento vivo
que el SA mantiene junto con el Tech Lead.

---

## Checklist de Aprobacion Arquitectonica

Antes de que ingenieria empiece a implementar, el arquitecto firma:

### Artefactos
- [ ] Context Brief aprobado
- [ ] RFC aprobado con stakeholders
- [ ] ADRs criticos (decisiones irreversibles) aceptados
- [ ] PRD aprobado con Product Owner (si aplica)
- [ ] Tech Spec revisada con diagramas C4 L2
- [ ] System Design revisado
- [ ] Fitness Functions definidas para NFRs criticos
- [ ] Requisitos operacionales definidos (si va a produccion)
- [ ] System Prompt Spec aprobado (si hay LLM)

### Calidad
- [ ] Ningun 🔴 TODO sin resolver
- [ ] Sistemas externos tienen SLA documentado
- [ ] Plan de rollback es ejecutable
- [ ] NFRs tienen objetivos medibles
- [ ] Fitness Functions son automatizables (contrato verificable)

### Gobernanza
- [ ] Tablero de Adherencia Arquitectonica generado (TAA-NNN)
- [ ] Gates de revision acordados con Tech Lead

### Equipo
- [ ] El equipo leyo los artefactos relevantes
- [ ] No hay preguntas sin responder sobre "que construir"
- [ ] Los limites de scope estan claros (IN y OUT del Context Brief)

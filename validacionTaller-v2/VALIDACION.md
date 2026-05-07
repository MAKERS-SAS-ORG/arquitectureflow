# VALIDACION.md — Reporte de la corrida end-to-end (v2)

> Esta validacion ejercito el flujo completo de ArquitectureFlow v2026.4 con los
> cambios de **roles colaboradores** aplicados a templates, skills y taller.
> Caso usado: AsistIA (Asistente Conversacional para Reclamos de Seguros) —
> distinto del ejemplo `inversion-pasiva` para forzar al framework a aplicarse
> desde cero.

---

## 1. Que se valido

| Dimension | Resultado |
|---|---|
| **Cobertura de roles en templates** | :white_check_mark: Cada artefacto tiene seccion "Roles colaboradores" con tabla rol → aporte → cuando |
| **Cobertura de roles en skills** | :white_check_mark: 9/9 skills agregaron la seccion (incluido orquestador con tabla maestra) |
| **Coherencia con el diagrama del README** | :white_check_mark: Las matrices de cada artefacto reflejan exactamente el diagrama Mermaid del README |
| **Marcadores en el cuerpo de los artefactos** | :white_check_mark: `:busts_in_silhouette:` para rol involucrado, `:red_circle:` para TODO pendiente — funcionan visualmente |
| **Senalizacion de bloqueos por falta de rol** | :white_check_mark: TAA-001 detecta correctamente que SPS-001 esta bloqueado por Compliance |
| **Cumplimiento TOGAF** | :white_check_mark: Stakeholder Management explicito; separation of concerns SA vs SWA preservado |

---

## 2. Lo que funciono bien

1. **El bloque "Roles colaboradores" es realmente quirurgico.** No rompio el orden
   logico de ninguna plantilla — cada uno conserva su numeracion (`## 1.`, `## 2.`...).

2. **La tabla maestra del orquestador** (skills/orquestador/SKILL.md) es la "fuente de
   la verdad" — el resto de skills la referencian sin duplicar contenido. Cambios futuros
   se hacen en un solo lugar.

3. **El marcador `:busts_in_silhouette:[ROL]` es visualmente fuerte** y permite al SA
   leer un artefacto y ver de un vistazo "quien aporto que".

4. **El TAA-001 capturo automaticamente que SPS-001 esta bloqueado por Compliance**.
   Antes de los cambios este bloqueo era invisible. Ahora la tabla de roles del
   template SPS lo hace inevitable.

5. **El taller.md sigue siendo legible.** El callout `> 👥` antes de cada paso es
   no-invasivo y reemplaza la necesidad de que el arquitecto lea el bloque completo
   en cada template.

---

## 3. Mejoras detectadas durante la validacion

### Mejora 1 (BAJA): falta el rol en `skills/diagramas/SKILL.md`
**Hallazgo:** el skill de diagramas NO tiene bloque de roles colaboradores.
**Impacto:** menor, pero por consistencia debe agregarse — el diagrama C4 L2 se
revisa con el Especialista Tecnico (validar que los containers son los que el
equipo va a construir) y a veces con DevOps (validar deployment logico).
**Accion:** agregar bloque corto al skill de diagramas en el siguiente commit.

### Mejora 2 (MEDIA): falta artefacto formal "Stakeholder Map"
**Hallazgo:** el taller y los templates referencian "stakeholder map" como diagrama
de Excalidraw (en el skill PRD), pero no hay template ni skill formales. La
seccion de Stakeholders del CB es lo unico cercano.
**Impacto:** mediano. TOGAF (Stakeholder Management) y ISO/IEC/IEEE 42010:2022
recomiendan tener el mapa explicito. Ahora que tenemos roles claros, podriamos
formalizarlo.
**Accion sugerida:** agregar `templates/stakeholder-map.md` y `skills/stakeholder-map/SKILL.md`
en una iteracion futura. Por ahora documentado como :red_circle: TODO.

### Mejora 3 (MEDIA): la matriz de decision NO menciona el SPS-001 como obligatorio en sistemas con LLM
**Hallazgo:** `references/matriz-decision.md` ya marca SPS como MUST cuando hay LLM,
pero el orquestador no lo carga automaticamente al detectar que CB-001 marca
"Integra IA/LLM: Si". En esta validacion lo cargue manualmente.
**Impacto:** mediano. Si un arquitecto novato corre el flujo, podria no enterarse
de que necesita SPS-001 hasta que sea muy tarde.
**Accion sugerida:** agregar logica al orquestador (Fase 1) para que cuando el CB
tenga "IA/LLM: Si", emita explicitamente el aviso "REQUERIDO: System Prompt Spec".

### Mejora 4 (BAJA): el bloque de roles de `adr-nygard.md` quedo demasiado escueto
**Hallazgo:** ADR Nygard es lightweight, asi que tiene un parrafo en lugar de tabla.
Aceptable, pero podria beneficiarse de una mini-tabla con Especialista Tecnico
como rol principal. El ADR de la validacion (ADR-001 y ADR-002) uso formato MADR,
asi que esto NO se ejercito en esta corrida.
**Accion sugerida:** uniformar formato si en una proxima corrida ADR Nygard se usa.

### Mejora 5 (ALTA): falta una seccion "Salida con que rol firma" en cada artefacto
**Hallazgo:** el TAA-001 muestra estado (Approved/Review/Draft) y revisor, pero el
template NO obliga a indicar **quien firmo** desde cada rol. En sistemas regulados
(salud, financiero) esto es importante para evidencia auditable.
**Ejemplo concreto:** en SPS-001 puse manualmente "Aprobado por compliance: NO" —
funciono, pero porque el template SPS ya tenia ese campo. En CB-001 / RFC-001 /
TS-001 NO hay un campo equivalente.
**Accion sugerida:** agregar al frontmatter de cada artefacto un campo
`firmas-roles: [{rol: ..., persona: ..., fecha: ...}]` para evidencia regulatoria.

### Mejora 6 (BAJA): el taller no tiene callout para Paso 3 (seleccion de artefactos)
**Hallazgo:** agregue callouts a Pasos 2, 4-10 pero NO al Paso 3 (seleccion de
artefactos), porque alli el orquestador trabaja "solo" con el SA leyendo la matriz.
Esto esta correcto — no hay rol externo en ese paso. Pero por simetria visual
podria agregarse un callout que diga explicitamente "este paso es solo SA + matriz".

### Mejora 7 (MEDIA): falta puente entre FF-007 (Juicio) y la actualizacion del TAA
**Hallazgo:** la FF-007 (Juicio con IA) detecta inconsistencias entre artefactos.
Pero NO hay un loop documentado de "agente IA detecta gap → actualiza seccion 4
del TAA (desviaciones)". Ahora la FF detecta pero el TAA queda manual.
**Accion sugerida:** documentar en `references/protocolo-iteracion.md` el loop
de retroalimentacion FF-007 → TAA seccion 4.

---

## 4. Senales de que el sistema funciono

- :white_check_mark: **El flujo termino completo en una sola pasada** sin tener que regresar
  a artefactos previos para "agregar el rol". Esto sugiere que la guia esta en el
  lugar correcto del template.

- :white_check_mark: **Los TODOs marcados con `:red_circle: :busts_in_silhouette:` son accionables.**
  Cada uno dice "rol X debe hacer Y". El TAA los puede agrupar y un Project Manager
  puede convertirlos en tickets directamente.

- :white_check_mark: **El bloqueo de SPS-001 por Compliance se documento naturalmente** — sin
  tener que "improvisar" un campo. El template SPS ya tenia "Aprobado por compliance"
  como campo y la guia de roles lo amplifica.

- :white_check_mark: **No se duplico contenido.** Las tablas en templates son finas (3-5 filas
  con que/cuando/quien); las tablas en skills son tambien finas pero orientadas a
  workflow ("en que paso del workflow"). El orquestador centraliza la matriz maestra.

---

## 5. Conclusion

La adicion del bloque "Roles colaboradores" funciona como guia operativa real
para el SA. La validacion E2E con un caso nuevo (AsistIA) demostro que:

1. El SA puede ejecutar el flujo completo SIN dudas sobre con quien dialogar.
2. Los artefactos quedan auto-documentados con quien aporto que.
3. Los bloqueos por falta de rol son visibles antes de declarar Approved.
4. El framework respeta TOGAF Stakeholder Management sin complicarlo.

**Recomendacion:** mergear la validacion + las mejoras de prioridad ALTA (#5 sobre
firmas-roles en frontmatter) y MEDIA (#2 stakeholder-map, #3 LLM auto-detect en
orquestador, #7 loop FF-007 → TAA) en una iteracion proxima.

**Versiones:**
- ArquitectureFlow framework: v2026.4
- Validacion ejecutada: 2026-05-07
- Caso usado: AsistIA — Asistente Conversacional para Reclamos (SaludVita Seguros)

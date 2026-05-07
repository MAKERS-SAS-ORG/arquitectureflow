---
titulo: "ADR-[NNN]: [Titulo de la Decision]"
identificador: ADR-[NNN]
tipo: ADR
estado: Aceptado
version: "1.0.0"
autor: "[Nombre]"
fecha-creacion: YYYY-MM-DD
fecha-ultima-revision: YYYY-MM-DD
artefactos-origen: ["RFC-NNN"]
supersede: null
superseded-by: null
firmas-roles: []   # SHOULD firma del Especialista Tecnico. Ver _frontmatter.md
tags: []
---

# ADR-[NNN]: [Titulo de la Decision]

## Roles colaboradores

> ADR formato lightweight: decision ya tomada o de bajo impacto. Aun asi conviene
> dejar evidencia de quien valido. Ver diagrama de roles en `README.md`.

| Rol | Que aporta al SA | Cuando consultarlo |
|---|---|---|
| **Especialista Tecnico** (SWA / Tech Lead) | Validacion rapida de consecuencias tecnicas; firma minimo | Antes de declarar "Aceptado" |
| **DevOps / SRE** | Solo si la decision toca operacion (ej: cambio de runtime, plataforma) | Antes de "Aceptado" si aplica |

> Para decisiones de mayor impacto o con multiples opciones, usar `templates/adr-madr.md` en su lugar.

## Estado
Aceptado

## Contexto
> Las fuerzas en juego, incluyendo tecnologicas, politicas, sociales y especificas del proyecto.
> 2-5 oraciones que explican POR QUE esta decision es necesaria.

## Decision
> La respuesta a las fuerzas. Oraciones completas con voz activa.
> "Usaremos [X] para [Y] porque [Z]."

## Consecuencias
> El contexto resultante despues de aplicar la decision.
> - Positivas: [que mejora]
> - Negativas: [que empeora o se complica]
> - Requiere: [que acciones o decisiones adicionales se derivan]

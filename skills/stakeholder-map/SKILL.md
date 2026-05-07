# Skill: Stakeholder Map — Mapeo de Stakeholders

> Referencia: TOGAF 10th Ed — Stakeholder Management — `references/bibliografia.md#togaf`
> Referencia: ISO/IEC/IEEE 42010:2022 — Architecture Stakeholders & Concerns — `references/bibliografia.md#iso42010`
> Referencia: Mendelow's Power-Interest Grid (1981)

---

## Proposito

Identificar, clasificar y disenar la estrategia de comunicacion con TODOS los
stakeholders de la solucion. Sin este mapa, el SA invierte tiempo de comunicacion
mal asignado: stakeholders criticos quedan informados de mas o de menos, y
bloqueos politicos sorprenden tarde.

## Cuando es Obligatorio

- Sistemas con **mas de 5 stakeholders** identificables (la mayoria de proyectos).
- Sistemas con **regulador externo** (financiero, salud, datos personales).
- Sistemas que **cruzan multiples areas** o **multiples empresas** (joint ventures).
- En escala TOGAF: cualquier sistema en **Architecture Vision** (Fase A) deberia tenerlo.

## Cuando es Opcional

- Sistemas internos con < 5 stakeholders bien conocidos.
- PoCs y spikes (donde el stakeholder es solo el equipo).

## Prerequisitos

- Context Brief aprobado (`CB-NNN`) — el bloque 2 del CB es el insumo principal.

## Roles colaboradores en este artefacto

> Ver bloque "Roles colaboradores" en `templates/stakeholder-map.md` y diagrama en `README.md`.

| Rol | Que pedirle al consultarlo | En que paso del workflow |
|---|---|---|
| **Acelerador / Sponsor** | **Principal.** Mapa politico real, intereses ocultos, historial de cada stakeholder | Pasos 1-2 (lista + power-interest grid) |
| **Patrocinador / VP** | Validar cuadrantes y firmar mapa | Paso 4 (estrategia comunicacion) |
| **Compliance / Legal** | Stakeholders regulatorios externos no obvios | Paso 1 si hay regulador |

## Workflow de Creacion

### Paso 1: Lista exhaustiva de stakeholders
Listar TODOS, sin filtrar. Incluir tipos: Acquirer, User, Developer, Maintainer,
Supplier, Regulator, Influencer (ISO/IEC/IEEE 42010:2022).

### Paso 2: Clasificacion en Power-Interest Grid (Mendelow)
Cada stakeholder en uno de 4 cuadrantes: Manage Closely, Keep Satisfied,
Keep Informed, Monitor. El SA NO debe omitir este paso — lo que parece obvio
casi siempre tiene sorpresas.

### Paso 3: Mapeo de concerns a artefactos
Cada stakeholder se mapea a los artefactos arquitectonicos que le interesan.
Esto evita "entregar la Tech Spec al sponsor" o "el resumen ejecutivo al Tech Lead".

### Paso 4: Estrategia de comunicacion
Frecuencia, canal y formato segun cuadrante. Documentar para que el SA pueda
delegar parte de la comunicacion.

### Paso 5: Riesgos del stakeholder management
Riesgos politicos / organizacionales que pueden bloquear la arquitectura.

## Plantilla

Usar `templates/stakeholder-map.md` como base.

## Diagramas

- **Power-Interest Grid:** Excalidraw (recomendado) — los 4 cuadrantes con
  stakeholders posicionados.
- **Stakeholder Influence Map:** Mermaid o Excalidraw — relaciones de influencia
  entre stakeholders (quien escucha a quien).

## Cuando se actualiza

- Al inicio del proyecto (Fase 0-1 del orquestador).
- En cada **Gate 4 (Post-Deploy / Review Mensual)** del TAA — revalidar cuadrantes.
- Cuando hay cambios organizacionales relevantes.

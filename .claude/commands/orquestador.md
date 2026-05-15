Lee el archivo `skills/orquestador/SKILL.md` completo y ejecuta el flujo.

## Pre-vuelo: Detectar Estado del Proyecto

ANTES de hacer cualquier cosa, escanea el directorio actual y subdirectorios buscando
artefactos de arquitectura existentes: `CB-*.md`, `RFC-*.md`, `ADR-*.md`, `PRD-*.md`,
`TS-*.md`, `API-*.md`, `SD-*.md`, `RO-*.md`, `CM-*.md`, `FF-*.md`, `TAA-*.md`,
`SPS-*.md`, `SM-*.md`.

### Si el usuario escribio `/orquestador` sin argumentos:

**Si NO hay artefactos:** Iniciar flujo nuevo (Fase 0 del skill).
Preguntar al usuario:
1. Que tipo de proyecto es (segun `references/matriz-decision.md`):
   - Nuevo sistema completo
   - Nueva funcionalidad mayor
   - Integracion con sistema externo
   - Cambio de decision arquitectonica
   - Incidente de produccion
   - Spike / investigacion tecnica
   - Agente LLM o componente IA
   - Migracion de plataforma
2. En que carpeta quiere guardar los artefactos (sugerir nombre basado en el proyecto)

**Si SI hay artefactos:** Presentar estado actual y preguntar que hacer:
```
Detecte una arquitectura existente en [carpeta]:

| Artefacto | ID | Estado |
|---|---|---|
| Context Brief | CB-001 | Approved |
| RFC | RFC-001 | Approved |
| ADR | ADR-001 | Aceptado |
| PRD | PRD-001 | Review |
...

Siguiente artefacto recomendado: [el que falta o esta en Draft]
TODOs pendientes: [lista de 🔴 TODOs encontrados]

Que quieres hacer?
1. Continuar con el siguiente artefacto ([nombre])
2. Resolver TODOs pendientes
3. Crear un artefacto especifico
4. Ejecutar critica (Fase 4) sobre un artefacto
5. Generar/actualizar Tablero de Adherencia
6. Iniciar una arquitectura NUEVA en otra carpeta
```

### Si el usuario escribio `/orquestador nuevo`:

Ignorar artefactos existentes. Preguntar tipo de proyecto y nombre de carpeta.
Ir directo a Fase 0 (Context Brief).

### Si el usuario escribio `/orquestador continuar`:

Buscar TODAS las carpetas con artefactos de arquitectura en el proyecto.
Presentar lista:
```
Arquitecturas encontradas:

1. soluciontaller1/ — 10 artefactos (CB-001 Approved, TAA-001 Draft)
2. micro-cdt/ — 4 artefactos (CB-001 Approved, ADR-001..004)
3. mi-proyecto/ — 1 artefacto (CB-001 Draft)

En cual quieres continuar?
```

Luego mostrar el estado detallado de la seleccionada y ofrecer las opciones.

### Si el usuario escribio `/orquestador [otra cosa]`:

Interpretar como instruccion directa. Ejemplos:
- `/orquestador critica el RFC-001` → Cargar Fase 4 sobre ese artefacto
- `/orquestador genera diagrama C4` → Cargar Fase 5
- `/orquestador genera el TAA` → Cargar Fase 7
- `/orquestador estado` → Mostrar estado sin preguntar

## Ejecucion

Una vez determinado el flujo, seguir `skills/orquestador/SKILL.md` desde la fase correspondiente.
Guardar artefactos en la carpeta del proyecto (no en la raiz del framework).

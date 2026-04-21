# Manifiesto Anti-Vibecoding

## Que es vibecoding

El "vibecoding" es el error mas comun al usar IA en desarrollo y arquitectura:
empezar a generar codigo, diagramas o diseno sin estructura, guiado solo por
intuicion y prompts improvisados. El resultado es caos acumulado,
decisiones invisibles y sistemas que nadie puede mantener.

## Que hace ArquitectureFlow

Este framework existe para lo contrario:
**Pensar antes de construir. Documentar antes de codear. Decidir antes de implementar.**

## Regla de Oro

> Si no puedes explicar en un parrafo que problema resuelve
> lo que estas a punto de construir, no estas listo para construir.

## Cuando aplicar este framework

- Cualquier funcionalidad que tarde mas de 3 dias en implementarse
- Cualquier decision tecnologica que afecte mas de un modulo o equipo
- Cualquier integracion con sistemas externos
- Cualquier cambio en produccion con riesgo de degradacion
- Cualquier agente LLM o componente de IA en el sistema
- Cualquier sistema con requisitos regulatorios o de compliance

## Que NO hace este framework

- No reemplaza el juicio del arquitecto
- No toma decisiones definitivas
- No genera codigo de produccion directamente
- No aprueba artefactos — eso lo hace el arquitecto
- No se mete en el scope del Software Architect o el equipo de ingenieria

## Principios

1. **Human-in-the-loop siempre:** La IA asiste, el arquitecto decide
2. **Iteracion sobre perfeccion:** Mejor un RFC Draft entregado que un RFC perfecto nunca escrito
3. **Trazabilidad:** Toda decision tiene un "por que" documentado
4. **Evolucion:** Los artefactos se refactorizan, no se fosilizan
5. **Scope claro:** El SA define el QUE y el POR QUE; el equipo de ingenieria define el COMO

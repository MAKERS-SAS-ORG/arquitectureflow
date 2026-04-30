Ejecuta el taller guiado de ArquitectureFlow con el ejercicio de la plataforma de micro-inversion en CDTs.

## Instrucciones

1. Lee `taller.md` para el contexto completo del ejercicio
2. Lee `skills/orquestador/SKILL.md` para el flujo del orquestador
3. Crea la carpeta `micro-cdt/` si no existe
4. Ejecuta el Pre-vuelo del orquestador:
   - Si `micro-cdt/` tiene artefactos → muestra estado y pregunta donde continuar
   - Si `micro-cdt/` esta vacia → inicia Fase 0 con el problema del taller

## El Problema

El 78% de los colombianos con capacidad de ahorro no invierte porque los CDTs
requieren montos minimos altos y procesos complejos. Se necesita una plataforma
digital que permita micro-inversion en renta fija desde $100.000 COP.

Restricciones: regulacion SFC, equipo de 5 (.NET + AWS), integraciones con
Deceval (custodia), PSE (pagos) y core bancario (KYC). Deadline: MVP Q4 2026.

## Flujo

Guia al arquitecto paso a paso por todos los artefactos:
CB-001 → RFC-001 → ADR-001 → PRD-001 → TS-001 → SD-001 → RO-001 → CM-001 → FF-001 → TAA-001

Guarda todo en `micro-cdt/`. El arquitecto aprueba cada artefacto antes de avanzar.

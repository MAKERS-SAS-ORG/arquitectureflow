---
titulo: "System Prompt Spec: [Nombre del Agente]"
identificador: SPS-[NNN]
tipo: System-Prompt-Spec
estado: Draft
version: "1.0.0"
autor: "[Nombre]"
fecha-creacion: YYYY-MM-DD
fecha-ultima-revision: YYYY-MM-DD
revisores: []
artefactos-origen: ["PRD-NNN"]
nivel-riesgo: Alto | Medio | Bajo
tags: []
---

# System Prompt Spec: [Nombre del Agente]

| Campo | Valor |
|---|---|
| Modelo LLM | [Claude / GPT / Gemini / modelo] |
| Version del prompt | v1.0 |
| Nivel de riesgo | Alto / Medio / Bajo |
| Aprobado por compliance | Si / No / Pendiente 🔴 |

## 1. Proposito del Agente
> Una sola oracion: que hace el agente y para quien.

## 2. Capacidades Permitidas (Allowlist)
El agente PUEDE:
- [ ] [capacidad 1]
- [ ] [capacidad 2]

## 3. Restricciones Obligatorias (Denylist)
El agente NO PUEDE bajo ninguna circunstancia:
- [ ] [restriccion 1]
- [ ] [restriccion 2]

## 4. System Prompt (version aprobada)

```
[INICIO SYSTEM PROMPT — NO MODIFICAR SIN APROBACION DEL ARQUITECTO]

[contenido del system prompt]

[FIN SYSTEM PROMPT]
```

## 5. Datos de Contexto Inyectados
```
CONTEXTO DEL USUARIO:
- [campo 1]: {variable}
- [campo 2]: {variable}
[NO incluir: datos sensibles que el agente no necesita]
```

## 6. Test Cases

| Caso | Input | Comportamiento esperado | Criterio de falla |
|---|---|---|---|
| Pregunta normal | [input] | [respuesta esperada] | [que seria falla] |
| Prompt injection | [intento de inyeccion] | Rechaza y explica limites | Obedece instruccion |
| Fuera de scope | [pregunta irrelevante] | Redirige a su funcion | Responde libremente |

## 7. Observabilidad del Agente
- Loguear: input, respuesta, model version, latencia
- NO loguear en texto plano: datos personales, informacion financiera
- Retencion: [dias] para revision, luego anonimizar

## 8. Compliance
- [Regulaciones aplicables al uso de IA en este dominio]
- Texto de disclosure obligatorio: "[texto]"

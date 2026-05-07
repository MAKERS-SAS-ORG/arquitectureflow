---
titulo: "ADR-[NNN]: [Titulo de la Decision]"
identificador: ADR-[NNN]
tipo: ADR
estado: Propuesto
version: "1.0.0"
autor: "[Nombre]"
fecha-creacion: YYYY-MM-DD
fecha-ultima-revision: YYYY-MM-DD
revisores: ["@persona1"]
artefactos-origen: ["RFC-NNN"]
supersede: null
superseded-by: null
firmas-roles: []   # MUST firma del Especialista Tecnico para estado Aceptado. Ver _frontmatter.md
tags: []
---

# ADR-[NNN]: [Titulo de la Decision]

## Roles colaboradores

> El SA es el dueno de la decision. Aqui el dialogo es casi 100% con el **Especialista Tecnico**.
> Ver diagrama de roles en `README.md`.

| Rol | Que aporta al SA | Cuando consultarlo |
|---|---|---|
| **Especialista Tecnico** (SWA / Tech Lead) | Consecuencias tecnicas de cada opcion, costo de operacion, deuda esperada, alternativas que el SA no vio | Antes de cerrar la seccion "Decision" y al redactar "Consecuencias" (es el rol que mejor anticipa los trade-offs reales) |
| **Acelerador** (Negocio) | Solo si la decision tiene impacto economico relevante (vendor lock-in, licencias) | Validar la justificacion economica si aplica |
| **DevOps / SRE** | Solo si la decision impacta operacion (eleccion de plataforma cloud, estrategia de deployment) | Validar viabilidad operativa antes de aprobar |

## Estado
Propuesto | Aceptado | Deprecado | Supersedido por ADR-NNN

## Contexto y Problema
> Describe el contexto sin el cual la decision no tiene sentido.
> Incluye las fuerzas en juego: tecnicas, regulatorias, de equipo.
> Sin este contexto, en 6 meses nadie entendera por que se decidio esto.

## Decision Drivers
- [Driver 1]: [descripcion y por que importa]
- [Driver 2]: [descripcion y por que importa]

## Opciones Consideradas
- Opcion 1: [nombre descriptivo]
- Opcion 2: [nombre descriptivo]
- Opcion 3: [nombre descriptivo]

## Decision

**Opcion elegida: "[Nombre]"**

### Justificacion
Porque [razon tecnica especifica], lo que satisface [criterio X].
A diferencia de [opcion alternativa] que [razon de descarte].

## Pros y Contras de las Opciones

### Opcion 1: [Nombre]
- (+) [pro]
- (-) [contra]

### Opcion 2: [Nombre]
- (+) [pro]
- (-) [contra]

### Opcion 3: [Nombre]
- (+) [pro]
- (-) [contra]

## Consecuencias

### Positivas
- [consecuencia positiva]

### Negativas / Trade-offs
- [trade-off — ser honesto aqui es critico]

### Neutrales
- [consecuencia neutral]

## Validacion
> Como sabremos en el futuro que fue la decision correcta?
- **Metrica:** [que medir]
- **Senal de alerta:** [que observar que indica re-evaluacion]
- **Revision programada:** [fecha o condicion]

## Referencias
- RFC-NNN, Seccion X.Y
- [Documentacion externa]

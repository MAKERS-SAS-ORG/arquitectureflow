---
titulo: "Context Map: [Nombre del Sistema]"
identificador: CM-[NNN]
tipo: Context-Map
estado: Draft
version: "1.0.0"
autor: "[Nombre]"
fecha-creacion: YYYY-MM-DD
fecha-ultima-revision: YYYY-MM-DD
artefactos-origen: ["SD-NNN"]
firmas-roles: []   # SHOULD firma del Especialista Tecnico (DDD). Ver _frontmatter.md
tags: []
---

# Context Map: [Nombre del Sistema]

> Referencia: Evans, E. *Domain-Driven Design.* 2003. Capitulo 14: Context Map.
> Referencia: Vernon, V. *Domain-Driven Design Distilled.* 2016. Capitulo 4.

## Roles colaboradores

> El SA mapea bounded contexts a nivel de solucion. El **Especialista Tecnico** es el
> aliado natural (DDD tactico). El **Acelerador** ayuda a separar Core de Supporting/Generic
> segun valor de negocio. Ver diagrama de roles en `README.md`.

| Rol | Que aporta al SA | Cuando consultarlo |
|---|---|---|
| **Acelerador** (Negocio) | Cuales subdominios son Core (diferenciador), cuales Supporting (necesarios) y cuales Generic (commodity) | Tabla de Bounded Contexts — clasificacion Core/Supporting/Generic |
| **Especialista Tecnico** (SWA / Tech Lead) | Patrones de relacion realistas (ACL, Conformist, Customer-Supplier), eventos de dominio existentes, riesgo de acoplamiento | Tabla de relaciones y tabla de domain events |
| **Equipos de cada bounded context** (si ya existen) | Realidad de sus interfaces y contratos actuales | Antes de definir Conformist o Partnership con su contexto |

## Bounded Contexts Identificados

| Bounded Context | Subdominio | Tipo | Responsabilidad |
|---|---|---|---|
| [Nombre] | Core / Supporting / Generic | [tipo] | [que hace] |

## Relaciones entre Contexts

| Upstream | Downstream | Patron | Descripcion |
|---|---|---|---|
| [Context A] | [Context B] | Customer-Supplier | [A provee API, B consume] |

### Patrones de Relacion (referencia DDD)

| Patron | Cuando usar |
|---|---|
| **Shared Kernel** | Dos contextos comparten un subconjunto del modelo |
| **Customer-Supplier** | Upstream/downstream con contrato negociado |
| **Conformist** | Downstream se adapta al modelo del upstream sin negociar |
| **Anti-Corruption Layer (ACL)** | Capa de traduccion que protege un contexto del modelo de otro |
| **Open Host Service** | API/protocolo bien definido para integracion publica |
| **Published Language** | Formato de intercambio estandar (JSON Schema, Protobuf, Avro) |
| **Separate Ways** | Sin integracion, contextos operan independientemente |
| **Partnership** | Coordinacion estrecha, dependencia mutua |

## Diagrama

> Generar con Excalidraw MCP: cada bounded context como rectangulo,
> relaciones como flechas con label del patron.

[Insertar diagrama]

## Domain Events entre Contexts

| Evento | Productor | Consumidor | Payload principal |
|---|---|---|---|
| [NombreEvento] | [Context] | [Context] | [campos clave] |

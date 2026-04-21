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
tags: []
---

# Context Map: [Nombre del Sistema]

> Referencia: Evans, E. *Domain-Driven Design.* 2003. Capitulo 14: Context Map.
> Referencia: Vernon, V. *Domain-Driven Design Distilled.* 2016. Capitulo 4.

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

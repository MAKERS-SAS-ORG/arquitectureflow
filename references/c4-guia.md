# Guia C4 Model para Arquitecto de Soluciones

> Referencia: Brown, S. *The C4 Model for Visualising Software Architecture.* c4model.com
> Principio: "Abstractions first, notation second"

---

## Los 4 Niveles de Zoom

```
L1: System Context  ──  El bosque (todos los arboles son cajas)
L2: Container        ──  Un arbol (ramas = contenedores)
L3: Component        ──  Una rama (hojas = componentes)
L4: Code             ──  Una hoja (nervaduras = clases)
```

## Uso Estrategico de Diagramas (Scope del SA)

> **Regla:** El SA se enfoca UNICAMENTE en L1 (Context) para comunicar con negocio
> y L2 (Container) para comunicar con desarrollo. Detallar componentes internos
> (L3 y L4) es responsabilidad del equipo de software.

| Nivel | Scope SA | Scope SWA | Audiencia |
|---|---|---|---|
| **L1 Context** | MUST crear | Revisar | Stakeholders de negocio, C-level, todos |
| **L2 Container** | MUST crear | Co-crear | Equipo tecnico, arquitectos, DevOps |
| **L3 Component** | Solo revisar | MUST crear | Desarrolladores del equipo |
| **L4 Code** | Fuera de scope | Opcional | Desarrolladores (auto-generar si es necesario) |

### Cuando usar cada nivel

- **L1 Context:** SIEMPRE como primer diagrama de cualquier proyecto. Es la herramienta
  principal de comunicacion del SA con stakeholders no tecnicos. Si solo puedes hacer
  un diagrama, haz este.
- **L2 Container:** Para cualquier sistema con mas de un componente deployable. Es el
  diagrama central de la Tech Spec. Muestra las decisiones tecnologicas del SA.
- **L3 Component:** El SA NO crea este diagrama. Lo revisa para verificar que
  cumpla con los contratos y NFRs definidos en la Tech Spec.

## Vocabulario C4

### Persona
Un usuario humano del sistema. Puede ser interno (empleado) o externo (cliente).
- Label: Nombre + Descripcion breve
- Ejemplo: "Inversionista — Persona que invierte en fondos de inversion"

### Sistema
Una aplicacion, servicio o conjunto de servicios que entrega valor.
- **Sistema principal:** El que estamos disenando (azul)
- **Sistema externo:** Sistemas de terceros o legacy (gris)
- Label: Nombre + Descripcion + [Tecnologia si es relevante]

### Contenedor (L2)
Una unidad deployable que ejecuta codigo o almacena datos:
- Aplicacion web, API, microservicio, serverless function
- Base de datos, file system, cache
- Cola de mensajes, event bus, stream
- Label: Nombre + [Tecnologia] + Descripcion

### Relacion
Conexion entre elementos. SIEMPRE incluir:
- **Verbo:** Que hace (Envia, Consulta, Lee, Escribe, Notifica)
- **Protocolo/mecanismo:** [REST/HTTPS], [gRPC], [Async/SQS], [TCP], [JDBC]

## Errores Comunes

1. **Diagrama demasiado detallado para L1:** L1 es contexto, no arquitectura interna
2. **Sin labels en relaciones:** Una flecha sin label no comunica nada
3. **Mezclar niveles:** No poner componentes internos en un diagrama de contexto
4. **Olvidar sistemas externos:** El valor de L1 es ver TODO lo que interactua
5. **No indicar tecnologia en L2:** Los contenedores sin tecnologia son ambiguos
6. **Diagrama sin titulo y leyenda:** Siempre incluir titulo del diagrama y nivel C4

## Template de Elementos para Excalidraw

Al generar diagramas C4 con Excalidraw, cada elemento MUST seguir esta estructura visual:

```
┌─────────────────────────┐
│    [Nombre]             │
│    [Tecnologia]         │
│                         │
│    Descripcion breve    │
└─────────────────────────┘
```

Para personas:
```
     ┌───┐
     │ 👤│
     └───┘
  [Nombre]
  [Descripcion]
```

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

## Scope del Arquitecto de Soluciones

| Nivel | Scope SA | Scope SWA | Notas |
|---|---|---|---|
| **L1 Context** | MUST crear | Revisar | SA lidera. Es el diagrama de comunicacion principal. |
| **L2 Container** | MUST crear | Co-crear | SA define contenedores y relaciones. SWA valida viabilidad. |
| **L3 Component** | Revisar | MUST crear | SWA lidera. SA revisa que cumpla NFRs y contratos. |
| **L4 Code** | Fuera de scope | Opcional | Auto-generar si es necesario. |

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

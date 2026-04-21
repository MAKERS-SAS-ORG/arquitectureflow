# Catalogo de Patrones de Integracion

> Referencia: Hohpe, G.; Woolf, B. *Enterprise Integration Patterns.* Addison-Wesley, 2003.
> Referencia: Brown, S. *C4 Model.* c4model.com — Container relationships.

---

## Patrones por Tipo de Comunicacion

### Sincrona (Request-Reply)

| Patron | Cuando usar | Trade-off |
|---|---|---|
| **REST/HTTP** | APIs publicas, CRUD simple, integracion con terceros | Simple pero acoplamiento temporal |
| **gRPC** | Comunicacion interna alta performance, contratos estrictos | Mas eficiente pero menos universal |
| **GraphQL** | Clientes con necesidades de datos variables (mobile, SPA) | Flexible pero complejidad en backend |

### Asincrona (Fire-and-Forget / Event-Driven)

| Patron | Cuando usar | Trade-off |
|---|---|---|
| **Message Queue** (SQS, RabbitMQ) | Procesamiento diferido, desacoplamiento temporal | Eventual consistency |
| **Pub/Sub** (SNS, Kafka topics) | Multiples consumidores, event-driven architecture | Complejidad de debugging |
| **Event Streaming** (Kafka, Kinesis) | Event sourcing, analytics en tiempo real, replay | Infraestructura mas compleja |

### Batch

| Patron | Cuando usar | Trade-off |
|---|---|---|
| **File Transfer** (S3, SFTP) | Integracion legacy, volumenes grandes periodicos | Latencia alta, complejidad de reconciliacion |
| **Database Replication** | Read replicas, analytics | Acoplamiento a schema |

## Patrones de Resiliencia (a nivel de politica SA)

| Patron | Proposito | Definicion SA |
|---|---|---|
| **Retry con Backoff** | Tolerancia a fallos transitorios | SA define: max reintentos, backoff base, timeout total |
| **Circuit Breaker** | Evitar cascada de fallos | SA define: umbral de apertura, tiempo de half-open |
| **Bulkhead** | Aislar fallos por dominio | SA define: que dominios se aislan |
| **Timeout** | Evitar espera indefinida | SA define: timeout por sistema externo |
| **Fallback** | Degradacion graceful | SA define: comportamiento alternativo por sistema |

**Nota:** El SA define la POLITICA (cuantos reintentos, que timeout). La IMPLEMENTACION (Polly, Resilience4j, custom) es decision del Software Architect.

## Patrones de Consistencia

| Patron | Cuando usar | Trade-off |
|---|---|---|
| **Saga (Orchestration)** | Transacciones distribuidas con coordinador central | Single point of failure en orquestador |
| **Saga (Choreography)** | Transacciones distribuidas sin coordinador | Dificil de debuggear flujo completo |
| **Outbox Pattern** | Garantizar at-least-once delivery de eventos | Complejidad adicional en DB |
| **Idempotencia** | Operaciones seguras ante retry | Cada escritura necesita idempotency key |

## Seleccion Rapida

```
Necesito integracion...

├── Sincrona y simple? ──────> REST/HTTP
├── Sincrona y alto performance? ──> gRPC
├── Asincrona y un consumidor? ──> Message Queue
├── Asincrona y multiples consumidores? ──> Pub/Sub
├── Con replay y auditoria? ──> Event Streaming
├── Con sistema legacy? ──> File Transfer o ACL
└── Transaccion distribuida? ──> Saga + Idempotencia
```

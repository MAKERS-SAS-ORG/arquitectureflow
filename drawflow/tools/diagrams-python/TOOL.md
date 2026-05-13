# Herramienta: Diagrams Python (diagrams.mingrammer.com)
# Tipo: Script Python + Graphviz
# Repo: https://github.com/mingrammer/diagrams

---

## Resumen

Librería Python para diagramar infraestructura cloud como código (Diagram as Code).
Genera imágenes PNG/SVG con **iconos oficiales** de proveedores cloud.

Ideal para: arquitectura de infraestructura AWS/GCP/Azure/K8s con iconos reales.
Complementario a Excalidraw para diagramas que necesitan reconocimiento visual
inmediato de servicios cloud.

## Setup

### Activar entorno virtual
```bash
source /Users/didierrestrepo/MK/arquitectureflow-main/drawflow/tools/diagrams-python/.venv/bin/activate
```

### Verificar
```bash
python3 -c "from diagrams import Diagram; print('OK')"
dot -V  # Graphviz
```

### Requisitos del sistema
- Python 3.7+ ✅ (instalado: 3.14.3)
- Graphviz ✅ (instalado: 12.1.1)
- diagrams ✅ (instalado: 0.25.1)

---

## Sintaxis Básica

```python
from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Nombre del Diagrama", show=False, direction="TB"):
    lb = ELB("Load Balancer")
    with Cluster("Web Tier"):
        web = [EC2("web1"), EC2("web2")]
    db = RDS("Database")
    
    lb >> web >> db
```

### Operadores de conexión
| Operador | Significado |
|---|---|
| `>>` | Flecha de izq a der (o arriba a abajo) |
| `<<` | Flecha de der a izq |
| `-` | Línea sin dirección |
| `Edge(color="red", label="HTTPS")` | Conexión con estilo |

### Parámetros de Diagram
| Param | Default | Descripción |
|---|---|---|
| `show` | `True` | Abrir imagen al generar |
| `direction` | `"LR"` | `"LR"`, `"TB"`, `"RL"`, `"BT"` |
| `filename` | nombre del diagrama | Nombre del archivo output |
| `outformat` | `"png"` | `"png"`, `"svg"`, `"pdf"`, `"dot"` |
| `graph_attr` | `{}` | Atributos de Graphviz |

---

## Proveedores Disponibles

### Cloud
| Proveedor | Import | Ejemplos |
|---|---|---|
| AWS | `diagrams.aws.*` | EC2, ECS, EKS, Lambda, RDS, S3, SQS, ELB, Route53, CloudFront |
| GCP | `diagrams.gcp.*` | GCE, GKE, Cloud Run, BigQuery, PubSub, Cloud SQL |
| Azure | `diagrams.azure.*` | VM, AKS, Functions, SQL DB, CosmosDB, Event Grid |
| K8s | `diagrams.k8s.*` | Pod, Deployment, Service, Ingress, StatefulSet, HPA |
| Firebase | `diagrams.firebase.*` | Auth, Firestore, Functions, Hosting |

### On-Premises
| Categoria | Import | Ejemplos |
|---|---|---|
| Compute | `diagrams.onprem.compute` | Server, Nomad |
| Database | `diagrams.onprem.database` | PostgreSQL, MySQL, MongoDB, Cassandra |
| Queue | `diagrams.onprem.queue` | Kafka, RabbitMQ, Celery |
| Cache | `diagrams.onprem.inmemory` | Redis, Memcached |
| Monitoring | `diagrams.onprem.monitoring` | Prometheus, Grafana, Datadog |
| Network | `diagrams.onprem.network` | Nginx, HAProxy, Traefik |
| CI/CD | `diagrams.onprem.ci` | Jenkins, GitLab CI, GitHub Actions |

### C4 Model
| Nodo | Import |
|---|---|
| Person | `diagrams.c4.Person` |
| System | `diagrams.c4.System` |
| Container | `diagrams.c4.Container` |
| Component | `diagrams.c4.Component` |
| SystemBoundary | `diagrams.c4.SystemBoundary` |
| Relationship | `diagrams.c4.Relationship` |

### Custom
```python
from diagrams.custom import Custom
custom_node = Custom("Mi Servicio", "/path/to/icon.png")
```

---

## Templates Disponibles

Ver `drawflow/tools/diagrams-python/templates/`:
- `c4_context.py` — C4 Level 1 (System Context)
- `c4_container.py` — C4 Level 2 (Container)
- `aws_architecture.py` — Arquitectura AWS típica
- `k8s_deployment.py` — Deployment Kubernetes
- `microservices.py` — Microservicios con eventos

### Ejecutar un template
```bash
source /Users/didierrestrepo/MK/arquitectureflow-main/drawflow/tools/diagrams-python/.venv/bin/activate
cd /Users/didierrestrepo/MK/arquitectureflow-main/drawflow/tools/diagrams-python
python3 templates/c4_context.py
# Output: c4_system_context.png
```

---

## Workflow para el Agente

1. Activar venv
2. Crear script Python con la arquitectura requerida
3. Ejecutar con `python3 script.py`
4. El PNG se genera en el directorio actual
5. Mover a `drawflow/tools/diagrams-python/output/` si se desea preservar

### Para C4 con Diagrams Python

```python
from diagrams import Diagram
from diagrams.c4 import Person, Container, System, SystemBoundary, Relationship

with Diagram("C4 Context", show=False):
    customer = Person("Customer", "A user of the system")
    
    with SystemBoundary("Enterprise"):
        webapp = Container("Web App", "React", "Delivers content")
        api = Container("API", "Node.js", "Business logic")
        db = Container("Database", "PostgreSQL", "Stores data")
    
    email = System("Email System", "SendGrid")
    
    customer >> Relationship("Uses") >> webapp
    webapp >> Relationship("API calls") >> api
    api >> Relationship("Reads/Writes") >> db
    api >> Relationship("Sends emails") >> email
```

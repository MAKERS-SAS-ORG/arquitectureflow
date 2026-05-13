"""
Microservices Architecture Diagram — Template
Arquitectura de microservicios con API Gateway, event bus y servicios.
Genera: microservices_architecture.png

Uso:
  source drawflow/tools/diagrams-python/.venv/bin/activate
  python3 drawflow/tools/diagrams-python/templates/microservices.py
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL, MongoDB
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.queue import Kafka
from diagrams.onprem.network import Nginx, Traefik
from diagrams.onprem.monitoring import Prometheus, Grafana
from diagrams.onprem.logging import FluentBit
from diagrams.onprem.tracing import Jaeger

graph_attr = {
    "splines": "spline",
    "pad": "1.5",
    "nodesep": "0.7",
    "ranksep": "1.0",
    "fontname": "Sans-Serif",
    "fontsize": "14",
}

with Diagram(
    "Microservices Architecture",
    show=False,
    direction="TB",
    filename="microservices_architecture",
    graph_attr=graph_attr,
):
    gateway = Traefik("API Gateway")

    with Cluster("Services"):
        with Cluster("User Domain"):
            user_svc = Server("User Service")
            user_db = PostgreSQL("Users DB")
            user_svc >> user_db

        with Cluster("Order Domain"):
            order_svc = Server("Order Service")
            order_db = PostgreSQL("Orders DB")
            order_svc >> order_db

        with Cluster("Product Domain"):
            product_svc = Server("Product Service")
            product_db = MongoDB("Products DB")
            product_svc >> product_db

        with Cluster("Notification Domain"):
            notif_svc = Server("Notification Svc")

    with Cluster("Infrastructure"):
        event_bus = Kafka("Event Bus")
        cache = Redis("Shared Cache")

    with Cluster("Observability"):
        prom = Prometheus("Metrics")
        graf = Grafana("Dashboards")
        logs = FluentBit("Log Collector")
        tracer = Jaeger("Tracing")
        prom >> graf

    gateway >> Edge(color="darkgreen") >> user_svc
    gateway >> Edge(color="darkgreen") >> order_svc
    gateway >> Edge(color="darkgreen") >> product_svc

    order_svc >> Edge(label="OrderCreated", color="orange") >> event_bus
    user_svc >> Edge(label="UserRegistered", color="orange") >> event_bus
    event_bus >> Edge(label="consume", color="blue") >> notif_svc
    event_bus >> Edge(label="consume", color="blue") >> product_svc

    user_svc >> Edge(color="red", style="dashed") >> cache
    order_svc >> Edge(color="red", style="dashed") >> cache

    [user_svc, order_svc, product_svc] >> Edge(
        color="gray", style="dashed"
    ) >> logs

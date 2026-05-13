"""
C4 Container Diagram — Template
Diagrama C4 Nivel 2: muestra los contenedores (apps, servicios, DBs) del sistema.
Genera: c4_container_diagram.png

Uso:
  source drawflow/tools/diagrams-python/.venv/bin/activate
  python3 drawflow/tools/diagrams-python/templates/c4_container.py
"""

from diagrams import Diagram, Edge
from diagrams.c4 import (
    Person, Container, System, SystemBoundary,
    Database, Relationship
)

graph_attr = {
    "splines": "spline",
    "pad": "2.0",
    "nodesep": "0.8",
    "ranksep": "1.2",
    "fontname": "Sans-Serif",
    "fontsize": "18",
    "fontcolor": "#2D3436",
}

with Diagram(
    "C4 Container Diagram",
    show=False,
    direction="TB",
    filename="c4_container_diagram",
    graph_attr=graph_attr,
):
    customer = Person(
        name="Cliente",
        technology="Persona Natural",
        description="Usa la app web/móvil",
    )

    with SystemBoundary("Sistema de Pedidos"):
        webapp = Container(
            name="Web App",
            technology="React / Next.js",
            description="Interfaz web para clientes",
        )

        mobile = Container(
            name="Mobile App",
            technology="React Native",
            description="App móvil para clientes",
        )

        api = Container(
            name="API Gateway",
            technology="Node.js / Express",
            description="API REST - Lógica de negocio",
        )

        worker = Container(
            name="Worker Service",
            technology="Node.js",
            description="Procesa tareas asíncronas",
        )

        db = Database(
            name="Base de Datos",
            technology="PostgreSQL",
            description="Almacena pedidos, usuarios",
        )

        cache = Database(
            name="Cache",
            technology="Redis",
            description="Sesiones y cache",
        )

        queue = Container(
            name="Cola de Mensajes",
            technology="RabbitMQ",
            description="Eventos asíncronos",
        )

    email = System(
        name="Email Service",
        technology="SendGrid",
        description="Notificaciones por correo",
        external=True,
    )

    payment = System(
        name="Payment Gateway",
        technology="Stripe",
        description="Procesamiento de pagos",
        external=True,
    )

    customer >> Relationship("Usa [HTTPS]") >> webapp
    customer >> Relationship("Usa [HTTPS]") >> mobile
    webapp >> Relationship("API calls [JSON/HTTPS]") >> api
    mobile >> Relationship("API calls [JSON/HTTPS]") >> api
    api >> Relationship("Lee/Escribe") >> db
    api >> Relationship("Cache [TCP]") >> cache
    api >> Relationship("Publica eventos") >> queue
    queue >> Relationship("Consume") >> worker
    worker >> Relationship("Envía email [API]") >> email
    api >> Relationship("Cobra [API]") >> payment

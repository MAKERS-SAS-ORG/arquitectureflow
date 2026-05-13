"""
C4 System Context Diagram — Template
Diagrama C4 Nivel 1: muestra el sistema en su contexto con usuarios y sistemas externos.
Genera: c4_system_context.png

Uso:
  source drawflow/tools/diagrams-python/.venv/bin/activate
  python3 drawflow/tools/diagrams-python/templates/c4_context.py
"""

from diagrams import Diagram, Edge
from diagrams.c4 import Person, System, SystemBoundary, Relationship

graph_attr = {
    "splines": "spline",
    "pad": "2.0",
    "nodesep": "1.0",
    "ranksep": "1.5",
    "fontname": "Sans-Serif",
    "fontsize": "18",
    "fontcolor": "#2D3436",
}

with Diagram(
    "C4 System Context",
    show=False,
    direction="TB",
    filename="c4_system_context",
    graph_attr=graph_attr,
):
    customer = Person(
        name="Cliente",
        technology="Persona Natural",
        description="Usa la aplicación web para gestionar sus pedidos",
    )

    admin = Person(
        name="Administrador",
        technology="Persona Interna",
        description="Gestiona productos, usuarios y configuración",
    )

    with SystemBoundary("Enterprise Boundary"):
        system = System(
            name="Sistema de Pedidos",
            technology="Next.js + Node.js",
            description="Permite a los clientes crear y rastrear pedidos",
        )

    email = System(
        name="Sistema de Email",
        technology="SendGrid",
        description="Envía notificaciones por correo",
        external=True,
    )

    payment = System(
        name="Pasarela de Pagos",
        technology="Stripe",
        description="Procesa pagos con tarjeta",
        external=True,
    )

    erp = System(
        name="ERP Legacy",
        technology="SAP",
        description="Sistema de inventario y facturación",
        external=True,
    )

    customer >> Relationship("Crea pedidos [HTTPS]") >> system
    admin >> Relationship("Administra [HTTPS]") >> system
    system >> Relationship("Envía emails [API]") >> email
    system >> Relationship("Procesa pagos [API]") >> payment
    system >> Relationship("Consulta inventario [SOAP]") >> erp

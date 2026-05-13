"""
AWS Architecture Diagram — Template
Arquitectura típica en AWS con ELB, ECS, RDS, cache y monitoring.
Genera: aws_architecture.png

Uso:
  source drawflow/tools/diagrams-python/.venv/bin/activate
  python3 drawflow/tools/diagrams-python/templates/aws_architecture.py
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import ECS, Lambda
from diagrams.aws.database import RDS, ElastiCache
from diagrams.aws.network import ELB, Route53, CloudFront
from diagrams.aws.storage import S3
from diagrams.aws.integration import SQS, SNS
from diagrams.aws.management import Cloudwatch
from diagrams.aws.security import WAF

graph_attr = {
    "splines": "spline",
    "pad": "1.5",
    "nodesep": "0.8",
    "ranksep": "1.0",
    "fontname": "Sans-Serif",
    "fontsize": "16",
}

with Diagram(
    "AWS Architecture",
    show=False,
    direction="TB",
    filename="aws_architecture",
    graph_attr=graph_attr,
):
    dns = Route53("Route53\nDNS")
    cdn = CloudFront("CloudFront\nCDN")
    waf = WAF("WAF")

    dns >> cdn >> waf

    with Cluster("VPC"):
        lb = ELB("ALB")
        waf >> lb

        with Cluster("App Tier (ECS Fargate)"):
            services = [
                ECS("API Service"),
                ECS("Auth Service"),
                ECS("Order Service"),
            ]

        lb >> services

        with Cluster("Data Tier"):
            with Cluster("Database"):
                db_primary = RDS("Primary")
                db_replica = RDS("Read Replica")
                db_primary - Edge(style="dashed") - db_replica

            cache = ElastiCache("Redis\nCache")

        services >> db_primary
        services >> cache

    with Cluster("Async Processing"):
        queue = SQS("Order Queue")
        topic = SNS("Notifications")
        worker = Lambda("Order\nProcessor")

        services >> queue >> worker
        worker >> topic

    static = S3("Static Assets")
    cdn >> Edge(style="dashed") >> static

    monitoring = Cloudwatch("CloudWatch")
    services >> Edge(color="gray", style="dashed") >> monitoring

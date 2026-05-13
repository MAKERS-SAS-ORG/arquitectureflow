"""
Kubernetes Deployment Diagram — Template
Deployment típico en K8s con ingress, services, pods, y storage.
Genera: k8s_deployment.png

Uso:
  source drawflow/tools/diagrams-python/.venv/bin/activate
  python3 drawflow/tools/diagrams-python/templates/k8s_deployment.py
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.k8s.compute import Deployment, Pod, ReplicaSet, StatefulSet
from diagrams.k8s.network import Ingress, Service
from diagrams.k8s.storage import PV, PVC, StorageClass
from diagrams.k8s.clusterconfig import HPA
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.monitoring import Prometheus, Grafana

graph_attr = {
    "splines": "spline",
    "pad": "1.5",
    "nodesep": "0.6",
    "ranksep": "0.8",
    "fontname": "Sans-Serif",
    "fontsize": "14",
}

with Diagram(
    "Kubernetes Deployment",
    show=False,
    direction="TB",
    filename="k8s_deployment",
    graph_attr=graph_attr,
):
    ingress = Ingress("api.example.com")

    with Cluster("Namespace: production"):
        with Cluster("API Service"):
            api_svc = Service("api-svc")
            api_hpa = HPA("api-hpa")
            api_pods = [Pod("api-1"), Pod("api-2"), Pod("api-3")]
            api_dep = Deployment("api-deploy")
            api_hpa >> api_dep
            api_svc >> api_pods

        with Cluster("Worker Service"):
            worker_svc = Service("worker-svc")
            worker_pods = [Pod("worker-1"), Pod("worker-2")]
            worker_dep = Deployment("worker-deploy")
            worker_svc >> worker_pods

        with Cluster("Database"):
            db_svc = Service("db-svc")
            db_ss = StatefulSet("postgres-ss")
            db_pod = Pod("postgres-0")
            db_pvc = PVC("data-pvc")
            db_pv = PV("data-pv")
            db_svc >> db_pod
            db_pod - db_pvc - db_pv

        with Cluster("Cache"):
            cache_svc = Service("redis-svc")
            cache_pod = Pod("redis-0")
            cache_svc >> cache_pod

    with Cluster("Monitoring"):
        prom = Prometheus("prometheus")
        graf = Grafana("grafana")
        prom >> graf

    ingress >> api_svc
    api_pods >> Edge(color="brown") >> db_svc
    api_pods >> Edge(color="red") >> cache_svc
    api_pods >> Edge(style="dashed") >> worker_svc
    api_pods >> Edge(color="gray", style="dashed") >> prom

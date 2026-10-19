from __future__ import annotations

from .ideological_cluster import IdeologicalCluster


class ClusterRegistry:

    def __init__(self) -> None:
        self._clusters: list[IdeologicalCluster] = []

    def register(self, cluster: IdeologicalCluster) -> None:
        self._clusters.append(cluster)

    def clusters(self) -> tuple[IdeologicalCluster, ...]:
        return tuple(self._clusters)

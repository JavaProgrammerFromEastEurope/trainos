from .ideological_cluster import IdeologicalCluster


class IdeologyEngine:

    def form_cluster(self, name: str) -> IdeologicalCluster:
        return IdeologicalCluster(name=name)

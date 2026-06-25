from trainos.kernel.evolution.memetics.ideology.cluster_registry import ClusterRegistry
from trainos.kernel.evolution.memetics.ideology.ideological_cluster import IdeologicalCluster


def test_cluster_registry_register():

    registry = ClusterRegistry()

    cluster = IdeologicalCluster(
        name="sustainability",
    )

    registry.register(cluster)

    assert registry.clusters() == (cluster,)
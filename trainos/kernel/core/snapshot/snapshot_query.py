from .snapshot_registry import SnapshotRegistry


class SnapshotQuery:

    def latest(self, registry: SnapshotRegistry):
        return registry.latest()

    def all(self, registry: SnapshotRegistry):
        return registry.all()

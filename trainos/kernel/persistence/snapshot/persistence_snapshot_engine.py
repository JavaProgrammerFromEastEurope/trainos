from .persistence_snapshot import PersistenceSnapshot


class PersistenceSnapshotEngine:

    def capture(
        self,
        snapshot: PersistenceSnapshot,
    ) -> PersistenceSnapshot:
        return snapshot

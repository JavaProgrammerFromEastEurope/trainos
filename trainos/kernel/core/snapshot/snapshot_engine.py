from .base_snapshot import BaseSnapshot


class SnapshotEngine:

    def capture(
        self,
        snapshot: BaseSnapshot,
    ) -> BaseSnapshot:
        return snapshot

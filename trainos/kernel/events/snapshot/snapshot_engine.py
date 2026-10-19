from .event_snapshot import EventSnapshot


class SnapshotEngine:

    def capture(
        self,
        snapshot: EventSnapshot,
    ) -> EventSnapshot:
        return snapshot

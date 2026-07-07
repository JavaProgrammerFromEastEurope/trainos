from .logistics_snapshot import LogisticsSnapshot


class LogisticsSnapshotEngine:

    def capture(
        self,
        snapshot: LogisticsSnapshot,
    ) -> LogisticsSnapshot:
        return snapshot
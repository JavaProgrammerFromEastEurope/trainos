from .consumption_snapshot import ConsumptionSnapshot


class ConsumptionSnapshotEngine:

    def capture(
        self,
        snapshot: ConsumptionSnapshot,
    ) -> ConsumptionSnapshot:
        return snapshot  

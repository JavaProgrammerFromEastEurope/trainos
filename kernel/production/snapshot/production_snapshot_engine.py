from .production_snapshot import ProductionSnapshot


class ProductionSnapshotEngine:

    def capture(
        self,
        snapshot: ProductionSnapshot,
    ) -> ProductionSnapshot:
        return snapshot

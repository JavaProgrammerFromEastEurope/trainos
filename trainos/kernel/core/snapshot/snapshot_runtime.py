from .snapshot_engine import SnapshotEngine


class SnapshotRuntime:

    def __init__(self) -> None:
        self._engine = SnapshotEngine()

    def initialize(self) -> None:
        pass

    def update(self, snapshot):
        return self._engine.capture(snapshot)

    def shutdown(self) -> None:
        pass

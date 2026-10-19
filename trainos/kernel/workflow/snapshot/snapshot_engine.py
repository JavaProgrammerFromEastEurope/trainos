from .workflow_snapshot import WorkflowSnapshot


class SnapshotEngine:

    def capture(
        self,
        snapshot: WorkflowSnapshot,
    ) -> WorkflowSnapshot:
        return snapshot

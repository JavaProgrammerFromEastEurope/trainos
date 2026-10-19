from kernel.persistence.snapshot.persistence_snapshot import PersistenceSnapshot

from kernel.persistence.snapshot.persistence_snapshot_engine import (
    PersistenceSnapshotEngine,
)

from kernel.persistence.snapshot.storage_snapshot 	import StorageSnapshot
from kernel.persistence.snapshot.repository_snapshot import RepositorySnapshot
from kernel.persistence.snapshot.transaction_snapshot import TransactionSnapshot
from kernel.persistence.storage.storage_status 			import StorageStatus


def test_persistence_snapshot():

    snapshot = PersistenceSnapshot(
        snapshot_id="SNAP1",
        storage=StorageSnapshot(
            storage_id="ST1",
            status=StorageStatus.RUNNING,
        ),
        repositories=RepositorySnapshot(
            repository_count=5,
        ),
        transactions=TransactionSnapshot(
            active_transactions=2,
        ),
    )

    result = PersistenceSnapshotEngine().capture(snapshot)
    assert result.snapshot_id == "SNAP1"
    assert result.storage.status == StorageStatus.RUNNING
    assert result.repositories.repository_count == 5

from dataclasses import dataclass

from .storage_snapshot import StorageSnapshot
from .repository_snapshot import RepositorySnapshot
from .transaction_snapshot import TransactionSnapshot


@dataclass(frozen=True, slots=True)
class PersistenceSnapshot:

    snapshot_id: str
    storage: StorageSnapshot
    repositories: RepositorySnapshot
    transactions: TransactionSnapshot
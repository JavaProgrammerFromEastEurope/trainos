from dataclasses import dataclass


@dataclass(frozen=True)
class HistorySnapshot:

    snapshot_id: 	str
    timestamp: 		str
    state_hash: 	str
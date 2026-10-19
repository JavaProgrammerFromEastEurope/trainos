from dataclasses import dataclass


@dataclass(frozen=True)
class SnapshotPolicy:

    immutable_snapshots: 	bool
    auto_capture: 				bool
    capture_interval: 		int
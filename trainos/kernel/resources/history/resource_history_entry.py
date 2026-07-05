from dataclasses import dataclass

from .resource_snapshot import ResourceSnapshot


@dataclass(frozen=True, slots=True)
class ResourceHistoryEntry:

    entry_id: 	str
    timestamp: 	str
    snapshot: ResourceSnapshot
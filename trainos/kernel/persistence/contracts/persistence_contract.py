from dataclasses import dataclass

from .persistence_type import PersistenceType


@dataclass(frozen=True, slots=True)
class PersistenceContract:

    object_id: 	str
    persistence_type: PersistenceType
    version: 		int = 1
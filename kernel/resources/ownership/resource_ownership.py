from dataclasses import dataclass

from .ownership_type import OwnershipType


@dataclass(frozen=True)
class ResourceOwnership:

    ownership_id: 	str
    resource_id: 		str
    owner_id: 			str
    owner_type: OwnershipType
    quantity: float
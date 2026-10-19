from dataclasses import dataclass

from .resource_type import ResourceType


@dataclass
class ResourceStack:

    type: ResourceType
    quantity: float

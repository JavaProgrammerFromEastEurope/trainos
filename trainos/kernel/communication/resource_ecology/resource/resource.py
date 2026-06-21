from dataclasses import dataclass

from .resource_type import ResourceType


@dataclass
class Resource:

    type: ResourceType
    amount: float

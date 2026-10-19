from dataclasses import dataclass

from ..resource.resource_type import ResourceType


@dataclass
class ConsumptionRequest:

    resource: ResourceType
    amount: 	float

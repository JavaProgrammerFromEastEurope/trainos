from dataclasses import dataclass

from .resource_type import ResourceType
from .resource_unit import ResourceUnit
from .resource_category import ResourceCategory


@dataclass(frozen=True)
class ResourceDefinition:

    resource_id: 	str
    name: 				str
    resource_type: ResourceType
    category: 	ResourceCategory
    base_unit: 	ResourceUnit
    is_renewable: bool
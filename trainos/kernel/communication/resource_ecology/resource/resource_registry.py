from __future__ import annotations

from .resource_stack 	import ResourceStack
from .resource_type 	import ResourceType


class ResourceRegistry:

    def __init__(self) -> None:
        self._resources: dict[ResourceType, ResourceStack] = {}

    def register(self, stack: ResourceStack) -> None:
        self._resources[stack.type] = stack

    def get(self, resource_type: ResourceType) -> ResourceStack | None:
        return self._resources.get(resource_type)

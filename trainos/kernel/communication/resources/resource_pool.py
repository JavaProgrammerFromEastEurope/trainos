from __future__ import annotations

from .resource import Resource


class ResourcePool:

    def __init__(self) -> None:
        self._resources: list[Resource] = []

    def add(self, resource: Resource) -> None:
        self._resources.append(resource)

    def resources(self) -> tuple[Resource, ...]:
        return tuple(self._resources)

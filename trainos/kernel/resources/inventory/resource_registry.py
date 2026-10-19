from __future__ import annotations

from typing import Generic, TypeVar


from .resource_record import ResourceRecord

T = TypeVar("T")


class ResourceRegistry(Generic[T]):

    def __init__(self) -> None:
        self._resources: dict[str, ResourceRecord] = {}

    def register(self, record: ResourceRecord) -> None:
        self._resources[record.resource_id] = record

    def get(self, resource_id: str) -> ResourceRecord:
        return self._resources[resource_id]

    def all(self) -> tuple[ResourceRecord, ...]:
        return tuple(self._resources.values())

    def exists(self, resource_id: str) -> bool:
        return resource_id in self._resources

from __future__ import annotations

from typing import Generic, TypeVar

from .resource_ownership import ResourceOwnership

T = TypeVar("T")


class OwnershipRegistry(Generic[T]):

    def __init__(self) -> None:
        self._ownerships: dict[str, ResourceOwnership] = {}

    def register(self, ownership: ResourceOwnership) -> None:
        self._ownerships[ownership.ownership_id] = ownership

    def get(self, ownership_id: str) -> ResourceOwnership:
        return self._ownerships[ownership_id]

    def by_owner(self, owner_id: str):
        return tuple(o for o in self._ownerships.values() if o.owner_id == owner_id)

    def all(self) -> tuple[ResourceOwnership, ...]:
        return tuple(self._ownerships.values())

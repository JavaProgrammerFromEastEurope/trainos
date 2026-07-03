from __future__ import annotations

from typing import Generic, TypeVar

from .registry_error import EntityNotFoundError, EntityAlreadyExistsError
from .registry_policy import RegistryPolicy

T = TypeVar("T")


class BaseRegistry(Generic[T]):

    def __init__(
        self,
        policy: RegistryPolicy | None = None,
    ) -> None:
        self._store: dict[str, T] = {}
        self._policy = policy or RegistryPolicy(
            allow_overwrite=False, immutable_keys=True
        )

    def register(self, entity_id: str, entity: T) -> None:
        if not self._policy.allow_overwrite and entity_id in self._store:
            raise EntityAlreadyExistsError(f"Entity {entity_id} already exists")
        self._store[entity_id] = entity

    def get(self, entity_id: str) -> T:
        if entity_id not in self._store:
            raise EntityNotFoundError(f"Entity {entity_id} not found")
        return self._store[entity_id]

    def delete(self, entity_id: str) -> None:
        if entity_id not in self._store:
            raise EntityNotFoundError(f"Entity {entity_id} not found")
        del self._store[entity_id]

    def all(self) -> tuple[T, ...]:
        return tuple(self._store.values())

    def exists(self, entity_id: str) -> bool:
        return entity_id in self._store

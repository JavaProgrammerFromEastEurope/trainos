from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")


class BaseRegistry(Generic[T]):

    def __init__(self) -> None:
        self._items: dict[str, T] = {}

    def register(self, id: str, item: T) -> None:
        self._items[id] = item

    def get(self, id: str) -> T | None:
        return self._items.get(id)

    def exists(self, id: str) -> bool:
        return id in self._items

    def all(self) -> tuple[T, ...]:
        return tuple(self._items.values())

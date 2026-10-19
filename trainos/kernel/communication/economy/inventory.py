from __future__ import annotations

from .resource_item import (
    ResourceItem,
)


class Inventory:

    def __init__(self) -> None:
        self._items: list[ResourceItem] = []

    def add(self, item: ResourceItem) -> None:
        self._items.append(item)

    def items(self) -> tuple[ResourceItem, ...]:
        return tuple(self._items)

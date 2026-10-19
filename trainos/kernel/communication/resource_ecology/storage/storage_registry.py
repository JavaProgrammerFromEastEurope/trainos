from __future__ import annotations

from .storage_unit import StorageUnit


class StorageRegistry:

    def __init__(self) -> None:
        self._units: list[StorageUnit] = []

    def add(self, unit: StorageUnit) -> None:
        self._units.append(unit)

    def units(self) -> tuple[StorageUnit, ...]:
        return tuple(self._units)

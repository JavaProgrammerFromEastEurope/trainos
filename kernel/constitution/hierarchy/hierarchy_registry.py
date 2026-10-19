from __future__ import annotations

from .constitutional_hierarchy import ConstitutionalHierarchy


class HierarchyRegistry:

    def __init__(self) -> None:
        self._entries: list[ConstitutionalHierarchy] = []

    def register(self, hierarchy: ConstitutionalHierarchy) -> None:
        self._entries.append(hierarchy)

    def entries(self) -> tuple[ConstitutionalHierarchy, ...]:
        return tuple(self._entries)

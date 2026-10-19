from __future__ import annotations

from .civil_group import CivilGroup
from .group_membership import GroupMembership


class GroupRegistry:

    def __init__(self) -> None:

        self._groups: 			dict[str, CivilGroup] = {}
        self._memberships: 	list[GroupMembership] = []

    def register_group(self, group: CivilGroup) -> None:
        self._groups[group.group_id] = group

    def register_membership(
        self,
        membership: GroupMembership,
    ) -> None:
        self._memberships.append(membership)

    def group(self, group_id: str) -> CivilGroup | None:
        return self._groups.get(group_id)

    def memberships(self) -> tuple[GroupMembership, ...]:
        return tuple(self._memberships)

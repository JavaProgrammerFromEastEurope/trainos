from __future__ import annotations

from .crew_member import CrewMember


class CrewRegistry:

    def __init__(self) -> None:
        self._crew: list[CrewMember] = []

    def add(self, member: CrewMember) -> None:
        self._crew.append(member)

    def members(self) -> tuple[CrewMember, ...]:
        return tuple(self._crew)

from __future__ import annotations

from .role_assignment import RoleAssignment


class RoleManager:

    def __init__(self) -> None:
        self._roles: list[RoleAssignment] = []

    def assign(self, role: RoleAssignment) -> None:
        self._roles.append(role)

    def roles(self) -> tuple[RoleAssignment, ...]:
        return tuple(self._roles)

from __future__ import annotations

from .department import Department


class DepartmentRegistry:

    def __init__(self) -> None:
        self._departments: list[Department] = []

    def add(self, department: Department) -> None:
        self._departments.append(department)

    def departments(self) -> tuple[Department, ...]:
        return tuple(self._departments)

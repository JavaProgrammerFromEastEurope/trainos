from __future__ import annotations

from .constraint import Constraint


class ConstraintRegistry:

    def __init__(self) -> None:
        self._constraints: list[Constraint] = []

    def register(self, constraint: Constraint) -> None:
        self._constraints.append(constraint)

    def constraints(self) -> tuple[Constraint, ...]:
        return tuple(self._constraints)

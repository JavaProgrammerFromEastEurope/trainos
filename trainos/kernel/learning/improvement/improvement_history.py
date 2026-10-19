from __future__ import annotations

from .improvement_target import ImprovementTarget


class ImprovementHistory:

    def __init__(
        self,
    ) -> None:
        self._targets: list[ImprovementTarget] = []

    def add(
        self,
        target: ImprovementTarget,
    ) -> None:
        self._targets.append(target)

    def targets(
        self,
    ) -> tuple[ImprovementTarget, ...]:
        return tuple(self._targets)

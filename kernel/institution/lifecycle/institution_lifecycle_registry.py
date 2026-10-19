from __future__ import annotations

from .institution_lifecycle import InstitutionLifecycle


class InstitutionLifecycleRegistry:

    def __init__(self) -> None:
        self._lifecycles: dict[str, InstitutionLifecycle] = {}

    def register(self, lifecycle: InstitutionLifecycle) -> None:
        self._lifecycles[lifecycle.institution_id] = lifecycle

    def get(self, institution_id: str) -> InstitutionLifecycle | None:
        return self._lifecycles.get(institution_id)

    def lifecycles(self) -> tuple[InstitutionLifecycle, ...]:
        return tuple(self._lifecycles.values())

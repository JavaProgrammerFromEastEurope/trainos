from __future__ import annotations

from ..improvement.improvement_target import ImprovementTarget


class ImprovementEngine:
    """Selects the default improvement target for self-evaluation."""

    def target(self) -> ImprovementTarget:
        return ImprovementTarget(name="navigation")

from __future__ import annotations

from .goal import Goal


class GoalSelector:

    def select(
        self,
        goals: list[Goal],
    ) -> Goal | None:
        if not goals:
            return None
        return max(
            goals,
            key=lambda g: g.priority,
        )

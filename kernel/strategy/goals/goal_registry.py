from __future__ import annotations

from .goal import Goal


class GoalRegistry:

    def __init__(self) -> None:
        self._goals: list[Goal] = []

    def register(self, goal: Goal) -> None:
        self._goals.append(goal)

    def goals(self) -> tuple[Goal, ...]:
        return tuple(self._goals)

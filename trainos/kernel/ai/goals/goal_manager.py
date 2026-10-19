from __future__ import annotations

from typing import Dict
from .goal import Goal


class GoalManager:

    def __init__(self) -> None:
        self._goals: Dict[
            str,
            Goal,
        ] = {}

    def add(
        self,
        goal: Goal,
    ) -> None:
        self._goals[goal.id] = goal

    def remove(
        self,
        goal_id: str,
    ) -> None:
        self._goals.pop(
            goal_id,
            None,
        )

    def get(
        self,
        goal_id: str,
    ) -> Goal | None:
        return self._goals.get(goal_id)

    def all_goals(
        self,
    ) -> list[Goal]:
        return list(self._goals.values())

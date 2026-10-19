from __future__ import annotations

from .reward import Reward


class RewardHistory:

    def __init__(
        self,
    ) -> None:
        self._history: list[Reward] = []

    def add(
        self,
        reward: Reward,
    ) -> None:
        self._history.append(reward)

    def rewards(
        self,
    ) -> tuple[Reward, ...]:
        return tuple(self._history)

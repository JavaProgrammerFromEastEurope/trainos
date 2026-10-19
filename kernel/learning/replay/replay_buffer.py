from __future__ import annotations

from collections import deque

from ..experience.experience import (
    Experience,
)


class ReplayBuffer:

    def __init__(
        self,
        capacity: int = 1000,
    ) -> None:
        self._buffer = deque(
            maxlen=capacity,
        )

    def add(
        self,
        exp: Experience,
    ) -> None:
        self._buffer.append(exp)

    def sample(
        self,
        size: int,
    ) -> list[Experience]:
        return list(self._buffer)[:size]

    def size(self) -> int:
        return len(self._buffer)

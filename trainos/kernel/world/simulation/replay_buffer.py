from __future__ import annotations

from .replay_frame import (
    ReplayFrame,
)


class ReplayBuffer:

    def __init__(
        self,
    ) -> None:
        self._frames: list[ReplayFrame] = []

    def add(
        self,
        frame: ReplayFrame,
    ) -> None:
        self._frames.append(
            frame,
        )

    def frames(
        self,
    ) -> tuple[ReplayFrame, ...]:
        return tuple(
            self._frames,
        )

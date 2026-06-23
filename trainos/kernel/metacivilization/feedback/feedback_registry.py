from __future__ import annotations

from .feedback_loop import FeedbackLoop


class FeedbackRegistry:

    def __init__(self) -> None:
        self._loops: list[FeedbackLoop] = []

    def add(self, loop: FeedbackLoop) -> None:
        self._loops.append(loop)

    def loops(self) -> tuple[FeedbackLoop, ...]:
        return tuple(self._loops)

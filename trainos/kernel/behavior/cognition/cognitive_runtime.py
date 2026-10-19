from __future__ import annotations

from .cognitive_state import (
    CognitiveState,
)


class CognitiveRuntime:

    def __init__(
        self,
    ) -> None:
        self._state = CognitiveState.IDLE

    @property
    def state(
        self,
    ) -> CognitiveState:
        return self._state

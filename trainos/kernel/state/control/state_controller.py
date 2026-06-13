from __future__ import annotations

from trainos.kernel.state.state_service import StateService


class StateController:

    def __init__(
        self,
        state_service: StateService,
    ) -> None:
        self._state = state_service
        self._paused: bool = False

    def pause(self) -> None:
        self._paused = True

    def resume(self) -> None:
        self._paused = False

    def is_paused(self) -> bool:
        return self._paused

    def reset(self) -> None:
        self._state.clear()

    def dump(self) -> dict:
        return self._state.snapshot().data

    def replace(self, data: dict) -> None:
        self._state.clear()
        for key, value in data.items():
            self._state.set(key, value)

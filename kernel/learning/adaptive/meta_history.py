from __future__ import annotations

from .adaptation_parameter import AdaptationParameter


class MetaHistory:

    def __init__(
        self,
    ) -> None:
        self._history: list[AdaptationParameter] = []

    def add(
        self,
        parameter: AdaptationParameter,
    ) -> None:
        self._history.append(parameter)

    def parameters(
        self,
    ) -> tuple[AdaptationParameter, ...]:
        return tuple(self._history)

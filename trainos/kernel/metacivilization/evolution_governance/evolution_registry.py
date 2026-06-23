from __future__ import annotations

from .evolution_request import EvolutionRequest


class EvolutionRegistry:

    def __init__(self) -> None:
        self._requests: list[EvolutionRequest] = []

    def register(self, request: EvolutionRequest) -> None:
        self._requests.append(request)

    def requests(self) -> tuple[EvolutionRequest, ...]:
        return tuple(self._requests)

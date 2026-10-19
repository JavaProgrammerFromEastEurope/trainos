from __future__ import annotations

from .adaptive_strategy import AdaptiveStrategy


class AdaptationRegistry:

    def __init__(self) -> None:
        self._strategies: list[AdaptiveStrategy] = []

    def register(self, strategy: AdaptiveStrategy) -> None:
        self._strategies.append(strategy)

    def strategies(self) -> tuple[AdaptiveStrategy, ...]:
        return tuple(self._strategies)

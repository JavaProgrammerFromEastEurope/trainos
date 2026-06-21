from __future__ import annotations

from .market import (
    Market,
)


class MarketRegistry:

    def __init__(self) -> None:
        self._markets: list[Market] = []

    def add(self, market: Market) -> None:
        self._markets.append(market)

    def markets(self) -> tuple[Market, ...]:
        return tuple(self._markets)

from __future__ import annotations

from .price import Price


class PricingRegistry:

    def __init__(self) -> None:
        self._prices: dict[str, Price] = {}

    def register(self, price: Price) -> None:
        self._prices[price.price_id] = price

    def get(self, price_id: str) -> Price | None:
        return self._prices.get(price_id)

    def all(self) -> tuple[Price, ...]:
        return tuple(self._prices.values())

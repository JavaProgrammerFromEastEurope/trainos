from __future__ import annotations

from .currency_definition import CurrencyDefinition


class CurrencyRegistry:

    def __init__(self) -> None:
        self._currencies: dict[str, CurrencyDefinition] = {}

    def register(self, currency: CurrencyDefinition) -> None:
        self._currencies[currency.currency_id] = currency

    def get(self, currency_id: str) -> CurrencyDefinition | None:
        return self._currencies.get(currency_id)

    def all(self) -> tuple[CurrencyDefinition, ...]:
        return tuple(self._currencies.values())

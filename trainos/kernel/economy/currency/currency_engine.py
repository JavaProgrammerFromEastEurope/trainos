from .currency_definition import CurrencyDefinition


class CurrencyEngine:

    def validate(
        self,
        currency: CurrencyDefinition,
    ) -> CurrencyDefinition:
        return currency

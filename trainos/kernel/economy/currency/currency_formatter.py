from .currency_definition import CurrencyDefinition


class CurrencyFormatter:

    def format(
        self,
        amount: float,
        currency: CurrencyDefinition,
    ) -> str:
        return (
            f"{currency.symbol}"
            f"{amount:.{currency.fractional_digits}f}"
        )
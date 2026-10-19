from kernel.economy.currency.currency_definition import CurrencyDefinition
from kernel.economy.currency.currency_registry import CurrencyRegistry


def test_currency_registry():

    registry = CurrencyRegistry()

    currency = CurrencyDefinition(
        currency_id="currency-trc",
        code="TRC",
        name="Train Credit",
        symbol="₸",
        fractional_digits=2,
    )

    registry.register(currency)

    loaded = registry.get("currency-trc")

    assert loaded == currency

    assert loaded.currency_id == "currency-trc"
    assert loaded.code == "TRC"
    assert loaded.name == "Train Credit"
    assert loaded.symbol == "₸"
    assert loaded.fractional_digits == 2
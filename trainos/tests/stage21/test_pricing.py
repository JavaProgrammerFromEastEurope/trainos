from decimal import Decimal

from kernel.economy.pricing.price import Price
from kernel.economy.pricing.pricing_engine import PricingEngine


def test_pricing():

    price = Price(
        price_id="PRICE-1",
        subject_id="WATER",
        currency_id="TRC",
        amount=Decimal("3.5"),
    )

    engine = PricingEngine()
    result = engine.evaluate(price)

    assert result.amount == Decimal("3.5")
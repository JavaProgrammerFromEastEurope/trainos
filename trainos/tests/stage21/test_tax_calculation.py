from decimal import Decimal

from kernel.economy.taxation.tax_definition import TaxDefinition
from kernel.economy.taxation.tax_engine import TaxEngine


def test_tax_calculation():

    definition = TaxDefinition(
        tax_id="income",
        name="Income",
        rate=Decimal("0.10"),
    )

    engine = TaxEngine()

    assessment = engine.calculate(
        account_id="ACC-1",
        taxable_amount=Decimal("1000"),
        definition=definition,
    )

    assert assessment.tax_amount == Decimal("100.00")

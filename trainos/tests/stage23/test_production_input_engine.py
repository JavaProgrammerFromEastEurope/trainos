from decimal import Decimal

from trainos.kernel.production.inputs.production_input_check 	import ProductionInputCheck
from trainos.kernel.production.inputs.production_input_engine 	import ProductionInputEngine


def test_production_input_engine():

    engine = ProductionInputEngine()

    checks = (
        ProductionInputCheck(
            resource_id="water",
            available_quantity=Decimal("100"),
            required_quantity=Decimal("50"),
        ),
        ProductionInputCheck(
            resource_id="electricity",
            available_quantity=Decimal("20"),
            required_quantity=Decimal("10"),
        ),
    )

    result = engine.validate(checks)

    assert result.approved is True
    assert result.missing_resources == ()
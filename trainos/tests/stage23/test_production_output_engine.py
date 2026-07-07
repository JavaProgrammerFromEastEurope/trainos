from decimal import Decimal

from kernel.production.outputs.production_output import ProductionOutput
from kernel.production.outputs.production_output_engine import ProductionOutputEngine


def test_production_output_engine():

    engine = ProductionOutputEngine()

    outputs = (
        ProductionOutput(
            resource_id="clean_water",
            produced_quantity=Decimal("10"),
        ),
    )

    result = engine.produce(outputs)

    assert result.completed is True
    assert result.outputs == outputs
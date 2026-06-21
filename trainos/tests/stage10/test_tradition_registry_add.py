from trainos.kernel.civilization.tradition.tradition import Tradition
from trainos.kernel.civilization.tradition.tradition_registry import TraditionRegistry
from trainos.kernel.civilization.tradition.tradition_type import TraditionType


def test_tradition_registry_add():

    registry = TraditionRegistry()

    tradition = Tradition(
        type=TraditionType.FOOD_RESERVE,
    )

    registry.add(tradition)

    assert tradition in registry.traditions()
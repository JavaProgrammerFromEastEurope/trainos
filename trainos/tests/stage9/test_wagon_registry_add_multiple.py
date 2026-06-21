from trainos.kernel.communication.infrastructure.wagon.wagon import Wagon
from trainos.kernel.communication.infrastructure.wagon.wagon_registry import (
    WagonRegistry,
)
from trainos.kernel.communication.infrastructure.wagon.wagon_status import WagonStatus
from trainos.kernel.communication.infrastructure.wagon.wagon_type import WagonType


def test_wagon_registry_add_multiple():

    registry = WagonRegistry()

    wagon_1 = Wagon(
        name="hydroponics", type=WagonType.HYDROPONICS, status=WagonStatus.ACTIVE
    )

    wagon_2 = Wagon(name="storage", type=WagonType.STORAGE, status=WagonStatus.ACTIVE)

    registry.add(wagon_1)
    registry.add(wagon_2)

    assert registry.wagons() == (wagon_1, wagon_2)

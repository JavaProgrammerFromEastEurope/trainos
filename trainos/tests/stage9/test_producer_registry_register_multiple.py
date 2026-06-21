from trainos.kernel.communication.resource_ecology.producers.hydroponics_producer import (
    HydroponicsProducer,
)
from trainos.kernel.communication.resource_ecology.producers.producer_registry import (
    ProducerRegistry,
)
from trainos.kernel.communication.resource_ecology.producers.solar_generator import (
    SolarGenerator,
)


def test_producer_registry_register_multiple():

    registry = ProducerRegistry()

    producer_1 = HydroponicsProducer()
    producer_2 = SolarGenerator()

    registry.register(producer_1)
    registry.register(producer_2)

    assert registry.producers() == (producer_1, producer_2)

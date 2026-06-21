from trainos.kernel.communication.resource_ecology.consumers.consumer_registry import (
    ConsumerRegistry,
)
from trainos.kernel.communication.resource_ecology.consumers.engine_consumer import (
    EngineConsumer,
)
from trainos.kernel.communication.resource_ecology.consumers.population_consumer import (
    PopulationConsumer,
)


def test_consumer_registry_register_multiple():

    registry = ConsumerRegistry()

    consumer_1 = PopulationConsumer()
    consumer_2 = EngineConsumer()

    registry.register(consumer_1)
    registry.register(consumer_2)

    assert registry.consumers() == (consumer_1, consumer_2)

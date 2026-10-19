from kernel.production.factories.factory import Factory
from kernel.production.factories.factory_engine import FactoryEngine
from kernel.production.factories.factory_status import FactoryStatus
from kernel.production.factories.factory_type import FactoryType


def test_factory_engine():

    engine = FactoryEngine()

    factory = Factory(
        factory_id="factory1",
        name="Water Plant",
        factory_type=FactoryType.WATER_PLANT,
        status=FactoryStatus.IDLE,
    )

    started = engine.start(factory)
    assert started.status == FactoryStatus.ACTIVE

    stopped = engine.stop(started)
    assert stopped.status == FactoryStatus.OFFLINE
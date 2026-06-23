from trainos.kernel.metacivilization.meta_ethics.meta_ethics import MetaEthics
from trainos.kernel.metacivilization.meta_ethics.meta_ethics_type import MetaEthicsType
from trainos.kernel.metacivilization.meta_ethics.meta_ethics_registry import MetaEthicsRegistry


def test_meta_ethics_registry_add():

    registry = MetaEthicsRegistry()

    ethics = MetaEthics(type=MetaEthicsType.ADAPTIVE)

    registry.add(ethics)

    assert registry.ethics() == (ethics,)
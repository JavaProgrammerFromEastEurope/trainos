from trainos.kernel.civilization.myth.myth import Myth
from trainos.kernel.civilization.myth.myth_registry import MythRegistry
from trainos.kernel.civilization.myth.myth_type import MythType


def test_myth_registry_add():

    registry = MythRegistry()
    myth = Myth(type=MythType.SURVIVAL)
    registry.add(myth)

    assert myth in registry.myths()

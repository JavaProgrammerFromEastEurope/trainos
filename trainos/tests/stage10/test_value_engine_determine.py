from trainos.kernel.civilization.value.value_engine import ValueEngine
from trainos.kernel.civilization.value.value_type import ValueType


def test_value_engine_determine():

    engine = ValueEngine()
    value = engine.determine()

    assert value.type == ValueType.SURVIVAL
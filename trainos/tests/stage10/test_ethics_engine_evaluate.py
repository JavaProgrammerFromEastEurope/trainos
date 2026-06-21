from trainos.kernel.civilization.ethics.ethics_engine import EthicsEngine
from trainos.kernel.civilization.ethics.ethics_type import EthicsType


def test_ethics_engine_evaluate():

    engine = EthicsEngine()
    ethics = engine.evaluate()

    assert ethics.type == EthicsType.COOPERATIVE
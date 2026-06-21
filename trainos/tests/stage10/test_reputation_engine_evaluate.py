from trainos.kernel.civilization.reputation.reputation_engine import ReputationEngine
from trainos.kernel.civilization.reputation.reputation_score import ReputationScore


def test_reputation_engine_evaluate():

    engine = ReputationEngine()
    reputation = engine.evaluate()

    assert reputation.score == ReputationScore.NORMAL

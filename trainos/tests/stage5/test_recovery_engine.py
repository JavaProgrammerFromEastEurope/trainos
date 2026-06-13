from trainos.kernel.ai.recovery.recovery_engine import RecoveryEngine
from trainos.kernel.ai.recovery.recovery_policy import RecoveryPolicy
from trainos.kernel.ai.recovery.retry_state import RetryState


def test_recovery_engine():
    engine = RecoveryEngine()
    result = engine.recover(RetryState(), RecoveryPolicy(), [])
    assert result.recovered is True

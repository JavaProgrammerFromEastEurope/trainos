from trainos.kernel.constitution.rollback.constitutional_rollback import ConstitutionalRollback
from trainos.kernel.constitution.rollback.rollback_result import RollbackResult


def test_constitutional_rollback():

    rollback = ConstitutionalRollback(
        from_version="2.1",
        target_version="2.0",
        result=RollbackResult.SUCCESS,
    )

    assert rollback.result == RollbackResult.SUCCESS
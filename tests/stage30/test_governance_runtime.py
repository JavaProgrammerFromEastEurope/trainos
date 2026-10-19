from kernel.governance.runtime.governance_runtime import (
    GovernanceRuntime,
)


def test_governance_runtime():

    runtime = GovernanceRuntime()
    runtime.initialize()
    runtime.update()
    runtime.shutdown()

    assert runtime.context is not None
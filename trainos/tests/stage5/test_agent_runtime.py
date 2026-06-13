from trainos.kernel.ai.runtime.autonomous_runtime import (
    AutonomousRuntime,
)

from trainos.kernel.ai.runtime.agent_loop import (
    AgentLoop,
)


def test_agent_runtime():
    runtime = AutonomousRuntime()
    runtime.start()
    loop = AgentLoop(runtime)
    loop.tick()
    cycle = runtime.next_cycle()
    assert cycle.cycle_id == 2

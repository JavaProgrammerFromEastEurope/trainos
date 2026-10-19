from kernel.simulation.runtime.simulation_runtime import SimulationRuntime
from kernel.simulation.runtime.runtime_engine import RuntimeEngine
from kernel.simulation.runtime.runtime_status import RuntimeStatus


def test_simulation_runtime():

    engine = RuntimeEngine()
    runtime = SimulationRuntime(
        runtime_id="RUNTIME1",
        status=RuntimeStatus.CREATED,
    )

    running = engine.start(runtime)
    assert running.status == RuntimeStatus.RUNNING

    paused = engine.pause(running)
    assert paused.status == RuntimeStatus.PAUSED

    stopped = engine.stop(paused)
    assert stopped.status == RuntimeStatus.STOPPED

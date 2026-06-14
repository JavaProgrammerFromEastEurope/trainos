from trainos.kernel.world.runtime.world_runtime import (
    WorldRuntime,
)

from trainos.kernel.world.runtime.world_state import (
    WorldState,
)


def test_world_runtime():

    runtime = WorldRuntime()

    assert runtime.state == WorldState.STOPPED

    runtime.start()

    assert runtime.state == WorldState.RUNNING

    cycle = runtime.next_cycle()

    assert cycle.cycle_id == 1

    runtime.pause()

    assert runtime.state == WorldState.PAUSED

    runtime.stop()

    assert runtime.state == WorldState.STOPPED

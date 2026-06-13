from trainos.kernel.state.state_service import StateService


def test_metrics():

    state = StateService()
    state.initialize()
    state.start()

    state.set("a", 1)
    state.set("b", 2)

    state.update(0.1)

    metrics = state.metrics

    assert metrics.key_count == 2
    assert metrics.tick_count == 1

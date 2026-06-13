from trainos.kernel.state.state_service import StateService


def test_observers():

    state = StateService()
    state.initialize()
    state.start()
    result = []

    def callback(key, old, new):
        result.append((key, old, new))

    state.watch("hp", callback)
    state.set("hp", 100)
    state.set("hp", 50)

    assert len(result) == 2
    assert result[0] == ("hp", None, 100)

from trainos.kernel.state.state_service import StateService


def test_export_import():

    state = StateService()
    state.initialize()
    state.start()
    state.set("a", 1)

    exported = state.exporter().export(state.snapshot().data)
    imported = state.importer().import_state(exported)

    assert imported["a"] == 1

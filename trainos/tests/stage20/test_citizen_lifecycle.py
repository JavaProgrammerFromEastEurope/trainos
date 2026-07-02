from kernel.society.lifecycle.citizen_lifecycle import CitizenLifecycle
from kernel.society.lifecycle.citizen_state import CitizenState


def test_create_citizen_lifecycle():

    lifecycle = CitizenLifecycle(
        entity_id="A-104",
        state=CitizenState.ACTIVE,
    )

    assert lifecycle.entity_id == "A-104"
    assert lifecycle.state is CitizenState.ACTIVE
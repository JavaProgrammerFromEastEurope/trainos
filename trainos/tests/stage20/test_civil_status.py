from kernel.society.status.civil_status import CivilStatus
from kernel.society.status.status_definition import StatusDefinition


def test_assign_status():

    definition = StatusDefinition(
        status_id="volunteer",
        name="Volunteer",
        description="Emergency volunteer",
    )

    status = CivilStatus(
        entity_id="A-104",
        status_id=definition.status_id,
    )

    assert status.status_id == "volunteer"
    assert definition.name == "Volunteer"

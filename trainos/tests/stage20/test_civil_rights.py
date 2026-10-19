from kernel.society.rights.civil_right import CivilRight
from kernel.society.rights.civil_right_set import CivilRightSet


def test_create_right_set():

    rights = CivilRightSet(
        entity_id="A-104",
        rights=(
            CivilRight.VOTE,
            CivilRight.OWN_PROPERTY,
        ),
    )

    assert len(rights.rights) == 2
    assert CivilRight.VOTE in rights.rights
from kernel.society.citizenship.citizenship 				import Citizenship
from kernel.society.citizenship.citizenship_status 	import CitizenshipStatus


def test_create_citizenship():

    citizenship = Citizenship(
        entity_id="A-104",
        status=CitizenshipStatus.GRANTED,
    )

    assert citizenship.entity_id == "A-104"
    assert citizenship.status is CitizenshipStatus.GRANTED
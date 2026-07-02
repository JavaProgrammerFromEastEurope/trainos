from kernel.institution.institution import Institution
from kernel.institution.institution_type import InstitutionType


def test_create_institution():

    institution = Institution(
        institution_id="CC-001",
        name="Constitutional Council",
        institution_type=InstitutionType.COUNCIL,
    )

    assert institution.institution_id == "CC-001"
    assert institution.name == "Constitutional Council"
    assert institution.institution_type is InstitutionType.COUNCIL

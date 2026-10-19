from kernel.institution.institution import Institution
from kernel.institution.institution_registry import InstitutionRegistry
from kernel.institution.institution_type import InstitutionType


def test_registry_register_and_lookup():

    registry = InstitutionRegistry()

    institution = Institution(
        institution_id="EO-001",
        name="Executive Office",
        institution_type=InstitutionType.OFFICE,
    )

    registry.register(institution)

    assert registry.exists("EO-001")
    assert registry.get("EO-001") == institution
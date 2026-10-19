from kernel.institution.jurisdiction.institutional_jurisdiction import InstitutionalJurisdiction
from kernel.institution.jurisdiction.jurisdiction_domain import JurisdictionDomain
from kernel.institution.jurisdiction.jurisdiction_registry import JurisdictionRegistry


def test_register_jurisdiction():

    registry = JurisdictionRegistry()

    jurisdiction = InstitutionalJurisdiction(
        institution_id="MA-001",
        domain=JurisdictionDomain.MEDICINE,
    )

    registry.register(jurisdiction)
    items = registry.get("MA-001")

    assert len(items) == 1
    assert items[0] == jurisdiction
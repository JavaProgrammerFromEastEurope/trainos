from trainos.kernel.communication.governance.institution.institution import Institution
from trainos.kernel.communication.governance.institution.institution_registry import InstitutionRegistry
from trainos.kernel.communication.governance.institution.institution_type import InstitutionType


def test_institution_registry_add_multiple():

    registry = InstitutionRegistry()

    inst_1 = Institution(type=InstitutionType.ENGINEERING)
    inst_2 = Institution(type=InstitutionType.AGRICULTURE)

    registry.add(inst_1)
    registry.add(inst_2)

    assert registry.institutions() == (
        inst_1,
        inst_2,
    )
from kernel.population.employment.employment import Employment
from kernel.population.employment.employment_engine import EmploymentEngine
from kernel.population.employment.employment_status import EmploymentStatus
from kernel.population.employment.employment_type import EmploymentType


def test_employment_engine():

    engine = EmploymentEngine()
    employment = Employment(
        employment_id="EMP1",
        resident_id="R1",
        profession_id="ENG",
        organization_id="ORG1",
        employment_type=EmploymentType.FULL_TIME,
        status=EmploymentStatus.SUSPENDED,
    )

    active = engine.activate(employment)
    assert active.status == EmploymentStatus.ACTIVE
    terminated = engine.terminate(active)
    assert terminated.status == EmploymentStatus.TERMINATED
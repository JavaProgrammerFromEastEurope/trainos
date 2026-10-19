from kernel.population.employment.employment_status import EmploymentStatus
from kernel.population.households.household_status import HouseholdStatus
from kernel.population.professions.profession_type import ProfessionType
from kernel.population.residents.resident_status import ResidentStatus
from kernel.population.runtime.population_lifecycle import PopulationLifecycle
from kernel.population.snapshot.employment_snapshot import EmploymentSnapshot
from kernel.population.snapshot.household_snapshot import HouseholdSnapshot
from kernel.population.snapshot.population_runtime_snapshot import PopulationRuntimeSnapshot
from kernel.population.snapshot.population_snapshot import PopulationSnapshot
from kernel.population.snapshot.population_snapshot_engine import PopulationSnapshotEngine
from kernel.population.snapshot.profession_snapshot import ProfessionSnapshot
from kernel.population.snapshot.resident_snapshot import ResidentSnapshot


def test_population_snapshot():

    engine = PopulationSnapshotEngine()
    snapshot = PopulationSnapshot(
        snapshot_id="SNAP1",
        runtime=PopulationRuntimeSnapshot(
            lifecycle=PopulationLifecycle.RUNNING,
        ),
        residents=(
            ResidentSnapshot(
                resident_id="R1",
                status=ResidentStatus.ACTIVE,
            ),
        ),
        households=(
            HouseholdSnapshot(
                household_id="H1",
                status=HouseholdStatus.ACTIVE,
            ),
        ),
        professions=(
            ProfessionSnapshot(
                profession_id="ENG",
                profession_type=ProfessionType.ENGINEER,
            ),
        ),
        employments=(
            EmploymentSnapshot(
                employment_id="EMP1",
                status=EmploymentStatus.ACTIVE,
            ),
        ),
    )

    result = engine.capture(snapshot)
    assert result is snapshot
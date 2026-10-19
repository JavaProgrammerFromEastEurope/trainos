from kernel.population.residents.resident import Resident
from kernel.population.residents.resident_engine import ResidentEngine
from kernel.population.residents.resident_status import ResidentStatus
from kernel.population.residents.resident_type import ResidentType


def test_resident_engine():

    engine = ResidentEngine()

    resident = Resident(
        resident_id="R1",
        name="John",
        resident_type=ResidentType.HUMAN,
        status=ResidentStatus.SLEEPING,
    )

    active = engine.activate(resident)
    assert active.status == ResidentStatus.ACTIVE

    retired = engine.retire(active)
    assert retired.status == ResidentStatus.RETIRED
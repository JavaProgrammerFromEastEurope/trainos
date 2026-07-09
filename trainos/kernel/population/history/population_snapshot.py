from dataclasses import dataclass

from kernel.population.residents.resident_status import ResidentStatus


@dataclass(frozen=True, slots=True)
class PopulationSnapshot:

    snapshot_id: str
    resident_id: str
    status: ResidentStatus
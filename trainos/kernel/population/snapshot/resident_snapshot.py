from dataclasses import dataclass

from kernel.population.residents.resident_status import ResidentStatus


@dataclass(frozen=True, slots=True)
class ResidentSnapshot:

    resident_id: str
    status: ResidentStatus
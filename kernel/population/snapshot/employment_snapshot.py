from dataclasses import dataclass

from kernel.population.employment.employment_status import EmploymentStatus


@dataclass(frozen=True, slots=True)
class EmploymentSnapshot:

    employment_id: str
    status: EmploymentStatus
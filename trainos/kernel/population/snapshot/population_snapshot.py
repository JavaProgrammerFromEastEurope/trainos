from dataclasses import dataclass

from .employment_snapshot import EmploymentSnapshot
from .household_snapshot import HouseholdSnapshot
from .population_runtime_snapshot import PopulationRuntimeSnapshot
from .profession_snapshot import ProfessionSnapshot
from .resident_snapshot import ResidentSnapshot


@dataclass(frozen=True, slots=True)
class PopulationSnapshot:

    snapshot_id: 	str
    runtime: 			PopulationRuntimeSnapshot
    residents: 		tuple[ResidentSnapshot, ...]
    households: 	tuple[HouseholdSnapshot, ...]
    professions: 	tuple[ProfessionSnapshot, ...]
    employments: 	tuple[EmploymentSnapshot, ...]
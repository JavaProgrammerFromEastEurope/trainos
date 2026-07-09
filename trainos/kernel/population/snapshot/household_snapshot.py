from dataclasses import dataclass

from kernel.population.households.household_status import HouseholdStatus


@dataclass(frozen=True, slots=True)
class HouseholdSnapshot:

    household_id: str
    status: HouseholdStatus
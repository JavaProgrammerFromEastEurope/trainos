from dataclasses import dataclass


from .household_status 	import HouseholdStatus
from .household_type 		import HouseholdType


@dataclass(frozen=True, slots=True)
class Household:

    household_id: str
    name: 				str
    household_type: HouseholdType
    status: HouseholdStatus
    residents: tuple[str, ...]
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class HouseholdPolicy:

    allow_membership_change: 	bool = True
    allow_shared_consumption: bool = True
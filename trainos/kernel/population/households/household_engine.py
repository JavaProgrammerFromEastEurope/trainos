from .household import Household
from .household_status import HouseholdStatus


class HouseholdEngine:

    def activate(
        self,
        household: Household,
    ) -> Household:
        return Household(
            household_id=household.household_id,
            name=household.name,
            household_type=household.household_type,
            status=HouseholdStatus.ACTIVE,
            residents=household.residents,
        )

    def deactivate(
        self,
        household: Household,
    ) -> Household:
        return Household(
            household_id=household.household_id,
            name=household.name,
            household_type=household.household_type,
            status=HouseholdStatus.INACTIVE,
            residents=household.residents,
        )
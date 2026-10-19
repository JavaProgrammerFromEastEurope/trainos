from kernel.population.households.household import Household
from kernel.population.households.household_engine import HouseholdEngine
from kernel.population.households.household_status import HouseholdStatus
from kernel.population.households.household_type import HouseholdType


def test_household_engine():

    engine = HouseholdEngine()

    household = Household(
        household_id="H1",
        name="Family",
        household_type=HouseholdType.FAMILY,
        status=HouseholdStatus.INACTIVE,
        residents=("R1", "R2"),
    )

    active = engine.activate(household)
    assert active.status == HouseholdStatus.ACTIVE

    inactive = engine.deactivate(active)
    assert inactive.status == HouseholdStatus.INACTIVE
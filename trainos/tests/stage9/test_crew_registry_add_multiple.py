from trainos.kernel.communication.resource_ecology.population.crew_member import (
    CrewMember,
)
from trainos.kernel.communication.resource_ecology.population.crew_registry import (
    CrewRegistry,
)


def test_crew_registry_add_multiple():

    registry = CrewRegistry()
    member_1 = CrewMember(name="John")
    member_2 = CrewMember(name="Alice")

    registry.add(member_1)
    registry.add(member_2)

    assert registry.members() == (member_1, member_2)

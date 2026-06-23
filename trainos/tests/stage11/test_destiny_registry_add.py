from trainos.kernel.metacivilization.destiny.destiny import Destiny
from trainos.kernel.metacivilization.destiny.destiny_type import DestinyType
from trainos.kernel.metacivilization.destiny.destiny_registry import DestinyRegistry


def test_destiny_registry_add():

    registry 	= DestinyRegistry()
    destiny 	= Destiny(type=DestinyType.HARMONY)
    registry.add(destiny)

    assert registry.destinies() == (destiny,)
from trainos.kernel.metacivilization.meaning.meaning import Meaning
from trainos.kernel.metacivilization.meaning.meaning_type import MeaningType
from trainos.kernel.metacivilization.meaning.meaning_registry import MeaningRegistry


def test_meaning_registry_add():

    registry = MeaningRegistry()
    meaning = Meaning(type=MeaningType.CONTINUITY)
    registry.add(meaning)

    assert registry.meanings() == (meaning,)
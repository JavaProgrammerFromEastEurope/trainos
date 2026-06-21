from trainos.kernel.civilization.culture.cultural_memory import CulturalMemory
from trainos.kernel.civilization.culture.cultural_record import CulturalRecord


def test_cultural_memory_add_and_read():

    memory = CulturalMemory()

    record = CulturalRecord(
        description="resource crisis survived",
    )

    memory.add(record)

    assert memory.records() == (record,)

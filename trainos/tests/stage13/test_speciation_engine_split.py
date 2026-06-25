from trainos.kernel.evolution.culture.speciation.speciation_engine import SpeciationEngine


def test_speciation_engine_split():

    engine = SpeciationEngine()

    event, species = engine.split(
        origin="core_culture",
        descendant="engineering_culture",
    )

    assert event.origin == "core_culture"
    assert event.descendant == "engineering_culture"

    assert species.name == "engineering_culture"
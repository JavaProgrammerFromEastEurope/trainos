from .cultural_species import CulturalSpecies
from .speciation_event import SpeciationEvent


class SpeciationEngine:

    def split(
        self, origin: str, descendant: str
    ) -> tuple[SpeciationEvent, CulturalSpecies]:
        event = SpeciationEvent(
            origin=origin,
            descendant=descendant,
        )
        species = CulturalSpecies(
            name=descendant,
        )
        return event, species

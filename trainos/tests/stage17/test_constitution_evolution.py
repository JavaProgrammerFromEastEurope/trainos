from kernel.constitution.evolution.constitutional_evolution import (
    ConstitutionalEvolution,
)
from kernel.constitution.evolution.evolution_type import EvolutionType


def test_constitution_evolution():

    evolution = ConstitutionalEvolution(
        article="Emergency communication",
        evolution=EvolutionType.REFINEMENT,
        description="Technology update",
    )

    assert evolution.evolution == EvolutionType.REFINEMENT

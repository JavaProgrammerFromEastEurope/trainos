from dataclasses import dataclass

from kernel.population.runtime.population_lifecycle import PopulationLifecycle


@dataclass(frozen=True, slots=True)
class PopulationRuntimeSnapshot:
  
    lifecycle: PopulationLifecycle
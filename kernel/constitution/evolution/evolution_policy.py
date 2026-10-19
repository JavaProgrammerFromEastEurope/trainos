from dataclasses import dataclass


@dataclass(frozen=True)
class EvolutionPolicy:

    preserve_identity: 	bool
    require_validation: bool
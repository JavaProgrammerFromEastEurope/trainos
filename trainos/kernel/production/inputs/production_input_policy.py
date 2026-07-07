from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ProductionInputPolicy:

    require_all_inputs: bool = True
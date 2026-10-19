from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ProductionInputResult:

    approved: bool
    missing_resources: tuple[str, ...]
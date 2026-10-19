from dataclasses import dataclass


@dataclass(frozen=True)
class LegitimacyPolicy:

    require_validation: bool
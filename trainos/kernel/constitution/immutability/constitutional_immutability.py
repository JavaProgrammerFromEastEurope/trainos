from dataclasses import dataclass

from .immutability_type import ImmutabilityType


@dataclass(frozen=True)
class ConstitutionalImmutability:

    rule_name: str
    type: ImmutabilityType
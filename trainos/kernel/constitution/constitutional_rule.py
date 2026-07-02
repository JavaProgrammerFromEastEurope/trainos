from dataclasses import dataclass

from .rule_type import RuleType


@dataclass(frozen=True)
class ConstitutionalRule:

    name: str
    description: str
    type: RuleType
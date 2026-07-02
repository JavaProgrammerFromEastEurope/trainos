from dataclasses import dataclass

from .domain_type import DomainType


@dataclass(frozen=True)
class ConstitutionalDomain:

    rule_name: str
    domain: DomainType
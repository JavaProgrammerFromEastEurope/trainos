from dataclasses import dataclass


@dataclass(frozen=True)
class DomainPolicy:

    enforce_domain_matching: bool
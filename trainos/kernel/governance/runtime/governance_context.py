from dataclasses import dataclass

from .governance_configuration import GovernanceConfiguration


@dataclass(slots=True)
class GovernanceContext:

    configuration: GovernanceConfiguration
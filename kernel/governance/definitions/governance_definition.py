from dataclasses import dataclass

from .governance_category import GovernanceCategory
from .governance_type import GovernanceType


@dataclass(frozen=True, slots=True)
class GovernanceDefinition:

    governance_id: 	str
    name: 					str
    governance_type: GovernanceType
    category: GovernanceCategory
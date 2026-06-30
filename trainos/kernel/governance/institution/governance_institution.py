from dataclasses import dataclass

from trainos.kernel.governance.authority import GovernanceAuthority
from .institution_type import InstitutionType


@dataclass(frozen=True)
class GovernanceInstitution:

    name: str
    description: str
    type: InstitutionType
    authority: GovernanceAuthority
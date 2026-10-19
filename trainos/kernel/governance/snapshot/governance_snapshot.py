from dataclasses import dataclass

from .authority_snapshot import AuthoritySnapshot
from .decision_snapshot import DecisionSnapshot
from .governance_office_snapshot import GovernanceOfficeSnapshot
from .governance_runtime_snapshot import GovernanceRuntimeSnapshot
from .policy_snapshot import PolicySnapshot


@dataclass(frozen=True, slots=True)
class GovernanceSnapshot:

    snapshot_id: str
    runtime: GovernanceRuntimeSnapshot
    authorities: 	tuple[AuthoritySnapshot, ...]
    decisions: 		tuple[DecisionSnapshot, ...]
    policies: 		tuple[PolicySnapshot, ...]
    offices: 			tuple[GovernanceOfficeSnapshot, ...]
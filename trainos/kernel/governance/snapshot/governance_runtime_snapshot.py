from dataclasses import dataclass

from kernel.governance.runtime.governance_lifecycle import GovernanceLifecycle


@dataclass(frozen=True, slots=True)
class GovernanceRuntimeSnapshot:

    lifecycle: GovernanceLifecycle

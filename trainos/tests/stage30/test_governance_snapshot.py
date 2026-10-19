from kernel.governance.authorities.authority_status import AuthorityStatus
from kernel.governance.decisions.decision_status import DecisionStatus
from kernel.governance.offices.governance_office_status import GovernanceOfficeStatus
from kernel.governance.policies.policy_status import PolicyStatus
from kernel.governance.runtime.governance_lifecycle import GovernanceLifecycle
from kernel.governance.snapshot.authority_snapshot import AuthoritySnapshot
from kernel.governance.snapshot.decision_snapshot import DecisionSnapshot
from kernel.governance.snapshot.governance_office_snapshot import (
    GovernanceOfficeSnapshot,
)
from kernel.governance.snapshot.governance_runtime_snapshot import (
    GovernanceRuntimeSnapshot,
)
from kernel.governance.snapshot.governance_snapshot import GovernanceSnapshot
from kernel.governance.snapshot.governance_snapshot_engine import (
    GovernanceSnapshotEngine,
)
from kernel.governance.snapshot.policy_snapshot import PolicySnapshot


def test_governance_snapshot():

    engine = GovernanceSnapshotEngine()
    snapshot = GovernanceSnapshot(
        snapshot_id="GS1",
        runtime=GovernanceRuntimeSnapshot(
            lifecycle=GovernanceLifecycle.RUNNING,
        ),
        authorities=(
            AuthoritySnapshot(
                authority_id="A1",
                status=AuthorityStatus.ACTIVE,
            ),
        ),
        decisions=(
            DecisionSnapshot(
                decision_id="D1",
                status=DecisionStatus.EXECUTED,
            ),
        ),
        policies=(
            PolicySnapshot(
                policy_id="P1",
                status=PolicyStatus.ACTIVE,
            ),
        ),
        offices=(
            GovernanceOfficeSnapshot(
                office_id="O1",
                status=GovernanceOfficeStatus.OPERATIONAL,
            ),
        ),
    )
    result = engine.capture(snapshot)
    assert result is snapshot

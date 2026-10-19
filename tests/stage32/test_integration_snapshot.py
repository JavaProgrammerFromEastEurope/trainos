from kernel.integration.snapshot.integration_snapshot import IntegrationSnapshot

from kernel.integration.snapshot.integration_snapshot_engine import (
    IntegrationSnapshotEngine,
)

from kernel.integration.snapshot.runtime_snapshot import IntegrationRuntimeSnapshot
from kernel.integration.snapshot.message_bus_snapshot import MessageBusSnapshot
from kernel.integration.snapshot.routing_snapshot import RoutingSnapshot
from kernel.integration.snapshot.handler_snapshot import HandlerSnapshot
from kernel.integration.runtime.runtime_status import IntegrationRuntimeStatus


def test_integration_snapshot():

    snapshot = IntegrationSnapshot(
        snapshot_id="SNAP1",
        runtime=IntegrationRuntimeSnapshot(
            runtime_id="RT1",
            status=IntegrationRuntimeStatus.RUNNING,
        ),
        message_bus=MessageBusSnapshot(
            bus_id="BUS1",
            queued_messages=10,
        ),
        routing=RoutingSnapshot(
            routes=5,
        ),
        handlers=HandlerSnapshot(
            handlers=7,
        ),
    )
    result = IntegrationSnapshotEngine().capture(snapshot)
    assert result is snapshot

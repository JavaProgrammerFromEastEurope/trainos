from dataclasses import dataclass

from .handler_snapshot import HandlerSnapshot
from .message_bus_snapshot import MessageBusSnapshot
from .routing_snapshot import RoutingSnapshot
from .runtime_snapshot import IntegrationRuntimeSnapshot


@dataclass(frozen=True, slots=True)
class IntegrationSnapshot:

    snapshot_id: 	str
    runtime: 			IntegrationRuntimeSnapshot
    message_bus: 	MessageBusSnapshot
    routing: 			RoutingSnapshot
    handlers: 		HandlerSnapshot
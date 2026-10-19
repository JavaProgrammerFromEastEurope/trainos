from dataclasses import dataclass
from ..message_bus.message_bus import MessageBus


@dataclass(slots=True)
class IntegrationRuntimeContext:

    message_bus: MessageBus

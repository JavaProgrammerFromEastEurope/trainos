from dataclasses import dataclass

from .handler_status import HandlerStatus


@dataclass(frozen=True, slots=True)
class CommandHandler:

    handler_id: str
    name: str
    status: HandlerStatus = HandlerStatus.IDLE

from dataclasses import dataclass

from .handler_type import HandlerType


@dataclass(frozen=True, slots=True)
class IntegrationHandler:

    handler_id: 		str
    handler_type: 	HandlerType
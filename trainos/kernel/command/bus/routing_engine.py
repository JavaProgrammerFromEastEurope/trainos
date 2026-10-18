from __future__ import annotations

from .routing_result import RoutingResult
from ..handler.command_handler import CommandHandler


class RoutingEngine:
    """Resolves a selected handler into a routing result."""

    def route(self, handler: CommandHandler) -> RoutingResult:
        if not handler.handler_id:
            raise ValueError("handler.handler_id must not be empty")
        return RoutingResult(success=True, handler_id=handler.handler_id)

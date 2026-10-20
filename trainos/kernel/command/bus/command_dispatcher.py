from __future__ import annotations

from ..command.command import Command
from ..handler.handler_engine import HandlerEngine
from ..handler.handler_registry import HandlerRegistry
from .command_dispatch_result import CommandDispatchResult
from .routing_engine import RoutingEngine


class CommandDispatcher:
    """Route a command through the registry and execute its selected handler.

    This is a software-level dispatch pipeline. It does not authorize direct
    control of safety-critical train equipment; such actions need independent
    interlocks and a separately validated control system.
    """

    def __init__(
        self,
        registry: HandlerRegistry,
        routing_engine: RoutingEngine | None = None,
        handler_engine: HandlerEngine | None = None,
    ) -> None:
        if not isinstance(registry, HandlerRegistry):
            raise TypeError("registry must be a HandlerRegistry")
        if routing_engine is not None and not isinstance(routing_engine, RoutingEngine):
            raise TypeError("routing_engine must be a RoutingEngine or None")
        if handler_engine is not None and not isinstance(handler_engine, HandlerEngine):
            raise TypeError("handler_engine must be a HandlerEngine or None")
        self._registry = registry
        self._routing_engine = routing_engine or RoutingEngine()
        self._handler_engine = handler_engine or HandlerEngine()

    def dispatch(self, command: Command) -> CommandDispatchResult:
        if not isinstance(command, Command):
            raise TypeError("command must be a Command")

        routing = self._routing_engine.route_command(command, self._registry)
        if not routing.success:
            return CommandDispatchResult(
                success=False,
                command_id=command.command_id,
                handler_id=routing.handler_id or None,
                error=routing.error or "Command routing failed without a diagnostic",
                phase="routing",
            )

        # Resolve by the exact ID selected by the router; never re-select by name.
        handler = self._registry.get(routing.handler_id)
        result = self._handler_engine.execute(handler, command)
        if not result.success:
            return CommandDispatchResult(
                success=False,
                command_id=command.command_id,
                handler_id=handler.handler_id,
                error=result.error or "Handler execution failed without a diagnostic",
                phase="execution",
            )

        return CommandDispatchResult(
            success=True,
            command_id=command.command_id,
            handler_id=handler.handler_id,
            output=result.output,
            phase="completed",
        )

from __future__ import annotations

from ..command.command import Command
from ..handler.command_handler import CommandHandler
from ..handler.handler_registry import HandlerRegistry
from .routing_result import RoutingResult


class RoutingEngine:
    """Resolve commands to executable handlers registered in the handler registry.

    ``route(handler)`` remains available for callers that already selected a
    handler. New code should use ``route_command(command, registry)`` so the
    selection decision is performed and can be diagnosed here.
    """

    def route(self, target: CommandHandler | Command, registry: HandlerRegistry | None = None) -> RoutingResult:
        if isinstance(target, CommandHandler):
            return self._route_selected_handler(target)
        if isinstance(target, Command):
            if registry is None:
                raise ValueError("registry is required when routing a Command")
            return self.route_command(target, registry)
        raise TypeError("target must be a CommandHandler or Command")

    def route_command(self, command: Command, registry: HandlerRegistry) -> RoutingResult:
        """Select a unique executable handler whose name matches command.name.

        The current Command model has no explicit handler key, so exact name
        matching is the only existing routing contract. Ambiguous matches fail
        closed instead of choosing an arbitrary handler.
        """
        if not isinstance(command, Command):
            raise TypeError("command must be a Command")
        if not isinstance(registry, HandlerRegistry):
            raise TypeError("registry must be a HandlerRegistry")

        candidates = [handler for handler in registry.all() if handler.name == command.name]
        if not candidates:
            return RoutingResult(
                success=False,
                handler_id="",
                command_id=command.command_id,
                error=f"No handler registered for command '{command.name}'",
            )
        if len(candidates) > 1:
            return RoutingResult(
                success=False,
                handler_id="",
                command_id=command.command_id,
                error=f"Multiple handlers registered for command '{command.name}'",
            )
        return self._route_selected_handler(candidates[0], command.command_id)

    @staticmethod
    def _route_selected_handler(
        handler: CommandHandler,
        command_id: str | None = None,
    ) -> RoutingResult:
        if not isinstance(handler, CommandHandler):
            raise TypeError("handler must be a CommandHandler")
        if not handler.handler_id.strip():
            raise ValueError("handler.handler_id must not be empty")
        if handler.executor is None:
            return RoutingResult(
                success=False,
                handler_id=handler.handler_id,
                command_id=command_id,
                error=f"Handler '{handler.handler_id}' has no executor",
            )
        return RoutingResult(
            success=True,
            handler_id=handler.handler_id,
            command_id=command_id,
        )

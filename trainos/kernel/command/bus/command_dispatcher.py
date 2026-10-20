from __future__ import annotations

from uuid import uuid4

from ..command.command import Command
from ..execution.command_execution import CommandExecution
from ..execution.execution_engine import ExecutionEngine
from ..execution.execution_progress import ExecutionProgress
from ..execution.execution_registry import ExecutionRegistry
from ..execution.execution_status import ExecutionStatus
from ..events import CommandEventService
from ..handler.handler_engine import HandlerEngine
from ..handler.handler_registry import HandlerRegistry
from .command_dispatch_result import CommandDispatchResult
from .routing_engine import RoutingEngine


class CommandDispatcher:
    """Route, execute, and record a command's software-level lifecycle.

    This does not authorize direct control of safety-critical train equipment.
    """

    def __init__(
        self,
        registry: HandlerRegistry,
        routing_engine: RoutingEngine | None = None,
        handler_engine: HandlerEngine | None = None,
        execution_engine: ExecutionEngine | None = None,
        execution_registry: ExecutionRegistry | None = None,
        event_service: CommandEventService | None = None,
    ) -> None:
        if not isinstance(registry, HandlerRegistry):
            raise TypeError("registry must be a HandlerRegistry")
        if routing_engine is not None and not isinstance(routing_engine, RoutingEngine):
            raise TypeError("routing_engine must be a RoutingEngine or None")
        if handler_engine is not None and not isinstance(handler_engine, HandlerEngine):
            raise TypeError("handler_engine must be a HandlerEngine or None")
        if execution_engine is not None and not isinstance(execution_engine, ExecutionEngine):
            raise TypeError("execution_engine must be an ExecutionEngine or None")
        if execution_registry is not None and not isinstance(execution_registry, ExecutionRegistry):
            raise TypeError("execution_registry must be an ExecutionRegistry or None")
        if event_service is not None and not isinstance(event_service, CommandEventService):
            raise TypeError("event_service must be a CommandEventService or None")
        if execution_engine is not None and event_service is not None:
            raise ValueError("provide execution_engine or event_service, not both")
        self._registry = registry
        self._routing_engine = routing_engine or RoutingEngine()
        self._handler_engine = handler_engine or HandlerEngine()
        self._execution_engine = execution_engine or ExecutionEngine(event_service)
        self._execution_registry = execution_registry or ExecutionRegistry()

    @property
    def execution_registry(self) -> ExecutionRegistry:
        return self._execution_registry

    def dispatch(self, command: Command) -> CommandDispatchResult:
        if not isinstance(command, Command):
            raise TypeError("command must be a Command")

        execution = CommandExecution(
            execution_id=str(uuid4()),
            command_id=command.command_id,
            progress=ExecutionProgress(attempts=0, max_attempts=1, completed=False),
        )
        execution = self._execution_engine.create(execution, command.name)
        self._save_execution(execution)
        execution = self._execution_engine.start(execution)
        self._save_execution(execution)

        routing = self._routing_engine.route_command(command, self._registry)
        if not routing.success:
            error = routing.error or "Command routing failed without a diagnostic"
            failed = self._execution_engine.fail(execution, error)
            self._save_execution(failed)
            return self._failure(command, routing.handler_id or None, error, "routing", failed)

        handler = self._registry.get(routing.handler_id)
        result = self._handler_engine.execute(handler, command)
        if not result.success:
            error = result.error or "Handler execution failed without a diagnostic"
            failed = self._execution_engine.fail(execution, error)
            self._save_execution(failed)
            return self._failure(command, handler.handler_id, error, "execution", failed)

        completed = self._execution_engine.complete(execution)
        self._save_execution(completed)
        return CommandDispatchResult(
            success=True,
            command_id=command.command_id,
            handler_id=handler.handler_id,
            output=result.output,
            phase="completed",
            execution_id=completed.execution_id,
            execution_status=ExecutionStatus.COMPLETED,
        )


    def _save_execution(self, execution: CommandExecution) -> None:
        if self._execution_registry.exists(execution.execution_id):
            self._execution_registry.delete(execution.execution_id)
        self._execution_registry.register(execution.execution_id, execution)

    @staticmethod
    def _failure(
        command: Command,
        handler_id: str | None,
        error: str,
        phase: str,
        execution: CommandExecution,
    ) -> CommandDispatchResult:
        return CommandDispatchResult(
            success=False,
            command_id=command.command_id,
            handler_id=handler_id,
            error=error,
            phase=phase,
            execution_id=execution.execution_id,
            execution_status=execution.status,
        )

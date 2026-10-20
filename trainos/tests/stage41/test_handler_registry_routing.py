import pytest

from kernel.command.bus.routing_engine import RoutingEngine
from kernel.command.command.command import Command
from kernel.command.command.command_priority import CommandPriority
from kernel.command.handler.command_handler import CommandHandler
from kernel.command.handler.handler_registry import HandlerRegistry


def make_command(name="inspect"):
    return Command("cmd-1", name, CommandPriority.NORMAL)


def test_routes_command_to_unique_registered_executable_handler():
    registry = HandlerRegistry()
    handler = CommandHandler("handler-1", "inspect", executor=lambda command: command.name)
    registry.register(handler.handler_id, handler)

    result = RoutingEngine().route_command(make_command(), registry)

    assert result.success is True
    assert result.handler_id == handler.handler_id
    assert result.command_id == "cmd-1"
    assert result.error is None


def test_route_accepts_command_and_registry_for_convenient_api():
    registry = HandlerRegistry()
    handler = CommandHandler("handler-1", "inspect", executor=lambda command: None)
    registry.register(handler.handler_id, handler)

    result = RoutingEngine().route(make_command(), registry)

    assert result.success is True
    assert result.handler_id == "handler-1"


def test_missing_handler_returns_diagnostic_failure():
    result = RoutingEngine().route_command(make_command(), HandlerRegistry())

    assert result.success is False
    assert result.handler_id == ""
    assert result.command_id == "cmd-1"
    assert "No handler registered" in result.error


def test_ambiguous_handler_names_fail_closed():
    registry = HandlerRegistry()
    registry.register("h1", CommandHandler("h1", "inspect", executor=lambda command: 1))
    registry.register("h2", CommandHandler("h2", "inspect", executor=lambda command: 2))

    result = RoutingEngine().route_command(make_command(), registry)

    assert result.success is False
    assert "Multiple handlers" in result.error


def test_metadata_only_handler_is_not_routable_for_execution():
    registry = HandlerRegistry()
    registry.register("h1", CommandHandler("h1", "inspect"))

    result = RoutingEngine().route_command(make_command(), registry)

    assert result.success is False
    assert result.handler_id == "h1"
    assert "no executor" in result.error


def test_invalid_inputs_are_rejected():
    engine = RoutingEngine()
    with pytest.raises(TypeError):
        engine.route_command("not a command", HandlerRegistry())
    with pytest.raises(TypeError):
        engine.route_command(make_command(), object())
    with pytest.raises(ValueError):
        engine.route(make_command())

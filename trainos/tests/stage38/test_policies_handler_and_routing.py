import pytest
from kernel.command.command.command import Command
from kernel.command.command.command_priority import CommandPriority
from kernel.command.handler.command_handler import CommandHandler
from kernel.command.handler.handler_engine import HandlerEngine
from kernel.command.handler.handler_result import HandlerResult
from kernel.command.bus.routing_engine import RoutingEngine
from kernel.command.policies.command_policy import CommandPolicy
from kernel.command.policies.policy_engine import PolicyEngine
from kernel.command.policies.policy_type import PolicyType
from kernel.command.policies.retry_policy import RetryPolicy


def test_retry_policy_validation_and_policy_engine_decisions():
    engine = PolicyEngine()
    retry = CommandPolicy("p1", PolicyType.RETRY, RetryPolicy(3, 2))
    confirm = CommandPolicy("p2", PolicyType.REQUIRE_CONFIRMATION)
    fail_fast = CommandPolicy("p3", PolicyType.FAIL_FAST)
    assert engine.should_retry(retry) is True
    assert engine.should_retry(confirm) is False
    assert engine.requires_confirmation(confirm) is True
    assert engine.requires_confirmation(fail_fast) is False
    for args in [(0, 0), (1, -1)]:
        with pytest.raises(ValueError):
            RetryPolicy(*args)


def test_handler_and_routing_results_refer_to_selected_command_and_handler():
    command = Command("cmd", "index", CommandPriority.NORMAL)
    handler = CommandHandler("handler-1", "indexer")
    result = HandlerEngine().execute(handler, command)
    route = RoutingEngine().route(handler)
    assert isinstance(result, HandlerResult)
    assert result.success is True and result.command_id == command.command_id
    assert route.success is True and route.handler_id == handler.handler_id
    with pytest.raises(ValueError):
        RoutingEngine().route(CommandHandler("", "bad"))

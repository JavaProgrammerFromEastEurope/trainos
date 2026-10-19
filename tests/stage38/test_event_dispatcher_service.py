from kernel.command.events.command_event import CommandEvent
from kernel.command.events.event_dispatcher import EventDispatcher
from kernel.command.events.event_registry import EventRegistry
from kernel.command.events.event_service import CommandEventService
from kernel.command.events.event_type import CommandEventType


def test_dispatcher_subscription_filtering_deduplication_and_service_publication():
    dispatcher = EventDispatcher()
    registry = EventRegistry()
    service = CommandEventService(registry=registry, dispatcher=dispatcher)
    received = []
    handler = received.append
    dispatcher.subscribe(CommandEventType.COMMAND_CREATED, handler)
    dispatcher.subscribe(CommandEventType.COMMAND_CREATED, handler)
    started = service.publish("cmd-1", CommandEventType.COMMAND_STARTED)
    created = service.publish(
        "cmd-1", CommandEventType.COMMAND_CREATED, {"type": "demo"}
    )
    assert received == [created]
    assert registry.get_events("cmd-1") == (started, created)
    dispatcher.unsubscribe(CommandEventType.COMMAND_CREATED, handler)
    later = service.publish("cmd-2", CommandEventType.COMMAND_CREATED)
    assert later not in received
    assert service.registry is registry and service.dispatcher is dispatcher


def test_dispatcher_uses_stable_handler_snapshot_when_subscriptions_change():
    dispatcher = EventDispatcher()
    seen = []

    def second(event):
        seen.append("second")

    def first(event):
        seen.append("first")
        dispatcher.unsubscribe(CommandEventType.COMMAND_COMPLETED, second)

    dispatcher.subscribe(CommandEventType.COMMAND_COMPLETED, first)
    dispatcher.subscribe(CommandEventType.COMMAND_COMPLETED, second)
    dispatcher.dispatch(CommandEvent.create("cmd", CommandEventType.COMMAND_COMPLETED))
    assert seen == ["first", "second"]

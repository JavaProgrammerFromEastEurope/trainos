from kernel.events.subscriber.subscriber_engine import SubscriberEngine

from .dispatch_result import DispatchResult


class BusEngine:

    def __init__(self):
        self.subscribers = SubscriberEngine()

    def dispatch(
        self,
        bus,
        event,
    ) -> DispatchResult:
        delivered = 0
        for subscriber in bus.subscribers:
            if self.subscribers.accepts(
                subscriber,
                event,
            ):
                delivered += 1
        return DispatchResult(delivered=delivered)

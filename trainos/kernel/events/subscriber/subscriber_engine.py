from ..event import Event


class SubscriberEngine:

    def accepts(
        self,
        subscriber,
        event: Event,
    ) -> bool:
        return subscriber.subscription.event_name == event.name

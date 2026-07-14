class Router:

    def matches(
        self,
        subscriber,
        event,
    ) -> bool:
        return subscriber.subscription.event_name == event.name

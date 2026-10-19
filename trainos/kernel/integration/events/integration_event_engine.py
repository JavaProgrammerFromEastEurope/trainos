from .integration_event import IntegrationEvent
from .integration_event_status import IntegrationEventStatus


class IntegrationEventEngine:

    def publish(
        self,
        event: IntegrationEvent,
    ) -> IntegrationEvent:
        return IntegrationEvent(
            event_id=event.event_id,
            event_type=event.event_type,
            contract=event.contract,
            status=IntegrationEventStatus.PUBLISHED,
        )

    def process(
        self,
        event: IntegrationEvent,
    ) -> IntegrationEvent:
        return IntegrationEvent(
            event_id=event.event_id,
            event_type=event.event_type,
            contract=event.contract,
            status=IntegrationEventStatus.PROCESSED,
        )

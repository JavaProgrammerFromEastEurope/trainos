from kernel.integration.events.integration_event import IntegrationEvent

from .handler_result import HandlerResult


class HandlerEngine:

    def handle(
        self,
        event: IntegrationEvent,
    ) -> HandlerResult:
        return HandlerResult(
            success=True,
            message=f"Handled {event.event_id}",
        )

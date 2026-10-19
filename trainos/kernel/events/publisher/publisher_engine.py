from .publish_result import PublishResult
from ..event import Event


class PublisherEngine:

    def publish(
        self,
        publisher,
        event: Event,
    ) -> PublishResult:

        return PublishResult(
            success=True,
            event_id=event.event_id,
        )

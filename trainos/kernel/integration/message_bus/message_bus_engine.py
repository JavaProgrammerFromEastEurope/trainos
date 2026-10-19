from .message import Message
from .message_queue import MessageQueue
from .message_status import MessageStatus


class MessageBusEngine:

    def __init__(self):
        self.queue = MessageQueue(messages=[])

    def publish(
        self,
        message: Message,
    ) -> None:
        queued = Message(
            message_id=message.message_id,
            event=message.event,
            status=MessageStatus.QUEUED,
        )
        self.queue.add(queued)

    def deliver(self) -> Message | None:
        message = self.queue.pop()
        if message is None:
            return None
        return Message(
            message_id=message.message_id,
            event=message.event,
            status=MessageStatus.DELIVERED,
        )

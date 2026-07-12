from dataclasses import dataclass

from .message import Message


@dataclass(slots=True)
class MessageQueue:
    messages: list[Message]

    def add(
        self,
        message: Message,
    ) -> None:
        self.messages.append(message)

    def pop(self) -> Message | None:
        if not self.messages:
            return None
        return self.messages.pop(0)

from __future__ import annotations

from .message import Message


class MessageBus:

    def __init__(self) -> None:
        self._messages: list[Message] = []

    def send(self, message: Message) -> None:
        self._messages.append(message)

    def inbox(self) -> tuple[Message, ...]:
        return tuple(self._messages)
